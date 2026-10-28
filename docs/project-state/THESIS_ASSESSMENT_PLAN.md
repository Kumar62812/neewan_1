# Thesis Assessment Plan — FORMAL-AMBIG-RTL

**Document status:** Planning document; not a results chapter.  
**As of:** 2026-10-10

## Purpose

Define what evidence is required before the thesis can make claims about ambiguity-aware LLM-generated RTL. This plan separates case-construction validity, human plausibility, formal behavioral analysis, LLM evaluation, and reporting.

## Assessment layers

### 1. Case readiness

For every case, retain:
- exact natural-language requirement and immutable version/hash;
- one or more defensible interpretations written before reference RTL;
- a behavioral specification for each interpretation;
- interface and environment assumptions;
- intended taxonomy category and provisional status;
- a traceability record linking requirement, interpretation, specification, RTL, formal artifacts, and decision.

### 2. Human plausibility

Where an ambiguity claim depends on competing interpretations:
- collect independent, separately submitted human ratings;
- predefine eligibility, scale, thresholds, and disagreement handling before collecting responses;
- report score distributions and rationales, not just an aggregate score;
- preserve minority objections, conflicts, and any adjudication;
- do not describe a case as certified ambiguous without passing the plausibility gate and the separate formal behavioral-distinction gate.

The P05 pilot protocol uses five independent reviewers as an operational feasibility threshold. This is not an externally validated threshold and does not support population-level generalization.

### 3. Formal analysis

Use the formal method appropriate to the specification and model:
- deterministic reference conformance against its stated property;
- equivalence checking between candidate interpretations where equivalence is relevant;
- a counterexample or other machine-checkable evidence when observably different behavior is claimed;
- explicit assumptions, tool versions, commands, logs, and hashes.

Formal non-equivalence establishes behavioral distinction under the encoded model; it does not establish that both behaviors are reasonable readings of the natural-language requirement.

### 4. LLM evaluation

Only evaluate a case against a certified gold-standard interpretation set after required gates pass. For each model run, record:
- provider/model name and version where available;
- date, prompt, decoding parameters, and system/context details;
- raw generated RTL and parse/elaboration result;
- property/formal outcome;
- whether the output matches interpretation A, B, both, neither, or is technically invalid/incomplete/inconclusive;
- toolchain, logs, hashes, exclusions, and deviations.

Use the exact same requirement text for all compared model runs. Distinguish within-model repeatability from between-model differences; report failures and ambiguous classifications transparently.

### 5. Reporting and claims

Before results are available, thesis chapters may describe the research question, frozen taxonomy, protocol, P01 deterministic control, and methods. They must not prestate P02–P12 results, LLM performance, benchmark-wide validity, or expected publication outcomes.

The results chapter should be populated only from retained machine/human evidence. The discussion should separate observed results from interpretation and acknowledge sampling, tool-modeling, prompt sensitivity, reviewer subjectivity, and benchmark coverage limitations.

## Current status

- P01 formal evidence: complete for documented effective tested source.
- P05 human plausibility: pending; zero responses in the current project record.
- P05 ambiguity certification: not claimed.
- LLM evaluation against P05 as a certified ambiguity case: not authorized until its gates pass.
- Thesis outcome/performance claims: not available from this plan alone.
