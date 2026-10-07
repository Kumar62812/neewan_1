# P01 Behavioral Specification

## Scope

This specification is defined over legal Boolean input assignments only:

\[
a, b, sel \in \{0, 1\}
\]

| sel | a | b | Required y |
|---:|---:|---:|---:|
| 0 | 0 | X | 0 |
| 0 | 1 | X | 1 |
| 1 | X | 0 | 0 |
| 1 | X | 1 | 1 |

**Notation:** `X` means *don't care*: either Boolean value (`0` or `1`) of that input is permitted in the corresponding row. It is not a SystemVerilog unknown value (`1'bx`) and does not introduce four-state logic into this behavioral specification.

Functional definition:

```text
y = a, if sel = 0
y = b, if sel = 1
```

The required behavior is purely combinational. No clock, reset, enable, storage, latency, or state behavior is part of this specification.

## Pre-RTL Review Record

**Decision:** APPROVED TO PROCEED TO RTL IMPLEMENTATION

The pre-RTL review found the requirement, interpretation, and behavioral specification consistent on the intended Boolean behavior: `sel = 0` selects `a`, and `sel = 1` selects `b`. No reasonable competing behavioral interpretation was identified for the tested behavior.

This decision advances only the pre-RTL review gate. It does **not** constitute formal verification, annotation completion, reproducibility completion, template freeze, or final `UNAMBIGUOUS` certification.
