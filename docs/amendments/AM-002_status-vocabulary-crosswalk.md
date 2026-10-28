# AM-002 — Certification status and lifecycle crosswalk

| Field | Value |
|---|---|
| Amendment ID | AM-002 |
| Resolves decision | D2 |
| Source document amended | `Files/Research_Papers/docs/benchmark_schema.md` |
| Section(s) | §§3–4 |
| Source SHA-256 before amendment | `18b5e39599b519872a427c8463213f35bce0cf175e9d553bce3035028493fcac` (transcribed from A3 §3; not independently recomputed in this draft) |
| Date drafted | 2026-10-29 |
| Drafted before or after viewing any model outcome? | AFTER — P05 exploratory pilot results were already visible |
| Status | DRAFT — NOT EFFECTIVE |

## 1. Text being amended

Benchmark schema §3 currently uses a single `status` field. Section 4 defines lifecycle labels `candidate`, `certified_ambiguous`, `unambiguous_control`, `negative_candidate`, and `inconclusive`, and notes a record may additionally be `frozen` in a release.

The frozen plan §6 defines certification statuses `UNAMBIGUOUS`, `CERTIFIED_AMBIGUOUS`, `UNRESOLVED`, and `EXCLUDED`. Existing P02/P05 metadata uses mixed status vocabularies.

## 2. Amended rule (proposed)

New T08 metadata shall separate:

- `certification_status`: one of `UNAMBIGUOUS`, `CERTIFIED_AMBIGUOUS`, `UNRESOLVED`, or `EXCLUDED`, following the frozen plan.
- `lifecycle_stage`: one of `candidate`, `certified_ambiguous`, `unambiguous_control`, `negative_candidate`, or `inconclusive`, following the benchmark lifecycle.
- A separate release/freeze indicator: whether the record is frozen for a release. T08 shall define its final field name and values. `frozen` is not a certification status or lifecycle stage.

### Proposed crosswalk

| `lifecycle_stage` | Corresponding `certification_status` | Qualification |
|---|---|---|
| `candidate` | `UNRESOLVED` | Evidence has not established a final status |
| `certified_ambiguous` | `CERTIFIED_AMBIGUOUS` | All required plausibility and formal criteria pass |
| `unambiguous_control` | `UNAMBIGUOUS` | One intended behaviour is supported for the tested scope |
| `negative_candidate` | `EXCLUDED` | A PLAN §6 exclusion reason is recorded |
| `inconclusive` | `UNRESOLVED`, or `EXCLUDED` with `INCONCLUSIVE_FORMAL` where applicable | Rationale must be recorded; no automatic conversion |
| Frozen/release state | No direct mapping | Independent of certification |

T08 must define required fields, enumerated values, allowed combinations, transitions and validation errors. The frozen plan's complete certification rule remains mandatory.

## 3. Reason

A single field can conflate scientific certification, technical progress, workflow stage and release state. The split prevents labels such as `technical_verification_complete` or `frozen` from being mistaken for certification.

## 4. Scope and effect

| Question | Answer |
|---|---|
| Affected instances | New cases using T08 metadata |
| Affected artifacts | Benchmark schema §§3–4; T08 schema, template, crosswalk and validator |
| Are earlier results rerun? | No automatic rerun; assess affected analyses separately |
| Effect on earlier results | Existing labels remain tied to original metadata versions |
| Existing records rewritten? | NO |

P01, P02 and P05 metadata must not be silently rewritten. Validate read-only copies and report mismatches. Any migration requires a separate authorized task and new file versions.

## 5. Validation

1. Test both field enumerations and required-field checks.
2. Test every crosswalk row and invalid combinations.
3. Validate a new T08 case.
4. Validate read-only copies of P02/P05 metadata and report, but do not repair, mismatches.
5. Confirm that `frozen` cannot imply a certification result.

## 6. Approval

| Field | Value |
|---|---|
| Disposition | PENDING |
| Approved by | |
| Date | |
| Approval-register entry | |
| Effective from commit | |

Template: [AMENDMENT_TEMPLATE.md](AMENDMENT_TEMPLATE.md). D2 must be recorded in the [A3 author decision form](../project-state/A3_AUTHOR_DECISION_FORM.md) before this amendment takes effect.
