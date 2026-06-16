---
type: Concept
title: Open vs Closed Loop
description: The fundamental distinction between exploratory agent loops (open) and
  bounded, verifiable loops (closed). Open loops let agents roam freely through discover...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Open vs Closed Loop

## Definition
The fundamental distinction between exploratory agent loops (open) and bounded, verifiable loops (closed). Open loops let agents roam freely through discovery and planning, burning tokens at exploratory rates. Closed loops constrain agents within a human-designed framework with clear goals, defined steps, evaluation gates, and stop conditions.

## Why It Matters
Open loops are the exciting end but burn an insane amount of tokens — impractical for 90% of builders without unlimited API budgets. Closed loops run on a normal budget because the path is tight and the standard keeps the agent honest. Without a quality gate, AI drifts. With a quality gate, AI improves.

## Key Ideas
- Open looping: exploratory, wide space, agent tries different paths, builds something not fully spec'd out — fast, messy, expensive
- Closed looping: bounded, clear goal, defined steps, evaluation at each step, stop or handback point — reliable, affordable, the one that pays off today
- Token economics: single agent loop costs 50K-200K tokens, fleet loop costs 500K-2M tokens, scheduled daily loops cost millions per week
- Start with closed loops, build a tight reliable system, then open it up once quality gates are proven
- Cheap models (DeepSeek V4 at 1.7B tokens for $20) remove the last real blocker to loop engineering

## Tradeoffs
- Open loops can discover solutions outside human specification but produce slop without strong eval gates
- Closed loops are reliable but constrained by the human's initial design — cannot surprise you with better approaches
- The transition from closed to open requires mature verification infrastructure

## Related
- [[concepts/Loop-Engineering]]
- [[concepts/Token-Burn]]
- [[concepts/Single-vs-Fleet-Loop]]
- [[concepts/Maker-Checker-Split]]

## Source
[[summaries/Sairahul1-Loops-What-Every-AI-Engineer-Needs-to-Know]]
