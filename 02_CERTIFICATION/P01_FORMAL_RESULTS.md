# P01 Formal Results Summary

## Effective tested source

| Item | Value |
|---|---|
| Base revision | `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35` |
| Patch | Retained path-only SBY repair |
| Patch SHA-256 | `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4` |
| Tools | Yosys 0.33; SBY v0.69; Z3 4.8.12 |
| Mode | BMC, depth 1 |
| Input assumptions | No assumptions on `a`, `b`, or `sel` |

## Results

| Design | Expected | Retained |
|---|---|---|
| Reference RTL | PASS | PASS |
| Deliberately wrong RTL | Assertion FAIL | Assertion FAIL |

Counterexample:

`a=0, b=1, sel=1, required y=1, observed y=0`.

## Evidence

Accepted archive:

`re/p01-20260930T220622Z-rev1.tar.gz`

SHA-256:

`32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`

## Non-claims

This result does not establish linguistic ambiguity, two plausible P01 interpretations, benchmark-wide validity, complete LLM methodology validity, or that the unmodified pinned revision passed.
