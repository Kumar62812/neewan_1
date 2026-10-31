# T08 — Canonical case metadata and layout contract (v2.0)

**State:** implementation candidate; not frozen  
**Authority:** D1/AM-001, D2/AM-002, D9/AM-003, D14/AM-004  
**Scope:** newly created benchmark cases only

## 1. Canonical layout

```
CASE_ID/
├── metadata.json
├── requirement/
│   └── requirement.md
├── interpretations/
│   ├── interpretation_A.md
│   └── interpretation_B.md        # ambiguity candidates only
├── behavioral_specification/
│   ├── specification_A.md
│   └── specification_B.md         # ambiguity candidates only
├── reference_rtl/
│   ├── A/
│   │   └── rtl.sv
│   └── B/
│       └── rtl.sv                 # ambiguity candidates only
├── formal/
│   ├── properties/
│   ├── harnesses/
│   └── scripts/
├── annotations/
├── provenance/
│   └── source_manifest.json
└── evidence/
    └── run-NN/                    # immutable after a run is sealed
```

The physical tree is the new-case target. The P01/P02/P05 path crosswalk is descriptive and read-only; it does not move or normalize historical files.

## 2. Metadata semantics

- `primary_category`: exactly one C1–C5 taxonomy category.
- `thematic_tags`: zero or more optional tags: reset, output, transition, timing, state, concurrency. They never replace or override the primary category.
- `certification_status`: exactly PLAN §6 vocabulary: UNAMBIGUOUS, CERTIFIED_AMBIGUOUS, UNRESOLVED, EXCLUDED.
- `lifecycle_stage`: exactly candidate, certified_ambiguous, unambiguous_control, negative_candidate, inconclusive.
- `release_frozen`: Boolean release state, independent of the above.
- `case_role`: structural role for conditional artifact requirements; it is not a scientific classification.
- `formal_evidence` and `annotations`: separate evidence vectors. Formal distinction does not prove linguistic plausibility.
- `provenance` and `reproducibility`: record source identity, commit and hashes without replacing source artifacts.

### Role conditions

| case_role | Required structure | Prohibited inference |
|---|---|---|
| unambiguous_control | C1; A interpretation and A RTL; B absent | A checker-negative control is not interpretation B |
| ambiguity_candidate | C2–C5; A/B interpretations and A/B reference RTL | Structural completeness does not certify plausibility or ambiguity |
| negative_candidate | explicit negative-candidate lifecycle; exclusion reason required if status is EXCLUDED | A placeholder rejection record is not an adjudication |
| robustness_case | explicit robustness role; checker-negative implementation is separate from interpretation fields | A wrong checker implementation is not interpretation B |

The role field is a structural discriminator only. It does not set the certification status automatically.

### Status crosswalk

| lifecycle_stage | default certification_status |
|---|---|
| candidate | UNRESOLVED |
| certified_ambiguous | CERTIFIED_AMBIGUOUS |
| unambiguous_control | UNAMBIGUOUS |
| negative_candidate | EXCLUDED only with an explicit decision and PLAN §6 reason; otherwise UNRESOLVED |
| inconclusive | UNRESOLVED |

An inconclusive record may become EXCLUDED only through an explicit decision with a specific PLAN §6 exclusion reason. Timeout, tool error, incomplete checks, or missing evidence alone never silently imply EXCLUDED.

## 3. Artifact path and evidence rules

- Metadata artifact paths are case-relative POSIX paths; absolute paths, parent traversal (`..`), and network paths are invalid.
- Every source file consumed by a run must be hash-pinned in the run manifest.
- Runs are created under `evidence/run-NN/` with `--new-run`; each run receives a manifest containing the metadata SHA-256 and creation identity. A pre-existing run directory is never overwritten. The runner does not make filesystems cryptographically immutable; the policy is append-only, and repository permissions/review protect committed evidence.
- A sealed run is immutable. Corrections create a new run number and retain the old run.
- Hashes are lowercase SHA-256 hex strings.
- Missing historical artifacts are recorded as absent in the crosswalk, never fabricated.

## 4. Versioning and compatibility

Schema and template are versioned independently of the frozen v1.0 YAML template. New cases use metadata schema 2.0. Existing P01/P02/P05 remain at their original paths and formats. No automatic migration is implemented or authorized.

## 5. Validation command

From repository root:

```bash
python Files/Research_Papers/benchmark/tools/validate_case.py --metadata PATH/metadata.json
python Files/Research_Papers/benchmark/tools/validate_case.py --init CASE_ID --role ambiguity_candidate --category C2 --root /tmp/t08-smoke\npython Files/Research_Papers/benchmark/tools/validate_case.py --new-run /tmp/t08-smoke/CASE_ID
```

The validator is intentionally standard-library-only. It checks required keys, types, enumerations, role-dependent artifacts, lifecycle/status consistency, safe relative paths, and source hash syntax. It does not certify plausibility, run formal tools, or adjudicate cases.

## 6. Freeze gate

This implementation candidate is not a frozen golden template. Freeze requires:
1. clean-case generation;
2. positive and negative validator tests;
3. role-aware fixture tests;
4. read-only P01/P02/P05 crosswalk verification;
5. immutable run-directory tests;
6. integrated CI passing after the approved D1/D2/D9/D14 decisions;
7. exact hashes and versions recorded in a separate author freeze decision.

No scored LLM experiments or human reviews are part of T08.
