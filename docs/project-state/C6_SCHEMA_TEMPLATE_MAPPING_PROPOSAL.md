# C6 — Non-binding schema-to-template mapping proposal

**Status:** Proposal package prepared; automated validation pending.  
**Proposal status:** `NON_BINDING_REQUIRES_AUTHOR_DECISION`.  
**Canonical schema/template:** unchanged.

## 1. Purpose

C5 identified schema/YAML naming and layout gaps. Project records state that D2 (certification/lifecycle vocabulary) and D14 (case layout) remain pending. C6 makes those decisions concrete as a field-by-field candidate mapping; it does not decide either on the author's behalf.

## 2. D2 — vocabulary and scientific state

The prose schema lists `candidate`, `certified_ambiguous`, `unambiguous_control`, `negative_candidate`, and `inconclusive`, then says accepted records may later be `frozen`. These labels may represent different concepts: workflow state, benchmark role, scientific classification, and release state.

**Option for discussion:** separate the concepts. Use a workflow/lifecycle status for process state; a distinct classification for scientific outcome; and, where useful, a case-role field for control/candidate type. These are proposal-only fields until D2 decides the vocabulary. Do not retrofit existing records silently.

## 3. D14 — package layout and field paths

The YAML template represents many schema concepts but nests them under different names. C6 maps each schema-listed field, including conditional `counterexample`, to a candidate path or marks it missing/insufficient. The proposal remains non-normative until D14 decides whether to retain the nested YAML and publish a formal mapping or issue a versioned schema/template revision with migration notes.

## 4. Field mapping summary

| Schema field | Candidate YAML path | Current finding |
|---|---|---|
| `instance_id` | `instance_id` | Direct |
| `version` | `instance_version` | Naming mismatch; decision required |
| `status` | `status` | Semantics need D2 decision |
| `category` | — | Missing explicit top-level field |
| `specification_text` | `requirement.specification_text` | Nested mapping candidate |
| `ambiguity_dimension` | `requirement.primary_ambiguity_dimension` | Naming/nesting mismatch |
| `interpretation_A/B` | `interpretations.A/B.text` | Nested candidate; B must be role-conditional |
| `interpretation_rationale_A/B` | `interpretations.A/B.rationale` | Nested mapping candidate |
| `reference_rtl_A/B` | `reference_rtl.A/B.path` | Nested candidate; role-conditional requirements |
| `formal_environment` | `formal_environment` | Direct object candidate |
| `observables` | `observables` | Direct object candidate |
| `formal_result` | `formal_result` | Direct object candidate; controlled outcomes need validation |
| `counterexample` | `formal_result.counterexample_path` | Conditional mapping candidate |
| `annotation_record` | `human_annotation.adjudication_record` | Insufficient alone; needs record/manifest pointer decision |
| `provenance` | `provenance` + `reproducibility` | Distributed across objects |

The machine-readable proposal file records all 18 schema-field entries and their decision flags. It also captures three proposal-only extensions: `case_role`, `classification`, and `annotation_record_path`.

## 5. Role-specific implications

- **Unambiguous control:** do not fabricate a second plausible interpretation. Deliberately incorrect RTL may test the formal checker only when explicitly labelled as a negative control.
- **Ambiguity candidate:** interpretations A and B, corresponding RTL, shared environment/observables and formal distinction evidence are needed; human plausibility remains separate.
- **Negative/rejected candidate:** preserve the reason for rejection—implausibility, equivalence, invalid RTL or inconclusive comparison—and retain the tested evidence.
- **Robustness case:** required artifacts must follow its authorized role; it is not automatically a certified ambiguity case.

## 6. Automated validation

- Machine-readable proposal: `docs/project-state/C6_SCHEMA_TEMPLATE_MAPPING_PROPOSAL.json`
- Validator: `Files/Research_Papers/benchmark/pilot_v0_1/validate_c6_schema_mapping_proposal.py`
- Regression tests: `Files/Research_Papers/benchmark/pilot_v0_1/tests/test_validate_c6_schema_mapping_proposal.py`
- Workflow: `.github/workflows/c6-schema-template-mapping.yml`

The actual CI outcome will be added only after GitHub reports the result.

## 7. Required gate before implementation

1. Approve the D2 controlled lifecycle/classification vocabulary, including whether these are separate fields.
2. Approve D14's canonical layout and exact field paths.
3. Decide whether to add the proposed role/classification/annotation-record fields.
4. Add role-aware fixtures against the chosen format.
5. Migrate only through a separately versioned change; preserve earlier case snapshots and evidence.

## 8. Non-claims

This is a proposal, not approval. It does not update canonical schema/template files, freeze the P01 template, alter historical case evidence, run formal tools, collect human review, execute LLM experiments, certify ambiguity, or mark the project complete.
