# C6 — Non-binding schema-to-template mapping proposal

**Validation result: PASS** — 10/10 source/coverage checks and 7/7 regression tests passed in [GitHub Actions run 40814081793](https://github.com/Kumar62812/neewan_1/actions/runs/40814081793).  
**Proposal status:** `NON_BINDING_REQUIRES_AUTHOR_DECISION`.  
**Canonical schema/template:** unchanged.

## Outcome sought

Translate C5's identified gaps into an auditable decision package. The JSON matrix maps all 18 schema fields, records source object IDs, and tags fields that are missing, distributed, conditional or semantically unresolved. The validator checks source identity, field coverage and role-specific requirements; six regression tests guard the proposal boundaries.

## Main recommendation for author discussion

The current schema's status labels mix a possible workflow lifecycle (candidate/frozen) with scientific outcomes (certified ambiguous, unambiguous control, negative candidate, inconclusive). Consider separating workflow status, scientific classification and benchmark role, but do not implement this suggestion before D2 is resolved. Under D14, select either a normative mapping for the existing nested YAML or a versioned format update with migration notes.

## Files

- Proposal: `docs/project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.json`
- Validator: `Files/Research_Papers/benchmark/pilot_v0_1/validate_c6_schema_mapping_proposal.py`
- Regression tests: `Files/Research_Papers/benchmark/pilot_v0_1/tests/test_validate_c6_schema_mapping_proposal.py`
- Workflow: `.github/workflows/c6-schema-template-mapping.yml`

Machine-readable validation evidence: [C6_SCHEMA_TEMPLATE_MAPPING_RUN_40814081793.json](evidence/C6_SCHEMA_TEMPLATE_MAPPING_RUN_40814081793.json). The [workflow report artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40814081793/artifacts/12871731814) is artifact ID `12871731814`, 1,111 bytes, ZIP digest `sha256:5cd7b46b8bb7e6435a34bd32a5669675d4f473a876013018d3eb109e43eb4b9e`, expires 2026-11-28 03:47:20 UTC.

## Non-claims

This proposal does not authorize D2/D14, change canonical schema/template files, freeze P01, migrate any existing case, modify historical evidence, run formal tools, perform human review, run LLM experiments, certify ambiguity or declare the project complete.


## 9. Verified execution

- Workflow [40814081793 — success](https://github.com/Kumar62812/neewan_1/actions/runs/40814081793), tested commit `cf8e753e21ef42f1e4280453bd4e3ff30fe875d2`.
- Validation: **10 checks passed, 0 failed**; the 18 schema fields each have exactly one mapping entry.
- Regression suite: **7 tests passed** under Python 3.12.15.
- The validator confirmed all three pinned source Git blob IDs.
- Audit result is PASS; proposal status remains `NON_BINDING_REQUIRES_AUTHOR_DECISION`.
