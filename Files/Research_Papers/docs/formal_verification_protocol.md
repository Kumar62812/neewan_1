# FORMAL-AMBIG-RTL Formal Verification Protocol

## 1. Purpose

Formal verification provides the behavioral evidence used to distinguish candidate interpretations and to evaluate generated RTL.

The protocol has two related objectives:

1. certify whether paired reference RTL implementations are behaviorally distinguishable; and
2. classify whether generated LLM RTL matches a certified reference behavior under the same legal environment.

## 2. Reference-RTL objective

For a candidate ambiguity, construct:

- RTL-A for Interpretation A;
- RTL-B for Interpretation B.

The two references must implement the documented interpretations rather than merely different coding styles.

The formal question is:

> Under the declared legal environment and observable signals, are RTL-A and RTL-B behaviorally equivalent?

If yes, the pair does not establish behavioral ambiguity for the declared observable domain.

If no, a legal distinguishing behavior is evidence for the formal component of certification.

## 3. Generated-RTL objective

For each generated RTL:

1. parse and extract the intended module;
2. compile/elaborate;
3. apply the same relevant interface and environment assumptions;
4. compare against RTL-A and RTL-B;
5. classify the result as A, B, AB, M, or Invalid.

A generated implementation is not called correct solely because it compiles.

## 4. Observable behavior

Observables must be declared before final formal analysis.

Typical observables include:

- output ports;
- state-dependent externally visible signals;
- protocol handshakes;
- cycle-accurate output behavior;
- reset-visible behavior when reset is in scope.

Internal signals should not be treated as externally meaningful unless the benchmark explicitly declares them observable.

## 5. Environment assumptions

Every formal comparison must record assumptions necessary to represent legal operation, including as applicable:

- clock structure;
- reset protocol and legal reset sequences;
- input-domain restrictions;
- valid-state restrictions;
- protocol constraints;
- initial-state assumptions;
- environmental fairness or sequencing assumptions where justified.

Assumptions must not be added merely to manufacture non-equivalence or equivalence. Each assumption requires a rationale linked to the specification or the declared hardware environment.

## 6. Formal outcomes

Use a controlled vocabulary:

- **EQUIVALENT** — equivalence established over the declared environment and observables.
- **NON_EQUIVALENT** — a legal distinguishing behavior is established.
- **INCONCLUSIVE** — the tool cannot establish the requested property under the current setup.
- **INVALID** — RTL cannot be parsed/elaborated or the formal model is invalid.

A timeout is not automatically equivalent or non-equivalent.

## 7. Counterexample policy

For NON_EQUIVALENT results, preserve:

- formal tool output;
- distinguishing input sequence/trace;
- relevant reset/initial conditions;
- differing observable outputs/state where relevant;
- script and assumptions required to reproduce the result.

Counterexamples must be interpreted under the legal environment. A trace that violates declared assumptions is not a valid ambiguity witness.

## 8. Reference certification rule

A candidate can proceed from formal analysis to human certification only when:

```
Reference RTL-A valid
AND
Reference RTL-B valid
AND
Formal result = NON_EQUIVALENT
AND
difference occurs on declared observables
AND
distinguishing behavior is legal
```

Formal evidence alone does not certify linguistic ambiguity.

## 9. Equivalence and non-equivalence methodology

The implementation may use open-source or other documented formal tools. The foundation workflow should support tools such as Yosys/ABC/SymbiYosys and SAT/SMT back ends where appropriate.

The exact proof method must be recorded per instance. Possible approaches include:

- sequential equivalence checking;
- miter construction;
- bounded model checking;
- exhaustive finite-state exploration;
- SAT/SMT-based distinguishing trace search.

The project must not claim a specific tool result until it has actually been executed.

## 10. Reproducibility record

Each formal case should retain:

```
formal/
├── harnesses/
├── assumptions/
├── scripts/
└── counterexamples/
```

and metadata for:

- RTL file hashes;
- harness version;
- formal command;
- tool name/version;
- solver/backend;
- timeout/resource limits;
- result;
- counterexample path;
- date;
- repository commit.

## 11. Sanity checks

Before trusting a formal result:

- verify that RTL-A and RTL-B are both valid;
- verify that the harness connects the intended ports;
- verify clock/reset semantics;
- inspect at least one distinguishing trace for NON_EQUIVALENT results;
- check that assumptions are satisfiable;
- ensure the comparison is not vacuous;
- verify that the observables match the benchmark metadata.

## 12. Limitations

Formal verification establishes properties relative to the modeled environment and observables. It does not prove that a natural-language interpretation is linguistically reasonable.

Bounded methods may provide bounded evidence rather than unrestricted equivalence/non-equivalence unless the finite-state space or proof conditions justify a stronger conclusion.

Tool timeouts, abstraction choices, unsupported constructs, and environment assumptions must be reported rather than silently converted into success/failure labels.

## 13. Separation of evidence

Keep these claims separate:

- **Linguistic evidence:** annotators judge A and B plausible.
- **Behavioral evidence:** formal analysis establishes A and B differ.
- **LLM evidence:** a model chooses, asks about, or generates behavior relative to A/B.

The final certified-ambiguity label combines the first two; it must not be inferred from the third.
