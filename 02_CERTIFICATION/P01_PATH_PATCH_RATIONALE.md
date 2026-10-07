# P01 Path-Only SBY Patch Rationale

## Purpose

Document the retained path-only repair used for the accepted P01 formal-evidence run.

## Pinned base revision

`6d09dca0e6d8292d0b4cf13ff19b3ed06ec3de35`

## Patch SHA-256

`71bee3408a34460b8c84bc34838779ff6cea0316662f1d6f8d35742be7e7d5c4`

## Problem

The unmodified pinned formal setup had an SBY/Yosys staged-source path-resolution defect.

## Repair scope

The retained patch changes only source-path references in the formal SBY flow.

The patch does not change:

- reference RTL functionality;
- deliberately wrong RTL functionality;
- shared property logic;
- harness interfaces;
- Boolean input contract;
- formal assumptions;
- solver;
- proof mode;
- proof depth;
- expected outcomes.

## Claim boundary

Allowed:

> The documented effective tested source completed the P01 formal-evidence flow.

Not allowed:

> The unmodified pinned revision passed formal verification unchanged.
