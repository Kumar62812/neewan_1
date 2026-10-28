# A2 — Research Questions, Claims and Scope Freeze

**Project:** FORMAL-AMBIG-RTL
**Version:** A2-v1.0 (2026-10-28)
**Status:** Consolidation record. Author approval PENDING.
**Purpose:** Gather the existing research definitions into one execution reference **without modifying any source document**. Where the sources disagree, the disagreement is recorded in the [A2 source-inconsistency register](A2_SOURCE_INCONSISTENCY_REGISTER.md) (items D1–D16) and is not resolved here.

## 0. Source baseline

Every definition below cites its source as `[document §section]`. The sources were read at branch head `e6168aa` (`research/end-to-end-sequence`) and are byte-identical to `main` `83046997dce1`.

| Key | Document | Declared status | SHA-256 |
|---|---|---|---|
| PLAN | `Files/FORMAL_AMBIG_RTL_PLAN.md` | v1.0-FROZEN | `19e1fe9abc5b8e07d96a3df339d2a020eae93fee7c9b3815a30dd49d112ee305` |
| RP | `Files/Research_Papers/docs/research_protocol.md` | "Phase-1 foundation / pre-results freeze" | `87d3a6e7632bc46e75c23b7ff25ed7d84a09691bc1652865f250a04c34cfaa63` |
| BS | `Files/Research_Papers/docs/benchmark_schema.md` | no status line | `18b5e39599b519872a427c8463213f35bce0cf175e9d553bce3035028493fcac` |
| FVP | `Files/Research_Papers/docs/formal_verification_protocol.md` | no status line | `28fc904292f2332b42b536a26cbc7a522fee5736abb058563556bbbe20c9724f` |
| AP | `Files/Research_Papers/docs/annotation_protocol.md` | no status line | `333f9d352c9e1978208043ef6f3cacbb9aa859779214bb8dac14ea2b0d578183` |
| GOV | `docs/project-sequence/` registers and approvals (author governance, 25–28 Oct 2026) | author decisions | — |

Only PLAN declares itself frozen. RP, BS, FVP and AP are treated as the operative baseline, but their freeze is not recorded (see D12). PLAN Gate 1 ("Research Foundation Freeze") has no ticked items.

## 1. Research objective

Evaluate whether LLM-generated RTL correctly handles underspecified natural-language hardware requirements. [PLAN §1]

The project distinguishes:

1. RTL that violates a clear requirement.
2. RTL that realises one defensible interpretation of an ambiguous requirement.
3. RTL that matches none of the certified interpretations.
4. RTL that is invalid, incomplete or formally inconclusive.

Central principle: differing from a single reference does not imply that the RTL is incorrect, when the requirement permits several reasonable, behaviourally distinct interpretations. [PLAN §1]

Evidence chain [PLAN §2]:

```text
Requirement (R) -> Interpretation (I) -> Specification (S) -> Reference RTL
               -> Formal evidence (F) -> Certification (C)
```

Interpretations and specifications are written before reference RTL. Formal verification establishes behavioural relations; human review establishes whether readings are reasonable. [PLAN §2] Formal non-equivalence alone does not establish linguistic ambiguity. [RP §2]

## 2. Research questions [RP §3, verbatim]

- **RQ1:** Can hardware-specific natural-language ambiguities be systematically constructed and certified using human plausibility and formal behavioral non-equivalence?
- **RQ2:** How often do LLMs recognize certified hardware ambiguity and request clarification rather than silently selecting an interpretation?
- **RQ3:** When an LLM does not request clarification, how often does its generated RTL correspond to a certified interpretation versus neither certified interpretation?
- **RQ4:** Does interactive clarification improve formal RTL correctness relative to single-shot generation, and what interaction cost accompanies the improvement?

## 3. Hypotheses [RP §4, verbatim]

- **H1:** Certified ambiguity cases can be constructed with repeatable human-plausibility and formal-verification evidence.
- **H2:** LLMs will exhibit distinct ASK, ASSUME, and MISINTERPRET behaviors on certified ambiguous requirements.
- **H3:** Interactive clarification can change the distribution of generated behaviors and may improve formal correctness relative to single-shot generation.
- **H4:** Ambiguity behavior will vary by ambiguity category and model.

These are hypotheses, not findings, and must not be written as results until tested. [RP §4]

## 4. Primary case taxonomy [PLAN §5]

| ID | Category | Meaning |
|---|---|---|
| C1 | Unambiguous–Deterministic | Requirement sufficiently specifies one intended externally observable behaviour |
| C2 | Ambiguous–Lexical/Semantic | Wording, scope, terminology, operator meaning or signal meaning permits multiple defensible semantics |
| C3 | Ambiguous–Temporal/Sequential | Clocking, ordering, latency, reset timing, transition timing, sampling or output timing is unresolved |
| C4 | Ambiguous–Behavioural/Functional | Functional outcome, priority, boundary behaviour or exceptional behaviour is unresolved |
| C5 | Underspecified–Implementation/Environment | Behaviour depends on omitted environment, initialisation, interface, protocol, parameter or implementation assumptions |

Each case has exactly one primary category and optional secondary tags. Every ambiguity candidate must have an **observable** behavioural consequence; coding style, state encoding or internal-only differences do not qualify. [PLAN §5]

RP §5 separately lists six thematic dimensions (reset, output, transition, timing, state, concurrency). They describe *what kind* of semantic choice a case isolates and are not category IDs. The mapping between the two schemes is not defined (D1).

## 5. Requirement certification statuses [PLAN §6]

| Status | Meaning |
|---|---|
| `UNAMBIGUOUS` | One operational interpretation is supported for the tested behaviour |
| `CERTIFIED_AMBIGUOUS` | At least two plausible interpretations are formally behaviourally distinct |
| `UNRESOLVED` | Evidence is insufficient to determine whether alternatives are genuinely reasonable |
| `EXCLUDED` | Fails benchmark-quality rules, with a recorded reason |

Recorded exclusion reasons [PLAN §6]: `FORMALLY_EQUIVALENT`, `ALTERNATIVE_NOT_PLAUSIBLE`, `INTERNAL_CONTRADICTION`, `INVALID_REFERENCE_RTL`, `INCONCLUSIVE_FORMAL`, `ILLEGAL_DIVERGENCE_TRACE`, `MISSING_INTERFACE_CONTEXT`, `NEAR_DUPLICATE`, `OUT_OF_SCOPE`.

**Certification rule** [PLAN §4; RP §2; AP §7; BS §5]. A case is `CERTIFIED_AMBIGUOUS` only when **all** of the following hold:

1. Both interpretations are independently judged reasonable under the annotation protocol, each meeting the plausibility threshold **τ = 0.80** (P_A ≥ τ and P_B ≥ τ). [AP §7]
2. Both reference implementations satisfy one common interface and legal-environment contract, with observables declared in advance. [PLAN §4; FVP §4]
3. Formal verification establishes a **legal** distinguishing behaviour (`NON_EQUIVALENT`) under that contract. [PLAN §4; FVP §6]
4. Formal results, assumptions, scripts, tool versions and counterexamples are retained and linked to the same instance version as the annotation evidence. [PLAN §4; BS §5]

Different RTL alone is never evidence of ambiguity. [PLAN §4]

The schema's lifecycle labels (`candidate`, `certified_ambiguous`, `unambiguous_control`, `negative_candidate`, `inconclusive`, later `frozen`) [BS §4] use a different vocabulary from the PLAN statuses (D2). How the 1–5 annotation scale [AP §6] aggregates into P_A is not defined (D7).

## 6. Model interaction outcomes [RP §7]

| Outcome | Definition |
|---|---|
| ASK | Identifies unresolved behaviour and asks a relevant clarification question |
| ASSUME | **Silently** selects or states an interpretation without obtaining clarification |
| MISINTERPRET | Produces behaviour inconsistent with all certified interpretations. Applies only to **valid, formally evaluable** RTL classified `M`; excludes syntax and tool failures. [PLAN §11] |
| INVALID | Response/RTL cannot be evaluated because it fails extraction, parsing, elaboration or required formal checks |

Interaction outcomes are recorded separately from formal RTL match classes. [RP §7]

## 7. Formal RTL match classes [PLAN §11; RP §7]

For generated RTL on a certified ambiguous case:

| Class | Definition |
|---|---|
| A | RTL_LLM ≡ RTL_A |
| B | RTL_LLM ≡ RTL_B |
| AB | RTL_LLM ≡ RTL_A **and** RTL_LLM ≡ RTL_B |
| M | Valid RTL that matches neither |

Equivalence (≡) is over the declared environment and observables. AB is possible only when RTL_A and RTL_B differ outside the declared observable domain. [RP §7] If they were proven `NON_EQUIVALENT` on the declared observables, AB should be unreachable (D5).

Technical outcomes are reported **separately** from match classes and never collapsed into `M` [PLAN §11; FVP §6]:

| Label | Meaning |
|---|---|
| `INVALID` | Cannot be parsed, elaborated, compiled or entered into the formal flow |
| `INCOMPLETE` | Required RTL or response content is missing |
| `INCONCLUSIVE` | Formal comparison cannot complete under the declared resource policy |

A timeout is neither equivalent nor non-equivalent. [FVP §6] A design that only compiles is not called correct. [FVP §3]

## 8. Experimental conditions [RP §6, §11, §12]

- **Single-shot:** specification → LLM → RTL.
- **Interactive clarification:** specification → LLM clarification request → supplied clarification → RTL.
- **Unambiguous controls:** requirements intended to determine a single reasonable behaviour.
- **Negative candidates:** cases investigated for ambiguity but rejected by certification.

Both generation conditions use the same extraction and RTL-verification pipeline. [RP §6]

**Observation unit:** (Model, Benchmark instance, Condition, Trial). Nondeterministic trials keep their trial IDs and generation settings. [RP §11]

**Required controls** [RP §12]: unambiguous requirements; negative ambiguity candidates; compile/elaboration checks; formal-tool sanity checks; common environment assumptions across paired references; fixed observable signals; prompt and model configuration records.

No benchmark label is exposed to the model, and generated RTL is stored immutably. [PLAN §13, Gate 4]

## 9. Pilot and benchmark scope

**Pilot cases** [PLAN §7]:

| ID | Primary category | Role in the study |
|---|---|---|
| P01 | C1 | Deterministic golden control (combinational 2:1 mux); separate from the core/extension groups [GOV] |
| P02 | C1 | **Deterministic control within the core benchmark set** (T05 decision O4, 2026-10-28) [PLAN §7; GOV] |
| P05 | C3 | Core ambiguity candidate: same-cycle vs next-cycle behaviour |
| P06 | C3 | Core ambiguity candidate: FSM transition/output timing |
| P08 | C4 | Core ambiguity candidate: FIFO boundary behaviour |
| P03 | C2 | Core ambiguity candidate: control wording |
| P04 | C2 | Core ambiguity candidate: signal polarity or meaning |
| P07 | C3 (possible C5 tag) | Conditional extension: reset timing |
| P09 | C4 | Conditional extension: simultaneous-condition / priority behaviour |
| P10 | C5 | Conditional extension: omitted reset/environment assumption |
| P11 | C5 | Conditional extension: handshake/interface assumption |
| P12 | none (not C1–C5) | Conditional extension: evaluator-robustness / negative control, subtypes P12a–d [PLAN §8] |

So the core set holds **one C1 control (P02) and five ambiguity candidates**. The core/extension grouping comes from later author governance, not from PLAN (D8).

**Construction order** [PLAN §7]: P01 → P02 → P05 → P06 → P08 → P03 → P04 → P07 → P09 → P10 → P11 → P12. Core and extension labels describe scope grouping and do not replace this order. Approval of case N is required before formal work on case N+1. [GOV]

**P12 expected evaluator results** [PLAN §8]: P12a → `INVALID`; P12b → property failure or `M`; P12c → `M`; P12d → `INCONCLUSIVE`.

## 10. Primary metrics [RP §8–9]

| Metric | Source formula |
|---|---|
| ADR — Ambiguity Detection Rate | N_correctly_detected / N_certified_ambiguous |
| CR — Clarification Rate | N_relevant_ASK / N_certified_ambiguous |
| VIR — Valid Interpretation Rate | (N_A + N_B) / N_generated |
| MIR — Misinterpretation Rate | N_M / N_generated |
| FCR — Formal Correctness Rate | N_formally_correct / N_attempted_generations |
| UCR — Unnecessary Clarification Rate | N_ASK_on_unambiguous_controls / N_unambiguous_controls |
| CU — Clarification Utility | (FCR_interactive − FCR_single-shot) / Interaction cost |
| BAS — Behavioural Ambiguity Severity (optional, secondary) | D(RTL_A, RTL_B), a declared divergence measure; never replaces the certification rule |

Formulas are reproduced from RP and are **not changed here**. Several numerators and denominators still need an operational definition before results are viewed: "correctly detected", "formally correct" on ambiguous cases, the treatment of AB/INVALID/INCONCLUSIVE in VIR, MIR and FCR, and the components of interaction cost (D13). RP §8 requires interaction cost to be defined before final analysis. Metric definitions must not change after results are seen. [RP §13–14]

## 11. Benchmark size targets [RP §10]

- 80–120 ambiguity candidates
- 40–80 certified ambiguous cases after rejection
- 20–40 unambiguous controls
- 20–40 negative/rejected candidates

These are **planning targets, not achieved counts**. The pilot (P01–P12) and the scaled benchmark are distinct.

**Actual counts at 2026-10-28:** 0 certified ambiguous cases; 2 C1 controls with formal evidence (P01, P02); 1 ambiguity candidate formally distinguished but not certified (P05); 9 pilot cases not yet constructed.

## 12. Claim boundaries

- Formal non-equivalence establishes behavioural distinction only under the declared formal model and assumptions. [RP §2]
- Human plausibility and formal distinction are separate, jointly required conditions. [PLAN §4]
- A hypothesis is not a result. [RP §4, §15]
- A planned benchmark size is not an achieved dataset size. [RP §10]
- A pilot result is not evidence of general model accuracy. The P05 Groq pilot (PR #9, three samples) is **exploratory** because it ran before PLAN Gate 3 (D10).
- `INVALID`, `INCOMPLETE`, `INCONCLUSIVE` and proven-failing (`M`) outcomes are never conflated. [PLAN §11]
- No ambiguity certification is claimed without satisfying the certification rule in §5.
- Every reported empirical claim traces to retained evidence. [BS §9–10; PLAN §4]
- Reports separate protocol definitions, observed results, interpretation and limitations. [RP §15]

## 13. Source documents and change control

This document consolidates existing definitions. It does not replace PLAN, RP, BS, FVP or AP, and none of them was modified.

A **substantive** change (certification rule, annotation threshold, inclusion/exclusion, outcome class, primary metric, experimental condition, model-selection criteria, or formal assumptions affecting the legal behaviour space) requires a dated, versioned amendment stating why, what is affected, whether earlier results are rerun, and whether the analysis is primary, secondary or exploratory. [PLAN §12; RP §14] Earlier results stay associated with the protocol version under which they were produced. [RP §14]

Inconsistencies found while preparing A2 are listed in the [source-inconsistency register](A2_SOURCE_INCONSISTENCY_REGISTER.md). They are recorded, not resolved.

## 14. A2 completion checklist

- [x] Research questions RQ1–RQ4 recorded (verbatim from RP §3).
- [x] Hypotheses H1–H4 recorded as hypotheses (verbatim from RP §4).
- [x] C1–C5 taxonomy recorded (PLAN §5), kept distinct from the RP §5 thematic dimensions.
- [x] Certification statuses and the full certification rule (including τ = 0.80) defined.
- [x] Interaction outcomes separated from RTL match classes and from technical outcomes (including `INCOMPLETE`).
- [x] Experimental conditions, observation unit, controls and benchmark scope recorded, with P02's role as a C1 control.
- [x] Metric names and source formulas referenced, with open operational gaps flagged.
- [x] Target ranges distinguished from actual counts.
- [x] Claim boundaries and source references (with SHA-256) recorded.
- [x] No source document modified: PLAN, RP, BS, FVP and AP hashes are unchanged.
- [ ] Author approval of A2-v1.0.