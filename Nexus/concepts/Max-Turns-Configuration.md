---
type: Concept
title: Max Turns Configuration
description: The goals.max_turns setting that controls how many reasoning-action cycles
  a /goal execution can perform before terminating. Default is 5-10; raise for compl...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Max Turns Configuration

## Definition
The goals.max_turns setting that controls how many reasoning-action cycles a /goal execution can perform before terminating. Default is 5-10; raise for complex tasks (20 for research/reports, 50 for code refactoring).

## Why It Matters
Setting max_turns too low truncates complex tasks mid-execution. Setting it too high wastes tokens on tasks that could finish in fewer steps. It's the primary knob for controlling goal complexity and cost.

## Key Ideas
- Default: 5-10 turns (sufficient for simple tasks)
- Research, reports, content drafts: raise to 20
- Code refactoring, multi-step builds: raise to 50
- Configure via: `hermes config set goals.max_turns <number>`
- Don't go higher without a reason — every turn costs tokens
- The 90-turn hard cap in [[concepts/Hermes-Agent-Architecture]] is the absolute ceiling

## Tradeoffs
- Higher max_turns = more token cost per goal
- Too low = truncated tasks, incomplete deliverables
- No auto-scaling — you must judge the right number per task type

## Related
- [[concepts/Goal-Command]] -- max_turns controls /goal execution depth
- [[concepts/Overnight-Goal-Runs]] -- overnight tasks typically need higher max_turns
- [[concepts/Hermes-Agent-Architecture]] -- 90-turn hard cap is the system ceiling

## Source
[[summaries/IBuzovskyi-Hermes-Agent-Complete-Guide]]
