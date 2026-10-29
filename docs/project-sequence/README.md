# FORMAL-AMBIG-RTL — project-sequence navigation

**Updated index prepared 2026-10-28 on `research/end-to-end-sequence`.** This branch brings the published `main` evidence tree together with the previously authored 00–22 [end-to-end research roadmap](../roadmap/end-to-end-research-sequence.md). The index **does not declare missing research complete or certify ambiguity**.

## Start here, in order

1. [Stage 00–22 work and exit-gate register](STAGE_REGISTER.md) — the continuous project flow, evidence and next-work conditions.
2. [Original T1–T31 task/approval crosswalk](TASK_T01_T31_CROSSWALK.md) — explicitly marks unavailable master-plan definitions as **UNKNOWN**, not guessed.
3. [Artifact and evidence index](ARTIFACT_AND_EVIDENCE_REGISTER.md) — source documents, HDL, formal witnesses, hashes and reproducibility pointers.
4. [Branches, PRs and research deltas](BRANCH_PR_REGISTER.md) — draft branches remain separate and unapproved unless independently established.
5. [Approvals and decision provenance](APPROVAL_AND_DECISION_REGISTER.md) — distinguishes author-reported decisions from independently verified signed records.
6. [Contradictions, blockers and next authorised action](CONFLICTS_AND_NEXT_ACTION.md) — do not resume execution by assuming a task is DONE.

## Evidence boundaries

- The scientific [frozen plan](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/FORMAL_AMBIG_RTL_PLAN.md) and [repository compass](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md) are preserved as-is. Their historical status statements are **not necessarily current**.
- P01 accepted evidence and source caveats, P02 formal runs and P05 formal runs remain in their original paths; no evidence, witness, run manifest or historical log was rewritten as part of this branch navigation.
- **Most recent author approval (2026-10-29)**: T06 P02 formal/provenance closure is **DONE** for `T06_P02_CLOSURE_REVIEW_v1`; see the [approved closure review](../project-state/T06_P02_CLOSURE_REVIEW_v1.md) and [approval record](./approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md). T05 remains DONE for its own named version; see its [approval record](./approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md). These task closures do not imply full project completion or ambiguity certification.
- **Review policy**: human reviews occur after the technical work. Formal evidence before then is provisional with respect to linguistic ambiguity certification.
- Historical snapshot vs verified reality: `main` at `83046997dce165fd3b40c190f7dffa1e280b2c86` contains P02/P05 executed evidence; the inherited `README.md` and compass contain earlier pre-execution status assertions. See [conflicts](CONFLICTS_AND_NEXT_ACTION.md).

## Security and visibility

This repository is **public**. Do not commit API keys, unpublished local-only prompts, private human review correspondence, or other sensitive data. Review local-only packages separately before any publication decision. A public draft branch does not imply redistribution or publication approval.

## Pilot benchmark inventory (C1)

- [P01–P12 pilot case inventory and readiness register](../project-state/C1_PILOT_BENCHMARK_INVENTORY.md)
- [Machine-readable inventory evidence](../project-state/evidence/C1_PILOT_CASE_INVENTORY_v1.json)

C1 records observable repository paths and known evidence/gates; it does not certify cases or infer that missing local-only artifacts never existed.

## D1 — taxonomy decision readiness

- [D1 taxonomy decision-readiness audit](../project-state/D1_TAXONOMY_DECISION_READINESS.md)
- [A3 decision matrix](../project-state/A3_PROTOCOL_DECISION_MATRIX_v1.0.md) · [author decision form](../project-state/A3_AUTHOR_DECISION_FORM.md) · [draft amendment AM-001](../amendments/AM-001_primary-taxonomy.md)

The technical recommendation is Option A: C1–C5 remains the single primary category and the six RP §5 dimensions become optional secondary tags. This is **not an approval**. D1 remains pending until an explicit author disposition and approved amendment are recorded.

## D2 — certification status and lifecycle decision readiness

- [D2 decision-readiness audit](../project-state/D2_STATUS_LIFECYCLE_DECISION_READINESS.md)
- [A3 decision matrix](../project-state/A3_PROTOCOL_DECISION_MATRIX_v1.0.md) · [author decision form](../project-state/A3_AUTHOR_DECISION_FORM.md) · [draft amendment AM-002](../amendments/AM-002_status-vocabulary-crosswalk.md)

The recommendation is Option A: separate PLAN-aligned `certification_status`, benchmark `lifecycle_stage`, and release/freeze state, linked by an evidence-guarded crosswalk. P02's `technical_verification_complete` must not be mistaken for certification. **D2 remains pending**; AM-002 is not effective and no existing metadata was migrated.

## P02/P05 source and evidence integrity (C2)

- [C2 P02/P05 retained evidence and source alignment audit](../project-state/C2_P02_P05_EVIDENCE_ALIGNMENT.md)
- [Machine-readable C2 CI result](../project-state/evidence/C2_P02_P05_VALIDATION_RUN_40808854269.json)
- [Successful C2 GitHub Actions run](https://github.com/Kumar62812/neewan_1/actions/runs/40808854269)

C2 passed the retained-run manifest integrity checks and selected source-snapshot identity checks. The known P05 reviewer-form version difference remains a gate before human-review data collection.




## C3 — P02/P05 Linux formal reproduction

- **PASS:** [GitHub Actions run #2](https://github.com/Kumar62812/neewan_1/actions/runs/40809992594)
- [C3 reproduction report](../project-state/C3_P02_P05_LINUX_REPRODUCTION.md)
- [Machine-readable execution evidence](../project-state/evidence/C3_P02_P05_LINUX_REPRODUCTION_v1.json)
- [90-day raw run artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40809992594/artifacts/12870250852)
- [Linux reproduction workflow](../../.github/workflows/p02-p05-formal-reproduction.yml)
- [Output validator](../../Files/Research_Papers/benchmark/pilot_v0_1/validate_formal_reproduction.py)

Both fresh formal runners exited 0; all 22 validator checks and all four C3 regression tests passed. T06 was separately approved and is now DONE. The P05 current-form identity is now explicitly pinned by C4; human-review collection remains blocked until technical completion. The local-asset audit, release-path hygiene, and wider project completion gates remain open.


## C4 — P05 review-input provenance

- [C4 report and validation status](../project-state/C4_P05_REVIEW_INPUT_PROVENANCE.md)
- [Prospective review-input manifest](../../Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/review_input_manifest_v1.json)
- [Validator](../../Files/Research_Papers/benchmark/pilot_v0_1/validate_p05_review_input_bundle.py)
- [Integrity workflow](../../.github/workflows/p05-review-input-integrity.yml)

C4 **PASS**: [61/61 checks and 6/6 tests passed](https://github.com/Kumar62812/neewan_1/actions/runs/40811887068). It pins the exact prospective P05 reviewer-facing materials and coordinator/technical provenance, records the distinct historical run-02 form, and does not authorize review before technical completion. [Evidence record](../project-state/evidence/C4_P05_REVIEW_INPUT_INTEGRITY_RUN_40811887068.json) · [artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40811887068/artifacts/12870139889).


## C5 — reusable-template and negative-control readiness

- [C5 readiness audit and gate findings](../project-state/C5_TEMPLATE_AND_NEGATIVE_CONTROL_READINESS.md)
- [Read-only audit script](../../Files/Research_Papers/benchmark/pilot_v0_1/audit_c5_template_readiness.py)
- [Regression tests](../../Files/Research_Papers/benchmark/pilot_v0_1/tests/test_audit_c5_template_readiness.py)
- [GitHub Actions workflow](../../.github/workflows/c5-template-readiness-audit.yml)

C5 is a bounded readiness audit, **not a template freeze**. It checks the schema/template mapping, P01's explicit not-frozen status, D2/D14 governance gate, and the distinct role of a deliberately wrong negative control. The readiness outcome remains BLOCKED until the open governance and role-aware validation gates are resolved. The official T1–T31 task numbering is not inferred.

**Verified CI:** [run 40813383592 — PASS](https://github.com/Kumar62812/neewan_1/actions/runs/40813383592): 10/10 audit checks and 6/6 regression tests passed. Readiness intentionally remains `BLOCKED_NOT_FROZEN`. [Evidence summary](../project-state/evidence/C5_TEMPLATE_READINESS_AUDIT_RUN_40813383592.json) · [report artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40813383592/artifacts/12871850130).


## C6 — non-binding schema-to-template mapping proposal

- [C6 proposal and decision questions](../project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.md)
- [Machine-readable 18-field mapping](../project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.json)
- [Validation report](../project-state/C6_SCHEMA_TEMPLATE_MAPPING_VALIDATION.md)
- [Validator](../../Files/Research_Papers/benchmark/pilot_v0_1/validate_c6_schema_mapping_proposal.py) · [tests](../../Files/Research_Papers/benchmark/pilot_v0_1/tests/test_validate_c6_schema_mapping_proposal.py) · [workflow](../../.github/workflows/c6-schema-template-mapping.yml)

C6 proposes, but does not implement, a normative field mapping. [CI run 40814081793 passed](https://github.com/Kumar62812/neewan_1/actions/runs/40814081793): 10/10 validation checks and 7/7 tests passed. [Evidence summary](../project-state/evidence/C6_SCHEMA_TEMPLATE_MAPPING_RUN_40814081793.json) · [report artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40814081793/artifacts/12871731814). D2 (lifecycle/status and scientific classification vocabulary) and D14 (canonical case layout) remain unresolved. No canonical source is migrated or frozen.


## C7 — role-aware illustrative fixtures

- [C7 findings and boundaries](../project-state/C7_ROLE_AWARE_FIXTURES.md)
- [Four synthetic fixtures](../../Files/Research_Papers/benchmark/pilot_v0_1/tests/fixtures/c7_role_aware/)
- [Read-only audit](../../Files/Research_Papers/benchmark/pilot_v0_1/audit_c7_role_aware_fixtures.py) · [tests](../../Files/Research_Papers/benchmark/pilot_v0_1/tests/test_audit_c7_role_aware_fixtures.py) · [workflow](../../.github/workflows/c7-role-aware-fixtures.yml)

C7 checks that an unambiguous control need not invent interpretation B, ambiguity/negative candidates require paired structure, and checker-negative controls stay separate. All examples are synthetic and non-binding; D2/D14 remain open and no freeze is implied.

**Verified CI:** [run 40814758386 — PASS](https://github.com/Kumar62812/neewan_1/actions/runs/40814758386), with 53/53 checks and 10/10 regression tests passing. Two earlier syntax-failure runs remain visible in Actions history; the validator was corrected before the final passing run. [Evidence summary](../project-state/evidence/C7_ROLE_AWARE_FIXTURES_RUN_40814758386.json) · [report artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40814758386/artifacts/12871802752).


## D3 — technical outcome label implementation

- [D3 implementation and verification report](../project-state/D3_TECHNICAL_OUTCOME_LABELS.md)
- [Traceable runner](../../tools/llm_eval/run_pipeline.py) · [offline regression tests](../../tools/llm_eval/test_d3_outcomes.py) · [GitHub Actions workflow](../../.github/workflows/d3-technical-outcome-labels.yml)

The D3 implementation version `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2` is **approved by G. Naveen** and passed [CI run 40822948756 (15/15 offline tests)](https://github.com/Kumar62812/neewan_1/actions/runs/40822948756); see the [dated approval record](./approvals/D3_TECHNICAL_OUTCOME_LABELS_APPROVAL_2026-10-29.md) and [machine-readable evidence](../project-state/evidence/D3_TECHNICAL_OUTCOME_LABELS_RUN_40822948756.json). Approval is version-specific. The code is not merged into PR #7; D4/D5 and scored-study gates remain open.

## D4 — MISINTERPRET policy guard

- [D4 policy report](../project-state/D4_MISINTERPRET_POLICY.md)
- [Policy helper](../../tools/llm_eval/misinterpret_policy.py) · [21 regression tests](../../tools/llm_eval/test_misinterpret_policy.py) · [workflow](../../.github/workflows/d4-misinterpret-policy.yml)
- [Passing CI run 40824632602](https://github.com/Kumar62812/neewan_1/actions/runs/40824632602) · [machine-readable evidence](../project-state/evidence/D4_MISINTERPRET_POLICY_RUN_40824632602.json)

The helper assigns `MISINTERPRET` only for valid/extracted RTL, successful compilation, explicit completed formal comparison, behavioral class `M`, and a referenced approved comparison contract. All missing or failed prerequisites fail closed. All 21 offline tests passed. D5 remains pending, so the synthetic test contract is not a real approved research contract; complete evaluator integration and scored use remain blocked.

## D5 — A/B/AB/M comparison-relation decision readiness

- [D5 decision-readiness brief](../project-state/D5_COMPARISON_RELATION_DECISION_READINESS.md)
- [A3 decision matrix](../project-state/A3_PROTOCOL_DECISION_MATRIX_v1.0.md) · [author decision form](../project-state/A3_AUTHOR_DECISION_FORM.md) · [P05 pilot PR #9](https://github.com/Kumar62812/neewan_1/pull/9)

The brief compares equivalence-only, contract-conformance-only, and dual-relation options. Its technical recommendation is Option C: preserve frozen-plan equivalence as primary and report contract conformance separately as secondary, if the author accepts the additional AM-007 change. **D5 remains pending**; the report is not an approval and does not authorize scored study results.

## C8 — C5–C7 cross-artifact integration

- [C8 integration report](../project-state/C8_CROSS_ARTIFACT_INTEGRATION.md)
- [Read-only integration validator](../../Files/Research_Papers/benchmark/pilot_v0_1/audit_c8_integration.py) · [regression tests](../../Files/Research_Papers/benchmark/pilot_v0_1/tests/test_audit_c8_integration.py) · [workflow](../../.github/workflows/c8-cross-artifact-integration.yml)

C8 passed 54/54 integration checks and 11/11 regression tests, with 16/16 pinned objects, 18/18 mapping fields, and four role fixtures verified. [CI run 40816068105](https://github.com/Kumar62812/neewan_1/actions/runs/40816068105) · [evidence](../project-state/evidence/C8_C5_C7_INTEGRATION_RUN_40816068105.json) · [artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40816068105/artifacts/12872102588). D2/D14 remain open, so the result does not authorize a template freeze.
