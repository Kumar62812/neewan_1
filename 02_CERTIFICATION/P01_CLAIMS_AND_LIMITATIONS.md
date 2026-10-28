# P01 Claims and Limitations

**Status:** Current review/governance record

| Claim | Status | Boundary |
|---|---|---|
| P01 reference mux satisfies the retained property | Supported | Effective tested source only |
| Deliberately swapped mux violates the retained property | Supported | Negative control, not an alternative interpretation |
| P01 formal evidence exists | Supported | Accepted rev1 archive and checksum |
| Evidence provenance is preserved | Supported | Pinned base + retained patch + archive identifiers |
| Unmodified pinned revision passed unchanged | **Not claimed** | Path-resolution defect existed in the unmodified setup |
| P01 is a certified ambiguous case | **Not claimed** | P01 is a C1 deterministic control |
| Two human-plausible P01 interpretations were validated | **Not claimed** | Wrong RTL is intentionally incorrect |
| Benchmark-wide methodology is validated | **Not claimed** | Requires later cases and validation |
| LLM ambiguity-handling performance is validated | **Not tested** | Requires later LLM evaluation |
| P01 Golden Template is frozen | **Not frozen** | Requires explicit methodology freeze decision |

## P01 formal scope

The retained result applies only to:

`6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`

plus the retained path-only SBY patch:

`71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`.

## Transition to P02

Professor approval to proceed with P02 is recorded as a project-state fact supplied by the project owner. It does not modify historical P01 evidence and does not constitute an independently signed certification dossier.

P02 artifacts must be created and checked sequentially.
