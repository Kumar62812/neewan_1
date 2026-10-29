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
- **Most recent author approval (2026-10-28)**: T05 P02 consistency is **DONE** for `T05_P02_CLOSURE_REVIEW_v1`; see the [approved review artifact](../project-state/T05_P02_CLOSURE_REVIEW_v1.md) and [approval record](./approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md). T06 P02 technical/provenance closure has a [draft review](../project-state/T06_P02_CLOSURE_REVIEW_v1.md) and remains **IN PROGRESS**, not complete. The O5 hashes are recorded as author-supplied values and were not independently rehashed in this repository update.
- **Review policy**: human reviews occur after the technical work. Formal evidence before then is provisional with respect to linguistic ambiguity certification.
- Historical snapshot vs verified reality: `main` at `83046997dce165fd3b40c190f7dffa1e280b2c86` contains P02/P05 executed evidence; the inherited `README.md` and compass contain earlier pre-execution status assertions. See [conflicts](CONFLICTS_AND_NEXT_ACTION.md).

## Security and visibility

This repository is **public**. Do not commit API keys, unpublished local-only prompts, private human review correspondence, or other sensitive data. Review local-only packages separately before any publication decision. A public draft branch does not imply redistribution or publication approval.

## Pilot benchmark inventory (C1)

- [P01–P12 pilot case inventory and readiness register](../project-state/C1_PILOT_BENCHMARK_INVENTORY.md)
- [Machine-readable inventory evidence](../project-state/evidence/C1_PILOT_CASE_INVENTORY_v1.json)

C1 records observable repository paths and known evidence/gates; it does not certify cases or infer that missing local-only artifacts never existed.

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

Both fresh formal runners exited 0; all 22 validator checks and all four C3 regression tests passed. T06 and the known P05 reviewer-form version gate remain open.
