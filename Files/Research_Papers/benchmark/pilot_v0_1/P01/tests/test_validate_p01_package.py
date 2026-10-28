"""Regression tests for the read-only P01 package validator.

The tests use isolated temporary repository fixtures and never run formal tools.
Run from a complete repository checkout:
    python3 Files/Research_Papers/benchmark/pilot_v0_1/P01/tests/test_validate_p01_package.py
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

P01_REL = Path("Files/Research_Papers/benchmark/pilot_v0_1/P01")
ARCHIVE_REL = Path("re/p01-20260930T220622Z-rev1.tar.gz")
FORMAL_SUMMARY_REL = Path("02_CERTIFICATION/P01_FORMAL_RESULTS.md")

CASE_FILES = [
    "requirement.md",
    "interpretations/interpretation_01.md",
    "behavioral_specification/specification_01.md",
    "reference_rtl/rtl_01.sv",
    "validation_rtl/deliberately_wrong_rtl.sv",
    "formal/properties/mux2to1_properties.sv",
    "formal/harness_reference.sv",
    "formal/harness_wrong.sv",
    "formal/reference.sby",
    "formal/wrong.sby",
    "formal/run_p01_formal.sh",
    "review/pre_rtl_review.md",
]

def find_repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / ARCHIVE_REL).is_file() and (parent / FORMAL_SUMMARY_REL).is_file():
            return parent
    raise RuntimeError("Could not locate a complete repository checkout and accepted P01 archive")

def make_fixture(root: Path) -> Path:
    real_root = find_repo_root()
    case_dir = root / P01_REL
    case_dir.mkdir(parents=True)
    for rel in CASE_FILES:
        source = real_root / P01_REL / rel
        target = case_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    validator = case_dir / "validate_p01_package.py"
    shutil.copy2(real_root / P01_REL / "validate_p01_package.py", validator)
    shutil.copy2(real_root / P01_REL / "p01_package_manifest_v1.json", case_dir / "p01_package_manifest_v1.json")
    archive_target = root / ARCHIVE_REL
    archive_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(real_root / ARCHIVE_REL, archive_target)
    summary = root / FORMAL_SUMMARY_REL
    summary.parent.mkdir(parents=True, exist_ok=True)
    summary.write_text("P01 formal results fixture\n", encoding="utf-8")
    return validator

class P01ValidatorRegressionTests(unittest.TestCase):
    def run_validator(self, root: Path, validator: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(validator)],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_unmodified_baseline_fixture_passes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p01-validator-pass-") as tmp:
            root = Path(tmp)
            validator = make_fixture(root)
            result = self.run_validator(root, validator)
            self.assertEqual(result.returncode, 0, result.stdout + "\n" + result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["failed"], 0)
            self.assertGreaterEqual(report["passed"], 20)
            self.assertFalse(report["formal_tools_executed"])
            self.assertFalse(report["human_certification_performed"])
            self.assertFalse(report["template_freeze_performed"])

    def test_source_mutation_is_detected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p01-validator-source-mutation-") as tmp:
            root = Path(tmp)
            validator = make_fixture(root)
            reference = root / P01_REL / "reference_rtl/rtl_01.sv"
            reference.write_text(
                reference.read_text(encoding="utf-8") + "\n// mutation\n",
                encoding="utf-8",
            )
            result = self.run_validator(root, validator)
            self.assertEqual(result.returncode, 1, result.stdout + "\n" + result.stderr)
            report = json.loads(result.stdout)
            failed_names = {item["check"] for item in report["checks"] if item["status"] == "FAIL"}
            self.assertIn("source:reference_rtl/rtl_01.sv", failed_names)

    def test_accepted_archive_mutation_is_detected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p01-validator-archive-mutation-") as tmp:
            root = Path(tmp)
            validator = make_fixture(root)
            archive = root / ARCHIVE_REL
            data = archive.read_bytes()
            archive.write_bytes(bytes([data[0] ^ 1]) + data[1:])
            result = self.run_validator(root, validator)
            self.assertEqual(result.returncode, 1, result.stdout + "\n" + result.stderr)
            report = json.loads(result.stdout)
            failed_names = {item["check"] for item in report["checks"] if item["status"] == "FAIL"}
            self.assertIn("accepted-archive-sha256", failed_names)


    def test_manifest_mutation_is_detected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p01-validator-manifest-mutation-") as tmp:
            root = Path(tmp)
            validator = make_fixture(root)
            manifest_path = root / P01_REL / "p01_package_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["case_role"] = "altered baseline"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
            result = self.run_validator(root, validator)
            self.assertEqual(result.returncode, 1, result.stdout + "\n" + result.stderr)
            report = json.loads(result.stdout)
            failed_names = {item["check"] for item in report["checks"] if item["status"] == "FAIL"}
            self.assertIn("manifest-git-blob-sha1", failed_names)

if __name__ == "__main__":
    unittest.main(verbosity=2)
