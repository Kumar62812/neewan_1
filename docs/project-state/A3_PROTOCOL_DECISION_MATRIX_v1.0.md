# A3 — Protocol Conflict Decision Matrix and Change-Control Plan

**Project:** FORMAL-AMBIG-RTL
**Version:** A3-v1.0
**Status:** DRAFT — author decisions pending
**Parent record:** [A2-v1.0](A2_RESEARCH_SCOPE_FREEZE_v1.0.md) and its [source-inconsistency register](A2_SOURCE_INCONSISTENCY_REGISTER.md)
**Date:** 2026-10-28
**Prepared at:** `research/end-to-end-sequence` head `a028d4d44e3adfcc552cb264934f36dcb31a573b`
**Companion files:** [A3 author decision form](A3_AUTHOR_DECISION_FORM.md) · [amendment template](../amendments/AMENDMENT_TEMPLATE.md)

## 1. Purpose

Turn the sixteen source inconsistencies recorded in A2 (D1–D16) into a sequenced, auditable decision plan.

A3 does not resolve methodology conflicts, amend frozen protocols, certify benchmark cases or declare experimental results. Each substantive decision needs three things: an explicit author decision, a dated record, and a versioned amendment where required.

## 2. Governing rules

1. Preserve `Files/FORMAL_AMBIG_RTL_PLAN.md` (v1.0-FROZEN). It is changed only through a separately versioned amendment under PLAN §12.
2. Do not edit historical formal evidence, accepted archives, source RTL, witnesses, run logs or evidence manifests as part of decision planning.
3. Keep five things distinct: technical verification, linguistic plausibility, ambiguity certification, author approval, and independent human review.
4. A timeout or incomplete formal check is never a proven mismatch.
5. Primary metric definitions do not change after scored outcomes have been seen.
6. A recommendation is not approval. A decision stays **PENDING** until the author records a disposition.

## 3. Evidence baseline

| Key | Path (branch / commit) | SHA-256 |
|---|---|---|
| PLAN | `Files/FORMAL_AMBIG_RTL_PLAN.md` (`a028d4d`) | `19e1fe9abc5b8e07d96a3df339d2a020eae93fee7c9b3815a30dd49d112ee305` |
| RP | `Files/Research_Papers/docs/research_protocol.md` | `87d3a6e7632bc46e75c23b7ff25ed7d84a09691bc1652865f250a04c34cfaa63` |
| BS | `Files/Research_Papers/docs/benchmark_schema.md` | `18b5e39599b519872a427c8463213f35bce0cf175e9d553bce3035028493fcac` |
| FVP | `Files/Research_Papers/docs/formal_verification_protocol.md` | `28fc904292f2332b42b536a26cbc7a522fee5736abb058563556bbbe20c9724f` |
| AP | `Files/Research_Papers/docs/annotation_protocol.md` | `333f9d352c9e1978208043ef6f3cacbb9aa859779214bb8dac14ea2b0d578183` |
| A2 | `docs/project-state/A2_RESEARCH_SCOPE_FREEZE_v1.0.md` | `028837c394267299e45ca297da9de056897fb7edd7325452078a76b194a0d53d` |
| A2-REG | `docs/project-state/A2_SOURCE_INCONSISTENCY_REGISTER.md` | `f9a1f86ae4f1d662e320dbae45a52529988e683078908613beb2d4a0cca37666` |
| EVAL | `tools/llm_eval/run_pipeline.py` (PR #7, `07a498a`) | `5fef241e48d200bdc463286414212880051d2f24a2588e8553a0b9b375bf1630` |
| EVAL-PLAN | `docs/experiments/llm_evaluation_plan_v0_1.md` (PR #7, `07a498a`) | `8886881bfd22b7840f5b664273b8cc9b1f1914e51ba4a3bc479d65635456fe54` |
| PILOT | `studies/P05-20261024-groq-v2/README.md` (PR #9, `31d3193`) | `07fe99e996363032de8b39d3f5b2f7b66ad59d299bb9fefdf6936ea8826d82a1` |
| PILOT-CSV | `studies/P05-20261024-groq-v2/results/paired_results.csv` (PR #9) | `7932d87c1a5dd26f22ded94dd5a7fd345edb7d8500bac14ab1e4e11363cd4681` |

Disposition codes: **ACCEPT** (adopt the recommendation) · **REJECT** (keep the source as-is) · **REVISE** (adopt with stated changes) · **DEFER** (postpone, with a named trigger) · **PENDING** (no decision yet).

## 4. Decisions required before T08

### D1 — Taxonomy relationship

- **Conflict:** PLAN §5 defines C1–C5 primary categories. RP §5 defines six thematic dimensions (reset, output, transition, timing, state, concurrency). No mapping exists.
- **Impact:** category-level analysis (H4) and case metadata need a single primary label.
- **Options:** (a) C1–C5 primary, RP dimensions as secondary tags; (b) RP dimensions primary; (c) maintain both as parallel primaries.
- **Recommendation:** (a). PLAN is the only frozen source, and PLAN §5 already allows "optional secondary tags".
- **Amendment needed:** yes. RP §5 changes status from taxonomy to tag vocabulary (amendment AM-001).
- **Validation:** the T08 metadata schema has one required `primary_category ∈ {C1…C5}` field and an optional `thematic_tags` list drawn from the RP §5 vocabulary.
- **Status:** PENDING_AUTHOR_DECISION.

### D2 — Certification status vocabulary

- **Conflict:** PLAN §6 statuses (`UNAMBIGUOUS`, `CERTIFIED_AMBIGUOUS`, `UNRESOLVED`, `EXCLUDED`) differ from BS §4 lifecycle labels (`candidate`, `certified_ambiguous`, `unambiguous_control`, `negative_candidate`, `inconclusive`, `frozen`). Existing records disagree too: P02 has `status: technical_verification_complete` and P05 has `status: UNRESOLVED`.
- **Options:** (a) PLAN statuses canonical in a `certification_status` field, BS stage in a separate `lifecycle_stage` field, plus a crosswalk; (b) BS labels canonical; (c) merge into one new vocabulary.
- **Recommendation:** (a).
- **Proposed crosswalk** (for approval, not in effect):

  | `lifecycle_stage` (BS) | Allowed `certification_status` (PLAN) |
  |---|---|
  | `candidate` | `UNRESOLVED` |
  | `certified_ambiguous` | `CERTIFIED_AMBIGUOUS` |
  | `unambiguous_control` | `UNAMBIGUOUS` |
  | `negative_candidate` | `EXCLUDED` with a PLAN §6 reason |
  | `inconclusive` | `UNRESOLVED` or `EXCLUDED`/`INCONCLUSIVE_FORMAL` |
  | `frozen` | a release flag, not a status; any of the above |

- **Existing records:** P01, P02 and P05 metadata are **not rewritten**. Any migration is a separately authorised task with new file versions.
- **Amendment needed:** yes, BS §4 (AM-002).
- **Validation:** a JSON schema for T08 metadata, validated against a new case and against read-only copies of P02/P05 metadata (the mismatches are reported, not fixed).
- **Status:** PENDING_AUTHOR_DECISION.

### D9 — P01 freeze gate versus work already performed

- **Conflict:** PLAN §9, §13 (Gate 2) and §14 forbid P02–P12 until the P01 golden template is frozen. P01 is **not frozen** (`governance/07_PROJECT_LOG.md`), yet P02 and P05 were built and formally verified. The recorded basis is the guide direction "Proceed with P02" (`02_CERTIFICATION/P01_GUIDE_MEETING_RECORD.md`, line 12), which was never recorded as a PLAN amendment.
- **Options:**
  - **A:** complete the P01 Gate 2 freeze before T08. Open items include the annotation workflow, the clean reproduction and the `p01_template_freeze.md` review.
  - **B:** approve a dated amendment that records the guide direction and its date, states the gate deviation openly, confirms P02/P05 evidence remains valid within its recorded scope, and moves the template-freeze function to T08.
- **Recommendation:** B. T08 is the reusable template task, so freezing P01 now would duplicate it. The amendment must not imply an approval existed before it was recorded.
- **Amendment needed:** yes, PLAN §9/§13/§14 (AM-003). The amendment records the guide-meeting date exactly as stated in the meeting record.
- **Validation:** the amendment links the guide record; P01/P02/P05 evidence hashes are unchanged before and after.
- **Status:** PENDING_AUTHOR_DECISION.

### D14 — Canonical case-template layout

- **Conflict:** PLAN §9–10 and BS §2 specify `metadata.yaml`, `interpretations/`, `behavioral_specification/`, `annotations/`, `review/` and `reference_rtl/A`, `B`. P02 and P05 use `metadata.json`, flat `P0x_*.md` files and `evidence/run-0N/`. BS §2 allows a logical rather than literal layout.
- **Options:** (a) T08 defines one canonical layout for new cases, with a path crosswalk for P01/P02/P05; (b) migrate existing cases to the PLAN layout; (c) adopt the P02/P05 layout as canonical.
- **Recommendation:** (a), choosing the P02/P05 layout (JSON metadata, immutable `evidence/run-NN/`) as the base, since it is the layout with executed, reproducible evidence.
- **Amendment needed:** yes, PLAN §10/BS §2 (AM-004), adopted together with T08.
- **Validation:** T08 runner creates a new case from the template; the crosswalk resolves every PLAN artifact for P01/P02/P05 to an existing path or records it as absent.
- **Status:** PENDING_AUTHOR_DECISION.

## 5. Decisions required before Gate 3 (certification)

### D7 — Annotation aggregation rule

- **Conflict:** AP §6 uses a 1–5 scale; AP §7 sets τ = 0.80 on "the predefined aggregation rule", which is never defined.
- **Must be fixed before any rating is analysed:** aggregation formula; how τ applies; minimum number of independent annotators; tie, disagreement and adjudication handling (AP §9); missing or invalid ratings; the agreement statistic (AP §8).
- **Options:** (a) P_X = share of eligible annotators rating interpretation X at 4 or 5, certified if P_A ≥ 0.80 and P_B ≥ 0.80; (b) mean rating rescaled to [0, 1]; (c) another rule the author specifies.
- **Recommendation:** (a). It matches the binary coding AP §6 anticipates. A minimum annotator count must be fixed with it (for example five, so that 0.80 corresponds to 4 of 5).
- **Constraint:** no annotation result is invented, and no rule is applied retrospectively. P05 currently has **0** recorded responses.
- **Amendment needed:** yes, AP §6–9 (AM-005).
- **Status:** PENDING_AUTHOR_DECISION.

### D11 — Provisional versus final classification

- **Conflict:** AP and the PR #7 evaluation plan (EVAL-PLAN lines 6, 12, 29, 70) block P05 evaluation and reporting until independent human review. Author governance schedules all independent reviews **after** 100 % technical completion.
- **Must be defined:** a provisional technical status (formal evidence only); the final certification status (all evidence in place); how unresolved plausibility affects inclusion in scored analyses.
- **Recommendation:** two separate fields. `technical_status` (for example `FORMALLY_DISTINCT`, `FORMALLY_EQUIVALENT`, `INCONCLUSIVE`) can be set now. `certification_status` stays `UNRESOLVED` until review. Scored primary analyses use only cases whose `certification_status` is final. Provisional scoring is reported as exploratory.
- **Rule:** formal distinction alone is never reported as certified ambiguity.
- **Amendment needed:** yes, AP, RP §13 and EVAL-PLAN (AM-006).
- **Status:** PENDING_AUTHOR_DECISION.

### D12 — Protocol version and freeze status

- **Conflict:** only PLAN is marked v1.0-FROZEN. RP says "pre-results freeze"; BS, FVP and AP carry no status; all PLAN Gate 1 items are unticked.
- **Options:** (a) freeze RP, BS, FVP and AP at the SHA-256 values in §3 as the operative baseline (v1.0), with later changes only by amendment; (b) record them as drafts, listing what must be approved before Gate 3.
- **Recommendation:** (a), but **after** D1, D2, D7 and D11 are decided. Freezing first and amending straight away would only add records.
- **Validation:** a baseline record listing each document, version and hash; PLAN Gate 1 items ticked only where evidence exists.
- **Status:** PENDING_AUTHOR_DECISION.

## 6. Decisions required before Gate 4 (scored experiments)

### D3 — Technical outcome labels

- **Requirement:** the evaluator distinguishes `INVALID` (technical failure), `INCOMPLETE` (content missing) and `INCONCLUSIVE` (formal check could not finish under the resource policy). None of these is a mismatch.
- **Current state (EVAL, PR #7):** **none of the three labels is emitted.**
  - Extraction produces `rtl_extracted`, `empty_response`, `clarification_requested`, `refusal` or `format_failure`.
  - Compile and formal steps produce `pass`, `fail`, `timeout` or `not_run`.
  - Formal `fail` is any non-zero exit code. A tool error is therefore **indistinguishable from a property failure**, unlike the P02 runner, which separates `FAIL` from `TOOL ERROR` and `INCONCLUSIVE`.
- **Required evidence:** unit tests with fixtures for each label: an empty response, a truncated module, a syntax error, an elaboration error, a forced timeout and a tool crash. Each must map to its own label, and none may map to `M`.
- **Status:** PENDING_IMPLEMENTATION_AND_APPROVAL.

### D4 — MISINTERPRET definition

- **Rule (PLAN §11):** `MISINTERPRET` applies only when the generated RTL is valid, formally evaluable and classified `M` under the declared comparison contract. Syntax errors, missing content and inconclusive checks are never relabelled as misinterpretation.
- **Current state (updated 2026-10-31):** a fail-closed D4 policy helper is implemented and author-accepted; [CI run 40824632602](https://github.com/Kumar62812/neewan_1/actions/runs/40824632602) passed syntax compilation and 21/21 offline regression tests. It requires valid/extracted RTL, successful compilation, explicit completed formal comparison, a separately supplied `M` behavioral class, and an explicitly approved comparison contract. It remains a standalone helper, not yet wired into the complete evaluator. D5 Option C is now approved; D4 must bind `M` to the primary equivalence classification only. The D4 positive test remains synthetic.
- **Status:** D4 policy helper CI-verified and author-accepted; production integration awaits evaluator validation. See [D4 report](D4_MISINTERPRET_POLICY.md) and [machine-readable evidence](evidence/D4_MISINTERPRET_POLICY_RUN_40824632602.json).

### D5 — A/B/AB/M comparison semantics

- **Conflict:** PLAN §11 and RP §7 define the classes by equivalence to RTL_A and RTL_B. If RTL_A and RTL_B are proven non-equivalent on the declared observables, AB cannot occur.
- **Current state (updated 2026-10-31):** the PR #9 pilot used per-interpretation contract conformance (`I1_contract.sv`, `I2_contract.sv`), not frozen-plan equivalence. Its 1 × I2_only and 2 × I1_only outputs remain exploratory and are not relabelled as primary A/B/AB/M. The author accepted Option C on 2026-10-31: equivalence remains primary under frozen PLAN §11 and RP §7; contract conformance is a separate secondary vector. See [D5 approval](approvals/D5_COMPARISON_SEMANTICS_APPROVAL_2026-10-31.md) and [AM-007](../amendments/AM-007_dual_comparison_relations.md).
- **Options:**
  - (a) Keep equivalence. AB is then reachable only when the references differ outside the observables, so on certified cases it is reported as structurally empty.
  - (b) Amend to **contract conformance**: class A means the design satisfies S_A's property set. AB then means it satisfies both contracts, which is possible when the contracts leave behaviour unconstrained. This needs an extra check that the contracts are tight (each reference fails the other's contract).
  - (c) Use both relations, with equivalence primary and conformance secondary.
- **Recommendation:** decide explicitly before Gate 4, and do not adopt (b) implicitly because the pilot used it. If (b) is chosen, the amendment states that PR #9 results were produced under a relation adopted later.
- **Amendment needed:** if (b) or (c), yes, PLAN §11/RP §7 (AM-007).
- **Status:** ACCEPTED — Option C; AM-007 approved. Implementation regression and end-to-end validation remain pending.

### D10 — Existing exploratory evaluation

- **Facts (PILOT, PR #9):**
  - It ran on 2026-10-24, before any case was certified (PLAN Gate 3), while EVAL-PLAN marked P05 evaluation **BLOCKED** pending human review.
  - It describes itself as "a descriptive pilot on one constructed case, not general model accuracy".
  - It records a post-output evaluator correction (v2.1) and supplementary checks "added after output inspection".
- **Required action:** label the pilot **EXPLORATORY** in the approval register and the PR #9 description, and exclude it from all primary metrics unless an approved protocol defines another valid use.
- **Note:** the pilot's own documentation is transparent about these points. The issue is classification, not concealment.
- **Status:** ACTION_REQUIRED_BEFORE_GATE_4.

### D13 — Operational metric definitions

The following must be predefined before any primary scored experiment, preserving the RP §8 formulas unless an amendment is approved first:

| Metric | Open question | Note |
|---|---|---|
| ADR | What counts as "correctly detected" (an ASK that names the unresolved behaviour? any ASK?) | EVAL detects clarification with a keyword regex, which is not an adequate ADR rule |
| CR | What makes an ASK "relevant" | Needs a pre-registered rubric |
| VIR | AB is not in the numerator (N_A + N_B) | Depends on D5 |
| MIR, VIR | Is N_generated all responses or only valid RTL? | INVALID/INCOMPLETE/INCONCLUSIVE treatment |
| FCR | What "formally correct" means on an ambiguous case (A, B or AB?) and on controls | Uses N_attempted, a different denominator from VIR/MIR |
| UCR | Which controls count (C1 only, or negatives too?) | P02 is now a C1 control |
| CU | Components and measurement of interaction cost | RP §8 requires this before final analysis |
| All | Confidence intervals, multiple-comparison handling, per-model/per-category breakdown, minimum trials per cell | Not in RP |

- **Amendment needed:** yes, RP §8 (AM-008), dated before the first scored run.
- **Status:** PENDING_AUTHOR_DECISION.

## 7. Documentation-only clarifications

These are already reflected in A2-v1.0 and need only an author acknowledgement. They do **not** imply that any methodology gate is approved.

| ID | Clarification | Where recorded |
|---|---|---|
| D6 | ASSUME = the system **silently** selects or states an interpretation without obtaining clarification (RP §7) | A2 §6; acknowledged by G. Naveen on 2026-10-31; [dated acknowledgement](approvals/D6_ASSUME_TERMINOLOGY_ACKNOWLEDGEMENT_2026-10-31.md) |
| D8 | The core/extension grouping is a later governance decision, not part of PLAN §7's construction order | A2 §9; acknowledged by G. Naveen on 2026-10-31; [dated acknowledgement](approvals/D8_CORE_EXTENSION_GROUPING_ACKNOWLEDGEMENT_2026-10-31.md) |
| D15 | Observation unit = (Model, Benchmark instance, Condition, Trial) (RP §11) | A2 §8; acknowledged by G. Naveen on 2026-10-31; [dated acknowledgement](approvals/D15_OBSERVATION_UNIT_ACKNOWLEDGEMENT_2026-10-31.md) |
| D16 | P02 is a deterministic C1 control within the core set, not an ambiguity case (PLAN §7; T05 decision O4) | A2 §9; acknowledged by G. Naveen on 2026-10-31; [dated acknowledgement](approvals/D16_P02_CORE_CONTROL_ACKNOWLEDGEMENT_2026-10-31.md) |

## 8. Decision register

The authoritative dispositions will be recorded in the [author decision form](A3_AUTHOR_DECISION_FORM.md). The table below is the planning state: none of the decisions has been made.

| ID | Gate | Evidence baseline | Recommendation | Disposition | Approval evidence | Amendment | Effective baseline | Validation |
|---|---|---|---|---|---|---|---|---|
| D1 | T08 | PLAN §5, RP §5 | C1–C5 primary; RP dimensions as optional secondary tags | ACCEPT — A | [D1 approval](approvals/D1_TAXONOMY_RELATIONSHIP_APPROVAL_2026-10-31.md) | [AM-001 approved](../amendments/AM-001_taxonomy_relationship.md) | 2026-10-31 | T08 schema and runner validation pending |
| D2 | T08 | PLAN §6, BS §4, P02/P05 metadata | PLAN status + separate lifecycle field + crosswalk | PENDING | — | AM-002 | — | JSON-schema validation |
| D9 | T08 | PLAN §9/13/14, guide record | Option B amendment | PENDING | — | AM-003 | — | Evidence hashes unchanged |
| D14 | T08 | PLAN §9–10, BS §2, P02/P05 trees | One layout for new cases + crosswalk | PENDING | — | AM-004 | — | Template run + crosswalk |
| D7 | Gate 3 | AP §6–9 | Share rating ≥ 4, τ = 0.80, fixed minimum n | PENDING | — | AM-005 | — | Rule fixed before any rating analysed |
| D11 | Gate 3 | AP, RP §13, EVAL-PLAN | Separate technical and certification status | PENDING | — | AM-006 | — | Metadata fields present |
| D12 | Gate 3 | §3 hashes | Freeze at listed hashes after D1/D2/D7/D11 | PENDING | — | baseline record | — | Hash re-verification |
| D3 | Gate 4 | EVAL | Implement three labels + fixtures | PENDING | — | none (implementation) | — | Unit tests per label |
| D4 | Gate 4 | PLAN §11, EVAL | Keep PLAN rule; implement | PENDING | — | none | — | Test: invalid ≠ MISINTERPRET |
| D5 | Gate 4 | PLAN §11, RP §7, PILOT | Option C: equivalence primary; contract conformance secondary | ACCEPT — C | [D5 approval](approvals/D5_COMPARISON_SEMANTICS_APPROVAL_2026-10-31.md) | AM-007 approved | 2026-10-31 | Separate-field regression and end-to-end validation pending |
| D10 | Gate 4 | PILOT, EVAL-PLAN | Label EXPLORATORY; exclude from primary | PENDING | — | none | — | Register + PR #9 label |
| D13 | Gate 4 | RP §8 | Pre-register operational rules | PENDING | — | AM-008 | — | Metric spec dated before first scored run |
| D6 | — | A2 §6 / RP §7 | Acknowledge existing ASSUME wording | ACKNOWLEDGED | [D6 acknowledgement](approvals/D6_ASSUME_TERMINOLOGY_ACKNOWLEDGEMENT_2026-10-31.md) | none | A2-v1.0 | Wording confirmed; frozen sources unchanged |
| D8 | — | A2 §9 | Acknowledge core/extension grouping as a governance decision, distinct from PLAN §7 construction order | ACKNOWLEDGED | [D8 acknowledgement](approvals/D8_CORE_EXTENSION_GROUPING_ACKNOWLEDGEMENT_2026-10-31.md) | none | A2-v1.0 | Existing grouping accepted; frozen sources unchanged |
| D15 | — | A2 §8 / RP §11 | Acknowledge observation unit (Model, Benchmark Instance, Condition, Trial) | ACKNOWLEDGED | [D15 acknowledgement](approvals/D15_OBSERVATION_UNIT_ACKNOWLEDGEMENT_2026-10-31.md) | none | A2-v1.0 | Existing unit confirmed; frozen sources unchanged |
| D16 | — | PLAN §7 / A2 §9 / T05 O4 | Acknowledge P02 as deterministic C1 control in the core set | ACKNOWLEDGED | [D16 acknowledgement](approvals/D16_P02_CORE_CONTROL_ACKNOWLEDGEMENT_2026-10-31.md) | none | PLAN v1.0-FROZEN / A2-v1.0 | Existing classification and evidence preserved |

Until a decision is recorded, the operative source and its existing limitations remain unchanged.

## 9. Execution order

1. Decide D1, D2, D9 and D14, then start T08.
2. Decide D7 and D11, then D12 (freeze baseline), before any Gate 3 certification work.
3. Decide D5 and D13, implement D3 and D4 in the evaluator, and record D10, all before Gate 4 scored experiments.
4. Acknowledge D6, D8, D15 and D16.
5. After every approved amendment, recheck the complete register and re-verify the §3 hashes.

A gate is not complete merely because its decision document or implementation exists.

## 10. Amendment procedure

Each amendment AM-NNN:

1. is written from the [amendment template](../amendments/AMENDMENT_TEMPLATE.md) as `docs/amendments/AM-NNN_<slug>.md`;
2. records the source document, section and SHA-256 **before** the change, the reason, the affected instances and artifacts, whether earlier results are rerun, and whether the affected analysis is primary, secondary or exploratory (PLAN §12; RP §14);
3. states whether it was written before or after any model outcome was viewed (RP §13);
4. leaves the frozen source file untouched, so the amendment is read alongside the source;
5. takes effect only after the author's dated disposition is recorded in the decision form and the approval register.

## 11. A3 acceptance checklist

- [x] All inconsistencies D1–D16 are accounted for (12 substantive, 4 documentation-only).
- [x] Each substantive decision has its impact, options and gate recorded.
- [x] Recommendations are clearly separated from approved decisions (all dispositions PENDING).
- [x] No source protocol, RTL, run log or evidence manifest was modified.
- [x] No benchmark case was newly certified by this documentation task.
- [x] No experimental result or metric was invented. Pilot figures are quoted from PILOT-CSV.
- [x] Every approved change will have a dated, versioned record (§10 and the amendment template).
- [ ] Author approval of A3 recorded separately in the [decision form](A3_AUTHOR_DECISION_FORM.md).

## 12. Completion boundary

A3 is complete as a decision-planning artifact when the matrix is consistent, source-linked and ready for the required decisions.

A3 does not mean that D1–D16 are resolved, T08 is authorised, Gate 3 is passed or Gate 4 is ready.

**Final status:** DRAFT — AUTHOR APPROVAL PENDING.
