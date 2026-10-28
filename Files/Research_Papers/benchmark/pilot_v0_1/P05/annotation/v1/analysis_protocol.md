# P05 Plausibility Analysis Protocol — v1

This protocol is to be used only after the five independent reviewer forms are received and locked.

## Inputs

- Five independent forms, coded R1–R5.
- A frozen requirement and two frozen candidate interpretations.
- Exact file hashes/version identifiers.
- Conflict-of-interest eligibility notes.

Do not begin scoring until the input set is complete or explicitly document an incomplete-round decision.

## Primary calculation

For each interpretation separately, count eligible reviewers who assigned a plausibility rating of 4 or 5.

`pass_A = count(A_rating >= 4)`  
`pass_B = count(B_rating >= 4)`

An interpretation passes at `count >= 4` of five eligible independent reviewers.

The pair-level primary gate passes only if:
1. `pass_A >= 4`;
2. `pass_B >= 4`; and
3. at least four of five reviewers answer “yes” to “Are both interpretations independently defensible?”

“Uncertain” and “no” do not count as “yes” for the primary gate. If a reviewer is ineligible due to material drafting involvement or a declared conflict, do not silently replace that reviewer with a post-hoc-selected person; document the exclusion, recruit a replacement under the same eligibility rule, and record both the original and replacement status.

## Required reporting

Report, without names:

- raw 1–5 score for each interpretation by reviewer code;
- frequency distribution across scores 1–5 for each interpretation;
- median and range as descriptive summaries;
- number of eligible reviewers and count passing threshold for each interpretation;
- pair-level yes/no/uncertain distribution;
- substantive reasons and exact requirement phrases cited;
- conflicts/exclusions/replacements and adjudication;
- final gate: PASS / FAIL / INCOMPLETE;
- whether formal behavioral distinction was separately established;
- case status and decision-record reference.

Do not substitute means or consensus for the predeclared threshold. Do not infer generalizability from five reviewers. Any exploratory sensitivity analysis must be labeled post hoc.

## Disagreement rules

- Preserve all original submissions.
- If one or both interpretations fail the threshold, or pair-level judgment fails, keep P05 **UNRESOLVED**.
- If threshold passes but reviewers flag a material unaddressed reading or hidden assumption, record it and obtain a documented adjudication before any certification decision.
- Any text change invalidates the current-round result for the changed item; assign a new version/hash and re-run review for the new version.
- Do not change thresholds after viewing the results.

## Current state

No human forms have been received in the current record. The calculation must not be run on blank forms or researcher-written examples. Human responses remain **0** until genuine independent submissions arrive.
