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
│   ├── concepts/           Atomic technical concepts
│   ├── frameworks/         Reusable mental models and methodologies
│   ├── tools/              Software, plugins, APIs, hardware
│   ├── architectures/      System design and architecture patterns
│   ├── workflows/          Step-by-step procedures and pipelines
│   ├── glossary/           Quick-reference definitions
│   ├── source_notes/       One note per source article
│   ├── indexes/            Thematic maps of related concepts
│   └── raw/                Incoming unprocessed markdown sources
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
4. Use glossary/ for quick definitions.
5. Browse concepts/, frameworks/, tools/, and architectures/ for atomic notes.
6. Add new markdown sources to Nexus/raw/ if you want to extend the vault. (use the Obsidian Web Clipper)
7. Run your preferred agent using the provided script to ingest new raw data

## Knowledge Model

Nexus uses a lightweight semantic model:

| Folder           | Purpose                                                          |
| ---------------- | ---------------------------------------------------------------- |
| `concepts/`      | Atomic ideas, principles, and reusable technical concepts        |
| `frameworks/`    | Mental models, methodologies, and reusable thinking structures   |
| `tools/`         | Specific tools, platforms, libraries, plugins, APIs, or hardware |
| `architectures/` | System structures, design patterns, and architectural decisions  |
| `workflows/`     | Repeatable procedures, pipelines, and operational steps          |
| `glossary/`      | Short definitions for fast lookup                                |
| `source_notes/`  | Compressed summaries of original sources                         |
| `indexes/`       | Navigation maps across related notes                             |
| `raw/`           | Temporary inbox for unprocessed markdown                         |



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

[[Source-Note]]
```

### Source Note

```text
---
title: "Original title"
source: "URL or source reference"
author: "Author"
published: "YYYY-MM-DD"
type: article
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
```

## Processing Workflow

Nexus follows a source-to-knowledge pipeline:

1. Add raw markdown sources to Nexus/raw/
2. Create one source note in Nexus/source_notes/
3. Extract reusable atomic notes
4. Place each note in the right folder
5. Create glossary entries when useful
6. Create or update thematic indexes
7. Normalize all wikilinks
8. Validate that every wikilink resolves

A detailed agent-compatible workflow is documented in: [note-taking/SKILL.md](https://github.com/Zer0Q/Nexus/blob/main/skills/note-taking/obsidian-vault-processor/SKILL.md)

## Naming Rules
- Filenames use kebab-case
- Avoid spaces, accents, dots, and underscores
- Wikilinks must match the exact filename stem
- Prefer stable concept names over source-specific names
- Avoid duplicate notes for overlapping ideas

Example:

```[[Agent-Swarm-Architecture]]```

must point to:

```Agent-Swarm-Architecture.md```

## Design Principles
1. Atomicity

Each note should capture one reusable idea.

2. Compression

Prefer short, high-signal explanations over long summaries.

3. Reuse

A note should be useful outside the source where it came from.

4. Linkability

Every important concept should connect to related concepts.

5. Source Traceability

Extracted notes should point back to their source note.

## Current Status

This repository is an evolving knowledge vault.

The vault can be used directly in Obsidian.
The automated processing workflow is currently documented as an agent procedure, not yet packaged as a standalone CLI.

---
 
## Roadmap
To be defined

## License

Code and scripts: MIT License
Notes and written content: Creative Commons Attribution 4.0

Final license terms should be added before making this repository public.
