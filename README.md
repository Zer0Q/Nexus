# Nexus

Nexus is an experimental AI-assisted Obsidian knowledge vault for turning raw technical sources into dense, atomic, semantically linked notes.

It is designed as a compressed second brain for AI, software architecture, systems thinking, knowledge graphs, agentic workflows, and engineering knowledge management.

## Why Nexus Exists

Most technical notes become either too verbose, too scattered, or too tied to a single source.

Nexus follows a different approach:

- Dense knowledge over long summaries
- Atomic notes over large documents
- Reusable concepts over course-specific notes
- Semantic links over rigid folder hierarchies
- High signal density over completeness
- Immutable originals alongside processed summaries

The goal is not to archive everything.  
The goal is to extract reusable knowledge.

## Who This Is For

Nexus is useful for:

- software architects building reusable technical knowledge
- AI engineers collecting concepts, tools, and workflows
- researchers converting articles into connected notes
- teams exploring company-brain or second-brain systems
- Obsidian users interested in lightweight knowledge graphs

## Repository Structure

```text
.
├── Nexus/                  Obsidian vault
│   ├── concepts/           Atomic technical concepts + definitions
│   ├── tools/              Software, plugins, APIs, hardware + frameworks
│   ├── summaries/          Compressed summaries of original sources
│   ├── raw-notes/          Immutable copies of original raw articles
│   ├── indexes/            Thematic maps of related concepts
│   └── raw/                Temporary inbox for unprocessed markdown
│
└── skills/
    └── note-taking/
        └── obsidian-vault-processor/
            └── SKILL.md    Agent workflow for processing sources
```

## Quick Start

1. Clone this repository.
2. Open the Nexus/ folder as an Obsidian vault.
3. Start from the indexes/ folder.
4. Browse concepts/ and tools/ for atomic notes.
5. Check summaries/ for compressed source overviews.
6. Check raw-notes/ for the original, unmodified source material.
7. Add new markdown sources to Nexus/raw/ if you want to extend the vault (use the Obsidian Web Clipper).
8. Run your preferred agent using the provided skill to ingest new raw data.

## Knowledge Model

Nexus follows the [Open Knowledge Format (OKF) v0.1](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) specification for knowledge representation. All concept documents include YAML frontmatter with standardized fields (`type`, `title`, `description`, `resource`, `tags`, `timestamp`).

Nexus uses a lightweight semantic model:

| Folder           | Purpose                                                          |
| ---------------- | ---------------------------------------------------------------- |
| `concepts/`      | Atomic ideas, principles, definitions, and reusable technical concepts |
| `tools/`         | Specific tools, platforms, libraries, plugins, APIs, hardware, frameworks, and methodologies |
| `summaries/`     | Compressed summaries of original sources with wikilinks          |
| `raw-notes/`     | Immutable copies of original raw articles (never modified)       |
| `indexes/`       | Navigation maps across related notes                             |
| `raw/`           | Temporary inbox for unprocessed markdown                         |

### Architecture decisions

- **`concepts/` absorbs glossary, architectures, workflows** — definitions, architectural patterns, and procedural workflows live in concepts/. No separate folders.
- **`tools/` absorbs frameworks** — mental models, methodologies, and reusable thinking structures live in tools/.
- **`summaries/` replaces source-notes** — one compressed summary per source, with links to raw-notes/ and extracted concepts.
- **`raw-notes/` preserves originals** — every ingested article is copied unchanged here before processing. This is the immutable provenance layer.

## Note Format

### Atomic Note

```text
# Concept Name

## Definition

Short compressed explanation.

## Why It Matters

Why this concept is important.

## Key Ideas

- point
- point
- point

## Tradeoffs

Optional tradeoffs.

## Related

- [[Related-Concept]]
- [[Another-Concept]]

## Source

[[summaries/Author-Topic]]
```

### Summary (replaces source note)

```text
---
type: Article
title: "Original title"
description: "One-line summary of the source."
resource: "URL or source reference"
tags: [tag1, tag2]
timestamp: "YYYY-MM-DDT00:00:00Z"
author: "Author"
---

# Source Title

## Summary

Compressed 2-3 sentence summary.

## Core Concepts

- [[Concept-A]] -- short description
- [[Concept-B]] -- short description

## Key Insights

- insight
- insight

## Open Questions

- question

## Source

[[raw-notes/normalized-original-filename]]
```

## Processing Workflow

Nexus follows a source-to-knowledge pipeline:

1. Add raw markdown sources to Nexus/raw/
2. Copy each raw article unchanged to Nexus/raw-notes/ (immutable original)
3. Create one summary in Nexus/summaries/ per source
4. Extract reusable atomic notes into concepts/ or tools/
5. Create or update thematic indexes
6. Normalize all wikilinks
7. Validate that every wikilink resolves
8. Clean raw/ after verification

A detailed agent-compatible workflow is documented in: [obsidian-vault-processor/SKILL.md](skills/note-taking/obsidian-vault-processor/SKILL.md)

## Naming Rules

- Filenames use kebab-case
- Avoid spaces, accents, dots, and underscores
- Wikilinks must match the exact filename stem
- Wikilinks must include the folder path (e.g. `[[concepts/Agent-Swarm]]`, `[[summaries/Author-Topic]]`)
- Prefer stable concept names over source-specific names
- Avoid duplicate notes for overlapping ideas

Example:

```[[concepts/Agent-Swarm-Architecture]]```

must point to:

```concepts/Agent-Swarm-Architecture.md```

## Design Principles

1. **Atomicity** — Each note should capture one reusable idea.
2. **Compression** — Prefer short, high-signal explanations over long summaries.
3. **Reuse** — A note should be useful outside the source where it came from.
4. **Linkability** — Every important concept should connect to related concepts.
5. **Source Traceability** — Extracted notes point to summaries; summaries point to raw-notes/.
6. **Immutable Originals** — Raw articles are preserved unchanged in raw-notes/. Summaries are the processed layer.

## Current Status

This repository follows the [Open Knowledge Format (OKF) v0.1](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) specification. All concept documents include standardized YAML frontmatter.

This repository is an evolving knowledge vault.

The vault can be used directly in Obsidian.
The automated processing workflow is documented as an agent skill ([obsidian-vault-processor](skills/note-taking/obsidian-vault-processor/SKILL.md)).

---

## Roadmap

To be defined.

## License

Code and scripts: MIT License
Notes and written content: Creative Commons Attribution 4.0

Final license terms should be added before making this repository public.
