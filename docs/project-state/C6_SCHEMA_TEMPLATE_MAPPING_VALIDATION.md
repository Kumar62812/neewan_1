# C6 — Non-binding schema-to-template mapping proposal

**Status:** Proposal package committed; CI validation pending.  
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

Actual workflow results and the machine-readable evidence record will be attached here after CI completes.

## Non-claims

This proposal does not authorize D2/D14, change canonical schema/template files, freeze P01, migrate any existing case, modify historical evidence, run formal tools, perform human review, run LLM experiments, certify ambiguity or declare the project complete.
