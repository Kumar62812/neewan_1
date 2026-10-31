# D15 author acknowledgement — experimental observation unit

- **Project:** FORMAL-AMBIG-RTL
- **Decision:** D15 — Observation unit
- **Disposition:** ACKNOWLEDGE
- **Author:** G. Naveen
- **Date:** 2026-10-31
- **Decision type:** Documentation clarification only; no protocol amendment required
- **Source:** [A2 Research Scope Freeze v1.0](../A2_RESEARCH_SCOPE_FREEZE_v1.0.md), §8; [Research Protocol](../../Files/Research_Papers/docs/research_protocol.md), §11; [A3 decision matrix](../A3_PROTOCOL_DECISION_MATRIX_v1.0.md), D15

## Author acknowledgement

> For D15, my author disposition is ACKNOWLEDGE. Author: G. Naveen.

The author acknowledges the existing observation-unit definition:

**(Model, Benchmark Instance, Condition, Trial).**

## Operational interpretation

1. Each observation is one model's attempt on one benchmark instance under one experimental condition in one trial.
2. Model identity and version, benchmark-instance identity, condition, and trial identifier remain separately recorded.
3. Repeated trials remain distinct observations and retain their trial identifiers and generation settings.
4. Single-shot and interactive conditions remain distinguishable.
5. Technical failures, incomplete responses, and inconclusive formal outcomes retain their appropriate status; they are not silently dropped or recoded as behavioral match classes.
6. Aggregated model- or condition-level summaries must be derived from the underlying observation records and must not replace them.

## Scope and limits

This acknowledgement accepts the existing unit; it does not define new metric denominators, trial counts, statistical procedures, missing-data rules beyond the existing protocol, or authorize scored experiments. Any such operational choices remain subject to their respective protocol decisions and freezes.

No amendment is required because this is an acknowledgement of existing A2/RP wording, not a substantive protocol change.

## Evidence preservation

The frozen PLAN, Research Protocol, A2 source, benchmark case artifacts, RTL, formal evidence, counterexamples, historical logs, run manifests, and P05 pilot artifacts are not modified by this acknowledgement.

## Verification

- Confirmed the observation-unit statement in A2 §8.
- Confirmed the matching definition in Research Protocol §11.
- Confirmed the D15 entry in the A3 clarification register.
- Confirmed the frozen PLAN and Research Protocol source files remain unchanged at their previously recorded Git blob SHAs.
- Confirmed the D15 author disposition is recorded in the A3 author decision form and decision matrix.

**Result:** D15 is ACKNOWLEDGED by G. Naveen on 2026-10-31. No amendment, implementation change, experiment, or certification is authorized or claimed by this record.
