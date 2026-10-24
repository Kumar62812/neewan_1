#!/usr/bin/env python3
"""Reproduce primary published outcomes using saved responses; no API calls."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def main(ident):
 for path,digest in json.loads((R/'SHA256SUMS.json').read_text()).items():
  assert hashlib.sha256((R/path).read_bytes()).hexdigest()==digest,path
 out=R/'build'/ident
 p=subprocess.run([sys.executable,'scripts/evaluate_retained.py','--prefix',ident,'--output',str(out.relative_to(R))],cwd=R,capture_output=True)
 (out/'reproduction.stdout.log').write_bytes(p.stdout);(out/'reproduction.stderr.log').write_bytes(p.stderr)
 assert p.returncode==0,p.stderr.decode(errors='replace')
 data=json.loads((out/'evaluation.json').read_text())
 actual={m['run_id']:[m['I1_result'],m['I2_result'],m['paired_outcome']] for m in data}
 expected={'P05-GROQ2-001':['FAIL','PASS','I2_only'],'P05-GROQ2-002':['PASS','FAIL','I1_only'],'P05-GROQ2-003':['PASS','FAIL','I1_only']}
 assert actual==expected,(actual,expected)
 (out/'validation.json').write_text(json.dumps(dict(status='PASS',samples=3,primary_contract_checks=6,new_model_requests=0,outcomes=actual),indent=2)+'\n')
 print('Published retained-response reproduction PASS: three samples, six primary contract outcomes, no API calls')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--run-id',required=True);a=p.parse_args();main(a.run_id)
