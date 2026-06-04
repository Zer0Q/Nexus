---
title: "llm-wiki"
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
author: "@karpathy"
published: ""
type: article
---

# LLM Wiki Pattern

## Summary
Karpathy's canonical description of the LLM wiki pattern: instead of RAG (query-time retrieval from raw docs), the LLM incrementally builds and maintains a persistent wiki of interlinked markdown files. Three layers: raw sources (immutable), wiki (LLM-maintained), schema (instructions for the LLM). Three operations: ingest (compile new sources), query (ask questions, file answers back), lint (health checks). Index and log files help navigation.

## Core Concepts
- [[concepts/LLM-Wiki-Pattern]] -- persistent wiki as compiled knowledge artifact
- [[concepts/Write-Time-Knowledge-Systems]] -- compile once, query many times
- [[concepts/Knowledge-Source-of-Truth]] -- raw sources are immutable
- [[tools/Compilation-Agent]] -- LLM as wiki maintainer
- [[concepts/Anti-Graveyard-Capture]] -- filed outputs compound knowledge
- [[concepts/Browsable-Knowledge]] -- Obsidian as wiki viewer

## Key Insights
- The wiki is a compounding artifact: cross-refs, contradictions, synthesis accumulate
- Schema file (CLAUDE.md/AGENTS.md) makes the LLM a disciplined maintainer
- Index file (content catalog) + log file (chronological record) enable navigation
- At moderate scale (~100 sources, ~hundreds of pages), index files beat RAG infrastructure
- The human curates sources and asks questions; the LLM does all bookkeeping
- Related to Vannevar Bush's Memex (1945) -- private, curated, associative links

## Open Questions
- How does the schema evolve as the wiki grows from hundreds to thousands of pages?
- What happens when the LLM makes a synthesis error that compounds?
