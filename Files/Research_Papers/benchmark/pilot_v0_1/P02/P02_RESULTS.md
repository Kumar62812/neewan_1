# P02 executed results — 2026-10-10

Final evidence: `evidence/run-02/`. Initial suite: `evidence/run-01/` (retained).
Yosys 0.63 (70a11c6bf), YoWASP package 0.63.0.0.post1107; Z3 4.15.4;
Python 3.12. macOS arm64. Full package versions, commands, timestamps, return codes,
source snapshots, SMT models, logs, VCD/Yosys witnesses and hashes are in each run.

| Executed task | Result | Scope |
|---|---|---|
| Reference BMC | PASS | 12 global steps |
| Reference temporal induction | PASS | Successful at step 11 within 12-step budget |
| Reference cover | PASS | All 8 goals reached by step 5 within 16-step budget |
| Wrong reset-polarity BMC | FAIL | Reset-priority assertion; step 1 |
| Wrong asynchronous-reset BMC | FAIL | Between-edge hold assertion; step 1 |

BMC plus induction establishes unbounded safety for the declared Boolean,
stable-edge digital environment, not physical timing or four-state behavior.
Cover witnesses establish satisfiable assumptions and exercise both initial q
values, both normal loads, reset with d=1, off-edge reset at both clock levels,
and load-one -> reset -> load-one. There is no assumed initial q or mandatory reset.
No SymbiYosys run is claimed: the runner directly invokes Yosys and Yosys-SMTBMC.

## Inspected counterexamples

`evidence/run-02/wrong-bmc.vcd`: step 0 has clk=0, rst=1, d=1, q=0;
step 1 has clk=1, rst=1, d=1, q=1. Inputs meet the sampling contract.
The required post-edge q is 0. This is a real active-high-reset violation.

`evidence/run-02/async-bmc.vcd`: step 0 has clk=0, rst=0, q=1;
step 1 keeps clk=0 and raises rst=1, but q becomes 0. No rising clock edge
occurs. This is a real synchronous-reset/hold violation from a legal initial state.
Both controls are intentionally wrong implementations, not alternative readings.

`evidence/run-02/reference-cover-6.vcd` shows q=1 holding when rst rises
while clk stays high. `reference-cover-7.vcd` shows sampled load-one,
reset-to-zero, and load-one after reset release at global steps 1, 3, 5.
Run-01 used a literal percent character in non-cover trace filenames; those
original files are retained unchanged. Run-02 uses ordinary trace filenames.

Technical P02 implementation and formal evidence are complete under the stated
scope. This does not freeze the P01 template or claim independent certification,
benchmark-wide validity, linguistic ambiguity, or LLM performance.
