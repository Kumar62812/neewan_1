# FORMAL-AMBIG-RTL — Current Project Brief

**Status date:** 2026-10-07

## Project position

P01 professor review is recorded as approved to proceed to P02. This is a project-direction record and does not imply an independently signed certification dossier.

## Research question

How can we decide, defensibly and reproducibly, whether a natural-language RTL requirement is ambiguous, and evaluate LLM-generated RTL without confusing interpretation differences with implementation differences?

## Evidence chain

`R → I → S → RTL → F → C`

Different RTL alone is not evidence of linguistic ambiguity.

## P01

P01 is a C1 unambiguous-deterministic control: a combinational 2-to-1 multiplexer.

Formal evidence is complete for the documented effective tested source:

- pinned base: `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`
- retained path-only SBY patch SHA-256: `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`
- accepted archive: `re/p01-20260930T220622Z-rev1.tar.gz`
- archive SHA-256: `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`

Reference RTL: PASS. Deliberately wrong RTL: assertion FAIL with retained counterexample `a=0,b=1,sel=1`.

## P01 non-claims

P01 does not establish a certified ambiguous case, benchmark-wide validity, complete LLM methodology validity, or that the unmodified pinned revision passed.

## P02

P02 is a deterministic sequential pilot: one-bit register with synchronous active-high reset.

Current state:

`Requirement: DRAFT PROPOSED`

`Interpretation: DRAFT PROPOSED`

`Specification: DRAFT PROPOSED`

`RTL: NOT IMPLEMENTED`

`Formal verification: NOT EXECUTED`

`Evidence: NOT GENERATED`

## Requested/recorded direction

Proceed with P02 using the reviewed P01 workflow while preserving P01 accepted evidence unchanged.

Approval date, mode, and exact professor wording are not stated here because they were not supplied.
