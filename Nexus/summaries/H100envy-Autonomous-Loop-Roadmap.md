---
type: Article
title: "Loop Engineering: A Technical Roadmap for an Autonomous Loop"
description: "A technical checklist for building autonomous loops with deterministic checks, stateless iterations, narrow context, isolation, reward-hacking gates, and logs."
resource: "https://x.com/h100envy/status/2068987470960623783"
tags: [loop-engineering, autonomous-agents, verification]
timestamp: "2026-06-23T00:00:00Z"
author: "@h100envy"
---

# Autonomous Loop Roadmap

## Summary
This article gives the most mechanical version of loop engineering: build only tasks with an external machine check, prove one manual pass, run stateless iterations, feed narrow context, block reward hacking, store state on disk, isolate the worktree, and log every turn. Its central warning is that an unverified loop is not autonomy; it is an expensive random walk.

## Core Concepts
- [[concepts/Loop-Engineering]] -- designing the repeatable system that finds work, acts, checks, and repeats.
- [[concepts/Stateless-Agent-Loop]] -- each iteration starts fresh and reads state from disk instead of accumulating conversational context.
- [[concepts/Evidence-Validation]] -- stop conditions must be external, deterministic, idempotent checks rather than self-assessment.
- [[concepts/Reward-Hacking]] -- agents can make metrics pass by weakening tests or exploiting the check instead of solving the task.
- [[concepts/Read-Only-Vault-Safety]] -- isolation and read-only boundaries reduce blast radius for autonomous work.

## Key Insights
- A task should fail the loop filter if it cannot be judged by a deterministic, stable, independent check.
- Stateless iteration solves both quality and cost problems by avoiding context rot and quadratic context rereading.
- Context should be assembled from the current failure, changed files, and relevant paths under an explicit token budget.
- Reward hacking needs physical or deterministic gates, such as read-only tests or diff checks, not just prompt warnings.
- Observability is a safety feature: structured logs reveal runaway loops, repeated failures, reward hacking, and silent death.

## Open Questions
- Which [[concepts/Loop-Engineering]] tasks can rely on deterministic checks, and which still require human taste?
- How can [[concepts/Reward-Hacking]] be detected in non-code loops where there are no tests to protect?
- What is the right balance between stateless iteration and richer memory in long-running loops?

## Source
[[raw-notes/loop-engineering-a-technical-roadmap-for-an-autonomous-loop]]
