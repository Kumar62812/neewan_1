# Chapter 2 — COMPREHENSIVE LITERATURE REVIEW

**Status:** Ordered synthesis outline. Paper-level findings remain blank until source identity and content are checked.

## 2.1 Foundational Theory & Baseline Architectures

### 2.1.1 LLM-Based RTL Generation

Review the benchmark task, reference assumptions, correctness criteria, supported designs, and evaluation limits of RTL-generation work. Candidate names from the supplied outline include RTLLM and OpenLLM-RTL. Verify each paper’s title, authors, version, and claims against its primary source before citation.

**Repository starting points:** [LLM-to-RTL papers](../../../Files/Research_Papers/01_LLM_to_RTL/), [base paper](../../../Files/Research_Papers/00_Base_Paper/), and [literature matrix](../../../Files/Research_Papers/literature/literature_matrix.csv).

### 2.1.2 FSM Generation & Hardware Reasoning

Review LLM-based FSM and sequential-hardware generation, including task complexity, transition and output semantics, and how the evaluation checks behavior. Treat “LLM-FSM” in the supplied outline as a search lead until the exact source is identified and verified.

**Repository starting point:** [FSM and hardware reasoning papers](../../../Files/Research_Papers/02_FSM_and_Hardware_Reasoning/).

### 2.1.3 Formal Verification Tools

Explain only the methods needed for this study: SAT/SMT, bounded model checking, induction where used, assertions, equivalence or miter checking, assumptions, observables, and distinguishing traces. State what each method establishes and its bound or modeling scope.

Do not imply that one tool was used for every case. P01’s accepted record uses Yosys 0.33, SymbiYosys SBY v0.69, Z3 4.8.12, smtbmc z3, and BMC depth 1. P02 explicitly used Yosys/Yosys-SMTBMC directly and does not claim a SymbiYosys run. Use the exact case record.

**Repository starting points:** [formal verification papers](../../../Files/Research_Papers/04_Formal_Verification/) and [formal verification protocol](../../../Files/Research_Papers/docs/formal_verification_protocol.md).

## 2.2 Problem Statement & Critical Gaps in Prior Art

Compare what each source evaluates against the research problem:

- Does it use one reference or accept multiple valid behaviors?
- Does it identify ambiguity or invite clarification?
- Are alternatives independently judged plausible?
- Are behaviors checked formally under common assumptions and declared observables?
- Does it distinguish an invalid implementation from a valid alternative reading?

State a gap only when the paper was checked for that capability. The repository audit found duplicate PDF bytes and title/content mismatches in the literature collection. Resolve source identity before relying on the affected rows; see the [2026-10-16 literature audit](../../audits/2026-10-16-repository-audit.md) and [literature matrix guide](../../../Files/Research_Papers/literature/README.md).

## 2.3 Objective-Formulation Literature

Use the literature to justify each research question, hypothesis, condition, and metric—not merely to support a broad motivation. Candidate leads in the supplied outline include Ambig-SWE and Proof2Silicon; verify the exact publication and PDF before describing either. Map reviewed sources to RQ1–RQ4 and H1–H4, and label the hypotheses as untested until results exist.

## Three-Bucket Synthesis Matrix

Keep the synthesis to these three primary buckets. The repository’s additional literature folders are source locations, not extra conceptual buckets.

| Bucket | Repository starting points | Compare consistently |
|---|---|---|
| LLM RTL generation and hardware reasoning | [00_Base_Paper](../../../Files/Research_Papers/00_Base_Paper/), [01_LLM_to_RTL](../../../Files/Research_Papers/01_LLM_to_RTL/), [02_FSM_and_Hardware_Reasoning](../../../Files/Research_Papers/02_FSM_and_Hardware_Reasoning/) | Task and dataset; reference or ground truth; correctness test; clarification support; formal evidence; limitations |
| Software ambiguity, clarification, and requirements engineering | [03_Ambiguity_and_Underspecification](../../../Files/Research_Papers/03_Ambiguity_and_Underspecification/), [05_Requirements_Engineering](../../../Files/Research_Papers/05_Requirements_Engineering/) | Ambiguity definition; interaction; human validation; outcome labels; evidence; what does and does not transfer to hardware |
| Formal verification and hardware behavioral equivalence | [04_Formal_Verification](../../../Files/Research_Papers/04_Formal_Verification/), [formal protocol](../../../Files/Research_Papers/docs/formal_verification_protocol.md) | Property or equivalence question; legal environment; observables; proof scope; counterexample; limitations |

Use [06_Benchmarks_and_Evaluation](../../../Files/Research_Papers/06_Benchmarks_and_Evaluation/) and [07_Related_Work](../../../Files/Research_Papers/07_Related_Work/) as cross-cutting sources assigned to the bucket their verified contribution supports.

For each paper, record the stable citation key, verified metadata, question, method, data, evaluation, reported limitation, relevance to an RQ, and source path in the [literature matrix](../../../Files/Research_Papers/literature/literature_matrix.csv). Do not fill a limitation or “gap” cell by guessing from a filename or abstract alone.

