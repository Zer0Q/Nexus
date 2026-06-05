# Vault Sustainability

## Problem: Vault Inflation

The vault becomes weaker when every interesting phrase becomes a standalone note. Broken links, single-use terms, and source-specific ideas can cause uncontrolled growth if they are automatically converted into notes.

Nexus avoids this by separating source preservation from knowledge extraction:

- Raw articles are copied unchanged to `raw-notes/`.
- Each source gets one compressed summary in `summaries/`.
- Reusable concepts/tools link to summaries.
- Summaries link back to raw-notes.

## Sustainable Source Pipeline

For each processed article:

1. Copy the original markdown unchanged to `raw-notes/`.
2. Create one compressed summary in `summaries/`.
3. Link the summary to the original with a folder-qualified link such as `[[raw-notes/building-effective-ai-agents]]`.
4. Link summary concepts/tools with folder-qualified links such as `[[concepts/Knowledge-Graph]]` and `[[tools/Obsidian]]`.
5. Update existing concept/tool notes before creating new ones.
6. Link concept/tool notes back to summaries, not directly to raw originals.

## Adaptive Note Creation Rule

A concept or tool only merits a standalone note when it:

- appears meaningfully in 2+ sources,
- is foundational to the vault's knowledge model, or
- connects or clarifies an existing cluster.

Single-source ideas should usually stay inside the compressed summary as plain text. Prefer fewer high-quality notes over many shallow notes.

## Three-Category Triage

Instead of blindly creating notes for broken links, classify each one:

| Category | Criteria | Action | Example |
| --- | --- | --- | --- |
| Reusable | Appears in 2+ sources, is foundational, or connects a cluster | Create or update note | `[[concepts/Knowledge-Mapping]]` |
| Single-use | Appears in only 1 source and is not foundational | Dry-run unwrap, keep readable text | `[[concepts/Trade-Capture-System]]` -> `Trade Capture System` |
| False reference | Placeholder, author name, team name, or organization | Dry-run unwrap or remove | `[[concepts/Topic-Name]]` -> `Topic Name` |

Unwrapping wikilinks is destructive because it removes graph structure. Always dry-run first and apply only after review.

## Naming and Link Sustainability

Every filename and wikilink should be:

- hyphenated,
- folder-qualified,
- free of spaces,
- free of underscores,
- free of accents, and
- free of dots except the final `.md` extension.

Good examples:

- `[[concepts/Knowledge-Graph]]`
- `[[tools/CLAUDE-MD-Project-Knowledge]]`
- `[[summaries/AddyOsmani-Agent-Harness-Engineering]]`
- `[[raw-notes/building-effective-ai-agents]]`

Invalid patterns:

- Bare links without folder paths.
- Links containing spaces.
- Links containing underscores.
- Links containing accents or diacritics.
- Links containing dots inside the filename stem.

## Orphan Detection

Run periodically every 10-15 processed articles. Notes unreferenced by any other note are orphans. Orphans are not necessarily bad because leaf concepts exist, but persistent orphans should be reviewed.

Orphan resolution must use dry-run/apply phases:

- Dry-run proposed links from related notes or indexes.
- Dry-run proposed merges into broader concept/tool notes.
- Dry-run proposed deletes for stale duplicates or notes that fail the knowledge model.
- Apply only after the proposed changes are reviewed.

## Pre-Creation Duplicate Check

Before creating any concept/tool note, scan existing `concepts/` and `tools/`.

If a note already covers the idea, update it with the new source insight and add a `[[summaries/Author-Topic]]` source link. This is the most effective anti-inflation measure.

## Validation Order

Run validation in this order:

1. Normalize filenames and wikilinks.
2. Verify link resolution and source connectivity.
3. Detect plain-text references.
4. Produce a validation report.

The validation report should list all pending destructive actions before apply: file renames, raw cleanup, wikilink unwrapping, orphan merges, and orphan deletes.

## Raw Cleanup Gate

Do not delete files from `raw/` until:

- the original has been copied unchanged to `raw-notes/`,
- the summary links to the raw note,
- concepts/tools link to summaries,
- every wikilink resolves,
- all links are folder-qualified,
- no plain-text references remain in structured relationship sections, and
- the raw deletion list has been reviewed in dry-run mode.

## Historical Lesson: BMAD + SDD Batch

A dense new domain can justify a new index when it does not fit existing clusters. However, a dense source does not justify a fixed number of atomic notes. The right output size is adaptive: create or update only the notes that are reusable, foundational, or cluster-connecting.
