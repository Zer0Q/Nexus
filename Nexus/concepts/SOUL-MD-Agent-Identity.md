---
type: Concept
title: SOUL.md Agent Identity
description: A concise identity file (SOUL.md) that defines an agent's personality,
  values, constraints, and operational boundaries — making the agent push back, hold
  sta...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# SOUL.md Agent Identity

## Definition
A concise identity file (SOUL.md) that defines an agent's personality, values, constraints, and operational boundaries — making the agent push back, hold standards, and refuse low-value tasks.

## Why It Matters
Default agent prompts produce compliant but useless output. SOUL.md gives agents a backbone — they challenge bad ideas, refuse slop, and maintain quality standards autonomously.

## Key Ideas
- ~170 lines of identity instructions
- Defines what the agent will and won't do
- Includes negative constraints (what to refuse)
- Sets accountability standards
- Creates split personality: helpful but principled

## Tradeoffs
- Overly strict SOUL.md blocks valid requests
- Requires careful calibration per use case
- Agent may push back when user just wants quick output

## Related
- [[concepts/SOUL-MD-Configuration]]
- [[concepts/SOUL-MD-Challenge-Instructions]]
- [[concepts/Compound-Effect-of-Persistent-Instructions]]

## Source
[[summaries/tonysimons-170-line-soul-md-hermes-agent-dangerous]]
