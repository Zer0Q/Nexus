---
type: Concept
title: Agent Skill Curator
description: Background maintenance system that cleans up agent-created skills. Runs
  on an inactivity check (7 days since last run + 2+ hours idle), spawning a background...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Skill Curator

## Definition
Background maintenance system that cleans up agent-created skills. Runs on an inactivity check (7 days since last run + 2+ hours idle), spawning a background fork with its own prompt cache, never touching active conversations.

## Why It Matters
Without maintenance, agent-created skills pile up into dozens of narrow, overlapping playbooks that waste tokens and pollute the skill catalog. The Curator ensures only useful skills survive.

## Key Ideas
- **Automatic transitions** (deterministic, no LLM): 30 days unused → stale, 90 days unused → archived
- **LLM review** (up to 8 iterations): forked agent surveys all agent-created skills, decides per-skill to keep, patch, consolidate, or archive
- Never touches bundled or hub-installed skills — only agent-authored ones
- Never auto-deletes — worst outcome is archival to .archive/ (recoverable)
- Takes tar.gz snapshot before every pass — rollback is one command
- Critical skills can be pinned with `hermes curator pin <skill>`

## Tradeoffs
- LLM review costs tokens (up to 8 iterations)
- May archive skills that are rarely needed but critical when needed
- Pinning protects from deletion but still allows patches/edits

## Related
- [[concepts/Self-Evolving-Skills]] -- creates the skills the Curator maintains
- [[concepts/GEPA-Prompt-Evolution]] -- ensures skills actually work before the Curator sees them
- [[concepts/Quarterly-Vault-Review]] -- similar periodic maintenance concept for knowledge vaults

## Source
[[summaries/AkshayPachaar-Hermes-Agent-Masterclass]]
