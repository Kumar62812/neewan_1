#!/usr/bin/env python3
"""D3 regression tests for technical failure labels; no model or RTL tools required."""
from __future__ import annotations

import os
import signal
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_pipeline import classify_technical_failure, extract_rtl, run_cmd  # noqa: E402

VALID_RTL = "module mux2(input logic a, input logic b, input logic sel, output logic y); assign y = sel ? b : a; endmodule\n"
GENERATION = {"status": "fixture_only"}
PASS = {"status": "pass", "exit_code": 0, "stdout": "", "stderr": ""}
NOT_RUN = {"status": "not_run", "exit_code": None, "stdout": "", "stderr": ""}


class D3OutcomeTests(unittest.TestCase):
    def evaluate(self, raw, compilation=None, formal=None, generation=None):
        _, extraction_status = extract_rtl(raw)
        label, reason = classify_technical_failure(
            extraction_status,
            generation or GENERATION,
            compilation if compilation is not None else PASS,
            formal if formal is not None else PASS,
        )
        return extraction_status, label, reason

    def test_empty_received_response_is_incomplete(self):
        extraction, label, _ = self.evaluate("")
        self.assertEqual(extraction, "empty_response")
        self.assertEqual(label, "INCOMPLETE")

    def test_truncated_module_is_incomplete_not_invalid(self):
        extraction, label, _ = self.evaluate("module mux2(input logic a;")
        self.assertEqual(extraction, "truncated_module")
        self.assertEqual(label, "INCOMPLETE")

    def test_clarification_without_rtl_is_incomplete_but_class_remains_visible(self):
        extraction, label, _ = self.evaluate("Could you specify reset polarity?")
        self.assertEqual(extraction, "clarification_requested")
        self.assertEqual(label, "INCOMPLETE")

    def test_syntax_diagnostic_is_invalid(self):
        compile_result = {
            "status": "nonzero_exit", "exit_code": 1,
            "stdout": "", "stderr": "syntax error: unexpected token",
        }
        _, label, _ = self.evaluate(VALID_RTL, compilation=compile_result)
        self.assertEqual(label, "INVALID")

    def test_elaboration_diagnostic_is_invalid(self):
        compile_result = {
            "status": "nonzero_exit", "exit_code": 1,
            "stdout": "", "stderr": "Unknown module type: missing_child",
        }
        _, label, _ = self.evaluate(VALID_RTL, compilation=compile_result)
        self.assertEqual(label, "INVALID")

    def test_unknown_compile_nonzero_is_inconclusive_not_assumed_invalid(self):
        compile_result = {
            "status": "nonzero_exit", "exit_code": 2,
            "stdout": "", "stderr": "unexpected driver termination",
        }
        _, label, _ = self.evaluate(VALID_RTL, compilation=compile_result)
        self.assertEqual(label, "INCONCLUSIVE")

    def test_forced_command_timeout_is_inconclusive(self):
        result = run_cmd(
            f'{sys.executable} -c "import time; time.sleep(2)"',
            0.05, Path("unused.sv"), Path.cwd(),
        )
        self.assertEqual(result["status"], "timeout")
        _, label, _ = self.evaluate(VALID_RTL, compilation=result)
        self.assertEqual(label, "INCONCLUSIVE")

    def test_missing_tool_is_inconclusive(self):
        result = run_cmd("__d3_missing_tool_which_must_not_exist__", 1, Path("unused.sv"), Path.cwd())
        self.assertEqual(result["status"], "tool_error")
        _, label, _ = self.evaluate(VALID_RTL, compilation=result)
        self.assertEqual(label, "INCONCLUSIVE")

    @unittest.skipUnless(os.name == "posix", "signal-based process-crash fixture requires POSIX")
    def test_tool_crash_is_inconclusive(self):
        command = f'{sys.executable} -c "import os,signal; os.kill(os.getpid(), signal.SIGTERM)"'
        result = run_cmd(command, 2, Path("unused.sv"), Path.cwd())
        self.assertEqual(result["status"], "tool_crash")
        _, label, _ = self.evaluate(VALID_RTL, compilation=result)
        self.assertEqual(label, "INCONCLUSIVE")

    def test_formal_timeout_is_inconclusive(self):
        formal = {"status": "timeout", "exit_code": None, "stdout": "", "stderr": ""}
        _, label, _ = self.evaluate(VALID_RTL, compilation=PASS, formal=formal)
        self.assertEqual(label, "INCONCLUSIVE")

    def test_formal_nonzero_without_explicit_result_marker_is_inconclusive(self):
        formal = {
            "status": "nonzero_exit", "exit_code": 1,
            "stdout": "", "stderr": "tool returned 1",
        }
        _, label, reason = self.evaluate(VALID_RTL, compilation=PASS, formal=formal)
        self.assertEqual(label, "INCONCLUSIVE")
        self.assertIn("cannot be distinguished", reason)

    def test_explicit_counterexample_is_not_invalid_or_m(self):
        formal = {
            "status": "nonzero_exit", "exit_code": 1,
            "stdout": "FORMAL_RESULT=COUNTEREXAMPLE\n", "stderr": "",
        }
        _, label, reason = self.evaluate(VALID_RTL, compilation=PASS, formal=formal)
        self.assertIsNone(label)
        self.assertIn("behavioral-classification", reason)
        self.assertNotIn("\bM\b", reason)

    def test_explicit_formal_model_invalid_is_invalid(self):
        formal = {
            "status": "nonzero_exit", "exit_code": 1,
            "stdout": "FORMAL_RESULT=INVALID\n", "stderr": "",
        }
        _, label, _ = self.evaluate(VALID_RTL, compilation=PASS, formal=formal)
        self.assertEqual(label, "INVALID")

    def test_formal_tool_crash_diagnostics_are_inconclusive(self):
        formal = {
            "status": "nonzero_exit", "exit_code": 2,
            "stdout": "", "stderr": "Internal error: segmentation fault",
        }
        _, label, _ = self.evaluate(VALID_RTL, compilation=PASS, formal=formal)
        self.assertEqual(label, "INCONCLUSIVE")

    def test_complete_formal_command_has_no_d3_failure_label(self):
        _, label, reason = self.evaluate(VALID_RTL, compilation=PASS, formal=PASS)
        self.assertIsNone(label)
        self.assertIn("behavioral classification is a separate stage", reason)


if __name__ == "__main__":
    unittest.main(verbosity=2)
