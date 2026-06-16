---
type: Concept
title: Five-Tool AI Stack
description: 'A five-layer AI stack where each tool owns a distinct operational layer:
  Claude (reasoning and context), Obsidian (memory), Kimi K2.6/open models (orchestrat...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Five-Tool AI Stack

## Definition
A five-layer AI stack where each tool owns a distinct operational layer: Claude (reasoning and context), Obsidian (memory), Kimi K2.6/open models (orchestration), Cursor (execution), and N8N (automation). Each tool does something the others cannot replicate.

## Why It Matters
The common mistake is using one tool for all five layers (ChatGPT for everything, or Claude for everything). The $30K vault uses the right tool at each layer: Claude is the brain, Obsidian is the memory, open models scale the cheap work, Cursor ships when code is required, and N8N glues it together.

## Key Ideas
- **Claude**: Reasoning and context layer. 200K window. Holds the whole vault during synthesis. Writes drafts that sound like you.
- **Obsidian**: Memory layer. Plain markdown, local, yours. Survives every model swap.
- **Kimi K2.6 / open models**: Orchestration layer. Long-horizon tasks Claude does not have to babysit. Open-source, free, runs 4000 steps.
- **Cursor**: Execution layer. For when output is code or product. Cloud handoff means your laptop can close.
- **N8N**: Automation layer. $5/month droplet. Schedules every workflow, routes captures, runs the loop while you sleep.

## Tradeoffs
- Five tools means five integrations to maintain and troubleshoot
- Context switching between tools has a cognitive cost
- Each tool has its own learning curve and configuration surface

## Related
- [[concepts/Five-Layer-AI-Stack]] -- similar concept from a different article, different tool assignments
- [[concepts/Four-Layer-Vault-Architecture]] -- related but focuses on vault layers rather than tool layers
- [[concepts/Model-Selection-Tiers]] -- cost-optimized routing within the automation layer

## Source
[[summaries/Zeuuss-Weaponize-Obsidian-Claude-For-Revenue]]
