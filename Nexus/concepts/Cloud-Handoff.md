---
type: Concept
title: Cloud Handoff
description: The ability to start a long-running coding task locally in Cursor, hand
  it off to Cursor's cloud infrastructure, close your laptop, and have the results
  sync...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Cloud Handoff

## Definition
The ability to start a long-running coding task locally in Cursor, hand it off to Cursor's cloud infrastructure, close your laptop, and have the results sync back when you reconnect. Built for migrations, large refactors, and test suite generation that would otherwise run for hours.

## Why It Matters
Long coding tasks (database migrations, full refactors, test suite generation) can take hours. Cloud handoff means your laptop can close while the work continues. When you reconnect, the pull request is waiting for your review.

## Key Ideas
- Start the task locally in the Cursor Agents Window
- Click "Hand off to Cloud" in the Agents Window
- Close your laptop -- the agent keeps running on Cursor's infrastructure
- When you reconnect, the pull request is waiting for your review
- Example: migrate entire database layer from PostgreSQL to Supabase in four phases
- Built specifically for tasks that would otherwise block your machine for hours

## Tradeoffs
- Cloud handoff requires Cursor Pro plan
- Network connectivity needed to reconnect and review results
- Sensitive code runs on Cursor's infrastructure, not your local machine

## Related
- [[concepts/Cursor-Agents-Window]] -- the interface where cloud handoff is initiated
- [[concepts/Five-Layer-AI-Stack]] -- part of Cursor's execution layer capabilities
- [[concepts/Long-Horizon-Coding]] -- cloud handoff enables long-horizon tasks on limited hardware

## Source
[[summaries/Damidefi-Five-Tool-AI-Stack-Full-Build]]
