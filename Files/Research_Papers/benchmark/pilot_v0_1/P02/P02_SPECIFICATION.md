# P02 Behavioral Specification

## Update equation

```text
q_next =
    0, if rst = 1
    d, if rst = 0
```

Equivalently:

```text
q_next = rst ? 1'b0 : d
```

The update is evaluated at each rising edge of `clk`.

## Behavior table

| Rising edge? | rst | d | Required next q |
|---|---:|---:|---:|
| yes | 0 | 0 | 0 |
| yes | 0 | 1 | 1 |
| yes | 1 | 0 | 0 |
| yes | 1 | 1 | 0 |
| no | X | X | retain previous q |

Here X denotes an irrelevant/unspecified value for that table row, not a SystemVerilog four-state value.

## Initial state

Before the first rising edge, `q` is unspecified.

No initial-value assumption is part of the specification.

## Example edge sequence

| Edge | rst | d | q after edge | Reason |
|---:|---:|---:|---:|---|
| 1 | 0 | 1 | 1 | load d |
| 2 | 0 | 0 | 0 | load d |
| 3 | 1 | 1 | 0 | reset has priority |
| 4 | 0 | 1 | 1 | load d after reset release |

Between edges, `q` retains the value established at the most recent rising edge.

## Consistency statement

This specification is directly derived from P02_REQUIREMENT.md and P02_INTERPRETATION.md. No RTL-specific behavior is added.
