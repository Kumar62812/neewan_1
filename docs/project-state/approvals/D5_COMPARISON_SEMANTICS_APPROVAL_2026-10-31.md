# D5 author approval — comparison semantics

- **Project:** FORMAL-AMBIG-RTL
- **Decision:** D5 — A/B/AB/M comparison semantics
- **Disposition:** ACCEPT — Option C (both relations, separately reported)
- **Author:** G. Naveen
- **Date:** 2026-10-31
- **Decision basis:** D5 readiness brief; A3 decision matrix v1.0
- **Amendment:** [AM-007 — Dual comparison relations](../../amendments/AM-007_dual_comparison_relations.md)
- **Decision form:** [A3 author decision form](../A3_AUTHOR_DECISION_FORM.md)

## Author-approved decision

> I approve Option C — Both, separately reported. Behavioral equivalence remains the primary A/B/AB/M classification under frozen PLAN §11 and Research Protocol §7. Contract conformance is added as a distinct secondary result vector and must never overwrite, merge with, or be relabelled as the primary equivalence class.

## Required interpretation

1. **Primary relation — equivalence:** classify generated RTL against reference RTL-A and RTL-B under the same declared legal environment and observable set. Preserve the frozen A/B/AB/M definitions. A formal timeout, tool error, or incomplete check is unresolved/inconclusive, not a proven mismatch or M.
2. **Secondary relation — contract conformance:** independently test the same generated RTL against the separately frozen contracts for interpretations A and B. Report in a separate field using `contracts_A_only`, `contracts_B_only`, `contracts_both`, `contracts_neither`, or `contracts_unresolved`. Never call `contracts_both` equivalence-based `AB`.
3. **Separation:** primary and secondary results require separate fields, evidence, denominators, inclusion/exclusion rules, summary tables and analysis scripts. Neither result may overwrite the other.
4. **P05 pilot:** retain its original contract-conformance outputs as exploratory evidence under the protocol used for that pilot. Do not relabel them as equivalence A/B/AB/M, promote them retrospectively to primary results, or alter their historical evidence.
5. **D4 binding:** D4's `MISINTERPRET` decision must use the approved primary equivalence classification. Secondary contract-conformance outcomes alone cannot trigger `MISINTERPRET`.
6. **Validation gate:** before production scoring, implement regression fixtures for the combined primary/secondary outcomes, verify the two result fields remain independent, test unresolved/tool-failure handling, and retain exact commands, tool versions, logs and hashes.

## Scope and limits

This approval selects the comparison methodology and authorizes AM-007 as the versioned protocol amendment. It does not certify any benchmark case, validate the evaluator implementation, approve model/prompt/trial settings, authorize primary scored experiments, or waive any other Gate 4 decision (including D10 and D13).

**Frozen-evidence instruction:** do not edit or replace the frozen PLAN source, Research Protocol source, prior P05 outputs, RTL, formal evidence, counterexamples, run logs or manifests. The amendment is read alongside the original sources; historical artifacts remain immutable.

**Approval result:** D5 Option C is ACCEPTED by G. Naveen on 2026-10-31. Production integration remains conditional on implementation validation and the remaining Gate 4 approvals.
