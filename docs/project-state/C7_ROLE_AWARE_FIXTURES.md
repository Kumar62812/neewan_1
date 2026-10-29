# C7 — Role-aware benchmark fixture validation

**Scope:** Validate proposal-only fixture shapes for unambiguous controls, ambiguity candidates, negative/rejected candidates, and robustness cases. These files are deliberately synthetic, not real benchmark instances.

**Status before CI:** implementation committed; validation pending.  
**Canonical schema/template status:** unchanged.  
**D2/D14:** unresolved; no authorization to freeze or migrate.

## Why C7

C6 produced a non-binding mapping proposal. C7 tests the most consequential implication: the data shape must support different case roles without forcing a control to invent a plausible second interpretation and without turning a deliberately wrong checker-control implementation into interpretation B.

## Fixture set

| Fixture role | Structural rule exercised | Explicit boundary |
|---|---|---|
| Unambiguous control | Interpretation A and reference A; B is absent; checker-negative control is separate | Wrong RTL is not interpretation B |
| Ambiguity candidate | Both A/B placeholders and paired RTL references are structurally required | Does not claim linguistic plausibility or formal distinction |
| Negative candidate | Rejection record is present but marked as a not-adjudicated placeholder | Does not claim a real candidate was rejected |
| Robustness case | Robustness target and wrong checker-control implementation are separate | Does not claim the control ran or passed/failed |

Every fixture uses reserved `C7-FIXTURE-` identifiers, `fixture://` artifact references, synthetic provenance, candidate workflow status, null classification, `NOT_RUN` formal status, zero human responses, and no certification. The fixtures are forbidden as LLM prompts, formal evidence, annotations, or benchmark data.

## Artifacts

- Fixtures: `Files/Research_Papers/benchmark/pilot_v0_1/tests/fixtures/c7_role_aware/`
- Audit: `Files/Research_Papers/benchmark/pilot_v0_1/audit_c7_role_aware_fixtures.py`
- Regression tests: `Files/Research_Papers/benchmark/pilot_v0_1/tests/test_audit_c7_role_aware_fixtures.py`
- Workflow: `.github/workflows/c7-role-aware-fixtures.yml`

CI result and machine-readable evidence will be recorded after the workflow completes.

## What would close the actual reusable-template gate

1. Record the approved D2 status/classification vocabulary.
2. Record the approved D14 canonical field paths and layout.
3. Decide whether proposal-only fields such as `case_role`, `classification` and `annotation_record_path` become canonical.
4. Convert the approved contract—not these sample fixtures—into schema-level validators and migration tests.
5. Test representative fixtures without modifying historical P01/P02/P05 evidence, then make a separate freeze decision.

## Non-claims

C7 does not approve D2/D14, update canonical schema/template files, freeze the Golden Template, construct a real P03/P04/P06/P08 case, run formal tools, collect reviews, execute LLM experiments, certify ambiguity, or mark the overall project complete.
