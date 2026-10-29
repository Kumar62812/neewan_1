# C3 — P02/P05 Linux Formal Reproduction

**Status at setup:** PREPARED; execution must be confirmed by a completed GitHub Actions run.  
**Branch:** research/end-to-end-sequence  
**Purpose:** Independently rerun the existing P02/P05 formal suites on Linux with pinned tools, retaining fresh run-03 output without modifying historical run-01/run-02 evidence.

## Scope and controls

The workflow .github/workflows/p02-p05-formal-reproduction.yml uses Python 3.12 and installs the pins in docs/reproducibility/formal-requirements.txt. Before rerunning the cases, it executes C2's read-only historical manifest/source checks and regression tests.

The P02 and P05 runners write to isolated temporary directories named p02-run-03 and p05-run-03. Logs, SMT files, VCD/Yosys witnesses, environment/package records, run JSON and SHA-256 manifests are retained in a 90-day workflow artifact. Historical evidence folders are not overwritten or appended.

## Acceptance criteria

- P02 reference BMC, induction and cover PASS; wrong-reset and asynchronous-reset controls FAIL with expected counterexamples.
- P05 reference BMC, induction and cover PASS; the equality check FAILs with the expected behavioral distinction.
- Each new SHA256SUMS inventory is complete and every listed file hash matches.
- All 19 registered contract/formal source files are byte-identical across current sources, fresh run-03 snapshots and historical run-02 snapshots.
- The environment is Linux, Python 3.12.x, Yosys 0.63 and Z3 4.15.4; both case runners exit zero.

A FAIL from an intentional negative control is an expected result, not a failed reproduction. Unexpected outcomes, source drift, missing files, changed hashes or tool errors fail the validation.

## Claim boundaries

This task does not edit RTL, historical logs, witnesses, run manifests, archived source snapshots or approval records. Results are scoped to the documented Boolean stable-sampled-edge model. They do not establish analog timing, four-state behaviour, linguistic ambiguity, human plausibility or LLM performance.

The P05 reviewer-form version mismatch found in C2 is not treated as a formal input change because the formal runner does not consume the form. It remains a required version-freeze action before human review. C3 does not by itself close T06's pending author decisions or certify P05 ambiguity.

## Result record

The execution result and artifact link will be added only after GitHub Actions reports a completed run. Until then, C3 is PREPARED, not PASS.
