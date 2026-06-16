---
title: How Checkpoints and /rollback make Hermes safer to use on real work
author: NeoAIForecast
published: '2026-04-17'
type: article
resource: https://x.com/NeoAIForecast/status/2045097742935195775
timestamp: '2026-04-17T00:00:00Z'
description: Most AI agent demos focus on what the agent can do. Write code. Refactor
  files. Run shell commands. Modify a project in seconds. The harder question is what
  ...
tags:
- summaries
---


# How Checkpoints and rollback make Hermes safer to use on real work

## Summary
Most AI agent demos focus on what the agent can do. Write code. Refactor files. Run shell commands. Modify a project in seconds. The harder question is what happens when the agent does the wrong thing. That is where a lot of AI tooling still feels immature. It can act, but it does not always give you a clean, native way to recover when the action was wrong.

## Core Concepts
- [[concepts/Hermes-Agent-Architecture]] -- related concept
- [[concepts/Agent-Profiles]] -- related concept
- [[concepts/Agent-Skill-Curator]] -- related concept
- [[concepts/Session-Recall]] -- related concept
- [[concepts/Hermes-Checkpoints-Rollback]] -- related concept
## Key Insights
- ~/.hermes/checkpoints/
- Inside a Hermes session, you can list checkpoints with:
- You can restore a checkpoint with:
- What problem this solves
- What Hermes actually does

## Open Questions
- How does this approach scale in production?
- What are the tradeoffs compared to alternatives?

## Source

- **Raw note:** [[how-checkpoints-and-rollback-make-hermes-safer-to-use-on-real-work.md]]
- **Original URL:** https://x.com/NeoAIForecast/status/2045097742935195775
