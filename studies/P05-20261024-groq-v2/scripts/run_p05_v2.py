#!/usr/bin/env python3
"""P05 evidence runner v2: preserve a separate waveform for every cover target."""
import argparse, csv, hashlib, json, os, platform, re, shutil, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, value): p.write_text(json.dumps(value, indent=2) + '\n')
def command(argv, directory, name, timeout=180):
    start = time.monotonic()
    try:
        p = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=timeout)
        code, stdout, stderr, timed = p.returncode, p.stdout, p.stderr, False
    except subprocess.TimeoutExpired as e:
        code, stdout, stderr, timed = None, e.stdout or b'', e.stderr or b'', True
    (directory/(name+'.stdout.log')).write_bytes(stdout)
    (directory/(name+'.stderr.log')).write_bytes(stderr)
    result = dict(argv=argv, cwd='repository root', returncode=code, timeout=timed,
                  seconds=round(time.monotonic()-start,3))
    save(directory/(name+'.command.json'), result)
    return result, stdout.decode(errors='replace')+'\n'+stderr.decode(errors='replace')
def native_status(meta, text):
    if meta['timeout']: return 'TIMEOUT'
    found = re.findall(r'Status:\s+(PASSED|FAILED|PREUNSAT|UNKNOWN)', text)
    if found and found[-1]=='PASSED' and meta['returncode']==0: return 'PASS'
    if found and found[-1]=='FAILED' and meta['returncode']!=0: return 'FAIL'
    if found and found[-1]=='UNKNOWN': return 'UNKNOWN'
    return 'TOOL_ERROR'
def inventory(path):
    cells=json.loads(path.read_text())['modules']['harness'].get('cells',{})
    return {k:sum(c['type']==k for c in cells.values()) for k in ('$assert','$assume','$cover')}
def run_job(out, job, yosys, smtbmc):
    name, dut, contract, source, expected, mode = job
    d=out/name; d.mkdir()
    defs=[f'-D DUT={dut}']
    if contract: defs += [f'-D {contract}']
    if mode in ('distinction','cover'): defs += ['-D DISTINCTION']
    if mode=='self': defs += ['-D SELF']
    if mode=='postreset': defs += ['-D POST_RESET']
    inputs=[source,'cases/P05/contracts/I1_contract.sv','cases/P05/contracts/I2_contract.sv',
            'cases/P05/formal/assumptions.sv','formal/P05/harness/current.sv',
            'formal/P05/harness/reference_state_properties.sv']
    snap=d/'source';snap.mkdir()
    for item in inputs:
        target=snap/item;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/item,target)
    smt=str((d/'model.smt2').relative_to(ROOT)); net=str((d/'netlist.json').relative_to(ROOT))
    script='read_verilog -formal -sv '+' '.join(defs+inputs)+'\nprep -top harness\nflatten\nclk2fflogic\nopt -full\nchformal -lower\nopt_clean\n'
    if mode=='cover': script+='chformal -assert -remove\n'
    script+=f'write_json {net}\nwrite_smt2 -wires {smt}\n'
    (d/'build.ys').write_text(script)
    m,t=command([yosys,'-s',str((d/'build.ys').relative_to(ROOT))],d,'elaboration')
    row=dict(job_id=name,dut=dut,contract=contract or mode,expected=expected,result='TOOL_ERROR',
             evidence=str(d.relative_to(ROOT)),git_commit=out_meta['git_commit'],commands=[m])
    if m['returncode']==0:
        inv=inventory(d/'netlist.json');row['property_inventory']=inv
        if inv['$assume']<4 or (mode=='cover' and inv['$cover']<2) or (mode!='cover' and inv['$assert']<1):
            row['error']='Property inventory is missing required assertions/assumptions/covers'
        else:
            base=[smtbmc,'-s','z3','--presat','-t','16','--timeout','180','--noprogress']
            opts=['-c'] if mode=='cover' else []
            dump=str(d.relative_to(ROOT)/('witness-%' if mode=='cover' else 'witness'))
            m,t=command(base+opts+['--dump-vcd',dump+'.vcd','--dump-yw',dump+'.yw',smt],d,'cover' if mode=='cover' else 'bmc')
            row['commands'].append(m);row['bmc_result']=native_status(m,t);row['result']=row['bmc_result']
            if mode!='cover' and row['result']=='PASS':
                m,t=command(base+['-i',smt],d,'induction');row['commands'].append(m)
                row['induction_result']=native_status(m,t)
                row['result']='PASS' if row['induction_result']=='PASS' else ('UNKNOWN' if row['induction_result']=='FAIL' else row['induction_result'])
                if row['result']=='UNKNOWN':
                    m,t=command([sys.executable,'scripts/reachability.py',smt,str(d.relative_to(ROOT))],d,'reachability')
                    row['commands'].append(m);row['reachability_result']=native_status(m,t)
                    if row['reachability_result']=='PASS':
                        checks=[]
                        for part in ('initiation','closure','safety'):
                            m,t=command(['z3',str((d/f'certificate-{part}.smt2').relative_to(ROOT))],d,'certificate-'+part)
                            row['commands'].append(m);checks.append(m['returncode']==0 and t.strip()=='unsat')
                        row['result']='PASS' if all(checks) else 'TOOL_ERROR'
            if mode=='distinction' and row['result']=='FAIL':
                m,t=command(base+['--yw',dump+'.yw','--check-witness','--dump-vcd',dump+'-replay.vcd','--dump-yw',dump+'-replay.yw',smt],d,'replay')
                row['commands'].append(m);row['replay_result']=native_status(m,t)
                m,t=command(base+['--yw',dump+'.yw','--dump-vcd',dump+'-replay.vcd','--dump-yw',dump+'-replay.yw',smt],d,'replay-trace')
                row['commands'].append(m);row['replay_trace_result']=native_status(m,t)
                if row['replay_result']!='PASS' or row['replay_trace_result']!='FAIL': row['result']='TOOL_ERROR'
    row['seconds']=round(sum(c['seconds'] for c in row['commands']),3)
    row['expected_observed']=row['result']==expected
    save(d/'result.json',row)
    print(name,row['result'],'expected',expected,flush=True)
    return row
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--run-id',required=True)
    parser.add_argument('--only',default='all')
    parser.add_argument('--rtl');parser.add_argument('--module',default='p05')
    parser.add_argument('--allow-dirty',action='store_true')
    args=parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+',args.run_id): parser.error('safe unique run ID required')
    state=subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=ROOT).decode()
    if state and not args.allow_dirty: parser.error('Tracked edits must be committed before running')
    out=ROOT/'cases/P05/evidence/current'/args.run_id;out.mkdir(parents=True,exist_ok=False)
    yosys=shutil.which('yowasp-yosys') or shutil.which('yosys')
    smtbmc=shutil.which('yowasp-yosys-smtbmc') or shutil.which('yosys-smtbmc')
    if not yosys or not smtbmc or not shutil.which('z3'): sys.exit('Missing Yosys/SMTBMC/Z3 on PATH')
    out_meta=dict(run_id=args.run_id,git_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),
                  tracked_dirty=state,utc=datetime.now(timezone.utc).isoformat(),platform=platform.platform(),
                  machine=platform.machine(),python=sys.version,runner_sha256=digest(Path(__file__)))
    for tool,argv in [('yosys',[yosys,'-V']),('z3',['z3','--version'])]:
        m,t=command(argv,out,tool+'-version');out_meta[tool]=t.strip()
    save(out/'environment.json',out_meta)
    ref='cases/P05/reference_rtl/responses.sv';mut='cases/P05/controls/strict_invalid_mutants/mutants.sv'
    if args.rtl:
        jobs=[(f'{args.run_id}-{c}',args.module,c,args.rtl,'UNSPECIFIED','conformance') for c in ('I1','I2')]
    else:
        jobs=[(f'{c}-{dut}',dut,c,ref,'PASS' if (c,dut) in [('I1','response_b'),('I2','response_a')] else 'FAIL','conformance') for c in ('I1','I2') for dut in ('response_a','response_b')]
        jobs += [('distinction','response_b',None,ref,'FAIL','distinction'),('reachability','response_b',None,ref,'PASS','cover')]
        jobs += [(f'self-{dut}',dut,c,ref,'PASS','self') for c,dut in [('I1','response_b'),('I2','response_a')]]
        jobs += [(f'{c}-{dut}',dut,c,mut,'FAIL','conformance') for c in ('I1','I2') for dut in ('no_response','latency_two','bad_reset')]
    if not args.rtl:
        jobs += [(f'{c}-{dut}-postreset',dut,c,mut,'FAIL','postreset') for c in ('I1','I2') for dut in ('no_response','latency_two','bad_reset')]
    if args.only!='all': jobs=[j for j in jobs if args.only in j[0]]
    if not jobs: sys.exit('No jobs selected')
    rows=[run_job(out,j,yosys,smtbmc) for j in jobs]
    save(out/'results.json',rows)
    with (out/'results.csv').open('w') as f:
        fields=['job_id','dut','contract','expected','result','bmc_result','induction_result','replay_result','seconds','expected_observed','evidence','git_commit']
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
    save(out/'checksums.json',{str(p.relative_to(out)):digest(p) for p in sorted(out.rglob('*')) if p.is_file() and p.name!='checksums.json'})
    sys.exit(0 if all(r['expected_observed'] or r['expected']=='UNSPECIFIED' for r in rows) else 1)
