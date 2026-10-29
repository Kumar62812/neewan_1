# C2 — P02/P05 Retained Evidence and Source Alignment Audit

**Purpose:** Move from C1's path inventory to a reproducible integrity and source-alignment check for the two existing P02/P05 cases.  
**Scope:** Read-only validation of retained run-01/run-02 manifests, current source-to-run-02 snapshot equality, run status summaries, and review-form version provenance.  
**Not a claim:** This audit does not rerun formal tools, independently recreate the recorded run, close T06, collect human reviews, certify ambiguity, or freeze P01/P05.

## 1. Artifacts created

- Validator: \`Files/Research_Papers/benchmark/pilot_v0_1/validate_p02_p05_evidence.py\`
- Regression tests: \`Files/Research_Papers/benchmark/pilot_v0_1/tests/test_validate_p02_p05_evidence.py\`
- CI workflow: \`.github/workflows/p02-p05-evidence-validation.yml\`
- C1 case/readiness inventory: [C1_PILOT_BENCHMARK_INVENTORY.md](C1_PILOT_BENCHMARK_INVENTORY.md)

The validator is read-only. It checks the committed SHA-256 manifest itself against a pinned Git blob ID, verifies the listed files and complete inventory for P02/P05 run-01 and run-02, checks the run-02 metadata/results status relationships, and compares 19 current contract/formal-source files with their retained run-02 source snapshots.

Run from repository root:

    python Files/Research_Papers/benchmark/pilot_v0_1/validate_p02_p05_evidence.py
    python Files/Research_Papers/benchmark/pilot_v0_1/tests/test_validate_p02_p05_evidence.py

The validator emits JSON and exits nonzero when a pinned manifest, file hash, package inventory, key source identity, or status consistency check fails. It does not update expected hashes to make a change pass.

## 2. Source alignment check

The pinned source pairs include P02's requirement, interpretation, specification, consistency review, formal strategy, harness, properties, runner, reference RTL and both negative controls. P05 pairs include its requirement, interpretations, specifications, formal strategy, harness, B-state properties, runner, and reference RTL.

The compared working-tree file and run-02 snapshot should remain byte-identical for those 19 audited contract/formal inputs. A mismatch blocks a clean alignment claim; it must be investigated rather than overwritten or relabeled as the source used by the historical run.

## 3. Explicit P05 reviewer-form version difference

The audit preserves one known and intentional **version-boundary finding**:

- Current reviewer form: \`P05/annotation/v1/reviewer_form.md\`, Git blob \`5f091e8b86ad3c255ac0cd4f99f7c0ad77573093\`.
- Form captured in run-02 source snapshot: \`P05/evidence/run-02/source/annotation/REVIEW_FORM.md\`, Git blob \`79179adf25d6ff604b11c4a33bc3bb9dc5d5673a\`.

These files are not byte-identical. The run-02 snapshot form says no human responses had been collected and describes a pending protocol; the current working form is a more detailed rating form. The formal runner does not consume the reviewer form, so this difference is not a formal proof input change. Nevertheless, before human review starts, the exact current requirement, interpretations, reviewer form and analysis protocol must be versioned/hashed together, with the version actually given to reviewers recorded. Do not silently substitute the current form into the historical run-02 evidence.

## 4. Expected case status and claim boundaries

### P02

- Technical status is recorded as \`technical_verification_complete\` for the stated Boolean stable-edge digital model.
- Run-02 statuses should show reference BMC, induction and cover PASS, and the two intentionally wrong controls FAIL with counterexamples.
- P02 is a deterministic control, not an ambiguity candidate.
- T06 remains governed by its draft named closure review and author-approval procedure; this audit does not mark T06 DONE.

### P05

- Run-02 records conformance and cover PASS, with the post-reset equality check FAIL as evidence of a behavioral distinction under the tested model.
- Metadata and results must continue to show zero human annotations, unresolved plausibility, and no ambiguity certification.
- The reviewer-form version boundary described above is retained as a finding requiring explicit version handling before collection.

## 5. CI and regression-test boundary

The workflow runs the read-only validator and four fixture-based regression tests. The tests cover a valid manifest, detection of a changed listed file, detection of a modified pinned manifest, and detection of root/snapshot drift. The workflow retains the validator JSON report as a downloadable artifact for 30 days.

A successful workflow establishes consistency against the registered manifests/pins and the validator's programmed checks. It is not an independent execution of Yosys/Yosys-SMTBMC/Z3 and does not verify that the historical formal execution can be recreated from scratch.

## 6. Current result record

The exact successful run and its report will be linked here and captured in the machine-readable evidence record after CI completes. Until then, the source files, pinned manifests, results prose, and documented P05 review-form mismatch are implementation/audit baselines, not a claimed passed C2 runtime validation.

## 7. Protected boundaries

- Do not edit run-01/run-02 logs, witnesses, \`runs.json\`, \`SHA256SUMS.json\`, captured source snapshots, or metadata to make the audit pass.
- Do not rewrite P02 or P05 RTL as part of this task.
- Do not convert the P05 formal distinction into an ambiguity-certification claim.
- Do not treat a change in the reviewer form as a new formal run or change the historical source snapshot.
- This does not implement missing P03/P04/P06/P08 or conditional P07/P09–P12.
