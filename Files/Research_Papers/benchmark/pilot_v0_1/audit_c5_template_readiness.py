#!/usr/bin/env python3
"""Read-only C5 audit of reusable case-template and negative-control readiness.

The audit records whether the current schema/template can be promoted safely.
It never rewrites case data, launches formal tools, performs human review, or
freezes a benchmark template. An audit PASS can coexist with readiness BLOCKED.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

SCHEMA = Path("Files/Research_Papers/docs/benchmark_schema.md")
FORMAL_PROTOCOL = Path("Files/Research_Papers/docs/formal_verification_protocol.md")
METADATA_TEMPLATE = Path("Files/Research_Papers/templates/instance_metadata_template.yaml")
P01_README = Path("Files/Research_Papers/benchmark/pilot_v0_1/P01/README.md")
P01_MANIFEST = Path("Files/Research_Papers/benchmark/pilot_v0_1/P01/p01_package_manifest_v1.json")
P01_VALIDATOR = Path("Files/Research_Papers/benchmark/pilot_v0_1/P01/validate_p01_package.py")
STAGE_REGISTER = Path("docs/project-sequence/STAGE_REGISTER.md")
REQUIRED_SOURCES = [
    SCHEMA, FORMAL_PROTOCOL, METADATA_TEMPLATE, P01_README, P01_MANIFEST,
    P01_VALIDATOR, STAGE_REGISTER,
]
SCHEMA_REQUIRED_FIELDS = [
    "instance_id", "version", "status", "category", "specification_text",
    "ambiguity_dimension", "interpretation_A", "interpretation_B",
    "interpretation_rationale_A", "interpretation_rationale_B",
    "reference_rtl_A", "reference_rtl_B", "formal_environment", "observables",
    "formal_result", "annotation_record", "provenance",
]
TEMPLATE_GROUPS = [
    "schema_version:", "instance_id:", "instance_version:", "status:",
    "provenance:", "requirement:", "interpretations:", "reference_rtl:",
    "formal_environment:", "observables:", "formal_result:",
    "human_annotation:", "certification:", "llm_evaluation:", "reproducibility:",
]
SCHEMA_TEMPLATE_MAPPING_GAPS = [
    {"schema_field": "version", "template_field": "instance_version",
     "issue": "different key names; no canonical mapping is declared"},
    {"schema_field": "category", "template_field": None,
     "issue": "no explicit top-level category field in the YAML template"},
    {"schema_field": "specification_text", "template_field": "requirement.specification_text",
     "issue": "same concept is nested in the template but top-level in schema prose"},
    {"schema_field": "ambiguity_dimension", "template_field": "requirement.primary_ambiguity_dimension",
     "issue": "different key names and nesting"},
    {"schema_field": "interpretation_A / interpretation_B",
     "template_field": "interpretations.A / interpretations.B",
     "issue": "nested representation is plausible but not normatively mapped"},
    {"schema_field": "reference_rtl_A / reference_rtl_B",
     "template_field": "reference_rtl.A / reference_rtl.B",
     "issue": "nested representation is plausible but not normatively mapped"},
    {"schema_field": "annotation_record", "template_field": "human_annotation",
     "issue": "different key names; no canonical mapping is declared"},
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def add(checks: list[dict[str, str]], name: str, ok: bool, detail: str) -> None:
    checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})


def audit_repo(repo_root: Path, commit: str | None = None) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    checks: list[dict[str, str]] = []
    missing = [str(rel) for rel in REQUIRED_SOURCES if not (repo_root / rel).is_file()]
    add(checks, "required-source-inventory", not missing,
        "all %d source artifacts are present" % (len(REQUIRED_SOURCES) - len(missing))
        if not missing else "missing: " + ", ".join(missing))

    contents: dict[Path, str] = {}
    for rel in REQUIRED_SOURCES:
        path = repo_root / rel
        if path.is_file():
            contents[rel] = path.read_text(encoding="utf-8")

    schema = contents.get(SCHEMA, "")
    formal_protocol = contents.get(FORMAL_PROTOCOL, "")
    template = contents.get(METADATA_TEMPLATE, "")
    p01_readme = contents.get(P01_README, "")
    stage_register = contents.get(STAGE_REGISTER, "")

    present_fields = [field for field in SCHEMA_REQUIRED_FIELDS if field in schema]
    add(checks, "schema-required-field-catalogue",
        len(present_fields) == len(SCHEMA_REQUIRED_FIELDS),
        "%d/%d required schema field names found" %
        (len(present_fields), len(SCHEMA_REQUIRED_FIELDS)))

    present_groups = [group for group in TEMPLATE_GROUPS if group in template]
    add(checks, "metadata-template-section-inventory",
        len(present_groups) == len(TEMPLATE_GROUPS),
        "%d/%d expected YAML groups/keys found" % (len(present_groups), len(TEMPLATE_GROUPS)))

    manifest: dict[str, Any] = {}
    manifest_path = repo_root / P01_MANIFEST
    if manifest_path.is_file():
        try:
            parsed = json.loads(manifest_path.read_text(encoding="utf-8"))
            if isinstance(parsed, dict):
                manifest = parsed
        except json.JSONDecodeError:
            manifest = {}
    manifest_status = manifest.get("status")
    nonclaims = manifest.get("explicit_nonclaims", [])
    manifest_boundary_ok = (
        manifest_status == "BASELINE_REFERENCE_NOT_A_FREEZE_OR_CERTIFICATION"
        and isinstance(nonclaims, list)
        and any("Golden Template" in str(x)
                and ("freeze" in str(x).lower() or "frozen" in str(x).lower())
                for x in nonclaims)
    )
    add(checks, "p01-manifest-does-not-claim-freeze", manifest_boundary_ok,
        "P01 manifest status is %r and explicit non-claims preserve the no-freeze boundary" % manifest_status)

    p01_not_frozen = "NOT FROZEN" in p01_readme
    pending_decisions = "D2" in p01_readme and "D14" in p01_readme and "remain pending" in p01_readme
    add(checks, "p01-freeze-status-remains-explicit", p01_not_frozen,
        "P01 README says Golden Template freeze is NOT FROZEN")
    add(checks, "d2-d14-governance-gate-visible", pending_decisions,
        "P01 README retains the D2/D14 pending-decision gate")

    negative_control_boundary = (
        "negative-control RTL is intentionally wrong" in p01_readme
        and "must not be presented as a plausible alternate interpretation" in p01_readme
    )
    add(checks, "negative-control-not-mislabelled-as-interpretation",
        negative_control_boundary,
        "P01 documents its wrong RTL as a checker negative control, not interpretation B")

    human_formal_boundary = (
        "Formal evidence alone does not certify linguistic ambiguity" in formal_protocol
    )
    add(checks, "formal-vs-human-certification-boundary", human_formal_boundary,
        "formal protocol separates formal distinction from linguistic plausibility")

    structural_gaps: list[str] = []
    gap_checks = {
        "version_vs_instance_version": not bool(re.search(r"(?m)^version:", template))
            and bool(re.search(r"(?m)^instance_version:", template)),
        "missing_top_level_category": not bool(re.search(r"(?m)^category:", template)),
        "annotation_record_vs_human_annotation": not bool(re.search(r"(?m)^annotation_record:", template))
            and bool(re.search(r"(?m)^human_annotation:", template)),
    }
    structural_gaps.extend(name for name, observed in gap_checks.items() if observed)
    add(checks, "schema-template-alignment-gap-detected",
        len(structural_gaps) == len(gap_checks),
        "observed mapping gaps: " + ", ".join(structural_gaps))

    stage06_present = "06" in stage_register and "reusable case-template" in stage_register.lower()
    add(checks, "stage-06-dependency-recorded", stage06_present,
        "stage register identifies reusable case-template/negative-control work")

    failed = sum(item["status"] == "FAIL" for item in checks)
    blockers = [
        {
            "id": "C5-B1", "status": "OPEN",
            "finding": "The benchmark schema and metadata YAML template use different names/nesting and no normative mapping is declared.",
            "required_resolution": "Record an approved schema-to-template mapping or versioned schema/template update, with migration implications."
        },
        {
            "id": "C5-B2", "status": "OPEN",
            "finding": "The metadata template has no explicit top-level category field matching the benchmark schema's required category field.",
            "required_resolution": "Resolve category placement and lifecycle semantics in the approved schema decision."
        },
        {
            "id": "C5-B3", "status": "OPEN",
            "finding": "P01 Golden Template is explicitly NOT FROZEN and D2/D14 decisions remain pending.",
            "required_resolution": "Record the relevant author-governance decisions and complete the P01 freeze gate before promoting a reusable template."
        },
        {
            "id": "C5-B4", "status": "OPEN",
            "finding": "P01's deliberately wrong RTL is a checker negative control, not a plausible alternate interpretation; control and ambiguity-candidate roles must remain distinct.",
            "required_resolution": "Define role-specific required/optional artifacts so an unambiguous control does not fabricate an interpretation-B requirement."
        },
        {
            "id": "C5-B5", "status": "OPEN",
            "finding": "Existing P01/P02/P05 package validation does not establish that one frozen template can correctly represent all case roles and lifecycle states.",
            "required_resolution": "After governance/schema resolution, add role-aware fixtures for control, ambiguity candidate, and rejected/negative candidate without changing historical evidence."
        },
    ]
    readiness = "BLOCKED_NOT_FROZEN" if blockers and failed == 0 else "AUDIT_FAILURE"
    checked_files = []
    for rel in REQUIRED_SOURCES:
        path = repo_root / rel
        if path.is_file():
            checked_files.append({
                "path": str(rel), "bytes": path.stat().st_size, "sha256": sha256_file(path)
            })
    return {
        "audit_id": "FORMAL-AMBIG-RTL-C5-TEMPLATE-READINESS",
        "audit_version": "1.0",
        "audit_result": "PASS" if failed == 0 else "FAIL",
        "template_readiness": readiness,
        "repo_commit": commit or os.environ.get("GITHUB_SHA", "UNRECORDED"),
        "source_facts": {
            "schema_required_fields_found": len(present_fields),
            "schema_required_fields_expected": len(SCHEMA_REQUIRED_FIELDS),
            "template_groups_found": len(present_groups),
            "template_groups_expected": len(TEMPLATE_GROUPS),
            "schema_template_mapping_gaps": SCHEMA_TEMPLATE_MAPPING_GAPS,
            "observed_gap_checks": structural_gaps,
            "p01_manifest_status": manifest_status,
            "p01_not_frozen": p01_not_frozen,
            "d2_d14_pending": pending_decisions,
            "formal_human_boundary_present": human_formal_boundary,
            "p01_negative_control_role_distinguished": negative_control_boundary,
        },
        "checks": checks,
        "failed_checks": failed,
        "open_blockers": blockers,
        "checked_source_files": checked_files,
        "explicit_nonclaims": [
            "No schema/template was changed or frozen.",
            "No P01/P02/P05 case content or historical evidence was changed.",
            "No formal tool was executed.",
            "No human review was collected or performed.",
            "No ambiguity certification, model evaluation, or project-completion claim is made.",
            "C5 is the user-directed C-series action label; this audit does not infer an official T1-T31 task number."
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--commit", default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = audit_repo(args.repo_root, args.commit)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if result["audit_result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
