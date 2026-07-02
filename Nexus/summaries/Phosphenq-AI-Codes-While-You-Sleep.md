---
type: Article
title: "Loop Engineering: Build an AI That Codes While You Sleep"
description: "A practical loop engineering guide covering state files, automations, worktrees, skills, connectors, sub-agents, brakes, and failure modes."
resource: "https://x.com/phosphenq/status/2068468824421364103"
tags: [loop-engineering, coding-agents, automation]
timestamp: "2026-06-23T00:00:00Z"
author: "@phosphenq"
---

# AI That Codes While You Sleep

## Summary
The article packages loop engineering as six pieces plus a question: state, automations, worktrees, skills, connectors, sub-agents, and a verifier that proves completion. It is a practical checklist for turning agentic coding from a one-off command into a scheduled, bounded, reviewable workflow.

## Core Concepts
- [[concepts/Loop-Engineering]] -- the design discipline behind recurring, self-checking agent work.
- [[concepts/State-Externalizing-Harnesses]] -- STATUS.md and related files let the next run inherit state without relying on chat memory.
- [[concepts/Overnight-Goal-Runs]] -- scheduled or goal-driven runs do work while the human is away.
- [[concepts/Maker-Checker-Split]] -- separate builder and reviewer agents keep generation and verification apart.
- [[concepts/Stop-Condition]] -- loops need explicit brakes before they are left unattended.

## Key Insights
- State is the only thing the next run inherits, so it must be written deliberately in files the loop reads first and writes last.
- Automations are what separate a loop from something you ran once.
- Worktrees are the practical unit of isolation for parallel coding agents.
- Skills encode intent once on the outside so every run does not rediscover the same rules.
- Brakes such as iteration caps, budget caps, stuck detectors, and protected files must be installed before unattended runs.

## Open Questions
- How should [[concepts/State-Externalizing-Harnesses]] be standardized across Claude Code, Codex, and other coding agents?
- What level of [[concepts/Maker-Checker-Split]] is enough before allowing overnight work?
- How can [[concepts/Stop-Condition]] include comprehension debt, not only test status?

## Source
[[raw-notes/loop-engineering-build-an-ai-that-codes-while-you-sleep]]
