# P02 stateful strategy

Read the actual SystemVerilog with Yosys; flatten and use `clk2fflogic` to
preserve explicit clock edges, then `write_smt2 -wires`. Run Yosys-SMTBMC with Z3:
12 global-step BMC, temporal induction with a maximum of 12 steps, and 16-step
cover search. Run the wrong reset control with the same 12-step BMC.
Each command has a 180-second wall timeout. BMC alone is bounded evidence;
unbounded safety requires BOTH base-case BMC and induction to pass.
Twelve steps exceed initialization/history warm-up and allow several clock edges;
16 cover steps allow load-one, reset, and subsequent load-one plus between-edge
reset changes. These bounds are search budgets, not a completeness claim.
P01's depth=1 is neither copied nor relied upon.

The initial clock is low to establish a known edge origin. Initial q is unconstrained;
no reset is assumed, no clock fairness is needed for safety, and rst/d are arbitrary.
At rising steps only, rst and d equal their preceding-step values. This expresses
stable digital sampling (no analog setup/hold or same-instant race model).
There is no requirement to reset before use. Clock may stall high or low, fall,
or rise; inputs can change on every non-rising step, including reset between edges.
Properties use the pre-edge sampled inputs. All assertions start after one history
sample and check the first observed rising edge as well as all subsequent steps.

Covers seek both initial q values, normal loads of zero/one, reset with d=1,
between-edge reset assertion while q=1 at both clock levels, and load after reset.
This checks reachability rather than claiming that a safety proof alone avoids vacuity.
The negative control changes reset polarity; it is never a plausible reading of P02.

Reference: https://yosyshq.readthedocs.io/projects/yosys/en/v0.50/cmd/clk2fflogic.html
Tool-specific command help and versions are retained by the runner.

After run-01, an additional asynchronous-reset negative control was added to test
the between-edge hold assertion directly. It uses the identical environment and
12-step BMC. Run-01 is preserved; the expanded final suite is run-02.
