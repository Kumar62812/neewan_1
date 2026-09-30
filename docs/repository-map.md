# Repository Map and Curation Policy

## 1. Current remote state inspected

The repository default branch is `main`. The active FORMAL-AMBIG-RTL development branch inspected for this curation is `formal-ambig-rtl-foundation` at commit `4b5288bb75eb8bce58af8ac1038f519306d7cfec`.

The repository currently contains two branches: `main` and `formal-ambig-rtl-foundation`. The two branches have diverged; the foundation branch contains the FORMAL-AMBIG-RTL work while `main` also contains unrelated/imported material.

No tag reference was found through the repository refs endpoint.

## 2. Logical architecture

```text
FORMAL-AMBIG-RTL/
├── README.md                         # 10-minute entry point
├── docs/
│   ├── repository-map.md             # this document
│   ├── provenance/                   # immutable-evidence registers and lineage
│   └── reproducibility/              # clean-checkout reproduction procedures
├── Files/
│   ├── FORMAL_AMBIG_RTL_PLAN.md      # scientific plan
│   ├── FORMAL_AMBIG_RTL_PROJECT_COMPASS.md
│   └── Research_Papers/
│       ├── docs/                     # research protocol/schema documents
│       └── benchmark/
│           └── pilot_v0_1/P01/       # active P01 construction/evidence tree
└── legacy/
    └── imported_root_material/       # retained non-core historical/imported files
```

The current branch still retains the older `Files/Research_Papers` literature-library layout because it is historical research material, not a clean-room benchmark artifact. It should be treated as a literature/archive layer rather than as the benchmark implementation itself.

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
C independent certification decision
```

The certification boundary is explicit: `C` remains pending. Formal evidence and certification are different gates.

## 4. Immutable / protected classes

The following must never be rewritten in place:

- accepted evidence archives;
- raw formal logs and counterexample traces;
- checksum manifests;
- historical audit records;
- retained source snapshots used to establish provenance;
- prior Git commits and tags.

A rerun gets a new run identifier and a new evidence package.

## 5. Historical provenance rule

For P01, the retained evidence record identifies:

- pinned base revision: `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`;
- effective tested source: pinned base revision plus a retained path-only SBY patch;
- patch SHA-256: `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`;
- accepted archive: `p01-20260930T220622Z-rev1.tar.gz`;
- accepted archive SHA-256: `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`.

The current repository checkout still contains the pre-patch SBY path form. Therefore the accepted formal result must not be described as a result of the unmodified checkout. The patch must remain an explicit provenance dependency.

## 6. Legacy material

Files that are clearly imported, duplicated, exploratory, or superseded may be moved into `legacy/` only when doing so does not alter accepted evidence. If an evidence item would become ambiguous after a move, leave it in place and add a pointer/index instead.

No historical material is deleted by this curation.
