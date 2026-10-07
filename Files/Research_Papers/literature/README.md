# Literature Matrix Guide

## Purpose

`literature_matrix.csv` is the evidence map for the FORMAL-AMBIG-RTL literature review.

It is intended to answer two questions:

1. What does each paper actually contribute?
2. What capability remains missing or insufficiently addressed for FORMAL-AMBIG-RTL?

The matrix is an evidence-tracking document, not a ranking of papers.

## Required discipline

For each paper:

- verify bibliographic metadata against the primary source;
- distinguish paper-reported facts from project interpretation;
- record "Not reported" rather than guessing;
- identify the paper's role in the research chain;
- describe limitations conservatively;
- link the paper to the specific FORMAL-AMBIG-RTL requirement it informs.

## Recommended workflow

1. Read the paper's abstract and methodology.
2. Inspect the evaluation setup and benchmark.
3. Record whether formal verification is actually used.
4. Record whether multiple interpretations or multiple valid outputs are supported.
5. Record whether interaction/clarification is evaluated.
6. Record human-validation methodology where present.
7. Record the limitation relevant to this project.
8. Revisit the row when the literature review changes.

## Role categories

Suggested roles include:

- LLM-to-RTL benchmark
- FSM/hardware reasoning
- ambiguity/clarification
- formal verification
- requirements engineering
- benchmark/evaluation
- related work

## Gap-analysis rule

Do not claim that a paper "does not address X" unless the paper was checked for X. Prefer wording such as:

> "The reported evaluation focuses on Y; the paper does not report the proposed multi-interpretation ambiguity protocol."

## Matrix maintenance

When adding a paper:

- add one row;
- use a stable citation key;
- add the PDF to the appropriate folder when licensing permits;
- add DOI/arXiv/publisher information;
- update this README if the role taxonomy changes.

Do not reorder rows to create rankings. The matrix is organized for traceability, not scoring.
