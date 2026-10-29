#!/usr/bin/env python3
"""Validate coverage and non-binding status of the C6 schema/template proposal."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

PROPOSAL = Path("docs/project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.json")
SCHEMA = Path("Files/Research_Papers/docs/benchmark_schema.md")
TEMPLATE = Path("Files/Research_Papers/templates/instance_metadata_template.yaml")
FORMAL = Path("Files/Research_Papers/docs/formal_verification_protocol.md")
PINNED = {
    str(SCHEMA): "ed9ddd7bd10f19bb59d126db2978579fe8fd19ea",
    str(TEMPLATE): "3a0d1fecf1228f320bd459e1c61283912a4238ed",
    str(FORMAL): "7533420227bed29579732e848fa03cb049b62c7c",
}
ALLOWED_STATUSES = {
    "DIRECT", "RENAME_CANDIDATE", "SEMANTIC_DECISION_REQUIRED", "MISSING_FIELD",
    "NESTING_CANDIDATE", "RENAME_AND_NESTING_CANDIDATE", "NESTED_REPRESENTATION_CANDIDATE",
    "DIRECT_OBJECT_CANDIDATE", "CONDITIONAL_MAPPING_CANDIDATE", "INSUFFICIENT_MAPPING",
    "DISTRIBUTED_MAPPING_CANDIDATE",
}

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()

def validate(repo: Path) -> dict[str, Any]:
    repo = repo.resolve()
    checks: list[dict[str, str]] = []
    def add(name: str, ok: bool, detail: str) -> None:
        checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})

    for path, expected in PINNED.items():
        full = repo / path
        ok = full.is_file() and git_blob_sha(full) == expected
        add("pinned-source:" + path, ok,
            "matches inspected source Git blob" if ok else "missing or changed; create a reviewed proposal revision")

    try:
        data = json.loads((repo / PROPOSAL).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        data = {}

    add("proposal-schema-and-nonbinding-status",
        data.get("proposal_id") == "FORMAL-AMBIG-RTL-C6-SCHEMA-TEMPLATE-MAPPING"
        and data.get("proposal_version") == "1.0"
        and data.get("status") == "NON_BINDING_REQUIRES_AUTHOR_DECISION",
        "proposal identity/version/status remains non-binding")

    schema_text = (repo / SCHEMA).read_text(encoding="utf-8") if (repo / SCHEMA).is_file() else ""
    section = schema_text.split("## 3. Required instance fields", 1)
    required = re.findall(r"- \x60([^\x60]+)\x60", section[1].split("\n## ", 1)[0]) if len(section) == 2 else []
    entries = data.get("field_mappings", [])
    names = [x.get("schema_field") for x in entries if isinstance(x, dict)]
    add("all-schema-fields-have-one-mapping",
        len(required) == len(names) and set(required) == set(names) and len(names) == len(set(names)),
        "%d schema field entries and %d unique proposal mappings" % (len(required), len(names)))

    invalid = [str(x.get("schema_field", "unknown")) for x in entries if
               not isinstance(x, dict) or x.get("mapping_status") not in ALLOWED_STATUSES
               or not isinstance(x.get("decision_needed"), bool)]
    add("mapping-entry-shape", not invalid,
        "all entries have recognized status and decision flag" if not invalid else "invalid entries: " + repr(invalid))

    decisions = data.get("decision_questions", [])
    decision_ids = {x.get("decision") for x in decisions if isinstance(x, dict)}
    add("D2-D14-decisions-explicit",
        decision_ids == {"D2", "D14"} and all(x.get("question") and x.get("options") for x in decisions),
        "both lifecycle/vocabulary and case-layout decisions are explicit")

    roles = {x.get("case_role") for x in data.get("role_requirements_proposal", []) if isinstance(x, dict)}
    add("role-aware-control-candidate-and-negative-cases",
        {"unambiguous_control", "ambiguity_candidate", "negative_candidate"}.issubset(roles),
        "proposal distinguishes controls, ambiguity candidates and negative candidates")

    additions = {x.get("field") for x in data.get("proposed_additional_fields", []) if isinstance(x, dict)}
    add("extensions-labelled-proposal-only",
        {"case_role", "classification", "annotation_record_path"}.issubset(additions)
        and all(x.get("status") == "PROPOSAL_ONLY" for x in data.get("proposed_additional_fields", [])),
        "extension fields are clearly non-binding suggestions")

    claims = data.get("explicit_nonclaims", [])
    add("historical-and-approval-boundaries",
        data.get("status") == "NON_BINDING_REQUIRES_AUTHOR_DECISION"
        and any("not normative" in x.lower() and "d2/d14" in x.lower() for x in claims)
        and any("remain unchanged" in x.lower() for x in claims)
        and any("No formal execution" in x for x in claims),
        "no schema migration, approval or experiment is claimed")

    failed = sum(c["status"] == "FAIL" for c in checks)
    return {
        "audit_id": "FORMAL-AMBIG-RTL-C6-MAPPING-PROPOSAL-VALIDATION",
        "audit_version": "1.0",
        "audit_result": "PASS" if failed == 0 else "FAIL",
        "proposal_status": data.get("status", "UNREADABLE"),
        "checks": checks,
        "checks_passed": len(checks) - failed,
        "checks_failed": failed,
        "schema_required_fields": required,
        "mapping_count": len(entries),
        "explicit_nonclaims": [
            "Validation confirms proposal coverage and source identity only.",
            "No canonical schema/template changes or governance approval are inferred.",
            "No formal tools, human review or model evaluation are run."
        ]
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = validate(args.repo_root)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if result["audit_result"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
