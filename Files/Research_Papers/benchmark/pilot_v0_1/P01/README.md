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

## Package validator and tests

- Read-only validator: [validate_p01_package.py](validate_p01_package.py)
- Regression tests: [test_validate_p01_package.py](tests/test_validate_p01_package.py)
- B2 guide: [P01 package validator](../../../../../docs/project-state/B2_P01_PACKAGE_VALIDATOR.md)
- B3 guide: [validator regression tests](../../../../../docs/project-state/B3_P01_VALIDATOR_TESTS.md)

The validator checks the pinned versioned manifest, source fingerprints, the mux contract, reference/negative RTL roles, shared property use, SBY configuration intent, and accepted archive SHA-256. Regression tests cover baseline success plus deliberate source, archive, and manifest mutations. The validator and all four tests passed in [GitHub Actions run 40752815545](https://github.com/Kumar62812/neewan_1/actions/runs/40752815545). Neither artifact independently reruns the archived formal job or certifies/freezes P01.

- Automated CI gate: [B4 validation workflow guide](../../../../../docs/project-state/B4_P01_CI_VALIDATION_GATE.md).

## Versioned manifest

- [Machine-readable P01 package manifest](p01_package_manifest_v1.json)
- [B5 manifest and provenance guide](../../../../../docs/project-state/B5_P01_VERSIONED_MANIFEST.md)

The manifest is a pinned baseline inventory, not template-freeze approval. The validator checks its pinned Git blob before evaluating source fingerprints and archive checksum.

## Verified package-validation result

**PASS:** [GitHub Actions run 40752815545](https://github.com/Kumar62812/neewan_1/actions/runs/40752815545). The read-only validator and four regression tests succeeded, and the JSON validation report was retained as a workflow artifact. The run is structural/integrity validation only; no formal RTL tools were invoked.

## Validation provenance record

- [B6 validation evidence and provenance](../../../../../docs/project-state/B6_P01_VALIDATION_EVIDENCE_RECORD.md)
- [Machine-readable CI run record](../../../../../docs/project-state/evidence/P01_CI_VALIDATION_RUN_40752919435.json)

The evidence records the exact successful CI run, tested commit, 26/26 validator checks, four regression tests, and workflow artifact expiry. This is not formal-run reproduction or template-freeze approval.

