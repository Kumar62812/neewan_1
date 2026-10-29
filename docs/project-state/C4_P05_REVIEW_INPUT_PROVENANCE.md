# C4 — P05 prospective review-input provenance

**Status: PASS** — the pinned preparation bundle passed 61/61 automated checks and all six regression tests in [GitHub Actions run 40811887068](https://github.com/Kumar62812/neewan_1/actions/runs/40811887068).  
**Branch:** \`research/end-to-end-sequence\`  
**Scope:** Make the prospective P05 review-input set reproducible, and account explicitly for the current reviewer form being different from the form captured in historical run-02.

## 1. Why C4 exists

C2 identified the version boundary: the current blank reviewer form and the form inside the historical P05 run-02 snapshot are not byte-identical. The formal runner does not consume the reviewer form, so the distinction does not invalidate the formal run. However, the form actually supplied to reviewers must be recorded exactly, and the historical form must never be silently substituted or relabeled.

C4 pins the prospective review materials and their coordinator/technical provenance in [review_input_manifest_v1.json](../../Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/review_input_manifest_v1.json). For every entry, the manifest records the Git blob ID, SHA-256 digest, byte count and role.

## 2. Frozen identities versus review authorization

The prospective reviewer-facing set is exactly:
- \`P05_REQUIREMENT.md\`
- \`P05_INTERPRETATIONS.md\`
- \`annotation/v1/reviewer_form.md\`

Coordinator-only and technical-provenance files are also pinned: the coordinator README and analysis protocol, P05 specifications, metadata and results, formal strategy/harness/properties/runner, reference RTL, and the run-02 manifest.

**This is a versioned preparation package, not an approval to start human review.** The current P05 case remains UNRESOLVED, human responses remain zero, ambiguity certification remains false, and LLM evaluation remains unperformed. The project policy requires technical completion before independent human reviews; that gate remains closed.

The current prospective form has Git blob \`5f091e8b86ad3c255ac0cd4f99f7c0ad77573093\` and SHA-256 \`817387d4fff25ba47871e1b9d43c71cddc1c1872363086fb0f1abd361dbe4aa8\`. The historic form captured in run-02 has Git blob \`79179adf25d6ff604b11c4a33bc3bb9dc5d5673a\` and SHA-256 \`c272940ef73e45d8159c8eb0df0e698706bec7797486b4ef36f4b9737dd81ce9\`. C4 keeps both identities explicit, including a check that the run-02 SHA-256 manifest still maps to the historic form digest.

## 3. Automation

- Validator: \`Files/Research_Papers/benchmark/pilot_v0_1/validate_p05_review_input_bundle.py\`
- Regression tests: \`Files/Research_Papers/benchmark/pilot_v0_1/tests/test_validate_p05_review_input_bundle.py\`
- Workflow: \`.github/workflows/p05-review-input-integrity.yml\`

The read-only validator checks the pinned manifest object, all 15 file identities (Git blob and SHA-256), byte counts, the current/historic form split, run-02 manifest binding, and P05 status boundaries. Regression tests exercise positive hash validation, changed-file detection, Git blob hash calculation and preservation of the historical form boundary.

## 4. Claim boundaries

C4 does not change the requirement, interpretations, specifications, form, analysis protocol, metadata, RTL, formal logs, witnesses, run-01/run-02 manifests, or captured source snapshots. It does not collect human ratings, infer that reviewers are recruited, claim the P05 gold standard is frozen, close the project, or certify ambiguity. If any pinned input changes, the manifest must be intentionally versioned and reviewed; do not silently refresh its expected hashes to make a test pass.

## 5. Verified result

**PASS:** [GitHub Actions run 40811887068](https://github.com/Kumar62812/neewan_1/actions/runs/40811887068) on commit \`e15fea31a53d4b656d057bedaec7cbf1ad883f70\`.

- **61/61 validation checks passed.** These include the pinned manifest identity, all 15 file records (Git blob SHA-1, SHA-256 and exact byte count), the current-versus-historical form boundary, run-02 manifest linkage, and P05's unresolved/no-human-review/no-certification state.
- **6/6 regression tests passed**, including mutation detection and the historical-form separation condition.
- [Machine-readable C4 evidence record](evidence/C4_P05_REVIEW_INPUT_INTEGRITY_RUN_40811887068.json).
- [Validation report artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40811887068/artifacts/12870139889), artifact ID 12870139889, 2,921 bytes, digest \`sha256:4727098a0dd9ff13d5978a82304e00cc262b1e06a23dfa1b0ec48a77b3e0912f\`, expires 2026-11-28 03:23:50 UTC.

## 6. Final status boundary

C4 completes the source-identity/provenance preparation step for the current prospective P05 review-input set. It does not make the P05 scientific candidate frozen or certified. Human review remains blocked until the project's complete technical-work gate is satisfied. If any of the pinned inputs changes, create and audit a new version; do not silently refresh the existing pins.
