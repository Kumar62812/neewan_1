# TASK7_FREEZE_CANDIDATE — FAR-T7-PROTOCOL-v1.1 (Phase 8, consolidated)

| Field | Value |
|---|---|
| Status | **FREEZE CANDIDATE: not frozen and not approved.** No Task 7 scored trial exists. Scored mode refuses until §11 is completed. |
| Author | G Naveen (Naveen Gugulothu), @Kumar62812 |
| Prepared | 2026-10-30 by Claude. Supervisor approval is neither claimed nor implied. |
| Manifest | `protocol/INTERACTIVE_SHA256SUMS_PROTOCOL.txt`, 56 files plus 8 Task 5 DEP lines. This candidate's manifest SHA-256 is **`4c505bff209b40f377b3c7ac84663576a8ccce207010f29d0cb60222e3e077f8`**. It changes once the quota and budget values are entered (§6), and the author verifies the regenerated manifest at T7-G8. |
| Repository | Not pushed. The intended location is the `research/end-to-end-sequence` branch of `Kumar62812/neewan_1`, as a separate `task7_v1_1/` directory, only on the author's instruction. |

## 1. Design (T7-G1): choose A or B

| | Variant A | **Variant B (recommended)** |
|---|---|---|
| Cells | IQ_I1, IQ_I2 for P03–P08 (5 cases); IQ_CTRL for P02 | A + CR (Task 6 R prompt) for P03–P08 |
| Trials / maximum completions | 220 / 440 | 320 / 540 |
| Plan file (SHA-256) | `INTERACTIVE_TRIAL_PLAN_A.json` `9c9d6dee…2a4eba` (identical to v1.0) | `INTERACTIVE_TRIAL_PLAN_B.json` `b031f097…39db618` |
| Confirmatory test | none | T7-F1: IQ_Ik vs CR, Holm m = 7 |
| Comparison with Task 6 | historical, descriptive | historical, descriptive, plus a drift check |

## 2. Prompts (T7-G2): unchanged

- **IQ prompts.** `prompts/rendered/P0x_IQ.txt` are byte-identical to v1.0 and to the Phase 1–2 package (V17).
- **CR prompts.** `P0x_CR.txt` are byte-identical to the Task 6 R prompts (V16).
- **Continuation instruction.** Unchanged.

## 3. Oracle (T7-G3)

- **Version.** ORACLE-T7-v2: `tools/oracle.py` `ce0c9af2…`, `config/clarification_oracles.json` `e680846e…`. These are unchanged since the Phase 1–2 package.
- **Specification.** ORACLE_POLICY_SPEC_v2.md.
- **Development validation.** 15/15, twice.
- **Held-out validation (pending, B4).** Criteria H1–H5 are pre-registered in `tools/heldout_question_probe.py`. T7-G3 can be approved only with a PASSED held-out score.

## 4. State machine (T7-G4)

Protocol §5:
- one clarification round, at most 2 turns per trial;
- a repeated question is never answered;
- RTL together with a question is evaluated, not answered;
- no fabricated turns;
- CR trials are single-shot.

## 5. Model, sampling and execution policy (T7-G5)

- **Model and sampling.** Groq `openai/gpt-oss-120b` with the Task 6 sampling settings (temperature 1.0, top_p 1.0, reasoning_effort medium, max_completion_tokens 8192).
- **Seeds.** 700001–700320; the same seed is used on both turns.
- **Order seed.** 20261030.
- **User-Agent.** The project User-Agent.
- **Execution policy.** T7-EXEC-POLICY-v1 (protocol §7):
  - preflight;
  - 401 → AUTH_HALT, 403 → ACCESS_HALT, 413 → QUOTA_HALT, each leaving the trial pending;
  - bounded 429 waits (single wait ≤ 900 s, total ≤ 3,600 s per turn);
  - RPM/TPM pacing; RPD/TPD → QUOTA_HALT; budget → BUDGET_HALT;
  - lock, ledger and payload verification on resume;
  - close-out only by explicit command.

## 6. Quota and budget: values to enter, with feasibility

**Enter** `execution_policy.quota` = {rpm, rpd, tpm, tpd} from your Groq limits page, and `execution_policy.budget` = {max_requests, max_total_tokens}. Then run `bash tools/write_t7_sums.sh`.

**Feasibility.** The table uses the free-tier figures (RPM 30, RPD 1,000, TPM 8,000, TPD 200,000). T is the mean tokens per request (prompt + completion); it is unknown until Stage 2 measures it.

| T (tokens/request) | Variant A tokens (440 completions) | A: minimum UTC days at TPD 200K | Variant B tokens (540) | B: minimum UTC days | Requests per minute under TPM 8K |
|---|---|---|---|---|---|
| 2,000 | 0.88 M | 5 | 1.08 M | 6 | 4 (RPM 30 not binding) |
| 4,000 | 1.76 M | 9 | 2.16 M | 11 | 2 |
| 6,000 | 2.64 M | 14 | 3.24 M | 17 | 1.3 |

- **On the free tier, TPD is the binding limit.** The run would halt with QUOTA_HALT every UTC day and resume with the same command; the policy is built for this.
- **On a paid tier,** the run is limited only by RPM/TPM.
- **Interleaving keeps the arms balanced.** Because the order mixes all cells, a multi-day run affects every cell alike. SA5 reports results by day.

**Suggested budget (author's decision).**
- `max_requests` ≈ 1.25 × maximum completions: A 550, B 675.
- `max_total_tokens` ≈ maximum completions × (1,500 + 8,192): A 4.3 M, B 5.3 M. This is an upper bound.
- Task 6 froze ≤ 2,621,440 completion tokens for 320 completions; the equivalent per-completion cap here is 8,192.

## 7. Evaluator

- **Versions.** fabeval 1.0.1, fabench 1.1.0 and eval_config_v1 are identical to Task 6 (DEP hashes).
- **Prompt types.** IQ_Ik → S_k, IQ_CTRL → R, CR → R.
- **Bounded-only specifications** stay INCONCLUSIVE (AM-008).

## 8. Statistical analysis plan (T7-G7)

SAP v1.1:
- T7-F1 is confirmatory only in variant B;
- H1/H2/DRIFT are descriptive;
- missing-response sensitivity MS1–MS6 applies, with the robustness rule (Holm-significant under ITT **and** significant under the worst case);
- SA1–SA5 apply.

**Concurrent-control evaluation:** SAP §2. **Task 6 baseline:** read only through the hash-gated adapter.

## 9. Validation evidence (Phase 7)

**95/95 numbered checks**, plus 18/18 fixture-suite tests, in each of two runs, with identical results (TASK7_VALIDATION_REPORT.md, TASK7_TEST_RESULTS.json). Prior work is unchanged (`validation/prior_work_hashes_{before,after}.txt`).

## 10. Deviations from Task 6

See TASK7_DEVIATIONS_FROM_TASK6.md (16 items). All are design properties of the new protocol. Task 6 is not amended.

## 11. Consolidated freeze decision (author; in this order)

1. **Non-scored Mac kit.** Run `bash tools/mac_nonscored_kit.sh all` (UA probe, held-out probe, Stage-2 rehearsal, pack). Label the held-out sheet blind and score it. Upload the zip and the score.
2. **Task 6 files.** Upload the approved Task 6 `trials.jsonl` and `analysis.json` for adapter validation.
3. **Configuration.** Enter the quota and budget values, then run `bash tools/write_t7_sums.sh` and `python3 tools/verify_freeze.py`.
4. **Approval file.** Copy `protocol/T7_AUTHOR_APPROVAL_TEMPLATE.json` to `protocol/T7_AUTHOR_APPROVAL.json`. Set `design_variant`. Record T6-G3, T6-G8, T6-PROBE, T6-SCORED-EVIDENCE and T7-G1…G8, each with a date and a note (the held-out score for G3, the rehearsal report for G6, the manifest SHA-256 for G8).
5. **Scored run.** Only then does `--scored` start (§12).

Task 21 supervisor items are recorded separately (template `supervisor_items_not_gates`) and are not inferred from this decision.

## 12. Execution commands

**Next command: non-scored only, on the Mac, from the unzipped `task7_v1_1/` folder.**

```
read -s GROQ_API_KEY
export GROQ_API_KEY
export T7_QUOTA='{"rpm":30,"rpd":1000,"tpm":8000,"tpd":200000}'
bash tools/mac_nonscored_kit.sh all
```

Replace the T7_QUOTA values with those on your Groq limits page. A halt (exit 3/4/5/6) is safe: run the same command again later to resume.

**Scored command: only after §11 is complete. Not to be run now.**

```
python3 tools/generate_interactive.py --scored --plan protocol/INTERACTIVE_TRIAL_PLAN_B.json --out runs/TASK7
```

Use `_A.json` if variant A is chosen. Rerun the same command after any halt.
