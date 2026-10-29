#!/usr/bin/env python3
"""Regression tests for the read-only C5 template readiness audit."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

PILOT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PILOT_ROOT))
from audit_c5_template_readiness import audit_repo


class C5TemplateReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo_root = Path(__file__).resolve().parents[5]
        cls.report = audit_repo(cls.repo_root, "test-snapshot")

    def test_source_observations_validate_cleanly(self):
        self.assertEqual(self.report["audit_result"], "PASS", self.report["checks"])
        self.assertEqual(self.report["failed_checks"], 0)

    def test_template_stays_blocked_not_frozen(self):
        self.assertEqual(self.report["template_readiness"], "BLOCKED_NOT_FROZEN")
        self.assertTrue(self.report["source_facts"]["p01_not_frozen"])
        self.assertTrue(self.report["source_facts"]["d2_d14_pending"])

    def test_schema_mapping_gaps_are_explicit(self):
        gaps = self.report["source_facts"]["schema_template_mapping_gaps"]
        schema_fields = {item["schema_field"] for item in gaps}
        self.assertIn("category", schema_fields)
        self.assertIn("annotation_record", schema_fields)
        self.assertIn("version", schema_fields)

    def test_negative_control_is_not_interpretation_b(self):
        self.assertTrue(self.report["source_facts"]["p01_negative_control_role_distinguished"])

    def test_formal_distinction_does_not_imply_human_certification(self):
        self.assertTrue(self.report["source_facts"]["formal_human_boundary_present"])
        self.assertGreaterEqual(len(self.report["open_blockers"]), 4)

    def test_audit_does_not_claim_side_effects(self):
        claims = self.report["explicit_nonclaims"]
        self.assertTrue(any("No schema/template was changed or frozen." in item for item in claims))
        self.assertTrue(any("No formal tool was executed." in item for item in claims))
        self.assertTrue(any("does not infer an official T1-T31" in item for item in claims))


if __name__ == "__main__":
    unittest.main(verbosity=2)
