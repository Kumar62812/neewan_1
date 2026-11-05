# Integrated DAC 2027 paper — working editorial specification

**Status: Working plan; NOT READY and NOT SUBMITTED.** See [Phase 0 evidence audit](../../docs/project-state/PHASE0_DAC_INTEGRATION_2026-11-06.md). This directory does not replace the original Task 6/7 frozen outputs or P05 pilot manuscript.

**Working title:** *When Should LLMs Ask? Formal Evaluation of Requirement Clarification in RTL Generation*

**Primary question:** Under a fixed RTL formal evaluation environment, does the one-round interactive clarification condition increase proven interpretation-specific conformance relative to a concurrent direct RTL condition? Does the model elect to ask a relevant clarification question? How do historical explicit-specification baselines inform, but not causally establish, that result?

## Paper structure

| Manuscript page | Evidence and contribution |
|---|---|
| 1 | RTL ambiguity and motivating interpretation pair; exact claims/limitations |
| 2 | Requirement → interpretation → formal contract → RTL → classification; Task 6/7 protocol and oracle |
| 3 | Task 6 R vs explicit S1/S2 outcomes; adapt Tables I/II only after frozen row/count audit |
| 4 | Task 7 concurrent IQ-vs-CR results, question rate and multiplicity-controlled P04/I1 comparison |
| 5 | Task 6-to-Task 7 P03 drift, question-selected subgroup limits and sensitivity checks |
| 6 | API failures vs formal classes; inconclusive/proof limits; pending human review; threats, related work and conclusion |

Check the official DAC 2027 author instructions before finalising pages, references, anonymity and AI-assistance disclosures. Do not pad pages with unsupported material.

## Required claim boundaries

- Main Task 7 comparison: P04/I1 18/20 vs 6/20, Holm 0.0017105323 **in the supplied frozen-analysis report**, with exact cell and reference-spec definitions to audit.
- `74/200` is a question-asking frequency, not an estimated causal effect of asking.
- `41/41` is not publishable until reconstructed from explicit disjoint trial IDs and formal-status selection.
- Task 6 `125/320` = API failures, not 39% formal correctness failures in Task 7.
- P03 historical R 12/20 vs later concurrent CR 20/20 is an observed cross-window difference, not proof of retraining or a causal drift mechanism.
- Classify syntactic invalidity, non-equivalence, inconclusive and proof-supported conformance separately. Never infer linguistic ambiguity from non-equivalence alone.
- Section 14 independent review is still pending; do not claim independent certification.
- One model and five ambiguous task cases do not establish generalisation to models, benchmarks or semantic ambiguity classes.

## Required next artifacts

- Frozen Task 6 Tables I/II with trial-ID-to-cell traceability.
- Integrated, template-compliant LaTeX manuscript and verified bibliography.
- Aggregate and per-class Task 7 outcome table (including negative/inconclusive observations).
- Independent Section 14 review and the authorised closure record.
- Guide/co-author approval and actual DAC submission receipt.

This directory is intentionally editorial; it does not claim that the manuscript, results packages or review data were fully merged into the remote branch.
