---
type: Concept
title: Overnight Goal Runs
description: Using Hermes Agent's /goal command to execute complex, multi-hour tasks
  while you sleep. Wake up with completed research reports, code refactoring, database
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Overnight Goal Runs

## Definition
Using Hermes Agent's /goal command to execute complex, multi-hour tasks while you sleep. Wake up with completed research reports, code refactoring, database migrations, SEO audits, or full app builds.

## Why It Matters
Turns idle hours into productive output. A task that would take a human analyst a full day can be queued before bed and completed by morning — effectively giving you extra working hours every night.

## Key Ideas
- Queue complex task before bed via /goal
- Agent executes autonomously through the night
- Wake up with finished deliverables saved to file
- Common use cases: competitor research reports, code refactoring, database migrations, full app builds, SEO audits, content calendars
- Set [[concepts/Max-Turns-Configuration]] higher for complex overnight tasks (20 for research/reports, 50 for code refactoring)
- Don't raise max_turns without reason — every turn costs tokens

## Tradeoffs
- Higher max_turns = higher token cost
- Complex tasks may hit blockers requiring human intervention
- Overnight runs need well-scoped goals to avoid scope creep

## Related
- [[concepts/Goal-Command]] -- the /goal mechanism enabling overnight runs
- [[concepts/Max-Turns-Configuration]] -- configuring complexity for long runs
- [[concepts/Kanban-Board-Workflow]] -- automated overnight execution via the board
- [[concepts/Agent-Cron-Scheduler]] -- scheduled alternative for recurring overnight tasks

## Source
[[summaries/IBuzovskyi-Hermes-Agent-Complete-Guide]]
