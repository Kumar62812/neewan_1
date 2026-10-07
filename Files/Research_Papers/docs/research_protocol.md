# FORMAL-AMBIG-RTL Research Protocol

**Protocol status:** Phase-1 foundation / pre-results freeze  
**Scope:** research definition, benchmark evaluation, and LLM experiment governance

## 1. Problem definition

Natural-language hardware requirements can leave semantic choices unresolved. A conventional single-reference RTL evaluation can therefore classify a generated implementation as incorrect even when it corresponds to another reasonable interpretation of the same requirement.

FORMAL-AMBIG-RTL addresses this by constructing multiple human-plausible interpretations, implementing reference RTL for each interpretation, formally testing their observable behavioral distinction, and then evaluating LLM behavior against this certified ground truth.

## 2. Central operational definition

A specification (S) is a **certified ambiguity** when:

[
CA(S) = P(I_A|S) land P(I_B|S) land (R_A \not\equiv R_B)
]

where:

- (I_A), (I_B) are competing interpretations;
- (P(I|S)) means the interpretation passes the predefined human-plausibility protocol;
- (R_A), (R_B) are reference RTL implementations;
- (R_A \not\equiv R_B) means they are behaviorally non-equivalent under the declared legal environment and observables.

Formal non-equivalence is evidence of a behavioral distinction, not proof of linguistic ambiguity by itself.

## 3. Research questions

**RQ1.** Can hardware-specific natural-language ambiguities be systematically constructed and certified using human plausibility and formal behavioral non-equivalence?

**RQ2.** How often do LLMs recognize certified hardware ambiguity and request clarification rather than silently selecting an interpretation?

**RQ3.** When an LLM does not request clarification, how often does its generated RTL correspond to a certified interpretation versus neither certified interpretation?

**RQ4.** Does interactive clarification improve formal RTL correctness relative to single-shot generation, and what interaction cost accompanies the improvement?

## 4. Hypotheses

**H1:** Certified ambiguity cases can be constructed with repeatable human-plausibility and formal-verification evidence.

**H2:** LLMs will exhibit distinct ASK, ASSUME, and MISINTERPRET behaviors on certified ambiguous requirements.

**H3:** Interactive clarification can change the distribution of generated behaviors and may improve formal correctness relative to single-shot generation.

**H4:** Ambiguity behavior will vary by ambiguity category and model.

These are research hypotheses, not expected results. They must not be written as findings until tested.

## 5. Ambiguity taxonomy

The initial taxonomy is:

1. **Reset semantics:** synchronous/asynchronous reset, polarity, priority, reset value.
2. **Output semantics:** Mealy/Moore, registered/combinational output, current-state/next-state interpretation.
3. **Transition semantics:** priority, overlapping conditions, simultaneous conditions, default transitions.
4. **Timing semantics:** same-cycle/next-cycle response, sampling edge, transition timing.
5. **State semantics:** initial state, illegal-state handling, recovery behavior.
6. **Concurrency semantics:** simultaneous events, conflicting conditions, event priority.

A case should normally isolate one primary ambiguity dimension. Secondary interactions may be recorded explicitly rather than hidden.

## 6. Experimental conditions

At minimum:

- **Single-shot:** specification → LLM → RTL.
- **Interactive:** specification → LLM clarification request → supplied clarification → RTL.
- **Unambiguous controls:** specifications intended to determine a single reasonable behavior.
- **Negative candidates:** cases investigated for ambiguity but rejected by the certification protocol.

All conditions use the same extraction and RTL-verification pipeline.

## 7. LLM outcome taxonomy

At the interaction level:

- **ASK:** identifies unresolved behavior and asks a relevant clarification question.
- **ASSUME:** silently selects or states an interpretation without obtaining clarification.
- **MISINTERPRET:** produces behavior inconsistent with all certified interpretations.
- **INVALID:** response/RTL cannot be evaluated because it fails extraction, parsing, elaboration, or required formal checks.

Generated RTL classification is recorded separately:

[
Class(R_{LLM}) =
egin{cases}
A & R_{LLM} \equiv R_A \
B & R_{LLM} \equiv R_B \
AB & R_{LLM} \equiv R_A land R_{LLM} \equiv R_B \
M & 	ext{otherwise}
end{cases}
]

The AB class is retained because an implementation can be behaviorally compatible with both references when the references differ only outside the declared observable domain.

## 8. Primary metrics

**Ambiguity Detection Rate**

[
ADR = \frac{N_{correctly\ detected}}{N_{certified\ ambiguous}}
]

**Clarification Rate**

[
CR = \frac{N_{relevant\ ASK}}{N_{certified\ ambiguous}}
]

**Valid Interpretation Rate**

[
VIR = \frac{N_A + N_B}{N_{generated}}
]

**Misinterpretation Rate**

[
MIR = \frac{N_M}{N_{generated}}
]

**Formal Correctness Rate**

[
FCR = \frac{N_{formally\ correct}}{N_{attempted\ generations}}
]

**Unnecessary Clarification Rate**

[
UCR = \frac{N_{ASK\ on\ unambiguous\ controls}}{N_{unambiguous\ controls}}
]

**Clarification Utility**

[
CU = \frac{FCR_{interactive}-FCR_{single-shot}}{Interaction\ Cost}
]

Interaction cost must be defined before final analysis; candidate components include clarification turns, tokens, latency, and human response effort.

## 9. Optional secondary metric: behavioral ambiguity severity

Where exhaustive or bounded exploration is practical, record:

[
BAS = D(R_A,R_B)
]

where (D) is a declared behavioral-divergence measure such as shortest distinguishing input sequence or another reproducible trace-based measure.

BAS is secondary and must not replace the binary certification rule.

## 10. Benchmark targets

The planned benchmark envelope is:

- 80–120 ambiguity candidates;
- 40–80 certified ambiguous cases after rejection;
- 20–40 unambiguous controls;
- 20–40 negative/rejected candidates.

These are target ranges, not claimed dataset counts. The final counts must be reported after construction and certification.

## 11. Data unit

The experimental observation unit is:

[
(Model, Benchmark Instance, Condition, Trial)
]

All nondeterministic trials must retain their trial identifiers and generation settings.

## 12. Controls

Controls must include:

- unambiguous requirements;
- negative ambiguity candidates;
- compile/elaboration checks;
- formal-tool sanity checks;
- common environment assumptions across paired references;
- fixed observable signals;
- prompt and model configuration records.

## 13. Results freeze

Before final statistical analysis, freeze:

- benchmark membership;
- certification labels;
- annotation data;
- model/version list;
- prompt templates;
- sampling settings;
- formal-tool versions;
- metric definitions;
- primary hypotheses.

Any post-freeze modification must be recorded in a change log and must identify whether the change was made before or after viewing model outcomes.

## 14. Change-control rules

A change is **substantive** if it changes:

- what qualifies as certified ambiguity;
- an annotation threshold;
- benchmark inclusion/exclusion;
- an outcome class;
- a primary metric;
- the experimental condition;
- model-selection criteria;
- formal assumptions that affect the legal behavior space.

Substantive changes require a dated protocol amendment and rationale. Previously generated results remain associated with the protocol version under which they were produced.

## 15. Reporting rule

The final paper must distinguish:

1. **protocol definitions** — fixed before model results;
2. **observed results** — produced by experiments;
3. **interpretation/analysis** — explanations supported by evidence;
4. **limitations** — known threats to validity.

No expected result, hypothesis, or target range may be presented as an achieved result.
