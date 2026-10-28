# P05 executed results — 2026-10-10

Status: UNRESOLVED ambiguity candidate; human annotation count = 0.
Final evidence: `evidence/run-02/`; exploratory run-01 is preserved.
Tools: Yosys 0.63 / YoWASP 0.63.0.0.post1107 and Z3 4.15.4.

| Executed task | Result | Interpretation |
|---|---|---|
| A/B conformance BMC | PASS | 12 global steps |
| A/B conformance induction | PASS | Step 11 within budget 12; both B state recurrences checked |
| Post-reset divergence covers | PASS | A=1/B=0 at step 3; A=0/B=1 at step 5 |
| Post-reset equality BMC | FAIL | Legal distinction at step 3; NON_EQUIVALENT behavioral evidence |

Both conformance proofs use the same interface/environment and hold semantics.
Only ack is an observable; B's pending state is used for a compositional proof.
The first non-reset B output may depend on unspecified pending state, exactly
as allowed in its specification. Divergence evidence requires a shared reset.

## Inspected distinguishing trace

From `evidence/run-02/equality-bmc.vcd`:

| Global step | clk | rst | req | ack A | ack B |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 1 | 0 | 0 |
| 3 | 1 | 0 | 1 | 1 | 0 |

Step 0 outputs are unconstrained initial choices and do not establish the claim.
Step 1 resets both circuits; step 3 captures a legal isolated request.
A responds at that edge; B defers the response. Equality fails after reset,
not because the initial states differed. The second cover also witnesses B's
response on the next rising edge after A has deasserted.

## Preserved unsuccessful proof attempt

Run-01 BMC PASS, cover PASS, equality BMC FAIL. Run-01 induction raw solver
status was FAILED, originally recorded as FAIL by the capture script; the
unbounded conformance outcome for that attempt is INCONCLUSIVE. Its trace
contains an unestablished checker-history/state relation, not a reachable
functional counterexample. See formal/STRATEGY.md for diagnosis and refinement.
Run-02 checks both B recurrences directly, preserving functional RTL, environment,
bounds, and the distinguishing miter. No failed attempt was overwritten.

Formal distinction does not establish that people accept both readings.
No human ratings, agreement score, threshold success or certification is claimed.
Use annotation/REVIEW_FORM.md and preregister aggregation before collection.
