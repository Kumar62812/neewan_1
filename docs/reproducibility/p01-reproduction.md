# P01 Reproduction Boundary

## Purpose

Define what a clean-checkout reproduction can and cannot claim.

## Required source lineage

The accepted P01 formal result is associated with:

1. pinned base revision `6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`;
2. retained path-only SBY patch with SHA-256 `71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`;
3. accepted evidence archive `p01-20260930T220622Z-rev1.tar.gz` with SHA-256 `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b`.

## Reproduction sequence

```text
clean checkout
    ↓
verify pinned revision
    ↓
verify retained patch SHA-256
    ↓
apply patch to a disposable working tree
    ↓
record exact Yosys / SBY / Z3 versions
    ↓
run reference and wrong-RTL formal jobs
    ↓
inspect native SBY results and counterexample
    ↓
write a NEW run identifier and NEW evidence package
```

The accepted archive is evidence to compare against; it is not a writable output directory.

## Toolchain recorded by the retained execution record

- Yosys 0.33
- SymbiYosys SBY v0.69
- Z3 4.8.12
- `smtbmc z3`
- BMC depth 1

A future reproduction must record the actual installed versions.

## Current project transition

P01 reproduction rules remain unchanged. Professor approval to begin P02 does not authorize changing historical P01 evidence.

P02 must produce its own requirement, interpretation, specification, RTL, formal configuration, run record, and evidence package in sequence.
