# A5 — A1–A4 Consistency and Gate-Readiness Record

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Status:** A5 documentation check completed; scientific gate decisions remain pending.

## 1. Purpose

Check that the four preceding work products fit together, identify the exact current state of the A1–A4 artifact chain, and record what is ready versus what remains blocked. This is a documentation and consistency check; it does not amend frozen sources or change scientific decisions.

## 2. A1–A4 artifact reconciliation

| Task | Artifact | Current state | Consistency finding |
|---|---|---|---|
| A1 | [Project-sequence state reconciliation](../project-sequence/A1_STATE_RECONCILIATION.md) | Present on this branch | Remote repository/evidence status and limitations are recorded. The companion dated report `A1_PROJECT_STATE_RECONCILIATION_2026-10-28.md` is on branch `research/a1-reconciliation-t06`, not this branch. |
| A2 | [Research scope freeze v1.0](A2_RESEARCH_SCOPE_FREEZE_v1.0.md) and [D1–D16 register](A2_SOURCE_INCONSISTENCY_REGISTER.md) | Present; A2 author approval pending | A2 consolidates the scope and records 16 inconsistencies without silently resolving them. |
| A3 | [Protocol decision matrix v1.0](A3_PROTOCOL_DECISION_MATRIX_v1.0.md), [author decision form](A3_AUTHOR_DECISION_FORM.md), and [amendment template](../amendments/AMENDMENT_TEMPLATE.md) | Present; dispositions pending | Recommendations and decisions are distinguished. No A3 decision is treated as approved merely because the matrix exists. |
| A4 | [AM-001](../amendments/AM-001_primary-taxonomy.md), [AM-002](../amendments/AM-002_status-vocabulary-crosswalk.md), [AM-003](../amendments/AM-003_p01-gate-deviation.md), and [AM-004](../amendments/AM-004_case-layout.md) | Four drafts present; none effective | The drafts address D1, D2, D9 and D14. Each keeps its disposition/approval fields pending and records the source-hash baseline as transcribed from A3 rather than independently recomputed. |

## 3. Cross-consistency checks

### 3.1 Evidence and source preservation

- The frozen `Files/FORMAL_AMBIG_RTL_PLAN.md` and the operative protocols were not edited by A1–A4.
- Existing P01/P02/P05 case metadata, RTL, formal run logs, witnesses and evidence manifests were not edited by the A4 amendment-drafting work.
- A4 drafts are separate records read alongside their source documents. None is effective.
- A2's source-inconsistency register remains a record of identified issues, not a record that those issues have been resolved.

### 3.2 Decisions remain distinguishable from recommendations

The following remain pending in A3:
- D1 — primary taxonomy versus secondary thematic tags.
- D2 — certification status versus lifecycle stage.
- D9 — treatment of the P01 freeze-gate deviation.
- D14 — canonical layout for new benchmark cases.

No approval is inferred from the creation of the four amendment drafts. In particular, AM-003 does not itself override the P01 freeze gate or authorize T08.

### 3.3 Existing scientific status is preserved

- P01 formal evidence exists, but the golden-template freeze remains open.
- P02 is retained as a deterministic control; T05 is approved for its named review version, while T06 remains in progress.
- P05 has a recorded formal distinction under its tested model, but independent human plausibility and ambiguity certification are not established by A1–A4.
- The P05 exploratory pilot is not converted into a primary benchmark-wide result.
- A timeout, missing response, invalid RTL, or incomplete formal run must not be promoted to a proven mismatch.

## 4. Readiness for the next technical task

| Dependency | Current record | Readiness |
|---|---|---|
| A1–A4 files reconciled | This file and the linked work products | Complete as documentation |
| D1 taxonomy decision | A3 form and AM-001 | Pending |
| D2 status-vocabulary decision | A3 form and AM-002 | Pending |
| D9 gate-deviation decision | A3 form and AM-003 | Pending |
| D14 case-layout decision | A3 form and AM-004 | Pending |
| T08 template implementation/validation | Not performed by A1–A5 documentation | Not yet verified |
| Gate authorization | No new authorization record was made | Not established |

This record does not change the operative rule: until the required decisions and any effective amendments are recorded under the project change-control procedure, the original frozen sources remain operative and T08 must not be described as authorized by A5 alone.

## 5. A5 acceptance checks

- [x] A1–A4 artifacts are linked and their status is stated.
- [x] The four A4 drafts map to D1, D2, D9 and D14.
- [x] Approval state is distinguished from the existence of a document.
- [x] Existing scientific evidence and case status are not upgraded.
- [x] No frozen source, case metadata, RTL, formal result or evidence manifest was modified.
- [x] Open dependencies for the next technical task are explicitly listed.
- [x] The project log records this A5 reconciliation.

## 6. Completion boundary

**A5 documentation check: COMPLETE.** This means the A1–A4 records have been cross-checked and their present limits are documented. It does not mean D1/D2/D9/D14 are approved, T08 is authorized, P01 is frozen, P05 is certified ambiguous, or T06 is closed.
