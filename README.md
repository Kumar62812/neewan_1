# FORMAL-AMBIG-RTL — Audit-Ready Research Repository

FORMAL-AMBIG-RTL is a research repository for evaluating how LLM-generated RTL handles underspecified natural-language hardware requirements using explicit interpretations, behavioral specifications, formal verification, and review-governed evidence.

## Current project position

**P01: Formal evidence complete; professor-approved.** Professor approval is recorded as project direction to proceed with P02; it does not imply completion of an independent certification record.

**P02: Requirement, interpretation, and specification prepared; pre-RTL consistency review pending.**

`P01: Formal evidence COMPLETE`

`P02: Requirement PRESENT → Interpretation PRESENT → Specification PRESENT → Consistency review PENDING → RTL NOT IMPLEMENTED → Formal verification NOT EXECUTED → Evidence NOT GENERATED`

## Start here

1. [`Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md`](Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md) — project control.
2. [`Files/FORMAL_AMBIG_RTL_PLAN.md`](Files/FORMAL_AMBIG_RTL_PLAN.md) — scientific plan and phase gates.
3. [`docs/repository-map.md`](docs/repository-map.md) — repository structure and provenance boundaries.
4. [`docs/provenance/p01-evidence-register.md`](docs/provenance/p01-evidence-register.md) — P01 evidence/provenance register.
5. [`docs/reproducibility/p01-reproduction.md`](docs/reproducibility/p01-reproduction.md) — clean-checkout reproduction boundary.
6. [`Files/Research_Papers/benchmark/pilot_v0_1/P01/`](Files/Research_Papers/benchmark/pilot_v0_1/P01/) — P01 source artifacts.
7. [`Files/Research_Papers/benchmark/pilot_v0_1/P02/`](Files/Research_Papers/benchmark/pilot_v0_1/P02/) — P02 requirement, interpretation, and specification artifacts.

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

**The accepted archive and checksum are protected and are not modified by P02 documentation work.**

The unmodified pinned revision is not represented as having formally passed.

## Current governance

- Formal evidence: **COMPLETE** for the documented effective tested source.
- Evidence audit/integrity: **COMPLETE**.
- P01 professor approval: **APPROVED** — see `02_CERTIFICATION/P01_GUIDE_MEETING_RECORD.md`.
- Independent certification record: **not completed/recorded in the current project record**.
- P01 Golden Template: **NOT FROZEN**.
- P02 requirement, interpretation, specification: **PRESENT; consistency review pending**.
- P02 RTL: **NOT IMPLEMENTED**.
- P02 formal verification: **NOT EXECUTED**.
- P02 evidence: **NOT GENERATED**.
- Benchmark-wide validity: **NOT CLAIMED**.
- Complete LLM-methodology validation: **NOT CLAIMED**.

Approval date, mode, and exact professor wording are not stated because they were not supplied in the project record.

## Repository conventions

- `Files/Research_Papers/benchmark/` contains benchmark artifacts.
- `Files/Research_Papers/docs/` contains research protocols and schemas.
- `docs/` contains repository-level navigation, provenance, reproducibility, and project-state controls.
- `legacy/` contains retained historical/imported material.
- Accepted evidence is immutable; reruns create new evidence packages rather than replacing old ones.
