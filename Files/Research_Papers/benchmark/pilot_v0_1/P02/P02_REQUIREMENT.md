# P02 Requirement

## Case

**P02 — One-bit register with synchronous active-high reset**

## Requirement

> Design a one-bit register with inputs `clk`, `rst`, and `d`, and output `q`. At every rising edge of `clk`, if `rst` is 1, set `q` to 0. Otherwise, load `d` into `q`. Between rising edges, `q` retains its previous value. The value of `q` before the first rising edge is unspecified.

## Port definitions

| Port | Direction | Width | Role |
|---|---|---:|---|
| `clk` | input | 1 | Clock |
| `rst` | input | 1 | Synchronous active-high reset |
| `d` | input | 1 | Data input |
| `q` | output | 1 | Stored output |

## Scope

This artifact records only the natural-language requirement and port definitions. It does not define an RTL implementation or formal result.
