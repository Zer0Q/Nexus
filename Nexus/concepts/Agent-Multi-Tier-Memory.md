---
type: Concept
title: Agent Multi-Tier Memory
description: 'A three-layer memory system for AI agents, each optimized for different
  access patterns: frozen snapshot (always in context, tiny), session search (unlimited...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Multi-Tier Memory

## Definition
A three-layer memory system for AI agents, each optimized for different access patterns: frozen snapshot (always in context, tiny), session search (unlimited, on-demand), and external providers (deep persistent memory plugins).

## Why It Matters
Single-memory agents either forget everything between sessions or waste tokens loading irrelevant context. Tiered memory lets critical facts stay in-context while keeping a searchable archive of everything else.

## Key Ideas
- **Tier 1**: Two small Markdown files (MEMORY.md ~2200 chars, USER.md ~1375 chars) injected as frozen snapshot at session start. Changes persist to disk but only appear in next session. Auto-consolidation at ~80% capacity.
- **Tier 2**: SQLite with FTS5 full-text search over all past conversations. Unlimited capacity but requires active search + LLM summarization.
- **Tier 3**: Eight pluggable external memory providers (prefetch before turn, sync after response, extract on session end). Only one active at a time.

## Tradeoffs
- Tier 1: always available but tiny — requires careful consolidation
- Tier 2: unlimited but costs tokens per search
- Tier 3: powerful but adds latency per turn

## Related
- [[concepts/Agent-Identity-Layer]] -- the fixed frame above memory
- [[concepts/Self-Evolving-Skills]] -- procedural memory (companion to factual memory)
- [[concepts/Compounding-Knowledge-Context]] -- memory enables compounding across sessions

## Source
[[summaries/AkshayPachaar-Hermes-Agent-Masterclass]]
