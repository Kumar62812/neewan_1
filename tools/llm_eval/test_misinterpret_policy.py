#!/usr/bin/env python3
"""D4 regression tests: only valid, formally evaluated class M can be MISINTERPRET."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from misinterpret_policy import classify_misinterpretation  # noqa: E402


BASE = {
    "generation_status": "received",
    "extraction_status": "rtl_extracted",
    "technical_failure_label": None,
    "compilation_status": "pass",
    "formal_comparison_complete": True,
    "behavioral_classification": "M",
    # Synthetic test fixture only. This is not a real approved D5 contract.
    "comparison_contract_ref": "fixture://synthetic-approved-contract",
    "comparison_contract_approved": True,
}


class D4MisinterpretPolicyTests(unittest.TestCase):
    def evaluate(self, **changes):
        args = dict(BASE)
        args.update(changes)
        return classify_misinterpretation(**args)

    def test_only_full_valid_class_m_evidence_assigns_misinterpret(self):
        label, reason = self.evaluate()
        self.assertEqual(label, "MISINTERPRET")
        self.assertIn("comparison contract is approved", reason)

    def test_class_a_is_not_misinterpret(self):
        self.assertIsNone(self.evaluate(behavioral_classification="A")[0])

    def test_class_b_is_not_misinterpret(self):
        self.assertIsNone(self.evaluate(behavioral_classification="B")[0])

    def test_class_ab_is_not_misinterpret(self):
        self.assertIsNone(self.evaluate(behavioral_classification="AB")[0])

    def test_missing_behavioral_class_is_not_misinterpret(self):
        self.assertIsNone(self.evaluate(behavioral_classification=None)[0])

    def test_invalid_rtl_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(technical_failure_label="INVALID")[0])

    def test_incomplete_response_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(
            extraction_status="truncated_module",
            technical_failure_label="INCOMPLETE",
        )[0])

    def test_inconclusive_formal_run_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(
            technical_failure_label="INCONCLUSIVE",
            formal_comparison_complete=False,
        )[0])

    def test_missing_rtl_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(extraction_status="format_failure")[0])

    def test_generation_timeout_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(generation_status="timeout")[0])

    def test_provider_error_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(generation_status="provider_error")[0])

    def test_compile_failure_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(compilation_status="nonzero_exit")[0])

    def test_compile_not_run_never_becomes_misinterpret(self):
        self.assertIsNone(self.evaluate(compilation_status="not_run")[0])

    def test_formal_comparison_must_be_explicitly_complete(self):
        self.assertIsNone(self.evaluate(formal_comparison_complete=False)[0])

    def test_unknown_formal_completion_value_fails_closed(self):
        self.assertIsNone(self.evaluate(formal_comparison_complete=None)[0])

    def test_contract_reference_is_required(self):
        self.assertIsNone(self.evaluate(comparison_contract_ref="")[0])
        self.assertIsNone(self.evaluate(comparison_contract_ref=None)[0])

    def test_comparison_contract_must_be_approved(self):
        label, reason = self.evaluate(comparison_contract_approved=False)
        self.assertIsNone(label)
        self.assertIn("not marked approved", reason)

    def test_unknown_behavioral_class_fails_closed(self):
        self.assertIsNone(self.evaluate(behavioral_classification="MISMATCH")[0])

    def test_technical_label_unknown_also_fails_closed(self):
        label, reason = self.evaluate(technical_failure_label="FAIL")
        self.assertIsNone(label)
        self.assertIn("fail closed", reason)

    def test_fixture_generation_does_not_receive_interaction_label(self):
        self.assertIsNone(self.evaluate(generation_status="fixture_only")[0])

    def test_unapproved_comparison_contract_blocks_real_scoring_during_d5_pending(self):
        # D5 is still pending. Synthetic unit fixtures may test the positive gate,
        # but no production case can assert an approved contract by implication.
        self.assertIsNone(self.evaluate(comparison_contract_approved=False)[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
