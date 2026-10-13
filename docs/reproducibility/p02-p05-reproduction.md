# P02/P05 clean reproduction record

- **Tested source commit:** `0874a36608a249b3c2c89ccc35e637936bd2987f`
- **Reproduction date:** 2026-10-10 (05:09–05:10 IST)
- **Environment:** macOS 15.5, arm64; Python 3.12.1
- **Tools:** Yosys 0.63 (`70a11c6bf`), YoWASP 0.63.0.0.post1107, Yosys-SMTBMC, Z3 4.15.4
- **Pinned packages:** `docs/reproducibility/formal-requirements.txt`
- **Publication update (2026-10-14):** [PR #6](https://github.com/Kumar62812/neewan_1/pull/6) merged 2026-10-11 UTC as commit `83046997dce165fd3b40c190f7dffa1e280b2c86`. The reproduction itself occurred earlier, at tested source commit `0874a36608a249b3c2c89ccc35e637936bd2987f`. The original execution snapshot, tested clean-reproduction source, and published-evidence merge commit are distinct provenance stages; merging evidence does not constitute a new formal run.

## Commands executed

Commands ran from a clean detached checkout at the tested commit. The Python environment and tool requirements were installed first:

```sh
python3 -m venv /tmp/formal-ambig-tools
/tmp/formal-ambig-tools/bin/pip install -r docs/reproducibility/formal-requirements.txt
export PATH="/tmp/formal-ambig-tools/bin:$PATH"
export XDG_CACHE_HOME="/tmp/formal-ambig-cache"
python Files/Research_Papers/benchmark/pilot_v0_1/P02/formal/run.py --out /tmp/p02-new-run
python Files/Research_Papers/benchmark/pilot_v0_1/P05/formal/run.py --out /tmp/p05-new-run
```

Both workflow invocations returned 0. The committed runners recorded child commands, return codes, and formal statuses in their `runs.json` files. P02 and P05 run logs and witness traces are in their respective `evidence/run-02/` directories.

## Outcomes

| Case | Check | Result |
|---|---|---|
| P02 | Reference bounded check, 12 global steps | PASS |
| P02 | Temporal induction, successful at step 11 within budget 12 | PASS |
| P02 | Eight cover targets, within budget 16 | PASS |
| P02 | Wrong reset-polarity negative control | Expected FAIL with inspected counterexample |
| P02 | Asynchronous-reset negative control | Expected FAIL with inspected counterexample |
| P05 | Joint A/B conformance bounded check, 12 global steps | PASS |
| P05 | Joint A/B induction, successful at step 11 within budget 12 | PASS |
| P05 | Both post-reset divergence directions covered | PASS |
| P05 | Post-reset equality check | FAIL with legal distinguishing trace at step 3 |

P05 demonstrates a formal behavioral distinction under the tested model. Human plausibility responses remain pending (0 received); no ambiguity certification or LLM evaluation result is claimed.

## Retained archive checksums

These locally retained clean-run bundles are not included in PR #6. Their upload was rejected by the connected GitHub review because it could not verify the contents of opaque archives. They were not extracted to prepare the PR.

```text
P02-clean-0874a36608a2-20261010.tar.gz
SHA-256: 234036a798c5e59dd6c542cbd968742d8576843b9763935f6cd6c9a57ebd7b3b

P05-clean-0874a36608a2-20261010.tar.gz
SHA-256: ec727e4346ec326fe379e48e13c44bd033bccc26d0728931c7777183f6ffee39
```

The P01 evidence archive and source are outside this reproduction package and remain unchanged. These results do not establish analog timing, four-state behavior, independent-person replication, cross-platform reproduction, human plausibility, or benchmark-wide validity.
