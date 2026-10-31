# AM-007 — Dual comparison relations: equivalence primary, contract conformance secondary

| Field | Value |
|---|---|
| Amendment ID | AM-007 |
| Resolves decision | D5 — comparison semantics |
| Source documents amended | `Files/FORMAL_AMBIG_RTL_PLAN.md`; `Files/Research_Papers/docs/research_protocol.md` |
| Sections | PLAN §11; RP §7 (additive clarification; frozen source files remain untouched) |
| PLAN source SHA-256 before amendment | `19e1fe9abc5b8e07d96a3df339d2a020eae93fee7c9b3815a30dd49d112ee305` |
| RP source SHA-256 before amendment | `87d3a6e7632bc46e75c23b7ff25ed7d84a09691bc1652865f250a04c34cfaa63` |
| Date drafted | 2026-10-31 |
| Drafted before or after viewing any model outcome? | AFTER. The P05 exploratory pilot outcomes were already viewed. This amendment does not promote, relabel, or retrospectively use those outcomes as primary evidence. |
| Status | APPROVED — protocol rule; implementation validation pending |
| Author approval | G. Naveen, D5 Option C, 2026-10-31; [approval record](../project-state/approvals/D5_COMPARISON_SEMANTICS_APPROVAL_2026-10-31.md) |

## 1. Text being amended

The frozen PLAN §11 defines the generated RTL classes by behavioral equivalence:

- A: generated RTL is equivalent to reference RTL-A.
- B: generated RTL is equivalent to reference RTL-B.
- AB: generated RTL is equivalent to both references.
- M: generated RTL is equivalent to neither reference.

Research Protocol §7 repeats the equivalence-based A/B/AB/M classification. The P05 exploratory pilot used per-interpretation assertion-contract conformance instead of reference-RTL equivalence. These are different relations and must not be combined under one label.

## 2. Amended rule

### 2.1 Primary comparison — behavioral equivalence

The primary generated-RTL classification remains exactly the equivalence-based A/B/AB/M rule in frozen PLAN §11 and RP §7. For each case/version, compare the same generated RTL against reference RTL-A and reference RTL-B under the same declared legal environment, assumptions, and observable set.

The primary classification is recorded in its own field (for example, `primary_equivalence_class`). It is not replaced or modified by contract-conformance results.

Formal outcomes must remain distinct:
- A completed proof of equivalence establishes the corresponding equivalence relation.
- A valid counterexample establishes non-equivalence for the checked assumptions and observables.
- Timeout, tool error, incomplete proof, missing evidence, or an unsupported run is unresolved/inconclusive; it is not proof of non-equivalence and must not be converted to M.
- Existing D3 technical-failure labels remain separate from behavioral classification.

For certified ambiguity cases whose references are formally non-equivalent on the declared observables, equivalence-based AB is structurally unavailable. Reports must state this limitation rather than imply all four classes are attainable.

### 2.2 Secondary comparison — contract conformance

A second, independent comparison may evaluate the same generated RTL against the frozen behavioral contract for interpretation A and the frozen behavioral contract for interpretation B.

For each generated RTL instance, record the two individual contract outcomes:
- `contract_A_status`: PASS, FAIL, or INCONCLUSIVE.
- `contract_B_status`: PASS, FAIL, or INCONCLUSIVE.

When both contract checks are determinate, derive a separate `secondary_contract_class`:
- `contracts_A_only`: A passes and B fails.
- `contracts_B_only`: A fails and B passes.
- `contracts_both`: both A and B pass.
- `contracts_neither`: both A and B fail.

If either contract check is inconclusive, incomplete, or affected by a formal-tool error, record `contracts_unresolved`; do not infer a failure for the unresolved contract. If generated RTL is invalid or incomplete under D3, retain the D3 technical label and do not manufacture a contract class.

The label `contracts_both` is never called, stored as, or counted as equivalence-based `AB`. Likewise, secondary contract outcomes never overwrite the primary equivalence class.

### 2.3 Contract and environment controls

Before a scored run, each case/version must freeze and identify:
1. Contract A and contract B source files and cryptographic hashes.
2. The behavioral specification each contract represents.
3. Common legal-environment assumptions and observable signals.
4. Formal tool and version, proof mode, commands, timeout/resource policy, and evidence paths.
5. The rules for interpreting PASS, FAIL, and INCONCLUSIVE.

Both contract checks must use the same generated RTL artifact and the declared common environment for that case. Contract overlap is permitted only when supported by the written behavioral specifications; it must not be introduced accidentally by omitted properties. Where the case claims mutually exclusive interpretations, validate the contracts against the reference designs and retain evidence of contract tightness. Any unresolved contract-quality issue blocks use of that case's secondary result in confirmatory analysis.

### 2.4 Separate reporting and analysis

Primary equivalence and secondary contract conformance must be reported independently:
- separate output fields and evidence references;
- separate denominators, exclusions, and missing/inconclusive counts;
- separate analysis code and summary tables;
- separate descriptions in the manuscript and artifact documentation.

Do not combine the two relations into a single A/B/AB/M field, a pooled metric, or an unlabelled count. Primary claims use the primary equivalence field only. Secondary contract-conformance results are clearly identified as secondary and cannot redefine primary claims.

### 2.5 Historical P05 pilot

The P05 Groq pilot remains exploratory and retains the relation actually used by that pilot: contract conformance against its recorded per-interpretation contracts. Its existing outputs must not be renamed as equivalence-based A/B/AB/M, retroactively promoted to primary results, or silently recalculated under this amendment. Preserve the pilot source, outputs, logs, and evidence unchanged. Any new evaluation of P05 must use the approved protocol prospectively and be recorded as a new run with its own immutable manifest.

### 2.6 D4 MISINTERPRET interaction

The D4 fail-closed `MISINTERPRET` policy is evaluated against the **primary equivalence classification**. A secondary contract result such as `contracts_neither` alone cannot trigger `MISINTERPRET`. D4 still requires all of its explicit prerequisites, including completed formal comparison and approved comparison-relation reference. D4's technical-failure exclusions remain in force.

## 3. Reason

D5 author decision selects Option C: preserve the frozen equivalence relation as primary while adding a separately reported contract-conformance relation. This preserves the pre-existing primary protocol, makes the pilot's different relation explicit, and permits additional behavioral-contract analysis without conflating distinct estimands.

The author approved Option C on 2026-10-31. The P05 pilot had already been observed; therefore this amendment explicitly records that it was drafted after viewing model outcomes and forbids retrospective promotion of those results.

## 4. Scope and effect

| Question | Answer |
|---|---|
| Affected instances | All dual-interpretation benchmark instances evaluated prospectively under the amended protocol; P05 historical pilot remains exploratory and unchanged. |
| Affected artifacts | Future evaluator schema, comparison adapters, run manifests, tests, analysis scripts, reporting tables, and protocol documentation. Frozen PLAN and RP source files are not edited. |
| Are earlier results rerun? | NO, not automatically. Historical P05 pilot remains as-run exploratory evidence. Any new run is separately versioned and manifested. |
| Effect on earlier results | P05 contract-conformance outputs remain exploratory; they are not primary equivalence results. |
| Existing records rewritten? | NO. Historical source files, RTL, formal evidence, counterexamples, logs, manifests, and pilot outputs remain immutable. |

## 5. Validation

Before production integration or primary scored experiments, retain a versioned validation report demonstrating:
1. The primary equivalence classifier matches frozen PLAN §11 on positive, negative, and unresolved fixtures.
2. The secondary contract classifier covers A-only, B-only, both, neither, and unresolved fixtures.
3. Combined fixtures demonstrate that all primary/secondary combinations are stored independently and neither field overwrites the other.
4. Tool failures, timeouts, invalid RTL, and incomplete checks do not become proven mismatch or `M`.
5. `contracts_both` is never mapped to equivalence `AB`.
6. D4 `MISINTERPRET` consumes the primary equivalence class only.
7. Each run manifest records source hashes, contract hashes, assumptions, observables, commands, tool versions, timeouts, and evidence locations.
8. Regression tests pass in the supported environment; logs and CI run are retained.

No production integration, real end-to-end validation, or scored experiment is claimed by this protocol amendment record.

## 6. Approval

| Field | Value |
|---|---|
| Disposition | ACCEPT — Option C (D5 comparison semantics) |
| Approved by | G. Naveen |
| Date | 2026-10-31 |
| Approval-register entry | [D5 author approval](../project-state/approvals/D5_COMPARISON_SEMANTICS_APPROVAL_2026-10-31.md) |
| Effective from commit | `f6361a42abdfe8cb8f889e0d74f34a4a60915ed7` (AM-007 creation commit); production use remains gated on Section 5 validation and remaining Gate 4 approvals. |
