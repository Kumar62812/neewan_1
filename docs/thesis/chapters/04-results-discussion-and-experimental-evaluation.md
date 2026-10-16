# Chapter 4 — RESULTS, DISCUSSION & EXPERIMENTAL EVALUATION

**Status:** Results outline. Populate only from retained case, human-review, or model-run evidence.

Apply **Data → Result → Discussion** to each case and experiment. Keep source identity, measured outcome, and interpretation separate.

## 4.1 Pilot Case Formal Results

### 4.1.1 P01 Formal Proof Convergence

**Data:** Use accepted run p01-20260930T220622Z, the native SBY output, BMC depth 1, tool versions, effective source lineage, and retained witness from the [P01 execution record](../../../Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/evidence/p01-20260930T220622Z/P01_EXECUTION_EVIDENCE_RECALL.md).

**Result:** The retained record reports reference SBY PASS and deliberately wrong RTL SBY FAIL. Its counterexample has a=0, b=1, sel=1, required y=1, observed y=0.

**Discussion:** This supports the tested C1 mux contract for the effective source only. It does not establish an ambiguity, independent certification, template freeze, or benchmark-wide validity. Preserve the distinction between the pinned base and the patched effective tested source; see the [P01 provenance register](../../provenance/p01-evidence-register.md) and [reproduction boundary](../../reproducibility/p01-reproduction.md).

### 4.1.2 P02 Sequential Control

**Data:** Use [P02_RESULTS.md](../../../Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_RESULTS.md) and its run-02 evidence. The record specifies Yosys 0.63, YoWASP 0.63.0.0.post1107, Z3 4.15.4, and Python 3.12.

**Result:** Reference BMC PASS at 12 global steps; temporal induction PASS at step 11 within a 12-step budget; all eight covers reached by step 5 within a 16-step budget; wrong reset-polarity and asynchronous-reset controls FAIL at step 1 with counterexamples.

**Discussion:** BMC plus induction establishes unbounded safety for the declared Boolean, stable-edge digital environment; it does not cover physical timing or four-state behavior. The record says the runner directly invokes Yosys and Yosys-SMTBMC; do not label it a SymbiYosys run. Both negative controls are incorrect implementations, not plausible alternative readings.

### 4.1.3 P05 Candidate Status

**Data:** Use [P05_RESULTS.md](../../../Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md), its run-02 records, and the current [phase workboard](../../project-state/PHASE_WORKBOARD.md).

**Result:** A/B conformance BMC and induction PASS. Post-reset divergence covers reach A=1/B=0 at step 3 and A=0/B=1 at step 5. Equality BMC FAIL provides a legal distinguishing trace at step 3 after a shared reset. The case remains `UNRESOLVED`; the result record reports zero human annotations.

**Discussion:** The proof uses a common interface and environment; `ack` is the observable, while B's pending state supports a compositional proof. The trace establishes the distinction after reset, not from unconstrained initial outputs. Preserve the boundary exactly: **Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.** A formal trace is not human evidence. Do not report P05 as certified ambiguous.

## 4.2 LLM Clarification and Generation Performance

**Current result status:** No model-performance result is established by the planning documents or the draft [PR #7](https://github.com/Kumar62812/neewan_1/pull/7) infrastructure. Keep this section marked planned/pending until eligible model runs and complete retained evidence exist.

Use only the primary metrics and denominators in the frozen [research protocol](../../../Files/Research_Papers/docs/research_protocol.md):

| Metric | Frozen definition |
|---|---|
| Ambiguity Detection Rate (ADR) | Correctly detected / certified ambiguous instances |
| Clarification Rate (CR) | Relevant ASK outcomes / certified ambiguous instances |
| Valid Interpretation Rate (VIR) | (A + B generated RTL classifications) / generated runs |
| Misinterpretation Rate (MIR) | M classifications / generated runs |
| Formal Correctness Rate (FCR) | Formally correct / attempted generations |
| Unnecessary Clarification Rate (UCR) | ASK on unambiguous controls / unambiguous controls |
| Clarification Utility (CU) | (FCR interactive − FCR single-shot) / predefined interaction cost |

Interaction cost must be defined before final analysis. The protocol lists turns, tokens, latency, and human effort as candidate components. Behavioral Ambiguity Severity (BAS) is optional and secondary; it cannot replace certification.

Retain the protocol’s observation unit (Model, Benchmark Instance, Condition, Trial), and distinguish Single-shot from Interactive conditions. Record A/B/AB/M for behaviorally classifiable generated RTL. Record INVALID at the interaction/run level when extraction, parsing, elaboration, or required formal checks prevent classification; do not conflate INVALID with M, which means the RTL is inconsistent with all certified interpretations. Record ASK/ASSUME/MISINTERPRET/INVALID interaction outcomes separately. Use the same requirement text and applicable extraction/formal pipeline across compared conditions.

The frozen target ranges are 80–120 ambiguity candidates, 40–80 certified cases after rejection, 20–40 unambiguous controls, and 20–40 rejected/negative candidates. These are targets, not achieved counts. Never substitute an outline label such as “interpretation accuracy” or “clarification frequency” for a frozen metric without a prospective amendment defining it.

## 4.3 Results Freeze and Discussion

Before final analysis, freeze benchmark membership, certification labels, annotation data, model/version list, prompt templates, sampling settings, formal-tool versions, metrics, and primary hypotheses. Record any later changes and whether they were made before or after viewing model outcomes.

For every table, report its denominator, exclusions, incomplete runs, and evidence path. Discuss sampling, tool modeling, prompt sensitivity, reviewer subjectivity, benchmark coverage, and other observed limitations only after the underlying data are available. Hypotheses, target ranges, and planned work are not results.

