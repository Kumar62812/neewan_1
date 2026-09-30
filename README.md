# FORMAL-AMBIG-RTL — Audit-Ready Research Repository

FORMAL-AMBIG-RTL is a research repository for evaluating how LLM-generated RTL handles underspecified natural-language hardware requirements using explicit interpretations, behavioral specifications, formal verification, and independent certification.

## Current gate state

**R ✓ → I ✓ → S ✓ → RTL ✓ → F ✓ → C: PENDING**

P01 certification is **not complete**. This repository does not authorize P02–P12 construction, benchmark scaling, or LLM evaluation before the P01 exit gate is independently satisfied.

## Start here

1. [`Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md`](Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md) — day-to-day project control.
2. [`Files/FORMAL_AMBIG_RTL_PLAN.md`](Files/FORMAL_AMBIG_RTL_PLAN.md) — scientific plan and phase gates.
3. [`docs/repository-map.md`](docs/repository-map.md) — repository structure and provenance boundaries.
4. [`docs/provenance/p01-evidence-register.md`](docs/provenance/p01-evidence-register.md) — P01 evidence/provenance register.
5. [`docs/reproducibility/p01-reproduction.md`](docs/reproducibility/p01-reproduction.md) — clean-checkout reproduction boundary.
6. [`Files/Research_Papers/benchmark/pilot_v0_1/P01/`](Files/Research_Papers/benchmark/pilot_v0_1/P01/) — P01 source artifacts.

## Evidence boundary

The retained formal evidence applies to the **effective tested source**:

`pinned base revision + retained path-only SBY patch`

Pinned base revision:
`6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`

Patch SHA-256:
`71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`

Accepted P01 archive:
`p01-20260930T220622Z-rev1.tar.gz`

Archive SHA-256:
`32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`

The unmodified pinned revision is **not** represented as having formally passed. Historical evidence, checksums, traces, and audit records must not be rewritten.

## Repository conventions

- `Files/Research_Papers/benchmark/` contains benchmark artifacts during the current foundation phase.
- `Files/Research_Papers/docs/` contains research protocols and schemas.
- `docs/` contains repository-level navigation, provenance, and reproducibility controls.
- `legacy/` contains retained historical/imported material that should not be confused with the active evidence chain.
- Accepted evidence is immutable; reruns create new evidence packages rather than replacing old ones.

## What this repository does not claim

It does not claim P01 certification, a frozen P01 golden template, authorization of P02–P12, full benchmark validation, or validation of the complete LLM evaluation methodology.
