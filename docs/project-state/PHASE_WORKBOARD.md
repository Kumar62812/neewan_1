# Phase workboard

Audited 2026-10-16 against published main `83046997dce165fd3b40c190f7dffa1e280b2c86`. This is a working index of evidence and next actions, not a phase-transition approval or a change to the frozen methodology.

## Start each work session here

1. Read the [compass](../../Files/FORMAL_AMBIG_RTL_PROJECT_COMPASS.md) and this workboard.
2. Choose the first actionable item in the queue below. A blocked item requires its listed evidence or decision, not a guessed completion.
3. Follow requirement → interpretation → specification → RTL → formal evidence → certification.
4. Save new evidence separately, record the actual result and source revision, then update this board and the [project log](../../governance/07_PROJECT_LOG.md).
5. A phase exit requires a traceable decision. A technical result or merged documentation PR alone does not pass a scientific gate.

## Original phases and current position

The numbering below follows the compass phase-transition map. Gate numbers follow section 13 of the [frozen plan](../../Files/FORMAL_AMBIG_RTL_PLAN.md); phase numbers and gate numbers are distinct.

| Phase | Purpose | Published position | Next action / exit evidence |
|---|---|---|---|
| 1A | Research foundation and methodology | Plan is labeled v1.0-FROZEN; gate checklist is not a signed completion record | Reconcile the Gate 1 decision record without rewriting frozen definitions |
| 1B | P01 golden-template construction | Requirement, interpretation, specification, RTL and formal evidence retained | Use existing artifacts; do not reconstruct P01 from scratch |
| 1C | P01 review, reproduction and freeze | Formal evidence complete for effective tested source; independent certification record incomplete; template not frozen | Close annotation, metadata, reproducibility and review gaps; record Gate 2 freeze decision |
| 2 | Construct pilot cases | P02 technical evidence and P05 candidate evidence already published; remaining cases absent | Reconcile the documented P02 proceed direction with the unclosed template gate; resolve P05 before starting P06 |
| 3 | Pilot review and protocol stabilization | Pilot incomplete; P05 human plausibility pending | Review cases, retain unresolved/excluded decisions and demonstrate P12 rejection behavior; satisfy Gate 3 |
| 4 | Scaled benchmark construction | No completed scaled benchmark evidenced | Only begin after pilot stabilization and the required documented transition |
| 5 | LLM single-shot and interactive evaluation | PR #7 is draft infrastructure; no model-performance result established | Pass case/pilot gates, freeze experiment settings and validate the candidate evaluator before evaluation (Gate 4) |
| 6 | Analysis, paper and release | Methods/planning material exists; results freeze not established | Compute results from frozen evidence and satisfy Gate 5 before final result claims |

**Governance reconciliation:** The [meeting record](../../02_CERTIFICATION/P01_GUIDE_MEETING_RECORD.md) records direction to proceed with P02. This is not an independent P01 certification or template freeze. Existing P02/P05 artifacts are retained as observed work; their existence does not retrospectively approve a phase transition. Record the applicable exception/transition decision before expanding the pilot.

## Case order and evidence

Preserve: **P01 → P02 → P05 → P06 → P08 → P03 → P04 → P07 → P09 → P10 → P11 → P12**.

| Case | Existing evidence | Remaining gate |
|---|---|---|
| [P01](../../Files/Research_Papers/benchmark/pilot_v0_1/P01/) | Reference and wrong-control evidence for pinned source plus retained path-only patch; [provenance](../provenance/p01-evidence-register.md) | Independent decision, complete template artifacts and explicit freeze |
| [P02](../../Files/Research_Papers/benchmark/pilot_v0_1/P02/) | [Results](../../Files/Research_Papers/benchmark/pilot_v0_1/P02/P02_RESULTS.md), reference BMC/induction, eight covers and two negative controls in run-02 | Public clean reproduction provenance and case review; technical verification is not benchmark-wide validation |
| [P05](../../Files/Research_Papers/benchmark/pilot_v0_1/P05/) | [Results](../../Files/Research_Papers/benchmark/pilot_v0_1/P05/P05_RESULTS.md), A/B conformance and a post-reset distinguishing trace | Exact reviewed-version freeze record, five independent responses, predefined threshold assessment and decision |
| P06, P08, P03, P04, P07, P09, P10, P11 | No case directories at audited main | Not started in published snapshot; follow order and gates |
| P12 | No case directory at audited main | Evaluator robustness only; never label as a certified ambiguity case |

P05 claim boundary: **Formal distinction: Reported demonstrated locally. Human plausibility: Pending. Certified ambiguity: Not claimed.** Published metadata records zero human responses; this does not assert knowledge of submissions outside the repository.

## Ordered work queue

| Priority | Work item | Completion evidence | Dependency |
|---|---|---|---|
| 1 | Reconcile phase decisions and P01 freeze gaps | Traceable transition/exception record; annotation, metadata, reproduction and freeze checklist with artifact links | Human review/decision where required; never fabricate signatures |
| 2 | Repair the public reproduction instructions | Obtain or replace the unavailable historical source reference with a documented, validated source mapping; run a new independent reproduction and retain its evidence | Historical commit cannot currently be resolved on GitHub; retain original records |
| 3 | Audit the literature catalog | Verify PDF titles against source metadata and repair catalog mappings with a retained old-to-new record | Several distinct paper titles currently resolve to identical PDF bytes; see audit |
| 4 | Complete P05 plausibility process | Version/hash record, five separate eligible reviews, threshold assessment, objections and decision | Follow existing protocol; no outreach or certification implied by this workboard |
| 5 | Repair PR #7 infrastructure | P01 eligibility enforced; generated RTL tested; native formal statuses and witness checks; failure preservation; complete manifests; positive/wrong-control tests | Infrastructure validation only; no scored model evaluation before gates |
| 6 | Continue pilot with P06, then remaining ordered cases | Full evidence chain and gate decision per case | Prior case/milestone closure or documented amendment |
| 7 | Stabilize, scale, evaluate and release | Phase-specific freeze and review records | Prior phase exits |

Items 2, 3 and offline infrastructure repairs may be prepared while human decisions are pending; this is not permission to bypass an experiment or certification gate.

## Evidence and status rules

- Distinguish **artifact present**, **reported result**, **integrity verified**, **freshly reproduced**, and **certified**.
- Keep `PASS`, expected negative-control `FAIL`, `INCONCLUSIVE` and `TOOL ERROR` separate.
- `UNRESOLVED` is an evidence status, not a failure to organize the project.
- No reviewer, approval, experiment, or freeze is inferred from file presence.
- Frozen plan/protocols, requirements, interpretations, specifications, source snapshots, evidence and accepted archives stay at their existing paths in this organization pass.
- See the [repository map](../repository-map.md) for where each phase's work belongs and the [audit](../audits/2026-10-16-repository-audit.md) for verified limitations.
