# Chapter 1 — INTRODUCTION & PROBLEM FORMULATION

**Status:** Ordered thesis outline. Draft claims only after their cited sources are verified.

## Front matter (before Chapter 1)

- Project: FORMAL-AMBIG-RTL
- Repository: Kumar62812/neewan_1
- Author: Naveen Gugulothu
- Institution: NIT Warangal
- Roll number: 25ECM1R11
- Add supervisor, department, degree, and submission date only from confirmed university records.

## 1.1 Background and Significance

Use this five-part introduction funnel in the order shown. The first three parts establish the context in 1.1; the fourth is developed in 1.2; the fifth is completed in 1.3.

1. **Broad context:** LLMs are being explored for EDA tasks, including RTL generation, verification, and debugging. Support each claim with a verified primary source.
2. **Evaluation context:** Explain how existing RTL-generation evaluations define correctness and what reference behavior they assume. Do not generalize from one benchmark to all prior work.
3. **Hardware-specific problem:** Hardware requirements can leave clocking, reset, ordering, latency, or output timing unspecified. The reset example in the supplied outline is illustrative; identify it as an example, not a measured result.
4. **Research gap:** Transition to the two gaps in 1.2, supported by the three-bucket literature synthesis in Chapter 2.
5. **Research response:** Introduce the evidence-based approach and research objectives in 1.3 without claiming the evaluation has already succeeded.

The significance claim is that a generated implementation may differ from one reference because it is incorrect, because it follows another defensible reading, or because the evidence is insufficient. Formal behavioral analysis and human plausibility answer different parts of that classification.

**Sources to verify:** [frozen research plan](../../../Files/FORMAL_AMBIG_RTL_PLAN.md), [research protocol](../../../Files/Research_Papers/docs/research_protocol.md), and the [literature matrix](../../../Files/Research_Papers/literature/literature_matrix.csv).

## 1.2 Research Gaps (FORMAL-AMBIG-RTL)

### Gap 1 — Single-ground-truth limitation

Explain the risk in evaluating generated RTL against one reference when the requirement may permit multiple readings. Support the scope of this claim paper by paper; do not say all existing benchmarks have this limitation unless the reviewed evidence establishes that.

### Gap 2 — Lack of Formal Behavioral Ground Truth

Explain why reset priority, clock edges, sequential state, and timing can affect externally observable behavior. Contrast this with software ambiguity work only after verifying what those studies actually measure. The claimed gap is the need to pair plausible hardware interpretations with formal behavioral evidence; it is not a claim that software ambiguity research is invalid.

**Problem statement:** Determine whether a generated RTL result is incorrect, matches a defensible alternative interpretation, or cannot be classified from the available evidence.

## 1.3 Research Objectives and Scope

Use the frozen research questions from the [research protocol](../../../Files/Research_Papers/docs/research_protocol.md):

- **RQ1:** Can hardware-specific natural-language ambiguities be systematically constructed and certified using human plausibility and formal behavioral non-equivalence?
- **RQ2:** How often do LLMs recognize certified hardware ambiguity and request clarification rather than silently selecting an interpretation?
- **RQ3:** When an LLM does not request clarification, how often does its generated RTL correspond to a certified interpretation versus neither certified interpretation?
- **RQ4:** Does interactive clarification improve formal RTL correctness relative to single-shot generation, and what interaction cost accompanies the improvement?

Map objectives to those questions: construct and assess cases; verify reference behavior; evaluate single-shot and interactive model behavior only after gates pass; and report correctness, clarification, cost, and limitations from retained evidence. The protocol’s H1–H4 are hypotheses, not findings.

Use the protocol’s full operational definition, not a shortened version:

**CA(S) = P(I_A | S) AND P(I_B | S) AND (R_A is not behaviorally equivalent to R_B)** under the declared legal environment and observables.

Both references must be valid and conform to their own specifications. Non-equivalence alone does not show that both readings are linguistically plausible.

**Scope boundary:** P01 and P02 are C1 unambiguous controls. P05 is an ambiguity candidate with formal distinction reported and human plausibility pending; it is not currently a certified ambiguity. The planned benchmark scale and future cases are targets or future work, not completed results. Use the [phase workboard](../../project-state/PHASE_WORKBOARD.md) for the current audited position.

**Contribution wording:** Describe the methodology, evidence chain, and implemented artifacts that are actually present. Do not claim benchmark-wide validity, completed model evaluation, or successful resolution of the research gap before those results exist.

**Chapter roadmap:** Chapter 2 synthesizes prior work; Chapter 3 defines the method; Chapter 4 reports retained evidence and any eligible model results; Chapter 5 draws only evidence-supported conclusions.

