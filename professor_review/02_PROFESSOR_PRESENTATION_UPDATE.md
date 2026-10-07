# P01 Professor Presentation — Update Record

The repository presentation update is defined by the following changes.

## Slide 1

Replace the subtitle:

`P01 golden-case certification review`

with:

`P01 Pilot Methodology and Evidence Review`

## New slide after P01 Reference RTL

### What the Formal Tool Receives and Produces

```text
INPUT FILES
• Reference RTL   Correct 2:1 multiplexer implementation
• Wrong RTL   Deliberately swapped-input mux; negative control
• Shared property   Required behavior: y = sel ? b : a
• Harness files   Connect the selected RTL to the same property
• SBY configuration files   Specify source files, top module, solver, and proof depth
• Runner script   Executes the two formal checks consistently

FORMAL TOOL FLOW
SymbiYosys + Yosys + Z3
Bounded Model Checking, depth 1
No assumptions on a, b, or sel

OUTPUT EVIDENCE
Reference RTL → PASS
Wrong RTL → Assertion FAIL
Failure output → Counterexample trace / waveform
Evidence → Logs, manifests, hashes, accepted archive
```

Bottom equation:

`RTL + Property + Harness + SBY Configuration → Formal Tool → PASS/FAIL + Logs + Counterexample`

## Final slide

Title:

`P01 Status and Requested Guide Direction`

Content:

```text
P01 STATUS
R ✓ → I ✓ → S ✓ → RTL ✓ → F ✓ → Guide Review Pending

P01 formal-evidence scope: Pinned base revision + retained path-only SBY patch

What P01 establishes:
• A traceable formal-evidence workflow for a C1 deterministic control case
• Correct reference RTL passes the retained property
• Deliberately wrong RTL fails the same property
• Evidence and provenance are retained and hash-verified

What P01 does not yet establish:
• A certified ambiguous benchmark case
• Benchmark-wide methodology validity
• LLM ambiguity-handling performance
• Authorization for P02–P12 execution

GUIDE DIRECTION REQUESTED
1. Proceed with P02 using this workflow
2. Proceed after specified corrections
3. Revise P01 before proceeding
```

The binary presentation was updated in the working project artifact; this Markdown record preserves the exact intended presentation changes in the repository.
