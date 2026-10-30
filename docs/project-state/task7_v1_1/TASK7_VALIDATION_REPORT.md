# TASK7_VALIDATION_REPORT — FAR-T7-PROTOCOL-v1.1 freeze candidate (Phase 7)

**Label: NON-SCORED.** All results below come from synthetic fixtures and a local fixture server; no model was called. No Task 7 scored trial exists. Machine-readable results are in `TASK7_TEST_RESULTS.json`.

## 1. Summary

| Suite | Run 1 | Run 2 | Identical | What it establishes |
|---|---|---|---|---|
| Oracle v2 regression (`tests/test_oracle_v2.py`) | 15/15 | 15/15 | byte-identical | ORACLE-T7-v2 extraction, classes, precedence, disclosure rules on the 75-item development corpus |
| Execution policy (`tests/test_execution_policy.py`, E01–E16) | 16/16 | 16/16 | byte-identical | T7-EXEC-POLICY-v1, covered in §2 |
| Analysis SAP v1.1 (`tests/test_analysis_v11.py`, A01–A08) | 8/8 | 8/8 | byte-identical | variant-B confirmatory family, missing-response sensitivity, variant-A behaviour and historical-comparison guards, all independently re-derived |
| Task 6 adapter (`tests/test_task6_adapter.py`, D01–D07) | 7/7 | 7/7 | byte-identical | read-only, hash-gated, schema/count validation (TASK6_BASELINE_ADAPTER_REPORT.md) |
| Held-out tooling (`tests/test_heldout_probe.py`, H01–H07) | 7/7 | 7/7 | byte-identical | turn-1-only collection, resume, blind sheet, scoring criteria, auth refusal |
| Oracle validation O1–O8 | 8/8 | — | — | oracle config and answer texts against PT-v1 and the requirement repo |
| Trial plans M1–M9 | 15/15 | — | — | variants A (220) and B (320); A identical to v1.0; B a superset of A; Stage-2 plan (16) |
| Fixture pipeline suite: 20 synthetic trials, tests A–O + CR + VARIANT_B_ANALYSIS + STATE_MACHINE | 18/18 tests | 18/18 tests | records and analysis identical (test P) | end-to-end generation → oracle → formal evaluation (Yosys 0.63 / Z3 4.15.4) → records → analysis → transcript validation → credential scan |
| Protocol validation V01–V19 | 19/19 | — | — | the aggregate checks in §3 |

**Totals: 95/95 numbered checks, plus 18/18 fixture-suite tests in each of two runs. Every repeated suite produced identical results.**

## 2. API reliability (Phase 4): requirement → evidence

| Requirement | Test(s) | Result |
|---|---|---|
| Authentication preflight; refuse before any trial | E01 (401 on preflight → exit 3, zero POSTs, no trial directory), H07 | PASS |
| Stop on 401 without consuming scored trials | E02 (mid-run 401 → AUTH_HALT, trial pending, resume completes with byte-identical payload and a `POLICY_RESUME after AUTH_HALT` note) | PASS |
| Bounded HTTP 429 waiting using `retry-after` | E03 (waits exactly 7 s, identical resend), E04 (retry-after above the 900 s cap → QUOTA_HALT, pending), E05 (total-wait cap 3,600 s per turn) | PASS |
| Quota-aware pause and resume | E07 (RPD → QUOTA_HALT before sending), E08 (RPM pacing waits logged), E16 (413 → QUOTA_HALT) | PASS |
| Edge / proxy denial never consumes a trial | E15 (403 → ACCESS_HALT exit 6, no retry, pending, resume completes) | PASS |
| Budget and request accounting | E06 (BUDGET_HALT before an over-budget request), E13 (server POSTs = ledger lines = attempt records across halt and resume) | PASS |
| Duplicate-completion prevention | E09 (run lock; stale-lock refusal; a stored response is never re-requested), E10 (tampered stored request → refused), fixture tests I5/I6 (DEVIATION_RESENT), J (rerun sends 0 requests) | PASS |
| Task 6 rule retained for genuine server errors | E11 (5xx ×3 → API_FAILURE), E12 (400 → API_FAILURE, no retry) | PASS |
| Close-out only by explicit command | E14 (`--close-out` → API_FAILURE_UNSENT) | PASS |
| Deterministic retry/resume regression | every E-test twice, byte-identical result files | PASS |

## 3. Protocol validation V01–V19 (`validation/protocol_validation_t7.json`)

| ID | Check | Result |
|---|---|---|
| V01–V03 | interactive prompts: no leakage; REQUIREMENT and PORTS byte-identical to Task 6 R; distinct from S_k; one prompt per case for IQ_I1/IQ_I2 | PASS |
| V04, V05 | oracle validation O1–O8; trial plans M1–M9 | PASS |
| V06–V08 | fixture suites run 1 and 2 all pass; two runs identical | PASS |
| V09 | scored safeguards: refuses without approvals; rehearsal refuses FAR7 plans; overrides refused in scored mode; `--plan` required; nothing written | PASS |
| V10 | dry runs: A = 220, B = 320 fresh `[system, user]` requests with unique seeds; the 100 CR requests carry the Task 6 R prompt; nothing sent | PASS |
| V11 | no baseline → no historical tables; different model → CROSS_MODEL; historical comparisons never carry a test statistic | PASS |
| V12 | analysis structure: T7-F1 vs concurrent CR, Holm, bounded pairs non-estimable, P02 outside, asked-vs-not labelled non-causal, sensitivity for every tested contrast | PASS |
| V13 | blinded review set carries no condition (incl. CR), ID, provider or model labels | PASS |
| V14 | freeze manifest and Task 5 dependencies verify | PASS |
| V15 | T7-F1 statistics independently re-derived (recount, quadratic Wilson, exact rational Fisher, Newcombe) | PASS |
| V16 | CR prompts byte-identical to the Task 6 R prompts, re-hashed from the Task 5 sources (5/5) | PASS |
| V17 | interactive prompts byte-identical to the v1.0 package | PASS |
| V18 | unit suites pass (oracle 15, policy 16, analysis 8, adapter 7) | PASS |
| V19 | with every gate APPROVED in a throw-away copy, scored mode still refuses on null quota/budget, on a plan that is not the approved variant's, and on a non-FAR7 plan | PASS |

## 4. Formal evaluator integration and Task 6 baseline (Phase 5)

- **Evaluator identity.** The evaluator is the Task 6 one (DEP hashes equal: fabeval `05a7f67c…`, fabench `e92e348b…`, eval_config `9b8f24a3…`).
- **CR fixture trials.** These are evaluated with `--prompt-type R`, with both contracts scored (CR1 → I2_ONLY, CR2 → I1_ONLY), and enter the variant-B analysis.
- **Adapter.** The Task 6 adapter is validated on synthetic data only. Validation on the real data is **BLOCKED** (files not provided); see TASK6_BASELINE_ADAPTER_REPORT.md.

## 5. Not executed: requires the author (BLOCKED, not failed)

| Item | Why it cannot run here | Prepared |
|---|---|---|
| Held-out oracle validation on real model questions | needs the API key, the Mac, and blind human labels | `tools/heldout_question_probe.py`, `protocol/HELDOUT_LABELLING_INSTRUCTIONS.md`, `tools/mac_nonscored_kit.sh heldout`; criteria H1–H5 pre-registered |
| Stage-2 real-API rehearsal (16 SYN7-REAL trials) | needs the API key and the Mac | `tools/mac_nonscored_kit.sh stage2`; kit tested end-to-end against the local fixture server (held-out 12 probes, Stage-2 16 trials, credential scan, zip) |
| Task 6 baseline validation on real data | approved `trials.jsonl` / `analysis.json` not provided | adapter command in TASK6_BASELINE_ADAPTER_REPORT.md §4 |

## 6. Integrity of prior work

- **Content hashes** of `/home/claude/task7` (v1.0), `task5`, `task6`, `task6_closure` and `task7_out` were recorded before Phase 3 and re-checked at the end (`validation/prior_work_hashes_{before,after}.txt`). They are identical.
- **Approved Phase 1–2 files.** The oracle files (`tools/oracle.py`, `config/clarification_oracles.json`) and all interactive prompts are byte-identical to the Phase 1–2 package.

## 7. Reproduce

```
bash tools/run_all_t7_tests.sh 1
bash tools/run_all_t7_tests.sh 2
python3 tools/run_fixture_suite.py --compare validation/suite_run1 validation/suite_run2
bash tools/write_t7_sums.sh
python3 tools/validate_protocol_t7.py --suite1 validation/suite_run1 --suite2 validation/suite_run2 --out validation/protocol_validation_t7.json
```
