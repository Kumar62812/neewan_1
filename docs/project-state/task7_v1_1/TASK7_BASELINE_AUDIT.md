# TASK7_BASELINE_AUDIT — Phase 1 reconciliation (FORMAL-AMBIG-RTL Task 7)

| Field | Value |
|---|---|
| Date | 2026-10-30 |
| Prepared by | Claude, for G Naveen (Naveen Gugulothu), @Kumar62812 |
| Inputs audited | <ul><li>Task 7 Stage-1 package FAR-T7-PROTOCOL-v1.0 (`/home/claude/task7`, manifest `769f6335…73d2`; evidence zip `331d3944…3028`)</li><li>Task 6 final evidence report v3 (`8fbea454…`)</li><li>Task 21 supervisor package (`ba13a8ed…`)</li><li>Task 6 governance closure package (`85a60c3d…`)</li></ul> |
| Workstream | New, separately versioned: `/home/claude/task7_v1_1` (**FAR-T7-PROTOCOL-v1.1**). The v1.0 tree is preserved byte-for-byte (content hash `00e344ba…172d` before and after). |
| Scored trials | **0.** Task 7 scored execution is not authorised. |

## 1. Existing artefacts (v1.0, preserved) and their status

| Artefact | SHA-256 (v1.0) | Status |
|---|---|---|
| `protocol/INTERACTIVE_CLARIFICATION_PROTOCOL.md` | `700b4681…fc1d` | Complete design; reused. To be revised in Phase 3/8 for v1.1. |
| `protocol/INTERACTIVE_STATISTICAL_ANALYSIS_PLAN.md` | `c44d2f2b…5998` | Draft SAP; needs the Phase 6 additions (concurrent-control decision, missing-response sensitivity, Task 6 window) |
| `protocol/INTERACTIVE_TRIAL_PLAN.json` | `a404a819…1d35f` | 220 trials, valid; regenerated for v1.1 (version field only; IDs and seeds unchanged) |
| `protocol/PROMPT_TEMPLATES_T7.md` and `prompts/rendered/*_IQ.txt` | `bd57d133…` | Complete; prompt bytes **unchanged** in v1.1 |
| `config/clarification_oracles.json` (ORACLE-T7-v1) | `427de7a0…047d` | **Defective** (Phase 2); superseded by ORACLE-T7-v2 |
| `tools/oracle.py` (v1) | `d5133292…88da54888` | **Defective** (Phase 2); superseded |
| `tools/generate_interactive.py` | `3366ebb6…` | State machine complete. **API reliability gaps** (§3). |
| `tools/evaluate_interactive.py`, `build_interactive_records.py`, `analyze_interactive.py` | see manifest | Complete. The Task 6 baseline adapter is unverified (§3). |
| `tools/validate_*.py`, `run_fixture_suite.py`, `fixture_server.py`, `build_review_set.py`, `package_evidence.py`, `verify_freeze.py` | see manifest | Complete; reused |
| `INTERACTIVE_VALIDATION_REPORT.md` | `acd115c3…02f9` | v1.0 evidence: 15/15, 8/8, 8/8, Tests A–P twice. Superseded by the v1.1 validation in Phase 7. |
| `protocol/T7_AUTHOR_APPROVAL_TEMPLATE.json` | `f567cb74…2318` | 12 gates, all PENDING |

## 2. Implemented functionality (reusable as is)

| Function | Evidence |
|---|---|
| Interactive prompt. REQUIREMENT and PORTS are byte-identical to Task 6 R. One prompt per case, shared by IQ_I1 and IQ_I2. No leakage. | V01–V03 |
| Multi-turn state machine: one clarification round, at most two turns, no fabricated turns, the repeated-question rule, per-turn resume | Tests C, F, I, J; validate_transcripts T1–T6 |
| Per-attempt logging: timestamps, HTTP status, latency, rate-limit headers. Explicit project User-Agent (fixes the Task 6 HTTP 403 / 1010 inside the hashed client). | `generate_interactive.py` |
| Trial plan: 220 trials (11 cells × 20), seeds 700001–700220, interleaved order (seed 20261030), disjoint from Task 6 | M1–M8 |
| Formal evaluation through the unchanged fabeval 1.0.1; contract and equivalence classes kept separate; bounded-only stays INCONCLUSIVE | Tests D2, H; V15 |
| Records, analysis (families T7-F1 and T7-F2, Holm), comparability guard (NOT_AVAILABLE / CROSS_MODEL) | V11, V12 |
| Blinded review set; credential scan; freeze verification | V13, Test O, V14 |

## 3. Known defects and gaps

| # | Area | Defect / gap | Disposition |
|---|---|---|---|
| K1 | Oracle | Over-broad matching disclosed the interpretation for 17 of 44 non-target questions (P03, P04, P05, P06, P08). Extraction split at `.`. No compound handling. "go" verb anchored P06. | **Fixed in Phase 2** (ORACLE-T7-v2; defects D1–D10) |
| K2 | API | Retry policy copied from Task 6. HTTP 401 → immediate API_FAILURE. HTTP 429 → 2 retries (30 s, 120 s), then API_FAILURE. No quota pacing, no authentication preflight, no budget guard. This would reproduce Task 6's 88 × 401 and 37 × 429 losses. | Phase 4 (open) |
| K3 | Quota | Actual Groq plan, limits and budget for Task 7 are unknown. Up to 440 model turns plus retries are needed. The free-tier TPD of 200K is very likely insufficient for one day. | Phase 4 + Task 21 budget subject (open) |
| K4 | Baseline | `analyze_interactive.py` expects Task 6 records in the frozen `build_records.py` schema. The approved Task 6 outputs (`trials.jsonl` `318841ed…`) were produced by the author's evaluation run; schema compatibility is not verified here. | Phase 5/6 (open; needs the Task 6 files) |
| K5 | Design | Task 6 ran in a separate window with 39.1 % API failure. A historical comparison cannot support a causal claim. The concurrent single-shot R arm is still undecided. | Phase 6 (open; recommendation pending the SAP update) |
| K6 | Validation | The oracle corpus and the rules were written by the same party; no held-out question set exists. | OI-2: non-scored, model-generated held-out questions plus blind labelling |
| K7 | Execution | The Stage-2 non-scored real-API rehearsal (11 SYN7-REAL trials) has not been run. | Phase 7 (needs the author's Mac and key) |
| K8 | Governance | Task 21 prospective subjects (model matrix, conditions, repetitions, budget/quota) have no supervisor disposition. T7 gates are PENDING. The T6 prerequisite gates must be recorded by the author: Task 6 technical evidence is now author-approved. | Phase 8 |

## 4. Reusable Task 6 components

| Component | Identity |
|---|---|
| Formal evaluator `fabeval.py` 1.0.1, runner `fabench.py` 1.1.0, `eval_config_v1.json` | `05a7f67c…`, `e92e348b…`, `9b8f24a3…` (pinned as DEP lines) |
| Statistics routines `analyze.py` (Wilson / Newcombe / Fisher / Holm) | `15753f8e…` (Task 5) |
| Independent re-derivation `verify_independent.py` (quadratic Wilson, exact rational Fisher) | `8333ae53…` (Task 6 pipeline) |
| Interpretation contracts, case files, PT-v1 clarification texts (G2) | Task 5 bench; `clarifications_v1.json` `69f2ae48…` |
| Freeze, manifest and frozen-evidence check tooling | `frozen_check.sh`, `write_*_sums.sh` |
| Lessons from Task 6 | The User-Agent fix; the rate-limit risk; separate handling of authentication failures; a recorded freeze chronology |

## 5. Remaining development work

| Phase | Work | Blocking inputs |
|---|---|---|
| 3 | Finalise conditions and protocol text for v1.1 (behaviour already specified; update documents for ORACLE-T7-v2) | none |
| 4 | Implement and validate a prospective API policy: authentication preflight and stop-on-401, bounded 429 waiting with `retry-after`, quota pause/resume without consuming trials, budget guard | Provider plan and limits; budget (author / Task 21) |
| 5 | Task 6 baseline adapter and integration test against the approved Task 6 records | Task 6 `trials.jsonl` / `analysis.json` files |
| 6 | Finalise the SAP: concurrent-control decision, missing-response sensitivity, cross-window limits | Author decision on the concurrent arm |
| 7 | Validation: unit, oracle, leakage, plan, hashes, evaluator, resume, plus the non-scored real-API probe and Stage-2 rehearsal and the held-out oracle set | Author's Mac and key |
| 8 | Consolidated freeze candidate and one author freeze decision; Task 21 prospective items listed separately | Phases 3–7 |
