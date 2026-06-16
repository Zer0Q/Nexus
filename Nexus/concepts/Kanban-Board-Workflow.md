---
type: Concept
title: Kanban Board Workflow
description: The Kanban task board in the Hermes Dashboard (v0.12.0+) that automates
  task triage, splitting, assignment, and execution. Drop tasks into Triage, walk
  away,...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Kanban Board Workflow

## Definition
The Kanban task board in the Hermes Dashboard (v0.12.0+) that automates task triage, splitting, assignment, and execution. Drop tasks into Triage, walk away, and the daemon processes them through six statuses automatically.

## Why It Matters
Transforms a list of to-dos into an automated execution pipeline. By the time you finish breakfast, half your task list is complete — the agent splits, assigns, and executes without babysitting.

## Key Ideas
- **Six statuses**: Triage → To-Do → Ready → In Progress → Blocked → Done
- **Automated pipeline**: Hermes takes tasks from Triage, splits into subtasks, assigns to sub-agents, executes in parallel
- **Daemon**: Runs continuously (v0.16+), checks for new tasks every 60 seconds
- No cron-based polling, no wasted tokens between tasks
- Multi-agent: different profiles can claim tasks from the board
- Morning routine: write to-do list, drop AI-handlable tasks in Triage, walk away

## Tradeoffs
- Tasks must be AI-handlable (not everything fits)
- Blocked tasks require human intervention
- Daemon consumes resources running continuously

## Related
- [[concepts/Hermes-Dashboard]] -- where the Kanban board lives
- [[concepts/Goal-Command]] -- Kanban automates /goal-style execution
- [[concepts/Multi-Agent-Org-Chart]] -- agents claim tasks from the board
- [[concepts/Agent-Cron-Scheduler]] -- daemon runs continuously vs cron polling

## Source
[[summaries/IBuzovskyi-Hermes-Agent-Complete-Guide]]
