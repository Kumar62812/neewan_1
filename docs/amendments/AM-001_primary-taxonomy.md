# AM-001 — Primary taxonomy and thematic tags

| Field | Value |
|---|---|
| Amendment ID | AM-001 |
| Resolves decision | D1 |
| Source document amended | `Files/Research_Papers/docs/research_protocol.md` |
| Section(s) | §5 |
| Source SHA-256 before amendment | `87d3a6e7632bc46e75c23b7ff25ed7d84a09691bc1652865f250a04c34cfaa63` (transcribed from A3 §3; not independently recomputed in this draft) |
| Date drafted | 2026-10-29 |
| Drafted before or after viewing any model outcome? | AFTER — P05 exploratory pilot results were already visible |
| Status | DRAFT — NOT EFFECTIVE |

## 1. Text being amended

Research protocol §5 begins, “The initial taxonomy is:” and lists reset, output, transition, timing, state and concurrency semantics. It says a case should normally isolate one primary ambiguity dimension.

The frozen plan §5 separately defines categories C1–C5, requires exactly one primary category per instance, and allows optional secondary tags.

## 2. Amended rule (proposed)

Use the frozen plan's C1–C5 taxonomy as the **single primary case-category vocabulary**. Retain the six research-protocol dimensions as optional secondary thematic tags:

- `reset_semantics`
- `output_semantics`
- `transition_semantics`
- `timing_semantics`
- `state_semantics`
- `concurrency_semantics`

The T08 metadata schema shall require exactly one `primary_category` value from C1–C5. An optional `thematic_tags` list may contain zero or more listed tag values. Tags do not replace or compete with the primary category. Each case should state its principal thematic focus where applicable and record secondary interactions explicitly.

The frozen plan is not edited by this amendment. This draft clarifies the role of the research-protocol vocabulary and is not effective until D1 is approved.

## 3. Reason

The plan and protocol currently use two taxonomies without a defined mapping. Consistent primary labels support benchmark quality and category-level analysis, including H4.

## 4. Scope and effect

| Question | Answer |
|---|---|
| Affected instances | New cases using the T08 schema; P01/P02/P05 remain unchanged |
| Affected artifacts | Research protocol §5; T08 schema, template, validation and later category analyses |
| Are earlier results rerun? | No automatic rerun; any affected analysis must be separately assessed before primary scoring |
| Effect on earlier results | Existing labels retain their original provenance |
| Existing records rewritten? | NO |

## 5. Validation

1. Confirm exactly one primary category from C1–C5 is required.
2. Validate that each thematic tag belongs to the six-value vocabulary.
3. Validate a new T08 case.
4. Inspect read-only copies of P01/P02/P05 and report differences without changing them.
5. Preserve the source protocol until an approved versioned change is effective.

## 6. Approval

| Field | Value |
|---|---|
| Disposition | PENDING |
| Approved by | |
| Date | |
| Approval-register entry | |
| Effective from commit | |

Template: [AMENDMENT_TEMPLATE.md](AMENDMENT_TEMPLATE.md). D1 must be recorded in the [A3 author decision form](../project-state/A3_AUTHOR_DECISION_FORM.md) before this amendment takes effect.
