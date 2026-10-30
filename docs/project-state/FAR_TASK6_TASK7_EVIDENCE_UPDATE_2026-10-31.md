# FAR Task 6/7 evidence intake update — 2026-10-31

This supplement records a local evidence inventory for the FAR reliability-study tasks. It is not a protocol amendment, experiment approval, task-closure decision, freeze, or ambiguity certification. FAR Task 6/7 are distinct from project-sequence T06/T07; the official crosswalk still does not establish a T07 title.

## FAR Task 6

- `formal_evaluations/trials.jsonl`, `formal_evaluations/analysis.json`, and `formal_evidence_bundle.zip` are present in the shared local output workspace. The bundle passes its ZIP integrity check, and its embedded `trials.jsonl` and `analysis.json` match the local files by SHA-256.
- The accessible `FAR1_Task6_final_evidence_report.md` is a review draft that leaves author disposition blank. The exact approved report v3 and freeze record v1.1 referenced by the 2026-10-30 status snapshot are not present in the accessible bundle/workspace search.
- The run files therefore do not establish the reported approval or Task 6 closure. Keep Task 6 distinct from project-sequence T06 and do not mark either task DONE on this basis. Task 21 decisions remain a separate project gate.

## FAR Task 7

- The local r7 directory is a working folder, not a Git checkout. Its source update archive and run outputs remain local and were not copied into this repository.
- The saved HO4 score file reports **NOT PASSED**. Keep T7-G3 pending; the failed result is not a pass or a freeze decision.
- The HO5 folder contains partial collection artifacts, with no final labelled sheet or score file available. No HO5 pass is recorded.
- This update does not include response counts, experimental metrics, labels, raw run files, credentials, or the sealed oracle key.

## Remaining evidence intake

- For Task 6, provide the exact approved report v3 and freeze record v1.1 (or their canonical controlled locations) to reconcile the approval record. The `trials.jsonl` and `analysis.json` do not need to be uploaded again for this local inventory.
- For a later Task 7 audit, use a controlled evidence package with the source/protocol version, run manifests and attempts, raw responses, blind label sheet, score output, and hashes. Keep provider credentials and the sealed oracle key outside the public repository. Package HO5 only after collection and scoring are complete; retain the failed HO4 evidence separately.

No experiment was rerun for this documentation update. It does not revise frozen evidence or alter any approval or scientific status.
