---
type: Concept
title: Telegram Vault Query
description: Using a Telegram bot connected to Hermes Agent to query your full knowledge
  vault from any device. Unlike Telegram capture bots that only save content, this
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Telegram Vault Query

## Definition
Using a Telegram bot connected to Hermes Agent to query your full knowledge vault from any device. Unlike Telegram capture bots that only save content, this allows bidirectional interaction -- send a question and receive vault-grounded answers from your phone.

## Why It Matters
Multi-surface access removes the constraint of being at your desk to research. An idea on a walk can be immediately checked against your thesis notes. The capture-to-intelligence gap collapses because the idea enters the vault and instantly has access to everything the vault contains.

## Key Ideas
- Hermes runs on desktop; Telegram bot connects remotely
- Supports research queries, not just content capture
- Example: "Does this connect to anything in my RWA thesis notes?"
- Agent reads the vault and returns connections, implications, and relevance
- Setup: create bot via BotFather, copy token, add to Hermes config

## Tradeoffs
- Requires Hermes daemon running on desktop (not fully mobile)
- Complex queries may be limited by phone screen real estate
- Token costs for vault reads on each query

## Related
- [[tools/Telegram-Bot-Capture]] -- the simpler unidirectional capture-only version
- [[concepts/Capture-to-Intelligence-Gap]] -- what this collapses
- [[concepts/Hermes-Obsidian-Integration]] -- the vault connection this queries

## Source
[[summaries/DamiDefi-Hermes-Obsidian-Vault-Integration]]
