# Repository Map and Curation Policy

## 1. Current remote state — checked 2026-10-30

- Default branch `main` is at `83046997dce165fd3b40c190f7dffa1e280b2c86`.
- The existing `research/end-to-end-sequence` workstream is at `526354123fe9b5c7f08af098a885b39bcce828e1`, is 138 commits ahead of `main`, and has no associated PR. Its decision registers and task crosswalk are linked from the [2026-10-30 status tracker](project-state/TASK6_TASK7_STATUS_2026-10-30.md).
- The live A3 author form records D3 as accepted for its named implementation. Other A3 decisions remain pending and the A3 approval block is blank; see the [current A3 form](https://github.com/Kumar62812/neewan_1/blob/research/end-to-end-sequence/docs/project-state/A3_AUTHOR_DECISION_FORM.md).
- GitHub search showed PRs #7, #8, and #9 open. PR #9 contains a three-sample P05 exploratory pilot; it does not establish human plausibility or ambiguity certification.
- This focused status update is prepared on `docs/task6-task7-status-20261030` from the live `main` commit, so it can be reviewed without folding the full 138-commit workstream into the same change.

The earlier P01 foundation synchronization was merged through PR #2. That historical merge record remains below as provenance; it is not the current project phase.

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

## 6. Historical P02 boundary at an earlier synchronization

This block is retained from an earlier synchronization and is not the current P02 status. Use the [current status tracker](project-state/TASK6_TASK7_STATUS_2026-10-30.md) and the linked project-sequence crosswalk for navigation. The frozen scientific plan and accepted evidence remain unchanged.

P02 was authorized to begin at the requirement → interpretation → specification stage at that earlier synchronization.

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
