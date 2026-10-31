# AM-002 — Separate certification status from benchmark lifecycle

| Field | Value |
|---|---|
| Amendment ID | AM-002 |
| Resolves decision | D2 — Certification status vocabulary ([A3 decision matrix](../project-state/A3_PROTOCOL_DECISION_MATRIX_v1.0.md)) |
| Source document amended | Files/Research_Papers/docs/benchmark_schema.md |
| Section(s) | §3 — Required instance fields; §4 — Status lifecycle |
| Source SHA-256 before amendment | 18b5e39599b519872a427c8463213f35bce0cf175e9d553bce3035028493fcac (A3 §3 evidence baseline) |
| Date drafted | 2026-10-31 |
| Drafted before or after viewing any model outcome? | AFTER. The P05 exploratory pilot had already been viewed. This amendment separates certification conclusions from lifecycle tracking; it does not alter outcome classes, metrics, benchmark membership, or historical pilot interpretation, and no pilot outcome is used to select the vocabulary or crosswalk. |
| Status | APPROVED |

## 1. Text being amended

Benchmark Schema §3 currently requires a single status field. Section 4 defines the lifecycle labels candidate, certified_ambiguous, unambiguous_control, negative_candidate and inconclusive. It further states that a later experimental release may mark an accepted record as frozen. This combines certification conclusions and lifecycle/release state in one vocabulary, while frozen Project Plan §6 defines a distinct set of certification statuses.

## 2. Amended rule

Read Benchmark Schema §§3–4 alongside frozen PLAN §6 using two separate dimensions.

### 2.1 Canonical certification status

The required certification_status field is governed exclusively by frozen PLAN §6 and MUST use exactly one of:

- UNAMBIGUOUS
- CERTIFIED_AMBIGUOUS
- UNRESOLVED
- EXCLUDED

The PLAN §6 definitions and exclusion-reason requirements remain authoritative. The benchmark lifecycle vocabulary MUST NOT replace or redefine these certification statuses.

### 2.2 Separate lifecycle stage

The required lifecycle_stage field tracks benchmark development and disposition and MUST use one of:

- candidate
- certified_ambiguous
- unambiguous_control
- negative_candidate
- inconclusive

The lifecycle stage is not itself a certification conclusion. A stage transition does not automatically certify or exclude a case.

### 2.3 Release state

The former frozen lifecycle label is a release-state indicator, not a lifecycle stage or certification status. Represent it separately as release_frozen (Boolean). It may be true or false independently of the certification status; freezing a record does not change its certification conclusion.

### 2.4 Crosswalk and inconclusive handling

| lifecycle_stage | Expected certification_status | Rule |
|---|---|---|
| candidate | UNRESOLVED | Evidence and review are not yet sufficient for a final conclusion. |
| certified_ambiguous | CERTIFIED_AMBIGUOUS | Use only after all PLAN §4 certification requirements, including plausibility and formal distinction, are satisfied. |
| unambiguous_control | UNAMBIGUOUS | Use when one operational interpretation is supported for the tested behavior. |
| negative_candidate | EXCLUDED | Record a specific applicable PLAN §6 exclusion reason. |
| inconclusive | UNRESOLVED | Default while a formal or other evidentiary investigation remains open or cannot yet support a final disposition. |

For inconclusive, EXCLUDED is permitted only when the author/certification process makes an explicit exclusion decision supported by a specific PLAN §6 reason, such as INCONCLUSIVE_FORMAL, and records that reason. A timeout, tool error, incomplete check, or missing evidence alone MUST NOT silently convert a case to EXCLUDED or establish a mismatch. Where investigation remains open, retain UNRESOLVED.

The crosswalk is a consistency rule, not an automatic migration or certification mechanism. Any exceptional pairing must be explained in the case decision record and remain consistent with PLAN §6.

### 2.5 Metadata and compatibility

New T08 metadata MUST contain distinct certification_status and lifecycle_stage fields, plus the separate Boolean release_frozen field. The legacy generic status field MUST NOT be treated as an authoritative substitute for either field in new records. Schema validation must reject unknown enum values and invalid types, and report crosswalk inconsistencies for review rather than silently rewriting them.

P01, P02 and P05 metadata, historical outputs and evidence are not rewritten. In particular, existing values such as P02's technical_verification_complete are not retrospectively reinterpreted as certification status. Any migration or derived crosswalk for existing records requires a separately authorized task and new versioned artifacts.

## 3. Reason

Frozen PLAN §6 defines the project's authoritative certification vocabulary. Benchmark Schema §4 describes a lifecycle, and its frozen label describes release state. Treating these as one status field conflates evidence-based certification with construction progress and release management. D2 Option A resolves this by preserving PLAN §6 as canonical and recording lifecycle and release state independently.

## 4. Scope and effect

| Question | Answer |
|---|---|
| Affected instances | New T08 cases and subsequent cases using the amended schema; P01/P02/P05 are used only for read-only compatibility checks |
| Affected artifacts | New-case metadata schema, T08 template/runner, benchmark lifecycle documentation, and analyses consuming certification or lifecycle fields |
| Are earlier results rerun? | NO. This amendment changes metadata semantics and field separation, not outcomes, metrics, benchmark membership, or historical pilot interpretation. |
| Effect on earlier results | No retrospective relabelling or promotion. Existing records retain their original contents and provenance. |
| Existing records rewritten? | NO. P01, P02 and P05 metadata and all historical evidence remain unchanged. Any migration requires separate authorization. |

## 5. Validation

The following checks remain required before T08 is considered validated:

1. The T08 JSON schema requires certification_status with exactly the four PLAN §6 values.
2. The schema requires lifecycle_stage with exactly the five lifecycle values above.
3. The schema requires Boolean release_frozen; it is not accepted as a lifecycle or certification enum.
4. Crosswalk validation checks the ordinary pairings in §2.4. An inconclusive case defaults to UNRESOLVED; an EXCLUDED disposition requires a specific PLAN §6 reason and explicit decision record.
5. Unknown values, invalid types, and unsupported legacy substitutions are reported as validation errors.
6. Validate one newly generated T08 case.
7. Run read-only compatibility checks against copies of P02/P05 metadata. Report mismatches; do not repair or rewrite the source records.
8. Retain schema, commands, validation output and hashes in the T08 evidence packet.

Validation status: Amendment approved; schema, template/runner implementation and T08 validation remain pending. This record does not claim those checks have passed.

## 6. Approval

| Field | Value |
|---|---|
| Disposition | ACCEPT — Option A |
| Approved by | G. Naveen |
| Date | 2026-10-31 |
| Approval-register entry | [D2 author approval](../project-state/approvals/D2_CERTIFICATION_STATUS_VOCABULARY_APPROVAL_2026-10-31.md) |
| Effective from commit | To be completed in the approval record after the amendment commit is created. |

Frozen-source instruction: Do not edit or replace Files/FORMAL_AMBIG_RTL_PLAN.md or Files/Research_Papers/docs/benchmark_schema.md. This amendment is read alongside the frozen sources. P01/P02/P05 metadata, source RTL, formal evidence, counterexamples, historical logs, run manifests and pilot artifacts remain unchanged.
