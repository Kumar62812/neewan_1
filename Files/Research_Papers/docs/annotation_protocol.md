# FORMAL-AMBIG-RTL Annotation Protocol

## 1. Purpose

Human annotation establishes whether competing interpretations of a natural-language hardware requirement are plausible readings of the original wording.

Annotation does not replace formal verification. It provides the linguistic component of the certified-ambiguity rule.

## 2. Annotator eligibility

Target annotators should have demonstrable experience with digital hardware design, RTL/HDL, FSMs, verification, requirements engineering, or a closely related area.

The study record should retain:

- anonymized annotator identifier;
- relevant expertise category;
- training completion;
- annotation batch/version.

Personal identifying information should not be stored in the public benchmark unless explicitly authorized.

## 3. Blinding

Where practical, annotators should not be shown:

- LLM outputs;
- model identities;
- experimental hypotheses about a specific model;
- final formal results before their plausibility judgment.

The aim is to prevent model behavior or formal outcomes from influencing the linguistic plausibility assessment.

## 4. Annotation unit

For each candidate, provide:

- original specification;
- Interpretation A;
- Interpretation B;
- concise interpretation rationales.

Do not reveal which interpretation is considered the project author's preferred reading.

## 5. Core questions

Annotators answer:

**Q1.** Is Interpretation A a reasonable reading of the original specification?

**Q2.** Is Interpretation B a reasonable reading of the original specification?

**Q3.** Does the original specification leave the choice between A and B unresolved?

**Q4.** If one interpretation is not reasonable, what wording or requirement evidence makes it unreasonable?

Optional confidence:

**Q5.** How confident are you in the judgment?

## 6. Response scale

Use a predefined scale. Recommended primary coding:

- 1 = not reasonable;
- 2 = probably not reasonable;
- 3 = uncertain;
- 4 = probably reasonable;
- 5 = clearly reasonable.

Binary certification coding may then use a preregistered threshold.

## 7. Acceptance threshold

For the foundation protocol, use:

[
	au = 0.80
]

as the planned plausibility threshold for each interpretation, unless a documented protocol amendment changes it before the relevant analysis is frozen.

The threshold should be applied to the predefined aggregation rule, not selected after inspecting model results.

A certified case requires:

[
P_A geq 	au
quadlandquad
P_B geq 	au
]

plus the formal non-equivalence requirement.

## 8. Agreement measurement

For multiple annotators, report an appropriate inter-annotator agreement statistic. Fleiss' kappa is a planned option for categorical ratings when its assumptions fit the annotation design.

Also report:

- number of annotators;
- number of items;
- category counts;
- agreement statistic;
- uncertainty or confidence interval where appropriate.

Do not use agreement alone as evidence that an interpretation is semantically correct.

## 9. Adjudication

If an item fails to meet the threshold or receives substantial disagreement:

1. preserve the original independent annotations;
2. do not overwrite individual judgments;
3. conduct adjudication using a predefined procedure;
4. record the adjudication outcome and rationale;
5. mark the item accordingly.

Adjudication cannot be used retrospectively to force a candidate into the certified set.

## 10. Data handling

Store:

- anonymized annotator ID;
- item ID/version;
- raw response;
- coded response;
- timestamp where useful;
- protocol version;
- adjudication record when applicable.

Do not store unnecessary personal information.

## 11. Certification decision

The final certification function is:

```
Certified Ambiguous =
Formal NON_EQUIVALENT
AND
Interpretation A passes plausibility threshold
AND
Interpretation B passes plausibility threshold
AND
all benchmark validation checks pass
```

If formal evidence is non-equivalent but one interpretation fails plausibility, classify as a negative candidate rather than certified ambiguity.

## 12. Quality checks

Before freezing annotations:

- [ ] annotator eligibility recorded;
- [ ] training/protocol version recorded;
- [ ] original wording preserved;
- [ ] A/B presentation balanced where practical;
- [ ] raw responses preserved;
- [ ] coded responses reproducible;
- [ ] agreement calculated;
- [ ] threshold applied consistently;
- [ ] adjudication documented;
- [ ] no model result exposed during blinded annotation where applicable.
