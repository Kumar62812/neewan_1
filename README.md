# FORMAL-AMBIG-RTL

Research on whether LLM-generated RTL violates a requirement, implements a defensible reading of an underspecified requirement, or remains unclassifiable. The evidence chain is **requirement → interpretation → behavioral specification → RTL → formal evidence → certification**.

## Start here

1. [Phase workboard](docs/project-state/PHASE_WORKBOARD.md) — current evidence, ordered next actions and phase exits.
2. [Project compass](Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md) — operating rules and original case order.
3. [Frozen scientific plan](Files/FORMAL_AMBIG_RTL_PLAN.md) — methodology and gates; not a live progress checklist.
4. [Repository map](docs/repository-map.md) — artifacts grouped by purpose and phase.
5. [Repository audit](docs/audits/2026-10-16-repository-audit.md) — integrity checks, inconsistencies and required follow-up.

## Current evidence position

Status reconciled on 2026-10-16 against main `83046997dce165fd3b40c190f7dffa1e280b2c86`.

| Area | Published evidence | Remaining limitation |
|---|---|---|
| P01 | Formal evidence complete for the documented effective tested source; professor direction to proceed with P02 recorded | Independent certification record incomplete; Golden Template not frozen |
| P02 | RTL, properties, harness, positive checks, eight covers and two negative-control failures published through merged PR #6 | Results are scoped to the Boolean sampled-edge model; public clean reproduction reference needs repair |
| P05 | A/B conformance and a legal post-reset distinguishing trace published through merged PR #6 | Zero human responses recorded; plausibility pending; ambiguity certification not claimed |
| LLM evaluation | [PR #7](https://github.com/Kumar62812/neewan_1/pull/7) contains draft infrastructure | Not merged; no model-performance result established; scientific and runner gates remain |

**Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.**

The immediate focus is P01 gate closure and reconciliation of existing P02/P05 work with the original phase rules. Technical progress does not imply that every earlier gate passed. Follow the [ordered work queue](docs/project-state/PHASE_WORKBOARD.md#ordered-work-queue).

## Evidence entry points

- [P01 evidence register](docs/provenance/p01-evidence-register.md) and [reproduction boundary](docs/reproducibility/p01-reproduction.md).
- [P02 readiness](docs/project-state/P02_READINESS.md) and [results](Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_RESULTS.md).
- [P05 plausibility status](docs/project-state/P05_PLAUSIBILITY_STATUS.md), [formal results](Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md), and [review procedure](Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/README.md).
- [P02/P05 reproduction record](docs/reproducibility/p02-p05-reproduction.md).
- [Project history](governance/07_PROJECT_LOG.md) and [thesis assessment plan](docs/project-state/THESIS_ASSESSMENT_PLAN.md).

## P01 preservation boundary

Accepted archive: `re/p01-20260930T220622Z-rev1.tar.gz`.

SHA-256: `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`.

The formal result applies to pinned revision `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35` plus the retained path-only SBY patch, SHA-256 `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`. The unmodified pinned revision is not claimed to have passed.

Evidence and accepted archives are immutable. Reruns create new packages. This navigation update changes no frozen scientific rules, benchmark sources, evidence files or archive paths. Benchmark-wide validity and complete LLM-methodology validation are not claimed.
