---
type: Article
title: "WTF Is a Loop? Peter Steinberger vs. Boris Cherny"
description: "A field report on the meaning of agent loops, from ReAct-style steps to scheduled orchestration, skills, verification, and cost."
resource: "https://x.com/mvanhorn/status/2063865685558903149"
tags: [agent-loops, loop-engineering, skills]
timestamp: "2026-06-23T00:00:00Z"
author: "@mvanhorn"
---

# WTF Is a Loop

## Summary
The article disentangles hype around "loops" by positioning them on a spectrum from simple ReAct cycles to scheduled, tool-using orchestration systems. Its strongest point is that loops are not magic autonomy: the expensive parts are verification, skills, context, and the human work of turning repeated observation into reusable tooling.

## Core Concepts
- [[concepts/Agent-Loop]] -- observe, act, evaluate, and repeat until a condition changes.
- [[concepts/Loop-Engineering]] -- designing recurring systems that prompt and verify agents rather than manually prompting them.
- [[concepts/ReAct-Framework]] -- the basic think-act-observe pattern underlying many agent loops.
- [[concepts/Skills-as-Primitives]] -- reusable skills often matter more than a generic loop wrapper.
- [[concepts/Token-Burn]] -- cost becomes central when loops run repeatedly or coordinate many agents.

## Key Insights
- "Loop" is used for many different systems, from interactive agent cycles to cron-like recurring work and multi-agent orchestration.
- Peter Steinberger's framing highlights removing humans from repeated observation, judgment, and routing tasks.
- Boris Cherny's framing points toward loops as a programming interface for agents, especially when paired with tools and memory.
- The research pattern shows loops only matter when they include verification and a useful skill/tool substrate.
- Cost and comprehension debt grow with autonomy, so blindly scaling loops can make the human less capable of judging the output.

## Open Questions
- Where should this vault draw the boundary between [[concepts/Agent-Loop]], [[concepts/Loop-Engineering]], and [[concepts/Orchestrator-Workers-Workflow]]?
- Which loop use cases justify [[concepts/Token-Burn]] versus simple human prompting?
- Are skills the more durable abstraction than loops for most agent work?

## Source
[[raw-notes/wtf-is-a-loop-peter-steinberger-vs-boris-cherny]]
