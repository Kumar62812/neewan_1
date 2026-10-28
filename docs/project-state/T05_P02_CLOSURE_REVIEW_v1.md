# T05 — P02 requirement/specification consistency and provenance: closure review v1

**Status: DRAFT FOR AUTHOR APPROVAL. Not DONE until the author approves this named version.**
Prepared 2026-10-28 as a read-only review of branch `research/end-to-end-sequence` at commit
`109336c88433be1c3f5836bfde351b5e0c841b0c`. No P02 source, evidence or run file was modified.
No formal tool was rerun; no new provenance ID is created. Reviewer: Claude (automated technical
review). This is not a human plausibility review or a certification decision.

## 1. Scope

T05 closes when four things are recorded and the author approves them:

1. Clause-level traceability from requirement (R) to interpretation (I), specification (S), RTL and formal property (F).
2. The clock, reset and initial-state modelling assumptions, stated explicitly.
3. Full SHA-256 values for every tested input.
4. A provenance statement that ties the evidence to source **content**, not to a commit identity.

T06 (P02 formal/provenance closure) is not started by this document.

## 2. Clause traceability

R = `P02_REQUIREMENT.md`, I = `P02_INTERPRETATION.md`, S = `P02_SPECIFICATION.md`,
RTL = `reference_rtl/register.sv`, F = `formal/properties/register_properties.sv` (line numbers), H = `formal/harness.sv`.

| # | Requirement clause (R) | I | S | RTL | Formal evidence | Negative control that exercises it |
|---|---|---|---|---|---|---|
| C1 | One-bit register, ports `clk`, `rst`, `d`, `q` | §1 | Interface | module ports | H instantiates the four ports | — |
| C2 | Update at every rising edge of `clk` | item 1 | Update equation | `always @(posedge clk)` | F:8 guard `!$past(clk) && clk` | — |
| C3 | `rst`=1 at an edge sets `q` to 0 (active high) | items 2–3 | Table rows 3–4 | `if (rst) q <= 0` | F:9 `assert(q == 0)` | `wrong_reset.sv` fails at F:9 |
| C4 | Reset is synchronous | item 2 | Reset statement | no `rst` in sensitivity list | F:18 between-edge hold | `wrong_async.sv` fails at F:18 |
| C5 | Reset has priority over `d` | item 3 | Table row 4 (rst=1, d=1 → 0) | `if/else` order | F:9; cover F:11 (rst=1, d=1, q=0) | `wrong_reset.sv` |
| C6 | Otherwise load sampled `d` | item 4 | Table rows 1–2 | `else q <= d` | F:10 `assert(q == $past(d))`; covers F:12–13 | — |
| C7 | Between rising edges `q` holds | item 5 | Between-edges row | edge-only process | F:18 `assert(q == $past(q))`; covers F:19–20 (reset asserted between edges, both clock levels) | `wrong_async.sv` |
| C8 | `q` before first rising edge unspecified | item 6 | Initial state | no initialiser | H leaves `q` unconstrained; covers F:23–24 reach both initial values | — |
| C9 | No enable | item 7 | Interface | no enable port | Structural only (no port exists); no property needed | — |
| C10 | Boolean scope; no X/Z claim | item 8 | Boolean scope | — | `clk2fflogic` two-valued SMT model | — |

All ten clauses trace end to end. The eight cover goals are F:11, 12, 13, 16, 19, 20, 23, 24, which matches the eight PASS covers recorded in run-02.

## 3. Modelling assumptions (from `harness.sv`, `STRATEGY.md`, `run.py`)

| Assumption | Where | Comment |
|---|---|---|
| Method: Yosys `prep; flatten; clk2fflogic; write_smt2 -wires`, then Yosys-SMTBMC with Z3. **No `.sby` file exists for P02.** | `run.py` | Matches the reference document. Tool: yowasp-yosys 0.63 (70a11c6bf), Z3 4.15.4 |
| Bounds: BMC 12 steps, induction ≤ 12, cover 16; 180 s wall timeout per command | `run.py`, `STRATEGY.md` | Reference BMC + induction both PASS, so safety is unbounded within the model |
| Clock is low at the first step | H line 15 `assume(!clk)` | Gives a defined first rising edge; not stated in R (see O3) |
| Clock otherwise arbitrary: may rise, fall or stall | H `anyseq` | No fairness needed for safety |
| `rst` and `d` equal their previous-step value at a rising step | H lines 18–19 | Stable-sampling abstraction; no analog setup/hold or same-instant race |
| `rst` and `d` may change on **every non-rising step**, i.e. while `clk` is low **and** while `clk` is high | H | Broader than "reset may change while clk low"; cover F:19 (clk low) and F:20 (clk high) both reached |
| `q` initial value unconstrained; no reset-before-use assumption | H | Matches C8 |

## 4. SHA-256 record (full values)

All 50 entries in `evidence/run-02/SHA256SUMS.json` were recomputed: **0 mismatches, 0 unlisted files, 0 missing files.**
Tested inputs, comparing the run-02 snapshot (`evidence/run-02/source/…`) with the live file at the commit above:

| File | SHA-256 | Live = snapshot |
|---|---|---|
| P02_REQUIREMENT.md | `9677855ab6c9c90aba6307b16fbe88ef64bd31eae30e63f6101ed9c5267f9a64` | yes |
| P02_INTERPRETATION.md | `331144c69b03df40bd8dcf05cab120083794c315a6e08ab4086f16be5ab4155d` | yes |
| P02_SPECIFICATION.md | `8ac494bb96f34a32f6c655ed4a47be1a61f47ab0aa3075d09878a86a2fc81688` | yes |
| P02_CONSISTENCY_REVIEW.md | `90765a3cbada753818d4aa2fab2b8f09769d1cc50d00bb744d9d1fb86d89e5e7` | yes |
| reference_rtl/register.sv | `891316d1f241693a87fb920b02be29639c65c979c3331d238633fcaa6dd1619f` | yes (also equals `metadata.json`) |
| validation_rtl/wrong_reset.sv | `eb7054c272023e5cb882e91bb12f388b5bf2209f219e57f71b3c0ae753d818c8` | yes |
| validation_rtl/wrong_async.sv | `0a4a40f7049eb0ba7555821a71d45063fd0ef8151763c361f0eb3b03b30c78e2` | yes |
| formal/harness.sv | `ab541f117834839ac3b8d1232eb83a6bf404d9c448d408ae6bd8cd6687bb1c47` | yes |
| formal/properties/register_properties.sv | `5b56301bca34a2df25551a93a50abc2cd00d2bed270ad649dd80dd65ac2ec5a8` | yes |
| formal/run.py | `2c44101bad7aa440a6a38d977d0ec4254300484fce70f2ba219122bb77b8f27d` | yes |
| formal/STRATEGY.md | `f129f7ffbce7a83639c4c26a3f009fb1785c6e5e6749a614f9a2c421d4b4b093` | yes |

Recorded statuses in run-02 logs: reference BMC PASSED, induction PASSED, cover PASSED (8/8); `wrong_reset` BMC FAILED at F:9; `wrong_async` BMC FAILED at F:18. Each failure has a retained `.vcd` and `.yw` witness.

## 5. Provenance statement

Three different commit identities are attached to P02 evidence:

- `ebc6e8a81669d9c8a4ff7b47f2de6d96d507c720`: `environment.json` base commit and `metadata.json`
- `0874a36608a249b3c2c89ccc35e637936bd2987f`: "tested source commit" in `P02_READINESS.md`
- `109336c88433be1c3f5836bfde351b5e0c841b0c`: the current branch head

The runner snapshots and hashes the exact inputs it read, so **the run-02 evidence is equivalent by content, not by commit identity**: every tested input at `109336c` is byte-identical to the run-02 snapshot (§4). The commit labels are informational; the hashes are the binding provenance. Run-02 was executed on macOS-15.5-arm64, Python 3.12.1, 2026-10-09T23:22 UTC (local paths are recorded in `runs.json`).

## 6. Observations needing an author decision

None of these invalidates the run-02 result. Fixing any of O1, O2, O5 changes a tested file's hash, so a fix belongs to a new versioned revision (with a rerun under a new provenance ID), not a silent edit.

| ID | Severity | Observation | Options |
|---|---|---|---|
| O1 | Low | `P02_INTERPRETATION.md` line 30 still contains a corrupted LaTeX fragment: `(q_{<TAB>ext{next}})` (`\t` was interpreted as a tab). `P02_CONSISTENCY_REVIEW.md` says the rendering was repaired; it was only repaired in the specification. The semantic equation on line 28 is correct. | (a) accept as cosmetic and note it; (b) fix in an I-v2 and rerun |
| O2 | Low | `metadata.json` `input_assumptions` reads "rst and data/**request** stable", which carries over a P05 term. | Same as O1 |
| O3 | Low | The harness assumes `clk` starts low and asserts between-edge hold **from the first step**, so `q` must also stay constant before the first rising edge. R only says that value is "unspecified". For a register this is the natural reading, but the formal model is slightly stronger than the text. | (a) accept and record it as a modelling assumption; (b) relax the hold assertion until the first edge in a v2 |
| O4 | Medium | The reference document lists P02 as a **core** benchmark case, but `metadata.json` says `primary_ambiguity_dimension: none` and `"Not an ambiguity candidate"`. P02 behaves like a second deterministic control. | Author to state P02's role (deterministic control vs. ambiguity case) before T06/T08 |
| O5 | Low | `P02_RESULTS.md` and `metadata.json` are not inside the run-02 snapshot (they were written after the run). That is expected, but their hashes should be recorded at T05 approval: `P02_RESULTS.md` `0b508df3c4569bf1ecdc026e70f47e89d1f002b533fc6dd5fe13bac00382bb6b`, `metadata.json` `6488b260226c633098d69c3e5dbbd87fd0cd5614ef44993df862d2abe35affde`. | Record these in the approval entry |

## 7. Approval request

> I approve **T05_P02_CLOSURE_REVIEW_v1** (this file, at the SHA-256 recorded in the approval register) as the T05 closure version, with decisions on O1–O5 as recorded below.
>
> O1: ___ O2: ___ O3: ___ O4: ___ O5: ___
> Author: __________ Date: __________

Until this block is completed, T05 stays **PENDING** and T06 stays **BLOCKED**.
