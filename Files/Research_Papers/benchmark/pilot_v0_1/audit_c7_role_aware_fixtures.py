#!/usr/bin/env python3
"""Read-only audit of C7 role-aware illustrative fixtures, never real cases."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

PROPOSAL = Path("docs/project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.json")
SCHEMA = Path("Files/Research_Papers/docs/benchmark_schema.md")
TEMPLATE = Path("Files/Research_Papers/templates/instance_metadata_template.yaml")
FORMAL = Path("Files/Research_Papers/docs/formal_verification_protocol.md")
FIXTURE_DIR = Path("Files/Research_Papers/benchmark/pilot_v0_1/tests/fixtures/c7_role_aware")
FIXTURE_PATHS = {
    "unambiguous_control": FIXTURE_DIR / "unambiguous_control.json",
    "ambiguity_candidate": FIXTURE_DIR / "ambiguity_candidate.json",
    "negative_candidate": FIXTURE_DIR / "negative_candidate.json",
    "robustness_case": FIXTURE_DIR / "robustness_case.json",
}
PINNED_SOURCES = {
    str(SCHEMA): "ed9ddd7bd10f19bb59d126db2978579fe8fd19ea",
    str(TEMPLATE): "3a0d1fecf1228f320bd459e1c61283912a4238ed",
    str(FORMAL): "7533420227bed29579732e848fa03cb049b62c7c",
    str(PROPOSAL): "f52c73984eea7bb342cc37c60f2169149b199c61",
}
EXPECTED_ROLES = set(FIXTURE_PATHS)

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def check(name: str, ok: bool, detail: str) -> dict[str, str]:
    return {"check": name, "status": "PASS" if ok else "FAIL", "detail": detail}

def obj(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}

def validate_fixture(record: Any, expected_role: str) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    def add(name: str, ok: bool, detail: str) -> None:
        checks.append(check(name, bool(ok), detail))
    if not isinstance(record, dict):
        return [check("record-is-object", False, "fixture must be a JSON object")]

    context = obj(record.get("fixture_context"))
    add("fixture-only-boundary", context.get("fixture_only") is True
        and context.get("not_a_real_benchmark_case") is True
        and context.get("fixture_status") == "NON_BINDING_PROPOSAL",
        "fixture is expressly synthetic and non-binding")
    add("fixture-not-for-research-use", isinstance(context.get("prohibited_uses"), list)
        and {"LLM prompt/evaluation", "formal evidence", "human annotation", "benchmark inclusion"}.issubset(set(context.get("prohibited_uses", []))),
        "LLM evaluation, formal evidence, human annotation and benchmark inclusion are prohibited")
    add("fixture-identity", record.get("fixture_id") == record.get("instance_id")
        and isinstance(record.get("fixture_id"), str) and record.get("fixture_id", "").startswith("C7-FIXTURE-"),
        "fixture and instance IDs use the reserved C7-FIXTURE prefix")
    add("role-matches-file", record.get("case_role") == expected_role, "case_role matches fixture slot")
    add("no-premature-classification", record.get("classification") is None and record.get("status") == "candidate",
        "scientific classification remains null and lifecycle status remains candidate")
    formal = obj(record.get("formal_result")); human = obj(record.get("human_annotation")); cert = obj(record.get("certification"))
    add("no-formal-or-human-outcome", formal.get("result") == "NOT_RUN"
        and human.get("status") == "NOT_COLLECTED" and human.get("responses_count") == 0
        and cert.get("certified_ambiguous") is False and cert.get("decision") == "NOT_ADJUDICATED",
        "no formal run, human data or ambiguity certification is claimed")
    provenance = obj(record.get("provenance"))
    add("synthetic-provenance-only", provenance.get("source_type") == "synthetic_test_fixture"
        and provenance.get("canonical_case_path") is None and provenance.get("source_commit") is None,
        "no canonical case path or source commit is asserted")
    requirement = obj(record.get("requirement"))
    add("requirement-placeholder-labelled", "FIXTURE PLACEHOLDER ONLY" in str(requirement.get("text", ""))
        and str(requirement.get("source_reference", "")).startswith("fixture://"),
        "requirement text and source reference are fixture-only")

    interpretations = obj(record.get("interpretations")); rtl = obj(record.get("reference_rtl"))
    a_interp = obj(interpretations.get("A")); a_rtl = obj(rtl.get("A"))
    add("interpretation-a-and-reference-a", bool(a_interp.get("text")) and bool(a_interp.get("rationale"))
        and str(a_rtl.get("path", "")).startswith("fixture://") and a_rtl.get("fixture_reference_only") is True,
        "Interpretation A and reference RTL A are non-executable fixture references")
    rtl_refs = [v.get("path") for v in rtl.values() if isinstance(v, dict) and v.get("path") is not None]
    add("all-rtl-paths-are-fixture-uris", all(isinstance(ref, str) and ref.startswith("fixture://") for ref in rtl_refs),
        "no runnable RTL artifact paths are present")

    b_interp = interpretations.get("B"); b_rtl = rtl.get("B")
    role_ok = False; role_detail = "unrecognized role"
    if expected_role == "unambiguous_control":
        c = obj(record.get("checker_negative_control"))
        role_ok = b_interp is None and b_rtl is None and c.get("role") == "formal_checker_negative_control" \
            and c.get("design_intent") == "INTENTIONALLY_WRONG_FOR_CHECKER_TEST" \
            and c.get("actual_formal_result") == "NOT_RUN" and c.get("fixture_reference_only") is True \
            and str(c.get("path", "")).startswith("fixture://")
        role_detail = "no interpretation B/RTL B; checker-negative implementation is separately labelled and unexecuted"
    elif expected_role == "ambiguity_candidate":
        b = obj(b_interp); brtl = obj(b_rtl)
        role_ok = bool(b.get("text")) and bool(b.get("rationale")) and str(brtl.get("path", "")).startswith("fixture://") and brtl.get("fixture_reference_only") is True
        role_detail = "A/B placeholders and RTL A/B exist; no plausibility or formal-distinction claim"
    elif expected_role == "negative_candidate":
        b = obj(b_interp); brtl = obj(b_rtl); rejection = obj(record.get("rejection_record"))
        role_ok = bool(b.get("text")) and bool(b.get("rationale")) and str(brtl.get("path", "")).startswith("fixture://") \
            and rejection.get("status") == "PLACEHOLDER_NOT_ADJUDICATED" \
            and rejection.get("reason_code") == "NOT_ADJUDICATED_FIXTURE_ONLY" \
            and str(rejection.get("evidence_reference", "")).startswith("fixture://")
        role_detail = "rejection fields are unadjudicated placeholders; no actual rejection is claimed"
    elif expected_role == "robustness_case":
        c = obj(record.get("checker_negative_control"))
        target = record.get("robustness_target")
        role_ok = isinstance(target, str) and target.startswith("FIXTURE_STRUCTURE_ONLY") \
            and c.get("role") == "robustness_negative_control" and c.get("actual_formal_result") == "NOT_RUN" \
            and c.get("fixture_reference_only") is True and str(c.get("path", "")).startswith("fixture://")
        role_detail = "robustness target and checker-negative implementation are separate from interpretations"
    add("role-specific-requirements", role_ok, role_detail)
    add("fixture-cannot-be-certified", cert.get("certified_ambiguous") is False and record.get("classification") is None
        and formal.get("result") == "NOT_RUN", "fixture remains uncertified and unexecuted")
    return checks

def audit_repo(repo_root: Path, commit: str | None = None) -> dict[str, Any]:
    root = repo_root.resolve()
    source_checks = []
    for rel, expected in PINNED_SOURCES.items():
        path = root / rel
        ok = path.is_file() and git_blob_sha(path) == expected
        source_checks.append(check("pinned-source:" + rel, ok,
            "matches inspected source object" if ok else "missing or changed; do not silently refresh baseline"))
    reports = []
    for role, rel in FIXTURE_PATHS.items():
        try:
            record = json.loads((root / rel).read_text(encoding="utf-8"))
            results = validate_fixture(record, role)
            reports.append({"path": str(rel), "fixture_id": record.get("fixture_id") if isinstance(record, dict) else None,
                "case_role": role, "checks": results,
                "passed": sum(c["status"] == "PASS" for c in results),
                "failed": sum(c["status"] == "FAIL" for c in results)})
        except (OSError, json.JSONDecodeError) as exc:
            reports.append({"path": str(rel), "fixture_id": None, "case_role": role,
                "checks": [check("fixture-readable", False, str(exc))], "passed": 0, "failed": 1})
    observed = {item["case_role"] for item in reports if item["fixture_id"]}
    role_check = check("fixture-role-set-complete", observed == EXPECTED_ROLES and len(reports) == len(EXPECTED_ROLES),
        "four distinct role fixtures found" if observed == EXPECTED_ROLES else "role set mismatch")
    all_checks = source_checks + [role_check] + [c for f in reports for c in f["checks"]]
    failed = sum(c["status"] == "FAIL" for c in all_checks)
    return {
        "audit_id": "FORMAL-AMBIG-RTL-C7-ROLE-AWARE-FIXTURES", "audit_version": "1.0",
        "audit_result": "PASS" if failed == 0 else "FAIL",
        "fixture_status": "SYNTHETIC_PROPOSAL_ONLY_NOT_BENCHMARK_CONTENT",
        "repo_commit": commit or "UNRECORDED",
        "source_checks": source_checks, "role_set_check": role_check,
        "fixture_count": len(reports), "fixture_reports": reports,
        "checks_total": len(all_checks), "checks_passed": len(all_checks)-failed, "checks_failed": failed,
        "required_roles": sorted(EXPECTED_ROLES),
        "explicit_nonclaims": [
            "Fixtures are examples for structural tests only; they are not real benchmark cases.",
            "No schema/template source or P01/P02/P05 case artifact was changed.",
            "No formal tools, human reviews or LLM evaluations were executed.",
            "No D2/D14 approval, template freeze, ambiguity certification or project completion is inferred."
        ]
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--commit", default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    report = audit_repo(args.repo_root, args.commit)
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if report["audit_result"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
