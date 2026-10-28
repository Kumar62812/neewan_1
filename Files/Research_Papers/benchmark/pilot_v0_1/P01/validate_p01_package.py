#!/usr/bin/env python3
"""Read-only structural and integrity checks for the P01 package.

This validator never edits source/evidence files and never launches formal tools.
Run from any directory: python3 validate_p01_package.py
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
ARCHIVE = REPO_ROOT / "re" / "p01-20260930T220622Z-rev1.tar.gz"
EXPECTED_ARCHIVE_SHA256 = "32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b"

# Git blob IDs from B1 baseline; these are not SHA-256 file digests.
EXPECTED_GIT_BLOBS = {
    "requirement.md": "ae8b409b4718ed67c76325f5e4ec0ddac9b297fc",
    "interpretations/interpretation_01.md": "35963b1bfb8b710d3bbf15f1bb570addd164dc77",
    "behavioral_specification/specification_01.md": "6795b105e034915855e808e0637014f7bd10873d",
    "reference_rtl/rtl_01.sv": "e0eae8f83d93680e220b86031e0bb6d22ff00b92",
    "validation_rtl/deliberately_wrong_rtl.sv": "e9ba4a6bb05402437d5d91f28e3da9ed1272cd45",
    "formal/properties/mux2to1_properties.sv": "caf96911983214d80ad828a94c217d37a0bb079d",
    "formal/harness_reference.sv": "dd699240e63b538197ad134500defdb149a2b371",
    "formal/harness_wrong.sv": "1b9a99f19940bc7d131ba9d0e74d4ad7aa219ed1",
    "formal/reference.sby": "141d45a02e4bd36600429b84302b3da0964fcaf4",
    "formal/wrong.sby": "3928adab6713701c8606bfe2c358be088d577302",
    "formal/run_p01_formal.sh": "a9d42b052f400e7de32f07966dddf6f45abb1be8",
    "review/pre_rtl_review.md": "c5a9dae7df498ea918acd72228df33b33f4605a6",
}

checks = []
def record(name: str, ok: bool, detail: str) -> None:
    checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()

for rel, expected in EXPECTED_GIT_BLOBS.items():
    path = P01 / rel
    if not path.is_file():
        record("source:" + rel, False, "required file missing")
        continue
    actual = git_blob_sha(path)
    record("source:" + rel, actual == expected,
           "baseline Git blob ID match" if actual == expected
           else "expected Git blob %s; found %s" % (expected, actual))

required_paths = list(EXPECTED_GIT_BLOBS.keys())
record("required-file-inventory",
       all((P01 / rel).is_file() for rel in required_paths),
       "%d/%d baseline files present" %
       (sum((P01 / rel).is_file() for rel in required_paths), len(required_paths)))

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

record("contract:requirement",
       all(x in requirement for x in ["sel", "y shall equal", "a", "b", "combinational"]),
       "requirement includes inputs, mux output selection and combinational scope")
record("contract:interpretation",
       all(x in interpretation for x in ["sel", "y equals", "a", "b", "purely combinational"]),
       "interpretation documents the same Boolean mux behavior")
record("contract:specification",
       "sel ? b : a" in specification and "don't care" in specification,
       "behavioral specification defines the mux function and Boolean don't-care notation")
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

archive_digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
record("accepted-archive-sha256", archive_digest == EXPECTED_ARCHIVE_SHA256,
       "accepted archive checksum matches" if archive_digest == EXPECTED_ARCHIVE_SHA256
       else "expected %s; found %s" % (EXPECTED_ARCHIVE_SHA256, archive_digest))

failures = [item for item in checks if item["status"] == "FAIL"]
report = {
    "validator": "P01 read-only package validator",
    "validator_version": "1.0",
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
