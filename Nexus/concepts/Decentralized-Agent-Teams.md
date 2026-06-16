---
type: Concept
title: Decentralized Agent Teams
description: A multi-agent architecture where agents self-organize around promising
  hypotheses without a central planner. Agents interpret shared experimental state,
  form...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Decentralized Agent Teams

## Definition
A multi-agent architecture where agents self-organize around promising hypotheses without a central planner. Agents interpret shared experimental state, form teams around directions, critique each other's proposals before spending compute, and reorganize when progress stalls.

## Why It Matters
Most multi-agent research systems funnel decisions through a planner that becomes a bottleneck. Decentralized self-organization sustains parallel search instead of a single thread, and explicit failure-sharing prevents redundant exploration.

## Key Ideas
- AutoScientists (Harvard): decentralized team for long-running computational science
- No central planner -- coordination emerges from common state
- Proposals are critiqued and scored before experimental compute is allocated
- Both successes and failures are recorded to avoid redundant exploration
- 74.4% mean leaderboard percentile on BioML-Bench (24 biomedical ML tasks), +8.33% over strongest prior AI agent
- Sustains parallel search across hours or days of experimentation

## Tradeoffs
- Emergent coordination vs explicit control -- harder to steer individual agents
- Failure-sharing overhead vs redundancy prevention
- Domain generality -- does self-organization work outside scientific search?

## Related
- [[concepts/Agent-Swarm-Architecture]]
- [[concepts/Multi-Agent-Development]]
- [[concepts/Agent-Logic]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week]]
