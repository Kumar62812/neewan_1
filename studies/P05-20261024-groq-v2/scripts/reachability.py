#!/usr/bin/env python3
"""Finite-state reachability fallback, with an independently checked SMT certificate.

The candidate invariant is a union of states. Native Z3 must independently prove
initiation, transition closure, and safety. Enumeration cannot by itself return PASS.
"""
import json, re, sys, time
from pathlib import Path
import z3

model_path=Path(sys.argv[1]); out=Path(sys.argv[2]); text=model_path.read_text()
if '; yosys-smt2-topmod harness' not in text: raise ValueError('Expected flattened harness')
regs=[]
for line in text.splitlines():
    if line.startswith('; yosys-smt2-witness '):
        w=json.loads(line.split(' ',2)[2])
        if w['type']=='reg': regs.append((str(w['smtname']),w['width']))
if not regs or sum(w for _,w in regs)>24: raise ValueError('State projection outside audited <=24-bit scope')
if any(token in text for token in ('yosys-smt2-anyconst','yosys-smt2-memory')): raise ValueError('Unsupported constants/memories')
# Every next-state accessor must be one of the projected register fields.
transition=text.split('(define-fun |harness_t|',1)[1]
targets=set(re.findall(r'\(\|harness#([^|]+)\| next_state\)',transition))
if targets!={n for n,_ in regs}: raise ValueError('Incomplete state projection')
width=sum(w for _,w in regs)
def vector(state):
    terms=[f'(|harness#{n}| {state})' for n,_ in regs]
    result=terms[0]
    for t in terms[1:]: result=f'(concat {result} {t})'
    return result
header=text+f'\n(declare-const s |harness_s|)\n(declare-const n |harness_s|)\n(declare-const v (_ BitVec {width}))\n'
header+='(assert (|harness_h| s))\n(assert (|harness_h| n))\n(assert (|harness_u| s))\n'
def members(values,state):
    return '(or '+' '.join(f'(= {vector(state)} (_ bv{v} {width}))' for v in sorted(values))+')' if values else 'false'
def enumerate_states(extra,existing=()):
    s=z3.Solver();s.set(timeout=150000)
    s.from_string(header+extra)
    v=z3.BitVec('v',width);found=set()
    for x in existing:s.add(v!=x)
    while True:
        result=s.check()
        if result==z3.unsat:return found
        if result!=z3.sat:raise RuntimeError('UNKNOWN '+s.reason_unknown())
        value=s.model().eval(v,model_completion=True).as_long()
        found.add(value);s.add(v!=value)
        if len(found)>65536:raise RuntimeError('State budget exceeded')
start=time.monotonic()
reachable=enumerate_states(f'(assert (|harness_i| s))\n(assert (= v {vector("s")}))')
if not reachable:raise RuntimeError('Empty initial set')
rounds=0
while True:
    rounds+=1
    fresh=enumerate_states(f'(assert {members(reachable,"s")})\n(assert (|harness_t| s n))\n(assert (|harness_u| n))\n(assert (= v {vector("n")}))',reachable)
    print('round',rounds,'reachable',len(reachable),'new',len(fresh),flush=True)
    if not fresh:break
    reachable |= fresh
    if time.monotonic()-start>150:raise RuntimeError('Reachability budget exceeded')
checks={
 'initiation':f'(and (|harness_i| s) (not {members(reachable,"s")}))',
 'closure':f'(and {members(reachable,"s")} (|harness_t| s n) (|harness_u| n) (not {members(reachable,"n")}))',
 'safety':f'(and {members(reachable,"s")} (not (|harness_a| s)))'}
statuses={}
for name,query in checks.items():
    certificate=header+f'\n(assert {query})\n(check-sat)\n'
    (out/f'certificate-{name}.smt2').write_text(certificate)
    s=z3.Solver();s.set(timeout=150000);s.from_string(certificate)
    statuses[name]=str(s.check());print(name,statuses[name],flush=True)
report=dict(registers=regs,width=width,reachable_states=sorted(reachable),rounds=rounds,checks=statuses,
            z3=z3.get_version_string(),seconds=time.monotonic()-start)
(out/'reachability.json').write_text(json.dumps(report,indent=2)+'\n')
ok=all(s=='unsat' for s in statuses.values())
print('Status: PASSED' if ok else 'Status: UNKNOWN',flush=True)
sys.exit(0 if ok else 2)
