# P05 behavioral specifications

Index n denotes a rising edge; req[n] and rst[n] are sampled there; ack[n]
is the value just after that edge. Every variable is Boolean.

A: ack[n] = rst[n] ? 0 : req[n].

B: pending[n] = rst[n] ? 0 : req[n];
ack[n] = rst[n] ? 0 : pending[n-1].
The initial pending value is unconstrained, as is initial ack for both readings.
At the first edge without reset, B may therefore output an arbitrary Boolean.
A reset edge clears all state. Both ack values and B's pending value hold
between rising edges. A reset cancels the pending response even if req=1.

The distinction must be shown after a shared reset to exclude independent
unconstrained initial values as the cause. Illustrative (not executed) trace:
reset edge -> request edge -> idle edge gives A ack: 0,1,0; B ack: 0,0,1.

Environment: clock initially low; sampled rst/req stable across a rising global
step; otherwise arbitrary. No forced reset in the proof, but the equality
comparison and distinguishing cover are enabled only after a sampled reset.
The isolated-request protocol is enforced outside reset, including reset cancellation.
