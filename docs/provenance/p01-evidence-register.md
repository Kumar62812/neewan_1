# P01 Evidence Register and Provenance Boundary

## Certification status

**R ✓ → I ✓ → S ✓ → RTL ✓ → F ✓ → C: PENDING**

This register is a provenance index, not a certification decision.

## Accepted formal-evidence lineage

| Item | Retained value | Interpretation |
|---|---|---|
| Pinned base revision | `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35` | Historical source revision used as the base of the tested source |
| Effective tested source | Pinned base + retained path-only SBY patch | The accepted formal result is scoped to this effective source |
| Patch SHA-256 | `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4` | Integrity identifier for the retained path-only correction |
| Accepted archive | `p01-20260930T220622Z-rev1.tar.gz` | Immutable accepted formal-evidence package |
| Archive SHA-256 | `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b` | Integrity identifier for the accepted archive |

## Scope

The accepted formal evidence concerns the declared one-bit Boolean mux contract and the effective tested source only. It does not certify linguistic ambiguity, P01 as a benchmark template, the wider benchmark, or the complete LLM methodology.

## Important repository observation

At the time of this curation, the active P01 SBY files in the repository still contain source paths such as `../reference_rtl/rtl_01.sv` and `../validation_rtl/deliberately_wrong_rtl.sv` in their `[script]` blocks. The retained execution record explains that the accepted run used a path-only patch so that the staged SBY environment reads the staged basenames.

Therefore:

> **Do not execute the current checkout and label its result as the accepted archived result without first applying and verifying the retained patch.**

The unmodified pinned revision is not claimed to have formally passed.

## Accepted archive handling

The accepted archive is treated as immutable. Do not unpack, edit, recompress, rename, or replace its contents as a way of “updating” the evidence. Any reproduction or extension must produce a new run/evidence identifier.

## Certification boundary

The independent certification decision is intentionally outside this register. No entry here authorizes a P01 freeze or P02–P12 construction.
