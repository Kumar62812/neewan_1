# Thesis chapter map and research workflow

**Status:** Working structure and writing guide; not a results chapter.  
**Project:** FORMAL-AMBIG-RTL / neewan_1

This guide maps the five thesis chapters to the repository’s canonical sources and lays out the evidence workflow. It does not amend the frozen research plan, taxonomy, protocols, case artifacts, or result records. Use the [phase workboard](../project-state/PHASE_WORKBOARD.md) for current project status and the [repository map](../repository-map.md) for the complete file map.

## 1. Keep the research workflow separate from the thesis order

The thesis is presented in Chapters 1–5. The benchmark work follows the evidence and gate sequence below; a chapter heading does not mean its evidence or gate is complete.

### Research and evaluation sequence

1. **Review and verify the literature.** Read the primary sources, verify bibliographic details, and record what each source actually evaluates in the [literature matrix](../../Files/Research_Papers/literature/literature_matrix.csv). Keep reported facts separate from this project’s interpretation.
2. **Freeze the case inputs.** Preserve the exact requirement and its version/hash. Write each interpretation and behavioral specification before writing its reference RTL. Record interfaces, legal environment, observables, assumptions, category, and status.
3. **Build the reference evidence chain.** For each candidate reading, link Requirement → Interpretation → Behavioral Specification → Reference RTL. A C1 control such as P01 or P02 has one intended behavior; it is not an ambiguity-certificate case.
4. **Run the appropriate formal checks.** Check each reference against its own behavioral specification. For competing readings, compare observable behavior under the same declared environment. Retain commands, exact tool/version, assumptions, logs, hashes, and witnesses. A deliberately wrong control should fail with an inspected counterexample; a compilation error or tool failure is not a behavioral counterexample.
5. **Assess human plausibility under the approved protocol.** Evaluate each proposed interpretation separately using the predeclared eligibility, rating, threshold, and disagreement rules. Keep reviewers independent and preserve objections. Do not infer a review or approval from a file’s presence.
6. **Make the case decision.** Apply the frozen operational definition in the [research protocol](../../Files/Research_Papers/docs/research_protocol.md): both interpretations must pass the human-plausibility protocol and their reference RTL must be behaviorally non-equivalent under the declared legal environment and observables. Each reference must first conform to its own specification. Formal non-equivalence alone does not establish linguistic plausibility. Keep unresolved and excluded cases visible.
7. **Pass the evaluation gate before model runs.** Use only eligible cases and a frozen experiment plan. Lock the requirement text, model/version, prompt and context, decoding settings, run count, outcome labels, metric definitions, denominators, exclusions, and failure handling before evaluation.
8. **Run and preserve each model outcome.** Retain the raw response, extracted RTL, parse/elaboration output, formal outcome, witness, toolchain details, and hashes. Preserve invalid, incomplete, inconclusive, and failed runs; do not silently retry or replace them.
9. **Freeze results, then analyze and release.** Calculate metrics from the retained runs using the preregistered denominators. Write the result first, then discuss what it means and its limitations. Link each thesis claim to the exact source, run, and status.

The frozen pilot order is **P01 → P02 → P05 → P06 → P08 → P03 → P04 → P07 → P09 → P10 → P11 → P12**. Preserve that order unless the project records an explicit, prospective amendment. P12 is evaluator robustness, not a certified-ambiguity case.

### Taxonomy crosswalk

Keep two different ideas separate:

- The frozen case categories are **C1–C5** in the [research plan](../../Files/FORMAL_AMBIG_RTL_PLAN.md). P01 and P02 are C1 unambiguous controls.
- The research protocol’s ambiguity dimensions are reset, output, transition, timing, state, and **concurrency** semantics. The supplied outline lists five dimensions; include concurrency when describing the frozen taxonomy. Do not silently change either list to make them match.

The protocol’s operational definition is more specific than the shorthand “plausibility and non-equivalence”: both competing interpretations must pass the predefined plausibility protocol, and the corresponding reference RTL must be observably non-equivalent under the declared model. Use the protocol’s exact wording in the thesis.

## 2. Thesis chapter order and source map

### Chapter 1 — Introduction and problem formulation

**Write:** background and research significance; the single-reference evaluation limitation; the hardware-specific ambiguity gap; research questions, objectives, scope, and contributions. Keep claims about prior work tied to verified literature sources.

**Start from:** the [frozen research plan](../../Files/FORMAL_AMBIG_RTL_PLAN.md), the [thesis assessment plan](../project-state/THESIS_ASSESSMENT_PLAN.md), and verified entries in the [literature matrix](../../Files/Research_Papers/literature/literature_matrix.csv).

**Finish when:** each gap and objective has a source or a clearly marked project rationale, and scope statements distinguish planned work from completed evidence.

### Chapter 2 — Literature review

Organize the review as a synthesis, not a sequence of paper summaries:

1. LLM-to-RTL generation and evaluation: [01_LLM_to_RTL](../../Files/Research_Papers/01_LLM_to_RTL/) and [00_Base_Paper](../../Files/Research_Papers/00_Base_Paper/).
2. FSM and hardware reasoning: [02_FSM_and_Hardware_Reasoning](../../Files/Research_Papers/02_FSM_and_Hardware_Reasoning/).
3. Ambiguity, clarification, and requirements engineering: [03_Ambiguity_and_Underspecification](../../Files/Research_Papers/03_Ambiguity_and_Underspecification/) and [05_Requirements_Engineering](../../Files/Research_Papers/05_Requirements_Engineering/).
4. Formal verification and sequential equivalence: [04_Formal_Verification](../../Files/Research_Papers/04_Formal_Verification/).
5. Benchmark design and related work: [06_Benchmarks_and_Evaluation](../../Files/Research_Papers/06_Benchmarks_and_Evaluation/) and [07_Related_Work](../../Files/Research_Papers/07_Related_Work/).

Use the [literature matrix guide](../../Files/Research_Papers/literature/README.md) and matrix to compare each work’s task, evidence, human validation, formal methods, interaction, and limitation. Verify each paper’s metadata and content before citing it; a filename or matrix row alone is not source verification.

**Finish when:** the three strands—LLM hardware generation, ambiguity/clarification, and formal methods—are compared against explicit research gaps and the proposed contribution.

### Chapter 3 — Methodology and system architecture

**Write:** the frozen evidence chain; the distinction between plausibility and formal behavioral distinction; the six ambiguity dimensions and C1–C5 case categories; case construction; formal environment and observables; review protocol; evaluation conditions; and gate sequence.

**Start from:** the [research protocol](../../Files/Research_Papers/docs/research_protocol.md), [formal verification protocol](../../Files/Research_Papers/docs/formal_verification_protocol.md), [benchmark schema](../../Files/Research_Papers/docs/benchmark_schema.md), [phase workboard](../project-state/PHASE_WORKBOARD.md), and canonical case folders under [pilot_v0_1](../../Files/Research_Papers/benchmark/pilot_v0_1/).

Describe each tool from that run’s retained record. In particular, the P02 results identify direct Yosys and Yosys-SMTBMC execution; do not describe that run as SymbiYosys. For P01, use the tool and configuration recorded in its retained evidence.

**Current claim boundaries:** P01 formal evidence applies to its documented effective tested source; independent certification and template-freeze status remain separate gates. P05 must retain the wording **Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.** The draft LLM runner is infrastructure work, not model-performance evidence.

**Finish when:** a reader can trace each reported method to a versioned artifact and understand the environment, assumptions, exclusions, and gates.

### Chapter 4 — Results and discussion

Use **Data → Result → Discussion** for every experiment and case.

- **Data:** identify the case, exact source revision, run, conditions, denominator, tool/model version, logs, witnesses, and hash or evidence path.
- **Result:** report the observed status or measured value, with exclusions and incomplete runs visible.
- **Discussion:** interpret that result within its scope; do not treat interpretation as additional data.

Report formal outcomes from the case records. Report human plausibility only from retained independent responses and the predefined decision rule. Report LLM metrics—such as clarification frequency, interpretation accuracy, misinterpretation rate, or formal correctness—only if they are in the applicable frozen plan and can be recomputed from retained runs with their denominators.

**No LLM performance result is established by the planning documents or draft runner alone.** Until eligible runs and their evidence exist, label those result sections planned or pending. Do not supply estimated, illustrative, or expected values as findings.

**Finish when:** every table and figure can be regenerated from linked evidence and its claim scope is stated beside it.

### Chapter 5 — Conclusion, future work, and viva preparation

**Write last:** answer each research question using only the Chapter 4 evidence; summarize demonstrated contributions at the level supported by those results; state limitations; and list future work as proposed work, not completed capability. Build viva questions from the frozen method, actual results, counterexamples, and acknowledged limitations. Label anticipated answers as defense preparation, not research findings.

Avoid a conclusion that says the project “successfully bridges” the research gap until the relevant benchmark, human-review, and evaluation evidence supports that claim. Before then, describe the framework and its status precisely.

## 3. Repository file arrangement

Use this chapter map as a navigation layer. Keep source artifacts in their canonical evidence-first locations:

- Literature PDFs and synthesis matrix: [Files/Research_Papers](../../Files/Research_Papers/).
- Frozen plan, protocols, schemas, and case sources: [Files/Research_Papers/docs](../../Files/Research_Papers/docs/) and [benchmark/pilot_v0_1](../../Files/Research_Papers/benchmark/pilot_v0_1/).
- Current status, thesis planning, and provenance: [docs/project-state](../project-state/) and [docs/provenance](../provenance/).
- Reproduction instructions and retained reproduction records: [docs/reproducibility](../reproducibility/).
- Decisions and dated history: [governance](../../governance/).
- Accepted historical packages: [re](../../re/).

Do not physically move, rename, edit, or duplicate frozen requirements, protocols, case sources, manifests, accepted archives, or evidence to make the directory tree look like the thesis. Commands, hashes, provenance records, and links depend on those paths. For future editable chapter drafts, use a separate ordered directory such as:

- docs/thesis/chapters/01-introduction.md
- docs/thesis/chapters/02-literature-review.md
- docs/thesis/chapters/03-methodology.md
- docs/thesis/chapters/04-results-discussion.md
- docs/thesis/chapters/05-conclusion-future-viva.md

Create those chapter files only when there is substantive draft content to review; do not use empty files as evidence of completion.

## 4. Writing control checklist

Before marking a thesis section complete:

- Confirm the source is present and on the intended branch; distinguish main, draft PR, and local-only material.
- Check every local link and exact evidence path.
- Verify literature identity against its primary source.
- Maintain a claim ledger: claim, chapter, source path, evidence status, scope, and limitation.
- Preserve the labels PASS, expected negative-control FAIL, INCONCLUSIVE, TOOL ERROR, UNRESOLVED, and PENDING according to the evidence.
- Keep the result and discussion separate; never promote a plan, hypothesis, draft, or file-presence check into a result.
- Reconcile status pages against the actual records before submission and cite the source revision for each result.

