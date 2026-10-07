# P02 Interpretation

## Selected interpretation

The requirement is interpreted as a deterministic sequential register with these semantics:

1. State changes only on a **rising edge** of `clk`.
2. `rst` is **synchronous**: its value is sampled at the rising edge; it does not independently change `q` between clock edges.
3. `rst=1` has **priority** over `d`.
4. When `rst=0` at a rising edge, `d` is loaded into `q`.
5. Between rising edges, `q` retains its previous state.
6. The initial value of `q` before the first rising edge is **unspecified**.

## Interpretation rationale

“At every rising edge” establishes edge-triggered sequential behavior. “If rst is 1, set q to 0. Otherwise, load d” establishes synchronous reset and reset priority. “Between rising edges, q retains its previous value” establishes state retention. The explicit unspecified initial-state sentence prevents an unstated time-zero assumption.

## Scope boundary

This interpretation does not add asynchronous reset behavior, initialization, enable logic, extra latency, or a pre-first-edge state assumption.
