# Repository map

Audited main: `83046997dce165fd3b40c190f7dffa1e280b2c86` (2026-10-16). [PR #6](https://github.com/Kumar62812/neewan_1/pull/6) is merged at this commit. [PR #7](https://github.com/Kumar62812/neewan_1/pull/7) is a separate draft branch; its runner is not on this main snapshot.

## Where to work by phase

| Purpose / phase | Location | Usage |
|---|---|---|
| Daily phase management | [Phase workboard](project-state/PHASE_WORKBOARD.md), [compass](../Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md) | Start here and record evidence-backed progress |
| Frozen foundation (1A) | [Plan](../Files/FORMAL_AMBIG_RTL_PLAN.md), [protocols](../Files/Research_Papers/docs/) | Preserve methodology; amendments must be explicit |
| Golden instance (1B–1C) | [P01](../Files/Research_Papers/benchmark/pilot_v0_1/P01/), [certification dossier](../02_CERTIFICATION/) | Close outstanding review/freeze gates |
| Pilot construction (2) | [P02](../Files/Research_Papers/benchmark/pilot_v0_1/P02/), [P05](../Files/Research_Papers/benchmark/pilot_v0_1/P05/) | Keep case source, metadata and evidence together |
| Pilot review (3) | [P05 annotation](../Files/Research_Papers/benchmark/pilot_v0_1/P05/annotation/v1/), case review files | Preserve independent responses and decisions; pending means pending |
| Scaling (4) | No completed scaled benchmark evidenced | Create only after phase transition |
| LLM evaluation (5) | Draft PR #7: `tools/llm_eval/` | Infrastructure still needs repair; not model results |
| Analysis and release (6) | [Thesis plan](project-state/THESIS_ASSESSMENT_PLAN.md), [professor review](../professor_review/) | Planning/presentation material; verify claims against current evidence |
| Literature | [Research papers](../Files/Research_Papers/), [literature matrix](../Files/Research_Papers/literature/literature_matrix.csv) | Check title/content identity before citing; audit flags mismatches |
| Provenance / reproduction | [P01 register](provenance/p01-evidence-register.md), [reproduction records](reproducibility/) | Distinguish source, retained evidence and new reproduction |
| Historical tools / archives | [re](../re/), [notebook index](../03_NOTEBOOKS/), [historical index](../06_HISTORICAL/), [legacy](../legacy/) | Retain historical context and archive identities |
| Decisions and history | [Project log](../governance/07_PROJECT_LOG.md) | Append events; do not rewrite historical truth |

## Why the physical paths remain stable

Benchmark sources currently live under `Files/Research_Papers/benchmark/pilot_v0_1/`. These paths appear in commands, evidence snapshots and provenance records. Navigation is organized by phase here without moving hashed artifacts. A later physical migration needs an explicit old-to-new mapping, reference audit and reproduction check.

Keep the accepted P01 archive and checksum at `re/p01-20260930T220622Z-rev1.tar.gz` and `re/p01-20260930T220622Z-rev1.tar.gz.sha256`. Do not rewrite, replace, recompress or rename them. See the [P01 register](provenance/p01-evidence-register.md) for the effective tested-source boundary.

## Which record answers which question?

- What rules apply? Frozen plan and protocols.
- What should happen next? Compass and phase workboard.
- What happened? Dated project log and original run records.
- What does the evidence establish? Case results plus raw logs/witnesses and review decisions.
- What changed during organization? [Original curation manifest](curation-manifest.md) and [2026-10-16 audit](audits/2026-10-16-repository-audit.md).

A status page cannot override raw evidence or create a missing human decision.
