# Interpretation 01 — Intended Behavior

The module is purely combinational.

For every legal Boolean assignment of `a`, `b`, and `sel`:

- If `sel == 1'b0`, output `y` equals `a`.
- If `sel == 1'b1`, output `y` equals `b`.

No clock, reset, enable, storage element, latency, or state behavior is present or implied.
