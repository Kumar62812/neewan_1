# B6 — P01 Validation Evidence and Provenance Record

**Status:** Completed. A successful remote validation run has been inspected, summarized in a stable repository record, and linked to its machine-readable counterpart.

## 1. Evidence record

- Machine-readable record: [P01 CI validation run 40752919435](evidence/P01_CI_VALIDATION_RUN_40752919435.json)
- GitHub Actions run: [40752919435 — PASS](https://github.com/Kumar62812/neewan_1/actions/runs/40752919435)
- Tested branch: \`research/end-to-end-sequence\`
- Tested commit: \`09094366a11294a86975e3a1a5aedccd47cfcc71\`
- Workflow: \`.github/workflows/p01-package-validation.yml\`, run number 13, push event, attempt 1.
- Recorded result: **26/26 validator checks passed; 0 failed.**

## 2. Checks and test results

The CI validator passed all 26 checks, including the manifest's pinned Git blob, manifest status/schema, all 12 baseline source fingerprints, file inventory, contract-text checks, RTL roles, common formal property/harness use, expected positive/negative SBY configuration intents, and the accepted archive SHA-256.

All four regression tests passed:

1. \`test_unmodified_baseline_fixture_passes\`
2. \`test_source_mutation_is_detected\`
3. \`test_accepted_archive_mutation_is_detected\`
4. \`test_manifest_mutation_is_detected\`

The recorded unittest duration was 0.144 seconds. The test mutation cases operate on temporary fixtures.

## 3. Tested source identities

| Artifact | Git blob ID |
|---|---|
| P01 package manifest | \`bd3329ea1af786eeedafb556c4a8ea7cb404bfcc\` |
| Validator v1.1 | \`38a90573e67c69f140a1fc7c80e00d4f11bcdc9d\` |
| Regression suite | \`cee11305b90829bfcdad8e9782e0e6fe3925fdb3\` |
| CI workflow | \`9ecd6321a1c0053d1c7c09eba585cb2c75a05d94\` |

These are Git blob object IDs, not SHA-256 digests of file bytes.

## 4. Retained GitHub artifact

The workflow report was uploaded as artifact \`p01-package-validation-report\` (ID \`12845086153\`, ZIP size 1,204 bytes). GitHub reports the ZIP digest as:

\`sha256:1a24dd92554b849478aec96054874e8215258fe94c8809db08f48afa0366c1c3\`

[Open or download the workflow artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40752919435/artifacts/12845086153).

The artifact is scheduled to expire at **2026-11-27 19:17:19 UTC**. The committed JSON record and Actions run page preserve the key provenance metadata beyond the artifact's retention period; they do not preserve the binary artifact after expiry.

## 5. Claim boundary

This validation establishes package/source integrity and expected validator regression behavior for the tested commit. It does **not**:
- run Yosys, SymbiYosys, Z3 or the P01 formal runner;
- independently reproduce the accepted formal execution;
- constitute an external methodology review or ambiguity certification;
- authorize a release tag or P01 Golden Template freeze.

P01 remains **NOT FROZEN**. Pending decisions D2 and D14 remain pending. The accepted P01 evidence remains limited to its recorded pinned base plus the retained path-only patch.

## 6. B6 completion checklist

- [x] Inspect the successful CI run and confirm every workflow step succeeded.
- [x] Record exact tested commit and Git blob identities for the manifest, validator, tests and workflow.
- [x] Record all 26 validator checks and all four regression test outcomes.
- [x] Record the uploaded artifact ID, ZIP digest, download link and expiry.
- [x] Separate integrity-test claims from formal reproduction and certification claims.
- [x] Add a machine-readable evidence record and project log entry.

## 6. Follow-up CI confirmation

After B6 was linked from the P01 README, GitHub Actions run [40765501022 — PASS](https://github.com/Kumar62812/neewan_1/actions/runs/40765501022) completed on commit \`92f8cf8323a7457325c2d5016c798783aa060171\`. It again reported **26/26 validator checks passed** and **4/4 regression tests passed**. Its report artifact is [available until 2026-11-27 20:41:27 UTC](https://github.com/Kumar62812/neewan_1/actions/runs/40765501022/artifacts/12849069246).

This follow-up checks the P01 package validator and regression suite on the branch commit containing the README links. The B6 JSON provenance file itself is a documentation record and is not one of the 12 source artifacts fingerprinted by the P01 manifest.


