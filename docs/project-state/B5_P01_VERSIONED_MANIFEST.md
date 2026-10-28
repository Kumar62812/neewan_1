# B5 — Versioned P01 Package Manifest

**Status:** Manifest committed; validator and regression tests now use it as the centralized baseline. This is a source/evidence inventory, not a freeze, certification or a substitute for a runtime validation result.

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

The archive checksum is transcribed from the already-existing provenance register and committed checksum sidecar. This B5 connected GitHub session did not download the binary archive to independently recompute that digest. The B2 validator will recompute it from the local archive when run on a complete checkout.

## Tamper-evident use

The B2 validator now reads the baseline artifact IDs and archive digest from the manifest. It also checks the manifest's own Git blob ID against a pin stored in the validator. This avoids silently redefining the expected hashes by editing the manifest alone.

Any intentional manifest change must be versioned and reviewed. The manifest pin inside the validator must then be updated deliberately in the same controlled change. Do not refresh hashes automatically in response to a failure.

The B3 regression suite now includes a fourth case which alters a copy of the manifest and requires the validator to report the mismatch. All test mutations occur in temporary fixtures.

## Limits

- The baseline fingerprints are taken from the B1 inspection snapshot; the presence of a hash does not independently prove a design property.
- The validator/regression suite has not been executed in this connected GitHub session.
- The accepted formal evidence remains scoped to the pinned base plus the retained path-only patch.
- Pending decisions D2 and D14 remain pending. This does not add canonical case metadata or activate AM-002/AM-004.
- P01 Golden Template remains NOT FROZEN. No release tag or certification is created by B5.

## B5 checklist

- [x] Add versioned JSON package manifest.
- [x] Centralize 12 baseline source Git blob IDs and accepted archive checksum reference.
- [x] Make the validator use the manifest and pin the manifest's own Git blob ID.
- [x] Add a regression test for manifest tampering.
- [x] Update B2/B3 guides, P01 README and project log.
- [ ] Runtime validator and four regression tests executed on complete checkout — pending.
