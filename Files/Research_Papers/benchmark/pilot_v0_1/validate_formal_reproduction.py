#!/usr/bin/env python3
"""Read-only validator for fresh P02/P05 Linux formal reproductions."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from typing import Any

PILOT = Path("Files/Research_Papers/benchmark/pilot_v0_1")
EXPECTED = {
    "P02": {"reference-bmc":"PASS", "reference-induction":"PASS", "reference-cover":"PASS",
            "wrong-bmc":"FAIL", "async-bmc":"FAIL"},
    "P05": {"reference-bmc":"PASS", "reference-induction":"PASS", "reference-cover":"PASS",
            "equality-bmc":"FAIL"},
}
# (label, case, source path relative to case, corresponding runner snapshot path)
SOURCE_PAIRS = [
    ("P02 requirement","P02","P02_REQUIREMENT.md","P02_REQUIREMENT.md"),
    ("P02 interpretation","P02","P02_INTERPRETATION.md","P02_INTERPRETATION.md"),
    ("P02 specification","P02","P02_SPECIFICATION.md","P02_SPECIFICATION.md"),
    ("P02 consistency review","P02","P02_CONSISTENCY_REVIEW.md","P02_CONSISTENCY_REVIEW.md"),
    ("P02 strategy","P02","formal/STRATEGY.md","formal/STRATEGY.md"),
    ("P02 harness","P02","formal/harness.sv","formal/harness.sv"),
    ("P02 properties","P02","formal/properties/register_properties.sv","formal/properties/register_properties.sv"),
    ("P02 runner","P02","formal/run.py","formal/run.py"),
    ("P02 reference RTL","P02","reference_rtl/register.sv","reference_rtl/register.sv"),
    ("P02 wrong-reset control","P02","validation_rtl/wrong_reset.sv","validation_rtl/wrong_reset.sv"),
    ("P02 async-reset control","P02","validation_rtl/wrong_async.sv","validation_rtl/wrong_async.sv"),
    ("P05 requirement","P05","P05_REQUIREMENT.md","P05_REQUIREMENT.md"),
    ("P05 interpretations","P05","P05_INTERPRETATIONS.md","P05_INTERPRETATIONS.md"),
    ("P05 specifications","P05","P05_SPECIFICATIONS.md","P05_SPECIFICATIONS.md"),
    ("P05 strategy","P05","formal/STRATEGY.md","formal/STRATEGY.md"),
    ("P05 harness","P05","formal/harness.sv","formal/harness.sv"),
    ("P05 B-state properties","P05","formal/b_properties.sv","formal/b_properties.sv"),
    ("P05 runner","P05","formal/run.py","formal/run.py"),
    ("P05 reference RTL","P05","reference_rtl/responses.sv","reference_rtl/responses.sv"),
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def add(checks: list[dict[str, str]], name: str, ok: bool, detail: str) -> None:
    checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})

def validate_manifest_dir(run_dir: Path) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    manifest_path = run_dir / "SHA256SUMS.json"
    if not manifest_path.is_file():
        add(checks, f"{run_dir.name}:manifest-present", False, "SHA256SUMS.json missing")
        return checks
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        add(checks, f"{run_dir.name}:manifest-json", False, str(exc))
        return checks
    schema_ok = isinstance(manifest, dict) and all(
        isinstance(p, str) and isinstance(d, str) and re.fullmatch(r"[0-9a-f]{64}", d)
        for p, d in manifest.items())
    add(checks, f"{run_dir.name}:manifest-schema", schema_ok,
        f"{len(manifest) if isinstance(manifest, dict) else 0} entries")
    if not schema_ok:
        return checks
    expected = set(manifest)
    actual = {p.relative_to(run_dir).as_posix() for p in run_dir.rglob("*")
              if p.is_file() and p != manifest_path}
    add(checks, f"{run_dir.name}:manifest-inventory", expected == actual,
        f"listed={len(expected)}, actual={len(actual)}, missing={sorted(expected-actual)}, unlisted={sorted(actual-expected)}")
    bad = []
    for rel, digest in manifest.items():
        path = run_dir / rel
        if Path(rel).is_absolute() or ".." in Path(rel).parts or not path.is_file() or sha256(path) != digest:
            bad.append(rel)
    add(checks, f"{run_dir.name}:manifest-sha256", not bad,
        f"{len(expected)-len(bad)}/{len(expected)} file hashes match" + (f"; mismatches={bad}" if bad else ""))
    return checks

def validate_expected_statuses(case: str, rows: Any) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        add(checks, f"{case}:runs-json-schema", False, "runs.json must be a list of objects")
        return checks
    names = [r.get("name") for r in rows]
    duplicates = sorted({n for n in names if names.count(n) > 1})
    add(checks, f"{case}:unique-run-names", not duplicates,
        f"duplicates={duplicates}" if duplicates else "all names unique")
    by_name = {r.get("name"): r for r in rows}
    missing, wrong = [], []
    for name, expected in EXPECTED[case].items():
        row = by_name.get(name)
        if row is None:
            missing.append(name)
            continue
        rc_expected = 0 if expected == "PASS" else 1
        if row.get("status") != expected or row.get("returncode") != rc_expected:
            wrong.append(f"{name}: expected {expected}/rc={rc_expected}, got {row.get('status')}/rc={row.get('returncode')}")
    add(checks, f"{case}:formal-outcomes", not missing and not wrong,
        f"{len(EXPECTED[case])-len(missing)-len(wrong)}/{len(EXPECTED[case])} expected outcomes matched"
        + (f"; missing={missing}" if missing else "") + (f"; mismatches={wrong}" if wrong else ""))
    return checks

def validate_environment(case: str, run_dir: Path) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    try:
        env = json.loads((run_dir / "environment.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        add(checks, f"{case}:environment-json", False, str(exc))
        return checks
    platform = str(env.get("platform", ""))
    python = str(env.get("python", ""))
    commit = str(env.get("base_commit", ""))
    add(checks, f"{case}:linux-environment", "linux" in platform.lower(), platform or "platform missing")
    add(checks, f"{case}:python-version", python.startswith("3.12."), f"Python {python or 'UNKNOWN'}; expected 3.12.x")
    add(checks, f"{case}:base-commit", re.fullmatch(r"[0-9a-f]{40}", commit) is not None, commit or "missing")
    for filename, token, label in [
        ("yosys-version.log","0.63","Yosys 0.63"), ("solver-version.log","4.15.4","Z3 4.15.4")]:
        p = run_dir / filename
        content = p.read_text(encoding="utf-8", errors="replace") if p.is_file() else ""
        add(checks, f"{case}:{label}", token in content,
            (content.strip().splitlines()[0] if content.strip() else f"{filename} missing")[:240])
    return checks

def validate_source_alignment(repo_root: Path, run_dirs: dict[str, Path]) -> list[dict[str, str]]:
    errors = []
    for label, case, source_rel, snapshot_rel in SOURCE_PAIRS:
        case_root = repo_root / PILOT / case
        current = case_root / source_rel
        fresh = run_dirs[case] / "source" / snapshot_rel
        historic = case_root / "evidence" / "run-02" / "source" / snapshot_rel
        if not current.is_file() or not fresh.is_file() or not historic.is_file():
            errors.append(f"{label}: missing current/new-run/run-02 file")
            continue
        hashes = (sha256(current), sha256(fresh), sha256(historic))
        if len(set(hashes)) != 1:
            errors.append(f"{label}: current/new-run/run-02 SHA-256 values differ: {hashes}")
    checks: list[dict[str, str]] = []
    add(checks, "source-snapshot-alignment", not errors,
        f"{len(SOURCE_PAIRS)-len(errors)}/{len(SOURCE_PAIRS)} current/run-03/run-02 files byte-identical"
        + (f"; discrepancies={errors}" if errors else ""))
    return checks

def audit(repo_root: Path, p02_dir: Path, p05_dir: Path, exit_codes_path: Path) -> dict[str, Any]:
    checks: list[dict[str, str]] = []
    run_dirs = {"P02": p02_dir, "P05": p05_dir}
    for case, run_dir in run_dirs.items():
        checks.extend(validate_manifest_dir(run_dir))
        try:
            rows = json.loads((run_dir / "runs.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            rows = None
            add(checks, f"{case}:runs-json", False, str(exc))
        checks.extend(validate_expected_statuses(case, rows))
        checks.extend(validate_environment(case, run_dir))
    checks.extend(validate_source_alignment(repo_root, run_dirs))
    try:
        codes = json.loads(exit_codes_path.read_text(encoding="utf-8"))
        ok = codes.get("P02") == 0 and codes.get("P05") == 0
        add(checks, "runner-exit-codes", ok, json.dumps(codes, sort_keys=True))
    except (OSError, json.JSONDecodeError, AttributeError) as exc:
        add(checks, "runner-exit-codes", False, str(exc))
    passed = sum(c["status"] == "PASS" for c in checks)
    failed = len(checks) - passed
    return {"schema_version":"1.0", "task":"C3_P02_P05_LINUX_FORMAL_REPRODUCTION",
            "read_only":True, "status":"PASS" if failed == 0 else "FAIL",
            "summary":{"checks":len(checks),"passed":passed,"failed":failed}, "checks":checks}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--p02-dir", type=Path, required=True)
    parser.add_argument("--p05-dir", type=Path, required=True)
    parser.add_argument("--exit-codes", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = audit(args.repo_root.resolve(), args.p02_dir.resolve(), args.p05_dir.resolve(), args.exit_codes.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status":result["status"], **result["summary"]}, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
