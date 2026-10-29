#!/usr/bin/env python3
"""Read-only evidence-integrity and source-alignment audit for P02 and P05.

This tool verifies retained SHA256SUMS manifests and compares important current
case sources with the exact source snapshots captured in run-02. It does not run
Yosys, SMTBMC, Z3, or modify evidence.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_MARKER = Path("Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_RESULTS.md")
PILOT_ROOT = Path("Files/Research_Papers/benchmark/pilot_v0_1")

RUN_MANIFESTS = [
    {
        "case": "P02", "run": "run-01",
        "path": "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-01/SHA256SUMS.json",
        "expected_git_blob_sha1": "4168ae6b27220eea975effe04f843770ecb9483e",
    },
    {
        "case": "P02", "run": "run-02",
        "path": "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/SHA256SUMS.json",
        "expected_git_blob_sha1": "e75a996e50f84b17c16f7e5664664e7f9eafd783",
    },
    {
        "case": "P05", "run": "run-01",
        "path": "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-01/SHA256SUMS.json",
        "expected_git_blob_sha1": "29e6a357b072c958cd4ec65eb2ceb52339660900",
    },
    {
        "case": "P05", "run": "run-02",
        "path": "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/SHA256SUMS.json",
        "expected_git_blob_sha1": "d572d9801ba889474f8d8e3999544131928ab6d4",
    },
]

# These are the key inputs/implementation sources to which the run-02 results
# refer. Expected values are Git blob object IDs, not file SHA-256 digests.
SOURCE_PAIRS = [
    ("P02 requirement", "Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_REQUIREMENT.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/P02_REQUIREMENT.md",
     "8f9801e5ef6d9df0654b051d551abd8120e39355"),
    ("P02 interpretation", "Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_INTERPRETATION.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/P02_INTERPRETATION.md",
     "041ddc377c05d6466261c66c4a0388d33381eb91"),
    ("P02 specification", "Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_SPECIFICATION.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/P02_SPECIFICATION.md",
     "637ee132e24de489a661ed9168c7b2496fd75872"),
    ("P02 consistency review", "Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_CONSISTENCY_REVIEW.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/P02_CONSISTENCY_REVIEW.md",
     "4f718891c0afb82e08fed90edd37b256090382a7"),
    ("P02 formal strategy", "Files/Research_Papers/benchmark/pilot_v0_1/P02/formal/STRATEGY.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/formal/STRATEGY.md",
     "25dc893d31579ca07ad0ba5f5e4aeebc264f3f58"),
    ("P02 formal harness", "Files/Research_Papers/benchmark/pilot_v0_1/P02/formal/harness.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/formal/harness.sv",
     "c0ba31913c942b22d7f4e81ac92eb41ebb754077"),
    ("P02 formal properties", "Files/Research_Papers/benchmark/pilot_v0_1/P02/formal/properties/register_properties.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/formal/properties/register_properties.sv",
     "a80db414d1cd7f2a6871c6adcee85d3c87e7581c"),
    ("P02 formal runner", "Files/Research_Papers/benchmark/pilot_v0_1/P02/formal/run.py",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/formal/run.py",
     "201a6a49c9a17d4b94ed4fcab9ccb88b51266113"),
    ("P02 reference RTL", "Files/Research_Papers/benchmark/pilot_v0_1/P02/reference_rtl/register.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/reference_rtl/register.sv",
     "8658ad86d40b93fef579334aae32a1126b8e1f72"),
    ("P02 reset-polarity negative control", "Files/Research_Papers/benchmark/pilot_v0_1/P02/validation_rtl/wrong_reset.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/validation_rtl/wrong_reset.sv",
     "26f27af71e2ac13dbbb6ca708c47c1721c6b16ee"),
    ("P02 asynchronous-reset negative control", "Files/Research_Papers/benchmark/pilot_v0_1/P02/validation_rtl/wrong_async.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/source/validation_rtl/wrong_async.sv",
     "23fef17e6c20a3efb52bb6fb49c0e2b80f54a47c"),
    ("P05 requirement", "Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_REQUIREMENT.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/P05_REQUIREMENT.md",
     "a544fa83625266cabae7642d4b6cb356ccf0c9f6"),
    ("P05 interpretations", "Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_INTERPRETATIONS.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/P05_INTERPRETATIONS.md",
     "31fedca9a16de2b35027ee87dd2e003a38bf35eb"),
    ("P05 specifications", "Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_SPECIFICATIONS.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/P05_SPECIFICATIONS.md",
     "65a34d0c689cdbbdba567cc306fa34041e920a87"),
    ("P05 formal strategy", "Files/Research_Papers/benchmark/pilot_v0_1/P05/formal/STRATEGY.md",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/formal/STRATEGY.md",
     "fbee5ad74384f59188dccd6f08f3fff2630aeba2"),
    ("P05 formal harness", "Files/Research_Papers/benchmark/pilot_v0_1/P05/formal/harness.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/formal/harness.sv",
     "9f15b23dd158a1a4af5f90bbbf6d1671998b873c"),
    ("P05 B-state formal properties", "Files/Research_Papers/benchmark/pilot_v0_1/P05/formal/b_properties.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/formal/b_properties.sv",
     "6b258d27f4e9529f3be43039b857a168e68770cd"),
    ("P05 formal runner", "Files/Research_Papers/benchmark/pilot_v0_1/P05/formal/run.py",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/formal/run.py",
     "144d37d1dbcd0ffe468aaf0e9c2f0bb14082c764"),
    ("P05 reference RTL", "Files/Research_Papers/benchmark/pilot_v0_1/P05/reference_rtl/responses.sv",
     "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/reference_rtl/responses.sv",
     "94eaaf0ee89341007892783935d7e1eeebddeea5"),
]

# This is deliberately a *recorded* difference, not an assertion that the two
# forms are interchangeable. The run-02 snapshot form is retained as evidence.
REVIEW_FORM_PAIR = {
    "current_path": "Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/reviewer_form.md",
    "current_git_blob_sha1": "5f091e8b86ad3c255ac0cd4f99f7c0ad77573093",
    "run02_snapshot_path": "Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/source/annotation/REVIEW_FORM.md",
    "run02_snapshot_git_blob_sha1": "79179adf25d6ff604b11c4a33bc3bb9dc5d5673a",
}

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def add_check(checks: list[dict[str, Any]], name: str, ok: bool, detail: str) -> None:
    checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})

def audit_hash_manifest(repo_root: Path, rel_manifest: str,
                        expected_manifest_blob: str | None = None) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    manifest_path = repo_root / rel_manifest
    prefix = rel_manifest.replace("/", ":")
    if not manifest_path.is_file():
        add_check(checks, prefix + ":present", False, "SHA256SUMS.json missing")
        return checks
    actual_manifest_blob = git_blob_sha(manifest_path)
    if expected_manifest_blob:
        add_check(checks, prefix + ":manifest-blob",
                  actual_manifest_blob == expected_manifest_blob,
                  "manifest Git blob matches pinned baseline" if actual_manifest_blob == expected_manifest_blob
                  else "manifest Git blob mismatch; review the source change before updating the pin")
    try:
        entries = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        add_check(checks, prefix + ":json", False, "invalid JSON: %s" % exc)
        return checks
    valid_schema = isinstance(entries, dict) and all(
        isinstance(name, str) and isinstance(digest, str) and re.fullmatch(r"[0-9a-fA-F]{64}", digest)
        for name, digest in entries.items()
    )
    add_check(checks, prefix + ":schema", valid_schema,
              "%d entries with SHA-256-shaped values" % (len(entries) if isinstance(entries, dict) else 0))
    if not isinstance(entries, dict) or not valid_schema:
        return checks

    run_dir = manifest_path.parent
    expected_files = set(entries)
    actual_files = {
        p.relative_to(run_dir).as_posix()
        for p in run_dir.rglob("*")
        if p.is_file() and p != manifest_path
    }
    add_check(checks, prefix + ":inventory",
              expected_files == actual_files,
              "%d listed files; %d actual files (excluding the manifest itself); missing=%s; unlisted=%s" % (
                  len(expected_files), len(actual_files),
                  sorted(expected_files - actual_files), sorted(actual_files - expected_files)))
    for rel, expected_digest in entries.items():
        rel_path = Path(rel)
        safe = not rel_path.is_absolute() and ".." not in rel_path.parts
        if not safe:
            add_check(checks, prefix + ":path:" + rel, False, "manifest path escapes the run directory")
            continue
        full = run_dir / rel_path
        if not full.is_file():
            add_check(checks, prefix + ":sha256:" + rel, False, "listed file missing")
            continue
        actual_digest = sha256_bytes(full.read_bytes())
        add_check(checks, prefix + ":sha256:" + rel, actual_digest.lower() == expected_digest.lower(),
                  "SHA-256 matches manifest" if actual_digest.lower() == expected_digest.lower()
                  else "expected %s; computed %s" % (expected_digest, actual_digest))
    return checks

def audit_source_pair(repo_root: Path, name: str, root_rel: str, snapshot_rel: str,
                      expected_blob: str) -> dict[str, Any]:
    root_file, snapshot_file = repo_root / root_rel, repo_root / snapshot_rel
    if not root_file.is_file() or not snapshot_file.is_file():
        return {"check": "source-pair:" + name, "status": "FAIL",
                "detail": "root or run-02 snapshot file missing", "root_path": root_rel,
                "snapshot_path": snapshot_rel}
    root_blob, snapshot_blob = git_blob_sha(root_file), git_blob_sha(snapshot_file)
    passed = root_blob == expected_blob and snapshot_blob == expected_blob and root_blob == snapshot_blob
    return {
        "check": "source-pair:" + name,
        "status": "PASS" if passed else "FAIL",
        "detail": "current source and run-02 snapshot are identical and match the C2 Git-blob pin"
                  if passed else "source/snapshot/pin mismatch; do not relabel the executed source",
        "root_path": root_rel,
        "snapshot_path": snapshot_rel,
        "expected_git_blob_sha1": expected_blob,
        "root_git_blob_sha1": root_blob,
        "snapshot_git_blob_sha1": snapshot_blob,
    }

def audit_semantic_status(repo_root: Path) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    root = repo_root / PILOT_ROOT
    try:
        p02_meta = json.loads((root / "P02/metadata.json").read_text(encoding="utf-8"))
        p05_meta = json.loads((root / "P05/metadata.json").read_text(encoding="utf-8"))
        p02_runs = json.loads((root / "P02/evidence/run-02/runs.json").read_text(encoding="utf-8"))
        p05_runs = json.loads((root / "P05/evidence/run-02/runs.json").read_text(encoding="utf-8"))
        p02_env = json.loads((root / "P02/evidence/run-02/environment.json").read_text(encoding="utf-8"))
        p05_env = json.loads((root / "P05/evidence/run-02/environment.json").read_text(encoding="utf-8"))
        p02_results = (root / "P02/P02_RESULTS.md").read_text(encoding="utf-8")
        p05_results = (root / "P05/P05_RESULTS.md").read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        add_check(checks, "semantic-sources:readable", False, str(exc))
        return checks

    add_check(checks, "P02:identity-and-status",
              p02_meta.get("instance_id") == "P02"
              and p02_meta.get("status") == "technical_verification_complete",
              "P02 metadata identifies the deterministic sequential control and technical status")
    add_check(checks, "P02:effective-source-commit",
              p02_meta.get("reproducibility", {}).get("repository_commit") == p02_env.get("base_commit"),
              "metadata commit and run-02 environment base commit agree")
    add_check(checks, "P02:reference-RTL-digest",
              p02_meta.get("reference_rtl", {}).get("reference_rtl/register.sv", {}).get("sha256")
              == json.loads((root / "P02/evidence/run-02/SHA256SUMS.json").read_text(encoding="utf-8"))
                  .get("source/reference_rtl/register.sv"),
              "metadata reference RTL SHA-256 agrees with retained run-02 source manifest")
    add_check(checks, "P02:control-not-ambiguity",
              p02_meta.get("requirement", {}).get("primary_ambiguity_dimension") == "none"
              and p02_meta.get("certification", {}).get("certified_ambiguous") is False,
              "P02 remains a deterministic control, not an ambiguity claim")
    p02_statuses = {item.get("name"): item.get("status") for item in p02_runs}
    expected_p02 = {"reference-bmc": "PASS", "reference-induction": "PASS",
                    "reference-cover": "PASS", "wrong-bmc": "FAIL", "async-bmc": "FAIL"}
    add_check(checks, "P02:run-statuses",
              all(p02_statuses.get(name) == status for name, status in expected_p02.items()),
              "run-02 statuses align with expected reference and deliberately wrong controls")
    add_check(checks, "P02:results-summary",
              all(term in p02_results for term in [
                  "Reference BMC | PASS", "Reference temporal induction | PASS",
                  "Reference cover | PASS", "Wrong reset-polarity BMC | FAIL",
                  "Wrong asynchronous-reset BMC | FAIL", "All 8 goals"]),
              "results prose records BMC, induction, cover and both negative-control outcomes")

    add_check(checks, "P05:identity-and-status",
              p05_meta.get("instance_id") == "P05" and p05_meta.get("status") == "UNRESOLVED",
              "P05 remains an unresolved candidate, not a certified case")
    add_check(checks, "P05:effective-source-commit",
              p05_meta.get("reproducibility", {}).get("repository_commit") == p05_env.get("base_commit"),
              "metadata commit and run-02 environment base commit agree")
    add_check(checks, "P05:reference-RTL-digest",
              p05_meta.get("reference_rtl", {}).get("reference_rtl/responses.sv", {}).get("sha256")
              == json.loads((root / "P05/evidence/run-02/SHA256SUMS.json").read_text(encoding="utf-8"))
                  .get("source/reference_rtl/responses.sv"),
              "metadata reference RTL SHA-256 agrees with retained run-02 source manifest")
    add_check(checks, "P05:no-human-certification",
              p05_meta.get("human_annotation", {}).get("annotator_count") == 0
              and p05_meta.get("certification", {}).get("human_requirement_met") is False
              and p05_meta.get("certification", {}).get("certified_ambiguous") is False,
              "zero annotations and no ambiguity certification are retained in metadata")
    p05_statuses = {item.get("name"): item.get("status") for item in p05_runs}
    expected_p05 = {"reference-bmc": "PASS", "reference-induction": "PASS",
                    "reference-cover": "PASS", "equality-bmc": "FAIL"}
    add_check(checks, "P05:run-statuses",
              all(p05_statuses.get(name) == status for name, status in expected_p05.items()),
              "run-02 conformance checks pass and equality miter finds the reported distinction")
    add_check(checks, "P05:results-summary",
              all(term in p05_results for term in [
                  "A/B conformance BMC | PASS", "A/B conformance induction | PASS",
                  "Post-reset divergence covers | PASS", "Post-reset equality BMC | FAIL",
                  "human annotation count = 0", "No human ratings"]),
              "results prose records formal distinction and explicitly pending human plausibility")

    return checks

def locate_repo_root(start: Path) -> Path | None:
    for parent in [start, *start.parents]:
        if (parent / REPO_MARKER).is_file():
            return parent
    return None

def run_audit(repo_root: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    manifest_summary = []
    for item in RUN_MANIFESTS:
        run_checks = audit_hash_manifest(repo_root, item["path"], item["expected_git_blob_sha1"])
        checks.extend(run_checks)
        manifest_summary.append({
            "case": item["case"], "run": item["run"], "manifest_path": item["path"],
            "manifest_expected_git_blob_sha1": item["expected_git_blob_sha1"],
            "manifest_checks": len(run_checks),
            "manifest_failures": sum(x["status"] == "FAIL" for x in run_checks),
        })
    for name, root_rel, snap_rel, expected_blob in SOURCE_PAIRS:
        checks.append(audit_source_pair(repo_root, name, root_rel, snap_rel, expected_blob))

    # Explicitly preserve the known non-identical annotation-form version rather
    # than silently treating it as part of the executed formal source.
    current_form = repo_root / REVIEW_FORM_PAIR["current_path"]
    snap_form = repo_root / REVIEW_FORM_PAIR["run02_snapshot_path"]
    drift_paths_present = current_form.is_file() and snap_form.is_file()
    if drift_paths_present:
        current_blob, snapshot_blob = git_blob_sha(current_form), git_blob_sha(snap_form)
        expected_drift_recorded = (
            current_blob == REVIEW_FORM_PAIR["current_git_blob_sha1"]
            and snapshot_blob == REVIEW_FORM_PAIR["run02_snapshot_git_blob_sha1"]
            and current_blob != snapshot_blob
        )
        add_check(checks, "P05:review-form-version-boundary",
                  expected_drift_recorded,
                  "known, pinned difference is explicitly retained; not a formal input, but the current form must be versioned/hashed before reviewers are approached"
                  if expected_drift_recorded else "review-form baseline changed; re-audit before use")
        known_findings = [{
            "id": "C2-F1",
            "severity": "ACTION_REQUIRED_BEFORE_HUMAN_REVIEW",
            "status": "KNOWN_VERSION_DIFFERENCE",
            "current_form": REVIEW_FORM_PAIR["current_path"],
            "current_form_git_blob_sha1": current_blob,
            "run02_snapshot_form": REVIEW_FORM_PAIR["run02_snapshot_path"],
            "run02_snapshot_git_blob_sha1": snapshot_blob,
            "interpretation": "The working reviewer form is not byte-identical to the form retained in P05 run-02 source snapshot. This does not alter formal execution because the form is not read by the formal runner, but the exact form/version/hash presented to human reviewers must be explicitly frozen and recorded before data collection."
        }]
    else:
        add_check(checks, "P05:review-form-version-boundary", False,
                  "current and run-02 snapshot reviewer forms must both exist")
        known_findings = []

    checks.extend(audit_semantic_status(repo_root))
    failures = sum(item["status"] == "FAIL" for item in checks)
    return {
        "audit_id": "FORMAL-AMBIG-RTL-C2-P02-P05-EVIDENCE-ALIGNMENT",
        "audit_version": "1.0",
        "status": "PASS" if failures == 0 else "FAIL",
        "scope": "P02/P05 retained SHA-256 evidence manifests, run-02 source alignment, metadata/result semantics, and explicit annotation-form version boundary",
        "repository_root": str(repo_root),
        "formal_tools_executed": False,
        "source_files_modified": False,
        "human_reviews_collected": False,
        "certification_or_freeze_changed": False,
        "manifest_summary": manifest_summary,
        "source_pairs_checked": len(SOURCE_PAIRS),
        "source_pairs_passing": sum(c["status"] == "PASS" and c["check"].startswith("source-pair:") for c in checks),
        "checks_total": len(checks),
        "checks_passed": len(checks) - failures,
        "checks_failed": failures,
        "known_findings": known_findings,
        "checks": checks,
        "limitations": [
            "A passing digest audit establishes file integrity against the committed run manifests; it does not independently recreate the historical tool execution.",
            "The current P05 reviewer form differs from the run-02 snapshot form. This is explicitly retained as a version boundary, not hidden or treated as a formal failure.",
            "P02 technical/provenance closure remains governed by T06 and its named author-approval procedure.",
            "P05 human plausibility remains pending; no ambiguity certification or LLM result is inferred.",
            "P03/P04/P06-P12 are not implemented by this C2 audit."
        ]
    }

def main() -> int:
    root = locate_repo_root(Path(__file__).resolve())
    if root is None:
        print(json.dumps({
            "audit_id": "FORMAL-AMBIG-RTL-C2-P02-P05-EVIDENCE-ALIGNMENT",
            "status": "ERROR",
            "error": "Could not locate repository root with P02 results file."
        }, indent=2))
        return 2
    report = run_audit(root)
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
