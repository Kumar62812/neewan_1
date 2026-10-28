# AM-004 — Canonical layout for new benchmark cases

| Field | Value |
|---|---|
| Amendment ID | AM-004 |
| Resolves decision | D14 |
| Source documents amended | `Files/FORMAL_AMBIG_RTL_PLAN.md`; `Files/Research_Papers/docs/benchmark_schema.md` |
| Section(s) | Plan §10; benchmark schema §2 |
| Source SHA-256 before amendment | PLAN: `19e1fe9abc5b8e07d96a3df339d2a020eae93fee7c9b3815a30dd49d112ee305`; BS: `18b5e39599b519872a427c8463213f35bce0cf175e9d553bce3035028493fcac` (transcribed from A3 §3; not independently recomputed in this draft) |
| Date drafted | 2026-10-29 |
| Drafted before or after viewing any model outcome? | AFTER — P05 exploratory pilot results were already visible |
| Status | DRAFT — NOT EFFECTIVE |

## 1. Text being amended

The frozen plan §10 specifies `requirement.md`, `metadata.yaml`, `interpretations/`, `behavioral_specification/`, `reference_rtl/`, `formal/`, `annotations/`, and `review/`.

Benchmark schema §2 describes `specifications/`, `interpretations/`, `reference_rtl/A` and `reference_rtl/B`, `formal/`, `annotations/`, `controls/`, `negative_candidates/`, and a dataset file. It permits the logical structure to remain under `Research_Papers` during the foundation stage.

Existing P02/P05 records use JSON metadata, case-specific documents and immutable `evidence/run-NN/` directories. A3 recommends one canonical layout for new cases, based on the JSON/run-evidence pattern, with a crosswalk for P01/P02/P05.

## 2. Amended rule (proposed)

T08 shall finalize one canonical layout for newly created cases. The following is the proposed starting point, not a frozen template:

```text
Pxx/
├── requirement.md
├── metadata.json
├── interpretations/
├── behavioral_specification/
├── reference_rtl/
│   ├── A/
│   └── B/
├── formal/
│   ├── properties/
│   ├── harness/
│   └── scripts/
├── evidence/
│   └── run-NN/
├── annotations/
└── review/
```

C1 controls may use one intended interpretation and one reference design. Ambiguous candidates require paired interpretations, behavioral specifications and reference designs under the applicable protocol. Logs, tool/version records, manifests, witnesses and counterexamples must be retained in the declared immutable run-evidence package or linked from it through a verifiable manifest.

The T08 template shall create the layout, validate metadata, and separate versioned source artifacts from run outputs. Published run directories must not be overwritten; a rerun or correction receives a new run identifier.

A path crosswalk must map each expected plan/schema artifact for P01/P02/P05 to an existing path or explicitly mark it absent. The crosswalk is descriptive; it does not migrate, rename, overwrite or back-fill existing cases.

## 3. Reason

The plan and schema describe related artifacts using different layouts. P02/P05 provide an existing JSON-metadata and per-run evidence pattern. A single validated layout for future cases reduces runner complexity while preserving existing provenance.

## 4. Scope and effect

| Question | Answer |
|---|---|
| Affected instances | New cases created after T08 template approval |
| Affected artifacts | Plan §10 and benchmark schema §2 via this separate amendment; T08 template, schema, runner and path crosswalk |
| Are earlier results rerun? | No rerun solely because of layout standardization; other approved changes may require separate assessment |
| Effect on earlier results | Existing evidence remains tied to original paths, versions and manifests |
| Existing records rewritten? | NO |

This draft does not authorize T08 or freeze the template. The layout becomes operative only after D14 is approved and recorded and T08's own validation/exit conditions are met.

## 5. Validation

1. Create a disposable case from the T08 template and verify its structure.
2. Validate required metadata and permitted field values.
3. Confirm the runner locates specifications, reference RTL, properties, harness/scripts and evidence directories.
4. Confirm run evidence is immutable and reruns receive new identifiers.
5. Produce the P01/P02/P05 path crosswalk, marking absent artifacts rather than inventing paths.
6. Verify existing case files, logs, witnesses and manifests are unchanged.

## 6. Approval

| Field | Value |
|---|---|
| Disposition | PENDING |
| Approved by | |
| Date | |
| Approval-register entry | |
| Effective from commit | |

Template: [AMENDMENT_TEMPLATE.md](AMENDMENT_TEMPLATE.md). D14 must be recorded in the [A3 author decision form](../project-state/A3_AUTHOR_DECISION_FORM.md) before this amendment takes effect.
