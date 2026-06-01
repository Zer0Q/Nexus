# Wikilink Enforcement — Lessons from 2026-05-27, 2026-06-01

## Bug: Source Notes Created Without Wikilinks

When processing BMAD + SDD articles, source notes were created with PLAIN TEXT in the `## Core Concepts` section instead of `[[wikilinks]]`. The Step 8 verification passed because it only checked that existing links resolve — it did NOT check that source notes HAVE links.

**Root cause:** The template shows `[[wikilinks]]` but the agent wrote plain-text bullets. The verification step had no check for "source notes must have outgoing links."

**Fix applied:**
1. Step 3: explicit rule — "Every bullet in `## Core Concepts` MUST be a `[[wikilink]]`"
2. Step 4: explicit rule — `## Related` MUST have 2+ wikilinks, `## Source` MUST have exactly 1
3. Step 5: explicit rule — `See also:` MUST have wikilinks
4. Step 8: added source note connectivity check — flags notes with zero outgoing links
5. Step 10: GATE — raw/ only deleted after Step 8 passes BOTH checks

**Pattern to remember:** When creating notes programmatically, the temptation is to write descriptive text instead of structured wikilinks. The template is a guide, not an enforcement mechanism. Verification scripts are the enforcement mechanism.

## Bug: Triage Script Counted All Links, Not Just Broken

The original Step 9 triage script counted ALL wikilinks across the vault, not just broken ones. This meant it would report "reusable" concepts that were already resolved, wasting effort creating duplicate notes.

**Fix:** Added `existing` map build + `if norm(target) not in existing` filter before counting.

## Bug: Hardcoded Index List in Orphan Detection

The orphan detection script had a hardcoded set of index names:
```python
{'AI-Vault-Integration-Index', 'Knowledge-Management-Index', ...}
```
When a new index was created (`AI-Development-Index`), it showed up as an orphan false positive.

**Fix:** Dynamic discovery — collect all files in `/indexes/` directory at runtime.

## Safety Gate: Raw Files Are Irrecoverable

Raw articles are the ONLY source material. Once deleted, information cannot be reconstructed from compressed notes. The Step 10 GATE enforces: do NOT delete raw/ until Step 8 confirms both zero broken links AND all source notes have outgoing links.

## Verification Checklist (run before every raw/ cleanup)

1. [ ] Step 7: wikilink normalization ran
2. [ ] Step 8a: all wikilinks resolve to existing files
3. [ ] Step 8b: no plain-text references where wikilinks belong
4. [ ] All source notes have at least one outgoing wikilink
5. [ ] Step 9: broken links triaged (create/remove/placeholder)
6. [ ] Only THEN: Step 10 — delete raw/

## Bug: Plain text references masquerading as wikilinks (2026-06-01)

`Agent-Harness-Engineering` appeared in 4 files as plain text (`- Agent-Harness-Engineering` or `See also: Agent-Harness-Engineering`) without `[[ ]]` wrappers. Obsidian rendered them as plain text — invisible broken links. The actual file was `AddyOsmani-Agent-Harness-Engineering.md`.

**Two sub-problems:**
1. Missing `[[ ]]` — the reference was never a wikilink, so Step 8 verification didn't catch it (it only checks existing `[[wikilinks]]`)
2. Shortened name — even if wrapped as `[[Agent-Harness-Engineering]]`, it would still be broken because the file is `AddyOsmani-Agent-Harness-Engineering.md`

**Fix applied:**
1. Step 4: Added explicit wikilink normalization rule with examples
2. Step 8b: New verification step — detects plain-text concept names in `## Related`, `## Core Concepts`, `See also:` sections
3. Step 10 GATE: Now requires Step 8b to pass (zero plain-text refs)
4. Pitfalls: Added rules against plain-text references and shortened filenames

**Root pattern:** When writing Related/See also sections, the agent writes the "concept name" rather than the actual filename. The fix is to always use the full filename stem and wrap it in `[[ ]]`.

## Bug: Non-canonical filenames (accents) (2026-06-01)

Two files had accents in their names: `ingeniería` and `cómo`. While Obsidian resolves these, they break the normalization scripts and create inconsistency. Always strip accents during file creation (Step 3/4).
