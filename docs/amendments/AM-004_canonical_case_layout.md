# AM-004 — Canonical case layout for new benchmark instances

**Project:** FORMAL-AMBIG-RTL  
**Amendment:** AM-004  
**Status:** APPROVED DIRECTION — exact implementation and source adoption are part of T08  
**Author:** G. Naveen  
**Author approval date:** 2026-10-31  
**Decision:** D14 — ACCEPT Option A

## 1. Source and scope

This amendment records the approved direction for reconciling frozen Project Plan v1.0-FROZEN §§9–10, Benchmark Schema v1.0 §2, and the existing P01/P02/P05 structures.

Inspected source identities at the decision baseline:
- `Files/FORMAL_AMBIG_RTL_PLAN.md` Git blob: `cb2e33203ab2982a88d1a242567fae72d223edac`; A3 §3 source SHA-256: `19e1fe9abc5b8e07d96a3df339d2a020eae93fee7c9b3815a30dd49d112ee305`.
- `Files/Research_Papers/docs/benchmark_schema.md` Git blob: `ed9ddd7bd10f19bb59d126db2978579fe8fd19ea`; A3 §3 source SHA-256: `18b5e39599b519872a427c8463213f35bce0cf175e9d553bce3035028493fcac`.

## 2. Approved D14 decision

On 2026-10-31, G. Naveen explicitly accepted Option A:

**T08 shall define and validate one canonical physical layout for newly created benchmark cases, using the executed P02/P05 layout as its starting point, and shall provide a read-only path crosswalk for P01, P02 and P05.**

The approved direction includes:
- JSON metadata as the starting convention (`metadata.json`), consistent with P02/P05.
- A stable, explicit organization for requirement, interpretation, behavioral specification, reference RTL, formal harnesses/scripts, annotations/review material, and provenance.
- Isolated, immutable evidence directories using a run-number convention such as `evidence/run-NN/`.
- Exact version/hash references for source inputs and retained outputs.
- A crosswalk mapping the logical artifacts required by the PLAN/schema to their actual P01/P02/P05 paths, or explicitly marking an artifact absent.

This approves the layout policy and direction. T08 must specify the exact directory tree, required/optional files, metadata contract, path-resolution rules, and validator/runner behavior before the layout is treated as implemented or frozen.

## 3. Existing cases and evidence — no migration

P01, P02 and P05 remain in their existing paths and formats. This decision does not migrate, rename, rewrite, normalize, or regenerate their metadata, source documents, RTL, formal harnesses, logs, witnesses, manifests, run directories, reports, or accepted archives.

The crosswalk is descriptive and read-only for those existing cases. Any future migration requires separate explicit authorization, new versioned artifacts, and preservation of the originals.

## 4. Adoption timing and relationship to T08

AM-004 is approved as the D14 governance direction on 2026-10-31. The exact canonical tree and corresponding conforming changes to PLAN §10 and Benchmark Schema §2 are to be prepared and adopted together with T08 after T08 validation.

This record does not itself modify the frozen PLAN or Benchmark Schema, does not declare T08 started or complete, and does not claim that a new-case runner or template has passed validation. D14 approval alone does not satisfy the other T08 prerequisites or freeze the template.

## 5. Required T08 validation

T08 must:
1. Define the exact canonical tree and metadata schema, including the D1 primary-category/optional thematic-tag rule and D2 certification/lifecycle/release-freeze separation.
2. Create a clean new case from the template using the intended runner.
3. Validate required/optional paths, metadata constraints, stable identifiers, versioning, and failure behavior.
4. Create a complete read-only path crosswalk for P01, P02 and P05; explicitly record absent artifacts without fabricating them.
5. Confirm evidence isolation and immutable run-directory behavior.
6. Validate source and evidence hashes without rewriting historical evidence.
7. Record exact template/schema/runner versions and hashes in the T08 freeze record.

## 6. Approval and limitations

**Disposition:** ACCEPT — D14 Option A  
**Author:** G. Naveen  
**Date:** 2026-10-31

This approval is limited to the canonical-layout direction described above. It does not certify any benchmark case, alter historical results, authorize scored experiments, complete T08, or declare the reusable template frozen.
