# P05 candidate interpretations (written before RTL)

A — Sampling-edge response: a sampled request produces ack during the cycle
immediately following that sampling edge. “Respond” is read as the action taken
when the request is sampled; the wording does not require a processing cycle.

B — Following-edge response: a sampled request is stored as pending and produces
ack at the following rising edge. “Respond” is read as a clocked response stage
following request capture; no explicit same-edge deadline excludes that stage.

Both are proposed defensible readings of the omitted response latency, not human
judgments. Each uses the same interface and legal input protocol. Neither is a
mutation of P02 nor a known violation offered as a plausible interpretation.
Whether B adds unjustified latency is a question for blinded human reviewers.
If either reading is rejected, retain this as a rejected candidate; do not certify it.
