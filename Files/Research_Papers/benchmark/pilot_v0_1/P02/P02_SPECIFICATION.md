# P02 Behavioral Specification

## Update equation

[
q_{	ext{next}} =
egin{cases}
0, & rst=1\
d, & rst=0
end{cases}
]

Equivalently:

`q_next = rst ? 1'b0 : d`

Here `q_next` means the value after the register update. `rst` and `d` are sampled at the rising edge.

The update is evaluated at each rising edge of `clk`.

## Required behavior

| Condition | Required behavior |
|---|---|
| Rising edge, `rst=1` | Set `q` to 0 |
| Rising edge, `rst=0` | Load sampled `d` into `q` |
| Between rising edges | Hold the previous `q` |
| Before first rising edge | `q` is unspecified |

Reset is active high, synchronous, and has priority over data loading. There is no enable.

## Boolean scope

The specification concerns Boolean behavior only. Four-state SystemVerilog X/Z behavior is not claimed.

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

Before the first rising edge, `q` is unspecified. No initial-value assumption is part of the specification.

## Example edge sequence

| Edge | rst | d | q after edge | Reason |
|---:|---:|---:|---:|---|
| 1 | 0 | 1 | 1 | load d |
| 2 | 0 | 0 | 0 | load d |
| 3 | 1 | 1 | 0 | reset has priority |
| 4 | 0 | 1 | 1 | load d after reset release |

Between edges, `q` retains the value established at the most recent rising edge.

**Important:** This example sequence is illustrative, not an executed verification result.

## Consistency statement

This specification is directly derived from P02_REQUIREMENT.md and P02_INTERPRETATION.md. No RTL-specific behavior is added.
