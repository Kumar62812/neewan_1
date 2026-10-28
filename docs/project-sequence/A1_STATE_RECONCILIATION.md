# A1 — Project State Reconciliation

**Project:** FORMAL-AMBIG-RTL  
**Audit date:** 2026-10-28  
**Repository:** `Kumar62812/neewan_1`  
**Audit scope:** Published GitHub repository and recorded project evidence. The author's local working tree was not accessible for this audit.

## 1. Repository and branch snapshot

- Default branch: `main`.
- Main commit used for comparison: `83046997dce165fd3b40c190f7dffa1e280b2c86`.
- Selected continuation branch: `research/end-to-end-sequence`.
- Pre-report branch commit inspected: `1e11b19b7d5af003b3abd1f7f2c10aac41acd4ce`.
- At comparison time, `research/end-to-end-sequence` was 18 commits ahead of `main`, 0 commits behind, with `main` as the merge base.
- `formal-ambig-rtl-foundation` was 0 commits ahead and 46 commits behind `main`; it is not the suitable continuation branch for the current project state.
- Repository visibility is public. The connected GitHub account reported push permission.

**Decision:** Use `research/end-to-end-sequence` for the current sequence documentation and subsequent controlled work. Do not force-update branches or rewrite history.

## 2. Local working tree

The GitHub connector cannot inspect the author's local checkout, untracked files, unstaged edits, or files retained only on the author's computer.

- Local branch and `git status`: **NOT VERIFIED**.
- Local-only artifacts and untracked files: **NOT VERIFIED**.
- Remote branch graph and remote commit relationship: **VERIFIED** as described in §1.

This report therefore makes no claim that the local working tree is clean or that every local-only file has been inventoried.

## 3. Frozen methodology and document consistency

The following documents exist on `main` and were inspected for project scope, status, and decision rules:

- `Files/FORMAL_AMBIG_RTL_PLAN.md` — identified as `v1.0-FROZEN`; describes the evidence chain, case taxonomy, certification criteria, and pilot order.
- `Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md` — still begins with `CURRENT: P01 / NOT STARTED` and restricts work to P01.
- `Files/Research_Papers/docs/research_protocol.md`.
- `Files/Research_Papers/docs/benchmark_schema.md`.
- `Files/Research_Papers/docs/formal_verification_protocol.md`.
- `Files/Research_Papers/docs/annotation_protocol.md`.

The frozen plan and protocols were not modified in this reconciliation. Their methodology is to keep plausible interpretation, behavioural specification, formal distinction, and certification as separate evidence layers.

### Status-document discrepancy

The Compass and `02_CERTIFICATION/00_STATUS.md` contain historical P01-only / pre-P02 statements. Those statements conflict with the later technical evidence already published on `main`:

- P01 formal evidence and its scope are recorded in `02_CERTIFICATION/P01_FORMAL_RESULTS.md` and `docs/reproducibility/p01-reproduction.md`.
- P02 executed results are recorded in `Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_RESULTS.md`.
- P05 executed results are recorded in `Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md`.

Treat the older status wording as a historical snapshot, not as evidence that the later work does not exist. Do not silently rewrite the frozen plan or accepted evidence to resolve the mismatch.

## 4. Existing technical evidence inventory

### P01 — deterministic control

- Formal result summary records the reference design as PASS and the deliberately incorrect design as an assertion failure.
- The stated tested source is base revision `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35` plus the retained path-only SBY repair, whose recorded SHA-256 is `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`.
- The accepted evidence archive `re/p01-20260930T220622Z-rev1.tar.gz` has recorded SHA-256 `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`.
- The project record says P01 formal evidence is complete for the documented effective tested source.
- P01 independent certification is not recorded as complete, and the golden-template freeze remains open.

### P02 — deterministic sequential control

- `P02_RESULTS.md` records reference bounded model checking PASS, temporal induction PASS, eight cover goals reached, and expected failures with retained witnesses for the wrong-reset and wrong-asynchronous-reset controls.
- The stated scope is the documented Boolean, sampled-edge digital environment; the record does not claim analogue timing or four-state X/Z verification.
- `metadata.json` labels P02 as `technical_verification_complete`, with no primary ambiguity dimension and no ambiguity certification.
- The exact named T05 review version is recorded as author-approved in `docs/project-sequence/approvals/T05_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-28.md`. The recorded O1–O5 decisions accept O1–O3 as cosmetic/modelling assumptions, define P02 as a deterministic control, and record the supplied O5 hashes as author-supplied values.
- The T05 review artifact is preserved unchanged; its generic draft banner remains in the reviewed text, while the separate approval record and decision register record approval for that named version.
- `docs/project-state/T06_P02_CLOSURE_REVIEW_v1.md` is a closure-review draft. T06 is IN PROGRESS, not complete.
- Existing run-01/run-02 evidence, hashes, logs and witnesses must remain unchanged. Any new run must be stored under a new provenance ID.

### P05 — unresolved ambiguity candidate

- `P05_RESULTS.md` records paired formal conformance results and a legal distinguishing trace for the post-reset equality check under the tested model.
- `metadata.json` records P05 as `UNRESOLVED`, with `certified_ambiguous: false` and human plausibility review pending.
- The published annotation README records zero reviewer responses at that snapshot. Any later off-repository review activity is unknown from the published evidence inspected here.
- Formal behavioural distinction alone does not establish that both interpretations are plausible readings; no certified-ambiguity claim is made by this reconciliation.

## 5. Branch and pull-request state

The following remote states were checked:

| Pull request | State at inspection | Contribution / treatment |
|---|---|---|
| [PR #6](https://github.com/Kumar62812/neewan_1/pull/6) | Merged | P02/P05 formal evidence and reproduction records are published. |
| [PR #7](https://github.com/Kumar62812/neewan_1/pull/7) | Open, unmerged | Evaluation pipeline and protocol draft; not treated as approved production infrastructure. |
| [PR #8](https://github.com/Kumar62812/neewan_1/pull/8) | Open, unmerged | Workboard and status reconciliation changes; not treated as merged. |
| [PR #9](https://github.com/Kumar62812/neewan_1/pull/9) | Open, unmerged | Three-sample P05 exploratory study; not treated as a frozen or certified benchmark result. |

Some older text in `docs/reproducibility/p02-p05-reproduction.md` still describes PR #6 as open and unmerged. That wording was accurate to an earlier snapshot but is stale relative to the current PR state. The dated historical log entry is retained as history and has not been rewritten here.

## 6. Approvals and open gates

| Item | Reconciled state |
|---|---|
| P01 guide direction | Recorded as permission to proceed with P02; not equivalent to independent P01 certification or template freeze. |
| P01 golden-template freeze | Open / not established as complete by inspected records. |
| T05 — P02 consistency and provenance | DONE for the named `T05_P02_CLOSURE_REVIEW_v1` version according to the separate author approval record on the continuation branch. |
| T06 — P02 formal/provenance closure | IN PROGRESS; its review document is still a draft and its exit checks are not recorded as complete. |
| P05 plausibility and ambiguity certification | Pending / not claimed in published instance records. |
| PR #7–#9 | Draft branches/PRs remain unmerged; do not imply their proposed changes are part of `main`. |
| Official full T1–T31 master plan and decision packet | The sequence register states that the authoritative full source was not located in the published GitHub tree; unknown task titles must not be reconstructed by guesswork. |

## 7. Discrepancies and next handling

1. **Stale Compass and status page:** preserve the frozen plan and historical source documents; use linked project-sequence records for newer status navigation.
2. **Outdated reproduction note:** PR #6 is merged, despite the older reproduction note calling it open. A later documentation correction may update navigation wording without changing run evidence.
3. **T05 banner versus approval record:** the immutable named T05 review still contains a generic draft banner; the separate approval record defines approval for that exact version. Do not edit the approved review in place.
4. **T06 status:** the review draft exists, but the task remains in progress. Do not equate a written review with completed verification or closure.
5. **P05 status:** formal non-equivalence is recorded; human plausibility and certified ambiguity are not established by the inspected published records.
6. **Unmerged PRs:** do not merge or copy their contents into `main` merely because they exist.
7. **Local-only artifacts:** local status, untracked files and machine-only evidence remain unverified through GitHub and require a separate local check if needed.

## 8. A1 checklist

- [x] Remote repository, default branch and selected continuation branch verified.
- [x] Remote commit relationships and ahead/behind counts verified.
- [x] Frozen plan and protocol locations/status checked; no frozen document changed.
- [x] Existing P01, P02 and P05 technical records inventoried.
- [x] Recorded approvals and certification limits reconciled.
- [x] Open and merged pull requests distinguished.
- [x] Main status conflicts and stale reproduction wording documented.
- [x] Existing formal runs, witnesses, archives and manifests preserved.
- [ ] Author's local checkout, untracked files and machine-only artifacts inspected — unavailable to this remote audit.

## 9. A1 outcome

**Remote repository-state reconciliation: COMPLETE.**  
**Local working-tree inventory: NOT VERIFIED.**

The selected continuation branch for sequence documentation is `research/end-to-end-sequence`. This report documents the observed state without changing the frozen methodology, altering formal evidence, making a new certification claim, or declaring any downstream technical task complete.
