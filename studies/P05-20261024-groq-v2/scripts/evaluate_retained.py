#!/usr/bin/env python3
"""Evaluator v2.1: lower accepted sequential processes before interface JSON export."""
import argparse, csv, hashlib, json, shutil, subprocess, sys, time
from pathlib import Path
from extract_rtl import extract
from public_common import ROOT, BASE, BATCH, sha, save

def main(prefix, output):
    output=ROOT/output;output.mkdir(parents=True,exist_ok=False)
    rows=[]
    for meta_path in sorted(BASE.glob('P05-GROQ2-*/metadata.json')):
        meta=json.loads(meta_path.read_text()); ident=meta['run_id']
        row=dict(meta,syntax_status='NOT_RUN',elaboration_status='NOT_RUN',evaluation_eligible=False,
            I1_result='NOT_EVALUATED',I2_result='NOT_EVALUATED',paired_outcome='EXCLUDED',
            formal_runtime_seconds=0,tool_error='',counterexample_path='',evidence_directory='')
        if meta['rtl_extraction_status']=='EXTRACTED':
            assert sha(ROOT/meta['raw_output_path'])==meta['raw_output_sha256']
            assert sha(ROOT/meta['rtl_path'])==meta['rtl_sha256']
            rtl,error=extract((ROOT/meta['raw_output_path']).read_text())
            assert not error and rtl==(ROOT/meta['rtl_path']).read_text()
            d=ROOT/'build/generation_evaluation'/prefix/ident;d.mkdir(parents=True,exist_ok=False)
            net=d/'interface.json'; script=d/'syntax.ys'
            script.write_text(f'read_verilog -sv {meta["rtl_path"]}\nhierarchy -check -top p05\nproc\nwrite_json {net.relative_to(ROOT)}\n')
            try:
                p=subprocess.run([shutil.which('yowasp-yosys') or shutil.which('yosys'),'-s',str(script.relative_to(ROOT))],cwd=ROOT,capture_output=True,timeout=180)
                (d/'syntax.stdout.log').write_bytes(p.stdout);(d/'syntax.stderr.log').write_bytes(p.stderr)
                row['syntax_status']='PASS' if p.returncode==0 else 'ERROR'
                row['elaboration_status']='ERROR'
                row['exclusion_reason']='Syntax or module elaboration error'
                if p.returncode==0:
                    ports=json.loads(net.read_text())['modules']['p05']['ports']
                    valid=set(ports)=={'clk','rst','req','ack'} and all(len(v['bits'])==1 and v['direction']==('output' if n=='ack' else 'input') for n,v in ports.items())
                    row['elaboration_status']='PASS' if valid else 'INTERFACE_ERROR'
                    row['exclusion_reason']='' if valid else 'Expected exact four one-bit ports'
                    if valid:
                        row['evaluation_eligible']=True;rid=prefix+'-'+ident
                        t=time.monotonic()
                        p=subprocess.run([sys.executable,'scripts/run_p05_v2.py','--run-id',rid,'--rtl',meta['rtl_path']],cwd=ROOT,capture_output=True,timeout=1200)
                        (d/'formal.stdout.log').write_bytes(p.stdout);(d/'formal.stderr.log').write_bytes(p.stderr)
                        row['formal_runtime_seconds']=round(time.monotonic()-t,3)
                        fd=ROOT/'cases/P05/evidence/current'/rid
                        row['evidence_directory']=str(fd.relative_to(ROOT))
                        result=json.loads((fd/'results.json').read_text())
                        assert len(result)==2 and {r['contract'] for r in result}=={'I1','I2'}
                        for r in result:
                            assert r['result'] in ['PASS','FAIL','UNKNOWN','TIMEOUT','TOOL_ERROR']
                            row[r['contract']+'_result']=r['result']
                            if r['result']=='FAIL':
                                f=ROOT/r['evidence']/'witness.vcd';assert f.exists()
                                row['counterexample_path']+=str(f.relative_to(ROOT))+';'
                        pair=(row['I1_result'],row['I2_result'])
                        row['paired_outcome']={('PASS','PASS'):'both',('FAIL','FAIL'):'neither',('PASS','FAIL'):'I1_only',('FAIL','PASS'):'I2_only'}.get(pair,'unresolved')
            except subprocess.TimeoutExpired as e:
                (d/'timeout.stdout.log').write_bytes(e.stdout or b'');(d/'timeout.stderr.log').write_bytes(e.stderr or b'')
                row.update(tool_error='TIMEOUT',exclusion_reason='Evaluator timeout')
                if row['evaluation_eligible']: row.update(I1_result='TIMEOUT',I2_result='TIMEOUT',paired_outcome='unresolved')
            except Exception as e:
                row.update(tool_error=type(e).__name__+': '+str(e))
                if row['evaluation_eligible']:row.update(I1_result='TOOL_ERROR',I2_result='TOOL_ERROR',paired_outcome='unresolved')
                else:row.update(exclusion_reason='Evaluator tool error')
            row['compile_evidence']=str(d.relative_to(ROOT))
        rows.append(row)
        print(ident,row['syntax_status'],row['I1_result'],row['I2_result'],flush=True)
        save(output/'evaluation.json',rows)
    assert len(rows)==3 and len({r['run_id'] for r in rows})==3,'All three planned attempts required'
    fields='run_id batch_id attempt_number seed model_provider model_name model_version resolved_model system_fingerprint generation_timestamp generation_status raw_output_path raw_output_sha256 rtl_path rtl_sha256 rtl_extraction_status syntax_status elaboration_status evaluation_eligible exclusion_reason I1_result I2_result paired_outcome formal_runtime_seconds tool_error counterexample_path evidence_directory git_commit'.split()
    with (output/'paired_results.csv').open('w') as f:
        w=csv.DictWriter(f,fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
    eligible=[r for r in rows if r['evaluation_eligible']]
    counts=dict(batch_id=BATCH,attempts=len(rows),raw_outputs=sum(bool(r['raw_output_path']) for r in rows),
        extractable=sum(r['rtl_extraction_status']=='EXTRACTED' for r in rows),syntax_valid=sum(r['syntax_status']=='PASS' for r in rows),
        elaborated=sum(r['elaboration_status']=='PASS' for r in rows),formally_evaluated=len(eligible),excluded=len(rows)-len(eligible))
    counts.update({k:sum(r['paired_outcome']==k for r in eligible) for k in ['I1_only','I2_only','both','neither','unresolved']})
    counts.update(I1_pass=sum(r['I1_result']=='PASS' for r in eligible),I2_pass=sum(r['I2_result']=='PASS' for r in eligible))
    save(output/'summary.json',counts)
    save(output/'analysis_metadata.json',dict(script_sha256=sha(Path(__file__)),git_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),prefix=prefix))
    print(json.dumps(counts,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--prefix',required=True);p.add_argument('--output',required=True);a=p.parse_args();main(a.prefix,a.output)
