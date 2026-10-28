# AM-003 — P01 gate deviation and proposed T08 gate handling

| Field | Value |
|---|---|
| Amendment ID | AM-003 |
| Resolves decision | D9 |
| Source document amended | `Files/FORMAL_AMBIG_RTL_PLAN.md` |
| Section(s) | §§12–13, including Gate 2 |
| Source SHA-256 before amendment | `19e1fe9abc5b8e07d96a3df339d2a020eae93fee7c9b3815a30dd49d112ee305` (transcribed from A3 §3; not independently recomputed in this draft) |
| Date drafted | 2026-10-29 |
| Drafted before or after viewing any model outcome? | AFTER — P05 exploratory pilot results were already visible |
| Status | DRAFT — NOT EFFECTIVE |

## 1. Text being amended

The frozen plan §12 states:

> Before P02–P12 are built, P01 is reviewed and frozen.

Section 13, Gate 2, requires the P01 Golden Template Freeze before P02–P12 and lists the complete artifact chain, formal positive/negative controls, reproducibility, an exercised annotation workflow, no unresolved methodology/schema/formal-contract changes, and versioned freeze status.

The [P01 Guide Meeting Record](../../02_CERTIFICATION/P01_GUIDE_MEETING_RECORD.md) records the direction “Proceed with P02 using the reviewed P01 workflow.” It also states that the meeting date and approval mode were not supplied. That record is a direction record, not an earlier amendment to the frozen plan.

## 2. Amended rule (proposed — Option B)

This proposal documents that P02/P05 work occurred while the original P01 freeze gate remained open. If the author explicitly accepts Option B:

1. Record the guide direction as the documented basis for proceeding with P02, without claiming it was a prior textual amendment.
2. Address the reusable-template and schema-freeze function through T08. T08 must define the versioned case template and exit checks, including positive/negative controls, runner behavior, and retained validation results.
3. Preserve P01/P02/P05 evidence under its original provenance and exact tested source, interface, environment, assumptions, tool configuration and retained evidence.
4. Do not retroactively upgrade a run, claim independent reproduction, certify P01, or certify P05 as ambiguous by virtue of this amendment.
5. Keep the historical gate deviation visible; do not rewrite history as if the freeze occurred earlier.

This draft is not effective until D9 is approved and entered into the decision/approval records. Until then, the original frozen-plan prerequisite remains operative. This draft does not authorize T08. Option A—complete the P01 Gate 2 freeze before T08—remains the alternative listed in A3.

## 3. Reason

The plan requires P01 freeze before P02–P12, but recorded P02/P05 work preceded the freeze. The guide record documents the reported direction to proceed, but does not itself amend the plan. A dated decision is needed to keep the actual execution sequence distinct from the operative methodology.

## 4. Scope and effect

| Question | Answer |
|---|---|
| Affected instances | P01/P02/P05 for gate-history interpretation; T08 for future template validation |
| Affected artifacts | Plan §§12–13 through this separate amendment record; guide record, gate register and T08 validation package |
| Are earlier results rerun? | No automatic rerun; if an accepted rule changes an assumption or check, assess and document any rerun separately |
| Effect on earlier results | Results remain bounded by original provenance and scope; no result is upgraded by this draft |
| Existing records rewritten? | NO |

## 5. Validation

1. Link the guide record without inventing its meeting date, mode, signature or verbatim approval wording.
2. Record the dated D9 disposition and effective amendment commit if accepted.
3. Compare P01/P02/P05 source and evidence hashes before and after adoption.
4. Define T08 exit checks and retain template/runner/positive-control/negative-control validation output.
5. Confirm no run is relabelled as independently reproduced and no ambiguity certification is inferred from this amendment.

## 6. Approval

| Field | Value |
|---|---|
| Disposition | PENDING |
| Approved by | |
| Date | |
| Approval-register entry | |
| Effective from commit | |

Template: [AMENDMENT_TEMPLATE.md](AMENDMENT_TEMPLATE.md). D9 is a substantive change to a frozen-plan gate and must not be applied without explicit author approval in the [A3 author decision form](../project-state/A3_AUTHOR_DECISION_FORM.md).
