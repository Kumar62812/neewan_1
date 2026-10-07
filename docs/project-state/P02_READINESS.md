# P02 Readiness

## Authorization

P02 is authorized to begin based on the professor approval reported by the project owner.

## Required first-stage artifacts

1. `P02_REQUIREMENT.md`
2. `P02_INTERPRETATION.md`
3. `P02_SPECIFICATION.md`

These three artifacts are now present in the repository.

## Consistency check

The requirement specifies:

- rising-edge updates;
- synchronous active-high reset;
- reset priority;
- loading `d` otherwise;
- state retention between rising edges;
- unspecified initial state.

The interpretation states the same semantics without adding asynchronous reset, initialization, enable, or extra latency.

The specification expresses:

`q_next = 0` when `rst=1`, otherwise `q_next=d`,

and includes the corresponding behavior table and example edge sequence.

## Next stage

After these artifacts are reviewed for consistency, P02 reference RTL, deliberate negative control, formal property, and sequential harness may be prepared.

No P02 formal execution or evidence is claimed yet.
