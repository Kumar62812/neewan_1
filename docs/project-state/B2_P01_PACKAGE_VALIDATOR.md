# B2 — P01 Read-Only Package Validator

**Status:** Validator implemented. Running it on a complete local checkout is required to produce a real runtime report. No new formal run, independent review, certification, or template freeze is claimed.

## What B2 adds

The adjacent script, validate_p01_package.py, performs read-only checks on the P01 control package:

1. Confirms the required requirement, interpretation, specification, RTL, property, harness, SBY configuration and review files are present.
2. Computes Git blob object IDs for B1 baseline source files and compares them with recorded IDs. These IDs are Git SHA-1 object identifiers, not SHA-256 file digests.
3. Checks requirement, interpretation and specification consistency for the same 2:1 mux behavior.
4. Checks that the reference RTL follows the contract, the negative control swaps data selection, and both harnesses instantiate the same property module.
5. Checks that the reference configuration expects PASS and the negative configuration expects FAIL.
6. Computes SHA-256 of the accepted archive and compares it with the registered checksum.

## How to run

From a complete local repository checkout, run:

    python3 Files/Research_Papers/benchmark/pilot_v0_1/P01/validate_p01_package.py

The script prints a JSON report and exits with code 0 when checks pass, 1 when checks fail, and 2 when the repository/accepted archive cannot be located.

## Safety and interpretation

- The validator is read-only. It does not alter any tracked source, evidence package, checksum, log or witness.
- This is a structural/source-integrity check; it does not run Yosys, SymbiYosys or Z3.
- A successful validator run is not formal verification, independent reproduction, human plausibility review, ambiguity certification or approval to freeze P01.
- The result is conditional on running the script on a complete checkout. GitHub source inspection in this task does not substitute for that local execution.
- The accepted evidence applies to the pinned base plus the retained path-only patch. Do not assume a new run recreates the archived run without rechecking patch/staging behavior.
- P01 Golden Template remains NOT FROZEN. D2/D14 schema and layout decisions remain pending, so this task does not introduce case metadata or silently activate AM-002/AM-004.

## B2 completion criteria

- [x] Reusable validator source committed.
- [x] Checks cover baseline source inventory, contract consistency, shared formal property, expected positive/negative SBY configuration and accepted archive checksum.
- [x] Validator explicitly reports that formal tools, independent certification and template freeze were not performed.
- [ ] Runtime execution and JSON output from a complete checkout — not performed in this connected GitHub documentation session.

## Regression tests (added in B3)

The isolated-fixture regression suite is documented in [B3](B3_P01_VALIDATOR_TESTS.md) and implemented at [test_validate_p01_package.py](../../Files/Research_Papers/benchmark/pilot_v0_1/P01/tests/test_validate_p01_package.py). The suite is committed but was not executed by this connected GitHub operation. B2's runtime-execution checkbox therefore remains pending.

