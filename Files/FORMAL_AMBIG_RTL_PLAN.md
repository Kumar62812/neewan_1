# FORMAL-AMBIG-RTL Project Plan

**Project:** FORMAL-AMBIG-RTL — Formally Certified Ambiguity Handling in LLM-Based FSM and RTL Generation  
**Document status:** v1.0-FROZEN  
**Current phase:** Phase 1 — Research Foundation  
**Immediate milestone:** P01 — Golden Benchmark Instance v1.0

## 1. Project objective

FORMAL-AMBIG-RTL evaluates whether an RTL-generating large language model can handle underspecified natural-language hardware requirements. The project distinguishes:

1. RTL that violates a clear requirement;
2. RTL that realizes one defensible interpretation of an ambiguous requirement;
3. RTL that matches none of the certified interpretations; and
4. RTL that is invalid, incomplete, or formally inconclusive.

The central principle is:

$$
\boxed{\text{RTL differs from a single reference} \not\Rightarrow \text{RTL is incorrect}}
$$

when the natural-language requirement permits multiple reasonable, behaviorally distinct interpretations.

## 2. Frozen methodological principle

All benchmark cases follow this evidence chain:

$$
\boxed{R \rightarrow I \rightarrow S \rightarrow RTL \rightarrow F \rightarrow C}
$$

| Symbol | Meaning | Required question |
|---|---|---|
| $R$ | Natural-language requirement | What exact requirement is presented to the model? |
| $I$ | Defensible interpretation | What does the requirement mean under this reading? |
| $S$ | Behavioral specification | What exact externally observable behavior follows? |
| $RTL$ | Reference implementation | What synthesizable implementation realizes the behavior? |
| $F$ | Formal verification evidence | What is formally proven about correctness, equivalence, or divergence? |
| $C$ | Certification decision | Is the case unambiguous, certified ambiguous, unresolved, or excluded? |

Reference RTL must never be the first evidence of an interpretation. Interpretations and behavior specifications are written before RTL. Formal verification establishes behavioral relations; human plausibility review establishes whether alternative readings are reasonable.

## 3. Scientific layers that must remain separate

```text
Taxonomy
    ↓ Why might the requirement permit multiple readings?

Status
    ↓ Has the case met the evidence threshold?

Interpretation
    ↓ What does the requirement mean under one defensible reading?

Behavioral specification
    ↓ What exact observable behavior follows?

Reference RTL
    ↓ What implementation realizes that behavior?

Formal evidence
    ↓ What relationship can be proven?

Model outcome
    ↓ What did the LLM-generated RTL actually do?
```

| Layer | Must not be confused with |
|---|---|
| Taxonomy category | Certification status or model outcome |
| Certification status | LLM response quality |
| Interpretation | A particular coding style or RTL syntax |
| Behavioral specification | Reference implementation |
| Formal evidence | Linguistic plausibility |
| Model outcome | Benchmark-category label |

## 4. Certified ambiguity rule

For a requirement $R$, interpretations $I_A$ and $I_B$, and reference designs $RTL_A$ and $RTL_B$:

$$
\operatorname{CertifiedAmbiguity}(R) = \operatorname{Plausible}(I_A,I_B \mid R) \land (RTL_A \not\equiv RTL_B)
$$

A case is `CERTIFIED_AMBIGUOUS` only when:

- Both interpretations are independently judged reasonable under the annotation protocol.
- Both reference implementations satisfy one common interface and legal-environment contract.
- Formal verification identifies distinguishable externally observable behavior under that contract.
- The formal result, assumptions, script, tool version, and counterexample evidence are retained.

Different RTL alone is never evidence of ambiguity.

## 5. Frozen taxonomy

| ID | Category | Meaning |
|---|---|---|
| C1 | Unambiguous–Deterministic | Requirement sufficiently specifies one intended externally observable behavior |
| C2 | Ambiguous–Lexical/Semantic | Wording, scope, terminology, operator meaning, or signal meaning permits multiple defensible semantics |
| C3 | Ambiguous–Temporal/Sequential | Clocking, ordering, latency, reset timing, transition timing, sampling, or output timing is unresolved |
| C4 | Ambiguous–Behavioral/Functional | Functional outcome, priority, boundary behavior, or exceptional behavior is unresolved |
| C5 | Underspecified–Implementation/Environment | Behavior depends on omitted environment, initialization, interface, protocol, parameter, or implementation assumptions |

Each instance has exactly one primary category and optional secondary tags. Every ambiguity candidate must have an observable behavioral consequence; coding style, state encoding, or internal-only differences do not qualify.

## 6. Requirement-status labels

| Status | Meaning |
|---|---|
| `UNAMBIGUOUS` | One operational interpretation is supported for the tested behavior |
| `CERTIFIED_AMBIGUOUS` | At least two plausible interpretations are formally behaviorally distinct |
| `UNRESOLVED` | Evidence is insufficient to determine whether alternatives are genuinely reasonable |
| `EXCLUDED` | The item fails benchmark-quality rules |

Common exclusion reasons include `FORMALLY_EQUIVALENT`, `ALTERNATIVE_NOT_PLAUSIBLE`, `INTERNAL_CONTRADICTION`, `INVALID_REFERENCE_RTL`, `INCONCLUSIVE_FORMAL`, `ILLEGAL_DIVERGENCE_TRACE`, `MISSING_INTERFACE_CONTEXT`, `NEAR_DUPLICATE`, and `OUT_OF_SCOPE`.

## 7. Pilot benchmark plan

The pilot begins with 12 small cases. The goal is to validate the taxonomy, formal flow, annotation procedure, metadata schema, and evaluator before scaling. Evidence quality takes priority over benchmark size.

| ID | Primary category | Case type | Purpose |
|---|---|---|---|
| P01 | C1 | Unambiguous control | Clear combinational logic; golden template |
| P02 | C1 | Unambiguous control | Clear sequential logic |
| P03 | C2 | Ambiguity candidate | Ambiguous control wording |
| P04 | C2 | Ambiguity candidate | Ambiguous signal polarity or meaning |
| P05 | C3 | Ambiguity candidate | Same-cycle versus next-cycle behavior |
| P06 | C3 | Ambiguity candidate | FSM transition/output timing |
| P07 | C3 with possible C5 secondary tag | Ambiguity candidate | Reset timing interpretation where timing is the central uncertainty |
| P08 | C4 | Ambiguity candidate | FIFO boundary behavior |
| P09 | C4 | Ambiguity candidate | Simultaneous-condition or transition-priority behavior |
| P10 | C5 | Ambiguity candidate | Omitted reset/environment assumption |
| P11 | C5 | Ambiguity candidate | Handshake/interface assumption |
| P12 | Not a C1–C5 certification case | Evaluator robustness / negative-control case | Demonstrate rejection of invalid or genuinely incorrect RTL |

### Pilot construction order

$$
P01 \rightarrow P02 \rightarrow P05 \rightarrow P06 \rightarrow P08 \rightarrow P03 \rightarrow P04 \rightarrow P07 \rightarrow P09 \rightarrow P10 \rightarrow P11 \rightarrow P12
$$

This order validates deterministic infrastructure first, then sequential behavior, temporal divergence, functional ambiguity, lexical ambiguity, environment assumptions, and evaluator robustness.

## 8. P12 evaluator-robustness rule

P12 remains separate from the certified-ambiguity benchmark. It tests whether the evaluation pipeline rejects RTL that is genuinely invalid or behaviorally wrong.

| P12 subtype | Candidate condition | Expected evaluator result |
|---|---|---|
| P12a | Syntax-invalid, elaboration-invalid, or unsupported HDL | `INVALID` |
| P12b | Compiles but violates a clear C1 behavioral specification | Formal-property failure or `M` |
| P12c | Compiles but matches neither certified interpretation in an ambiguity case | `M` |
| P12d | Formal tool cannot complete within declared resource policy | `INCONCLUSIVE` |

P12 prevents the methodology from becoming permissive. A design is not accepted as an alternative interpretation merely because it differs from reference RTL.

## 9. Immediate milestone: P01 — Golden Benchmark Instance v1.0

P01 is the only active construction target until its methodology is complete, reviewed, reproducible, and frozen. It is a C1 unambiguous control used to validate the end-to-end workflow.

### P01 definition

| Field | Value |
|---|---|
| Instance ID | `P01` |
| Category | `C1 — Unambiguous–Deterministic` |
| Status | `UNAMBIGUOUS` |
| Design | Combinational 2-to-1 multiplexer |
| Valid result | Reference RTL formally satisfies the behavior |
| Negative result | Deliberately wrong but compilable RTL formally fails |
| Purpose | Validate all project artifacts before P02–P12 |

### P01 requirement

```text
Implement a combinational 2-to-1 multiplexer.

Inputs:
- a: 1-bit data input
- b: 1-bit data input
- sel: 1-bit select input

Output:
- y: 1-bit output

Behavior:
- When sel is 0, y shall equal a.
- When sel is 1, y shall equal b.

The module is combinational. It has no clock, reset, enable, storage element, or latency.
```

### P01 required artifacts

```text
benchmark/
└── pilot_v0_1/
    └── P01/
        ├── requirement.md
        ├── metadata.yaml
        ├── interpretations/
        │   └── interpretation_01.md
        ├── behavioral_specification/
        │   ├── specification_01.md
        │   └── properties.md
        ├── reference_rtl/
        │   └── rtl_01.sv
        ├── validation_rtl/
        │   └── deliberately_wrong_rtl.sv
        ├── formal/
        │   ├── properties/
        │   ├── harness/
        │   ├── scripts/
        │   ├── logs/
        │   └── counterexamples/
        ├── annotations/
        │   ├── annotation_form.yaml
        │   └── annotation_summary.yaml
        └── review/
            ├── certification_decision.md
            ├── reproducibility_check.md
            └── p01_template_freeze.md
```

### P01 behavioral specification

| `sel` | `a` | `b` | Required `y` |
|---:|---:|---:|---:|
| 0 | 0 | X | 0 |
| 0 | 1 | X | 1 |
| 1 | X | 0 | 0 |
| 1 | X | 1 | 1 |

$$
y =
\begin{cases}
a, & \text{if } sel = 0 \\
b, & \text{if } sel = 1
\end{cases}
$$

### P01 required formal checks

1. The valid reference RTL must pass all declared properties.
2. A deliberately wrong but compilable RTL implementation must fail at least one property.
3. The failing run must provide a counterexample or reproducible failure trace.
4. Tool name, version, command, timeout, assumptions, logs, and outcomes must be recorded.
5. A clean execution from a fresh clone or separate environment must reproduce the recorded outcomes.

### P01 completion gate

P01 is complete only when:

- [ ] Requirement, interpretation, behavior specification, reference RTL, formal evidence, and certification decision are present.
- [ ] Reference RTL compiles and formally passes.
- [ ] Deliberately wrong RTL compiles but formally fails.
- [ ] Failure evidence is retained.
- [ ] Metadata paths, hashes, status fields, and tool versions are complete.
- [ ] Annotation procedure is exercised and supports one intended interpretation.
- [ ] A clean reproduction succeeds without undocumented manual steps.
- [ ] Team review identifies no necessary change to the methodology, schema, or formal contract.
- [ ] P01 is committed and frozen as `Golden Benchmark Instance v1.0`.

## 10. Standard benchmark-case structure

Every later instance follows the same evidence structure. Ambiguous cases include two interpretations, two behavioral specifications, and two reference RTL designs; C1 controls include one intended interpretation and one reference design.

```text
Pxx/
├── requirement.md
├── metadata.yaml
├── interpretations/
├── behavioral_specification/
├── reference_rtl/
├── formal/
│   ├── properties/
│   ├── harness/
│   ├── scripts/
│   ├── logs/
│   └── counterexamples/
├── annotations/
└── review/
```

For a certified ambiguous case:

$$
R \rightarrow \{I_A,I_B\} \rightarrow \{S_A,S_B\} \rightarrow \{RTL_A,RTL_B\} \rightarrow F \rightarrow C
$$

No case is certified merely because two designers or two models produced different RTL.

## 11. Formal classification of generated RTL

For generated RTL $RTL_{LLM}$ on a certified ambiguous case:

$$
\operatorname{Class}(RTL_{LLM}) =
\begin{cases}
A, & RTL_{LLM} \equiv RTL_A \\
B, & RTL_{LLM} \equiv RTL_B \\
AB, & RTL_{LLM} \equiv RTL_A \land RTL_{LLM} \equiv RTL_B \\
M, & \text{otherwise}
\end{cases}
$$

Report technical failures separately:

| Label | Meaning |
|---|---|
| `INVALID` | RTL cannot be parsed, elaborated, compiled, or entered into the formal flow |
| `INCOMPLETE` | Required RTL or response content is missing |
| `INCONCLUSIVE` | Formal comparison cannot complete under the declared resource policy |
| `M` | Valid RTL formally matches neither certified interpretation |

`MISINTERPRET` applies to a valid, formally evaluable RTL result classified as `M`. It does not include syntax or tool failures.

## 12. Change-control rule

Before P02–P12 are built, P01 is reviewed and frozen. After the freeze, do not silently change taxonomy definitions, metadata fields, annotation questions, formal assumptions, scoring rules, or primary prompt formats.

Any necessary later change must be documented as a versioned amendment that states:

- why the change is needed;
- which instances and artifacts are affected;
- whether earlier results are rerun;
- whether the resulting analysis is primary, secondary, or exploratory.

## 13. Phase gates

### Gate 1 — Research Foundation Freeze

Required before benchmark construction:

- [ ] Problem statement frozen.
- [ ] Five-category taxonomy frozen.
- [ ] Requirement-status labels frozen.
- [ ] RTL outcome labels frozen.
- [ ] Benchmark schema frozen.
- [ ] Annotation protocol frozen.
- [ ] Formal-verification protocol frozen.
- [ ] Evaluation metrics and controls frozen.

### Gate 2 — P01 Golden Template Freeze

Required before P02–P12:

- [ ] Complete P01 artifact chain exists.
- [ ] Valid RTL formally passes.
- [ ] Deliberately wrong RTL formally fails.
- [ ] Reproducibility check passes.
- [ ] Annotation workflow is exercised.
- [ ] No necessary methodology/schema/formal-contract changes remain unresolved.
- [ ] P01 is versioned and frozen.

### Gate 3 — Pilot Certification

Required before model evaluation:

- [ ] P01–P12 candidate cases constructed.
- [ ] Ambiguity candidates independently annotated.
- [ ] Ambiguous cases meet the certification rule.
- [ ] C1 controls remain unambiguous.
- [ ] P12 robustness cases demonstrate rejection behavior.
- [ ] Formal evidence and counterexamples are retained.
- [ ] All unresolved/excluded cases are explicitly recorded.

### Gate 4 — Experimental Evaluation

Only after the pilot certification gate:

- [ ] Model/prompt set frozen.
- [ ] Generation conditions frozen.
- [ ] No benchmark labels exposed to the model.
- [ ] Generated RTL is stored immutably.
- [ ] Compilation and formal outcomes are recorded separately.
- [ ] Results are reproducible from the repository artifacts.

### Gate 5 — Results Freeze

Before paper analysis:

- [ ] Primary metrics are computed from frozen artifacts.
- [ ] Exceptions and inconclusive cases are reported.
- [ ] No post-hoc taxonomy changes are used to improve results.
- [ ] Exploratory analyses are clearly separated from primary results.

## 14. Immediate action

Construct P01 completely. Do not start P02–P12, large-scale benchmark generation, or LLM evaluation until P01 passes its completion gate.

**Success statement:**

> FORMAL-AMBIG-RTL can preserve the complete trace from requirement through certification, formally accept correct reference RTL, formally reject behaviorally incorrect RTL, and reproduce the result from documented artifacts.
