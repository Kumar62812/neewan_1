# FORMAL-AMBIG-RTL Research Foundation

## Scope

**FORMAL-AMBIG-RTL** studies ambiguity in natural-language hardware requirements and its effect on large-language-model (LLM) RTL/FSM generation.

The project does not treat a single reference RTL implementation as the unquestionable ground truth when the source requirement may permit multiple reasonable interpretations. Instead, it constructs competing interpretations, implements reference RTL for those interpretations, establishes whether their observable behaviors are distinguishable under an explicit formal environment, and then uses human plausibility validation to determine whether the alternatives are genuinely reasonable readings of the requirement.

The current repository is an infrastructure and literature foundation. **No model results are claimed here.**

## Research gap

Existing natural-language-to-RTL evaluation commonly evaluates generated RTL against a predetermined target implementation or behavior. That paradigm is appropriate when the requirement determines a unique intended behavior, but it can conflate implementation error with interpretation choice when the natural-language requirement is underspecified.

The project investigates the intersection of:

1. LLM-based natural-language-to-RTL generation;
2. FSM and hardware reasoning;
3. ambiguity and clarification in requirements;
4. formal hardware verification; and
5. reproducible benchmark construction.

The intended contribution is a benchmark and evaluation methodology in which ambiguity is established before model evaluation rather than inferred from an LLM failure.

## Certified-ambiguity rule

For this project, a **certified ambiguous case** requires both:

```
Human plausibility
        AND
Formal behavioral non-equivalence
```

Operationally, the two interpretations must:

- be independently judged plausible by qualified annotators;
- arise from the same natural-language requirement;
- represent a genuine unresolved semantic choice rather than merely different coding styles;
- produce reference RTL designs that compile/elaborate under the same declared environment; and
- be formally shown to differ in an observable behavior under legal assumptions.

Formal non-equivalence by itself does **not** establish linguistic ambiguity. Conversely, linguistic ambiguity without a demonstrated behavioral distinction is not sufficient for the project's certified-ambiguity label.

## Repository map

```
Files/Research_Papers/
├── 00_Base_Paper/
├── 01_LLM_to_RTL/
├── 02_FSM_and_Hardware_Reasoning/
├── 03_Ambiguity_and_Underspecification/
├── 04_Formal_Verification/
├── 05_Requirements_Engineering/
├── 06_Benchmarks_and_Evaluation/
├── 07_Related_Work/
├── docs/
│   ├── research_protocol.md
│   ├── benchmark_schema.md
│   ├── formal_verification_protocol.md
│   └── annotation_protocol.md
├── literature/
│   ├── literature_matrix.csv
│   └── README.md
├── templates/
│   └── instance_metadata_template.yaml
├── CONTRIBUTING.md
└── README.md
```

The existing PDFs are retained. This foundation branch adds protocols and machine-readable project infrastructure; it does not delete or rewrite research papers.

## Workflow

```
Literature
   ↓
Research definition
   ↓
Candidate requirement
   ↓
Interpretation A + Interpretation B
   ↓
Reference RTL-A + RTL-B
   ↓
Formal verification
   ↓
Human plausibility annotation
   ↓
Certified / rejected / control
   ↓
LLM single-shot + interactive evaluation
   ↓
Generated RTL formal evaluation
   ↓
Metrics + statistical analysis
   ↓
Results freeze
   ↓
Paper and reproducibility package
```

## Reproducibility commitments

Every benchmark instance should retain provenance from its original specification through final evaluation. The project will preserve:

- stable instance identifiers;
- original natural-language wording;
- interpretation rationale;
- reference RTL and generated RTL separately;
- formal assumptions and observables;
- tool versions and scripts;
- proof outcomes and counterexamples;
- annotation records and agreement statistics;
- exact prompts and model/version settings;
- raw model responses;
- extraction/compilation/formal logs where appropriate; and
- derived metrics with their source data.

No manual modification of an LLM-generated RTL file may overwrite the original model output.

## Status labels

The following labels are used throughout the project:

- **candidate** — proposed benchmark instance, not yet certified.
- **formal_non_equivalent** — reference implementations differ formally under the declared legal environment.
- **human_validated** — both interpretations passed the predefined plausibility protocol.
- **certified_ambiguous** — formal non-equivalence and human plausibility requirements are both satisfied.
- **unambiguous_control** — the requirement is intended to determine a single reasonable behavior.
- **negative_candidate** — investigated as a possible ambiguity but rejected because one or more certification conditions failed.
- **inconclusive** — evidence is insufficient or the formal/annotation process requires revision.
- **frozen** — included in a versioned experimental release and protected by change-control rules.

## Current status

This branch establishes the Phase-1 research definition and the supporting documentation/schema needed to build the benchmark. It does not contain executed LLM results or claim empirical performance.

The current literature collection includes work spanning LLM-to-RTL generation, FSM reasoning, ambiguity/requirements engineering, formal verification, and natural-language-to-formal-specification workflows. The literature matrix records evidence and limitations rather than treating any one paper as the final authority.

**Working base-paper status:** LLM-FSM is currently maintained in `00_Base_Paper/` as the working base paper for the FSM/RTL-generation thread. Final base-paper selection remains subject to the completed literature comparison.

## Citation policy

- Cite the original paper whenever a literature claim is used.
- Prefer the paper's DOI, official publisher page, or stable arXiv record.
- Do not cite a secondary summary when the primary source is available.
- Keep bibliographic metadata consistent with the source.
- Distinguish source-reported findings from project interpretation.
- Do not present a paper's reported ranking, score, or claim as an independent project conclusion without verification.
- For benchmark instances, cite any source requirement or reused design material and record provenance in metadata.
- Do not claim "first" or "no prior work" without a documented literature search supporting that statement.

## Change control

Research definitions, benchmark labels, certification thresholds, and primary metrics are frozen by the Phase-1 protocol. Any substantive change after experimental execution begins must be recorded as a protocol amendment with a rationale and date. Results already generated under the previous protocol must not be silently relabeled.

See:

- [Research Protocol](docs/research_protocol.md)
- [Benchmark Schema](docs/benchmark_schema.md)
- [Formal Verification Protocol](docs/formal_verification_protocol.md)
- [Annotation Protocol](docs/annotation_protocol.md)
- [Literature Matrix Guide](literature/README.md)
- [Contribution Guide](CONTRIBUTING.md)
