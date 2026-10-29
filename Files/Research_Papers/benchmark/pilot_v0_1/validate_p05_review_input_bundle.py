#!/usr/bin/env python3
"""Read-only validation of the pinned, prospective P05 review-input package.

This binds file identity and records the known historical form boundary.
It does not collect reviews, score annotation data, or certify ambiguity.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

MANIFEST_REL = Path("Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/review_input_manifest_v1.json")
EXPECTED_MANIFEST_GIT_BLOB_SHA1 = "f0875ee08e81aed2c642e9478379dc178c492844"
METADATA_REL = Path("Files/Research_Papers/benchmark/pilot_v0_1/P05/metadata.json")
RESULTS_REL = Path("Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md")
ANNOTATION_README_REL = Path("Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/README.md")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1_bytes(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def add(checks: list[dict[str, str]], name: str, ok: bool, detail: str) -> None:
    checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})


def safe_file(repo_root: Path, relative: str) -> Path | None:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        return None
    return repo_root / path


def validate_pinned_files(repo_root: Path, entries: Any) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    if not isinstance(entries, list) or not entries or not all(isinstance(e, dict) for e in entries):
        add(checks, "pinned-files-schema", False, "pinned_files must be a non-empty list of objects")
        return checks
    seen: set[str] = set()
    for item in entries:
        rel = item.get("path")
        if not isinstance(rel, str) or rel in seen:
            add(checks, f"file-entry:{rel}", False, "path is missing, invalid, or duplicated")
            continue
        seen.add(rel)
        path = safe_file(repo_root, rel)
        if path is None:
            add(checks, f"file:{rel}:safe-path", False, "absolute or parent-traversal path rejected")
            continue
        if not path.is_file():
            add(checks, f"file:{rel}:present", False, "pinned file missing")
            continue
        data = path.read_bytes()
        actual_git = git_blob_sha1_bytes(data)
        actual_sha = sha256_bytes(data)
        byte_count = len(data)
        expected_git = item.get("git_blob_sha1")
        expected_sha = item.get("sha256")
        expected_bytes = item.get("bytes")
        add(checks, f"file:{rel}:git-blob",
            actual_git == expected_git and isinstance(expected_git, str) and re.fullmatch(r"[0-9a-f]{40}", expected_git) is not None,
            f"expected={expected_git}; actual={actual_git}")
        add(checks, f"file:{rel}:sha256",
            actual_sha == expected_sha and isinstance(expected_sha, str) and re.fullmatch(r"[0-9a-f]{64}", expected_sha) is not None,
            f"expected={expected_sha}; actual={actual_sha}")
        add(checks, f"file:{rel}:size", byte_count == expected_bytes,
            f"expected_bytes={expected_bytes}; actual_bytes={byte_count}")
    return checks


def validate_manifest_pin(repo_root: Path, manifest_rel: Path = MANIFEST_REL,
                          expected_git_blob: str = EXPECTED_MANIFEST_GIT_BLOB_SHA1) -> tuple[list[dict[str, str]], dict[str, Any] | None]:
    checks: list[dict[str, str]] = []
    path = repo_root / manifest_rel
    if not path.is_file():
        add(checks, "manifest:present", False, f"{manifest_rel.as_posix()} missing")
        return checks, None
    raw = path.read_bytes()
    actual_blob = git_blob_sha1_bytes(raw)
    add(checks, "manifest:pinned-git-blob",
        actual_blob == expected_git_blob,
        f"expected={expected_git_blob}; actual={actual_blob}")
    try:
        manifest = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        add(checks, "manifest:json", False, str(exc))
        return checks, None
    add(checks, "manifest:schema-version", manifest.get("schema_version") == "1.0",
        str(manifest.get("schema_version")))
    add(checks, "manifest:task-identity",
        manifest.get("task_id") == "C4" and manifest.get("case_id") == "P05",
        f"task={manifest.get('task_id')}; case={manifest.get('case_id')}")
    add(checks, "manifest:preparation-only-state",
        manifest.get("status") == "PINNED_PREPARATION_ONLY",
        f"status={manifest.get('status')}")
    reviewer_roles = {
        "reviewer_facing_requirement",
        "reviewer_facing_interpretations",
        "reviewer_facing_blank_form",
    }
    items = manifest.get("pinned_files", [])
    derived_reviewer_paths = [x.get("path") for x in items if x.get("role") in reviewer_roles]
    add(checks, "manifest:reviewer-facing-set",
        derived_reviewer_paths == manifest.get("reviewer_facing_paths"),
        f"derived={derived_reviewer_paths}; declared={manifest.get('reviewer_facing_paths')}")
    return checks, manifest


def validate_historical_form_boundary(repo_root: Path, manifest: dict[str, Any] | None) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    if not isinstance(manifest, dict):
        add(checks, "historical-form-boundary:manifest", False, "manifest unavailable")
        return checks
    boundary = manifest.get("historical_form_boundary", {})
    current_rel = boundary.get("current_form_path")
    historical_rel = boundary.get("historical_run02_form_path")
    current = safe_file(repo_root, current_rel) if isinstance(current_rel, str) else None
    historical = safe_file(repo_root, historical_rel) if isinstance(historical_rel, str) else None
    if current is None or historical is None or not current.is_file() or not historical.is_file():
        add(checks, "historical-form-boundary:files-present", False, "current or historical form missing/unsafe")
        return checks
    current_data, old_data = current.read_bytes(), historical.read_bytes()
    current_git, old_git = git_blob_sha1_bytes(current_data), git_blob_sha1_bytes(old_data)
    current_sha, old_sha = sha256_bytes(current_data), sha256_bytes(old_data)
    add(checks, "historical-form-boundary:identities-match-manifest",
        current_git == boundary.get("current_form_git_blob_sha1")
        and current_sha == boundary.get("current_form_sha256")
        and old_git == boundary.get("historical_run02_form_git_blob_sha1")
        and old_sha == boundary.get("historical_run02_form_sha256"),
        f"current_git={current_git}; historical_git={old_git}; current_sha256={current_sha}; historical_sha256={old_sha}")
    add(checks, "historical-form-boundary:forms-remain-distinct",
        current_data != old_data and current_git != old_git,
        "current form is explicitly the prospective input; run-02 snapshot remains historical evidence")
    run_manifest_rel = next((x.get("path") for x in manifest.get("pinned_files", [])
                             if x.get("role") == "historical_run02_manifest"), None)
    run_manifest = safe_file(repo_root, run_manifest_rel) if isinstance(run_manifest_rel, str) else None
    entry_matches = False
    detail = "run-02 manifest missing/unreadable"
    if run_manifest is not None and run_manifest.is_file():
        try:
            old_manifest = json.loads(run_manifest.read_text(encoding="utf-8"))
            listed = old_manifest.get("source/annotation/REVIEW_FORM.md")
            entry_matches = listed == old_sha
            detail = f"run-02 manifest snapshot digest={listed}; recomputed historical form digest={old_sha}"
        except (OSError, json.JSONDecodeError) as exc:
            detail = str(exc)
    add(checks, "historical-form-boundary:run02-manifest-binds-old-form", entry_matches, detail)
    return checks


def validate_case_state(repo_root: Path, manifest: dict[str, Any] | None) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    metadata_path = repo_root / METADATA_REL
    results_path = repo_root / RESULTS_REL
    readme_path = repo_root / ANNOTATION_README_REL
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        annotation = metadata.get("human_annotation", {})
        certification = metadata.get("certification", {})
        llm = metadata.get("llm_evaluation", {})
        add(checks, "P05:unresolved-case-status", metadata.get("status") == "UNRESOLVED",
            f"status={metadata.get('status')}")
        add(checks, "P05:zero-human-annotations", annotation.get("annotator_count") == 0,
            f"annotator_count={annotation.get('annotator_count')}")
        add(checks, "P05:not-certified-ambiguous",
            certification.get("certified_ambiguous") is False and certification.get("human_requirement_met") is False,
            json.dumps(certification, sort_keys=True))
        add(checks, "P05:no-LLM-evaluation-claimed", llm.get("status") == "not performed",
            f"llm_evaluation.status={llm.get('status')}")
    except (OSError, json.JSONDecodeError) as exc:
        add(checks, "P05:metadata-json", False, str(exc))
    if results_path.is_file():
        results = results_path.read_text(encoding="utf-8")
        add(checks, "P05:results-maintain-unresolved-boundary",
            "UNRESOLVED" in results and "No human ratings" in results and "No human ratings, agreement score" in results,
            "result summary preserves zero-review and no-certification language")
    else:
        add(checks, "P05:results-present", False, str(RESULTS_REL))
    if readme_path.is_file():
        instructions = readme_path.read_text(encoding="utf-8")
        add(checks, "P05:review-procedure-still-preparation-only",
            "Preparation only" in instructions and "No reviewer responses have been collected" in instructions,
            "review protocol remains preparation-only")
    else:
        add(checks, "P05:review-readme-present", False, str(ANNOTATION_README_REL))
    gate = manifest.get("review_gate", {}) if isinstance(manifest, dict) else {}
    add(checks, "P05:collection-remains-blocked",
        gate.get("collection_authorized") is False and gate.get("technical_completion_required") is True,
        json.dumps(gate, sort_keys=True))
    add(checks, "P05:ambiguity-and-LLM-claims-remain-off",
        gate.get("ambiguity_certified") is False and gate.get("llm_evaluation_authorized") is False,
        json.dumps(gate, sort_keys=True))
    return checks


def audit(repo_root: Path) -> dict[str, Any]:
    checks, manifest = validate_manifest_pin(repo_root)
    if manifest is not None:
        checks.extend(validate_pinned_files(repo_root, manifest.get("pinned_files")))
    checks.extend(validate_historical_form_boundary(repo_root, manifest))
    checks.extend(validate_case_state(repo_root, manifest))
    passed = sum(c["status"] == "PASS" for c in checks)
    failed = len(checks) - passed
    return {
        "schema_version": "1.0",
        "task_id": "C4",
        "audit": "P05 prospective review-input provenance",
        "status": "PASS" if failed == 0 else "FAIL",
        "summary": {"checks": len(checks), "passed": passed, "failed": failed},
        "review_collection_authorized": False,
        "p05_status": "UNRESOLVED",
        "checks": checks,
    }


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = audit(args.repo_root.resolve())
    serialized = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(json.dumps({"status": result["status"], **result["summary"]}, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
