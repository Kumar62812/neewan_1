# D1 author approval — taxonomy relationship

- **Project:** FORMAL-AMBIG-RTL
- **Decision:** D1 — Taxonomy relationship
- **Disposition:** ACCEPT — Option A
- **Author:** G. Naveen
- **Date:** 2026-10-31
- **Approved amendment:** [AM-001 — C1–C5 primary taxonomy with thematic secondary tags](../../amendments/AM-001_taxonomy_relationship.md)
- **Decision form:** [A3 author decision form](../A3_AUTHOR_DECISION_FORM.md)
- **Decision matrix:** [A3 protocol decision matrix](../A3_PROTOCOL_DECISION_MATRIX_v1.0.md)

## Author-approved decision

> For D1, I select Option A as my author decision. Author: G. Naveen.

**Option A is approved:** the five categories C1–C5 defined in frozen PLAN §5 remain the sole primary taxonomy. The six dimensions in Research Protocol §5 (reset, output, transition, timing, state and concurrency) are retained as optional secondary thematic tags.

## Operational requirements

1. Each benchmark instance has exactly one required primary category in C1–C5.
2. The optional `thematic_tags` field may contain zero or more values from the six approved Research Protocol dimensions.
3. Secondary tags do not replace or override the primary category and do not independently establish ambiguity or certification status.
4. Multi-dimensional interactions must be documented explicitly; thematic-tag analyses must account for non-mutually-exclusive tags.
5. T08 schema and runner validation must enforce the primary-category and secondary-tag vocabularies.
6. P01, P02 and P05 metadata and historical outputs are not rewritten or retrospectively relabelled.

## Scope and limitations

This approval authorizes AM-001 as a versioned clarification of the taxonomy hierarchy. It does not modify frozen PLAN §5 or the Research Protocol source file. It does not certify benchmark cases, complete T08, pass schema validation, authorize scored experiments, or alter historical pilot outcomes. Implementation validation remains pending.

AM-001 was drafted after the P05 exploratory pilot outcome had been viewed. The amendment records that timing transparently and does not use pilot outcomes to tune or retrospectively change the taxonomy, outcome classes, metrics, or benchmark membership.

## Frozen-evidence preservation

The frozen PLAN, Research Protocol, P01/P02/P05 metadata, source RTL, formal evidence, counterexamples, historical logs, run manifests and P05 pilot artifacts must remain unchanged. The amendment is read alongside the source documents.

**Result:** D1 Option A is ACCEPTED by G. Naveen on 2026-10-31. AM-001 is approved; T08 implementation and validation remain outstanding.
