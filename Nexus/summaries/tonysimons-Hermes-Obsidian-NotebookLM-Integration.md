---
title: Wire Hermes + Obsidian + NotebookLM (2026 Build Guide)
author: Tony Simons
published: '2026-06-08'
type: article
resource: https://www.tonyreviewsthings.com/wire-hermes-agent-obsidian-notebooklm-stack/
timestamp: '2026-06-08T00:00:00Z'
description: 'Step-by-step guide for wiring Hermes Agent, Obsidian, and NotebookLM
  into an automated research loop: Hermes cron jobs watch Obsidian Sources/ for new
  files,...'
tags:
- summaries
---


# Hermes + Obsidian + NotebookLM Integration

## Summary
Step-by-step guide for wiring Hermes Agent, Obsidian, and NotebookLM into an automated research loop: Hermes cron jobs watch Obsidian Sources/ for new files, push them to a NotebookLM notebook via the notebooklm-py wrapper (Playwright-based, no public API), ask grounded questions, and write answers back to the vault. The key insight is starting with a no-agent cron job (zero LLM tokens) to prove the wire works before adding LLM-calling skills. The loop has 4 documented failure modes: hallucinated citations, notebook ID drift, vault-notebook desync, and hardcoded secrets.

## Core Concepts
- Local-REST-API-Plugin -- Obsidian community plugin (v4.1.3, 484k+ downloads) that exposes the vault as a local MCP server on 127.0.0.1:27124, enabling any Hermes cron job or skill to read/write the vault via file CRUD, active-file read/write, JsonLogic search, and tag queries
- NotebookLM-Py -- community wrapper (v0.7.1) that drives the NotebookLM web UI via Playwright since Google has no public consumer API; supports source add, ask, generate audio, download; fragile to internal endpoint changes
- No-Agent-Cron -- Hermes cron mode that runs scripts without LLM tokens; a 10-line bash script watching Sources/ with find -newer + .last-pushed sentinel for idempotent uploads; the load-bearing cheap primitive for proving the wire works
- [[concepts/Grounded-Research-Loop]] -- closed loop: sources in Obsidian -> NotebookLM for bounded research -> grounded answers with inline citations back to vault -> morning briefing via Hermes; the loop itself is the product, not the individual notes

## Related
- [[concepts/MCP]]
- [[concepts/Hermes-Agent-Architecture]]
- [[tools/NotebookLM]]

## Key Insights
- The three tools cover non-overlapping jobs: Obsidian (durable substrate), NotebookLM (bounded-research sandbox), Hermes (scheduled operator)
- NotebookLM has NO public consumer API as of 2026-06-07; the Enterprise product does, but for consumers the notebooklm-py wrapper is the only automation path
- The wiring pattern (cron -> skill -> MCP -> vault) is operator-agnostic: Claude Code, Cursor, and Claude Desktop all have first-class MCP support for the same Local REST API plugin
- Local REST API v4.1.3 (2026-06-04) fixed a path-traversal vulnerability; update before wiring
- The no-agent cron costs zero LLM tokens and scales to thousands of files; the expensive LLM skills (Steps 4, 5, 7) are optional additions
- Google AI Free tier ($0, 15 GB) is sufficient for most builder loops; Plus is $7.99/mo (200 GB)
- The 4 failure modes are real and expected: citation hallucination, notebook ID drift, vault-rename-desync, hardcoded secrets
- Templater plugin recommended for deterministic file naming (Sources/{{date}}-{{slug}}.md) so find -newer always returns the right files

## Open Questions
- How fragile is the notebooklm-py wrapper to Google internal endpoint changes -- what's a viable fallback strategy when it breaks?
- Can the Local REST API plugin's MCP server handle concurrent writes from multiple Hermes cron jobs without conflicts?

## Source
- **Raw note:** [[raw-notes/wire-hermes-obsidian-notebooklm-2026-build-guide]]
- **Original URL:** https://www.tonyreviewsthings.com/wire-hermes-agent-obsidian-notebooklm-stack/
