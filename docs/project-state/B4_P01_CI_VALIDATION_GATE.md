# B4 — Automated P01 Package Validation Gate

**Status:** Continuous-integration workflow added. A successful workflow run must be observed before calling automated validation operational. This gate does not perform P01's accepted formal run or freeze/certify the template.

## Workflow

The workflow at \`.github/workflows/p01-package-validation.yml\` is intended to run on relevant pushes to \`main\` and \`research/end-to-end-sequence\`, and on pull requests targeting \`main\` when P01 package, validation, or workflow files change.

It performs the following in a clean GitHub-hosted runner:

1. Checks out the repository and configures Python 3.11.
2. Runs the read-only package validator, preserving its JSON output as a workflow artifact.
3. Runs the B3 regression tests, including baseline success and two integrity-mutation checks.
4. Uploads the validation JSON report, including on failure, for diagnosis.

## Scope limits

- The validator checks baseline source fingerprints and the registered accepted-archive SHA-256. Changes to protected baseline files are surfaced as failures rather than silently accepted.
- The regression tests mutate only isolated temporary copies.
- No RTL/formal tools are invoked by this workflow; it is a structural, source-integrity, and validator-regression gate.
- A successful workflow run does not substitute for formal reproduction, independent human review, ambiguity certification, or author-approved template freeze.
- This workflow cannot validate local-only backups or prove that all unpublished material is preserved.

## Run interpretation

- **PASS:** source fingerprints and archive checksum match the B1 baseline and the regression suite behaves as expected.
- **FAIL:** inspect the named validator check or test failure; do not update baseline hashes simply to make a changed file pass. Any intentional baseline update requires separate versioned provenance.
- **Workflow not yet run / queued:** automation is committed but operational result is not yet demonstrated.

## B4 completion boundary

- [x] CI workflow definition committed.
- [x] Validator and regression tests wired into the workflow.
- [x] JSON report artifact configured.
- [ ] Successful remote workflow run verified — depends on GitHub Actions execution.
- [ ] P01 independent certification / template freeze — outside B4 and not claimed.
