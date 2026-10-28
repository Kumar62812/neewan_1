# B1 — P01 Golden Benchmark Package Readiness Audit

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Baseline inspected:** `a2cb0923d114eb3f80e14884965e6251e5839be9`  
**Status:** B1 technical documentation/indexing completed; final template freeze is not claimed.

## 1. Objective

Make the P01 golden mux control package navigable and audit its existing source-to-evidence chain without rewriting accepted formal evidence, the frozen plan, case RTL, or existing result records.

## 2. Verified source inventory

The inventory below is grounded in the repository tree and the file objects inspected at the baseline commit. The identifiers in the last column are Git blob object IDs (not SHA-256 digests of the file bytes).

| Role | Path | Git blob ID |
|---|---|---|
| Requirement | `Files/Research_Papers/benchmark/pilot_v0_1/P01/requirement.md` | `ae8b409b4718ed67c76325f5e4ec0ddac9b297fc` |
| Interpretation | `Files/Research_Papers/benchmark/pilot_v0_1/P01/interpretations/interpretation_01.md` | `35963b1bfb8b710d3bbf15f1bb570addd164dc77` |
| Behavioral specification | `Files/Research_Papers/benchmark/pilot_v0_1/P01/behavioral_specification/specification_01.md` | `6795b105e034915855e808e0637014f7bd10873d` |
| Positive reference RTL | `Files/Research_Papers/benchmark/pilot_v0_1/P01/reference_rtl/rtl_01.sv` | `e0eae8f83d93680e220b86031e0bb6d22ff00b92` |
| Negative-control RTL | `Files/Research_Papers/benchmark/pilot_v0_1/P01/validation_rtl/deliberately_wrong_rtl.sv` | `e9ba4a6bb05402437d5d91f28e3da9ed1272cd45` |
| Shared property module | `Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/properties/mux2to1_properties.sv` | `caf96911983214d80ad828a94c217d37a0bb079d` |
| Reference harness | `Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/harness_reference.sv` | `dd699240e63b538197ad134500defdb149a2b371` |
| Negative harness | `Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/harness_wrong.sv` | `1b9a99f19940bc7d131ba9d0e74d4ad7aa219ed1` |
| Reference SBY config | `Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/reference.sby` | `141d45a02e4bd36600429b84302b3da0964fcaf4` |
| Negative SBY config | `Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/wrong.sby` | `3928adab6713701c8606bfe2c358be088d577302` |
| Runner | `Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/run_p01_formal.sh` | `a9d42b052f400e7de32f07966dddf6f45abb1be8` |
| Pre-RTL review | `Files/Research_Papers/benchmark/pilot_v0_1/P01/review/pre_rtl_review.md` | `c5a9dae7df498ea918acd72228df33b33f4605a6` |
| Formal result summary | `02_CERTIFICATION/P01_FORMAL_RESULTS.md` | `e4a8c1e74de5bbc768a7f2b73590289cd11d72c4` |
| Traceability matrix | `02_CERTIFICATION/P01_TRACEABILITY_MATRIX.md` | `6ed4ef2fb4ca7e67f4f2babacecd62ed49ce527d` |
| Provenance register | `docs/provenance/p01-evidence-register.md` | `dfb0da1b35070a918f585adefcf55fd553fcfd2d` |

## 3. Behavioral and formal consistency

The requirement, interpretation and specification all express the same Boolean contract: `y = a` when `sel = 0`; `y = b` when `sel = 1`. The reference RTL implements this rule. The negative control intentionally swaps the selected inputs and is expected to violate the shared property.

Both harnesses instantiate the same property module and declare no additional input assumptions. The formal configs record BMC depth 1 with `smtbmc z3`, with reference expected PASS and negative control expected FAIL. The repository result summary records the reported PASS/FAIL and a distinguishing assignment. This audit inspected source and records but did **not** execute the runner or independently reproduce the formal run.

## 4. Accepted evidence and limits

The provenance register records:
- base revision `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`;
- path-only patch SHA-256 `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`;
- accepted archive `re/p01-20260930T220622Z-rev1.tar.gz`;
- archive SHA-256 `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`.

The active SBY configurations remain source files with their current tracked contents. Do not assume that a new run recreates the accepted run without revalidating the path-only patch/staging behavior. The accepted archive must remain byte-identical and unchanged.

## 5. Readiness matrix

| Gate/check | Result | Basis |
|---|---|---|
| R → I → S consistency | PASS (documented review) | P01 pre-RTL review and source inspection |
| Reference RTL present | PASS (presence/source inspection) | `reference_rtl/rtl_01.sv` |
| Deliberately wrong RTL present | PASS (presence/source inspection) | `validation_rtl/deliberately_wrong_rtl.sv` |
| Common formal contract/harness | PASS (source inspection) | Shared properties instantiated by both harnesses |
| Reported formal result | PRESENT | `P01_FORMAL_RESULTS.md` and provenance register |
| Independent fresh reproduction | NOT PERFORMED in this task | Runner not executed here |
| Human/independent certification | NOT ESTABLISHED | Current certification status record |
| P01 Golden Template freeze | NOT FROZEN | `02_CERTIFICATION/00_STATUS.md` and project logs |
| Metadata aligned to approved D2/D14 decisions | BLOCKED / PENDING | D2/D14 and AM-002/AM-004 remain pending |

## 6. B1 work completed

- [x] Created a root-level P01 README that explains the contract, source paths, evidence lineage and freeze boundary.
- [x] Recorded a verifiable source inventory using Git blob IDs.
- [x] Checked the reference and negative control against the same stated property.
- [x] Preserved the accepted archive, existing source RTL, formal logs, witness traces, and frozen protocols.
- [x] Recorded the limits: no independent re-run, no independent certification, no template freeze.
- [x] Added this audit to the project log.

**B1 result:** The P01 control package is now easier to navigate and trace. This does not close the certification gate or authorize a P01 freeze tag.
