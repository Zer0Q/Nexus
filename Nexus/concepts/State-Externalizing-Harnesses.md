---
type: Concept
title: State Externalizing Harnesses
description: Agent training approach that offloads routine bookkeeping (candidate
  pools, curated sets, evidence links, verification records) from the agent policy
  into an...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# State Externalizing Harnesses

## Definition
Agent training approach that offloads routine bookkeeping (candidate pools, curated sets, evidence links, verification records) from the agent policy into an environment-side working memory, so RL only optimizes genuine search decisions rather than recoverable state tracking.

## Why It Matters
Search agents trained as policies over growing transcripts force RL to optimize both real decisions and recoverable state. Moving state out of the policy lets smaller models match or outperform much larger frontier searchers. Harness-1 (20B) reaches 0.730 curated recall across 8 benchmarks, beating open-source baselines by 11.4 points.

## Key Ideas
- Environment-side working memory holds: candidate pools, importance-tagged curated sets, compact evidence links, verification records
- Agent policy focuses on genuine search decisions (which evidence to pursue, which claims to check)
- Stronger generalization on unseen domains because the policy is not entangled with state tracking
- Decouples agent intelligence from infrastructure concerns

## Tradeoffs
- Requires designing the environment-side memory schema upfront
- May not apply to domains where state tracking IS the core decision (e.g., creative writing)
- Adds complexity to the training environment

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/LEAP]]
- [[concepts/AdaCoM]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week-June-7]]
