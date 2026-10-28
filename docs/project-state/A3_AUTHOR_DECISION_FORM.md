# A3 author decision form

**For:** [A3-v1.0 decision matrix](A3_PROTOCOL_DECISION_MATRIX_v1.0.md)
**How to use:** fill in one row per decision and the approval block. A decision takes effect only when its row has a disposition, a date and, where marked, an approved amendment. Rows can be completed at different times; leave the rest PENDING.

Disposition codes: **ACCEPT** (adopt the A3 recommendation) · **REJECT** (keep the source as it is) · **REVISE** (adopt with the changes written in Notes) · **DEFER** (postpone; name the trigger in Notes) · **PENDING**.

## Before T08

| ID | Decision | A3 recommendation | Disposition | Date | Notes / revision |
|---|---|---|---|---|---|
| D1 | Taxonomy relationship | C1–C5 primary; RP §5 dimensions as secondary tags (AM-001) | PENDING | | |
| D2 | Status vocabulary | PLAN status field + separate lifecycle field + crosswalk (AM-002); existing metadata not rewritten | PENDING | | |
| D9 | P01 freeze gate | Option B: dated amendment recording the guide direction; template freeze moves to T08 (AM-003) | PENDING | | |
| D14 | Case layout | One layout for new cases, based on P02/P05; crosswalk for P01/P02/P05 (AM-004) | PENDING | | |

## Before Gate 3

| ID | Decision | A3 recommendation | Disposition | Date | Notes / revision |
|---|---|---|---|---|---|
| D7 | Aggregation rule | P_X = share of eligible annotators rating ≥ 4; τ = 0.80; minimum annotators: ___ (AM-005) | PENDING | | |
| D11 | Provisional vs final | Separate `technical_status` and `certification_status`; primary analyses use final status only (AM-006) | PENDING | | |
| D12 | Protocol freeze | Freeze RP/BS/FVP/AP at A3 §3 hashes after D1, D2, D7, D11 | PENDING | | |

## Before Gate 4

| ID | Decision | A3 recommendation | Disposition | Date | Notes / revision |
|---|---|---|---|---|---|
| D3 | Technical labels | Implement INVALID / INCOMPLETE / INCONCLUSIVE in the evaluator with fixture tests | PENDING | | |
| D4 | MISINTERPRET rule | Keep PLAN §11 restriction; implement and test | PENDING | | |
| D5 | Comparison relation | Choose (a) equivalence, (b) contract conformance or (c) both: ___ | PENDING | | |
| D10 | P05 Groq pilot | Label EXPLORATORY; exclude from primary metrics | PENDING | | |
| D13 | Metric operations | Pre-register operational rules and statistics (AM-008) before the first scored run | PENDING | | |

## Documentation clarifications

| ID | Clarification | Acknowledged | Date |
|---|---|---|---|
| D6 | ASSUME wording ("silently") | PENDING | |
| D8 | Core/extension grouping is a governance decision | PENDING | |
| D15 | Observation unit (Model, Instance, Condition, Trial) | PENDING | |
| D16 | P02 is a C1 control in the core set | PENDING | |

## Approval of A3 itself

> I approve **A3-v1.0** (`docs/project-state/A3_PROTOCOL_DECISION_MATRIX_v1.0.md`, SHA-256 recorded in the approval register) as the decision plan. This approves the plan, not the individual decisions above, which take effect only as their rows are completed.
>
> Author: __________ Date: __________

Approving A3 does not resolve D1–D16, authorise T08, pass Gate 3 or make Gate 4 ready.
