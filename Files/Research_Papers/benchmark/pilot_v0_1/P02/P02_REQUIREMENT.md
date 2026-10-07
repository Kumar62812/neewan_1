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

## Required behavioral details

- **Design:** one-bit register.
- **Clock:** update on rising edges of `clk`.
- **Reset polarity:** active high.
- **Reset timing:** synchronous.
- **Reset priority:** reset overrides data loading.
- **Reset behavior:** at a rising edge with `rst=1`, set `q` to 0.
- **Normal behavior:** at a rising edge with `rst=0`, load sampled `d` into `q`.
- **Between edges:** hold the previous `q`.
- **Initial state:** `q` is unspecified before the first rising edge.
- **Enable:** none.
- **Formal scope:** Boolean behavior; four-state SystemVerilog X/Z behavior is not claimed.

## Scope

This artifact records only the natural-language requirement and port definitions. It does not define an RTL implementation or formal result.
