# P01 Requirement

Implement a combinational 2-to-1 multiplexer.

## Inputs

- `a`: 1-bit data input.
- `b`: 1-bit data input.
- `sel`: 1-bit select input.

## Output

- `y`: 1-bit output.

## Required behavior

- When `sel` is `0`, `y` shall equal `a`.
- When `sel` is `1`, `y` shall equal `b`.

The module is combinational. It has no clock, reset, enable, storage element, or latency.
