#!/usr/bin/env python3
"""Traceable LLM-to-RTL runner with explicit D3 technical-failure labels.

Fixture mode is for infrastructure tests only. It does not call a model and its
results must never be reported as model-performance evidence.

D3 labels describe technical failure only:
- INVALID: evidence shows RTL/model parse, elaboration, or compile invalidity.
- INCOMPLETE: required response/RTL content is absent or truncated.
- INCONCLUSIVE: the tool/formal attempt could not provide a defensible result.
A completed formal check is left for the separate A/B/AB/M classification stage.
This module never assigns M.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

D3_LABELS = {"INVALID", "INCOMPLETE", "INCONCLUSIVE"}

# Match common parser/elaborator diagnostics, not arbitrary nonzero exit codes.
INVALID_RTL_DIAGNOSTIC = re.compile(
    r"(?:syntax\s+error|parse\s+error|unexpected\s+token|"
    r"failed\s+to\s+parse|unknown\s+module\s+type|"
    r"(?:top\s+)?module\s+[^\n]*not\s+found|"
    r"unable\s+to\s+bind|cannot\s+find\s+module|can't\s+find\s+module|"
    r"elaboration\s+(?:failed|error)|failed\s+to\s+elaborate|"
    r"port\s+[^\n]*not\s+found)",
    re.IGNORECASE,
)
TOOL_FAILURE_DIAGNOSTIC = re.compile(
    r"(?:segmentation\s+fault|segfault|core\s+dumped|"
    r"internal\s+error|assertion\s+failed|out\s+of\s+memory|"
    r"fatal\s+tool\s+error|compiler\s+crash|tool\s+crash|"
    r"process\s+was\s+killed|panic:)",
    re.IGNORECASE,
)
FORMAL_RESULT_MARKER = re.compile(
    r"^\s*FORMAL_RESULT\s*=\s*(PASS|COUNTEREXAMPLE|INVALID|INCONCLUSIVE)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _text(value: Any) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return "" if value is None else str(value)


def _result_text(result: dict[str, Any] | None) -> str:
    if not result:
        return ""
    return _text(result.get("stdout")) + "\n" + _text(result.get("stderr"))


def run_cmd(command: str, timeout: int, rtl: Path, cwd: Path) -> dict[str, Any]:
    """Execute a configured command without equating every nonzero exit with a proof failure."""
    if not command:
        return {
            "status": "not_run", "command": None, "exit_code": None,
            "stdout": "", "stderr": "",
        }
    argv = [part.replace("{rtl}", str(rtl.resolve())) for part in shlex.split(command)]
    try:
        p = subprocess.run(
            argv, cwd=cwd, capture_output=True, text=True, timeout=timeout, check=False
        )
        if p.returncode == 0:
            status = "pass"
        elif p.returncode < 0:
            status = "tool_crash"
        else:
            status = "nonzero_exit"
        return {
            "status": status, "command": argv, "exit_code": p.returncode,
            "stdout": p.stdout, "stderr": p.stderr,
        }
    except subprocess.TimeoutExpired as e:
        return {
            "status": "timeout", "command": argv, "exit_code": None,
            "stdout": _text(e.stdout), "stderr": _text(e.stderr),
        }
    except OSError as e:
        return {
            "status": "tool_error", "command": argv, "exit_code": None,
            "stdout": "", "stderr": str(e),
        }


def extract_rtl(raw: str) -> tuple[str, str]:
    """Return extracted RTL and a generation/extraction class, preserving failure reasons."""
    blocks = re.findall(
        r"```(?:systemverilog|verilog|sv)?\s*\n(.*?)```",
        raw, flags=re.I | re.S,
    )
    candidates = blocks or [raw]
    for candidate in candidates:
        has_module = bool(re.search(r"\bmodule\b", candidate))
        has_endmodule = bool(re.search(r"\bendmodule\b", candidate))
        if has_module and has_endmodule:
            return candidate.strip() + "\n", "rtl_extracted"
        if has_module and not has_endmodule:
            return "", "truncated_module"
    if not raw.strip():
        return "", "empty_response"
    if re.search(r"\b(?:clarify|could you specify|need more information|what should)\b", raw, re.I):
        return "", "clarification_requested"
    if re.search(r"\b(?:cannot help|can't help|unable to provide)\b", raw, re.I):
        return "", "refusal"
    return "", "format_failure"


def classify_technical_failure(
    extraction_status: str,
    generation: dict[str, Any],
    compilation: dict[str, Any] | None,
    formal: dict[str, Any] | None,
) -> tuple[str | None, str]:
    """Return (D3 label or None, reason); None means D3 is not a behavioral class.

    A nonzero formal exit is only treated as a completed counterexample if the
    adapter emits a standalone 'FORMAL_RESULT=COUNTEREXAMPLE' marker. Otherwise
    it is INCONCLUSIVE. This avoids mapping tool errors to M or to a proven mismatch.
    """
    gen_status = str((generation or {}).get("status", "unknown")).lower()
    if gen_status in {"timeout", "provider_error", "tool_error", "tool_crash"}:
        return "INCONCLUSIVE", f"Generation/adapter did not provide a dependable completed response ({gen_status})."

    if extraction_status != "rtl_extracted":
        return "INCOMPLETE", (
            f"Required RTL content was absent or incomplete at extraction "
            f"(extraction_status={extraction_status})."
        )

    comp_status = str((compilation or {}).get("status", "not_run")).lower()
    comp_text = _result_text(compilation)
    if comp_status == "pass":
        pass
    elif comp_status in {"timeout", "tool_error", "tool_crash", "not_run"}:
        return "INCONCLUSIVE", f"Compilation could not produce a dependable result ({comp_status})."
    elif comp_status == "nonzero_exit":
        if TOOL_FAILURE_DIAGNOSTIC.search(comp_text):
            return "INCONCLUSIVE", "Compiler/tool diagnostics indicate an infrastructure or tool failure."
        if INVALID_RTL_DIAGNOSTIC.search(comp_text):
            return "INVALID", "Compiler diagnostics identify a parse, compile, or elaboration error."
        return "INCONCLUSIVE", (
            "Compilation exited nonzero without a recognized RTL-invalidity diagnostic; "
            "the exit is not assumed to be a design error."
        )
    else:
        return "INCONCLUSIVE", f"Unrecognized compilation result status: {comp_status}."

    form_status = str((formal or {}).get("status", "not_run")).lower()
    form_text = _result_text(formal)
    markers = FORMAL_RESULT_MARKER.findall(form_text)
    marker = markers[-1].upper() if markers else None

    if marker == "INVALID":
        return "INVALID", "Formal adapter explicitly marked the formal model INVALID."
    if marker == "INCONCLUSIVE":
        return "INCONCLUSIVE", "Formal adapter explicitly marked the comparison INCONCLUSIVE."
    if marker == "COUNTEREXAMPLE":
        return None, (
            "Formal adapter explicitly reported a completed counterexample. "
            "Retain it for the later behavioral-classification stage; do not label it M here."
        )
    if marker == "PASS":
        if form_status == "pass":
            return None, (
                "Formal command completed successfully. No D3 technical-failure label applies; "
                "behavioral classification is a separate stage."
            )
        return "INCONCLUSIVE", (
            "Formal adapter marked PASS but the process exited nonzero; conflicting evidence."
        )

    if form_status == "pass":
        return None, (
            "Formal command completed with exit code 0. No D3 technical-failure label applies; "
            "behavioral classification is a separate stage."
        )
    if form_status in {"timeout", "tool_error", "tool_crash", "not_run", "unknown"}:
        return "INCONCLUSIVE", f"Formal comparison did not complete dependably ({form_status})."
    if form_status == "nonzero_exit":
        if TOOL_FAILURE_DIAGNOSTIC.search(form_text):
            return "INCONCLUSIVE", "Formal tool diagnostics indicate a tool/runtime failure."
        return "INCONCLUSIVE", (
            "Formal command exited nonzero without a recognized FORMAL_RESULT marker; "
            "a proof/counterexample result cannot be distinguished from tool failure."
        )
    return "INCONCLUSIVE", f"Unrecognized formal result status: {form_status}."


def main() -> int:
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
            generation = {
                "status": "received" if p.returncode == 0 else "provider_error",
                "command": argv, "exit_code": p.returncode, "stderr": p.stderr,
            }
        except subprocess.TimeoutExpired as e:
            raw = ""
            generation = {
                "status": "timeout", "command": argv, "exit_code": None,
                "stderr": _text(e.stderr),
            }
        except OSError as e:
            raw = ""
            generation = {
                "status": "tool_error", "command": argv, "exit_code": None,
                "stderr": str(e),
            }
    else:
        (out / "ERROR.txt").write_text("Provide --fixture-response or --model-command.\n")
        raise SystemExit("No response source configured; run directory records the setup error.")

    (out / "raw_response.txt").write_text(raw, encoding="utf-8")
    rtl, extraction_status = extract_rtl(raw)
    (out / "extracted_rtl.sv").write_text(rtl, encoding="utf-8")
    compile_result = run_cmd(
        args.compile_command, args.compile_timeout, out / "extracted_rtl.sv", out
    )
    if compile_result["status"] == "pass":
        formal_result = run_cmd(
            args.formal_command, args.formal_timeout, out / "extracted_rtl.sv", out
        )
    else:
        formal_result = {
            "status": "not_run", "reason": f"compile did not complete successfully ({compile_result['status']})",
            "command": None, "exit_code": None, "stdout": "", "stderr": "",
        }

    for name, result in (("compile", compile_result), ("formal", formal_result)):
        (out / f"{name}.stdout.txt").write_text(_text(result.get("stdout")), encoding="utf-8")
        (out / f"{name}.stderr.txt").write_text(_text(result.get("stderr")), encoding="utf-8")

    technical_label, technical_reason = classify_technical_failure(
        extraction_status, generation, compile_result, formal_result
    )

    files = {}
    for p in sorted(out.iterdir()):
        if p.is_file() and p.name not in {"manifest.json", "summary.json"}:
            files[p.name] = {"sha256": sha256(p), "bytes": p.stat().st_size}
    summary = {
        "schema_version": "0.2-d3-candidate",
        "run_id": args.run_id,
        "case": args.case,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "classification": extraction_status,
        "generation": generation,
        "compilation": compile_result["status"],
        "formal": formal_result["status"],
        "technical_failure_label": technical_label,
        "technical_failure_reason": technical_reason,
        "behavioral_classification": None,
        "pipeline_test_only": bool(fixture),
        "note": (
            "Fixture runs are infrastructure tests, not model evaluation evidence. "
            "D3 technical failure labels never assign M; behavior classification is separate."
            if fixture else
            "Preserve provider/model/version metadata alongside this run. "
            "Do not use for primary scored results until governance and protocol gates are approved."
        ),
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    manifest = {"schema_version": "0.2-d3-candidate", "summary": "summary.json", "files": files}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"run_dir": str(out), "summary": summary, "manifest": "manifest.json"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
