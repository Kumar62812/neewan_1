# P05 requirement — response timing candidate v1

> Design a request acknowledgment circuit with one-bit inputs clk, rst, req and
> one-bit output ack. Requests are sampled on rising clock edges. Respond to each
> request with a one-cycle acknowledgment pulse. Reset is synchronous, active high,
> overrides requests, and clears acknowledgment and pending requests. Hold stored
> values between rising edges. Initial stored values are unspecified.

Legal request protocol: outside reset, successive sampled requests have at least
one rising edge with req=0 between them. Reset cancels outstanding requests.
The observable is ack after each edge and between edges. No output latency is
specified beyond the phrase “respond to each request.”

Provenance: original candidate constructed by Codex on 2026-10-10 for the user's
repository continuation. Written before interpretations/specifications/RTL.
This is a proposed timing-ambiguity case, not a certified ambiguity case.
