# FORMAL-AMBIG-RTL Project Compass

**CURRENT: P01 / NOT STARTED**

**Purpose:** This is the project’s day-to-day source of truth.  
Read this file before starting work. If a proposed task is not permitted by the  
current phase, do not start it without a documented phase-transition decision.

**Scientific plan:** `FORMAL_AMBIG_RTL_PLAN.md`  
**Research protocol:** `Research_Papers/docs/research_protocol.md`  
**Benchmark schema:** `Research_Papers/docs/benchmark_schema.md`  
**Formal protocol:** `Research_Papers/docs/formal_verification_protocol.md`  
**Annotation protocol:** `Research_Papers/docs/annotation_protocol.md`

---

## 1. One-sentence project goal

Build a hardware benchmark that determines whether LLM-generated RTL is incorrect,  
a valid interpretation of an underspecified requirement, or unable to be classified,  
using human plausibility evidence and formal behavioral verification.

---

## 2. Non-negotiable evidence chain

Every benchmark case must follow:

\[
R \rightarrow I \rightarrow S \rightarrow RTL \rightarrow F \rightarrow C
\]

- `R`: Natural-language requirement
- `I`: Defensible interpretation
- `S`: Behavioral specification independent of RTL
- `RTL`: Reference implementation
- `F`: Formal verification evidence
- `C`: Certification decision

Never create two RTL variants first and call them “interpretations” afterward.

---

## 3. Non-negotiable rules

1. Evidence quality is more important than benchmark size.
2. Every ambiguity claim requires both plausibility and formal non-equivalence.
3. Taxonomy category, certification status, and LLM outcome are separate labels.
4. All compared RTL uses the same interface and legal-environment contract.
5. Invalid RTL, formally wrong RTL, and formally inconclusive RTL are different outcomes.
6. No metric, prompt, formal assumption, or certification rule may change silently.
7. No model evaluation begins before P01 is frozen.
8. No new pilot case begins until the preceding milestone exit gate passes.
9. P12 is an evaluator-robustness test, not a certified ambiguity case.
10. Every substantive artifact is version-controlled.

---

## 4. Current state

| Field | Current value |
|---|---|
| Project phase | Phase 1 — Research Foundation |
| Current milestone | P01 — Golden Benchmark Instance v1.0 |
| Current status | Not started |
| Allowed work | Create and validate P01 only |
| Not allowed yet | P02–P12 construction, model experiments, benchmark scaling, performance claims |
| Exit condition | P01 passes all evidence, formal, annotation, metadata, and reproduction gates |

---

## 5. Current task: P01 only

### P01 identity

| Field | Value |
|---|---|
| Instance ID | `P01` |
| Category | `C1 — Unambiguous–Deterministic` |
| Status target | `UNAMBIGUOUS` |
| Design | Combinational 2-to-1 multiplexer |
| Purpose | Validate the complete benchmark methodology |
| Positive test | Valid reference RTL formally passes |
| Negative test | Wrong but compilable RTL formally fails |

### P01 checklist

#### A. Requirement and meaning
- [ ] Store the exact model-facing requirement.
- [ ] Document one intended interpretation.
- [ ] Confirm no competing interpretation is reasonable for the tested behavior.
- [ ] Declare interface and observable outputs.

#### B. Behavioral specification
- [ ] Create a truth table.
- [ ] State the functional equation.
- [ ] Document that the behavior is combinational.
- [ ] Ensure the specification does not depend on RTL syntax.

#### C. RTL
- [ ] Create valid reference RTL.
- [ ] Create deliberately wrong but compilable RTL.
- [ ] Confirm both files use the same interface.

#### D. Formal verification
- [ ] Create properties.
- [ ] Create a reference harness.
- [ ] Create a wrong-RTL harness.
- [ ] Run the valid reference: expected `PASS`.
- [ ] Run the wrong RTL: expected `FAIL_WITH_COUNTEREXAMPLE`.
- [ ] Save scripts, logs, tool version, command, timeout, and failure evidence.

#### E. Annotation and decision
- [ ] Complete the C1 annotation form.
- [ ] Record annotation summary.
- [ ] Write the `UNAMBIGUOUS` certification decision.

#### F. Reproducibility
- [ ] Complete metadata and source hashes.
- [ ] Re-run from a clean environment.
- [ ] Confirm no undocumented manual steps are required.
- [ ] Complete template-freeze review.

---

## 6. Definition of done for P01

P01 is done only when all answers below are “yes.”

| Question | Must be yes? |
|---|---:|
| Is the exact requirement stored? | Yes |
| Is the intended interpretation stored separately from RTL? | Yes |
| Is the behavioral specification independent of code? | Yes |
| Does the valid reference RTL compile and formally pass? | Yes |
| Does wrong but compilable RTL formally fail? | Yes |
| Is failure evidence retained? | Yes |
| Is annotation evidence complete? | Yes |
| Is metadata complete and traceable? | Yes |
| Can a clean environment reproduce the result? | Yes |
| Has the team frozen the P01 template? | Yes |

If any answer is “no,” P01 is not complete.

---

## 7. Phase transition map

```text
Phase 1A: Frozen methodology
        ↓ completed
Phase 1B: P01 golden-template construction
        ↓ current
Phase 1C: P01 verification, annotation, reproduction, and freeze
        ↓ only after all P01 gates pass
Phase 2: Build P02–P12 pilot cases
        ↓ only after pilot evidence is complete
Phase 3: Pilot review and protocol stabilization
        ↓ only after pilot is frozen
Phase 4: Scaled benchmark construction
        ↓ only after benchmark version is frozen
Phase 5: LLM single-shot and interactive evaluation
        ↓ only after results are frozen
Phase 6: Analysis, paper writing, artifact release, and submission
```

---

## 8. Pilot construction order

Do not change this order without a documented amendment:

\[
P01 \rightarrow P02 \rightarrow P05 \rightarrow P06 \rightarrow P08
\rightarrow P03 \rightarrow P04 \rightarrow P07 \rightarrow P09
\rightarrow P10 \rightarrow P11 \rightarrow P12
\]

| Stage | Cases | What it validates |
|---|---|---|
| Foundation | P01 | Full infrastructure, formal acceptance, formal rejection |
| Deterministic sequential | P02 | Clock, reset, sequential behavior |
| Temporal | P05–P07 | Cycle-level divergence and timing interpretation |
| Functional | P08–P09 | Boundary conditions and transition priority |
| Lexical/semantic | P03–P04 | Plausibility of language-level alternatives |
| Environment | P10–P11 | Assumption and protocol ambiguity |
| Robustness | P12 | Invalid and genuinely wrong RTL rejection |

---

## 9. Stop rules

Stop and resolve the issue before continuing if:

- The requirement does not define enough interface context.
- The interpretation was inferred only after writing RTL.
- A candidate alternative is not plausibly supported by the wording.
- Reference RTL designs do not share a common interface.
- Formal divergence requires an illegal input trace.
- The formal run is inconclusive.
- The annotation threshold is not met.
- A metric or category definition appears inadequate.
- A tool limitation prevents reproducibility.

The response to a stop rule is one of:

1. Repair the artifact before proceeding.
2. Reclassify the case as `UNRESOLVED`.
3. Exclude the case with a recorded reason.
4. Propose a versioned protocol amendment before changing a frozen rule.

---

## 10. What to do after every work session

1. Update the checkbox state in this document.
2. Commit every completed artifact with a descriptive message.
3. Record tool commands, versions, outputs, and failures.
4. Write unresolved questions in the relevant review file.
5. Do not mark a gate complete based on memory or informal discussion.
6. At the next session, begin by reading this compass and the current case metadata.

---

## 11. Immediate next action

Create the P01 directory tree and complete these three files first:

1. `requirement.md`
2. `interpretations/interpretation_01.md`
3. `behavioral_specification/specification_01.md`

Do not write RTL until these three artifacts have been reviewed and accepted.

---

## 12. Durability rules

To keep the plan “sticky,” follow these operating habits:

- Keep the Compass at `Files/` level, not buried under research papers.
- Put a one-line status banner at the top:
  - `CURRENT: P01 / NOT STARTED`
  - Later: `CURRENT: P01 / FORMAL VERIFICATION`
  - Later: `CURRENT: P02 / CONSTRUCTION`
- Update only:
  - Current phase,
  - Current milestone,
  - Current status,
  - Checkboxes,
  - Immediate next action.
- Do not rewrite the research goal every day.
- Do not change frozen methodology based on one inconvenient result.
- Commit at every gate, not only at the end of a large task.
- Treat every failed formal proof, rejected interpretation, and excluded case as useful research evidence.
