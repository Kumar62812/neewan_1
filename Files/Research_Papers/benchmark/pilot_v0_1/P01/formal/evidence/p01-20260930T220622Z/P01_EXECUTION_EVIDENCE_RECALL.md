# P01 Execution and Evidence Recall Record

## 1. Document Control

| Field | Value |
|---|---|
| Project | FORMAL-AMBIG-RTL |
| Instance | P01 |
| Document title | P01 Execution and Evidence Recall Record |
| Purpose | Future recall, reproduction, revision, and methodology transfer |
| Status | Retrospective record; formal evidence complete; review direction recorded |
| Formal-evidence status | **COMPLETE for the documented effective tested source** |
| Current project position | **P01 professor review approved to proceed with P02, according to the project owner's record** |
| Record author | Project record — prepared from retained execution evidence |
| Record date | 2026-10-07 |
| Document version | v1.1 |

This document is a retrospective execution/evidence/lessons-learned record. It does not create or populate an independent certification decision.

## 2. P01 Identity and Objective

P01 is the FORMAL-AMBIG-RTL C1 deterministic control used to validate the end-to-end evidence workflow.

**Design:** One-bit combinational 2-to-1 multiplexer.

**Functional requirement:**

```text
sel = 0 → y = a
sel = 1 → y = b
```

## 3. Evidence-Chain Summary

```text
R → I → S → RTL → F → C
```

| Stage | Meaning | Current status |
|---|---|---|
| R | Natural-language requirement | ✓ Complete |
| I | Defensible interpretation | ✓ Complete |
| S | Behavioral specification | ✓ Complete |
| RTL | Reference + negative-control implementations | ✓ Complete |
| F | Formal verification evidence | ✓ Complete for effective tested source |
| C | Independent certification decision | Separate decision record; not fabricated here |

## 4. Accepted Formal Result

Run ID:

```text
p01-20260930T220622Z
```

Reference native SBY result: **PASS**

Wrong-RTL native SBY result: **FAIL**

Retained counterexample:

```text
a = 0
b = 1
sel = 1
required y = 1
observed y = 0
```

The accepted evidence remains scoped to the pinned base revision plus the retained path-only SBY patch.

## 5. Provenance

Pinned base:

```text
6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35
```

Patch SHA-256:

```text
71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4
```

Accepted archive SHA-256:

```text
32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b
```

**The unmodified pinned revision is not claimed to have passed.**

## 6. Current transition

Professor approval to proceed with P02 is recorded as a project-state input. Exact approval date, mode, and wording were not supplied and are therefore not invented.

The next authorized action is the P02 deterministic sequential requirement → interpretation → specification stage.

No P02 formal result or evidence is claimed by this record.
