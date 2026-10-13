# P02/P05 Existing Evidence Index

**Index status:** Links and recorded provenance collected from the repository; no formal run was repeated to create this index.  
**Reproduction record:** [docs/reproducibility/p02-p05-reproduction.md](https://github.com/Kumar62812/neewan_1/blob/main/docs/reproducibility/p02-p05-reproduction.md)  
**Recorded tested source commit:** `0874a36608a249b3c2c89ccc35e637936bd2987f`  
**Toolchain recorded by the reproduction record:** macOS 15.5 arm64, Python 3.12.1, Yosys 0.63, YoWASP 0.63.0.0.post1107, Yosys-SMTBMC, Z3 4.15.4.

## P02

- [Case source and evidence directory](https://github.com/Kumar62812/neewan_1/tree/main/Files/Research_Papers/benchmark/pilot_v0_1/P02)
- [Run 1 checksum manifest](https://github.com/Kumar62812/neewan_1/blob/main/Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-01/SHA256SUMS.json)
- [Run 2 checksum manifest](https://github.com/Kumar62812/neewan_1/blob/main/Files/Research_Papers/benchmark/pilot_v0_1/P02/evidence/run-02/SHA256SUMS.json)

The evidence directories contain recorded environment/tool-version files, commands/configurations, logs, and formal witness artifacts. Use each run's `SHA256SUMS.json` as the recorded per-artifact hash inventory.

## P05

- [Case source and evidence directory](https://github.com/Kumar62812/neewan_1/tree/main/Files/Research_Papers/benchmark/pilot_v0_1/P05)
- [Run 1 checksum manifest](https://github.com/Kumar62812/neewan_1/blob/main/Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-01/SHA256SUMS.json)
- [Run 2 checksum manifest](https://github.com/Kumar62812/neewan_1/blob/main/Files/Research_Papers/benchmark/pilot_v0_1/P05/evidence/run-02/SHA256SUMS.json)
- [Blinded annotation/review protocol](https://github.com/Kumar62812/neewan_1/tree/main/Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1)

## Reproduction commands recorded in the existing log

```sh
python3 -m venv /tmp/formal-ambig-tools
/tmp/formal-ambig-tools/bin/pip install -r docs/reproducibility/formal-requirements.txt
export PATH="/tmp/formal-ambig-tools/bin:$PATH"
export XDG_CACHE_HOME="/tmp/formal-ambig-cache"
python Files/Research_Papers/benchmark/pilot_v0_1/P02/formal/run.py --out /tmp/p02-new-run
python Files/Research_Papers/benchmark/pilot_v0_1/P05/formal/run.py --out /tmp/p05-new-run
```

These commands are transcribed from the existing reproduction record, not executed as part of this index. Do not rerun solely to regenerate documentation.

## Publication/provenance caveat

The current main tree exposes the P02/P05 evidence paths above. The reproduction record states that PR #6 was open against main at the time it was written; this index does not reinterpret that historical statement as proof of the PR's current status. The source commit and existing run checksum manifests should be treated as the primary provenance records.

## P05 human-review gate

> Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.

Do not show reviewers model outputs, formal results, witnesses/counterexamples, or the preferred outcome. P05 final LLM evaluation remains blocked until review is complete and adjudicated.
