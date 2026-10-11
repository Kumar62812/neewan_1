# P05 strategy

Use the same explicit-clock transformation and stable-edge sampling convention
as P02, with independently specified A/B equations. B's first non-reset output
is unconstrained by the specification; after one edge, the previous sampled
request defines its next value. Neither initial output is forced to zero.

Prove each reference against its equation and hold property with 12-step BMC
plus up-to-12-step induction. Seek both directions of post-reset divergence
with 16-step cover. Finally assert post-reset equality under the same environment
and run 12-step BMC to retain a distinguishing counterexample. A FAIL on this
last task means a behavioral distinction, not a failed reference implementation.
Bounds allow reset, request capture, delayed response, and idle intervals;
unbounded conformance is claimed only if both BMC and induction pass.
Every command has a 180-second wall timeout. No linguistic judgment follows
from formal results. See P02 STRATEGY.md for the tool documentation reference.
