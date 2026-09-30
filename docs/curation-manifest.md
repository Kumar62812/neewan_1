# Repository Curation Manifest

**Curation branch:** `curation/formal-ambig-rtl-audit`

**Base branch:** `formal-ambig-rtl-foundation`

**Base commit:** `4b5288bb75eb8bce58af8ac1038f519306d7cfec`

## Actions in this curation pass

1. Add an audit-oriented root README and repository map.
2. Add a P01 evidence/provenance register.
3. Add a P01 clean-checkout reproduction boundary.
4. Establish a `legacy/` namespace for retained imported material.
5. Move only clearly duplicated/imported root-level PDFs and the historical root P01 archive into `legacy/`; retain their blob contents unchanged.
6. Do not modify P01 source artifacts, formal logs, counterexamples, accepted evidence archives, checksums, or historical audit records.
7. Do not alter Git history, prior commits, or tags.

## Explicitly deferred

- Moving the accepted P01 evidence archive because the accepted archive named by the provenance record is not present at the expected repository path in the inspected branch.
- Rewriting or “fixing” the P01 SBY files in place, because doing so would blur the boundary between the pinned source and the separately tested patched source.
- Reclassifying P01 certification.
- Creating P02–P12 artifacts.
- Changing the research protocol or methodology definitions.

## Legacy moves

| Original path | New logical path | Reason |
|---|---|---|
| `Agent.pdf` | `legacy/imported_root_material/Agent.pdf` | Duplicate/imported root-level PDF; same blob retained |
| `Agent (4).pdf` | `legacy/imported_root_material/Agent (4).pdf` | Duplicate/imported root-level PDF; same blob retained |
| `Agentic_AI.pdf` | `legacy/imported_root_material/Agentic_AI.pdf` | Duplicate/imported root-level PDF; same blob retained |
| `p01-20260930T155000Z-rev3 (3).tar.gz` | `legacy/historical-evidence-archives/p01-20260930T155000Z-rev3 (3).tar.gz` | Historical archive differs from the accepted archive named by the P01 provenance record |

The move preserves the original binary blob contents. The accepted `p01-20260930T220622Z-rev1.tar.gz` remains a separate provenance item and is not replaced by the older archive.
