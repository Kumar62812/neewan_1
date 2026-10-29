# D3 — Technical Outcome Labels: Implementation and Verification

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Status:** IMPLEMENTATION CANDIDATE CI-PASS — AUTHOR APPROVAL PENDING  
**Decision source:** [A3 Protocol Conflict Decision Matrix](A3_PROTOCOL_DECISION_MATRIX_v1.0.md), D3  
**Normative baseline:** [Frozen plan §11](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/FORMAL_AMBIG_RTL_PLAN.md#L103)

## 1. Findings carried forward

A3 D3 records that the draft evaluator at `research/llm-evaluation-pipeline` classified compile/formal command status as `pass`, `fail`, `timeout`, or `not_run`; any nonzero exit was treated as `fail`. That conflates a formal counterexample with a tool failure and does not emit the plan's `INVALID`, `INCOMPLETE`, or `INCONCLUSIVE` technical labels.

The evaluator source was not present on this branch before this task. This task ports the traceable runner into the research sequence branch as a separate candidate version; it does not rewrite or amend the open PR #7 branch.

## 2. D3 implementation contract

The runner now records `technical_failure_label`, restricted to the plan's three technical-failure labels, separately from the extraction/generation, compilation and formal-stage statuses.

| Evidence observed | D3 result | Rule |
|---|---|---|
| Empty response or required RTL absent | `INCOMPLETE` | No required design content was received |
| RTL module declaration present but `endmodule` missing | `INCOMPLETE` | Treat a truncated module as missing content, not as a compiler-proven RTL defect |
| Recognized parser/compile/elaboration diagnostic | `INVALID` | Invalidity is emitted only when the diagnostics support the conclusion |
| Timeout, missing executable, process signal crash, formal tool error, or unclassified nonzero formal exit | `INCONCLUSIVE` | A tool/runner failure is not evidence of an RTL mismatch |
| Formal adapter emits `FORMAL_RESULT=COUNTEREXAMPLE` | No D3 failure label | The completed formal counterexample is retained for later behavioral classification; it is not converted to `M` here |
| Formal adapter emits `FORMAL_RESULT=INVALID` or `FORMAL_RESULT=INCONCLUSIVE` | Corresponding technical label | Explicit adapter signal is retained |
| Formal command completes with exit code zero | No D3 failure label | This does not itself choose A/B/AB/M or certify a case |

For reliable formal nonzero-exit handling, an adapter should write exactly one standalone line:
`FORMAL_RESULT=PASS`, `FORMAL_RESULT=COUNTEREXAMPLE`, `FORMAL_RESULT=INVALID`, or `FORMAL_RESULT=INCONCLUSIVE`.
An unmarked nonzero formal exit defaults to `INCONCLUSIVE`. This is intentionally conservative. A completed check with no D3 technical failure still requires the separate, protocol-approved behavioral classifier.

## 3. Code and test artifacts

- Runner: [`tools/llm_eval/run_pipeline.py`](../../tools/llm_eval/run_pipeline.py)
- Offline regression fixtures: [`tools/llm_eval/test_d3_outcomes.py`](../../tools/llm_eval/test_d3_outcomes.py)
- CI workflow: [`d3-technical-outcome-labels.yml`](../../.github/workflows/d3-technical-outcome-labels.yml)

The fixtures cover empty and truncated responses, clarification-only output, syntax error, elaboration error, unknown compile exit, forced timeout, missing tool, process crash, formal timeout, unmarked nonzero formal exit, explicit counterexample, explicit invalid formal model, formal tool crash, and normal completed formal execution. They use local subprocesses and synthetic outputs only—no model call, scored experiment, human review or real RTL formal run.

## 4. Verified run evidence

- Machine-readable evidence: [D3 run record](evidence/D3_TECHNICAL_OUTCOME_LABELS_RUN_40822948756.json).
- Tested implementation commit: `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2`.
- Workflow: [run 40822948756](https://github.com/Kumar62812/neewan_1/actions/runs/40822948756), completed successfully. Python 3.12.15; syntax compilation passed; 15/15 offline regression tests passed, with zero failures and zero skips.

## 5. Evidence and limitations

- No model was invoked and no scored run was created.
- No historical P01/P02/P05 metadata, RTL, formal evidence, counterexample, run log or manifest was changed.
- No behavior class `M` is assigned by this D3 layer.
- This branch's runner is a D3 implementation candidate and is not yet integrated into or merged back into PR #7.
- **Verified CI:** [GitHub Actions run 40822948756 — PASS](https://github.com/Kumar62812/neewan_1/actions/runs/40822948756). Python 3.12.15; syntax compilation passed; all 15 offline regression tests passed (0 failed, 0 skipped). The tested source commit is pinned in the machine-readable evidence record.
- D3's recorded status remains pending author approval; the workflow's passing tests would verify implementation behavior, not approve the research protocol or unblock Gate 4.

## 5. Verified run evidence

- Machine-readable evidence: [D3 run record](evidence/D3_TECHNICAL_OUTCOME_LABELS_RUN_40822948756.json).
- Tested implementation commit: `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2`.
- Workflow: [run 40822948756](https://github.com/Kumar62812/neewan_1/actions/runs/40822948756), completed with conclusion `success`.
- Steps: `py_compile` PASS; offline regression fixtures PASS, 15/15.
- Test scope: synthetic outputs and local subprocesses only. No model call, RTL formal run, human review or scored experiment.

## 6. Closure requirements

D3 implementation behavior is CI-verified for the covered fixtures. D3 governance/author approval remains pending until an explicit author approval of the named implementation version is recorded. Gate 4 remains blocked by the independent D3/D4/D5/D10/D13 protocol and evaluator requirements, the approved status of the experiment plan, and the other project-level gates.
