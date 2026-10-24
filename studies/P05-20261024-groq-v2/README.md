# P05 Groq model pilot - 24 October 2026

Three prospectively fixed Groq-hosted GPT-OSS 120B requests returned three eligible RTL samples. Each received both frozen timing contracts.

| Sample | I1: following edge | I2: sampling edge | Paired outcome |
|---|---|---|---|
| P05-GROQ2-001 | FAIL | PASS | I2 only |
| P05-GROQ2-002 | PASS | FAIL | I1 only |
| P05-GROQ2-003 | PASS | FAIL | I1 only |

The prospectively designated I2 comparator accepts 1/3, while the internally admitted I1/I2 set accepts 3/3. This is a descriptive pilot on one constructed case, not general model accuracy, a provider comparison, human plausibility or certified ambiguity. The original three local CLI initialization failures remain separate: six total attempts, three model outputs, three evaluated samples and three access exclusions. No failure was replaced or silently retried.

## Results and provenance

[Paired results](results/paired_results.csv), [batch/cumulative counts](results/summary.json), [retained model outputs](generation/batches/P05-20261024-groq-v2/), [native evidence](evidence/), [technical manuscript](paper/main.pdf), and [publication scope](SCOPE.md). Local scientific source commit: 6f2acd74e80e807d785c9166cb1c449751638f81; it is provenance for the full local package, not a claim that its private Git history is published here.

The first evaluator accepted the HDL frontend and hierarchy but omitted process lowering before JSON export. Its error labels were evaluator backend defects, not RTL syntax failures. The separately versioned v2.1 correction adds proc before interface JSON export and reruns every sample unchanged. [Correction record](artifacts/evaluator_v2_1_correction.json). The public adapter changes only imports so evaluation can run without publishing private prompt files or API execution code. The same formal runner, contracts, assumptions, invariant checker and raw/extracted RTL bytes are retained.

PASS requires bounded checking plus induction, or native Z3 initiation/closure/safety certificates. FAIL requires a reachable counterexample; proof timeouts/errors are not semantic failures. The full local pilot also retained six corrected-adapter control outcomes and three supplementary native post-reset mismatch witnesses, all reproduced on the same host. Those supplementary checks were added after output inspection. This public runner independently rechecks the six primary candidate/contract outcomes from saved outputs.

## Reproduce the published subset

Requires Python 3.12 and the pinned YoWASP/Z3 dependencies. From this directory:

```sh
python3 -m venv .venv
.venv/bin/pip install -r formal/requirements.txt
export PATH="$PWD/.venv/bin:$PATH"
export YOWASP_CACHE_DIR="$PWD/build/yowasp-cache"
python3 scripts/reproduce_public.py --run-id my-public-reproduction
```

No API key or model request is used. The command checks content hashes, re-extracts each raw response without edits, checks the exact one-bit interface, evaluates both contracts, and compares all three paired outcomes. Use a unique run ID. Reproduction logs are written under build/. A successful retained-output replay does not prove identical future stochastic model responses. Exact prompt bodies are excluded; their original hashes, seeds, settings, timestamps, usage, returned model alias and fingerprint are retained. An alias/fingerprint is not an immutable weight snapshot.

The inherited baseline and P05 requirement remain at their existing upstream paths, e.g. [pinned P05 source directory](https://github.com/Kumar62812/neewan_1/tree/83046997dce165fd3b40c190f7dffa1e280b2c86/Files/Research_Papers/benchmark/pilot_v0_1/P05). No inherited file or frozen evidence has been rewritten. Academic review, inherited redistribution rights and venue/public-release decisions remain open.

Native SMT models/certificates in evidence/ use deterministic gzip compression; [the decompressed hash map](provenance/compressed_smt.json) records their original identities. Decompress a certificate and run z3 on it to recheck its UNSAT result, or use the source reproduction command to regenerate native artifacts.

[Prepared public-subset reproduction result](results/public_reproduction.json): PASS for all three samples and six primary contract outcomes; no new model requests.
