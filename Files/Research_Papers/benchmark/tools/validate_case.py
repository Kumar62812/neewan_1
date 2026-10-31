#!/usr/bin/env python3
"""T08 v2 metadata validator and non-overwriting case scaffold generator."""
from __future__ import annotations
import argparse, copy, hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "instance_metadata_template.v2.json"
SCHEMA = ROOT / "schema" / "instance.schema.v2.json"
CATEGORIES = {"C1", "C2", "C3", "C4", "C5"}
TAGS = {"reset", "output", "transition", "timing", "state", "concurrency"}
CERT = {"UNAMBIGUOUS", "CERTIFIED_AMBIGUOUS", "UNRESOLVED", "EXCLUDED"}
STAGES = {"candidate", "certified_ambiguous", "unambiguous_control", "negative_candidate", "inconclusive"}
ROLES = {"unambiguous_control", "ambiguity_candidate", "negative_candidate", "robustness_case"}

def safe_rel(value: str) -> bool:
    p = Path(value)
    return bool(value) and not p.is_absolute() and ".." not in p.parts and not value.startswith(("\\\\", "//"))

def validate(data: dict) -> list[str]:
    e=[]
    required={"schema_version","instance_id","instance_version","case_role","primary_category","thematic_tags","certification_status","lifecycle_stage","release_frozen","provenance","requirement","interpretations","reference_rtl","formal_environment","observables","formal_evidence","annotations","certification_decision","reproducibility"}
    missing=sorted(required-data.keys())
    if missing: e.append("missing required fields: "+", ".join(missing))
    if data.get("schema_version")!="2.0": e.append("schema_version must be '2.0'")
    if not isinstance(data.get("instance_id"),str) or not re.fullmatch(r"[A-Z][A-Z0-9_-]{1,31}",data.get("instance_id","")): e.append("instance_id must match ^[A-Z][A-Z0-9_-]{1,31}$")
    if not isinstance(data.get("instance_version"),str) or not re.fullmatch(r"v[1-9][0-9]*",data.get("instance_version","")): e.append("instance_version must be vN")
    role=data.get("case_role")
    if role not in ROLES: e.append("case_role must be one of "+", ".join(sorted(ROLES)))
    if data.get("primary_category") not in CATEGORIES: e.append("primary_category must be exactly one C1-C5")
    tags=data.get("thematic_tags")
    if not isinstance(tags,list) or len(tags)!=len(set(tags or [])) or any(t not in TAGS for t in (tags or [])): e.append("thematic_tags must be a unique array of approved optional tags")
    if data.get("certification_status") not in CERT: e.append("certification_status must use PLAN §6 vocabulary")
    if data.get("lifecycle_stage") not in STAGES: e.append("lifecycle_stage must use the approved lifecycle vocabulary")
    if not isinstance(data.get("release_frozen"),bool): e.append("release_frozen must be Boolean")
    cross={"candidate":"UNRESOLVED","certified_ambiguous":"CERTIFIED_AMBIGUOUS","unambiguous_control":"UNAMBIGUOUS","inconclusive":"UNRESOLVED"}
    stage=data.get("lifecycle_stage"); status=data.get("certification_status")
    if stage in cross and status!=cross[stage]: e.append(f"lifecycle_stage={stage} requires certification_status={cross[stage]}")
    if stage=="negative_candidate":
        if status=="EXCLUDED" and not (data.get("certification_decision",{}).get("exclusion_reason")): e.append("EXCLUDED negative_candidate requires a specific exclusion_reason")
        if status not in {"EXCLUDED","UNRESOLVED"}: e.append("negative_candidate status must be EXCLUDED or UNRESOLVED")
    if role=="unambiguous_control":
        if data.get("primary_category")!="C1" or stage!="unambiguous_control" or status!="UNAMBIGUOUS": e.append("unambiguous_control requires C1/unambiguous_control/UNAMBIGUOUS")
        if data.get("interpretations",{}).get("B") is not None or data.get("reference_rtl",{}).get("B") is not None: e.append("unambiguous_control must leave interpretation B and reference RTL B absent")
    if role=="ambiguity_candidate":
        if data.get("primary_category") not in {"C2","C3","C4","C5"}: e.append("ambiguity_candidate requires primary category C2-C5")
        for section in ("interpretations","reference_rtl"):
            for key in ("A","B"):
                if not isinstance(data.get(section,{}).get(key),dict): e.append(f"ambiguity_candidate requires {section}.{key}")
    if role=="negative_candidate" and stage!="negative_candidate": e.append("negative_candidate role requires lifecycle_stage=negative_candidate")
    for section,key in (("interpretations","A"),("interpretations","B")):
        item=data.get(section,{}).get(key)
        if item is not None and (not isinstance(item,dict) or not item.get("text") or not item.get("rationale")): e.append(f"{section}.{key} requires non-empty text and rationale")
    for key,item in data.get("reference_rtl",{}).items():
        if item is not None:
            if not isinstance(item,dict) or not isinstance(item.get("path"),str) or not safe_rel(item["path"]): e.append(f"reference_rtl.{key}.path must be a safe case-relative path")
            h=item.get("sha256")
            if h is not None and not re.fullmatch(r"[a-f0-9]{64}",str(h)): e.append(f"reference_rtl.{key}.sha256 must be lowercase SHA-256 or null")
    prov=data.get("provenance",{})
    for k in ("source_type","source_reference","created_at","created_by"):
        if not prov.get(k): e.append(f"provenance.{k} is required")
    formal=data.get("formal_evidence",{})
    if formal.get("status") not in {"NOT_RUN","PASS","FAIL","INCONCLUSIVE","INVALID"}: e.append("formal_evidence.status is invalid")
    for ref in formal.get("evidence_references",[]):
        if not isinstance(ref,dict) or not safe_rel(ref.get("path","")): e.append("formal evidence references must use safe case-relative paths")
    ann=data.get("annotations",{})
    if ann.get("status") not in {"NOT_COLLECTED","IN_PROGRESS","COMPLETE","ADJUDICATED"}: e.append("annotations.status is invalid")
    for ref in ann.get("record_references",[]):
        if not isinstance(ref,dict) or not safe_rel(ref.get("path","")): e.append("annotation references must use safe case-relative paths")
    for h in data.get("reproducibility",{}).get("source_hashes",{}).values():
        if not re.fullmatch(r"[a-f0-9]{64}",str(h)): e.append("reproducibility source_hashes must be lowercase SHA-256")
    return e

def scaffold(case_id: str, role: str, category: str, root: Path) -> Path:
    if not re.fullmatch(r"[A-Z][A-Z0-9_-]{1,31}",case_id): raise ValueError("invalid case id")
    if role not in ROLES or category not in CATEGORIES: raise ValueError("invalid role/category")
    if role=="unambiguous_control" and category!="C1": raise ValueError("unambiguous_control requires C1")
    if role=="ambiguity_candidate" and category=="C1": raise ValueError("ambiguity_candidate requires C2-C5")
    target=root/case_id
    if target.exists(): raise FileExistsError(f"refusing to overwrite existing case: {target}")
    data=json.loads(TEMPLATE.read_text(encoding="utf-8"))
    data["instance_id"]=case_id; data["case_role"]=role; data["primary_category"]=category
    if role=="unambiguous_control":
        data["lifecycle_stage"]="unambiguous_control"; data["certification_status"]="UNAMBIGUOUS"
        data["interpretations"]["B"]=None; data["reference_rtl"]["B"]=None
    elif role=="ambiguity_candidate":
        data["lifecycle_stage"]="candidate"; data["certification_status"]="UNRESOLVED"
    elif role=="negative_candidate":
        data["lifecycle_stage"]="negative_candidate"; data["certification_status"]="UNRESOLVED"
        data["interpretations"]["B"]=None; data["reference_rtl"]["B"]=None
    else:
        data["lifecycle_stage"]="candidate"; data["certification_status"]="UNRESOLVED"
        data["interpretations"]["B"]=None; data["reference_rtl"]["B"]=None
    target.mkdir(parents=True)
    dirs=["requirement","interpretations","behavioral_specification","reference_rtl/A","formal/properties","formal/harnesses","formal/scripts","annotations","provenance","evidence"]
    if role=="ambiguity_candidate": dirs += ["reference_rtl/B"]
    for d in dirs: (target/d).mkdir(parents=True,exist_ok=True)
    (target/"metadata.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    return target

def create_run(case_path: Path) -> Path:
    case_path = case_path.resolve()
    metadata_path = case_path / "metadata.json"
    if not metadata_path.is_file():
        raise FileNotFoundError(f"metadata.json not found: {metadata_path}")
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        raise ValueError("case metadata invalid: " + "; ".join(errors))
    evidence = case_path / "evidence"
    evidence.mkdir(exist_ok=True)
    existing = [int(m.group(1)) for p in evidence.iterdir()
                if p.is_dir() and (m := re.fullmatch(r"run-(\d{2,})", p.name))]
    number = max(existing, default=0) + 1
    run_dir = evidence / f"run-{number:02d}"
    # mkdir without exist_ok is the final race-safe no-overwrite guard.
    run_dir.mkdir()
    manifest = {
        "manifest_version": "1.0",
        "run_id": run_dir.name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "instance_id": data["instance_id"],
        "instance_version": data["instance_version"],
        "metadata_path": "metadata.json",
        "metadata_sha256": hashlib.sha256(metadata_path.read_bytes()).hexdigest(),
        "source_commit": data.get("reproducibility", {}).get("source_commit"),
        "immutability_rule": "Do not modify this run directory; corrections require a new run."
    }
    (run_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return run_dir

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--metadata")
    p.add_argument("--init")
    p.add_argument("--new-run", help="create the next immutable evidence/run-NN directory for an existing case")
    p.add_argument("--role",choices=sorted(ROLES))
    p.add_argument("--category",choices=sorted(CATEGORIES))
    p.add_argument("--root",default=".")
    a=p.parse_args()
    if a.new_run:
        try:
            path = create_run(Path(a.new_run))
            print(f"CREATED_NEW_EVIDENCE_RUN {path}")
            return 0
        except Exception as ex:
            print(f"ERROR: {ex}", file=sys.stderr)
            return 2
    if a.init:
        try:
            path=scaffold(a.init,a.role,a.category,Path(a.root))
            errs=validate(json.loads((path/"metadata.json").read_text()))
            if errs: raise ValueError("; ".join(errs))
            print(f"CREATED_AND_VALIDATED {path}")
            return 0
        except Exception as ex: print(f"ERROR: {ex}",file=sys.stderr); return 2
    if not a.metadata: p.error("provide --metadata or --init")
    path=Path(a.metadata); data=json.loads(path.read_text(encoding="utf-8")); errors=validate(data)
    if errors:
        print("INVALID")
        for err in errors: print(f"- {err}")
        return 1
    print(f"VALID {path}")
    return 0
if __name__=="__main__": raise SystemExit(main())
