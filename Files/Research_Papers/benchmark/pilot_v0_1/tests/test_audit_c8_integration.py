#!/usr/bin/env python3
"""Regression tests for C8 cross-artifact integrity and role boundaries."""
from __future__ import annotations
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PILOT_ROOT = ROOT / "Files/Research_Papers/benchmark/pilot_v0_1"
sys.path.insert(0, str(PILOT_ROOT))
from audit_c8_integration import FIXTURES, audit_repo, validate_fixture

def load_fixture(role):
    return json.loads((ROOT / FIXTURES[role]).read_text(encoding="utf-8"))

class C8IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit_repo(ROOT, "test-c8-snapshot")

    def test_whole_c5_c7_bundle_is_consistent(self):
        self.assertEqual(self.report["audit_result"], "PASS", self.report)
        self.assertEqual(self.report["checks_failed"], 0)

    def test_all_pinned_source_objects_match(self):
        self.assertEqual(self.report["source_pin_total"], 16)
        self.assertEqual(self.report["source_pin_passed"], 16)

    def test_mapping_covers_all_schema_fields(self):
        self.assertEqual(self.report["schema_field_count"], 18)
        self.assertEqual(self.report["mapping_entry_count"], 18)

    def test_four_fixture_roles_are_present(self):
        self.assertEqual(self.report["fixture_count"], 4)
        self.assertEqual({x["case_role"] for x in self.report["fixture_reports"]}, {
            "unambiguous_control", "ambiguity_candidate", "negative_candidate", "robustness_case"
        })

    def test_control_does_not_invent_interpretation_b(self):
        c = load_fixture("unambiguous_control")
        self.assertIsNone(c["interpretations"]["B"])
        self.assertIsNone(c["reference_rtl"]["B"])
        self.assertFalse(any(x["status"] == "FAIL" for x in validate_fixture(c, "unambiguous_control")))

    def test_wrong_control_mutation_is_rejected(self):
        c = load_fixture("unambiguous_control")
        c["interpretations"]["B"] = copy.deepcopy(c["interpretations"]["A"])
        failed = {x["check"] for x in validate_fixture(c, "unambiguous_control") if x["status"] == "FAIL"}
        self.assertIn("role-specific-contract", failed)

    def test_ambiguity_candidate_requires_paired_b(self):
        c = load_fixture("ambiguity_candidate")
        self.assertFalse(any(x["status"] == "FAIL" for x in validate_fixture(c, "ambiguity_candidate")))
        c["reference_rtl"]["B"] = None
        failed = {x["check"] for x in validate_fixture(c, "ambiguity_candidate") if x["status"] == "FAIL"}
        self.assertIn("role-specific-contract", failed)

    def test_negative_candidate_requires_rejection_placeholder(self):
        c = load_fixture("negative_candidate")
        self.assertFalse(any(x["status"] == "FAIL" for x in validate_fixture(c, "negative_candidate")))
        c.pop("rejection_record")
        failed = {x["check"] for x in validate_fixture(c, "negative_candidate") if x["status"] == "FAIL"}
        self.assertIn("role-specific-contract", failed)

    def test_robustness_wrong_control_is_separate(self):
        c = load_fixture("robustness_case")
        self.assertIsNone(c["interpretations"]["B"])
        self.assertEqual(c["checker_negative_control"]["role"], "robustness_negative_control")
        self.assertFalse(any(x["status"] == "FAIL" for x in validate_fixture(c, "robustness_case")))

    def test_formal_or_certification_mutation_is_rejected(self):
        c = load_fixture("ambiguity_candidate")
        c["certification"]["certified_ambiguous"] = True
        failed = {x["check"] for x in validate_fixture(c, "ambiguity_candidate") if x["status"] == "FAIL"}
        self.assertIn("no-result-promotion", failed)

    def test_governance_gates_stay_open(self):
        self.assertEqual(self.report["governance"]["D2"], "OPEN")
        self.assertEqual(self.report["governance"]["D14"], "OPEN")
        self.assertEqual(self.report["integration_status"], "CONSISTENT_BUT_GOVERNANCE_BLOCKED")

if __name__ == "__main__":
    unittest.main(verbosity=2)
