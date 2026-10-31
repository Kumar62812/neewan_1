# D14 — Canonical Case-Template Layout Author Approval

**Project:** FORMAL-AMBIG-RTL  
**Decision:** D14 — Canonical case-template layout  
**Disposition:** ACCEPT — Option A  
**Author:** G. Naveen  
**Date:** 2026-10-31  
**Amendment:** [AM-004 — Canonical case layout for new benchmark instances](../../amendments/AM-004_canonical_case_layout.md)

## Explicit author decision

G. Naveen approves Option A: T08 will define one canonical physical layout for new benchmark cases, based on the executed P02/P05 layout, and provide a read-only path crosswalk for P01, P02 and P05.

The approved direction uses JSON metadata as the starting convention and isolated immutable `evidence/run-NN/` directories. T08 must define the exact directory tree, metadata contract, required/optional artifacts, path-resolution rules, and runner/validator behavior.

## Preservation and scope

- P01, P02 and P05 existing files, metadata, source RTL, formal evidence, run directories, manifests, witnesses, reports, and accepted archives remain unchanged.
- No existing case is migrated or rewritten. The crosswalk is descriptive and read-only.
- Any future migration requires separate explicit authorization and new versioned artifacts.
- Frozen PLAN §10 and Benchmark Schema §2 are not modified by this decision. The corresponding source adoption is to be prepared together with T08 after validation.
- D14 does not itself start or complete T08, freeze the reusable template, certify any case, or authorize scored experiments.

## Approval

> D14 author disposition: A. Author: G. Naveen. Date: 2026-10-31.

**Recorded:** ACCEPT — Option A, 2026-10-31.
