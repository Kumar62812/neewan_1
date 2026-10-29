# D2 — Certification Status and Lifecycle Decision-Readiness Audit

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Status:** TECHNICAL REVIEW COMPLETE — AUTHOR DISPOSITION PENDING  
**Decision source:** [A3 Protocol Conflict Decision Matrix](A3_PROTOCOL_DECISION_MATRIX_v1.0.md), D2  
**Draft amendment:** [AM-002 — Certification status and lifecycle crosswalk](../amendments/AM-002_status-vocabulary-crosswalk.md)

## 1. Decision to be made

D2 addresses a semantic conflict between two existing sources:

- Frozen plan §6 defines **certification/requirement-status labels**: `UNAMBIGUOUS`, `CERTIFIED_AMBIGUOUS`, `UNRESOLVED`, and `EXCLUDED`.
- Benchmark schema §4 defines a **workflow lifecycle**: `candidate`, `certified_ambiguous`, `unambiguous_control`, `negative_candidate`, and `inconclusive`. The schema also allows a later release to mark a record `frozen`.

A single `status` field cannot safely represent both scientific disposition and workflow/release state. The existing case records demonstrate the problem: P02 uses `status: technical_verification_complete`; P05 uses `status: UNRESOLVED`. Both also contain a nested `certification.certified_ambiguous` Boolean. Those values cannot be interpreted consistently as a single status vocabulary.

## 2. Options and recommendation

| Option | Rule | Assessment |
|---|---|---|
| **A — Recommended** | Use `certification_status` for PLAN §6 labels, `lifecycle_stage` for the schema's workflow labels, and a separate release/freeze indicator. Maintain an explicit crosswalk and validation rules. | Best separation of scientific conclusion, workflow progress, and release state; preserves the currently frozen plan's certification vocabulary. |
| B | Make the benchmark schema's lifecycle labels the canonical single status field. | Would subordinate or replace the frozen plan's certification labels and make workflow state carry scientific meaning; higher change-control impact. |
| C | Merge both vocabularies into one new status taxonomy. | Requires a new canonical vocabulary and a much larger migration/change-control decision; risks collapsing independent dimensions again. |

**Technical recommendation:** ACCEPT Option A, as recorded in A3 D2 and draft AM-002. This recommendation is not the author's decision and does not make AM-002 effective.

## 3. Proposed mapping (for decision, not yet normative)

| `lifecycle_stage` | Proposed `certification_status` | Required condition / guard |
|---|---|---|
| `candidate` | `UNRESOLVED` | A candidate is not certified simply by being created or formally tested. |
| `certified_ambiguous` | `CERTIFIED_AMBIGUOUS` | All plan-required formal and plausibility criteria must be satisfied for the same case/version. Formal distinction alone is insufficient. |
| `unambiguous_control` | `UNAMBIGUOUS` | Evidence supports one intended behavior for the stated scope. |
| `negative_candidate` | `EXCLUDED` | The rejection/exclusion criterion and a PLAN §6 exclusion reason are recorded. Until rejection is actually established, do not infer exclusion from the label alone. |
| `inconclusive` | Usually `UNRESOLVED`; `EXCLUDED` only when an explicit exclusion rule and reason justify that decision | Record the reason and retain inconclusive formal evidence as inconclusive; do not call it a behavioral mismatch. |
| Release/freeze state | No direct mapping | Use an independent release/freeze field; `frozen` must not imply ambiguity certification. |

The crosswalk is not a mechanical status-conversion script. It is a set of allowed relationships and required evidence conditions. A schema validator must reject incompatible combinations, not silently rewrite them.

### Technical-progress labels

P02's `technical_verification_complete` is neither a PLAN certification status nor one of the benchmark schema's listed lifecycle labels. It must **not** be mapped automatically to `UNAMBIGUOUS`, `CERTIFIED_AMBIGUOUS`, or `frozen`. If the project adopts a distinct `technical_status` field, its exact vocabulary is governed by the separate D11 decision and applicable amendments. Until then, treat the existing P02 value as a legacy mixed-status value to report during read-only validation, not to normalize silently.

### Redundant Boolean guard

Existing P02/P05 metadata contains `certification.certified_ambiguous` as well as a top-level `status`. The approved T08 schema must explicitly define whether that Boolean is removed, retained as a derived assertion, or checked for consistency against `certification_status`. It must not become a second independent source of truth. This is a schema-contract requirement, not permission to edit the historical case files.

## 4. Preservation and change-control boundaries

- Keep the frozen plan unchanged. D2 is addressed by the proposed versioned amendment to benchmark schema §§3–4, not by editing PLAN §6.
- Do not rewrite existing P01/P02/P05 metadata or historical formal results as part of this decision.
- Validate read-only copies of P02/P05 and report legacy values and field conflicts; do not repair or normalize them in place.
- Do not back-fill a certification conclusion from technical verification alone, the presence of a counterexample, or a release freeze.
- Do not start T08 schema/template migration until D2 and the other required pre-T08 author decisions are recorded under the project's change-control rules.
- AM-002's source SHA-256 baseline is transcribed from A3 §3; this documentation audit did not independently recompute that digest.

## 5. Acceptance tests after author approval

1. The schema requires exactly one `certification_status` from the four PLAN labels.
2. The schema requires exactly one `lifecycle_stage` from the five benchmark lifecycle labels, if that field is made mandatory by the approved schema.
3. The release/freeze flag is separate; `frozen` is rejected as a value for either status field.
4. Every proposed crosswalk row is tested, including role/evidence prerequisites for `CERTIFIED_AMBIGUOUS`.
5. `negative_candidate` cannot become `EXCLUDED` without a recorded exclusion reason.
6. `inconclusive` cannot become `CERTIFIED_AMBIGUOUS`; formal timeouts/tool errors cannot be counted as a proven RTL mismatch.
7. `technical_verification_complete` is rejected from both enumerations and reported as a legacy value in the read-only P02 audit.
8. The approved rule for `certification.certified_ambiguous` is tested, including disagreement with `certification_status`.
9. A new synthetic T08 case validates against the approved schema.
10. Read-only copies of P02 and P05 are checked; mismatches are reported, not fixed.
11. Test output, schema version, source pins, and runner/tool versions are retained as reproducible evidence.

These are proposed acceptance tests. They were not executed by this documentation-only task.

## 6. Decision and gate status

| Item | Status |
|---|---|
| Source conflict in A2/A3 | Confirmed from the pinned PLAN, schema, and current P02/P05 metadata |
| Best-supported technical recommendation | Option A |
| AM-002 | DRAFT — NOT EFFECTIVE |
| Author disposition for D2 | **PENDING** |
| Approval date / effective commit | Not recorded |
| T08 authorization | Not established |
| D1, D9, D14 | Separate pre-T08 decisions; not resolved by this report |

**Closure rule:** D2 remains open until the author records an explicit `ACCEPT`, `REJECT`, `REVISE`, or `DEFER` disposition with date and notes in the A3 author decision form, and required amendments are approved under the project change-control procedure. The existence of AM-002 or this report is not approval.
