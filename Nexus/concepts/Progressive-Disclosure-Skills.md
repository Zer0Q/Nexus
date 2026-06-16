---
type: Concept
title: Progressive Disclosure Skills
description: 'Token-efficient skill loading system with three levels: names + descriptions
  only (~3k tokens for full catalog), full skill content on demand, and drill-down...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Progressive Disclosure Skills

## Definition
Token-efficient skill loading system with three levels: names + descriptions only (~3k tokens for full catalog), full skill content on demand, and drill-down into specific reference files. The agent sees the catalog at Level 0 and only loads details when needed.

## Why It Matters
Loading all skill content into context every turn wastes tokens. Progressive disclosure keeps the agent aware of available skills without the cost of full content, loading details only when a skill is actually relevant to the current task.

## Key Ideas
- **Level 0**: Names + descriptions (~3k tokens for full catalog). Agent scans this to find relevant skills.
- **Level 1**: Full skill content loaded when the agent needs a specific skill.
- **Level 2**: Reference files within a skill (references/, scripts/, templates/) loaded on demand.
- Reduces input token overhead significantly compared to loading all skills upfront
- Enables large skill catalogs without context window explosion

## Tradeoffs
- Extra round-trip to load full content after scanning catalog
- Risk of missing relevant skills if descriptions are unclear
- Agent may load skills it doesn't actually need (over-cautious scanning)

## Related
- [[concepts/Self-Evolving-Skills]] -- the skills that use progressive disclosure
- [[concepts/Context-Explosion]] -- mitigates context growth from too many loaded resources
- [[concepts/Compounding-Knowledge-Context]] -- efficient context management enables compounding

## Source
[[summaries/AkshayPachaar-Hermes-Agent-Masterclass]]
