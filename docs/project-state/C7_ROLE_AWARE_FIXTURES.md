# C7 — Role-aware benchmark fixture validation

**Scope:** Validate proposal-only fixture shapes for unambiguous controls, ambiguity candidates, negative/rejected candidates, and robustness cases. These files are deliberately synthetic, not real benchmark instances.

**Audit result: PASS** — 53/53 source/fixture checks and 10/10 regression tests passed in [GitHub Actions run 40814758386](https://github.com/Kumar62812/neewan_1/actions/runs/40814758386).  
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

Machine-readable evidence: [C7_ROLE_AWARE_FIXTURES_RUN_40814758386.json](evidence/C7_ROLE_AWARE_FIXTURES_RUN_40814758386.json). [Validation report artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40814758386/artifacts/12871802752), artifact ID `12871802752`, 1,771 bytes, uploaded ZIP digest `sha256:f76d7480fc923714ae30cd29068e379915a7a4a717c9f137d5447182d822f581`, expires 2026-11-28 03:54:39 UTC.

## What would close the actual reusable-template gate

1. Record the approved D2 status/classification vocabulary.
2. Record the approved D14 canonical field paths and layout.
3. Decide whether proposal-only fields such as `case_role`, `classification` and `annotation_record_path` become canonical.
4. Convert the approved contract—not these sample fixtures—into schema-level validators and migration tests.
5. Test representative fixtures without modifying historical P01/P02/P05 evidence, then make a separate freeze decision.

## Non-claims

C7 does not approve D2/D14, update canonical schema/template files, freeze the Golden Template, construct a real P03/P04/P06/P08 case, run formal tools, collect reviews, execute LLM experiments, certify ambiguity, or mark the overall project complete.


## Verified CI and correction history

- **Passing workflow:** [40814758386](https://github.com/Kumar62812/neewan_1/actions/runs/40814758386), tested commit `2a4dd8998b6e8aaae6aa6a0ba5e8098273148014`.
- **Audit:** 53 checks passed, 0 failed, covering four role fixtures and four pinned source objects.
- **Regression tests:** 10 passed under Python 3.12.15.
- Two earlier C7 workflow attempts are retained in Actions history: [40814629811](https://github.com/Kumar62812/neewan_1/actions/runs/40814629811) and [40814692433](https://github.com/Kumar62812/neewan_1/actions/runs/40814692433). Both exposed syntax errors in the newly added validator. Those errors were corrected before the passing run; the failures are not deleted or relabelled.
- This verifies the synthetic fixture rules only. No D2/D14 decision, canonical schema change, formal run, human review, or certification is claimed.
