# FORMAL-AMBIG-RTL — End-to-End Research Sequence

**Purpose:** Provide the authoritative execution map for taking FORMAL-AMBIG-RTL from its research question through benchmark construction, controlled LLM experiments, formal classification, reproducibility, thesis/manuscript preparation, independent review, adjudication, and release.

**Status convention:** Status labels describe the evidence currently reported in the project record. “Documented” does not mean independently validated; “formal evidence exists” does not by itself mean a case is certified as ambiguous. Do not silently upgrade a status without retaining the supporting artifacts.

## End-to-end research flow

Research problem → Literature → Methodology → P01 control → P02 validation → Case template → P05 validation → Remaining benchmark cases → Evaluation infrastructure → Experimental protocol → LLM experiments → Formal classification → Statistical analysis → Technical reproduction → Thesis/manuscript → Technical freeze → Independent human review → Final adjudication → Publication and release

The order encodes scientific dependencies. Previously completed or attempted work must be preserved and audited, not repeated unnecessarily or retrospectively relabelled. A later stage cannot be treated as complete merely because its files exist.

## Stage register

| Stage | Project work | Current evidence-based position | Exit evidence / gate |
|---:|---|---|---|
| 00 | Establish research question, objectives, and contributions | Documented | Explicit research questions, scope, and contribution claims with traceable rationale |
| 01 | Literature review, novelty assessment, and research gaps | Foundation exists; latest audit pending | Search/screening record, paper inventory, synthesis, and qualified novelty/gap claims |
| 02 | Define ambiguity taxonomy, specifications, formal methodology, and governance | Documented; governance reconciliation ongoing | Consistent definitions, case schema, decision rules, and change-control policy |
| 03 | Build, verify, and preserve P01 golden control | Formal evidence exists; final freeze unresolved | Immutable source/archive, hashes, tool versions, commands, logs, counterexample where applicable, and explicit gate decision |
| 04 | Reconcile P02 requirement, interpretations, specifications, and provenance | Current Task 5; closure pending | Requirement-to-interpretation-to-specification traceability; source hashes and discrepancy resolution |
| 05 | Finalise P02 validation and close technical/provenance gates | Formal evidence exists; Task 6 gated | Reproducible formal result, preserved evidence package, and authorized gate closure |
| 06 | Validate reusable benchmark template, runner, and negative controls | Planned technical work | Same-interface controls, known-pass and known-fail checks, deterministic runner, and documented failure handling |
| 07 | Validate and freeze P05 technical ambiguity candidate | Technical evidence exists; certification pending | Frozen requirement, interpretations A/B, specifications, hashes/source commit, formal distinction evidence; human plausibility remains unclaimed until reviewed |
| 08 | Construct and formally validate P06 | Planned | Complete provenance chain and reproducible formal results |
| 09 | Construct and formally validate P08 | Planned | Complete provenance chain and reproducible formal results |
| 10 | Construct and formally validate P03 | Planned | Complete provenance chain and reproducible formal results |
| 11 | Construct and formally validate P04 | Planned | Complete provenance chain and reproducible formal results |
| 12 | Construct approved extension cases P07 and P09–P12 | Conditional on author approval | Explicit approval and case-specific rationale before construction |
| 13 | Freeze technical benchmark cases, metadata, and exclusion records | Pending | Versioned case manifest, hashes, inclusion/exclusion reasons, and immutable benchmark snapshot |
| 14 | Validate generated-RTL evaluation infrastructure | Draft infrastructure exists | Clean-checkout runner, tests, environment/tool versions, logs, error handling, and validated expected outcomes |
| 15 | Freeze models, prompts, sampling, comparison, and analysis protocols | Pending | Preregistered or version-controlled protocol; model/version identifiers, decoding settings, seeds where supported, and analysis plan |
| 16 | Execute controlled LLM single-shot and disambiguated-generation experiments | P05 exploratory Groq pilot exists; full study pending | Complete run ledger, raw outputs, failures, exact prompts/settings, and reproducible execution records |
| 17 | Execute interactive clarification experiments | Pending | Defined interaction policy, budgets, stopping rules, transcripts, and comparable outcome records |
| 18 | Formally classify outputs against both interpretations and run statistical analysis | Pending | Classification rules, per-output evidence, confusion/error accounting, uncertainty estimates, and appropriate statistical tests |
| 19 | Conduct technical integrity checks, reproducibility testing, and error analysis | Pending | Independent clean reproduction, discrepancy log, sensitivity/error analysis, and resolved or disclosed failures |
| 20 | Complete technical thesis/manuscript and freeze reviewer-accessible evidence | Pending | Claim-to-evidence map, complete methods/results, limitations, artifact manifest, and frozen review package |
| 21 | Conduct independent human reviews after technical completion | Pending | Reviewer instructions, blinded/independent judgements where applicable, agreement analysis, and preserved review records |
| 22 | Adjudicate ambiguity labels, finalise valid claims, and release thesis, paper, and artifacts | Pending | Predefined adjudication rules applied, claims aligned to evidence, release checks completed, and persistent artifact/version links |

## Scientific gate rules

1. **Preserve the evidence chain:** Requirement → Defensible interpretation → Behavioral specification → Reference RTL → Formal evidence → Certification decision.
2. **Keep formal distinction separate from human plausibility.** Different formal behavior can establish a technical distinction under a stated contract; it does not alone prove that both interpretations are linguistically reasonable.
3. **Do not infer completion from plans or file presence.** A stage closes only when its exit evidence exists and is linked from the project records.
4. **Keep accepted evidence immutable.** Corrections, reruns, or new tool environments must produce versioned evidence rather than overwrite historical logs, traces, archives, or hashes.
5. **Do not silently promote exploratory results.** The existing P05 exploratory Groq pilot remains exploratory until the complete controlled protocol and evidence requirements are satisfied.
6. **Respect case authorization.** P07 and P09–P12 remain conditional on author approval.
7. **Keep technical completion and certification distinct.** The technical benchmark, experiments, analysis, reproduction, and manuscript can be prepared before independent human review, but final ambiguity certification and final claims must reflect adjudication.
8. **Retain exclusions and failures.** Record malformed outputs, tool errors, excluded cases, missing runs, and deviations with reasons; do not discard them merely because they complicate results.

## Current operating position

The repository's current documented gate state is:

**R ✓ → I ✓ → S ✓ → RTL ✓ → F ✓ → C: PENDING**

This is the repository-level P01 position recorded in the project README: P01 certification is not complete, and the existence of formal evidence must not be misreported as certification. P02–P12 construction, benchmark scaling, and LLM evaluation remain subject to the applicable P01/P02 and governance exit gates. Reconcile this sequence with the current project compass and evidence registers before authorizing any gated work.

## Change control

- This document is a roadmap, not evidence that any pending experiment or review has been performed.
- Update a stage's status only with a dated evidence link, artifact identifier, or commit reference.
- Record scope changes and approved deviations explicitly.
- Keep the project compass, case manifests, provenance/evidence registers, and this sequence consistent; when they disagree, flag the discrepancy and resolve it transparently rather than silently choosing one.
