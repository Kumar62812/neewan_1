# P01 Evidence Register and Provenance Boundary

## Current status

**Formal evidence: COMPLETE for the documented effective tested source.**

**Evidence audit/integrity: COMPLETE.**

**P01 professor/guide direction: APPROVED TO PROCEED WITH P02, according to the project owner's recorded statement.**

This register remains a provenance index, not an independent certification decision.

## Accepted formal-evidence lineage

| Item | Retained value | Interpretation |
|---|---|---|
| Pinned base revision | `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35` | Historical source revision used as the base of the tested source |
| Effective tested source | Pinned base + retained path-only SBY patch | Accepted formal result is scoped to this effective source |
| Patch SHA-256 | `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4` | Integrity identifier for the retained path-only correction |
| Accepted archive | `p01-20260930T220622Z-rev1.tar.gz` | Immutable accepted formal-evidence package |
| Archive SHA-256 | `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b` | Integrity identifier for the accepted archive |

## Scope

The accepted formal evidence concerns the declared one-bit Boolean mux contract and the effective tested source only. It does not certify linguistic ambiguity, P01 as a Golden Template, the wider benchmark, or the complete LLM methodology.

## Important repository observation

The active P01 SBY files retain the original staged-path form. The accepted execution used a retained path-only patch so that the staged SBY environment reads the staged basenames.

Therefore:

> Do not execute the current checkout and label its result as the accepted archived result without first applying and verifying the retained patch.

The unmodified pinned revision is not claimed to have passed.

## Accepted archive handling

The accepted archive is immutable. P02 work must not edit, rename, replace, extract-over, recompress, or otherwise alter it.

## P02 authorization boundary

The project owner has recorded professor approval to proceed with P02. This authorizes the next research construction stage; it does not retroactively alter P01 evidence or imply an independent certification signature.

Approval metadata that has not been supplied is intentionally left unrecorded rather than invented.
