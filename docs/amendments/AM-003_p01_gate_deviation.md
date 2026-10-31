# AM-003 — P01 Gate 2 sequencing deviation and T08 template-freeze responsibility

**Project:** FORMAL-AMBIG-RTL  
**Amendment:** AM-003  
**Status:** APPROVED — author disposition D9 Option B  
**Author:** G. Naveen  
**Author approval date:** 2026-10-31  
**Effective date:** 2026-10-31 (the date this amendment is recorded; not retroactive)

## 1. Source and scope

This amendment addresses the frozen Project Plan v1.0-FROZEN, §§9, 13 (Gate 2), and 14.

- Frozen source: `Files/FORMAL_AMBIG_RTL_PLAN.md`
- Source SHA-256 recorded in A3 §3: `19e1fe9abc5b8e07d96a3df339d2a020eae93fee7c9b3815a30dd49d112ee305`
- Git blob at the inspected branch baseline: `cb2e33203ab2982a88d1a242567fae72d223edac`
- Related project-direction record: `02_CERTIFICATION/P01_GUIDE_MEETING_RECORD.md`
- Guide record Git blob at the inspected baseline: `6efb7340550c7145b00b97e65af4d54938581e00`

The guide record reports professor approval/direction to proceed with P02. It explicitly states that the actual meeting date, approval date, approval mode, and verbatim wording were not supplied. Its **student record date is 2026-10-08**. That date is recorded only as the student record date; it is not represented as the meeting date or professor-approval date.

## 2. Author decision

On 2026-10-31, G. Naveen explicitly accepted D9 Option B and approved this amendment.

The decision acknowledges that P02 and P05 work was performed before P01 Golden Template was formally frozen, contrary to the original sequence in PLAN §§9, 13, and 14. The deviation is disclosed as a historical sequencing fact. This amendment does not state or imply that the original Gate 2 requirements had already been met.

## 3. Approved governance rule

1. The reusable P01-derived template-freeze function is assigned to T08, the reusable case-template task.
2. T08 must define and validate the canonical reusable template, preserve the P01 evidence lineage, and explicitly record the template-freeze decision and its supporting checks before any claim that the reusable template is frozen.
3. T08 remains subject to the A3 execution order: D1, D2, D9, and D14 must be decided before T08 starts. D14 remains a separate pending author decision; this amendment does not bypass it.
4. The original P01 Gate 2 requirements are not silently marked as historically completed. Outstanding annotation-workflow, clean-reproduction, review, and template-validation evidence must be explicitly inventoried and resolved or transparently scoped by T08.
5. This amendment takes effect only from its recording on 2026-10-31. It is not a retroactive authorization of earlier P02/P05 construction or formal execution.

## 4. Historical evidence and claim boundaries

- Existing P01, P02, and P05 artifacts, metadata, source RTL, formal logs, witnesses, run manifests, accepted archives, checksums, and historical reports are not rewritten, migrated, or relabelled by this amendment.
- Existing P02/P05 results remain usable only within the exact technical assumptions, tested revisions, and limitations already stated in their own evidence records and approvals. This amendment does not broaden or independently revalidate those claims.
- P01 remains a C1 deterministic control. Its retained formal result applies only to the documented effective tested source (pinned base revision plus the retained path-only SBY patch); it does not establish independent certification or ambiguity.
- P01 Golden Template remains **NOT FROZEN** until the applicable T08 work and explicit freeze record are completed.
- No independent certification, human-plausibility result, benchmark-wide validity, or scored-experiment authorization is created here.

## 5. Date and provenance disclosure

The guide record's student record date is 2026-10-08. The actual professor meeting/approval date is not supplied in the accessible project record and remains unknown. No date is inferred, reconstructed, or backdated. The author approval of AM-003 is dated 2026-10-31 and is the only approval date asserted by this amendment.

## 6. Validation and preservation requirements

Before closing the T08 template-freeze work:

- verify the P01 accepted archive and registered checksum;
- verify P01 package/source fingerprints against the retained manifest;
- complete or explicitly disposition the outstanding annotation workflow and clean-reproduction requirements;
- validate the reusable template and its case-generation/runner behavior;
- record a dated freeze decision with exact source/version hashes;
- verify that P01/P02/P05 historical evidence remains byte-identical and that no prior result has been retrospectively promoted.

The approval operation for AM-003 is documentation-only. It does not itself execute these validations.

## 7. Approval

**Disposition:** ACCEPT — D9 Option B  
**Author:** G. Naveen  
**Date:** 2026-10-31  
**Approval evidence:** [D9 P01 freeze-gate approval record](../project-state/approvals/D9_P01_FREEZE_GATE_APPROVAL_2026-10-31.md)

**Effective baseline:** this amendment as committed on 2026-10-31. Frozen PLAN v1.0 remains unchanged; this versioned amendment is the approved change-control record under PLAN §12.
