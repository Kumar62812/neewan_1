# FORMAL-AMBIG-RTL Benchmark Schema

## 1. Purpose

This document defines the structure and lifecycle of benchmark instances. The benchmark is intended to separate:

- certified ambiguous requirements;
- unambiguous controls; and
- negative/rejected ambiguity candidates.

A benchmark instance is not certified merely because two RTL implementations can be written.

## 2. Directory layout

```
06_Benchmarks_and_Evaluation/
├── specifications/
├── interpretations/
├── reference_rtl/
│   ├── A/
│   └── B/
├── formal/
│   ├── harnesses/
│   ├── assumptions/
│   ├── scripts/
│   └── counterexamples/
├── annotations/
├── controls/
├── negative_candidates/
└── dataset/
    └── benchmark.json
```

The repository may retain this logical structure under the broader Research_Papers directory during the foundation stage.

## 3. Required instance fields

Every instance must have a stable identifier and, at minimum:

- `instance_id`
- `version`
- `status`
- `category`
- `specification_text`
- `ambiguity_dimension`
- `interpretation_A`
- `interpretation_B`
- `interpretation_rationale_A`
- `interpretation_rationale_B`
- `reference_rtl_A`
- `reference_rtl_B`
- `formal_environment`
- `observables`
- `formal_result`
- `counterexample` when non-equivalence is established
- `annotation_record`
- `provenance`

LLM results are not required for initial certification and must not be back-filled into reference-ground-truth fields.

## 4. Status lifecycle

```
candidate
   ├──> certified_ambiguous
   ├──> unambiguous_control
   ├──> negative_candidate
   └──> inconclusive
```

A later experimental release may additionally mark an accepted record as `frozen`.

## 5. Certified ambiguous inclusion criteria

All of the following are required:

1. The original requirement is available verbatim.
2. Two interpretations are explicitly documented.
3. Both interpretations are plausible under the annotation protocol.
4. The alternatives correspond to a genuine semantic choice rather than coding style.
5. Both reference RTL implementations compile/elaborate.
6. The same declared environment is used for both references.
7. Observable signals are explicitly defined.
8. Formal analysis establishes non-equivalence under legal assumptions.
9. A reproducible counterexample or equivalent formal witness is retained when applicable.
10. Annotation and formal evidence are linked to the same instance/version.

## 6. Exclusion/rejection criteria

Reject or keep as negative/inconclusive when:

- one interpretation is clearly contradicted by the requirement;
- the difference is only stylistic or structural;
- the RTL pair is equivalent over the declared legal environment;
- formal analysis is inconclusive and the reason cannot be resolved;
- the environment permits illegal/unconstrained behavior that invalidates the intended comparison;
- the reference RTL is invalid;
- the ambiguity depends on information unavailable to an independent annotator;
- the case contains multiple unresolved dimensions that prevent a defensible attribution;
- provenance is missing.

Rejection is not failure of the project; rejected candidates provide evidence that certification is selective.

## 7. Unambiguous controls

A control should use wording intended to constrain a single reasonable interpretation. Controls should cover the same hardware concepts as ambiguity cases where practical.

Controls are used to estimate false clarification behavior and to test whether an LLM asks questions even when the specification is sufficiently explicit.

## 8. Negative controls

Negative candidates are cases initially suspected to be ambiguous but rejected after formal or human analysis. Typical reasons include:

- only one interpretation is plausible;
- alternatives are formally equivalent;
- the proposed distinction is outside the declared observables;
- the distinction requires an unreasonable reading.

Negative cases must preserve the evidence supporting rejection.

## 9. Validation checklist

Before certification, verify:

### Specification
- [ ] Exact wording stored.
- [ ] Source/provenance stored.
- [ ] Primary ambiguity dimension assigned.
- [ ] No hidden clarification supplied to the benchmark.

### Interpretations
- [ ] A documented.
- [ ] B documented.
- [ ] Rationale for each documented.
- [ ] A and B are semantically distinct.
- [ ] Neither interpretation is a deliberate strawman.

### RTL
- [ ] A compiles/elaborates.
- [ ] B compiles/elaborates.
- [ ] Same interface.
- [ ] Same clock/reset conventions unless the ambiguity concerns them.
- [ ] Observable behavior explicitly declared.

### Formal
- [ ] Environment assumptions stored.
- [ ] Formal script stored.
- [ ] Tool/version stored.
- [ ] Result reproducible.
- [ ] Counterexample/witness stored for non-equivalence.

### Human validation
- [ ] Annotators meet eligibility requirements.
- [ ] Annotation was blinded where applicable.
- [ ] Both interpretations meet the frozen threshold.
- [ ] Agreement statistic calculated.
- [ ] Adjudication record stored if needed.

## 10. Versioning

Instance identifiers must remain stable. If wording or reference RTL changes materially, create a new instance version rather than silently replacing evidence.

Recommended form:

```
FSM_RST_001
FSM_RST_001@v1
FSM_RST_001@v2
```

A frozen release must reference exact file hashes or Git commit identifiers where practical.
