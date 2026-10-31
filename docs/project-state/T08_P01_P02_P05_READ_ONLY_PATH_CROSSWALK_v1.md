# T08 — P01/P02/P05 read-only path crosswalk (v1)

**Purpose:** map logical artifacts to observed repository paths without changing historical cases.  
**Inspection ref:** `research/end-to-end-sequence`, commit `8cf8fca70fe853b67dac936137f175d477b6de05`.  
**Disposition:** descriptive mapping only; no migration, normalization, or equivalence claim.

| Logical artifact | P01 observed path | P02 observed path | P05 observed path |
|---|---|---|---|
| Metadata | `P01/p01_package_manifest_v1.json` (not a metadata.json equivalent) | `P02/metadata.json` | `P05/metadata.json` |
| Requirement | `P01/requirement.md` | `P02/P02_REQUIREMENT.md` | `P05/P05_REQUIREMENT.md` |
| Interpretation | `P01/interpretations/interpretation_01.md` | `P02/P02_INTERPRETATION.md` | `P05/P05_INTERPRETATIONS.md` |
| Behavioral specification | `P01/behavioral_specification/specification_01.md` | `P02/P02_SPECIFICATION.md` | `P05/P05_SPECIFICATIONS.md` |
| Reference RTL | `P01/reference_rtl/rtl_01.sv` | `P02/reference_rtl/register.sv` | `P05/reference_rtl/responses.sv` |
| Formal properties | `P01/formal/properties/mux2to1_properties.sv` | `P02/formal/properties/register_properties.sv` | `P05/formal/b_properties.sv` (run-02 source also contains this) |
| Formal harness | `P01/formal/harness_reference.sv` and `harness_wrong.sv` | `P02/formal/harness.sv` | `P05/formal/harness.sv` |
| Formal scripts | `P01/formal/run_p01_formal.sh` | `P02/formal/run.py` | `P05/formal/run.py` |
| Annotation/review | `P01/review/pre_rtl_review.md`; no separate annotation package observed | No annotation directory observed at case root | `P05/annotation/v1/` |
| Provenance | Package manifest and formal evidence recall; no separate provenance directory observed | Evidence run environment and source snapshot | Annotation manifest and evidence run source snapshot |
| Evidence runs | `P01/formal/evidence/p01-20260930T220622Z/` | `P02/evidence/run-01/`, `run-02/` | `P05/evidence/run-01/`, `run-02/` |

## Interpretation constraints

- P01's package manifest is not silently reinterpreted as v2 metadata.
- P02/P05 metadata remains untouched and is not assumed to conform to v2.
- Missing case-root annotation/provenance artifacts are reported as not observed; source snapshots embedded inside evidence runs are not moved.
- The crosswalk records observed paths at the inspection commit only. Re-check exact paths and blob hashes in the current tree before any later release operation.
- Existing evidence directories and checksum manifests remain immutable. Any migration requires separate explicit authorization and new versioned artifacts.
