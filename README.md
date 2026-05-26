# Nexus — Compressed Knowledge Vault

A high-signal technical knowledge vault built with Obsidian, inspired by Andrej Karpathy's note-taking philosophy.

## Philosophy

- **Dense knowledge** over verbose explanations
- **Atomic notes** over large documents
- **Reusable concepts** over course-specific summaries
- **Semantic links** over hierarchical folders
- **Signal density** over completeness

Every note provides standalone value. No fluff, no repetition, no filler.

## Vault Structure

```
Nexus/
├── concepts/       Atomic technical concepts (one idea per note)
├── frameworks/     Reusable workflows, mental models, methodologies
├── tools/          Specific software, plugins, APIs, hardware
├── architectures/  System design patterns
├── workflows/      Step-by-step procedures and pipelines
├── glossary/       Quick-reference term definitions
├── source_notes/   One note per source article
├── indexes/        Thematic index notes mapping related concepts
└── raw/            Incoming unprocessed articles
```

## Automated Processing

The `obsidian-vault-processor` skill automates article ingestion:

1. **Scan** `raw/` for new `.md` articles
2. **Read** each article in full
3. **Create** one source note per article
4. **Extract** 10-25 atomic knowledge notes per article
5. **Generate** glossary entries and index notes
6. **Normalize** all `[[wikilinks]]` (kebab-case, no accents, no spaces)
7. **Verify** cross-link coherence (zero broken links)
8. **Clean** `raw/` after successful processing

## Note Structure

### Atomic Notes
```markdown
# Concept Name

## Definition
Short compressed explanation.

## Why It Matters
Why this concept is important.

## Key Ideas
- point
- point

## Tradeoffs
Optional tradeoffs.

## Related
- [[Related Concept]]

## Source
[[Source-Note]]
```

### Source Notes
```markdown
# Source Title

## Summary
Compressed 2-3 sentence summary.

## Core Concepts
- [[Concept A]] -- description

## Key Insights
- insight

## Open Questions
- question
```

## Naming Conventions

- **Filenames:** `kebab-case`, no accents, no spaces, max 64 chars
- **Wikilinks:** `[[Concept-Name]]` must match the exact filename
- **Frontmatter:** YAML metadata in source notes (title, source, author, date, type)

## Tech Stack

- **Obsidian** — vault and note editor
- **Hermes Agent** — automated processing via `obsidian-vault-processor` skill
- **Python** — wikilink normalization and cross-link verification scripts

## Usage

Drop `.md` articles into `Nexus/raw/` and trigger the processor. The skill handles the rest — extraction, linking, normalization, and verification.
