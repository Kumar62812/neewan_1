# D4 — MISINTERPRET Policy Implementation and Verification

**Project:** FORMAL-AMBIG-RTL  
**Prepared:** 2026-10-29  
**Branch:** `research/end-to-end-sequence`  
**Status:** AUTHOR ACCEPTED — POLICY HELPER CI-PASS — PRODUCTION INTEGRATION BLOCKED BY D5  
**Normative basis:** Frozen plan §11; A3 D4  
**Related dependency:** D5 comparison-relation decision remains pending

## 1. Rule implemented

Frozen plan §11 restricts `MISINTERPRET` to a generated design that is valid, formally evaluable, and separately classified as `M` under the declared comparison contract. Syntax/compile failures, missing output, and inconclusive formal checks must not be converted into misinterpretations.

The new fail-closed policy helper returns `MISINTERPRET` only if all of these are explicit:
1. A completed response was received.
2. RTL was extracted.
3. No D3 technical-failure label is present.
4. Compilation status is `pass`.
5. The formal comparison is explicitly marked complete.
6. A separate behavioral class in A/B/AB/M is supplied and equals `M`.
7. A non-empty comparison-contract reference is supplied.
8. That comparison contract is explicitly approved.

Any missing or contradictory prerequisite returns no `MISINTERPRET` label and a reason. The function does not classify ASK/ASSUME, infer M from an exit code, or itself decide A/B/AB/M.

## 2. Code and tests

- [Policy helper](../../tools/llm_eval/misinterpret_policy.py)
- [Offline regression tests](../../tools/llm_eval/test_misinterpret_policy.py)
- [GitHub Actions workflow](../../.github/workflows/d4-misinterpret-policy.yml)

Twenty-one tests cover the positive valid-class-M gate and fail-closed behavior for A/B/AB, missing class, D3 technical failures, missing/truncated output, timeout/provider failure, compile failure/not-run, incomplete formal comparison, missing/unapproved contract, unknown class/status, and fixture-only generation. Test contracts are synthetic `fixture://` data; they do not stand in for an approved research comparison contract.

## 3. Important D5 boundary

D5 has not chosen between equivalence, contract conformance, or both. This D4 helper therefore **does not nominate a comparison relation**. It requires a contract reference and an explicit approval input, so the current pending D5 decision prevents production scoring from treating any current contract as approved by implication.

The approved D3 runner itself has not been modified by this D4 addition, preserving the exact D3-approved source version. This D4 artifact is a standalone policy gate; connection to a complete A/B/AB/M evaluator awaits a versioned D5 decision and integration test. Do not call the whole evaluator production-ready from this helper alone.

## 4. Verified CI evidence

The D4 workflow completed successfully on the exact implementation commit `1c6269d3d107d8bbdd225d459390e17cfac588f3`. Python 3.12.15 `py_compile` passed and the unit-test log reports **Ran 21 tests; OK**. All 21 tests passed, with zero failures and zero skips. See [workflow run 40824632602](https://github.com/Kumar62812/neewan_1/actions/runs/40824632602) and [machine-readable evidence](evidence/D4_MISINTERPRET_POLICY_RUN_40824632602.json).

## 5. Evidence boundary

- No model calls, scored experiments, real RTL formal runs, or human reviews were run.
- No P01/P02/P05 metadata, RTL, formal evidence, counterexamples, historical logs or run manifests were changed.
- The policy test's positive example is explicitly synthetic; no case or contract is certified.
- **Verified CI:** [GitHub Actions run 40824632602 — PASS](https://github.com/Kumar62812/neewan_1/actions/runs/40824632602). Python 3.12.15; syntax compilation passed; all 21 offline regression tests passed (0 failed, 0 skipped). [Machine-readable run evidence](evidence/D4_MISINTERPRET_POLICY_RUN_40824632602.json).
- **Author disposition: ACCEPT (2026-10-31).** See [dated approval record](approvals/D4_MISINTERPRET_POLICY_APPROVAL_2026-10-31.md) and the updated [A3 author decision form](A3_AUTHOR_DECISION_FORM.md). Acceptance covers the exact standalone helper implementation and preserves frozen PLAN §11. D5 and Gate 4 remain separate open decisions; production integration is not approved by this record.
