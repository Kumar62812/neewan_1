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

```
y = a, if sel = 0
y = b, if sel = 1
```

The required behavior is purely combinational. No clock, reset, enable, storage, latency, or state behavior is part of this specification.
