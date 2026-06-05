# Wikilink Enforcement

## Bug: Summaries Created Without Wikilinks

When processing BMAD + SDD articles, summaries were created with plain text in the `## Core Concepts` section instead of folder-qualified `[[wikilinks]]`. The verification passed because it only checked that existing links resolve; it did not check that summaries have outgoing knowledge links.

**Root cause:** The template showed wikilinks, but the agent wrote plain-text bullets. The verification step had no check for "summaries must have outgoing links."

**Fix applied:**
1. Summary creation: every bullet in `## Core Concepts` must be a folder-qualified wikilink.
2. Concept/tool notes: `## Related` must use folder-qualified wikilinks; `## Source` must link to summaries.
3. Validation: add summary connectivity checks and raw-note provenance checks.
4. Raw cleanup gate: delete `raw/` files only after validation passes.

**Pattern to remember:** When creating notes programmatically, the temptation is to write descriptive text instead of structured wikilinks. The template is a guide, not an enforcement mechanism. Verification scripts are the enforcement mechanism.

## Bug: Triage Script Counted All Links, Not Just Broken

The original Step 9 triage script counted ALL wikilinks across the vault, not just broken ones. This meant it would report "reusable" concepts that were already resolved, wasting effort creating duplicate notes.

**Fix:** Added an existing-file map and counted only unresolved targets before triage.

## Bug: Hardcoded Index List in Orphan Detection

The orphan detection script had a hardcoded set of index names:
```python
{'AI-Vault-Integration-Index', 'Knowledge-Management-Index', ...}
```
When a new index was created (`AI-Development-Index`), it showed up as an orphan false positive.

**Fix:** Dynamic discovery: collect all files in `indexes/` at runtime.

## Safety Gate: Raw Files Are Irrecoverable

Raw articles are the only source material before ingestion. Once deleted from `raw/`, information can only be recovered if the unchanged copy exists in `raw-notes/`. The cleanup gate enforces: do not delete `raw/` until validation confirms zero broken links, summary-to-raw-note connectivity, and concept/tool-to-summary connectivity.

## Verification Checklist (run before every raw/ cleanup)

1. [ ] Filename and wikilink normalization ran.
2. [ ] All wikilinks resolve to existing files.
3. [ ] All links are folder-qualified.
4. [ ] No plain-text references remain where wikilinks belong.
5. [ ] Every summary links to `raw-notes/`.
6. [ ] New concepts/tools link to `summaries/`.
7. [ ] Broken links are triaged.
8. [ ] Raw cleanup has been dry-run before apply.

## Bug: Plain text references masquerading as wikilinks (2026-06-01)

`Agent-Harness-Engineering` appeared in 4 files as plain text (`- Agent-Harness-Engineering` or `See also: Agent-Harness-Engineering`) without `[[ ]]` wrappers. Obsidian rendered them as plain text — invisible broken links. The actual file was `AddyOsmani-Agent-Harness-Engineering.md`.

**Two sub-problems:**
1. Missing `[[ ]]`: the reference was never a wikilink, so link verification did not catch it.
2. Shortened name: even if wrapped as a bare link, it would still be ambiguous because the actual summary filename was longer.

**Fix applied:**
1. Added explicit wikilink normalization rules with folder-qualified examples.
2. Added a plain-text reference check for `## Related`, `## Core Concepts`, `## Sources`, and `## Source`.
3. Updated the cleanup gate to require zero plain-text references.
4. Added rules against plain-text references and shortened filenames.

**Root pattern:** When writing relationship sections, the agent may write the display concept name rather than the actual folder-qualified filename. The fix is to always use the full folder-qualified filename stem.

## Bug: Non-canonical filenames (accents) (2026-06-01)

Two files had accents in their names. While Obsidian may resolve these, they break normalization scripts and create inconsistency. Always strip accents during file creation.
