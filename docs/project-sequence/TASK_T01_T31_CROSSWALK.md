# T1–T31 task to 00–22 stage crosswalk

**Status caveat:** The authoritative approved 31-task master plan and complete closure packets have **not** been located in the published GitHub tree. The statuses below use explicitly reported user instructions and existing branch observations; they are not independent approval evidence. Unknown titles are deliberately not reconstructed. Stage identifiers are navigation labels, not a replacement numbering scheme.

| Master task | Best-supported objective | Evidence/approval status | Related stages |
|---|---|---|---|
| T01 | Baseline/reconciliation | User-reported APPROVED AS PARTIAL baseline; no final DONE approval | 02/03 |
| T02 | Governance/methods freeze | User-reported APPROVED AS PARTIAL; supervisor decisions gated to T21 | 02 |
| T03 | Research source review/audit | Author approval PENDING; external source audit open | 01/02 |
| T04 | P01 control validation | Author-reported APPROVED on 2026-10-25; verified closure artifact in repo UNKNOWN | 03 |
| T05 | P02 requirements/specification consistency and provenance | **DONE — author approved `T05_P02_CLOSURE_REVIEW_v1` on 2026-10-28**; see [review artifact](../project-state/T05_P02_CLOSURE_REVIEW_v1.md) and [approval record](./approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md) | 04 |
| T06 | P02 formal/provenance closure | **DONE — author approved `T06_P02_CLOSURE_REVIEW_v1` on 2026-10-29**; see [closure review](../project-state/T06_P02_CLOSURE_REVIEW_v1.md) and [approval record](./approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md) | 05 |
| T07 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T08 | Case template v1, runner and negative controls | Approved scope described in Amendment 06, but execution/closure unverified | 06 |
| T09 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T10 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T11 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T12 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T13 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T14 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T15 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T16 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T17 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T18 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T19 | Parallel-preparation workstream (exact master-plan wording unverified) | Planning permitted; execution details and closure UNKNOWN | 02/15 |
| T20 | Follow-on work after T8 (exact master-plan wording unverified) | Conditional; closure UNKNOWN | 14/15 |
| T21 | Supervisor decision checkpoint (exact master-plan wording unverified) | Decisions pending | 02/15 |
| T22 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T23 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T24 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T25 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T26 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T27 | Later gated task (exact master-plan wording unavailable) | Blocked by T3 audited sources before closure as reported | 20 |
| T28 | End of technical project before external reviews | Future gate; exact master-plan wording unavailable | 20 |
| T29 | Annotation/certification records | External-review execution after technical completion; exact master-plan wording unavailable | 21/22 |
| T30 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |
| T31 | UNKNOWN — approved master-plan title not located in published snapshot | UNKNOWN — do not invent or mark DONE | UNMAPPED |

## Scope amendments (reported, not freshly verified against signed master plan)

- Amendment 01: additional governance controls for per-task author approval and post-technical external review; full approved text/version requires retrieval.
- Amendment 02: carry P02 provenance, P01 archive rehash, README/repo-map/PR #6 conflicts and canonical checkout confirmation as separate items.
- Amendment 03: exact approval/version **UNKNOWN**.
- Amendment 04: T4 may run while T3 audit remains open; T3 must close before T27.
- Amendment 05: **Core:** P02, P05, P06, P08, P03, P04; **Extensions:** P07, P09–P12; P01 outside both. No invented Tier 1/2 names.
- Amendment 06: T8 template = R, S1/S2, two mapped reference RTLs, properties, two negative controls, expected-failure witnesses, miter harness, consistency review, metadata, runner and immutable per-run evidence. Task 29, not T8, contains annotation/certification folders. Three model prompt conditions: R, S1, S2. Scoring against both interpretations yields I1-only/I2-only/both/neither/inconclusive. Formal work on case N+1 requires author approval of case N.
- Any later amendment: **UNKNOWN until version/approval provenance is supplied**.

## Closure rules

A task may be marked DONE only on explicit **author approval of its named version** after verification. PARTIAL approval is not DONE. Simulated reviews do not satisfy external human reviews. No task status should be inferred from a model response, a branch or a roadmap.

**Latest closure:** T06 P02 formal/provenance closure is **DONE** for the named v1 review under the recorded [author approval](./approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md). C3's Linux run is separate reproducibility evidence. The project is not complete: other mapped/unmapped tasks, missing core cases, governance decisions, evaluator/protocol validation, benchmark-wide reproduction and publication/release gates remain. Because the authoritative T1–T31 master file is still unavailable in the verified tree, this crosswalk does not invent a new official T-number as the next task.
