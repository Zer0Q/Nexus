---
type: Concept
title: Scoped Vault Access
description: 'A safety pattern for connecting AI agents to knowledge vaults: start
  by granting access to a dedicated subfolder, verify clean read/write behavior over
  sever...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Scoped Vault Access

## Definition
A safety pattern for connecting AI agents to knowledge vaults: start by granting access to a dedicated subfolder, verify clean read/write behavior over several days, then expand to the full vault. Never grant full vault access on day one.

## Why It Matters
AI agents can read and write files. Without scoped testing, a misconfigured agent could corrupt notes, create spam files, or leak sensitive information. Scoped access provides a controlled environment to verify behavior before expanding permissions.

## Key Ideas
- Create a dedicated folder (e.g., 04-Claude/hermes/) for initial access
- Run the agent for 3+ days reading and writing only within that scope
- Verify: no unexpected files created, no existing files corrupted, output quality acceptable
- Expand to full vault only after confidence is established
- This is especially important for vaults with personal or sensitive content

## Tradeoffs
- Slower onboarding -- you cannot get full benefits until scoped testing passes
- Agent may produce different quality output with limited context vs. full vault
- Some users skip this step and regret it

## Related
- [[concepts/Hermes-Obsidian-Integration]] -- the setup this pattern applies to
- [[concepts/Read-Only-Vault-Safety]] -- stricter alternative: read-only access only
- [[concepts/Risk-by-Design]] -- broader safety-by-default philosophy

## Source
[[summaries/DamiDefi-Hermes-Obsidian-Vault-Integration]]
