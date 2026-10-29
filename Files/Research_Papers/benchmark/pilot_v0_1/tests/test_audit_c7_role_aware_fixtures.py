#!/usr/bin/env python3
"""Regression tests for C7 role-aware synthetic fixtures."""
from __future__ import annotations
import copy, json, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PILOT_ROOT = ROOT / "Files/Research_Papers/benchmark/pilot_v0_1"
sys.path.insert(0, str(PILOT_ROOT))
from audit_c7_role_aware_fixtures import FIXTURE_PATHS, audit_repo, validate_fixture

def load_fixture(role):
    return json.loads((ROOT / FIXTURE_PATHS[role]).read_text(encoding="utf-8"))

class C7RoleAwareFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit_repo(ROOT, "test-fixture-snapshot")

    def test_all_fixtures_pass_audit(self):
        self.assertEqual(self.report["audit_result"], "PASS", self.report)
        self.assertEqual(self.report["checks_failed"], 0)

    def test_four_distinct_roles_are_covered(self):
        self.assertEqual(self.report["fixture_count"], 4)
        self.assertEqual(set(self.report["required_roles"]), {"unambiguous_control","ambiguity_candidate","negative_candidate","robustness_case"})

    def test_control_does_not_need_interpretation_b(self):
        c=load_fixture("unambiguous_control")
        self.assertIsNone(c["interpretations"]["B"]); self.assertIsNone(c["reference_rtl"]["B"])
        self.assertFalse(any(x["status"]=="FAIL" for x in validate_fixture(c,"unambiguous_control")))

    def test_control_rejects_wrong_rtl_mislabelled_as_interpretation_b(self):
        c=load_fixture("unambiguous_control"); c["interpretations"]["B"]=copy.deepcopy(c["interpretations"]["A"])
        failures={x["check"] for x in validate_fixture(c,"unambiguous_control") if x["status"]=="FAIL"}
        self.assertIn("role-specific-requirements",failures)

    def test_ambiguity_candidate_requires_a_and_b(self):
        c=load_fixture("ambiguity_candidate")
        self.assertFalse(any(x["status"]=="FAIL" for x in validate_fixture(c,"ambiguity_candidate")))
        c["reference_rtl"]["B"]=None
        failures={x["check"] for x in validate_fixture(c,"ambiguity_candidate") if x["status"]=="FAIL"}
        self.assertIn("role-specific-requirements",failures)

    def test_negative_candidate_requires_unadjudicated_rejection_record(self):
        c=load_fixture("negative_candidate")
        self.assertFalse(any(x["status"]=="FAIL" for x in validate_fixture(c,"negative_candidate")))
        c.pop("rejection_record")
        failures={x["check"] for x in validate_fixture(c,"negative_candidate") if x["status"]=="FAIL"}
        self.assertIn("role-specific-requirements",failures)

    def test_robustness_negative_control_is_separate(self):
        c=load_fixture("robustness_case")
        self.assertIsNone(c["interpretations"]["B"])
        self.assertEqual(c["checker_negative_control"]["role"],"robustness_negative_control")
        self.assertFalse(any(x["status"]=="FAIL" for x in validate_fixture(c,"robustness_case")))

    def test_fixture_cannot_claim_formal_or_human_certification(self):
        c=load_fixture("ambiguity_candidate"); c["certification"]["certified_ambiguous"]=True
        failures={x["check"] for x in validate_fixture(c,"ambiguity_candidate") if x["status"]=="FAIL"}
        self.assertIn("no-formal-or-human-outcome",failures)
        self.assertIn("fixture-cannot-be-certified",failures)

    def test_paths_are_fixture_uris_not_runnable_sources(self):
        for role in FIXTURE_PATHS:
            for item in load_fixture(role)["reference_rtl"].values():
                if item is not None:
                    self.assertTrue(item["path"].startswith("fixture://"))
                    self.assertTrue(item["fixture_reference_only"])

    def test_provenance_never_claims_a_canonical_case(self):
        for role in FIXTURE_PATHS:
            c=load_fixture(role)
            self.assertIsNone(c["provenance"]["canonical_case_path"])
            self.assertIsNone(c["provenance"]["source_commit"])
            self.assertTrue(c["fixture_context"]["not_a_real_benchmark_case"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
