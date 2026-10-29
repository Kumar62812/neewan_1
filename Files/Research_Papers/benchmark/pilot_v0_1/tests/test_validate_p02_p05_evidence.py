"""Regression tests for the read-only P02/P05 evidence validator."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import validate_p02_p05_evidence as validator  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class P02P05EvidenceValidatorTests(unittest.TestCase):
    def make_manifest_fixture(self, root: Path) -> tuple[Path, Path]:
        run_dir = root / "P02" / "evidence" / "run-02"
        run_dir.mkdir(parents=True)
        payload = run_dir / "sample.log"
        payload.write_text("retained result\n", encoding="utf-8")
        manifest = run_dir / "SHA256SUMS.json"
        manifest.write_text(json.dumps({"sample.log": sha256(payload)}, indent=2) + "\n",
                            encoding="utf-8")
        return payload, manifest

    def test_valid_sha256_manifest_passes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="c2-manifest-pass-") as tmp:
            root = Path(tmp)
            _, manifest = self.make_manifest_fixture(root)
            checks = validator.audit_hash_manifest(
                root, manifest.relative_to(root).as_posix(),
                validator.git_blob_sha(manifest),
            )
            self.assertTrue(checks)
            self.assertTrue(all(item["status"] == "PASS" for item in checks), checks)

    def test_mutated_artifact_is_detected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="c2-manifest-mutation-") as tmp:
            root = Path(tmp)
            payload, manifest = self.make_manifest_fixture(root)
            payload.write_text("modified result\n", encoding="utf-8")
            checks = validator.audit_hash_manifest(root, manifest.relative_to(root).as_posix())
            failures = [item for item in checks if item["status"] == "FAIL"]
            self.assertTrue(any(":sha256:sample.log" in item["check"] for item in failures), failures)

    def test_manifest_pin_detects_manifest_change(self) -> None:
        with tempfile.TemporaryDirectory(prefix="c2-manifest-pin-") as tmp:
            root = Path(tmp)
            _, manifest = self.make_manifest_fixture(root)
            pinned = validator.git_blob_sha(manifest)
            entries = json.loads(manifest.read_text(encoding="utf-8"))
            entries["review.txt"] = "0" * 64
            manifest.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
            checks = validator.audit_hash_manifest(root, manifest.relative_to(root).as_posix(), pinned)
            failures = [item for item in checks if item["status"] == "FAIL"]
            self.assertTrue(any(item["check"].endswith(":manifest-blob") for item in failures), failures)

    def test_source_pair_detects_snapshot_drift(self) -> None:
        with tempfile.TemporaryDirectory(prefix="c2-source-pair-") as tmp:
            root = Path(tmp)
            source = root / "source.md"
            snapshot = root / "run-02" / "source.md"
            snapshot.parent.mkdir(parents=True)
            source.write_text("original contract\n", encoding="utf-8")
            snapshot.write_text("original contract\n", encoding="utf-8")
            expected = validator.git_blob_sha(source)
            matched = validator.audit_source_pair(root, "fixture", "source.md", "run-02/source.md", expected)
            self.assertEqual(matched["status"], "PASS", matched)
            snapshot.write_text("changed contract\n", encoding="utf-8")
            changed = validator.audit_source_pair(root, "fixture", "source.md", "run-02/source.md", expected)
            self.assertEqual(changed["status"], "FAIL", changed)

if __name__ == "__main__":
    unittest.main(verbosity=2)
