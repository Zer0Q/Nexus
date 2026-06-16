---
type: Concept
title: Agent-Computer Interface (ACI)
description: 'The interface between LLM agents and the tools/systems they interact
  with. Design principles: give the model enough tokens to think, keep formats natural,
  el...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent-Computer Interface (ACI)

## Definition
The interface between LLM agents and the tools/systems they interact with. Design principles: give the model enough tokens to think, keep formats natural, eliminate formatting overhead, and poka-yoke to prevent mistakes.

## Why It Matters
Tool design is as important as prompt design. Poor ACI design causes systematic agent errors that no amount of prompt engineering can fix. Anthropic spent more time optimizing tools than prompts for their SWE-bench agent.

## Key Ideas
- Give model tokens to "think" before committing to a format (avoid writing yourself into a corner)
- Keep formats close to what the model has seen naturally (markdown > JSON for code)
- Eliminate formatting overhead (no line counting, no string escaping)
- Poka-yoke: make it harder to make mistakes (absolute paths > relative paths)
- Invest in ACI design as much as HCI design
- Test tool usage with many example inputs, iterate on mistakes
- Good tool definition: example usage, edge cases, input format, boundaries from other tools

## Tradeoffs
- More user-friendly formats for humans may be harder for LLMs
- Simpler tool interfaces may require more tools to cover the same functionality

## Related
- [[concepts/Agent-Tool-Use]]
- [[concepts/Augmented-LLM]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
