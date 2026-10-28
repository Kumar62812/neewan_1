# B5 — Versioned P01 Package Manifest

**Status:** Manifest committed; validator and four regression tests passed in [GitHub Actions run 40752919435](https://github.com/Kumar62812/neewan_1/actions/runs/40752919435). This is a source/evidence inventory, not a freeze or certification.

## Manifest

The machine-readable inventory is at:

    Files/Research_Papers/benchmark/pilot_v0_1/P01/p01_package_manifest_v1.json

It records:
- the P01 package identity and its non-frozen status;
- the B1 baseline snapshot commit;
- 12 source artifacts and their Git blob object IDs (SHA-1 Git object identifiers, not SHA-256 digests);
- the accepted evidence archive path and registered SHA-256 checksum;
- the pinned base revision and retained path-only patch checksum;
- explicit non-claims about certification, freeze and independent reproduction.

The expected archive checksum was transcribed from the existing provenance register and committed checksum sidecar. The B5 authoring step did not itself download the archive, but the B2 validator subsequently recomputed SHA-256 from the archive in the checked-out repository and passed in [GitHub Actions run 40752919435](https://github.com/Kumar62812/neewan_1/actions/runs/40752919435).

## Tamper-evident use

The B2 validator now reads the baseline artifact IDs and archive digest from the manifest. It also checks the manifest's own Git blob ID against a pin stored in the validator. This avoids silently redefining the expected hashes by editing the manifest alone.

Any intentional manifest change must be versioned and reviewed. The manifest pin inside the validator must then be updated deliberately in the same controlled change. Do not refresh hashes automatically in response to a failure.

The B3 regression suite now includes a fourth case which alters a copy of the manifest and requires the validator to report the mismatch. All test mutations occur in temporary fixtures.

## Limits

- The baseline fingerprints are taken from the B1 inspection snapshot; the presence of a hash does not independently prove a design property.
- The validator/regression suite passed in the remote workflow run linked above; this is structural/integrity validation, not a formal-tool rerun.
- The accepted formal evidence remains scoped to the pinned base plus the retained path-only patch.
- Pending decisions D2 and D14 remain pending. This does not add canonical case metadata or activate AM-002/AM-004.
- P01 Golden Template remains NOT FROZEN. No release tag or certification is created by B5.

## B5 checklist

- [x] Add versioned JSON package manifest.
- [x] Centralize 12 baseline source Git blob IDs and accepted archive checksum reference.
- [x] Make the validator use the manifest and pin the manifest's own Git blob ID.
- [x] Add a regression test for manifest tampering.
- [x] Update B2/B3 guides, P01 README and project log.
- [x] Runtime validator and all four regression tests passed on GitHub-hosted runner in [run 40752919435](https://github.com/Kumar62812/neewan_1/actions/runs/40752919435).

## B6 validation evidence

The stable execution/provenance record is available at [B6 — P01 Validation Evidence and Provenance Record](B6_P01_VALIDATION_EVIDENCE_RECORD.md), with its machine-readable run record at [P01_CI_VALIDATION_RUN_40752919435.json](evidence/P01_CI_VALIDATION_RUN_40752919435.json). The recorded GitHub Actions run passed all 26 validator checks and four regression tests. It is a source-integrity/validator test result, not an RTL formal-tool run or certification.

