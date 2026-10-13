#!/usr/bin/env python3
"""Traceable LLM-to-RTL pipeline harness.

Fixture mode is for infrastructure tests only. It does not call a model and its
results must never be reported as model-performance evidence.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shlex, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def run_cmd(command: str, timeout: int, rtl: Path, cwd: Path):
    if not command:
        return {"status": "not_run", "command": None, "exit_code": None}
    argv = [part.replace("{rtl}", str(rtl.resolve())) for part in shlex.split(command)]
    try:
        p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, check=False)
        return {"status": "pass" if p.returncode == 0 else "fail",
                "command": argv, "exit_code": p.returncode,
                "stdout": p.stdout, "stderr": p.stderr}
    except subprocess.TimeoutExpired as e:
        return {"status": "timeout", "command": argv, "exit_code": None,
                "stdout": e.stdout or "", "stderr": e.stderr or ""}

def extract_rtl(raw: str) -> tuple[str, str]:
    blocks = re.findall(r"```(?:systemverilog|verilog|sv)?\s*\n(.*?)```", raw,
                        flags=re.I | re.S)
    candidates = blocks or [raw]
    for candidate in candidates:
        if re.search(r"\bmodule\b", candidate) and re.search(r"\bendmodule\b", candidate):
            return candidate.strip() + "\n", "rtl_extracted"
    if not raw.strip():
        return "", "empty_response"
    if re.search(r"\b(?:clarify|could you specify|need more information|what should)\b", raw, re.I):
        return "", "clarification_requested"
    if re.search(r"\b(?:cannot help|can't help|unable to provide)\b", raw, re.I):
        return "", "refusal"
    return "", "format_failure"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--prompt-file", required=True, type=Path)
    ap.add_argument("--out-root", default="runs", type=Path)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--fixture-response", type=Path,
                    help="Use a saved fixture response; infrastructure testing only.")
    ap.add_argument("--model-command", default="",
                    help="Optional adapter command; stdout must be the raw response. Use {prompt} as argument placeholder.")
    ap.add_argument("--compile-command", default="")
    ap.add_argument("--formal-command", default="")
    ap.add_argument("--compile-timeout", type=int, default=30)
    ap.add_argument("--formal-timeout", type=int, default=120)
    args = ap.parse_args()

    out = args.out_root / args.run_id
    out.mkdir(parents=True, exist_ok=False)
    prompt = args.prompt_file.read_text(encoding="utf-8")
    (out / "prompt.txt").write_text(prompt, encoding="utf-8")
    fixture = args.fixture_response is not None
    if fixture:
        raw = args.fixture_response.read_text(encoding="utf-8")
        generation = {"status": "fixture_only", "command": None, "exit_code": 0}
    elif args.model_command:
        argv = [part.replace("{prompt}", str((out / "prompt.txt").resolve()))
                for part in shlex.split(args.model_command)]
        try:
            p = subprocess.run(argv, capture_output=True, text=True, timeout=120, check=False)
            raw = p.stdout
            generation = {"status": "received" if p.returncode == 0 else "provider_error",
                          "command": argv, "exit_code": p.returncode,
                          "stderr": p.stderr}
        except subprocess.TimeoutExpired as e:
            raw = ""
            generation = {"status": "timeout", "command": argv, "exit_code": None,
                          "stderr": str(e)}
    else:
        (out / "ERROR.txt").write_text("Provide --fixture-response or --model-command.\n")
        raise SystemExit("No response source configured; run directory records the setup error.")

    (out / "raw_response.txt").write_text(raw, encoding="utf-8")
    rtl, extraction_status = extract_rtl(raw)
    (out / "extracted_rtl.sv").write_text(rtl, encoding="utf-8")
    compile_result = run_cmd(args.compile_command, args.compile_timeout, out / "extracted_rtl.sv", out)
    formal_result = run_cmd(args.formal_command, args.formal_timeout, out / "extracted_rtl.sv", out) if compile_result["status"] == "pass" else {"status":"not_run","reason":"compile did not pass"}

    for name, result in (("compile", compile_result), ("formal", formal_result)):
        (out / f"{name}.stdout.txt").write_text(result.get("stdout", ""), encoding="utf-8")
        (out / f"{name}.stderr.txt").write_text(result.get("stderr", ""), encoding="utf-8")

    files = {}
    for p in sorted(out.iterdir()):
        if p.is_file() and p.name not in {"manifest.json", "summary.json"}:
            files[p.name] = {"sha256": sha256(p), "bytes": p.stat().st_size}
    summary = {
        "run_id": args.run_id, "case": args.case,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "classification": extraction_status, "generation": generation,
        "compilation": compile_result["status"], "formal": formal_result["status"],
        "pipeline_test_only": bool(fixture),
        "note": "Fixture runs are infrastructure tests, not model evaluation evidence." if fixture else "Preserve provider/model/version metadata alongside this run.",
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    manifest = {"schema_version":"0.1", "summary":"summary.json", "files":files}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"run_dir":str(out), "summary":summary, "manifest":"manifest.json"}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
