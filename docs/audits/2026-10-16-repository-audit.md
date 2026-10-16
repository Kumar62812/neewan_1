# Repository research and organization audit — 2026-10-16

Repository: [Kumar62812/neewan_1](https://github.com/Kumar62812/neewan_1). Audited main: `83046997dce165fd3b40c190f7dffa1e280b2c86`. PR #7 head: `07a498a6a94a88cca213ce49445c92738f27384d`, open/draft when checked.

## Assessment

The repository contains useful retained formal evidence, but project navigation conflated historical planning with current technical progress. Organize ongoing work around the original phases and incomplete gates, not by treating all implemented cases as certified. A phase workboard now makes that separation explicit.

The original research question is whether different generated RTL represents error, a defensible alternative interpretation, or insufficient evidence. Formal behavioral difference alone does not establish linguistic plausibility. This audit does not establish research novelty, independent replication, human agreement, or model performance.

## What was inspected

- Live GitHub repository, branches, complete recursive tree, PR #6 merge state, PR #7 source, workflow-run and release listings.
- All 328 files materialized from the exact public main commit in a local object database; every file matched that commit's Git blob identity before edits. Network cloning was unavailable; no uncommitted local work was imported.
- Frozen plan, compass, project log, status/reproduction documents, P02/P05 results, metadata and runner code; P01 evidence boundaries.
- Four P02/P05 manifests, accepted P01 archive hash, duplicate PDF/archive identities, and first-page text for selected conflicting paper titles.
- Scope limit: no full review of every literature paper, no new formal solver execution, no LLM call, no human-review collection, and no independent inspection of external unpublished artifacts.

## Findings and disposition

| Priority | Finding | Organization action / next work |
|---|---|---|
| Required | README, compass and repository map described P01/P02 work as absent despite published artifacts | Reconciled active navigation; added phase and case workboard |
| Required | P01 template freeze remains open while P02/P05 work exists | Exposed governance reconciliation; retained professor-direction boundary; no retrospective approval invented |
| Required | PR #6 was described as open although merged | Corrected active state and reproduction pages; dated historical log preserved |
| Required | Historical tested-source commit `0874a36608a249b3c2c89ccc35e637936bd2987f` is not resolvable through GitHub (422) | Documented public reproduction gap; require validated source mapping and new run evidence |
| Required | Distinct literature titles share identical PDF bytes | Flag catalog identity errors for source-verified correction before citation; no files deleted or renamed |
| Required for PR #7 | Candidate pipeline can accept arbitrary case IDs and derive formal pass/fail solely from process exit | Enforce eligibility and verify generated RTL using native formal outcomes and witnesses before evaluation |
| Required for PR #7 | Timeout output can be bytes; launch errors are uncaught; failed generation can continue downstream | Normalize partial output, preserve errors and stop dependent stages; validate with failure controls |
| Required for PR #7 | Manifest walks only immediate files and excludes summary | Finalize summary then recursively hash artifacts, excluding only manifest itself |
| Follow-up | No workflow runs and no releases returned by live GitHub listings; no `.github/workflows` in main tree | Add scoped integrity/link checks after agreeing validation behavior; release only validated packages |
| Follow-up | Main has no root license and GitHub reports no detected license | Owner should choose licensing terms, including treatment of third-party papers; do not invent a license |
| Follow-up | Deep legacy paths mix literature and benchmarks; duplicate archives remain | Preserve provenance now; any physical migration needs explicit mappings and reference/reproduction validation |

PR #7 findings are from current source inspection, not newly executed runtime tests. No changes to that separate PR are included in this organization pass.

## Integrity results

| Check | Result | Meaning |
|---|---|---|
| P02 run-01 | 43/43 hashes match | Published bytes internally consistent |
| P02 run-02 | 50/50 hashes match | Published bytes internally consistent |
| P05 run-01 | 31/31 hashes match | Published bytes internally consistent |
| P05 run-02 | 30/30 hashes match | Published bytes internally consistent |
| Accepted P01 archive | SHA-256 matches `32811754b548108c74095f19362ddd18bb379aadd220bd8a7e4b2abee82c063b` | Accepted archive identity preserved |
| Fresh formal reproduction | NOT RUN | Hash matching is not proof of execution or independent replication |

P05 run-01's unsuccessful induction attempt is retained. The results document distinguishes it from run-02; it must not be erased during cleanup.

## Literature identity findings

There are 26 groups of byte-identical PDFs and 1 group of byte-identical tar archives in the audited tree. Duplication alone may be intentional; conflicting titles are the more serious issue. Selected first-page checks confirm:

| Filename label | Actual first-page title |
|---|---|
| FIXME: Towards End-to-End Benchmarking... | Evaluating Large Language Models for Automatic Register Transfer Logic Generation via High-Level Synthesis |
| Late Breaking Results: LLM-assisted Automated Incremental Proof Generation... | VeriGen: A Large Language Model for Verilog Code Generation |
| LalaEval... | CLAMBER: A Benchmark of Identifying and Clarifying Ambiguous Information Needs in Large Language Models |
| Lost in Benchmarks... | OpenLLM-RTL: Open Dataset and Benchmark for LLM-Aided Design RTL Generation |
| LLM4EDA... | Ambiguity resolution of legal requirements: an exploratory study in the literature |

These findings are limited to identity, not the scientific quality of those papers. The `Seqver` and hardware-literature-survey filenames also share bytes with the inspected OpenLLM-RTL group; the `VERISEC` filename shares bytes with the inspected legal-requirements paper. Reconcile the literature matrix and expected publisher records before treating these as separate sources. Preserve old-path mapping when correcting them.

## Phase-based organization delivered

- README becomes the entry point with evidence-qualified status.
- `docs/project-state/PHASE_WORKBOARD.md` maps all original phases, gates, case order, dependencies and immediate work.
- Compass current-state and immediate-action sections point to real outstanding work while retaining methodology and original rules.
- Repository map routes each phase to existing canonical locations.
- Active P02/P05 status and reproduction pages reflect merged publication and the unresolved source reference.
- The dated certification snapshot is labeled historical and linked to current navigation; the project log gains an appended reconciliation entry.

Frozen plan/protocols, case sources, metadata, evidence, reviewer materials, PDF files, notebook files and archives are unchanged. No experiment, phase transition or certification is authorized by these documentation changes.

## Recommended sequence

1. Close P01 review/freeze gaps and record the applicable phase/exception decisions.
2. Repair public reproduction provenance and verify paper identity mappings.
3. Complete P05 human plausibility under the existing predefined protocol.
4. Repair and test PR #7's candidate evaluation infrastructure without running scored experiments prematurely.
5. Continue P06 and the original remaining case order only after required gates or a documented amendment.
6. Stabilize the pilot, scale, freeze experimental conditions, evaluate and report in the original phase order.

**Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.**
