#!/usr/bin/env python3
"""Standard-library regression tests for the C3 formal-reproduction validator."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_formal_reproduction import validate_expected_statuses, validate_manifest_dir

class FormalReproductionValidatorTests(unittest.TestCase):
    def make_manifest(self, root):
        payload = root / "sample.log"
        payload.write_text("stable fixture\n", encoding="utf-8")
        digest = hashlib.sha256(payload.read_bytes()).hexdigest()
        (root / "SHA256SUMS.json").write_text(
            json.dumps({"sample.log": digest}, indent=2) + "\n", encoding="utf-8")
        return root

    def test_valid_manifest_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            checks = validate_manifest_dir(self.make_manifest(Path(temp)))
            self.assertTrue(checks)
            self.assertTrue(all(c["status"] == "PASS" for c in checks))

    def test_mutated_manifested_file_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.make_manifest(Path(temp))
            (root / "sample.log").write_text("mutated fixture\n", encoding="utf-8")
            checks = validate_manifest_dir(root)
            outcome = next(c for c in checks if c["check"].endswith(":manifest-sha256"))
            self.assertEqual(outcome["status"], "FAIL")

    def test_expected_negative_control_failures_are_accepted(self):
        statuses = {"reference-bmc":"PASS", "reference-induction":"PASS",
                    "reference-cover":"PASS", "wrong-bmc":"FAIL", "async-bmc":"FAIL"}
        rows = [{"name":n, "status":s, "returncode":0 if s=="PASS" else 1} for n,s in statuses.items()]
        self.assertTrue(all(c["status"]=="PASS" for c in validate_expected_statuses("P02", rows)))

    def test_wrong_negative_control_outcome_is_detected(self):
        rows = [{"name":"reference-bmc","status":"PASS","returncode":0},
                {"name":"reference-induction","status":"PASS","returncode":0},
                {"name":"reference-cover","status":"PASS","returncode":0},
                {"name":"wrong-bmc","status":"PASS","returncode":0},
                {"name":"async-bmc","status":"FAIL","returncode":1}]
        outcome = next(c for c in validate_expected_statuses("P02", rows)
                       if c["check"] == "P02:formal-outcomes")
        self.assertEqual(outcome["status"], "FAIL")

if __name__ == "__main__":
    unittest.main(verbosity=2)
