import json, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/"tools"/"validate_case.py"
TEMPLATE=Path(__file__).resolve().parents[1]/"templates"/"instance_metadata_template.v2.json"

class T08ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.base=json.loads(TEMPLATE.read_text())

    def test_ambiguity_candidate_template_is_valid(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        self.assertEqual([],mod.validate(self.base))

    def test_primary_category_is_single_c1_to_c5_value(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        x=dict(self.base); x["primary_category"]="C6"
        self.assertTrue(any("primary_category" in e for e in mod.validate(x)))

    def test_thematic_tags_are_optional_and_cannot_replace_primary(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        x=dict(self.base); x["thematic_tags"]=["reset","timing"]
        self.assertEqual([],mod.validate(x))
        x["primary_category"]=None
        self.assertTrue(any("primary_category" in e for e in mod.validate(x)))

    def test_inconclusive_defaults_to_unresolved(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        x=json.loads(json.dumps(self.base)); x["lifecycle_stage"]="inconclusive"
        self.assertEqual([],mod.validate(x))
        x["certification_status"]="EXCLUDED"
        self.assertTrue(any("requires certification_status" in e for e in mod.validate(x)))

    def test_negative_candidate_exclusion_requires_reason(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        x=json.loads(json.dumps(self.base)); x["case_role"]="negative_candidate"; x["lifecycle_stage"]="negative_candidate"
        x["certification_status"]="EXCLUDED"; x["interpretations"]["B"]=None; x["reference_rtl"]["B"]=None
        self.assertTrue(any("exclusion_reason" in e for e in mod.validate(x)))

    def test_unambiguous_control_does_not_invent_interpretation_b(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        x=json.loads(json.dumps(self.base)); x["case_role"]="unambiguous_control"; x["primary_category"]="C1"
        x["lifecycle_stage"]="unambiguous_control"; x["certification_status"]="UNAMBIGUOUS"
        x["interpretations"]["B"]=None; x["reference_rtl"]["B"]=None
        self.assertEqual([],mod.validate(x))

    def test_ambiguity_candidate_requires_paired_interpretations_and_rtl(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        x=json.loads(json.dumps(self.base)); x["interpretations"]["B"]=None
        self.assertTrue(any("interpretations.B" in e for e in mod.validate(x)))

    def test_parent_path_traversal_rejected(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case",str(SCRIPT)).load_module()
        x=json.loads(json.dumps(self.base)); x["reference_rtl"]["A"]["path"]="../outside.sv"
        self.assertTrue(any("safe case-relative" in e for e in mod.validate(x)))

    def test_scaffold_is_non_overwriting(self):
        with tempfile.TemporaryDirectory() as d:
            cmd=[sys.executable,str(SCRIPT),"--init","T08_SMOKE","--role","ambiguity_candidate","--category","C2","--root",d]
            first=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(0,first.returncode,first.stderr)
            second=subprocess.run(cmd,capture_output=True,text=True)
            self.assertNotEqual(0,second.returncode)
            self.assertIn("refusing to overwrite",second.stderr)

    def test_scaffold_validates_control_shape(self):
        with tempfile.TemporaryDirectory() as d:
            cmd=[sys.executable,str(SCRIPT),"--init","T08_CONTROL","--role","unambiguous_control","--category","C1","--root",d]
            r=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(0,r.returncode,r.stderr)
            data=json.loads((Path(d)/"T08_CONTROL"/"metadata.json").read_text())
            self.assertIsNone(data["interpretations"]["B"])
            self.assertIsNone(data["reference_rtl"]["B"])


    def test_evidence_run_is_new_and_non_overwriting(self):
        from importlib.machinery import SourceFileLoader
        mod=SourceFileLoader("validate_case_runs",str(SCRIPT)).load_module()
        with tempfile.TemporaryDirectory() as d:
            case=mod.scaffold("T08_RUN_CASE","ambiguity_candidate","C2",Path(d))
            first=mod.create_run(case)
            second=mod.create_run(case)
            self.assertEqual("run-01",first.name)
            self.assertEqual("run-02",second.name)
            manifest=json.loads((first/"run_manifest.json").read_text())
            self.assertEqual("T08_RUN_CASE",manifest["instance_id"])
            self.assertEqual(64,len(manifest["metadata_sha256"]))

if __name__=="__main__": unittest.main(verbosity=2)
