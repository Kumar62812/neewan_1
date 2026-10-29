# C1 — Pilot Benchmark Inventory and Readiness Register

**Prepared:** 2026-10-29  
**Repository:** \`Kumar62812/neewan_1\`  
**Working branch:** \`research/end-to-end-sequence\`  
**Inventory snapshot inspected:** \`50b8d926b8c8b29fa2375eda40b0c6cfa48325f2\`  
**Machine-readable companion:** [C1_PILOT_CASE_INVENTORY_v1.json](evidence/C1_PILOT_CASE_INVENTORY_v1.json)

## 1. Objective

Establish one source-grounded inventory of the P01–P12 pilot-case paths, technical artifacts, and known closure gates before case expansion. This is a read-only audit of the repository snapshot. It does not create missing case content, alter formal evidence, approve an amendment, or certify a case.

## 2. Inventory result

The recursive repository-tree inspection found case-directory path components for **P01, P02, and P05 only**. No path component for P03, P04, P06, P07, P08, P09, P10, P11, or P12 was found in the inspected tree. This means those cases are **not evidenced in this repository snapshot**; it does not rule out local-only materials outside the inspected repository.

| Case | Reported group | Case directory present? | Observed state | Immediate gap / gate |
|---|---|---:|---|---|
| P01 | Control; outside P02–P12 scope | Yes | Formal evidence and package-integrity/CI checks recorded | Golden Template **NOT FROZEN**; independent certification and D2/D14 decisions remain open |
| P02 | Core (reported) | Yes | Requirement, interpretation, specification, RTL, formal runner/properties, run-01/run-02 evidence and results present | T06 technical/provenance closure remains **IN PROGRESS**; publication/merge wording is inconsistent across repository records |
| P03 | Core (reported) | **No** | No case path found | Approved requirement/case definition and artifacts not evidenced |
| P04 | Core (reported) | **No** | No case path found | Approved requirement/case definition and artifacts not evidenced |
| P05 | Core (reported) | Yes | Formal behavioral distinction recorded; human plausibility review pending | Zero human responses; status remains **UNRESOLVED**; no ambiguity certification |
| P06 | Core (reported) | **No** | No case path found | Approved case construction and evidence not evidenced |
| P07 | Conditional extension (reported) | **No** | No case path found | Explicit eligibility/author approval required before construction |
| P08 | Core (reported) | **No** | No case path found | Approved case construction and evidence not evidenced |
| P09 | Conditional extension (reported) | **No** | No case path found | Explicit eligibility/author approval required before construction |
| P10 | Conditional extension (reported) | **No** | No case path found | Explicit eligibility/author approval required before construction |
| P11 | Conditional extension (reported) | **No** | No case path found | Explicit eligibility/author approval required before construction |
| P12 | Conditional extension (reported) | **No** | No case path found | Explicit eligibility/author approval required before construction |

**Scope caveat:** Core/extension labels above reflect the project crosswalk and stage register's *reported* Amendment 05 scope. The signed, approved master-plan source text was not located for independent comparison. These labels are not new approval evidence.

## 3. Evidence pointers for existing pilot cases

### P02 — deterministic sequential control

Primary files present in the inspected tree:

- \`P02/P02_REQUIREMENT.md\`, \`P02/P02_INTERPRETATION.md\`, \`P02/P02_SPECIFICATION.md\`
- \`P02/P02_CONSISTENCY_REVIEW.md\`, \`P02/P02_RESULTS.md\`, \`P02/metadata.json\`
- \`P02/reference_rtl/register.sv\`, \`P02/validation_rtl/wrong_reset.sv\`, \`P02/validation_rtl/wrong_async.sv\`
- \`P02/formal/\` runner, harness, property and strategy sources
- \`P02/evidence/run-01/\` and \`P02/evidence/run-02/\` retained evidence trees

The result record reports reference BMC and induction PASS, eight cover goals reached, and expected failures for the two deliberately incorrect controls. Its scope is the documented Boolean stable-edge digital environment; this must not be widened into a physical-timing, four-state, ambiguity, or benchmark-wide claim. The project sequence still records T06 as IN PROGRESS.

Repository publication state is intentionally not resolved in C1: some records describe PR #6 as open/not merged, while other repository navigation text describes the P02/P05 evidence as part of the published tree. This register relies on the observable files in the inspected branch and does not infer merge or task approval from file presence.

### P05 — candidate response-latency case

Primary files present in the inspected tree:

- \`P05/P05_REQUIREMENT.md\`, \`P05/P05_INTERPRETATIONS.md\`, \`P05/P05_SPECIFICATIONS.md\`
- \`P05/P05_RESULTS.md\`, \`P05/metadata.json\`, \`P05/formal/\`
- \`P05/evidence/run-01/\` and \`P05/evidence/run-02/\`
- \`P05/annotation/v1/README.md\`, \`reviewer_form.md\`, and \`analysis_protocol.md\`

The result record reports A/B conformance and induction PASS under the tested model and a legal distinguishing trace in the post-reset equality check. The metadata and plausibility status record zero human annotations, unresolved plausibility, and no ambiguity certification. Human review remains a separate required gate; formal distinction alone is not sufficient.

## 4. Work sequencing from the observed state

1. **Keep P01 as the control reference**, not as evidence that the Golden Template freeze is complete.
2. **Complete T06 for P02** using the existing closure review, preserving run-01/run-02 files and hash records; do not rewrite evidence to resolve documentation discrepancies.
3. **For P05, close the human-plausibility gate** using the existing frozen-version/hash and five-reviewer protocol, and preserve all individual responses and minority objections. Until the gate passes, P05 remains unresolved and cannot be called a certified ambiguity case.
4. **Before creating P03/P04/P06/P08**, locate or establish the authorized case-definition/version and follow the repository's case-by-case authorization rule. Do not invent case titles or jump directly to RTL/formal runs.
5. **Before P07/P09–P12**, record explicit eligibility/author approval because the project register identifies them as conditional extensions.
6. Reconcile PR/main publication status and locate the approved master-plan text as separate provenance tasks; this inventory does not silently settle either issue.

## 5. What C1 establishes — and what it does not

**Established:** A branch-snapshot inventory of P01–P12, canonical path presence, source/evidence pointers for existing P02/P05, current known gates, and missing case-directory gaps.

**Not established:** Completion of missing cases, a P02 T06 closure decision, P05 human plausibility, independent certification, P01 freeze, benchmark-wide freeze, any new formal run, or any LLM evaluation outcome.

No case source, RTL, formal log, witness, run manifest, accepted archive, or approval record was changed.

## 6. Provenance and limitations

- The exact approved 56-task A–H checklist wording was not present in the inspected repository/library snapshot; this artifact records C1 as the inventory/readiness baseline and does not reconstruct missing official task wording.
- The reported core/extension list is not freshly verified against a signed approved master plan.
- Missing from the inspected tree means missing from this tree snapshot, not proof that local-only work never existed.
- Existing status documents contain historical or inconsistent publication statements; conflicts are disclosed, not resolved by inference.

## C2 follow-up — source/evidence integrity

C1's path inventory is followed by [C2 — P02/P05 Retained Evidence and Source Alignment Audit](C2_P02_P05_EVIDENCE_ALIGNMENT.md). The C2 CI audit passed 198 checks, verified all four retained P02/P05 run manifests, and matched all 19 selected root formal-source files against the run-02 snapshots. It also preserves the known P05 reviewer-form version difference as a required action before human review; see the [machine-readable C2 evidence record](evidence/C2_P02_P05_VALIDATION_RUN_40808854269.json).

