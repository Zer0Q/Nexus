---
type: Concept
title: Automated Business Workflows
description: 'Six interconnected systems running on schedule and trigger within an
  Obsidian vault: client intelligence (pre-call briefs, communication logging), project
  op...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Automated Business Workflows

## Definition
Six interconnected systems running on schedule and trigger within an Obsidian vault: client intelligence (pre-call briefs, communication logging), project operations (daily pulse, auto-updater), content production (morning brief, draft engine, performance tracker), financial operations (revenue logging, monthly brief, invoice reminders), research/intelligence (daily brief, research queue), and performance/review (weekly review, quarterly review).

## Why It Matters
Removes the knowledge worker from 4-6 hours/day of administrative coordination. The vault runs the business while you sleep -- you capture tasks when they occur, the system executes them on its next cycle, you review results when convenient.

## Key Ideas
- N8N workflow pattern: trigger -> read CLAUDE.md -> read vault -> call Claude -> write output -> notify -> log
- Three trigger types: cron (scheduled), file watch (event-based), webhook (external events)
- QUEUE/GENERATED async pattern: drop request, system processes, output appears
- Weekly Focus in CLAUDE.md weights all actions toward current priorities
- After 6 months: vault knows business at depth requiring years of human onboarding

## Tradeoffs
- Complex setup with multiple interconnected workflows
- Token costs for daily/weekly AI processing
- Risk of automated errors compounding if not reviewed

## Related
- [[concepts/Three-Layer-Architecture]]
- [[concepts/Async-Queue-Pattern]]
- [[concepts/Compounding-Knowledge-Context]]

## Source
[[summaries/CyrilXBT-Business-Operating-System]]
