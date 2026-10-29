# C8 — C5–C7 cross-artifact integration audit

**Scope:** Read-only integration of the C5 readiness audit, C6 schema/template mapping proposal, and C7 role-aware fixture validation. C8 checks that the reports, source fingerprints, mapping and fixtures tell a consistent story.

**Status before CI:** implementation committed; automated result pending.  
**Expected governance boundary:** D2/D14 open; reusable template remains not frozen.

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
- CI result and machine-readable evidence will be recorded after execution.

## Interpretation

A PASS means only that the pinned records are mutually consistent as of the tested commit. It does not approve D2/D14, make the schema mapping normative, establish scientific truth for any fixture, freeze a template, or establish project completion.

## Non-claims

No canonical schema/template, P01/P02/P05 source, historical formal run, manifest or witness is modified. No formal tool, human review or LLM experiment is executed. The C7 fixtures remain prohibited from benchmark/model-evaluation use.
