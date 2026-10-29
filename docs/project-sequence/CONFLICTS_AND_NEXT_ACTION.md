# Open conflicts, blockers and next authorised action

**This is an index of unresolved gates, not a task closure or an author/supervisor sign-off.** Last status synchronization: 2026-10-29.

| Severity | Issue | Why it matters | Next permitted action |
|---|---|---|---|
| BLOCKER | Authoritative T1–T31 master file and full decision registers D1–D7 not available as verified GitHub artifacts | Invented mappings would invalidate provenance | Recover exact plan/approved closure records from controlled source before marking tasks DONE |
| HIGH | `main` README and compass contain earlier P02-not-implemented / P01-only state, despite published [P02 results](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_RESULTS.md) and [P05 results](https://github.com/Kumar62812/neewan_1/blob/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md) | Historical status can be mistaken for present state | Use this newer navigation first; amend historical status only via separately documented non-destructive correction |
| HIGH | P05 early formal distinction is not independent human plausibility | Cannot claim certified ambiguous case or certified model accuracy | Maintain author-approved candidate classification until post-technical human review/adjudication |
| HIGH | Benchmark schema and metadata template use different names/nesting, with no normative field mapping and no top-level category in the YAML template | Premature migration could change case semantics or mislabel control/ambiguity roles | C5 audit and C6 non-binding field-mapping proposal document the gap and options; retain NOT FROZEN until D2/D14 are resolved and role-aware fixtures pass |
| HIGH | Draft PR #7 requires runner verification and scientific gate review | A proposed evaluator is not validated | Audit existing code as infrastructure; preserve all failures and fixed test fixtures |
| HIGH | Draft PR #8 workboard is 16 Oct snapshot, not current 25–28 Oct governance | Stale next-action claims | Use as historical phase source; reconcile with approved task ledger |
| HIGH | Draft PR #9 public P05 Groq pilot is only a scoped subset of the full local study | Full prompts, request data, private history may be intentionally excluded | Pin public results without inventing local-completeness; audit the local package privately |
| HIGH | Earlier P05 protocol blocks final scored evaluation until human review; latest author policy puts *all independent reviews after technical completion* | Circular or contradictory study dependencies | Obtain explicit approved amendment: define provisional technical scoring vs final human-certified scoring; do not silently claim gate resolved |
| HIGH | Local backup and latest local-only files not inspected | GitHub repository cannot prove total preservation | Compare local checkout, untracked content, archives and checksum manifests before full-completeness claim |
| MEDIUM | Some literature titles map to duplicate/different PDF blobs according to October phase audit | Bibliographic integrity risk | Check PDF actual title, DOI and catalog with old-to-new provenance, preserving original source hashes |

## Recently closed gate — T06 P02 formal/provenance closure

**T06 is DONE** for `T06_P02_CLOSURE_REVIEW_v1` following explicit author approval on 2026-10-29. See the [approval record](./approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md). P02's original run-01/run-02 evidence remains unchanged. P1 cross-platform follow-up is supported by the separately retained [C3 Linux run](https://github.com/Kumar62812/neewan_1/actions/runs/40809992594); P2 local archive verification remains an open non-blocking audit item, and P3 absolute-path redaction remains a pre-release action.

## Next authorised research checkpoint

**T06 is no longer the next gate.** The explicit author approval and closure record are now present. The next official T1–T31 task number is not inferred because the approved master plan remains unavailable in the verified tree. The remaining items above stay open, and the project must not be declared complete based on T06/C3 alone. For the separate user-directed C-series, C4 and C5 are bounded provenance/readiness audits; neither grants review authorization or template freeze. Continue with the next scoped audit while keeping the official task crosswalk caveat intact.

## Branch navigation status

Bringing the existing `main` history into this branch restores published P02/P05 artifacts and P01 certification records. Other draft PRs remain linked separately. The 00–22 roadmap outlines work including future stages, but no future work or human review is represented as completed.
