#!/usr/bin/env python3
"""Standard-library tests for C4 P05 review-input provenance validation."""
from __future__ import annotations
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_p05_review_input_bundle import (
    git_blob_sha1_bytes,
    sha256_bytes,
    validate_historical_form_boundary,
    validate_pinned_files,
)


class P05ReviewBundleTests(unittest.TestCase):
    def test_git_blob_hash_matches_git_object_convention(self):
        self.assertEqual(git_blob_sha1_bytes(b"abc"), "f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f")

    def test_sha256_matches_known_vector(self):
        self.assertEqual(sha256_bytes(b"abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_pinned_file_bytes_and_hashes_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            data = b"requirement v1\n"
            (root / "requirement.md").write_bytes(data)
            entry = {"path":"requirement.md","git_blob_sha1":git_blob_sha1_bytes(data),
                     "sha256":sha256_bytes(data),"bytes":len(data),"role":"reviewer_facing_requirement"}
            checks = validate_pinned_files(root, [entry])
            self.assertTrue(checks)
            self.assertTrue(all(c["status"] == "PASS" for c in checks))

    def test_mutated_pinned_input_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            old = b"requirement v1\n"
            (root / "requirement.md").write_bytes(old)
            entry = {"path":"requirement.md","git_blob_sha1":git_blob_sha1_bytes(old),
                     "sha256":sha256_bytes(old),"bytes":len(old),"role":"reviewer_facing_requirement"}
            (root / "requirement.md").write_bytes(b"requirement changed\n")
            checks = validate_pinned_files(root, [entry])
            self.assertEqual(sum(c["status"] == "FAIL" for c in checks), 3)

    def test_historical_form_must_remain_distinct_and_bound(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            current = b"current form v1\n"
            historical = b"historic captured form\n"
            (root / "current.md").write_bytes(current)
            (root / "run02").mkdir()
            (root / "run02/REVIEW_FORM.md").write_bytes(historical)
            (root / "run02/SHA256SUMS.json").write_text(
                json.dumps({"source/annotation/REVIEW_FORM.md":sha256_bytes(historical)}), encoding="utf-8")
            manifest = {
                "pinned_files":[{"role":"historical_run02_manifest","path":"run02/SHA256SUMS.json"}],
                "historical_form_boundary":{
                    "current_form_path":"current.md","current_form_git_blob_sha1":git_blob_sha1_bytes(current),
                    "current_form_sha256":sha256_bytes(current),"historical_run02_form_path":"run02/REVIEW_FORM.md",
                    "historical_run02_form_git_blob_sha1":git_blob_sha1_bytes(historical),
                    "historical_run02_form_sha256":sha256_bytes(historical)
                }
            }
            checks = validate_historical_form_boundary(root, manifest)
            self.assertTrue(all(c["status"] == "PASS" for c in checks))

    def test_same_current_and_historical_form_is_not_the_declared_boundary(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            data = b"identical form\n"
            (root / "current.md").write_bytes(data)
            (root / "historical.md").write_bytes(data)
            (root / "run02").mkdir()
            (root / "run02/SHA256SUMS.json").write_text(
                json.dumps({"source/annotation/REVIEW_FORM.md":sha256_bytes(data)}), encoding="utf-8")
            manifest = {
                "pinned_files":[{"role":"historical_run02_manifest","path":"run02/SHA256SUMS.json"}],
                "historical_form_boundary":{
                    "current_form_path":"current.md","current_form_git_blob_sha1":git_blob_sha1_bytes(data),
                    "current_form_sha256":sha256_bytes(data),"historical_run02_form_path":"historical.md",
                    "historical_run02_form_git_blob_sha1":git_blob_sha1_bytes(data),
                    "historical_run02_form_sha256":sha256_bytes(data)
                }
            }
            checks = validate_historical_form_boundary(root, manifest)
            outcome = next(c for c in checks if c["check"].endswith("forms-remain-distinct"))
            self.assertEqual(outcome["status"], "FAIL")


if __name__ == "__main__":
    unittest.main(verbosity=2)
