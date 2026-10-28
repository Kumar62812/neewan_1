#!/usr/bin/env python3
"""Read-only structural and integrity checks for the P01 package.

The versioned JSON manifest is the single source of baseline artifact fingerprints.
This validator never edits evidence and never launches formal tools.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = next(
    (p for p in HERE.parents
     if (p / "02_CERTIFICATION" / "P01_FORMAL_RESULTS.md").is_file()
     and (p / "re" / "p01-20260930T220622Z-rev1.tar.gz").is_file()),
    None,
)
if REPO_ROOT is None:
    print("ERROR: could not locate repository root and accepted archive.", file=sys.stderr)
    print("Run this script from a complete repository checkout.", file=sys.stderr)
    sys.exit(2)

P01 = REPO_ROOT / "Files/Research_Papers/benchmark/pilot_v0_1/P01"
MANIFEST_PATH = P01 / "p01_package_manifest_v1.json"
# This pin prevents a modified manifest from silently redefining its own baseline.
EXPECTED_MANIFEST_GIT_BLOB = "bd3329ea1af786eeedafb556c4a8ea7cb404bfcc"

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()

if not MANIFEST_PATH.is_file():
    print("ERROR: versioned P01 package manifest is missing.", file=sys.stderr)
    sys.exit(2)
try:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    print("ERROR: cannot read valid P01 package manifest: %s" % exc, file=sys.stderr)
    sys.exit(2)

artifacts = manifest.get("artifacts")
archive_record = manifest.get("accepted_formal_evidence")
if (manifest.get("manifest_id") != "FORMAL-AMBIG-RTL-P01-PACKAGE-MANIFEST"
        or manifest.get("manifest_version") != "1.0"
        or not isinstance(artifacts, list)
        or not artifacts
        or not isinstance(archive_record, dict)
        or not archive_record.get("archive_path")
        or not archive_record.get("archive_sha256")):
    print("ERROR: P01 package manifest has an invalid schema or missing required values.", file=sys.stderr)
    sys.exit(2)

checks = []
def record(name: str, ok: bool, detail: str) -> None:
    checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})

actual_manifest_blob = git_blob_sha(MANIFEST_PATH)
record("manifest-git-blob-sha1",
       actual_manifest_blob == EXPECTED_MANIFEST_GIT_BLOB,
       "versioned manifest matches its pinned Git blob" if actual_manifest_blob == EXPECTED_MANIFEST_GIT_BLOB
       else "expected manifest Git blob %s; found %s" % (EXPECTED_MANIFEST_GIT_BLOB, actual_manifest_blob))
record("manifest-status-boundary",
       manifest.get("status") == "BASELINE_REFERENCE_NOT_A_FREEZE_OR_CERTIFICATION",
       "manifest explicitly does not authorize freeze or certification")

expected_git_blobs = {}
valid_artifacts = True
for item in artifacts:
    if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not isinstance(item.get("git_blob_sha1"), str):
        valid_artifacts = False
        continue
    if item["path"] in expected_git_blobs:
        valid_artifacts = False
    expected_git_blobs[item["path"]] = item["git_blob_sha1"]
record("manifest-artifact-schema",
       valid_artifacts and len(expected_git_blobs) == len(artifacts),
       "%d unique package source entries" % len(expected_git_blobs))

for rel, expected in expected_git_blobs.items():
    path = P01 / rel
    if not path.is_file():
        record("source:" + rel, False, "required file missing")
        continue
    actual = git_blob_sha(path)
    record("source:" + rel, actual == expected,
           "manifest Git blob ID match" if actual == expected
           else "expected Git blob %s; found %s" % (expected, actual))

record("required-file-inventory",
       valid_artifacts and all((P01 / rel).is_file() for rel in expected_git_blobs),
       "%d/%d manifest-listed files present" %
       (sum((P01 / rel).is_file() for rel in expected_git_blobs), len(expected_git_blobs)))

def read(rel: str) -> str:
    path = P01 / rel
    return path.read_text(encoding="utf-8") if path.is_file() else ""

requirement = read("requirement.md")
interpretation = read("interpretations/interpretation_01.md")
specification = read("behavioral_specification/specification_01.md")
reference = read("reference_rtl/rtl_01.sv")
wrong = read("validation_rtl/deliberately_wrong_rtl.sv")
properties = read("formal/properties/mux2to1_properties.sv")
ref_harness = read("formal/harness_reference.sv")
wrong_harness = read("formal/harness_wrong.sv")
ref_sby = read("formal/reference.sby")
wrong_sby = read("formal/wrong.sby")

normalized_requirement = requirement.replace("`", "").lower()
normalized_interpretation = interpretation.replace("`", "").lower()
normalized_specification = specification.replace("`", "").lower()
record("contract:requirement",
       all(x in normalized_requirement for x in ["sel", "y shall equal a", "y shall equal b", "combinational"]),
       "requirement states both select cases and combinational scope")
record("contract:interpretation",
       all(x in normalized_interpretation for x in ["sel", "y equals a", "y equals b", "purely combinational"]),
       "interpretation documents both select cases and combinational scope")
record("contract:specification",
       ("y = a, if sel = 0" in normalized_specification
        and "y = b, if sel = 1" in normalized_specification
        and "don't care" in normalized_specification),
       "behavioral specification defines both select cases and Boolean don't-care notation")
record("reference-rtl-selects-correct-input",
       "y = a;" in reference and "y = b;" in reference and "sel == 1'b0" in reference,
       "reference RTL expresses sel=0 -> a and sel=1 -> b")
record("negative-control-swaps-inputs",
       "y = b;" in wrong and "y = a;" in wrong and "sel == 1'b0" in wrong,
       "negative control intentionally reverses selection")
record("shared-property",
       "module mux2to1_properties" in properties and "assert (y == (sel ? b : a));" in properties,
       "shared assertion encodes required mux behavior")
record("same-property-instantiated",
       "mux2to1_properties props" in ref_harness and "mux2to1_properties props" in wrong_harness,
       "both harnesses instantiate the same property module")
record("reference-config-expects-pass",
       "expect pass" in ref_sby.lower() and "smtbmc z3" in ref_sby.lower(),
       "reference configuration expects PASS with smtbmc z3")
record("negative-config-expects-fail",
       "expect fail" in wrong_sby.lower() and "smtbmc z3" in wrong_sby.lower(),
       "negative configuration expects FAIL with smtbmc z3")

archive_path_value = archive_record["archive_path"]
archive_path = REPO_ROOT / archive_path_value
if not archive_path.is_file():
    record("accepted-archive-sha256", False, "manifest-listed accepted archive is missing")
else:
    archive_digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    expected_archive_digest = archive_record["archive_sha256"]
    record("accepted-archive-sha256", archive_digest == expected_archive_digest,
           "archive checksum matches the manifest" if archive_digest == expected_archive_digest
           else "expected %s; found %s" % (expected_archive_digest, archive_digest))

failures = [item for item in checks if item["status"] == "FAIL"]
report = {
    "validator": "P01 read-only package validator",
    "validator_version": "1.1",
    "manifest_id": manifest["manifest_id"],
    "manifest_version": manifest["manifest_version"],
    "manifest_baseline_commit": manifest.get("baseline_snapshot", {}).get("inspected_for_B1"),
    "repository_root": str(REPO_ROOT),
    "case_directory": str(P01),
    "formal_tools_executed": False,
    "human_certification_performed": False,
    "template_freeze_performed": False,
    "check_count": len(checks),
    "passed": len(checks) - len(failures),
    "failed": len(failures),
    "checks": checks,
}
print(json.dumps(report, indent=2))
sys.exit(1 if failures else 0)
