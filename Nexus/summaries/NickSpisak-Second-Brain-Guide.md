---
title: How to Build Your Second Brain
author: '@NickSpisak_'
published: '2026-04-04'
type: article
resource: https://x.com/NickSpisak_/status/2040448463540830705
timestamp: '2026-04-04T00:00:00Z'
description: 'Practical guide to building a Karpathy-style knowledge base: three folders
  (raw/, wiki/, outputs/), automated source collection with agent-browser CLI, schem...'
tags:
- summaries
---


# Nick Spisak Second Brain Guide

## Summary
Practical guide to building a Karpathy-style knowledge base: three folders (raw/, wiki/, outputs/), automated source collection with agent-browser CLI, schema file (CLAUDE.md/AGENTS.md), LLM compilation of wiki, iterative Q&A with answers saved back, and monthly health checks. Emphasizes that flat files + schema outperform complex tool stacks.

## Core Concepts
- [[concepts/LLM-Wiki-Pattern]] -- raw to wiki compilation pattern
- [[concepts/Knowledge-Source-of-Truth]] -- raw/ as immutable source
- [[concepts/Anti-Graveyard-Capture]] -- saving answers back into the KB
- [[concepts/Markdown-as-Universal-Format]] -- flat files over proprietary tools
- [[concepts/CLAUDE-MD-as-Context-Layer]] -- schema as AI instruction manual
- [[Periodic KB Health Check]] -- monthly linting for contradictions and gaps

## Key Insights
- Three folders are enough: raw (sources), wiki (organized), outputs (answers)
- agent-browser CLI lets AI scrape web pages directly into raw/
- Schema file is the most important component -- don't skip it
- Don't edit wiki by hand -- that's the AI's job
- Save answers back to make the KB smarter iteratively
- Obsidian with 47 plugins is the "Notion trap" -- flat files win 90% of the time

## Open Questions
- How does agent-browser compare to Obsidian Web Clipper for bulk collection?
- At what point does the wiki/ folder become too large for the LLM to navigate?

## Source

- **Raw note:** [[how-to-build-your-second-brain.md]]
- **Original URL:** https://x.com/NickSpisak_/status/2040448463540830705
