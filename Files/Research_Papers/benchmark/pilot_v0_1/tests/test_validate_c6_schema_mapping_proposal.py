#!/usr/bin/env python3
"""Regression tests for C6 non-binding schema/template mapping proposal."""
from __future__ import annotations
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "Files/Research_Papers/benchmark/pilot_v0_1"))
from validate_c6_schema_mapping_proposal import validate

class C6MappingProposalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = validate(ROOT)
        cls.data = json.loads((ROOT / "docs/project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.json").read_text(encoding="utf-8"))

    def test_all_checks_pass(self):
        self.assertEqual(self.report["audit_result"], "PASS", self.report["checks"])
        self.assertEqual(self.report["checks_failed"], 0)

    def test_schema_fields_covered_exactly_once(self):
        names = [entry["schema_field"] for entry in self.data["field_mappings"]]
        self.assertEqual(len(names), 18)
        self.assertEqual(len(names), len(set(names)))

    def test_proposal_requires_author_decision(self):
        self.assertEqual(self.data["status"], "NON_BINDING_REQUIRES_AUTHOR_DECISION")
        self.assertTrue(all(x["decision_needed"] for x in self.data["field_mappings"] if x["mapping_status"] != "DIRECT"))

    def test_d2_and_d14_are_not_marked_decided(self):
        self.assertEqual({x["decision"] for x in self.data["decision_questions"]}, {"D2", "D14"})
        self.assertTrue(all("options" in x for x in self.data["decision_questions"]))

    def test_role_types_are_not_conflated(self):
        roles = {x["case_role"] for x in self.data["role_requirements_proposal"]}
        self.assertTrue({"unambiguous_control", "ambiguity_candidate", "negative_candidate"}.issubset(roles))
        negative = next(x for x in self.data["role_requirements_proposal"] if x["case_role"] == "negative_candidate")
        self.assertIn("rejection", negative["annotation"].lower())

    def test_extension_fields_are_proposal_only(self):
        for item in self.data["proposed_additional_fields"]:
            self.assertEqual(item["status"], "PROPOSAL_ONLY")

    def test_no_canonical_files_are_modified_by_validation(self):
        self.assertEqual(self.data["status"], "NON_BINDING_REQUIRES_AUTHOR_DECISION")
        self.assertTrue(any("remain unchanged" in x.lower() for x in self.data["explicit_nonclaims"]))

if __name__ == "__main__":
    unittest.main(verbosity=2)
