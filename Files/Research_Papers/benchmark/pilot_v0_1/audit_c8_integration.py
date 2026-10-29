#!/usr/bin/env python3
"""Cross-artifact C8 consistency audit for C5-C7. Read-only and non-binding."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

C5_REPORT = Path("docs/project-state/C5_TEMPLATE_AND_NEGATIVE_CONTROL_READINESS.md")
C5_EVIDENCE = Path("docs/project-state/evidence/C5_TEMPLATE_READINESS_AUDIT_RUN_40813383592.json")
C6_PROPOSAL = Path("docs/project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.json")
C6_REPORT = Path("docs/project-state/C6_SCHEMA_TEMPLATE_MAPPING_VALIDATION.md")
C6_EVIDENCE = Path("docs/project-state/evidence/C6_SCHEMA_TEMPLATE_MAPPING_RUN_40814081793.json")
C7_REPORT = Path("docs/project-state/C7_ROLE_AWARE_FIXTURES.md")
C7_EVIDENCE = Path("docs/project-state/evidence/C7_ROLE_AWARE_FIXTURES_RUN_40814758386.json")
SCHEMA = Path("Files/Research_Papers/docs/benchmark_schema.md")
TEMPLATE = Path("Files/Research_Papers/templates/instance_metadata_template.yaml")
FORMAL = Path("Files/Research_Papers/docs/formal_verification_protocol.md")
C7_VALIDATOR = Path("Files/Research_Papers/benchmark/pilot_v0_1/audit_c7_role_aware_fixtures.py")
C7_TESTS = Path("Files/Research_Papers/benchmark/pilot_v0_1/tests/test_audit_c7_role_aware_fixtures.py")
FIXTURE_DIR = Path("Files/Research_Papers/benchmark/pilot_v0_1/tests/fixtures/c7_role_aware")
FIXTURES = {
    "unambiguous_control": FIXTURE_DIR / "unambiguous_control.json",
    "ambiguity_candidate": FIXTURE_DIR / "ambiguity_candidate.json",
    "negative_candidate": FIXTURE_DIR / "negative_candidate.json",
    "robustness_case": FIXTURE_DIR / "robustness_case.json",
}
PINNED = {
    str(SCHEMA): "ed9ddd7bd10f19bb59d126db2978579fe8fd19ea",
    str(TEMPLATE): "3a0d1fecf1228f320bd459e1c61283912a4238ed",
    str(FORMAL): "7533420227bed29579732e848fa03cb049b62c7c",
    str(C5_REPORT): "7cf349f96630bda7e95acbbd359c674c57b83b42",
    str(C5_EVIDENCE): "5b12a21d893f106e94bffa56481002cd140bbc40",
    str(C6_PROPOSAL): "f52c73984eea7bb342cc37c60f2169149b199c61",
    str(C6_REPORT): "60c7ae2c3823ae0aa9eb13ff4251b991fa0abe92",
    str(C6_EVIDENCE): "7441b84251d5c6b86387a4fbaab643b21ca9f616",
    str(C7_REPORT): "1cb6815ae15a7a4abfffc83cba86c3d9d8e5f89a",
    str(C7_EVIDENCE): "531e638d5c8f234875cb4ab47d47b19b11369c7a",
    str(C7_VALIDATOR): "b4f923e27868226c3d8a8841c6b48e0d114233f7",
    str(C7_TESTS): "d39d741fc259d7668b9d97a09f22bf3970a8cd27",
    str(FIXTURE_DIR / "unambiguous_control.json"): "95308c4e04241ed68a2999fe44960cce6a7b63d8",
    str(FIXTURE_DIR / "ambiguity_candidate.json"): "57fb823fe592695d0587321389d55609f3910bea",
    str(FIXTURE_DIR / "negative_candidate.json"): "c95a84fe7b62c46fe209f6568dd4df1aef8c5e85",
    str(FIXTURE_DIR / "robustness_case.json"): "1ce2fe75200d1b2d288b15c5ca1c08c9419d8561",
}
EXPECTED_ROLES = set(FIXTURES)
C6_STATUS = "NON_BINDING_REQUIRES_AUTHOR_DECISION"
C7_RUN_ID = 40814758386

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def check(name: str, ok: bool, detail: str) -> dict[str, str]:
    return {"check": name, "status": "PASS" if ok else "FAIL", "detail": detail}

def read_json(root: Path, rel: Path) -> dict[str, Any]:
    try:
        value = json.loads((root / rel).read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}

def obj(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}

def validate_fixture(record: Any, role: str) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    def add(name: str, ok: bool, detail: str) -> None:
        checks.append(check(name, bool(ok), detail))
    if not isinstance(record, dict):
        return [check("fixture-record-is-object", False, "fixture must be an object")]
    context = obj(record.get("fixture_context"))
    formal = obj(record.get("formal_result"))
    human = obj(record.get("human_annotation"))
    cert = obj(record.get("certification"))
    interp = obj(record.get("interpretations"))
    rtl = obj(record.get("reference_rtl"))
    provenance = obj(record.get("provenance"))
    add("fixture-boundary", context.get("fixture_only") is True
        and context.get("not_a_real_benchmark_case") is True
        and context.get("fixture_status") == "NON_BINDING_PROPOSAL",
        "fixture remains synthetic, non-binding, and not a benchmark instance")
    add("role-and-identity", record.get("case_role") == role
        and record.get("fixture_id") == record.get("instance_id")
        and str(record.get("fixture_id", "")).startswith("C7-FIXTURE-"),
        "case role and reserved fixture identity agree")
    add("no-result-promotion", record.get("status") == "candidate"
        and record.get("classification") is None
        and formal.get("result") == "NOT_RUN"
        and human.get("status") == "NOT_COLLECTED" and human.get("responses_count") == 0
        and cert.get("certified_ambiguous") is False and cert.get("decision") == "NOT_ADJUDICATED",
        "fixture has no formal result, human responses, classification or certification")
    add("synthetic-provenance", provenance.get("source_type") == "synthetic_test_fixture"
        and provenance.get("canonical_case_path") is None and provenance.get("source_commit") is None,
        "fixture has no asserted canonical case path or source commit")
    add("fixture-uri-only", str(obj(record.get("requirement")).get("source_reference", "")).startswith("fixture://")
        and all(str(v.get("path", "")).startswith("fixture://")
                for v in rtl.values() if isinstance(v, dict) and v.get("path") is not None),
        "requirement and any RTL references use fixture URIs")
    b_interp = interp.get("B")
    b_rtl = rtl.get("B")
    role_ok = False
    role_detail = "unknown role"
    if role == "unambiguous_control":
        control = obj(record.get("checker_negative_control"))
        role_ok = b_interp is None and b_rtl is None \
            and control.get("role") == "formal_checker_negative_control" \
            and control.get("actual_formal_result") == "NOT_RUN" \
            and control.get("fixture_reference_only") is True
        role_detail = "control leaves B absent and labels the wrong implementation separately"
    elif role == "ambiguity_candidate":
        role_ok = isinstance(b_interp, dict) and bool(b_interp.get("text")) \
            and isinstance(b_rtl, dict) and b_rtl.get("fixture_reference_only") is True
        role_detail = "candidate has placeholder interpretation B and RTL B, without scientific claims"
    elif role == "negative_candidate":
        rejection = obj(record.get("rejection_record"))
        role_ok = isinstance(b_interp, dict) and isinstance(b_rtl, dict) \
            and rejection.get("status") == "PLACEHOLDER_NOT_ADJUDICATED" \
            and rejection.get("reason_code") == "NOT_ADJUDICATED_FIXTURE_ONLY"
        role_detail = "negative case has an explicitly unadjudicated placeholder rejection record"
    elif role == "robustness_case":
        control = obj(record.get("checker_negative_control"))
        role_ok = b_interp is None and b_rtl is None \
            and str(record.get("robustness_target", "")).startswith("FIXTURE_STRUCTURE_ONLY") \
            and control.get("role") == "robustness_negative_control" \
            and control.get("actual_formal_result") == "NOT_RUN"
        role_detail = "robustness aim and checker-negative implementation are separate from B"
    add("role-specific-contract", role_ok, role_detail)
    return checks

def audit_repo(repo_root: Path, commit: str | None = None) -> dict[str, Any]:
    root = repo_root.resolve()
    checks: list[dict[str, str]] = []
    def add(name: str, ok: bool, detail: str) -> None:
        checks.append(check(name, bool(ok), detail))

    source_checks = []
    for rel, expected in PINNED.items():
        path = root / rel
        ok = path.is_file() and git_blob_sha(path) == expected
        item = check("pinned:" + rel, ok,
            "matches recorded Git blob object" if ok else "missing or changed; do not refresh without a reviewed version")
        source_checks.append(item)
        checks.append(item)

    c5_text = (root / C5_REPORT).read_text(encoding="utf-8") if (root / C5_REPORT).is_file() else ""
    c6_text = (root / C6_REPORT).read_text(encoding="utf-8") if (root / C6_REPORT).is_file() else ""
    c7_text = (root / C7_REPORT).read_text(encoding="utf-8") if (root / C7_REPORT).is_file() else ""
    schema_text = (root / SCHEMA).read_text(encoding="utf-8") if (root / SCHEMA).is_file() else ""
    schema_section = schema_text.split("## 3. Required instance fields", 1)
    schema_fields = []
    if len(schema_section) == 2:
        for line in schema_section[1].splitlines():
            stripped = line.strip()
            if stripped.startswith("- ") and stripped.count(chr(96)) == 2:
                schema_fields.append(stripped[2:].strip(chr(96)))

    c5 = read_json(root, C5_EVIDENCE)
    c6 = read_json(root, C6_EVIDENCE)
    c7 = read_json(root, C7_EVIDENCE)
    proposal = read_json(root, C6_PROPOSAL)
    mappings = proposal.get("field_mappings", [])
    mapping_names = [x.get("schema_field") for x in mappings if isinstance(x, dict)]
    add("C5-blocker-preserved",
        "BLOCKED — NOT FROZEN" in c5_text and c5.get("template_readiness") == "BLOCKED_NOT_FROZEN"
        and c5.get("open_blocker_count", 0) >= 1,
        "C5 keeps the template blocked and unfrozen")
    add("C5-machine-evidence-consistent",
        c5.get("audit", {}).get("checks_passed") == 10
        and c5.get("audit", {}).get("regression_tests_passed") == 6
        and c5.get("audit", {}).get("checks_failed") == 0,
        "C5 evidence preserves successful audit and test totals")
    add("C6-proposal-nonbinding",
        proposal.get("proposal_id") == "FORMAL-AMBIG-RTL-C6-SCHEMA-TEMPLATE-MAPPING"
        and proposal.get("proposal_version") == "1.0" and proposal.get("status") == C6_STATUS
        and "not normative" in " ".join(proposal.get("explicit_nonclaims", [])).lower(),
        "C6 remains a versioned non-binding proposal")
    add("C6-schema-fields-mapped-once",
        len(schema_fields) == 18 and len(mappings) == 18 and len(mapping_names) == 18
        and set(mapping_names) == set(schema_fields) and len(set(mapping_names)) == 18,
        "all schema-listed fields appear exactly once in the C6 mapping")
    add("C6-source-references-match-pins",
        {x.get("path"): x.get("git_blob_sha1") for x in proposal.get("source_refs", [])}
        == {str(SCHEMA): PINNED[str(SCHEMA)], str(TEMPLATE): PINNED[str(TEMPLATE)], str(FORMAL): PINNED[str(FORMAL)]},
        "C6 proposal references the same three canonical source objects")
    c6v = c6.get("validation", {})
    add("C6-validation-evidence-consistent",
        c6.get("proposal_status") == C6_STATUS and c6v.get("audit_result") == "PASS"
        and c6v.get("check_count") == 10 and c6v.get("checks_failed") == 0
        and c6v.get("mapping_count") == 18 and c6v.get("regression_tests_passed") == 7
        and c6.get("governance_status", {}).get("D2") == "OPEN"
        and c6.get("governance_status", {}).get("D14") == "OPEN",
        "C6 evidence records 18 mappings, 7 tests, and open D2/D14")
    add("C6-report-evidence-agree", "10/10 source/coverage checks" in c6_text
        and "7/7 regression tests passed" in c6_text and C6_STATUS in c6_text,
        "C6 human-readable report agrees with machine evidence")
    expected_roles = {"unambiguous_control", "ambiguity_candidate", "negative_candidate", "robustness_case"}
    proposed_roles = {x.get("case_role") for x in proposal.get("role_requirements_proposal", []) if isinstance(x, dict)}
    add("C6-roles-cover-C7-fixtures", proposed_roles == expected_roles,
        "C6 role proposal covers exactly the four C7 fixture roles")
    add("C7-evidence-success-consistent",
        c7.get("workflow", {}).get("run_id") == C7_RUN_ID
        and c7.get("workflow", {}).get("conclusion") == "success"
        and c7.get("validation", {}).get("audit_result") == "PASS"
        and c7.get("validation", {}).get("checks_total") == 53
        and c7.get("validation", {}).get("checks_failed") == 0
        and c7.get("validation", {}).get("regression_tests_passed") == 10
        and c7.get("validation", {}).get("regression_tests_failed") == 0,
        "C7 evidence records the successful 53-check, 10-test run")
    add("C7-report-evidence-agree", "53/53 source/fixture checks" in c7_text
        and "10/10 regression tests passed" in c7_text and "D2/D14: unresolved" in c7_text,
        "C7 report agrees with machine evidence and preserves open governance")
    add("D2-D14-remain-open",
        c6.get("governance_status", {}).get("D2") == "OPEN"
        and c6.get("governance_status", {}).get("D14") == "OPEN"
        and c7.get("governance", {}).get("D2") == "OPEN"
        and c7.get("governance", {}).get("D14") == "OPEN",
        "D2 and D14 remain explicitly open in both C6 and C7 evidence")

    fixture_reports = []
    for role, rel in FIXTURES.items():
        data = read_json(root, rel)
        role_checks = validate_fixture(data, role)
        fixture_reports.append({
            "path": str(rel), "fixture_id": data.get("fixture_id"),
            "case_role": role, "checks": role_checks,
            "passed": sum(c["status"] == "PASS" for c in role_checks),
            "failed": sum(c["status"] == "FAIL" for c in role_checks),
        })
        checks.extend(role_checks)
    roles_found = {x.get("case_role") for x in fixture_reports if x.get("fixture_id")}
    add("all-four-fixtures-present", len(fixture_reports) == 4 and roles_found == expected_roles,
        "four role-specific fixtures are readable with distinct roles")
    add("C7-evidence-fixture-count-agrees",
        c7.get("validation", {}).get("fixtures_total") == 4
        and set(c7.get("validation", {}).get("roles", [])) == expected_roles,
        "C7 machine evidence agrees with the four inspected fixture roles")
    add("canonical-files-remain-unchanged",
        all(item["status"] == "PASS" for item in source_checks[:3])
        and c6.get("governance_status", {}).get("canonical_schema_changed") is False
        and c6.get("governance_status", {}).get("canonical_yaml_template_changed") is False
        and c7.get("governance", {}).get("canonical_schema_changed") is False
        and c7.get("governance", {}).get("canonical_yaml_template_changed") is False,
        "canonical source fingerprints match and C6/C7 claim no schema/template change")

    failed = sum(item["status"] == "FAIL" for item in checks)
    return {
        "audit_id": "FORMAL-AMBIG-RTL-C8-C5-C7-INTEGRATION",
        "audit_version": "1.0",
        "audit_result": "PASS" if failed == 0 else "FAIL",
        "integration_status": "CONSISTENT_BUT_GOVERNANCE_BLOCKED" if failed == 0 else "INTEGRATION_MISMATCH",
        "repo_commit": commit or "UNRECORDED",
        "checks": checks,
        "checks_total": len(checks),
        "checks_passed": len(checks) - failed,
        "checks_failed": failed,
        "source_pin_total": len(source_checks),
        "source_pin_passed": sum(item["status"] == "PASS" for item in source_checks),
        "schema_field_count": len(schema_fields),
        "mapping_entry_count": len(mappings),
        "fixture_count": len(fixture_reports),
        "fixture_reports": fixture_reports,
        "governance": {"D2": "OPEN", "D14": "OPEN", "template_freeze": "BLOCKED_NOT_FROZEN"},
        "explicit_nonclaims": [
            "This audit checks consistency of C5-C7 records only.",
            "C7 fixtures are synthetic test material, not real benchmark cases.",
            "No canonical schema/template or historical case evidence was modified.",
            "No formal tool, human review or LLM experiment was executed.",
            "No D2/D14 decision, template freeze, ambiguity certification or project completion is inferred."
        ],
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--commit", default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    report = audit_repo(args.repo_root, args.commit)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["audit_result"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
