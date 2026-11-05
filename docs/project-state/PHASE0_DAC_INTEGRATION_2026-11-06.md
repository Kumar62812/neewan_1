# FORMAL-AMBIG-RTL — Phase 0 DAC integration audit (2026-11-06 IST)

**Status: DRAFT / NOT SCIENTIFIC CLOSURE.** This derivative memo does not amend frozen experimental evidence, approve Task 7, unblind the review, or report a DAC submission.

## Single DAC submission direction

Prepare **one integrated DAC 2027 paper**: Task 7 one-round clarification as the main intervention and Task 6 R-vs-explicit-S1/S2 as historical baseline/context. Compare interactive conditions against **concurrent Task 7 CR**, not a causally assumed historical Task 6 R baseline. Do not submit overlapping Task-6-only and Task-7-only manuscripts. Retain the P05 pilot draft unchanged.

## Audit of author-supplied sources

- `T7_RESULTS_v1_1.zip` SHA-256: `46595d7e0c25426527eed4bf3f980ea6f08950e0f724d655639315a059d4c2f4`; its internal SHA256SUMS has **10/10 matches**.
- `INTERACTIVE_TRIAL_RECORDS.json`: **320/320 `generation_status=COMPLETED`**. This is not 320 correct designs or 320 proof certificates.
- Task 7 interactive ambiguous-case question rate **74/200**; P02 control 0/20. The denominator is not 320 for the ambiguous IQ rate.
- P04/I1: **18/20** target proven matches in IQ against **6/20** in concurrent CR; supplied re-derivation gives two-sided Fisher p=0.000244361757 and Holm p=0.001710532300 over seven confirmatory contrasts. Formal match is under the frozen model/environment; it is not a human ambiguity certification.
- P04/I2: **20/20** IQ against **14/20** CR; adjusted p=0.1211761212 (not significant at 0.05).
- Historical P03/S1 R **12/20** in Task 6 versus concurrent CR **20/20** in Task 7: a descriptive **cross-window drift**, not evidence of an identified cause. Any cross-time Task 6 R-to-S claims need a validity qualification.
- The **125/320 (39.0625%) API failures belong to Task 6**, as reported by the baseline adapter; they are **not** Task 7 RTL correctness failures.
- The uploaded Section 14 `review_form.csv` includes 320 rows with **blank ratings**. No completed independent review or controlled unblinding is established here.
- The proposed **41/41** conditional claim is *not verified for publication*: supply its exact trial-ID selection predicate, denominator, and applicable conformance/proof rule.

These observations come from the attached analysis packages and independent-rederivation outputs. Internal hash integrity is not an independently rerun complete formal audit. Avoid conflating API delivery, syntax errors, formal inconclusive results, bounded checks, unbounded proofs, and independent plausibility.

## Incoming bundles — assessed, not imported

- `task7_v1_2_repo_branch(1).bundle` and prior `v1_2` file: identical SHA-256 `f09fb26adea685f0a76f0243e10111039df4170e006de7db6da33c3c17bea650`, HEAD `4dff12201f668f1ea3eaa9ffcc32b03dc0c224ce`.
- `task7_v1_21_repo_branch.bundle`: SHA-256 `d53f9f7fc3001292d2c3fa0075632b9c65b4c1feec1561940aa14d136ef607aa`, HEAD `86c168d93f6f473faebb098ef53cba3f5618efb4`; merge includes status commit `08cf558`.
- Both are incremental bundles that require prerequisite `9be08412455a52daeb8e24016732e99c5a84c95e`. A clean offline repository could not verify/import the complete bundles without that history. The `results/task7-v1.1` branch was not on GitHub at audit time. The new bundle's commit message explicitly describes review answers as **provisional**. Do not force-push or merge the bundles on the strength of this memo alone.

## Phase 0 acceptance gates (all open)

1. **G0-T7-review:** Completed genuinely blinded Section 14 human scores, reviewer provenance, validation, approved unblinding, and reconciled report.
2. **G0-T7-closure:** Formal author/supervisor acceptance pursuant to frozen governance; original evidence, failed/inconclusive outcomes and deviations retained.
3. **G0-DAC-evidence:** Claim-to-trial/formal-evidence table, separate Task 6 and Task 7 denominators, P03 drift and all outcome classes disclosed.
4. **G0-DAC-manuscript:** Integrated manuscript built, format/anonymous review and citation audit passed, with no invented numbers.
5. **G0-author-approval:** Required guide/co-author approval.
6. **G0-submission:** Full-paper submission completed and receipt plus PDF/hash preserved.

**Overall: Phase 0 OPEN; no manuscript submission asserted.** This document is navigation/evidence bookkeeping only. No scored-run or frozen file was edited.
