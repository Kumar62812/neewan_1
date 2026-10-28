# Open conflicts, blockers and next authorised action

**This is an index of unresolved gates, not a task closure or an author/supervisor sign-off.** Last GitHub evidence snapshot verified 2026-10-28.

| Severity | Issue | Why it matters | Next permitted action |
|---|---|---|---|
| BLOCKER | T5 P02 clause traceability, initial-state/reset/clock assumptions and provenance needs author-approved closure | Existing P02 run-02 already exists but does not establish task-governance closeout | Read-only reconcile T5; record full SHA-256s, method `clk2fflogic + yosys-smtbmc`, reset may change while clk low, and `equivalent by content, not commit identity`; request author's T5 named approval |
| BLOCKER | Authoritative T1–T31 master file and full decision registers D1–D7 not available as verified GitHub artifacts | Invented mappings would invalidate provenance | Recover exact plan/approved closure records from controlled source before marking tasks DONE |
| HIGH | `main` README and compass contain earlier P02-not-implemented / P01-only state, despite published [P02 results](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_RESULTS.md) and [P05 results](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md) | Historical status can be mistaken for present state | Use this newer navigation first; amend historical status only via separately documented non-destructive correction |
| HIGH | P05 early formal distinction is not independent human plausibility | Cannot claim certified ambiguous case or certified model accuracy | Maintain author-approved candidate classification until post-technical human review/adjudication |
| HIGH | Draft PR #7 requires runner verification and scientific gate review | A proposed evaluator is not validated | Audit existing code as infrastructure; preserve all failures and fixed test fixtures |
| HIGH | Draft PR #8 workboard is 16 Oct snapshot, not current 25–28 Oct governance | Stale next-action claims | Use as historical phase source; reconcile with approved task ledger |
| HIGH | Draft PR #9 public P05 Groq pilot is only a scoped subset of the full local study | Full prompts, request data, private history may be intentionally excluded | Pin public results without inventing local-completeness; audit the local package privately |
| HIGH | Earlier P05 protocol blocks final scored evaluation until human review; latest author policy puts *all independent reviews after technical completion* | Circular or contradictory study dependencies | Obtain explicit approved amendment: define provisional technical scoring vs final human-certified scoring; do not silently claim gate resolved |
| HIGH | Local backup and latest local-only files not inspected | GitHub repository cannot prove total preservation | Compare local checkout, untracked content, archives and checksum manifests before full-completeness claim |
| MEDIUM | Some literature titles map to duplicate/different PDF blobs according to October phase audit | Bibliographic integrity risk | Check PDF actual title, DOI and catalog with old-to-new provenance, preserving original source hashes |

## Next authorised research checkpoint

**T5 P02 requirement/specification consistency**, *read-only closure review*, with author approval **PENDING**. Verify R/S and both interpretation records against source-snapshot hashes, reset may change when clock low, clock-to-flop lowering and SMTBMC modelling; record no `.sby` for P02. Do not begin T6 merely because historical P02 formal evidence exists.

## Branch navigation status

Bringing the existing `main` history into this branch restores published P02/P05 artifacts and P01 certification records. Other draft PRs remain linked separately. The 00–22 roadmap outlines work including future stages, but no future work or human review is represented as completed.
