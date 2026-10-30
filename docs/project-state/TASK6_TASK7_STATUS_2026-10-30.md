# Task 6 and Task 7 status — 2026-10-30

This is a dated status and evidence index for the FORMAL-AMBIG-RTL reliability study and its Task 7 continuation. It distinguishes report-reported results, direct author approval, verified file integrity, and gates that remain open. The scientific plan, historical Task 6 protocol files, and 320-trial evidence are not modified by this record.

## Current status tracker

| Area | Status as of 2026-10-30 | Boundary |
|---|---|---|
| P01 | Formal evidence is complete for the documented effective tested source. | P01 template freeze and independent certification remain separate; no new certification is claimed. |
| P02 | The current workstream records the named T05 and T06 P02 closure reviews as author-approved. | These are the project-sequence T05/T06 reviews, not the FAR Task 6 study below. See the [workstream index](https://github.com/Kumar62812/neewan_1/blob/research/end-to-end-sequence/docs/project-sequence/README.md) and its [T1–T31 crosswalk](https://github.com/Kumar62812/neewan_1/blob/research/end-to-end-sequence/docs/project-sequence/TASK_T01_T31_CROSSWALK.md). |
| P05 | The three-sample Groq pilot in open PR #9 is exploratory and descriptive. | Human plausibility remains pending. No case is certified ambiguous and no general accuracy claim follows. |
| FAR Task 6 | The author approved the final evidence report v3 and freeze record v1.1 on 2026-10-30, with their stated limitations. | This is technical/protocol-level approval. It is not project-level confirmatory closure and does not resolve Task 21. The exact v3 report and v1.1 freeze-record source files were not present in the accessible workspace, so their contents are not copied here and no hashes are asserted for them. |
| FAR Task 7 | FAR-T7-PROTOCOL-v1.1 remains a freeze candidate. | The freeze candidate has not been approved or frozen; the design variant and planned concurrent 100-R control are not selected/frozen, and scored trials remain 0. |
| A3 protocol decisions | The live `research/end-to-end-sequence` decision form records D3 as accepted for its named implementation; the remaining A3 decisions and the A3 approval block are pending/blank. | A recommendation or a prepared registration is not approval. The current form is [here](https://github.com/Kumar62812/neewan_1/blob/research/end-to-end-sequence/docs/project-state/A3_AUTHOR_DECISION_FORM.md). |
| Task 21 | Supervisor decisions are pending. | The five prospective decisions are external-review threshold and eligibility, model matrix, conditions, repetitions/trials, and budget. |

## FAR Task 6 — approved technical evidence, bounded claims

The author reports 320 planned trial records: 195 `RECEIVED` and 125 `API_FAILURE` (88 HTTP 401 and 37 HTTP 429). The 125 failures remain in the record and were not regenerated. Formal evaluation is reported for all 195 received responses. Under the prespecified analysis, P03/I2 and P04/I1 are reported significant; the report’s stated limitations remain in force, including the availability losses and non-estimable bounded-only comparisons.

On 2026-10-30, the author explicitly approved **Task 6 final evidence report v3** and **freeze record v1.1**. Record this as author approval of those exact technical/protocol artifacts only. It does not establish Task 21 supervisor approval, confirmatory project closure, human plausibility, or ambiguity certification. The exact approved source files were not available in the current workspace search; this update records the approval event without reproducing those files or assigning them an unverified checksum.

The earlier local `FAR1_Task6_final_evidence_report.md` is an unsigned review draft and is not substituted for the approved v3. No Task 6 report, freeze record, trial record, generation archive, or formal evidence bundle is copied into this update.

## FAR Task 7 — verified source package and present state

The uploaded freeze-candidate archive `Task7_v1_1_freeze_candidate_package.zip` has SHA-256 `6bfd08cf0d846d1ab47f92ec43df9f30e83d454713810f7c5b7ab3a146744422`. Its internal `task7_v1_1/SHA256SUMS.txt` lists 2,536 files; all 2,536 listed entries matched, with no missing entries or hash mismatches. The following three source reports were byte-matched to the archive and copied unchanged into this repository:

| Source report | SHA-256 |
|---|---|
| [Task 7 validation report](task7_v1_1/TASK7_VALIDATION_REPORT.md) | `d73d72ca8811f874a4b76ed41065c6b74557c7f299286f5b46770478322df26f` |
| [Task 7 baseline audit](task7_v1_1/TASK7_BASELINE_AUDIT.md) | `a64a539f1b409524d603ad8e0c6c919c1735149a67f167d0e5426f7d52c0d0a7` |
| [Task 7 freeze candidate](task7_v1_1/TASK7_FREEZE_CANDIDATE.md) | `50a6543160c1131f96cf724bfa5acb6deed4ab92c8993790a40c35c797da774a` |

The validation report records 95/95 numbered checks and 18/18 fixture-suite tests in each of two runs, with identical repeated results. This update verified the archive’s internal hashes and the three report identities; it did not rerun those tests. The report’s synthetic validation does not establish live API reliability, selection of Variant B, or a protocol freeze.

The user-supplied Mac console excerpt shows:

- Non-scored User-Agent diagnostic: Python’s default User-Agent returned HTTP 403; the project User-Agent returned HTTP 200.
- Held-out probe: 60/60 calls were `RECEIVED`; all 60 were classified `DIRECT_RTL`, with 8 subquestions reported. Blind labelling and the H1–H5 held-out score remain open.
- Stage-2 rehearsal: 9 `COMPLETED` entries are visible. The excerpt does not establish the outcome of the remaining planned trials, so the rehearsal is incomplete/unverified as a whole.

Remaining Task 7 gates include the actual Groq quota and budget, selection/freeze of the design variant and planned concurrent 100-R control, validation of the Task 6 baseline adapter against the approved real files, recording Task 6 prerequisite gates in the Task 7 approval file, held-out blind scoring, the complete Stage-2 outcome, and approval of T7-G1…G8. No scored Task 7 execution is authorized or reported here.

## A3 and approval namespace check

The current GitHub workstream branch is `research/end-to-end-sequence` at `526354123fe9b5c7f08af098a885b39bcce828e1`, which is 138 commits ahead of `main` and has no associated PR. Its A3 author decision form records D3 `ACCEPT` for implementation commit `aed8f38cf0fca5e2a0ff8e3d3bc07349e6d20df2`. D1, D2, D4, D5, D7, D9–D14 remain `PENDING`; clarifications D6, D8, D15 and D16 remain pending; the approval block for A3 itself is blank. This update does not infer approval of A3 or those decisions.

The repository’s project-sequence `T06` means P02 formal/provenance closure; it is distinct from **FAR Task 6**, the reliability and scored-evidence study summarized above.

## repo_update_to_do

1. Locate the exact approved Task 6 report v3 and freeze record v1.1, verify their source hashes, and add them as new versioned files without replacing FAR-PROTOCOL-v1.0 or the 320-trial evidence.
2. Resolve and record the five Task 21 supervisor decisions before confirmatory closure or any gated scored study.
3. Verify the actual Groq quota and budget; select the Task 7 variant and freeze the concurrent R-control decision; validate the baseline adapter against the approved Task 6 `trials.jsonl` and `analysis.json`.
4. Blind-label the held-out probe and record the H1–H5 score. Obtain the complete Stage-2 package and verify all planned outcomes; the nine visible completions are not a complete rehearsal result.
5. Record the prerequisite and T7-G1…G8 decisions in the Task 7 approval file, regenerate and verify the manifest after quota/budget decisions, and keep scored execution at zero until every applicable gate is closed.
6. Complete the pending A3 decisions and required amendments as separate, dated approvals. Preserve the distinction between technical verification, author approval, supervisor decisions, human plausibility, and ambiguity certification.
