# C8 — C5–C7 cross-artifact integration audit

**Scope:** Read-only integration of the C5 readiness audit, C6 schema/template mapping proposal, and C7 role-aware fixture validation. C8 checks that the reports, source fingerprints, mapping and fixtures tell a consistent story.

**Audit result: PASS** — 54/54 integration checks passed; 16/16 pinned objects matched; 18/18 schema fields mapped; 4/4 fixture roles present; and 11/11 regression tests passed in [GitHub Actions run 40816068105](https://github.com/Kumar62812/neewan_1/actions/runs/40816068105).  
**Integration disposition:** CONSISTENT BUT GOVERNANCE BLOCKED. D2/D14 remain open; reusable template remains not frozen.

## Why C8

Individual audits can pass while their outputs disagree. C8 adds a single integration gate to catch drift across: the canonical source object IDs; C5's blocked-readiness result; C6's 18-field non-binding proposal and validation evidence; C7's 53-check / 10-test result; the four C7 role fixtures; and the open D2/D14 governance decisions.

## Integration conditions

1. Every pinned C5–C7 record, canonical source and fixture retains the expected Git blob identity.
2. The schema's 18 listed fields are represented exactly once by C6's mapping proposal.
3. C6 remains non-binding and its source references match the pinned schema, YAML template and formal protocol.
4. C6 and C7 evidence records agree with their human-readable reports and report successful runs.
5. The four fixture roles agree with the C6 role proposal and enforce the appropriate shape; all remain synthetic, unexecuted and uncertified.
6. D2/D14 remain explicitly open and P01's template stays blocked/not frozen.

## Artifacts

- Validator: `Files/Research_Papers/benchmark/pilot_v0_1/audit_c8_integration.py`
- Regression tests: `Files/Research_Papers/benchmark/pilot_v0_1/tests/test_audit_c8_integration.py`
- Workflow: `.github/workflows/c8-cross-artifact-integration.yml`
- [Machine-readable C8 evidence](evidence/C8_C5_C7_INTEGRATION_RUN_40816068105.json).
- [Workflow report artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40816068105/artifacts/12872102588), artifact ID `12872102588`, size 2,288 bytes, uploaded ZIP digest `sha256:e89e433ee71bcd5e783a23a9015ed3c2de5acd840ca2b919f19f02e56e40707d`, expires 2026-11-28 04:08:41 UTC.

## Interpretation

A PASS means only that the pinned records are mutually consistent as of the tested commit. It does not approve D2/D14, make the schema mapping normative, establish scientific truth for any fixture, freeze a template, or establish project completion.

## Non-claims

No canonical schema/template, P01/P02/P05 source, historical formal run, manifest or witness is modified. No formal tool, human review or LLM experiment is executed. The C7 fixtures remain prohibited from benchmark/model-evaluation use.


## Verified CI and audit trail

- Successful workflow: [40816068105](https://github.com/Kumar62812/neewan_1/actions/runs/40816068105), tested commit `8fda51296dce56c398fcf92166361c5117fd9ec6`.
- Results: **54/54 checks passed**, **16/16 pinned objects**, **18 schema fields and 18 mapping entries**, **four role fixtures**, and **11/11 tests passed** under Python 3.12.15.
- The aggregate status is `CONSISTENT_BUT_GOVERNANCE_BLOCKED`: C5–C7 artifacts agree; this does not resolve the underlying decisions.
- Four earlier attempts are retained as CI evidence: [40815419231](https://github.com/Kumar62812/neewan_1/actions/runs/40815419231), [40815590451](https://github.com/Kumar62812/neewan_1/actions/runs/40815590451), [40815924948](https://github.com/Kumar62812/neewan_1/actions/runs/40815924948), and [40815990451](https://github.com/Kumar62812/neewan_1/actions/runs/40815990451). They exposed a fixture pin-path error and overly broad/exact report-parsing assertions; fixes were committed before the passing run. No failed run was deleted or relabelled.
- Final artifact: [12872102588](https://github.com/Kumar62812/neewan_1/actions/runs/40816068105/artifacts/12872102588), 2,288 bytes, ZIP digest `sha256:e89e433ee71bcd5e783a23a9015ed3c2de5acd840ca2b919f19f02e56e40707d`.
