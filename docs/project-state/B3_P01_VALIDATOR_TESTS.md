# B3 — P01 Validator Regression-Test Suite

**Status:** Regression tests added. Execution requires the complete repository checkout; this connected GitHub session did not execute the suite.

## Covered tests

The standard-library unittest suite in P01's tests folder builds an isolated temporary package fixture from files in the checkout. It includes:

1. **Baseline success:** unchanged baseline source files and accepted archive should return exit code 0, emit valid JSON, and state that formal tools, certification and freeze were not performed.
2. **Source-integrity failure:** mutating reference RTL should return exit code 1 and identify the changed Git blob.
3. **Archive-integrity failure:** mutating one byte in the temporary copy of the accepted archive should return exit code 1 and flag the SHA-256 mismatch.

Each test uses a separate temporary directory. It does not change source files in the real checkout, and it does not run Yosys, SymbiYosys or Z3.

## Run command

From a complete local repository checkout:

    python3 Files/Research_Papers/benchmark/pilot_v0_1/P01/tests/test_validate_p01_package.py

## Interpretation

- Passing tests establish the validator's expected behavior on the fixture and two deliberate mutation cases.
- They do not constitute fresh formal proof or independent reproduction of the archived P01 result.
- Accepted evidence is tied to the pinned base plus the retained path-only patch. Do not run a new formal job and label it the accepted archived run.
- P01 Golden Template remains NOT FROZEN. B3 does not create an approval, certificate, release tag or metadata migration.

## Completion boundary

- [x] Regression suite added for expected-success and mutation-detection behavior.
- [x] Test mutations are confined to temporary fixture directories.
- [x] Test purpose and command documented.
- [ ] Actual suite execution and retained test log — pending execution on a complete checkout.

## Manifest-integrity regression (B5)

A fourth test mutates the manifest in its temporary fixture and requires the validator to flag the pinned manifest Git blob check. This confirms that the source of truth cannot be edited silently. The real package manifest and source files are not altered by the mutation test.

