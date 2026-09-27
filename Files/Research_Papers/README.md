# Research Papers

Literature repository for the FORMAL-AMBIG-RTL thesis project.

## Preferred folder structure

- `00_Base_Paper/` — working primary reference for the thesis
- `01_LLM_to_RTL/` — LLM-based RTL generation and evaluation
- `02_FSM_and_Hardware_Reasoning/` — FSM reasoning and hardware-specific generation
- `03_Ambiguity_and_Underspecification/` — ambiguity, underspecification, clarification, and specification interpretation
- `04_Formal_Verification/` — formal equivalence, non-equivalence, model checking, and verification methodology
- `05_Requirements_Engineering/` — hardware/system requirements analysis and validation
- `06_Benchmarks_and_Evaluation/` — RTL benchmarks, evaluation protocols, and metrics
- `07_Related_Work/` — adjacent work useful for positioning and novelty analysis

## Current working base paper

**LLM-FSM: Scaling Large Language Models for Finite-State Reasoning in RTL Code Generation**  
Yuheng Wu, Berk Gokmen, Zhouhua Xie, Peijing Li, Caroline Trippel, Priyanka Raina, Thierry Tambe (2026).

This is the current working base paper because it directly targets finite-state reasoning from natural-language specifications to RTL. Final base-paper status should still be confirmed after the complete literature comparison.

## Standardized papers currently organized

### 01 — LLM to RTL

1. **RTLLM: An Open-Source Benchmark for Design RTL Generation with Large Language Model**
2. **VerilogEval: Evaluating Large Language Models for Verilog Code Generation**
3. **Revisiting VerilogEval: A Year of Improvements in Large-Language Models for Hardware Code Generation**
4. **OpenLLM-RTL: Open Dataset and Benchmark for LLM-Aided Design RTL Generation**

### 02 — FSM and Hardware Reasoning

5. **Enhancing Finite State Machine Design Automation with Large Language Models and Prompt Engineering Techniques**

### 03 — Ambiguity and Underspecification

6. **Addressing Lexical and Semantic Ambiguity in Natural Language Requirements**
7. **Requirements Ambiguity Detection and Explanation with LLMs: An Industrial Study**

### 00 — Working Base Paper

8. **LLM-FSM: Scaling Large Language Models for Finite-State Reasoning in RTL Code Generation**

## Files requiring title identification

The repository also contains six older PDFs with numeric filenames (`7.pdf`, `10.pdf`, `11.pdf`, `12.pdf`, `13.pdf`, `14.pdf`). Their binary contents are not exposed by the available GitHub text interface, so they are intentionally not renamed by guesswork. Once their titles are confirmed, they should be moved into the appropriate folders among `03`, `04`, `05`, `06`, or `07`.

## Related literature not yet present in this repository

The 15-paper literature set also includes **Interactive Agents to Overcome Ambiguity in Software Engineering (Ambig-SWE)**, which is not currently visible as a PDF in this repository and therefore has not been fabricated or placed here.
