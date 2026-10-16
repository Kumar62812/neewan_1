# Chapter 3 — METHODOLOGY & SYSTEM ARCHITECTURE

**Status:** Method outline. The frozen plan and protocols govern over any conflicting shorthand in this outline.

## 3.1 Non-Negotiable Evidence Chain

Follow the chain:

**Requirement (R) → Interpretation (I) → Behavioral Specification (S) → Reference RTL → Formal Verification (F) → Certification (C).**

For each ambiguity candidate, version and hash the requirement, both interpretations, both specifications, reference RTL, environment assumptions, observables, formal scripts, human-review record, and decision. Each reference must be valid and conform to its own specification before its distinction is used as evidence.

The frozen research protocol defines certified ambiguity as both interpretations passing the predefined human-plausibility protocol and their reference RTL being behaviorally non-equivalent under the declared legal environment and observables. Formal non-equivalence is not a plausibility judgment. A C1 control follows the one-reference path and is not certified ambiguous.

Keep artifact presence, reported result, integrity verification, fresh reproduction, human plausibility, formal distinction, and certification as separate statuses. A phase transition also requires its recorded decision; a technical result or merged documentation change does not grant it.

## 3.2 Ambiguity Taxonomy across FSM & Sequential RTL

The frozen research protocol lists six ambiguity dimensions:

1. **Reset semantics:** synchronous/asynchronous reset, polarity, priority, reset value.
2. **Output semantics:** Mealy/Moore, registered/combinational output, current-state/next-state interpretation.
3. **Transition semantics:** priority, overlapping or simultaneous conditions, default transitions.
4. **Timing semantics:** same-cycle/next-cycle response, sampling edge, transition timing.
5. **State semantics:** initial state, illegal-state handling, recovery behavior.
6. **Concurrency semantics:** simultaneous events, conflicting conditions, event priority.

Do not confuse these dimensions with the distinct C1–C5 case categories in the frozen research plan:

- **C1:** Unambiguous–Deterministic.
- **C2:** Ambiguous–Lexical/Semantic.
- **C3:** Ambiguous–Temporal/Sequential.
- **C4:** Ambiguous–Behavioral/Functional.
- **C5:** Underspecified–Implementation/Environment.

Assign one primary category and record secondary dimensions as tags when justified. P01 and P02 are C1 controls. P12 is evaluator robustness, not a certification case.

Preserve the pilot construction order: **P01 → P02 → P05 → P06 → P08 → P03 → P04 → P07 → P09 → P10 → P11 → P12**. Any deviation requires a prospective, dated change or transition record.

## 3.3 Pilot Case P01 Implementation

P01 is the C1 deterministic baseline: a combinational 2-to-1 multiplexer with sel=0 selecting a and sel=1 selecting b. It validates the evidence workflow; it is not an ambiguity case.

Use the [P01 requirement, interpretation, specification, RTL, and formal files](../../../Files/Research_Papers/benchmark/pilot_v0_1/P01/) and the [execution recall record](../../../Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/evidence/p01-20260930T220622Z/P01_EXECUTION_EVIDENCE_RECALL.md).

The accepted run is p01-20260930T220622Z. Its record reports Yosys 0.33, SymbiYosys SBY v0.69, Z3 4.8.12, smtbmc z3, and BMC depth 1. The native SBY reference result is PASS; the deliberately wrong RTL result is FAIL with a retained counterexample (a=0, b=1, sel=1, required y=1, observed y=0).

The accepted result applies only to pinned base revision 6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35 plus the retained path-only SBY patch, SHA-256 71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4. The accepted archive SHA-256 is 32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b. The unmodified base is not claimed to have passed. The active checkout’s staged-path form must not be run and reported as the accepted result without the patch.

This formal evidence does not create an independent certification decision, freeze the P01 Golden Template, validate the wider benchmark, or establish ambiguity.

**P01 property-scope check:** the current shared property module contains an immediate assertion, `y == (sel ? b : a)`. Both harnesses state that no assumptions are added; the checked P01 property/configuration files contain no cover property. The supplied thesis outline mentions `assert`, `assume`, and `cover`, but only describe each as executed if a retained P01 run artifact demonstrates it. Do not claim assumptions or coverage goals for the accepted run. See the [shared property module](../../../Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/properties/mux2to1_properties.sv), [reference harness](../../../Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/harness_reference.sv), and [reference](../../../Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/reference.sby)/[wrong](../../../Files/Research_Papers/benchmark/pilot_v0_1/P01/formal/wrong.sby) SBY configurations.

## 3.4 System Architecture and Evaluation Governance

Describe the formal path and model-evaluation path separately:

- **Reference path:** frozen requirement → interpretation(s) → specification(s) → reference RTL → formal conformance/equivalence and witnesses → case decision.
- **Model path:** eligible frozen case → single-shot or interactive condition → raw response → extracted RTL → parse/elaboration → formal classification → retained run record.

The research protocol defines Single-shot and Interactive conditions, unambiguous controls, negative candidates, interaction outcomes ASK/ASSUME/MISINTERPRET/INVALID, and generated-RTL classes A/B/AB/M. Report those categories as distinct; do not equate a clarification question with formally correct RTL.

Use the [benchmark schema](../../../Files/Research_Papers/docs/benchmark_schema.md), [formal protocol](../../../Files/Research_Papers/docs/formal_verification_protocol.md), [P01 provenance register](../../provenance/p01-evidence-register.md), and [phase workboard](../../project-state/PHASE_WORKBOARD.md). Model runs must wait for the required case, review, and evaluator gates.

