# A1 — Project State Reconciliation

**Project:** FORMAL-AMBIG-RTL
**Inspection date:** 2026-10-28 (rechecked 2026-10-28 23:00 IST against the live remote)
**Repository:** Kumar62812/neewan_1
**Report location:** `docs/project-state/A1_PROJECT_STATE_RECONCILIATION_2026-10-28.md` on branch `research/a1-reconciliation-t06`

Each claim below is marked **[verified]** if it was rechecked against the remote with git on 2026-10-28,
or **[updated]** where the remote had moved on since the original inspection.

## 1. Repository and branch state

- The inspected main commit is `83046997dce165fd3b40c190f7dffa1e280b2c86`, which is the merge commit of PR #6. **[verified]** `main` still points here.
- The branch `formal-ambig-rtl-foundation` (`881c00ec5c68…`, the PR #2 head) is 46 commits behind main and has no commits ahead of main. **[verified]**
- Commit `109336c88433be1c3f5836bfde351b5e0c841b0c` contains project-sequence documentation and is two commits ahead of the inspected main revision (`5536595`, `109336c`). **[verified]**
- **[updated]** The head of `research/end-to-end-sequence` is now `762c68df4217d8c6cbf0c93ce4447d1bc136ba88`, nine commits ahead of main and zero behind. The seven newer commits (`dc2656d` … `762c68d`, all 2026-10-28 22:07–22:08 IST) record the T05 author approval and update the navigation registers.
- The project-sequence changes are **not merged into main**. `Files/Research_Papers/benchmark/pilot_v0_1/` is byte-identical between `main` and the branch head, so the branch changes only documentation. **[verified]**

## 2. P01 status

- Existing formal evidence and preservation records are present (`Files/Research_Papers/benchmark/pilot_v0_1/P01/`, `02_CERTIFICATION/`). **[verified]**
- Independent certification is not established by the inspected project-state records. **[verified]**
- The P01 golden-template freeze remains an open item ("P01 Golden Template: NOT FROZEN" in `governance/07_PROJECT_LOG.md`). **[verified]**

## 3. P02 status

- P02 formal-verification evidence and run records are published (`evidence/run-01`, `evidence/run-02`). **[verified]** All 50 run-02 and 43 run-01 SHA-256 manifest entries recompute without mismatch.
- The project records distinguish technical evidence from task-closure documentation. **[verified]**
- **[updated]** T05 is recorded as **DONE (author-approved 2026-10-28)** in `docs/project-sequence/approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md`, and T06 as **unblocked / authorised to begin**.
- **[updated]** The two O5 hashes recorded in that approval as "author-supplied" were rehashed against the committed bytes at `762c68d` and match: `P02_RESULTS.md` `0b508df3…82bb6b`, `metadata.json` `6488b260…35affde`.
- Existing run-02 evidence and hashes are preserved. The P02 tree is unchanged from `109336c` to `762c68d`. **[verified]**
- T06 closure review v1 is drafted in this branch (`docs/project-state/T06_P02_CLOSURE_REVIEW_v1.md`), awaiting author approval.

## 4. P05 status

- P05 formal comparison evidence is recorded (`P05/evidence/run-01`, `run-02`). **[verified]**
- Independent human plausibility certification remains open in the inspected records. **[verified]**
- The published model-evaluation results (PR #9, three Groq samples) are scoped to the documented pilot and must not be presented as general accuracy or certified ambiguity. **[verified]**

## 5. Pull-request status at inspection

| PR | Head branch | State | Basis |
|---|---|---|---|
| #6 | `p02-p05-clean-publication` | merged | `main` HEAD is "Merge pull request #6" **[verified]** |
| #7 | `research/llm-evaluation-pipeline` | open, unmerged | head not in `main`; `refs/pull/7/merge` still exists **[verified]** |
| #8 | `docs/phase-based-organization` | open, unmerged | same basis **[verified]** |
| #9 | `study/p05-groq-pilot-20261024` | open, unmerged | same basis **[verified]** |

These states come from git refs, because the GitHub API was not available to this inspection. Draft flags
were not rechecked. Recheck them before relying on them as current state.

## 6. Main discrepancies

1. The Project Compass on main (`Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md`, lines 3 and 65) still says **"CURRENT: P01 / NOT STARTED"**, despite existing P01 evidence and published P02/P05 work. **[verified]**
2. The foundation branch is 46 commits behind main. **[verified]**
3. Project-sequence documentation, now including the T05 approval, exists only on `research/end-to-end-sequence` and is not part of main. **[verified, updated]**
4. Technical evidence, author approvals, independent certification and template-freeze status must remain separate. **[verified]**
5. **[new]** The T05 approval record names `T05_P02_CLOSURE_REVIEW_v1` and pins commit `109336c` as its version reference, but **the review document itself was not committed** in `109336c` or anywhere on the branch. The approval therefore points to a document the repository did not contain. This branch adds the file unchanged (SHA-256 `ccc6a7d637f424937ce349a207f02bd287b10de224e45ee64c5b971d9bd79a04`, the exact bytes the author approved) at `docs/project-state/T05_P02_CLOSURE_REVIEW_v1.md`. The approval record is not edited.
6. **[new]** `docs/reproducibility/p02-p05-reproduction.md` and `docs/project-state/P02_READINESS.md` still describe PR #6 as "open … not merged", although it is merged. They are historical records; correct them only through a dated note, not by rewriting.

## 7. A1 outcome

The repository contains existing technical evidence, but its project-status records are not fully aligned.
Since the original inspection, T05 has been approved and recorded on the sequence branch. The remaining
alignment gaps are the stale Compass and PR #6 wording on main and in historical docs, the missing review
document behind the T05 approval (fixed in this branch), and the unmerged sequence branch.

This report records the discrepancies found during inspection.
It does not modify existing formal evidence, certify any benchmark
case, or claim that outstanding project tasks are complete.

## 8. Recommended follow-up (not performed by A1)

| # | Action | Needs |
|---|---|---|
| 1 | Merge this branch into `research/end-to-end-sequence` so the T05 review file sits beside its approval | Author |
| 2 | Add a dated correction note to the Compass on main (do not rewrite the historical text) | Author decision |
| 3 | Decide when `research/end-to-end-sequence` is proposed to `main` | Author |
| 4 | Decide whether to delete or archive `formal-ambig-rtl-foundation` (fully contained in main) | Author |
| 5 | Approve T06 closure review v1 with decisions P1–P3 | Author |

## 9. Completion checklist

- [x] Remote branch and commit relationships inspected.
- [x] Existing P01, P02 and P05 status records inspected.
- [x] Relevant pull-request states inspected.
- [x] Major project-state discrepancies documented.
- [x] Report saved in the project working tree (`docs/project-state/`, branch `research/a1-reconciliation-t06`).
- [ ] Report appended to GitHub. Pending: the author pushes this branch or applies the patch. The inspection session had read-only access.