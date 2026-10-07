# Repository Map and Curation Policy

## 1. Current remote state

The repository default branch is `main`.

The FORMAL-AMBIG-RTL foundation work from `formal-ambig-rtl-foundation` has now been merged into `main` through PR #2:

- PR: #2
- Merge commit: `4af94063d69c48ef616727853b99187fe468a0dc`
- Purpose: synchronize the audited P01 foundation and curation layer into `main`.

The current working synchronization branch is `sync/current-project-state-p02`.

## 2. Logical architecture

```text
FORMAL-AMBIG-RTL/
├── README.md
├── docs/
│   ├── repository-map.md
│   ├── provenance/
│   ├── reproducibility/
│   └── project-state/
├── Files/
│   ├── FORMAL_AMBIG_RTL_PLAN.md
│   ├── FORMAL_AMBIG_RTL_PROJECT_COMPASS.md
│   └── Research_Papers/
│       ├── docs/
│       └── benchmark/
│           ├── pilot_v0_1/P01/
│           └── pilot_v0_1/P02/
├── 02_CERTIFICATION/
├── 03_NOTEBOOKS/
└── 06_HISTORICAL/
```

## 3. P01 evidence chain

```text
R requirement
  ↓
I interpretation
  ↓
S behavioral specification
  ↓
RTL reference + negative control
  ↓
F formal evidence
  ↓
C independent certification/review decision
```

P01 formal evidence is complete for its documented effective tested source. The independent certification dossier decision remains a separate matter and is not fabricated by this repository update.

## 4. Protected evidence

The accepted P01 archive and checksum are immutable:

```text
re/p01-20260930T220622Z-rev1.tar.gz
re/p01-20260930T220622Z-rev1.tar.gz.sha256
```

SHA-256:

```text
32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b
```

Do not rewrite, replace, recompress, rename, or regenerate the accepted archive as part of P02 work.

## 5. P01 provenance

- Pinned base revision: `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`
- Effective tested source: pinned base + retained path-only SBY patch
- Patch SHA-256: `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`
- Accepted archive SHA-256: `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`

The unmodified pinned revision is not claimed to have passed.

## 6. P02 boundary

P02 is authorized to begin at the requirement → interpretation → specification stage.

At this synchronization point:

```text
P02 requirement       DRAFT PROPOSED
P02 interpretation    DRAFT PROPOSED
P02 specification     DRAFT PROPOSED
P02 reference RTL     NOT IMPLEMENTED
P02 negative control  NOT IMPLEMENTED
P02 formal properties NOT IMPLEMENTED
P02 harness           NOT IMPLEMENTED
P02 formal execution  NOT EXECUTED
P02 evidence          NOT GENERATED
```

Each later state must be recorded only after the corresponding artifact or execution actually exists.
