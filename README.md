# FORMAL-AMBIG-RTL — Audit-Ready Research Repository

FORMAL-AMBIG-RTL is a research repository for evaluating how LLM-generated RTL handles underspecified natural-language hardware requirements using explicit interpretations, behavioral specifications, formal verification, and review-governed evidence.

## Current project position

**P01 professor review: APPROVED, as recorded by the project owner.** This records professor direction to proceed; it does not imply that an independent certification dossier has been signed.

**P02: READY TO BEGIN.**

`P01 requirement → interpretation → specification → RTL → formal evidence: COMPLETE`

`P02 requirement/specification: DRAFT PROPOSED`

`P02 RTL: NOT YET IMPLEMENTED`

`P02 formal verification: NOT YET EXECUTED`

`P02 evidence: NOT YET GENERATED`

## Start here

1. [`Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md`](Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md) — project control.
2. [`Files/FORMAL_AMBIG_RTL_PLAN.md`](Files/FORMAL_AMBIG_RTL_PLAN.md) — scientific plan and phase gates.
3. [`docs/repository-map.md`](docs/repository-map.md) — repository structure and provenance boundaries.
4. [`docs/provenance/p01-evidence-register.md`](docs/provenance/p01-evidence-register.md) — P01 evidence/provenance register.
5. [`docs/reproducibility/p01-reproduction.md`](docs/reproducibility/p01-reproduction.md) — clean-checkout reproduction boundary.
6. [`Files/Research_Papers/benchmark/pilot_v0_1/P01/`](Files/Research_Papers/benchmark/pilot_v0_1/P01/) — P01 source artifacts.
7. [`Files/Research_Papers/benchmark/pilot_v0_1/P02/`](Files/Research_Papers/benchmark/pilot_v0_1/P02/) — P02 working requirement/specification artifacts.

## P01 evidence boundary

The retained P01 formal evidence applies only to the **effective tested source**:

`pinned base revision + retained path-only SBY patch`

Pinned base revision:
`6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`

Patch SHA-256:
`71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`

Accepted P01 archive:
`p01-20260930T220622Z-rev1.tar.gz`

Archive SHA-256:
`32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`

**The accepted archive and checksum are protected and are not modified by P02 work.**

The unmodified pinned revision is not represented as having formally passed.

## Current governance

- Formal evidence: **COMPLETE** for the documented effective tested source.
- Evidence audit/integrity: **COMPLETE**.
- P01 professor/guide direction: **APPROVED TO PROCEED WITH P02**, based on the project owner's recorded statement.
- P01 Golden Template: **NOT FROZEN**.
- P02: **AUTHORIZED TO BEGIN**.
- P02 formal execution: **NOT YET EXECUTED**.
- P02 evidence: **NOT YET GENERATED**.
- Benchmark-wide validity: **NOT CLAIMED**.
- Complete LLM-methodology validation: **NOT CLAIMED**.

Approval metadata not supplied in the current record (exact approval date, approval mode, and exact professor wording) must not be invented.

## Repository conventions

- `Files/Research_Papers/benchmark/` contains benchmark artifacts.
- `Files/Research_Papers/docs/` contains research protocols and schemas.
- `docs/` contains repository-level navigation, provenance, reproducibility, and project-state controls.
- `legacy/` contains retained historical/imported material.
- Accepted evidence is immutable; reruns create new evidence packages rather than replacing old ones.
