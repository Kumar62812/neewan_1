# LLM-to-RTL runner

This is a minimal provenance-first harness for single-shot LLM-to-RTL experiments.

## Fixture smoke test (no model call)

From the repository root, prepare a prompt and a fixture response containing a complete SystemVerilog module, then run:

```bash
python3 tools/llm_eval/run_pipeline.py \
  --case P01 --run-id P01-smoke-001 \
  --prompt-file path/to/p01_prompt.txt \
  --fixture-response path/to/fixture_response.txt \
  --out-root artifacts/llm_eval
```

This validates prompt/raw-response/RTL/manifest writing only. Since no compile/formal commands are supplied, their statuses will be `not_run`. To test tool integration, pass explicit compile/formal commands. The runner substitutes `{rtl}` with the extracted RTL path. Example compile command if Icarus Verilog is installed: `iverilog -g2012 -s mux2 -o compile.out {rtl}`; adapt the top module to the frozen P01 interface. Formal execution should use the project's existing P01 harness and frozen configuration, not an improvised property.

## Real model adapter

`--model-command` launches an adapter command and expects raw model text on stdout. Use `{prompt}` as a placeholder for the rendered prompt file path. Record exact provider/model/version/decoding metadata in the run record before treating a run as scored evidence. Do not use this option for P05 until the human review gate has passed.

## Artifact contract

Each run has `prompt.txt`, `raw_response.txt`, `extracted_rtl.sv`, compile/formal stdout and stderr, `summary.json`, and `manifest.json`. The manifest stores SHA-256 hashes for files present when the manifest is generated; summary and manifest are excluded from the self-referential hash list. Never reuse a run ID.

**Important:** This is an initial harness, not yet validated against the repository's exact P01 formal script. Smoke-test it locally and inspect the generated artifacts before use.
