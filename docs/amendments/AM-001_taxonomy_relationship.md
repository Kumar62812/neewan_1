# AM-001 — C1–C5 primary taxonomy with thematic secondary tags

| Field | Value |
|---|---|
| Amendment ID | AM-001 |
| Resolves decision | D1 — Taxonomy relationship ([A3 decision matrix](../project-state/A3_PROTOCOL_DECISION_MATRIX_v1.0.md)) |
| Source document amended | `Files/Research_Papers/docs/research_protocol.md` |
| Section(s) | §5 — Ambiguity taxonomy |
| Source SHA-256 before amendment | `87d3a6e7632bc46e75c23b7ff25ed7d84a09691bc1652865f250a04c34cfaa63` (A3 §3 evidence baseline) |
| Date drafted | 2026-10-31 |
| Drafted before or after viewing any model outcome? | AFTER. The P05 exploratory pilot had already been viewed. This amendment resolves the taxonomy hierarchy only; it does not change outcome classes, metrics, benchmark membership, or historical pilot interpretation. No pilot outcome is used to select or tune the taxonomy mapping. |
| Status | APPROVED |

## 1. Text being amended

Research Protocol §5 currently introduces the following as its initial taxonomy:

> The initial taxonomy is:
>
> 1. Reset semantics: synchronous/asynchronous reset, polarity, priority, reset value.
> 2. Output semantics: Mealy/Moore, registered/combinational output, current-state/next-state interpretation.
> 3. Transition semantics: priority, overlapping conditions, simultaneous conditions, default transitions.
> 4. Timing semantics: same-cycle/next-cycle response, sampling edge, transition timing.
> 5. State semantics: initial state, illegal-state handling, recovery behavior.
> 6. Concurrency semantics: simultaneous events, conflicting conditions, event priority.

The section does not explicitly state how these six dimensions relate to the five primary categories C1–C5 in frozen PLAN §5.

## 2. Amended rule

Read Research Protocol §5 alongside frozen PLAN §5 using the following hierarchy:

1. **Primary taxonomy:** Every benchmark instance has exactly one required primary category from the frozen PLAN set: `C1`, `C2`, `C3`, `C4`, or `C5`. The meanings and boundaries of these primary categories remain those in PLAN §5.
2. **Secondary thematic tags:** The six dimensions listed in Research Protocol §5 are optional secondary tags: `reset`, `output`, `transition`, `timing`, `state`, and `concurrency`. A case may have zero, one, or multiple tags where supported by its documented requirement and interpretation evidence.
3. **No competing primary labels:** A thematic tag never replaces, duplicates, or overrides the single PLAN primary category. A tag does not independently establish ambiguity or certification status.
4. **Interactions:** Where multiple thematic dimensions materially interact, record the interaction explicitly in the case rationale or metadata; do not conceal it by assigning multiple primary categories.
5. **Analysis:** Category-level primary analyses use the C1–C5 field. Thematic analyses use the secondary-tag field and must identify their own denominator and treatment of multi-tag cases. Multi-tag counts must not be summed as if they were mutually exclusive primary-category counts.
6. **Case construction:** T08 metadata must contain one required `primary_category ∈ {C1,C2,C3,C4,C5}` field and an optional `thematic_tags` list drawn only from the six-value vocabulary above.

This amendment clarifies the relationship between the two taxonomies. It does not change the frozen PLAN definitions or the Research Protocol's six thematic descriptions.

## 3. Reason

Frozen PLAN §5 defines C1–C5 as the primary taxonomy and permits optional secondary tags. Research Protocol §5 supplies six useful thematic dimensions but does not specify their hierarchy relative to C1–C5. Without an explicit relationship, case metadata and category-level analyses could use competing primary labels. D1 selects the A3 recommendation: preserve the frozen primary taxonomy and use the Research Protocol dimensions as secondary tags.

## 4. Scope and effect

| Question | Answer |
|---|---|
| Affected instances | Future T08 metadata and subsequent cases using the clarified taxonomy; P01/P02/P05 are referenced only for read-only compatibility checks |
| Affected artifacts | New-case metadata schema, T08 template/runner validation, taxonomy documentation and analyses that consume primary categories or thematic tags |
| Are earlier results rerun? | NO. This amendment does not change outcome classes, metrics, benchmark membership, or the meaning of historical labels. |
| Effect on earlier results | No retrospective relabelling or promotion. Existing pilot results retain the protocol and metadata under which they were produced. Any future crosswalk is a separate, transparent derived view. |
| Existing records rewritten? | NO. P01, P02 and P05 metadata and all historical evidence remain unchanged. |

## 5. Validation

The following implementation checks remain required before T08 is considered validated:

1. A schema requires exactly one `primary_category` value from C1–C5.
2. The schema permits an optional list of zero or more `thematic_tags`, restricted to the six approved values.
3. Validation rejects unknown primary categories and unknown thematic tags.
4. Validation confirms that a thematic tag cannot populate or override `primary_category`.
5. Validate a newly generated case from the T08 template.
6. Run read-only compatibility checks against P02/P05 metadata; report mismatches without rewriting source records.
7. Retain schema, commands, validation output and hashes in the T08 evidence packet.

**Validation status:** Amendment approved; implementation and T08 validation are pending. This record does not claim those checks have already passed.

## 6. Approval

| Field | Value |
|---|---|
| Disposition | ACCEPT — Option A |
| Approved by | G. Naveen |
| Date | 2026-10-31 |
| Approval-register entry | [D1 author approval](../project-state/approvals/D1_TAXONOMY_RELATIONSHIP_APPROVAL_2026-10-31.md) |
| Effective from commit | `470c97e26cd066493353d12d9c8e40656c57ff95` (approved amendment creation commit) |

**Frozen-source instruction:** Do not edit or replace `Files/FORMAL_AMBIG_RTL_PLAN.md` or `Files/Research_Papers/docs/research_protocol.md`. This amendment is read alongside the frozen sources. Historical case artifacts, RTL, formal evidence, pilot outputs, logs and manifests remain immutable.
