# P05 freeze record — v1 (provisional hash audit)

**Immutable source snapshot:** `main` at commit `83046997dce165fd3b40c190f7dffa1e280b2c86`, the base commit for pipeline PR #7. The exact source files are pinned by this commit and the Git blob IDs below.

## Frozen source artifacts

- `Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_REQUIREMENT.md` — Git blob SHA `a544fa83625266cabae7642d4b6cb356ccf0c9f6` — [source file](https://github.com/Kumar62812/neewan_1/blob/main/Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_REQUIREMENT.md)
- `Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_INTERPRETATIONS.md` — Git blob SHA `31fedca9a16de2b35027ee87dd2e003a38bf35eb` — [source file](https://github.com/Kumar62812/neewan_1/blob/main/Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_INTERPRETATIONS.md)
- `Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_SPECIFICATIONS.md` — Git blob SHA `65a34d0c689cdbbdba567cc306fa34041e920a87` — [source file](https://github.com/Kumar62812/neewan_1/blob/main/Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_SPECIFICATIONS.md)

## Hash audit status

The source commit and Git blob identities above are recorded. **SHA-256 of the three source files has not yet been independently recomputed and recorded in this manifest.** Do not treat Git blob SHA values as SHA-256; they are different hash schemes. This is an explicit outstanding freeze-audit item and must be completed before the first LLM experiment. Do not edit the frozen source files; any intended change requires a new versioned candidate and manifest.

## Interpretation index

- Requirement: response acknowledgment circuit with one-bit `clk`, `rst`, `req`, `ack`; rising-edge sampling; one-cycle acknowledgment; synchronous active-high reset; isolated-request protocol; response latency phrase is underspecified.
- Interpretation A: sampled-edge response.
- Interpretation B: following-edge response using pending state.
- The three source files above are authoritative; this index is not a replacement for their full wording.

## Required status (verbatim)

> Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.

## Blinded review firewall

Do not disclose model outputs, formal results, witnesses/counterexamples, or the researcher's preferred outcome to reviewers before their judgments are locked. The formal distinction does not establish human plausibility. Final P05 LLM evaluation remains blocked pending human review.
