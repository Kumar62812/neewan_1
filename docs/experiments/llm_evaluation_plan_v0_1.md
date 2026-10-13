# LLM-to-RTL Evaluation Plan (Pre-registration)

**Status:** Infrastructure plan; no model calls have been made under this plan.  
**Repository:** `Kumar62812/neewan_1`  
**Plan version:** 0.1-draft  
**P05 certified evaluation:** **BLOCKED** pending independent human plausibility review.

## 1. Frozen case governance

- P01: infrastructure smoke-test case only; smoke-test artifacts are not final model-performance evidence.
- P02: eligible only after its published reproduction package is linked to the exact source commit and checksums.
- P05: do not run final LLM evaluation until the reviewer decision is recorded. Preserve exact requirement, interpretations A/B, behavioral specifications, source commit, and SHA-256 hashes in a read-only freeze manifest before experiments.
- Other cases: not included until individually authorized in the frozen case list.

Required P05 status string (retain verbatim):

> Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.

## 2. Models and versions

No model is selected or invoked by this document. Before the first scored run, append an immutable model registry with provider, exact model identifier/version or dated snapshot, API/SDK version, decoding parameters, endpoint/region if applicable, and date verified. A moving alias without a recorded resolution is insufficient for reproducible results.

## 3. Cases and run counts

| Case | Purpose | Runs per model/case | Evaluation status |
|---|---|---:|---|
| P01 | Runner/infrastructure smoke test | 1 fixture run; later scored runs separately preregistered | Smoke test only |
| P02 | Benchmark case | 5 independent single-shot runs, unless a preregistered amendment says otherwise | Await evidence-link audit |
| P05 | Ambiguity case | 5 independent single-shot runs only after review gate passes | **BLOCKED** |
| Other cases | Not in current plan | Not set | Not authorized |

The five-run choice is a planned protocol, not evidence that runs have occurred. Use distinct run IDs and preserve every raw output. Do not silently replace failed generations.

## 4. Exact prompt policy

Prompts must be committed before any model call and identified by SHA-256. The prompt template must include the case's frozen requirement verbatim and ask for synthesizable SystemVerilog only, with a declared module/interface contract. Do not include interpretations, preferred answers, reference RTL, formal properties, expected results, or reviewer judgments unless that information is explicitly part of the requirement shown to every model.

For each run, save the fully rendered prompt as `prompt.txt`; do not reconstruct it later from a template.

## 5. Conditions and clarification rules

- Primary condition: single-shot generation; no conversational follow-up.
- Interactive clarification condition: not included in this initial experiment. If added later, preregister a separate condition and exact scripted user replies before model calls.
- No human clarification or hidden prompt repair during a run.
- If the model asks a question instead of returning RTL, classify as `clarification_requested`; do not answer it in the single-shot condition.

## 6. Retry, repair, and timeout policy

- No automatic retry or repair for scored generations.
- Transport failures may be retried only if no model response was received; retain the failure record and all attempt IDs.
- A received malformed or empty response is an outcome, not a reason to regenerate.
- Default generation timeout: 120 seconds; compilation timeout: 30 seconds; formal timeout: 120 seconds. Record actual timeout and exit status.
- Any policy change requires a dated protocol amendment before affected runs.

## 7. Output classifications

Assign one primary generation class: `rtl_extracted`, `empty_response`, `clarification_requested`, `refusal`, `format_failure`, `timeout`, or `provider_error`.

Independently record compilation as `pass`, `fail`, `timeout`, or `not_run`; formal verification as `pass`, `fail_with_counterexample`, `unknown`, `timeout`, or `not_run`. Never collapse compilation and formal results into one status. A formal pass means only that the specified property and assumptions passed for that implementation; it does not establish that an interpretation is plausible.

## 8. Metrics

Report, per model and case:
- RTL extraction rate and compilation pass rate.
- Formal pass rate, counterexample rate, and unknown/timeout rate.
- Exact-match or equivalence-to-reference only where the case's specification makes that comparison meaningful and the method is preregistered.
- Latency and token usage/cost when reliably supplied by the provider.
- Number of valid responses and denominator for every rate.

For P05, report interpretation choice / behavioral class only after the human review gate is satisfied. Do not call a formal behavioral distinction “certified ambiguity” without the independent plausibility review.

## 9. Provenance and artifact contract

Every run must have a unique run directory and a manifest linking:
1. source commit and case-freeze manifest;
2. exact prompt and SHA-256;
3. raw provider response and SHA-256 (or explicit fixture marker for smoke tests);
4. extracted RTL and SHA-256;
5. compile command, tool version, stdout/stderr, exit status;
6. formal command/configuration, tool versions, logs, result and witness/counterexample paths;
7. summary JSON and a run-level SHA-256 manifest.

Never overwrite a run directory. Preserve tool versions and exact commands. The fixture smoke test must be labelled `pipeline_test_only`.

## 10. P05 reviewer firewall

Reviewers receive only the frozen requirement and anonymized candidate interpretations/specifications required by the review protocol. Do not disclose model outputs, formal outcomes, counterexamples, or the researcher's preferred interpretation before judgments are locked. Reviewer eligibility and independence must be recorded; identify five eligible reviewers, but do not imply they have agreed until confirmed.

## 11. Release gates

- [ ] Freeze P05 source artifacts and record source commit + SHA-256 hashes.
- [ ] Link existing P02/P05 reproduction packages without rerunning successful experiments.
- [ ] Approve this protocol and freeze exact prompt templates/model registry.
- [ ] Pass P01 fixture smoke test and inspect all artifact links.
- [ ] Complete five independent P05 plausibility reviews and record adjudication.
- [ ] Only then unblock final P05 LLM evaluation.
