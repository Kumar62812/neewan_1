# Decision and approval register

The distinction between **repository artifact**, **author-reported approval**, **supervisor-reviewed record**, and **independent human certification** is mandatory. Approval claims are recorded only when the corresponding explicit instruction and versioned record are identified; this register does not infer independent certification.

| Decision | Grounding | Status / limitation |
|---|---|---|
| P01 guide proceed direction | [meeting record](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/02_CERTIFICATION/P01_GUIDE_MEETING_RECORD.md) | Recorded in repo; **not** independent template certification |
| P01 golden-template freeze | [certification folder](https://github.com/Kumar62812/neewan_1/tree/83046997dce165fd3b40c190f7dffa1e280b2c86/02_CERTIFICATION) | Not verified as completed |
| T1 baseline | Author-reported 25 Oct | APPROVED AS PARTIAL; do not call DONE |
| T2 governance | Author-reported 25 Oct | APPROVED AS PARTIAL; supervisor decisions carry to T21 |
| T3 evidence audit | Author-reported 25 Oct | PENDING |
| T4 P01 validation | Author-reported 25 Oct | APPROVED as reported; named closure file/version not verified in GitHub |
| T5 P02 consistency | [Closure review](../project-state/T05_P02_CLOSURE_REVIEW_v1.md) (SHA-256 `ccc6a7d637f424937ce349a207f02bd287b10de224e45ee64c5b971d9bd79a04`); [author approval record](./approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md), pinned review commit `109336c88433be1c3f5836bfde351b5e0c841b0c` | **DONE — explicitly approved by author on 2026-10-28 for `T05_P02_CLOSURE_REVIEW_v1`** |
| T6 P02 closure | [T06 closure review](../project-state/T06_P02_CLOSURE_REVIEW_v1.md); [author approval record](./approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md) | **DONE — explicitly approved by author on 2026-10-29 for `T06_P02_CLOSURE_REVIEW_v1`**; residual local-asset/release hygiene items are non-blocking follow-ups |
| D3 technical outcome labels | [D3 implementation report](../project-state/D3_TECHNICAL_OUTCOME_LABELS.md); [approval record](./approvals/D3_TECHNICAL_OUTCOME_LABELS_APPROVAL_2026-10-29.md); [CI run 40822948756](https://github.com/Kumar62812/neewan_1/actions/runs/40822948756) | **ACCEPTED — G. Naveen approved implementation commit `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2` on 2026-10-29**; 15/15 fixture tests passed. Approval is version-specific; D4/D5 and Gate 4 remain open |
| P05 independent plausibility | [review procedure](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/README.md) | Published repo metadata says 0 human responses at snapshot; later off-repo reviews UNKNOWN |
| P05 technical non-equivalence | [recorded formal result](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md) | Reported technical result, not certification |
| T1–T31 official plan | Not found in GitHub | Full task titles, approval signatures and hashes UNKNOWN; external source needed |

## Scientific governance

- Accepted P01/P02/P05 evidence, historical SHA manifests, witness traces, existing approved specs and historical notes must be preserved without rewriting.
- Scientific protocols may not be silently amended. Keep P05 certified scoring blocked pending a recorded decision resolving the post-technical independent-review policy and original preregistered review gate.
- Approval belongs to the exact content/version; a changed file or new branch does not inherit an old approval.
- Do not publish private user chats, credentials, unpublished full prompt bodies, reviewers' identities or unapproved local-only assets in this public repository.


## T05 P02 closure approval — 2026-10-28

The project author explicitly approved `T05_P02_CLOSURE_REVIEW_v1` at the pinned review commit `109336c88433be1c3f5836bfde351b5e0c841b0c`. See the [approval record](./approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md).

- O1, O2, O3: accepted as cosmetic/modelling assumptions; preserve run-02 hashes.
- O4: P02 confirmed as a deterministic control case within the core benchmark set.
- O5: author-supplied SHA-256 for `P02_RESULTS.md`: `0b508df3c4569bf1ecdc026e70f47e89d1f002b533fc6dd5fe13bac00382bb6b`; for `metadata.json`: `6488b260226c633098d69c3e5dbbd87fd0cd5614ef44993df862d2abe35affde`.
- T05 is DONE for its named review version. T06 is now DONE for its separately approved named review version; see the T06 approval record below.
- The listed hashes are recorded as author-supplied and have not been independently rehashed in this documentation update.

Approved review document (added 2026-10-28, bytes unchanged): [`T05_P02_CLOSURE_REVIEW_v1.md`](../project-state/T05_P02_CLOSURE_REVIEW_v1.md), SHA-256 `ccc6a7d637f424937ce349a207f02bd287b10de224e45ee64c5b971d9bd79a04`. The T06 review content approved by the author is pinned by Git blob ID `cccb18d2d7e67566a45e213f235b29f6d881e4b2` in [the T06 approval record](./approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md); the subsequent status/disposition annotation reflects approval and C3 without changing historical formal evidence.

## T06 P02 closure approval — 2026-10-29

The author explicitly approved `T06_P02_CLOSURE_REVIEW_v1`; see [approval record](./approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md). T06 is DONE for the named review. The C3 Linux P02/P05 reproduction is supplemental, separately retained evidence, not a full-project completion claim.


## D3 technical outcome-label approval — 2026-10-29

G. Naveen explicitly approved the D3 implementation version at `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2`. The exact approval wording and scope are preserved in [the dated approval record](./approvals/D3_TECHNICAL_OUTCOME_LABELS_APPROVAL_2026-10-29.md). The successful CI run [40822948756](https://github.com/Kumar62812/neewan_1/actions/runs/40822948756) passed syntax compilation and 15/15 offline regression tests. This is implementation evidence for D3 only; it does not approve D4/D5 or authorize scored experiments.
