# D3 — Technical Outcome Labels: Implementation, Verification, and Approval

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Status:** **IMPLEMENTATION CI-PASS — AUTHOR-APPROVED FOR THE NAMED VERSION**  
**Approved implementation:** `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2`  
**Decision source:** [A3 Protocol Conflict Decision Matrix](A3_PROTOCOL_DECISION_MATRIX_v1.0.md), D3  
**Approval record:** [D3 author approval, 2026-10-29](../project-sequence/approvals/D3_TECHNICAL_OUTCOME_LABELS_APPROVAL_2026-10-29.md)  
**Normative baseline:** [Frozen plan §11](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/FORMAL_AMBIG_RTL_PLAN.md#L103)

## 1. Finding and scope

The prior draft evaluator treated any nonzero compile/formal exit as `fail`, conflating a genuine formal counterexample with infrastructure or tool failure. D3 implements and tests the plan's three technical-failure labels. The tested runner is a versioned implementation on `research/end-to-end-sequence`; it has not been merged into or substituted for the open PR #7 branch.

## 2. Implementation contract

| Evidence observed | D3 result | Rule |
|---|---|---|
| Empty response or required RTL absent | `INCOMPLETE` | Required design content was not received. |
| RTL module declaration exists but `endmodule` is missing | `INCOMPLETE` | Truncated content is not assumed to be a compiler-proven RTL defect. |
| Recognized parser, compile, or elaboration diagnostic | `INVALID` | Emit only when diagnostics support RTL/model invalidity. |
| Timeout, missing executable, process crash, formal tool error, or unclassified nonzero formal exit | `INCONCLUSIVE` | Tool/runner failure is not evidence of RTL mismatch. |
| Formal adapter emits `FORMAL_RESULT=COUNTEREXAMPLE` | No D3 failure label | Preserve as a completed formal result for the later behavioral-classification stage; do not convert it to `M` here. |
| Formal adapter emits `FORMAL_RESULT=INVALID` or `FORMAL_RESULT=INCONCLUSIVE` | Corresponding technical label | Honor the explicit adapter result. |
| Formal command completes with exit code zero | No D3 failure label | Behavioral class and certification remain separate decisions. |

For nonzero formal exits, an adapter should emit a standalone marker: `FORMAL_RESULT=PASS`, `FORMAL_RESULT=COUNTEREXAMPLE`, `FORMAL_RESULT=INVALID`, or `FORMAL_RESULT=INCONCLUSIVE`. An unmarked nonzero exit defaults to `INCONCLUSIVE`. The D3 layer never assigns `M`.

## 3. Implementation and regression artifacts

- [Traceable runner](../../tools/llm_eval/run_pipeline.py)
- [Offline regression fixtures](../../tools/llm_eval/test_d3_outcomes.py)
- [CI workflow](../../.github/workflows/d3-technical-outcome-labels.yml)
- [Passing GitHub Actions run 40822948756](https://github.com/Kumar62812/neewan_1/actions/runs/40822948756)
- [Machine-readable run evidence](evidence/D3_TECHNICAL_OUTCOME_LABELS_RUN_40822948756.json)

## 4. Verification evidence

CI ran on `ubuntu-latest` with Python 3.12.15. Syntax compilation passed and the offline regression suite passed **15/15 tests** (0 failures, 0 skipped). The fixtures cover empty/truncated responses, clarification-only output, syntax/elaboration diagnostics, unknown compile exits, timeouts, unavailable/crashed tools, formal-result sentinels, unmarked nonzero formal exits, and a completed formal command.

The tests use synthetic outputs and local subprocesses. No model call, scored experiment, actual RTL formal run, or human review occurred. The result is implementation evidence for the named version, not full end-to-end production validation.

## 5. Author approval

G. Naveen explicitly approved implementation commit `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2` on 2026-10-29 after CI passed. See the [versioned approval record](../project-sequence/approvals/D3_TECHNICAL_OUTCOME_LABELS_APPROVAL_2026-10-29.md). The A3 author decision form records `ACCEPT` for D3.

The approval is version-specific and does not inherit to altered code. It does not approve D4 or D5, merge the code into PR #7, authorize scored experiments, or close Gate 4. PR #7 integration and end-to-end validation remain open.
