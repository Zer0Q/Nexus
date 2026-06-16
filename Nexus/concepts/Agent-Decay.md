---
type: Concept
title: Agent Decay
description: The gradual degradation of agent performance over time due to stale tools,
  outdated models, deprecated MCPs, and drifted workflows. Agents need weekly audits...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Decay

## Definition
The gradual degradation of agent performance over time due to stale tools, outdated models, deprecated MCPs, and drifted workflows. Agents need weekly audits after updates to prevent silent performance regression.

## Why It Matters
Agents are not set-and-forget systems. The tools, models, and APIs they depend on change continuously. Without regular maintenance, agents accumulate technical debt that manifests as subtle failures, incorrect outputs, and broken integrations.

## Key Ideas
- Weekly audits after updates to tools, models, MCPs, and workflows
- Decay mechanisms: API changes, model updates, tool deprecations, workflow drift
- Silent failures are the most dangerous -- agent appears to work but produces degraded output
- Maintenance is part of the agent lifecycle, not an afterthought
- Agent decay is related to but distinct from agent aging (which is about memory/state degradation)

## Tradeoffs
- Audit frequency vs operational overhead
- Automated health checks vs manual review
- Rollback vs update -- when a new version degrades performance, revert or adapt?

## Related
- [[concepts/Agent-Aging]]
- [[concepts/Runtime-Monitoring]]
- [[concepts/Specialized-Agent-Crews]]

## Source
[[summaries/gkisokay-21-Mistakes-Building-AI-Agents]]
