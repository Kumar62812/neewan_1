# T06 — P02 formal/provenance closure: closure review v1

**Status: AUTHOR-APPROVED — DONE for the named review version `T06_P02_CLOSURE_REVIEW_v1` as of 2026-10-29.** See [author approval record](../project-sequence/approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md). The technical review content approved by the author is pinned in that record; this status annotation is a subsequent administrative update.
Prepared 2026-10-28 after T05 was approved ([approval record](../project-sequence/approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md)). This review is
read-only over branch `research/end-to-end-sequence` at commit `109336c88433be1c3f5836bfde351b5e0c841b0c`;
the P02 tree is byte-identical through branch head `762c68df4217d8c6cbf0c93ce4447d1bc136ba88`.
No P02 source, evidence or run file was modified. Reviewer: Claude (automated technical review). This is not
a human review or a certification decision.

## 1. What T06 closes

T05 established that the P02 contract (R, I, S) traces to the RTL and the properties, and that the tested
inputs are identical by content. T06 closes the **formal evidence** that rests on that contract:

1. The executed run is intact and complete.
2. Every recorded status is supported by the raw tool logs.
3. The negative-control counterexamples are legal under the declared environment and show the intended violation.
4. The claims made in `P02_RESULTS.md` match the evidence, and their limits are stated.
5. P02's case role and the version of its evidence package are fixed.

## 2. Evidence integrity

| Package | Manifest entries | Recomputed SHA-256 mismatches | Unlisted / missing files |
|---|---:|---:|---|
| `evidence/run-02/` (final) | 50 | 0 | none / none |
| `evidence/run-01/` (initial, retained) | 43 | 0 | — |

Run-02 manifest file: `evidence/run-02/SHA256SUMS.json`. Its tested-input hashes are listed in full in
[T05 closure review v1 §4](T05_P02_CLOSURE_REVIEW_v1.md).

## 3. Recorded statuses against raw logs

| Check | `runs.json` status, return code | Raw log evidence | Agrees |
|---|---|---|---|
| Reference BMC, 12 steps | PASS, 0 | `Status: PASSED` | yes |
| Reference induction, ≤ 12 | PASS, 0 | `Temporal induction successful` at step 11; `Status: PASSED` | yes |
| Reference cover, 16 | PASS, 0 | 8 `Reached cover statement` lines; `Status: PASSED` | yes |
| `wrong_reset` BMC, 12 | FAIL, 1 | `Assert failed … register_properties.sv:9` | yes |
| `wrong_async` BMC, 12 | FAIL, 1 | `Assert failed … register_properties.sv:18` | yes |

All three elaborations returned 0. Tool versions in the logs: Yosys 0.63 (git `70a11c6bf`, YoWASP), Z3 4.15.4.
The runner's exit rule requires each negative control to FAIL rather than treating it as a pass.

Cover goals reached (property line: step): 23: 0, 24: 0, 11: 1, 12: 1, 13: 1, 19: 1, 20: 2, 16: 5. That is all
eight goals by step 5, so the environment assumptions are satisfiable and the safety proof is not vacuous.

## 4. Counterexample re-derivation

Both traces were decoded independently from the VCD files and checked against the harness assumptions
(clock low at step 0; `rst` and `d` unchanged across a rising step).

| Trace | Step 0 | Step 1 | Legal? | What it shows |
|---|---|---|---|---|
| `wrong-bmc.vcd` | clk=0 rst=1 d=1 q=0 | clk=1 rst=1 d=1 q=1 (rising edge) | yes | Reset held high at an edge, yet `q` loads 1. Violates active-high reset (T05 C3). |
| `async-bmc.vcd` | clk=0 rst=0 d=1 q=1 | clk=0 rst=1 d=0 q=0 (no edge) | yes | `q` drops while the clock stays low. Violates between-edge hold / synchronous reset (T05 C4, C7). |

This matches the counterexample descriptions in `P02_RESULTS.md` exactly. The async trace depends on the
recorded modelling assumption that `rst` may change while `clk` is low; without it the two reset styles
could not be distinguished.

## 5. Claims and limits

**Claim supported by the evidence:** under the declared Boolean, stable-sampled-edge, two-valued
environment, the P02 reference RTL satisfies the P02 specification for all reachable states (BMC base case
plus temporal induction), and two deliberately wrong implementations are rejected with legal witnesses.

**Not claimed by the original run-02 package alone:** analog setup/hold timing; four-state X/Z behaviour; behaviour before the first edge beyond the T05 O3 assumption; independent-person replication; linguistic ambiguity, human plausibility or LLM-performance results. The separate C3 Linux run provides additional cross-platform reproducibility evidence for P02/P05 without modifying or being folded into run-02. P02 was never a SymbiYosys run; there is no `.sby` file.

## 6. Case role and package version

Per T05 decision O4 ([approval record](../project-sequence/approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md)), **P02 is the deterministic control in the core benchmark set**. Its metadata already
agrees: `primary_ambiguity_dimension: none`, `certified_ambiguous: false`, rejection reason
"Not an ambiguity candidate". P02 therefore needs no S1/S2 pair, miter or human plausibility review, and
its formal closure is final at technical level. In LLM experiments it serves as the control: a generated
RTL should match the single specification.

The closed P02 evidence package is **`evidence/run-02/`**, identified by the hash of its manifest:

| File | SHA-256 |
|---|---|
| `evidence/run-02/SHA256SUMS.json` | `35b88570326d7160a2a9b695b4ea92e5867d67d6491a3f8b3e87d398a4765392` |
| `P02_RESULTS.md` | `0b508df3c4569bf1ecdc026e70f47e89d1f002b533fc6dd5fe13bac00382bb6b` |
| `metadata.json` | `6488b260226c633098d69c3e5dbbd87fd0cd5614ef44993df862d2abe35affde` |

## 7. Closure dispositions and non-blocking follow-up

| ID | Severity | Closure disposition | Residual handling |
|---|---|---|---|
| P1 | Medium | **RESOLVED for T06 closure.** The independent C3 Linux reproduction completed successfully at [run 40809992594](https://github.com/Kumar62812/neewan_1/actions/runs/40809992594); fresh P02 run-03 outcomes matched the expected results. | Keep the C3 artifact as separate provenance. Do not merge its outputs into or rewrite run-02. The project-wide reproduction audit remains open under stage 19. |
| P2 | Low | **NON-BLOCKING, OPEN local-asset audit.** The author-held archive \`P02-clean-0874a36608a2-20261010.tar.gz\`, SHA-256 \`234036a798c5e59dd6c542cbd968742d8576843b9763935f6cd6c9a57ebd7b3b\`, was not available for direct verification in this repository review. | Retain the asset-hash check as a separate local preservation task. It does not invalidate the visible run-01/run-02 manifests or block T06 closure. |
| P3 | Low | **NON-BLOCKING release action.** Absolute local paths in historical \`runs.json\` remain part of the recorded run package. | Before public release, produce a redacted release copy or sanitized companion record; preserve the original forensic package and its checksums unchanged. |

These dispositions are recorded to complete the named review. The author’s explicit message approves T06; the separate approval record distinguishes that approval from remaining non-blocking local-asset/release follow-ups.

## 8. Optional reproduction command (new provenance ID, run-03)

Run from a clean checkout of the commit above on any Linux or macOS machine with Python ≥ 3.12. It writes
a new package and never touches run-01 or run-02.

```sh
python3 -m venv /tmp/fv && /tmp/fv/bin/pip install -r docs/reproducibility/formal-requirements.txt
export PATH="/tmp/fv/bin:$PATH"
python Files/Research_Papers/benchmark/pilot_v0_1/P02/formal/run.py \
  --out Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-03
echo "exit=$?"   # 0 means all five expected outcomes reproduced
```

Acceptance: exit 0; the `source/` hashes in `run-03/SHA256SUMS.json` equal the T05 §4 values.

C3 separately completed the P02/P05 Linux rerun using isolated temporary run-03 packages; see [C3 report](C3_P02_P05_LINUX_REPRODUCTION.md) and [raw run artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40809992594/artifacts/12870250852). Those outputs are retained under the Actions artifact rather than written into the canonical P02 evidence tree. The run-02 manifest and hashes remain unchanged.

## 9. Approval record

The author explicitly approved \`T06_P02_CLOSURE_REVIEW_v1\` in the conversation on 2026-10-29:

> T06 approved. Do not request further approval—C3 only covers P02/P05 reproducibility, not full project completion. — G. Naveen

The approval record [T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md](../project-sequence/approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md) pins the technical review content that was presented for approval and records closure/follow-up dispositions.

**Closure decision: T06 DONE** for P02 formal/provenance closure under the stated Boolean stable-sampled-edge model. This is not a declaration that FORMAL-AMBIG-RTL is complete, that the benchmark is certified ambiguous, or that P05's linguistic plausibility is established.
