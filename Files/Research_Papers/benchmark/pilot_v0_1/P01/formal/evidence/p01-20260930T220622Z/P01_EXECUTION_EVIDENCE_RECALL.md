# P01 Execution and Evidence Recall Record

## 1. Document Control

| Field | Value |
|---|---|
| Project | FORMAL-AMBIG-RTL |
| Instance | P01 |
| Document title | P01 Execution and Evidence Recall Record |
| Purpose | Future recall, reproduction, revision, and methodology transfer |
| Status | Retrospective record; certification pending |
| Current gate state | **R ✓ → I ✓ → S ✓ → RTL ✓ → F ✓ → C: PENDING** |
| Record author | Project record — prepared from retained execution evidence |
| Record date | 2026-10-01 |
| Document version | v1.0 |

### Change log

| Date | Version | Author | Description |
|---|---|---|---|
| 2026-10-01 | v1.0 | Project record | Initial retrospective P01 execution, evidence, and lessons-learned record |

This document is a retrospective execution/evidence/lessons-learned record. It is not a certification decision and does not populate or alter the independent certification decision.

---

## 2. P01 Identity and Objective

P01 is the FORMAL-AMBIG-RTL golden methodology-validation instance.

**Proposed category:** C1 — Unambiguous–Deterministic

**Design:** One-bit combinational 2-to-1 multiplexer.

**Inputs:**
- `a`: one-bit data input
- `b`: one-bit data input
- `sel`: one-bit select input

**Output:**
- `y`: one-bit output

**Functional requirement:**

```
sel = 0 → y = a
sel = 1 → y = b
```

Equivalent Boolean expression:

```
y = sel ? b : a
```

The module is combinational and has no clock, reset, enable, storage element, or latency.

The retained project specification identifies P01 as the C1 unambiguous control used to validate the end-to-end workflow before later pilot cases.

---

## 3. Evidence-Chain Summary

The required evidence chain is:

```
R → I → S → RTL → F → C
```

| Stage | Meaning | P01 artifact or evidence | Current status | Key restriction |
|---|---|---|---|---|
| R | Natural-language requirement | `P01/requirement.md` | ✓ Complete | Exact requirement must be retained |
| I | Defensible interpretation | `P01/interpretations/interpretation_01.md` | ✓ Complete | Interpretation must remain independent of RTL |
| S | Behavioral specification | `P01/behavioral_specification/specification_01.md` | ✓ Complete | Specification must remain RTL-independent |
| RTL | Reference and negative-control implementations | `reference_rtl/rtl_01.sv`; `validation_rtl/deliberately_wrong_rtl.sv` | ✓ Complete | Wrong RTL is a negative control, not an alternate interpretation |
| F | Formal verification evidence | Accepted P01 formal-evidence archive and independent formal audit | ✓ Complete | Scope is the effective tested source only |
| C | Certification decision | P01 Certification Dossier / reviewer decision | **PENDING** | Only an independent reviewer may decide |

The scientific layers must remain separate:

- Interpretation is not RTL.
- Behavioral specification is not reference RTL.
- Formal proof evidence is not linguistic plausibility evidence.
- Different RTL is not, by itself, evidence of ambiguity.

For ambiguity cases, the project methodology requires linguistic plausibility and formal behavioral distinction; different implementations alone are insufficient.

---

## 4. Behavioral Contract

### Truth table

| `sel` | `a` | `b` | Required `y` |
|---:|---:|---:|---:|
| 0 | 0 | X | 0 |
| 0 | 1 | X | 1 |
| 1 | X | 0 | 0 |
| 1 | X | 1 | 1 |

Here `X` means Boolean irrelevance for that table row. It does not mean SystemVerilog four-state unknown semantics.

The single behavioral relation is:

```
y = sel ? b : a
```

The retained specification explicitly defines the input domain as:

```
a, b, sel ∈ {0, 1}
```

and defines `X` as a don't-care Boolean value, not `1'bx`.

---

## 5. Formal Verification Design

P01 uses two formal jobs against one shared property.

### Reference RTL

The reference implementation is required to satisfy the shared mux property.

Expected formal outcome:

```
PASS
```

### Deliberately wrong RTL

The negative-control implementation swaps the selected inputs:

```
sel = 0 → y = b
sel = 1 → y = a
```

Expected formal outcome:

```
Assertion FAIL with a tool-generated counterexample
```

This implementation is deliberately incorrect and is **not** treated as a plausible alternate interpretation.

### Shared formal property

```systemverilog
assert (y == (sel ? b : a));
```

Both jobs are required to retain the same:

- Boolean input contract
- Observable output
- Assertion/property
- Solver and engine configuration
- BMC bound/depth
- Interface assumptions

The accepted formal evidence records Yosys 0.33, SymbiYosys SBY v0.69, and Z3 4.8.12 with BMC depth 1 and `smtbmc z3`.

---

## 6. Execution History and Lessons Learned

### Attempt 1 — Runner permission problem

**Result:**
- Shell exit status: **126**
- Error: permission denied

**Cause:**

The runner did not have executable permission in the checkout.

**Preferred reproducible invocation:**

```bash
bash ./run_p01_formal.sh
```

This avoids changing the worktree file mode merely to execute the script.

### Attempt 2 — SBY path-resolution/configuration failure

**Pinned base revision:**

```
6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35
```

**Runner result:**
- Runner exit: **3**
- Reference SBY internal result: **ERROR, rc=16**

**Key error:**

```
Can't open input file '../reference_rtl/rtl_01.sv'
```

This was an SBY/Yosys staging/path configuration failure, not a failed reference formal proof.

The unmodified pinned revision is **not** claimed to have formally passed.

### SymbiYosys staged-file lesson

The `[files]` section identifies files from their source-tree locations.

The `[script]` block executes in the SBY-generated staged environment, so it should read the staged basenames.

Correct pattern:

```
[files]
../reference_rtl/rtl_01.sv

[script]
read_verilog -formal -sv rtl_01.sv
```

Incorrect pattern:

```
read_verilog -formal -sv ../reference_rtl/rtl_01.sv
```

The original relative path was unavailable from the staged `src/` directory.

### Corrective patch

The correction was path-only.

It changed only the SBY source references in:

```
reference.sby
wrong.sby
```

No changes were made to:
- Reference RTL
- Wrong RTL
- Shared property
- Harnesses
- Engine selection
- Solver selection
- BMC depth
- Boolean contract
- Formal assumptions
- Expected results

**Effective tested source:**

```
Pinned base revision + retained path-only SBY patch
```

**Patch SHA-256:**

```
71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4
```

**Important non-claim:**

```
Unmodified pinned base revision is not claimed to have formally passed.
```

### Final evidence-producing run

**Run ID:**

```
p01-20260930T220622Z
```

**Command:**

```bash
cd /content/neewan_1/Files/Research_Papers/benchmark/pilot_v0_1/P01/formal
bash ./run_p01_formal.sh
```

**Runner exit status:** 0

**Reference native SBY result:** PASS

**Wrong-RTL native SBY result:** FAIL

The wrong task's overall SBY command can return zero because `wrong.sby` uses `expect fail`. Native SBY status and engine logs therefore remain authoritative.

---

## 7. Accepted Formal Evidence

**Final evidence-producing run ID:**

```
p01-20260930T220622Z
```

**Formal archive:**

```
p01-20260930T220622Z-rev1.tar.gz
```

**Archive SHA-256:**

```
32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b
```

**Independent formal audit decision:** ACCEPT

**Accepted scope:** Effective tested source only.

The retained evidence categories include:

- Repository and pinned-revision identity
- Path-only patch and patch SHA-256
- Input/source hashes
- Tool versions and executable paths
- Environment metadata
- Exact invocation command
- UTC timestamps
- Standard output and standard error
- Runner exit status
- Reference formal work directory and logs
- Wrong-RTL formal work directory and logs
- Native SBY result/status records
- Generated VCD trace
- Yosys witness
- Generated counterexample/testbench trace
- SMT constraint trace
- Counterexample inspection output
- SHA-256 manifest

The formal-evidence archive passed independent audit.

**Formal evidence status:**

```
F: COMPLETE
```

---

## 8. Formal Results

### Reference RTL

**Accepted formal result:**

```
PASS
```

Meaning: the reference RTL satisfied the shared mux property within the configured Boolean combinational BMC task.

### Wrong RTL

**Accepted formal result:**

```
Assertion FAIL
```

Meaning: the deliberately swapped RTL violated the same shared property.

### Counterexample

Retained tool-generated trace values:

```
a   = 0
b   = 1
sel = 1
observed y = 0
```

Required behavior:

```
required y = sel ? b : a
           = 1 ? 1 : 0
           = 1
```

Therefore:

```
required y = 1
observed y = 0
mismatch = True
```

This is a legal Boolean counterexample that validates the negative control and shows that the swapped implementation selects `a` when `sel=1`, while the requirement selects `b`.

---

## 9. Scope and Non-Claims

The accepted P01 evidence establishes only:

- One-bit combinational 2-to-1 mux behavior.
- Inputs `a`, `b`, and `sel` under the declared Boolean contract.
- One-bit observable output `y`.
- The relation `y = sel ? b : a`.
- Bounded model checking at depth 1, appropriate to this stateless combinational relation.
- Reference-pass and negative-control-fail behavior for the accepted effective source.

It does **not** establish:

- SystemVerilog four-state X/Z semantics.
- Sequential, temporal, clock, reset, latency, or storage behavior.
- Protocol or environment correctness beyond the declared Boolean contract.
- Correctness of larger RTL designs.
- Benchmark-wide validity.
- Validity of the complete LLM evaluation methodology.
- That the wrong RTL is a plausible alternate interpretation.
- That the unmodified pinned revision passed.
- P01 certification.

---

## 10. Reproduction Procedure

For future P01-style reproduction:

1. Check out the recorded pinned revision.
2. Verify the source tree against retained hashes.
3. Apply the retained path-only patch and verify its SHA-256.
4. Verify tool availability and record exact tool versions.
5. Confirm `reference.sby` and `wrong.sby` follow the SBY staged-file path rule.
6. Confirm reference and wrong RTL share the same interface.
7. Confirm the formal property remains independent of either RTL implementation.
8. Invoke the runner using:

```bash
bash ./run_p01_formal.sh
```

9. Preserve raw stdout, stderr, work directories, logs, status records, and counterexample traces.
10. Inspect native SBY results, not only the shell exit status.
11. Inspect and retain the wrong-RTL counterexample.
12. Hash the completed evidence/archive.
13. Obtain an independent formal audit before considering F complete.
14. Obtain independent certification before considering C complete.

---

## 11. Future Improvements

The following are prospective, version-controlled improvements. They are **not** changes to historical P01 evidence.

- Commit the SBY staged-path correction upstream.
- Define and preserve expected runner executable permissions.
- Include runner source directly in future evidence packages.
- Preserve a Git bundle or verified source snapshot.
- Capture tool-binary hashes or container-image digests.
- Use an external timestamp or detached signature for final archives.
- Consider explicit `(* anyseq *)` declarations for formal free inputs if appropriate.
- Retain a unique run ID for every attempt, including failed attempts.
- Maintain a machine-readable run report and audit checklist.
- Keep historical evidence immutable; create new evidence packages for reruns.

---

## 12. Certification Boundary

This record supports future recall, reproduction, and revision. It does **not** certify P01.

The formal-evidence status is accepted only for the retained effective tested source:

```
Pinned base revision
+
retained path-only SBY patch
+
accepted evidence archive
```

The independent certification decision remains blank and pending.

```
R ✓ → I ✓ → S ✓ → RTL ✓ → F ✓ → C: PENDING
```

Only an independent reviewer may record **ACCEPT**, **REJECT**, or **REMEDIATION REQUIRED** in the P01 Certification Dossier.

Only an independent **ACCEPT** may authorize the P01 Golden Template Freeze and subsequent P02–P12 construction.
