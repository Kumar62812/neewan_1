# P01 — Golden Mux Control Case

**Case type:** Deterministic / unambiguous control  
**Design:** Combinational one-bit 2:1 multiplexer  
**Current status:** Formal evidence is recorded for the documented effective tested source; Golden Template freeze is **NOT FROZEN**.

## Behavioral contract

Inputs: `a`, `b`, `sel` (one-bit Boolean values). Output: `y`.

```text
sel = 0  =>  y = a
sel = 1  =>  y = b
y = sel ? b : a
```

The circuit is combinational: no clock, reset, storage, enable, or latency is part of the contract. The `X` entries in the behavioral-specification truth table mean Boolean don't-care values for the input not selected by `sel`; they are not SystemVerilog four-state unknowns.

## Source index

| Evidence-chain stage | Canonical path |
|---|---|
| Requirement | `requirement.md` |
| Interpretation | `interpretations/interpretation_01.md` |
| Behavioral specification | `behavioral_specification/specification_01.md` |
| Positive reference RTL | `reference_rtl/rtl_01.sv` |
| Deliberately incorrect negative control | `validation_rtl/deliberately_wrong_rtl.sv` |
| Shared property | `formal/properties/mux2to1_properties.sv` |
| Reference harness/configuration | `formal/harness_reference.sv`, `formal/reference.sby` |
| Negative-control harness/configuration | `formal/harness_wrong.sv`, `formal/wrong.sby` |
| Runner | `formal/run_p01_formal.sh` |
| Retained execution recall | `formal/evidence/p01-20260930T220622Z/P01_EXECUTION_EVIDENCE_RECALL.md` |
| Pre-RTL review | `review/pre_rtl_review.md` |

Cross-package governance evidence:
- [Formal result summary](../../../../../02_CERTIFICATION/P01_FORMAL_RESULTS.md)
- [Traceability matrix](../../../../../02_CERTIFICATION/P01_TRACEABILITY_MATRIX.md)
- [Claims and limitations](../../../../../02_CERTIFICATION/P01_CLAIMS_AND_LIMITATIONS.md)
- [Accepted evidence provenance register](../../../../../docs/provenance/p01-evidence-register.md)

## Recorded formal result and provenance boundary

The certification record reports the reference assertion as PASS and the intentionally swapped implementation as assertion FAIL, with counterexample `a=0, b=1, sel=1, required y=1, observed y=0`. The accepted result applies only to the pinned base revision plus the retained path-only SBY patch.

- Pinned base revision: `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`
- Patch SHA-256: `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`
- Accepted archive: `re/p01-20260930T220622Z-rev1.tar.gz`
- Accepted archive SHA-256: `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`

Do not treat a new run of the current checkout as the accepted archived run. The provenance register says the retained run used a path-only patch so the staged SBY environment could read staged basenames. Preserve the archive and its checksum unchanged. Record any fresh run under a separate provenance ID.

## Freeze boundary

This README is a navigation aid; it does not certify or freeze P01. The existing record still says **P01 Golden Template: NOT FROZEN**. The negative-control RTL is intentionally wrong and must not be presented as a plausible alternate interpretation. Formal inequivalence between the reference and negative control validates the checker; it does not prove ambiguity.

A case-level metadata file is not added here because the A3 decisions on canonical certification/lifecycle vocabulary (D2) and case layout (D14), with draft AM-002/AM-004, remain pending. Do not retrofit frozen sources or existing case records to pre-empt those decisions.
