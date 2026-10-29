# C3 — P02/P05 Linux Formal Reproduction

**Status: PASS** — independently executed on Linux; run-03 output packages, regression tests and the validation report are retained in the linked workflow artifact.  
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

## Verified execution result

**PASS:** [GitHub Actions run #2](https://github.com/Kumar62812/neewan_1/actions/runs/40809992594), tested commit 78e67788ade02881bef5c3321f385c03ea9579b8.

- Environment: Ubuntu Linux x86_64, Python 3.12.15, pinned Yosys 0.63 and Z3 4.15.4.
- P02 runner exit code: 0. Reference BMC, induction and cover PASS; wrong-reset and asynchronous-reset negative controls produced the required FAIL outcomes.
- P05 runner exit code: 0. Reference BMC, induction and cover PASS; equality BMC produced the required FAIL with a behavioral distinction.
- Validation: **22/22 checks passed**, including manifest inventories/digests, both case result vectors, environment/tool versions, runner exit codes, and **19/19 current/run-03/run-02 source snapshot pairs byte-identical**.
- Regression tests: C3 validator **4/4 passed**. C2 preflight source/evidence validation and its **4/4 tests** also passed.
- Raw logs, SMT models, witnesses, environment records, manifests and reports: [download the C3 run artifact](https://github.com/Kumar62812/neewan_1/actions/runs/40809992594/artifacts/12870250852).
- Artifact metadata: ID 12870250852; 90,300 bytes; SHA-256 8f3c0242f376c04ba83d47801e23ce2dc3258cd87f07c8d6462879c4cf887977; expires 2027-01-27 03:03:56 UTC.
- Durable summary record: [C3_P02_P05_LINUX_REPRODUCTION_v1.json](evidence/C3_P02_P05_LINUX_REPRODUCTION_v1.json).

## CI correction history

The first workflow attempt (run [#1](https://github.com/Kumar62812/neewan_1/actions/runs/40809905373)) executed both case runners successfully and the same 22-check validator passed, but the job was marked failed because the regression test imported the validator from the wrong directory. The import path was corrected in commit 78e67788ade02881bef5c3321f385c03ea9579b8 and the complete workflow was rerun successfully as run #2. The initial attempt remains in Actions history; it was not relabeled as a pass.

## Remaining boundaries

C3 establishes Linux reproducibility for these two existing cases under the registered model. C3 itself did not auto-close T06; the separate author approval is recorded at [T06 approval](../project-sequence/approvals/T06_P02_CLOSURE_REVIEW_v1_APPROVAL_2026-10-29.md). C3 itself also did not resolve the P05 reviewer-form identity boundary; that was handled separately in [C4](C4_P05_REVIEW_INPUT_PROVENANCE.md), which pins the current prospective form and preserves the historical run-02 snapshot as distinct. Human reviews remain blocked until full technical completion; no ambiguity certification or LLM-performance claim is made.
