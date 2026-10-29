# D1 — Taxonomy Decision-Readiness Audit

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Status:** TECHNICAL REVIEW COMPLETE — AUTHOR DISPOSITION PENDING  
**Decision source:** [A3 Protocol Conflict Decision Matrix](A3_PROTOCOL_DECISION_MATRIX_v1.0.md), D1  
**Draft amendment:** [AM-001 — Primary taxonomy and thematic tags](../amendments/AM-001_primary-taxonomy.md)

## 1. Decision to be made

D1 concerns the difference between two vocabularies:

- The frozen plan, §5, defines five primary categories: C1–C5. It requires exactly one primary category per instance and permits optional secondary tags.
- The research protocol, §5, defines six thematic dimensions: reset, output, transition, timing, state, and concurrency semantics. It says that a case should normally isolate one primary ambiguity dimension.

Without an explicit relationship between these vocabularies, a case's primary classification can be confused with the semantic feature or features it exercises. That would undermine consistent case metadata and category-level analysis, including H4.

## 2. Options and evaluation

| Option | Definition | Consequence | Assessment |
|---|---|---|---|
| **A — Recommended** | Keep C1–C5 as the single primary category; represent the six protocol dimensions as optional secondary thematic tags. | Preserves the frozen plan's category contract and lets cases record one or more relevant thematic features without creating a second primary classification. | **Best aligned with the currently frozen source.** |
| B | Make the six research-protocol dimensions primary. | Reverses the hierarchy in the frozen plan and would require an amendment to the plan, not merely clarification of the protocol. | Not recommended; higher change-control impact. |
| C | Keep both vocabularies as parallel primary taxonomies. | Leaves two competing primary classifications and would require an additional rule for analysis, conflicting with the one-primary-category rule in the plan. | Not recommended; does not cleanly resolve the conflict. |

**Recommendation:** ACCEPT Option A, exactly as proposed in A3 D1 and draft AM-001. This is a technical recommendation only, not the author's disposition.

## 3. Proposed implementation contract (not yet normative)

If the author accepts Option A, the T08 metadata contract should require:

- `primary_category`: exactly one value from `C1`, `C2`, `C3`, `C4`, or `C5`.
- `thematic_tags`: optional list, permitting zero or more values from `reset_semantics`, `output_semantics`, `transition_semantics`, `timing_semantics`, `state_semantics`, and `concurrency_semantics`.

The primary category answers *what benchmark category is assigned to this instance?* The tags answer *which thematic semantics does this instance exercise?* Tags do not override, substitute for, or compete with the primary category. A case may have multiple tags when its behavior genuinely spans multiple dimensions; the case author should identify the principal thematic focus and disclose secondary interactions in the case documentation.

## 4. Preservation and scope

- Do not edit the frozen plan as part of D1.
- Do not rewrite P01, P02, or P05 metadata as part of this decision.
- Do not relabel past outcomes or reinterpret past metrics automatically.
- Apply the approved convention only through a versioned amendment and the T08 schema/template work, after required governance decisions are resolved.
- AM-001's recorded baseline SHA-256 is transcribed from A3 §3; this audit did not independently recompute that digest.

## 5. Acceptance tests after author approval

1. Schema validation rejects a missing or multiple `primary_category` value.
2. Schema validation rejects any primary value outside C1–C5.
3. Schema validation accepts an omitted `thematic_tags` field and an empty list.
4. Schema validation accepts any subset of the six allowed thematic tags.
5. Schema validation rejects unknown tags and duplicate tags unless a later approved schema explicitly allows duplicates.
6. A synthetic case can carry one primary category plus multiple tags without treating any tag as a second primary category.
7. Read-only audits of P01/P02/P05 report existing taxonomy fields and differences without modifying any case file.
8. The validator and test evidence are pinned to the exact amended protocol/schema/template versions.

These are proposed acceptance tests; none is claimed to have run as part of this documentation audit.

## 6. Decision and gate status

| Item | Status |
|---|---|
| Source conflict described by A2/A3 | Confirmed from the cited section text |
| Best-supported technical recommendation | Option A |
| AM-001 | DRAFT — NOT EFFECTIVE |
| Author disposition for D1 | **PENDING** |
| D1 approval date / effective commit | Not recorded |
| T08 authorization | Not established |
| D2, D9, and D14 | Still separate pre-T08 decisions; not resolved by D1 |

**Closure rule:** D1 remains open until the author records an explicit `ACCEPT`, `REJECT`, `REVISE`, or `DEFER` disposition with date and notes in the A3 author decision form, and any required amendment is approved under the project's change-control rules. Merely adding this audit report does not resolve D1.
