#!/usr/bin/env python3
"""Run actual HDL formal checks, retaining commands, source snapshots and raw logs."""
import argparse, datetime, hashlib, json, os, platform, shutil, subprocess, time
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--out', required=True, type=Path, help='New evidence directory; must not exist')
ap.add_argument('--yosys', default='yowasp-yosys')
ap.add_argument('--smtbmc', default='yowasp-yosys-smtbmc')
a = ap.parse_args()
case = Path(__file__).resolve().parents[1]
out = a.out.resolve()
out.mkdir(parents=True, exist_ok=False)
records = []

def run(name, cmd, cwd=out):
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    t = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True, timeout=180)
        log, rc = p.stdout, p.returncode
        status = ('PASS' if 'Status: PASSED' in log and rc == 0 else
                  'FAIL' if 'Status: FAILED' in log else
                  'INCONCLUSIVE' if 'Status: UNKNOWN' in log else
                  'TOOL ERROR' if rc else None)
    except subprocess.TimeoutExpired as e:
        raw = e.stdout or b''
        log = raw.decode(errors='replace') if isinstance(raw, bytes) else raw
        log += '\nWALL TIMEOUT: 180 seconds\n'
        rc, status = None, 'INCONCLUSIVE'
    except OSError as e:
        log, rc, status = str(e), None, 'TOOL ERROR'
    (out / (name + '.log')).write_text(log)
    row = dict(name=name, command=cmd, cwd=str(cwd), started_utc=started,
               elapsed_seconds=round(time.monotonic()-t,3), returncode=rc, status=status)
    records.append(row)
    (out/'runs.json').write_text(json.dumps(records, indent=2)+'\n')
    print(name, status or 'command completed', flush=True)
    return rc, status

for rel in ['reference_rtl', 'validation_rtl', 'formal']:
    shutil.copytree(case/rel, out/'source'/rel)
for f in case.glob('*.md'):
    shutil.copy2(f, out/'source'/f.name)
repo = case
while not (repo/'.git').exists(): repo = repo.parent
(out/'environment.json').write_text(json.dumps(dict(platform=platform.platform(),
    python=platform.python_version(), base_commit=subprocess.check_output(
        ['git','rev-parse','HEAD'],cwd=repo,text=True).strip(), timeout_seconds=180,
    yosys=a.yosys, smtbmc=a.smtbmc),indent=2)+'\n')
run('yosys-version', [a.yosys,'-V'])
run('solver-version', ['z3','-version'])
run('python-packages', [os.sys.executable,'-m','pip','freeze'])
for variant in ['reference','wrong']:
    script = (f'read_verilog -formal -sv {"-D WRONG " if variant == "wrong" else ""}'
              'source/reference_rtl/register.sv source/validation_rtl/wrong_reset.sv '
              'source/formal/properties/register_properties.sv source/formal/harness.sv\n'
              'prep -top harness\nflatten\nclk2fflogic\nopt_clean\n'
              f'write_smt2 -wires {variant}.smt2\n')
    (out/(variant+'.ys')).write_text(script)
    rc, status = run(variant+'-elaborate',[a.yosys,'-s',variant+'.ys'])
    if rc != 0: continue
    tasks = [('bmc',[],12)]
    if variant == 'reference': tasks += [('induction',['-i'],12),('cover',['-c'],16)]
    for task,flags,depth in tasks:
        name = variant+'-'+task
        run(name,[a.smtbmc,'-s','z3','-t',str(depth),*flags,
                  '--dump-vcd',name+'-%.vcd','--dump-yw',name+'-%.yw',variant+'.smt2'])
manifest = {str(f.relative_to(out)):hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted(out.rglob('*')) if f.is_file()}
(out/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
# A negative control FAIL is required, not silently recoded as a proof PASS.
expected = {'reference-bmc':'PASS','reference-induction':'PASS','reference-cover':'PASS','wrong-bmc':'FAIL'}
observed = {r['name']:r['status'] for r in records}
raise SystemExit(0 if all(observed.get(k)==v for k,v in expected.items()) else 1)
