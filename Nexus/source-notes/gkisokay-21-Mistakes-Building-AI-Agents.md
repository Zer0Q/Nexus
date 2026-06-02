---
title: "21 painful mistakes I made building AI agents so you don't have to"
source: "https://x.com/gkisokay/status/2059986597391823286"
author: "@gkisokay"
published: "2026-05-04"
type: article
---

# 21 Mistakes Building AI Agents

## Summary
Practical lessons from 3 months of building Hermes and OpenClaw agents daily: build specialized agent crews not monoliths, research-first architecture, cost tracking for autonomous loops, model diversity for resilience, local LLMs for always-on cognition, and skill bundling over monolithic prompts.

## Core Concepts
- [[concepts/Specialized-Agent-Crews]] -- multiple focused agents with clear ownership beat one bloated agent
- [[concepts/Research-First-Architecture]] -- research agent as input intelligence layer feeding all other agents
- [[concepts/Runtime-Monitoring]] -- supervisor watching intended flow vs actual flow, catching failures mid-run
- [[concepts/Cost-Tracking]] -- logging exact cost per run; critical for 24/7 autonomous loops
- [[concepts/Model-Diversity]] -- multi-provider resilience against downtime, pricing changes, quality drops
- [[concepts/Agent-Decay]] -- agents degrade over time without weekly audits after updates
- [[concepts/Content-Agent-Architecture]] -- voice replication is not enough; need taste, thesis, proof, forbidden patterns

## Key Insights
- Agents fail on architecture, not intelligence; most bugs are tools fighting each other
- Autonomous workflows need a supervisor layer to catch failures mid-run
- Self-building systems need a self-thinking layer first (noticing friction, failed runs, bottlenecks)
- Define what "done" means with acceptance criteria, recovery logic, and success checks
- Use frontier models for planning/debugging; local models for scanning/summaries
- The system around the model (research, routing, memory, supervision) is the product, not the model itself
- Boring infrastructure (clean inputs, handoffs, monitoring, evals) is the real moat

## Open Questions
- How do you quantify the ROI of runtime monitoring vs post-hoc debugging?
- What's the optimal threshold for when a monolithic agent should be split into specialized ones?
