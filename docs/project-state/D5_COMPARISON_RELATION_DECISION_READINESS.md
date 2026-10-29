# D5 — A/B/AB/M Comparison Relation: Decision-Readiness Brief

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Status:** TECHNICAL OPTIONS ANALYSED — AUTHOR DISPOSITION PENDING  
**Decision source:** [A3 Protocol Conflict Decision Matrix](A3_PROTOCOL_DECISION_MATRIX_v1.0.md), D5  
**Related implementation:** [D4 MISINTERPRET policy](D4_MISINTERPRET_POLICY.md)  
**Pilot source:** [P05 Groq pilot, PR #9](https://github.com/Kumar62812/neewan_1/pull/9)

## 1. Decision required

D5 determines what it means for generated RTL to correspond to interpretation A, interpretation B, both, or neither. The frozen plan §11 defines the generated-design classes using behavioral equivalence to reference RTL-A and RTL-B. The research protocol §7 repeats that relation but also explains `AB` as compatible with both references when they differ only outside the observable domain. That creates a logical tension: if A and B are non-equivalent on the very same declared observables—as a certified ambiguity pair requires—then one candidate cannot be equivalent to both.

The public P05 Groq pilot uses a different relation: conformance against per-interpretation assertion contracts, not equivalence to the reference RTL. Its result counts are therefore evidence about contract conformance, not an automatic implementation of the frozen A/B/AB/M definition.

## 2. Source-grounded facts

1. **Frozen plan §11:** `A` means the generated RTL is equivalent to RTL-A; `B` means equivalent to RTL-B; `AB` means equivalent to both; `M` means neither.
2. **Frozen plan §11 technical-failure boundary:** `INVALID`, `INCOMPLETE`, and `INCONCLUSIVE` must remain separate from `M`; a syntax error, missing response, or inconclusive formal check is not a misinterpretation.
3. **Research protocol §7:** defines the same equivalence-based classes and retains `AB` on the stated observable-domain rationale.
4. **P05 pilot PR #9:** the retained outputs were checked against `I1_contract.sv` and `I2_contract.sv`. The published paired rows are 2 `I1_only`, 1 `I2_only`, 0 `both`, and 0 `neither`. These are three descriptive samples from one constructed case, expressly not a general model-accuracy or certified-ambiguity result. They must not be silently renamed as frozen-plan A/B/AB/M results.
5. **D4 implementation:** the D4 helper is intentionally relation-agnostic. It requires a separately supplied behavioral class M and an explicitly approved comparison-contract reference. It does not decide D5 or generate A/B/AB/M.

## 3. Options

| Option | Primary rule | Benefits | Costs / constraints |
|---|---|---|---|
| **A — Equivalence only** | Preserve the frozen plan exactly; compare generated RTL with each reference under the same legal environment and observables. | Maximum fidelity to the already-frozen protocol; simplest primary analysis; no AM-007 needed according to A3. | For a certified pair whose references are non-equivalent on the declared observables, `AB` is structurally unreachable. Report this explicitly rather than implying that all four outcomes are attainable. The contract-conformance outputs from PR #9 remain a separate exploratory result. |
| **B — Contract conformance only** | Define A/B by satisfying each interpretation's explicit behavioral property set; AB means satisfying both contracts; M means satisfying neither. | Aligns the label with specified behaviors and the relation used by the P05 pilot. Can classify implementations that satisfy an interpretation without being bit-for-bit behaviorally equivalent to one canonical reference. | Changes the frozen PLAN/RP relation; requires AM-007 and predeclared contract construction, tightness and overlap rules. Existing pilot results cannot be promoted retroactively to primary results just because they used this relation. |
| **C — Both, separately reported** | Keep equivalence as the **primary** A/B/AB/M classification; add a separate, secondary contract-conformance result vector. Do not merge the two relations into one label. | Preserves compatibility with the frozen plan and adds a semantically useful compatibility check. Makes it possible to expose differences between exact reference matching and property-level conformance. | Requires AM-007 to name both relations, the secondary result vocabulary, reporting/denominator rules, and which results may be primary vs secondary/exploratory. Equivalence-based AB remains structurally unreachable for genuinely non-equivalent references; the secondary “both contracts satisfied” result must not be renamed `AB`. |

## 4. Technical recommendation (not an author decision)

**Recommend Option C** if the research goal includes both exact reference-behavior comparison and checking whether generated designs satisfy each interpretation's property contract. Keep equivalence as the primary relation because it is the relation already frozen in PLAN §11 and RP §7. Report contract conformance as a distinct secondary outcome, with separate names, counts, denominators and scripts.

This avoids two errors: silently replacing the frozen relation with the one used in the later pilot, and discarding potentially useful contract-conformance evidence. If minimizing protocol change is more important than the secondary compatibility analysis, Option A is the defensible low-change alternative. Option B should be selected only through an explicit versioned amendment accepting that the primary estimand and label semantics have changed.

This recommendation is a technical assessment only. **D5 remains PENDING_AUTHOR_DECISION.**

## 5. Required rules regardless of option

- Define the comparison relation against a single declared legal environment and observable set for each case/version.
- Preserve formal outcomes separately: a counterexample can establish non-equivalence; timeout/tool error is inconclusive, not a mismatch.
- Never infer linguistic plausibility or certified ambiguity from behavioral difference alone.
- Preserve the same generated RTL, reference RTL, assumptions, and source hashes across all comparisons for a run.
- Record the exact relation, formal tool, command, timeout/resource policy, evidence paths, and version in the run manifest.
- Do not combine equivalence and contract-conformance results into one A/B/AB/M field.
- Do not silently reinterpret the PR #9 pilot or recalculate its counts as primary results. Any later use must follow D10's exploratory-labeling rule and an explicit approved protocol.

## 6. Option-specific acceptance criteria

### If Option A is chosen

1. Positive/negative equivalence tests establish the generated design's relation to RTL-A and RTL-B.
2. Certified pairs have a pinned non-equivalence witness on declared observables.
3. The report explains that equivalence-based `AB` is unreachable on certified pairs with non-equivalent references.
4. D4 receives the frozen-plan comparison record as the approved contract/relation reference.
5. The PR #9 contract-conformance figures remain separately labelled and are not used as equivalence-class evidence.

### If Option B is chosen

1. AM-007 versions PLAN §11 and RP §7 before primary scored results are produced.
2. Each interpretation has a frozen, reviewed behavioral contract with exact assumptions and observables.
3. Contract tightness is checked: each reference satisfies its own contract and fails the other where a disjoint interpretation is required.
4. The policy defines `both`, `neither`, and `unresolved` outcomes, including timeouts and tool errors.
5. The prior P05 pilot remains marked exploratory; no post-hoc promotion into primary metrics.

### If Option C is chosen

1. AM-007 freezes equivalence as primary and contract conformance as a separately named secondary relation.
2. Regression fixtures cover all combinations between the two relation types; separate output fields are mandatory.
3. The primary class cannot be overwritten by the secondary conformance result.
4. The report marks equivalence-based `AB` as structurally unavailable for certified non-equivalent references and uses a different name such as `contracts_both` for secondary conformance.
5. Primary and secondary metrics are tabulated separately with their denominators, inclusion rules, exclusions and analysis status.

## 7. Author decision record

No option is approved by this report. Record the chosen disposition in [A3 author decision form](A3_AUTHOR_DECISION_FORM.md), then approve AM-007 if Option B or C is selected. The amendment must name affected protocol sections, affected instances and artifacts, treatment of the already-observed P05 pilot, whether any historical results are rerun, and which analyses are primary, secondary, or exploratory.

**Gate consequence:** D5 must be settled before the evaluator can safely bind the D4 policy helper to the production comparison relation or before Gate 4 primary scoring. This report does not unblock those gates.
