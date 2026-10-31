# D2 author approval — certification status vocabulary

- **Project:** FORMAL-AMBIG-RTL
- **Decision:** D2 — Certification status vocabulary
- **Disposition:** ACCEPT — Option A
- **Author:** G. Naveen
- **Date:** 2026-10-31
- **Approved amendment:** [AM-002 — separate certification status from benchmark lifecycle](../../amendments/AM-002_certification_status_vocabulary.md)
- **Decision form:** [A3 author decision form](../A3_AUTHOR_DECISION_FORM.md)
- **Decision matrix:** [A3 protocol decision matrix](../A3_PROTOCOL_DECISION_MATRIX_v1.0.md)

## Author-approved decision

> D2 author disposition: A. Author: G. Naveen. Date: 2026-10-31. Approve Option A and AM-002 exactly as recommended, including the clarified inconclusive mapping.

**Option A is approved:** frozen PLAN §6 remains the sole authoritative certification-status vocabulary. Benchmark lifecycle is recorded separately, with a crosswalk. The former frozen lifecycle label is represented as a separate Boolean release flag, not as a certification status or lifecycle stage.

## Operational requirements

1. New T08 metadata must contain a required certification_status field using exactly PLAN §6 values: UNAMBIGUOUS, CERTIFIED_AMBIGUOUS, UNRESOLVED, EXCLUDED.
2. New T08 metadata must contain a separate lifecycle_stage field using the benchmark lifecycle values: candidate, certified_ambiguous, unambiguous_control, negative_candidate, inconclusive.
3. Release freezing is represented separately by Boolean release_frozen; it does not change certification status.
4. The ordinary crosswalk is: candidate → UNRESOLVED; certified_ambiguous → CERTIFIED_AMBIGUOUS; unambiguous_control → UNAMBIGUOUS; negative_candidate → EXCLUDED with a specific PLAN §6 reason; inconclusive → UNRESOLVED while investigation remains open.
5. For an inconclusive case, EXCLUDED is allowed only after an explicit exclusion decision with a specific PLAN §6 reason, such as INCONCLUSIVE_FORMAL. A timeout, tool error, incomplete check or missing evidence alone does not silently exclude a case or establish mismatch.
6. Schema validation must report invalid values, types and crosswalk inconsistencies rather than silently rewriting records.
7. P01, P02 and P05 metadata and historical evidence remain unchanged. Any migration requires separate authorization and new versioned artifacts.

## Scope and limitations

This approval authorizes AM-002 as a versioned clarification of Benchmark Schema §§3–4. It does not modify frozen PLAN §6 or the Benchmark Schema source file. It does not certify benchmark cases, complete T08, pass schema validation, authorize scored experiments, or retrospectively migrate existing metadata. Schema, template/runner implementation and T08 validation remain pending.

AM-002 was drafted after the P05 exploratory pilot outcome had been viewed. The amendment records that timing transparently. The pilot outcome was not used to tune the status vocabulary or crosswalk, and no outcome classes, metrics, benchmark membership or historical pilot interpretation are changed.

## Frozen-evidence preservation

The frozen PLAN and Benchmark Schema source files, P01/P02/P05 metadata, source RTL, formal evidence, counterexamples, historical logs, run manifests and P05 pilot artifacts must remain unchanged. The amendment is read alongside the source documents.

**Result:** D2 Option A is ACCEPTED by G. Naveen on 2026-10-31. AM-002 is approved; T08 schema, template/runner implementation and validation remain outstanding.
