# P05 Independent Plausibility Review — v1

**Status:** Preparation only. No reviewer responses have been collected. P05 ambiguity/plausibility is **PENDING**. No ambiguity certification is claimed.

## 1. Purpose

This procedure defines an independent human-plausibility review for the competing interpretations documented for P05. It must be applied to the frozen requirement and interpretation texts. It does not replace formal verification and does not itself establish that the interpretations are behaviorally distinct.

## 2. Review panel and independence

- Obtain ratings from **five independent reviewers**.
- Reviewers should not coordinate their ratings before submission.
- Each reviewer completes a separate form.
- Do not expose earlier reviewers' answers before a reviewer has submitted their own rating.
- Record reviewer identifiers using neutral codes (R1–R5) in the analysis dataset. Keep names/contact details separately, with restricted access if collected.
- Record conflicts of interest and any prior participation in drafting the case. A reviewer who materially drafted the requirement or interpretations should not count as an independent reviewer for the primary threshold.

## 3. Materials and blinding

Give each reviewer the exact natural-language requirement and the candidate interpretations being assessed, with enough context to understand their wording. Do not show the intended certification outcome, other reviewers' ratings, model output, formal results, or the researcher's preferred interpretation before the independent ratings are locked.

The review package must identify the version/hash of each presented item. Any wording change after review begins creates a new review version and must be documented; do not silently combine ratings across versions.

## 4. Per-interpretation rating form

For each candidate interpretation, independently record:

1. **Plausibility rating (1–5):**
   - 1 — Not a reasonable reading of the requirement.
   - 2 — Weak reading; requires an assumption poorly supported by the text.
   - 3 — Arguably reasonable, but substantial interpretive assumptions are needed.
   - 4 — Reasonable reading supported by the wording and ordinary hardware-design context.
   - 5 — Very natural reading directly supported by the requirement.
2. **Textual support:** identify the exact phrase(s) supporting or conflicting with the interpretation.
3. **Assumptions introduced:** list any assumptions that the requirement does not state.
4. **Confidence (1–5):** 1 = very low, 5 = very high.
5. **Free-text rationale:** explain the rating briefly.
6. **Prior involvement/conflict:** none / describe.

Reviewers rate each interpretation separately before answering the pair-level questions.

## 5. Pair-level review form

For the interpretation pair, each reviewer records:

- Are both interpretations independently defensible from the requirement? yes / no / uncertain.
- Does the pair reflect a real ambiguity in the language/requirements, rather than an arbitrary alternative? yes / no / uncertain.
- What exact wording allows the competing readings?
- What clarification would resolve the difference?
- Optional comments on whether the interpretations overlap or rely on incompatible unstated assumptions.

Formal non-equivalence is assessed separately. Reviewers must not infer non-equivalence from prose alone.

## 6. Predefined decision thresholds

Use these thresholds as an operational review rule, not as a claim that they are universal or externally validated:

- An interpretation is **human-plausible** when at least **4 of 5** independent reviewers rate it **4 or 5**.
- The pair passes the primary **plausibility gate** only when **both interpretations** meet that per-interpretation threshold and at least 4 of 5 reviewers answer “yes” to the pair-level question that both are defensible.
- A pair is a candidate for **certified ambiguity** only when the human-plausibility gate passes, the interpretations specify observably different behavior, formal analysis confirms the behavioral difference under the stated scope, and the required independent decision is recorded.
- If the threshold is not met, or reviewer judgments expose missing context, classify the case **UNRESOLVED** and revise only through a versioned change process. Do not lower thresholds after seeing the ratings.
- “Uncertain” responses do not count as “yes” for the primary threshold. Preserve raw responses so sensitivity analysis can be reported.

## 7. Disagreement handling

1. Freeze and export the five individual forms before discussion.
2. Report each reviewer’s score, the distribution, and the number passing the predefined threshold. Do not report only an average.
3. Do not replace individual judgments with a consensus score.
4. If the pair-level threshold passes but a substantive minority raises a concrete textual objection, record the objection and conduct a documented adjudication. Adjudication may change the case status only through the project's decision log and must not erase original ratings.
5. If the threshold fails, reviewers may discuss what clarification is needed, but the existing version remains unresolved. A revised requirement/interpretation receives a new version identifier and a fresh independent rating round.
6. Report inter-reviewer agreement descriptively; if a statistic is calculated, specify the measure and its assumptions. Do not present five reviewers as a large or representative population.

## 8. Evidence to retain

Retain, at minimum:

- requirement and interpretation version identifiers and SHA-256 hashes;
- the blank form and review instructions supplied to reviewers;
- five independently submitted forms with submission timestamps;
- the analysis script or calculation sheet;
- threshold calculation and decision rationale;
- all adjudication notes and version changes;
- reviewer-independence/conflict declarations;
- the commit SHA that freezes the review materials and the commit SHA that records the completed analysis.

Redact personal information in the public repository unless reviewers have explicitly consented to publication. Public artifacts should normally contain anonymized response codes and ratings.

## 9. Current P05 state

- Review procedure: **PREPARED**
- Reviewer responses: **0 of 5**
- Plausibility gate: **PENDING**
- Formal behavioral distinction for P05: **not established by this procedure**
- Ambiguity certification: **NOT CLAIMED**
- Any LLM evaluation based on a certified P05 gold standard: **NOT AUTHORIZED until the case gates are satisfied**

This file defines the preparation workflow. It does not assert that reviewers have been recruited or that any review has occurred.
