---
type: Article
title: "WTF Is a Loop? Part 2: The 15 Loops People Are Actually Running (and the Commands to Steal Them)"
description: "A catalog of real agent loops across code review, repository maintenance, email operations, quality streaks, adversarial review, and completion contracts."
resource: "https://x.com/mvanhorn/status/2068426104088748331"
tags: [agent-loops, loop-library, automation]
timestamp: "2026-06-23T00:00:00Z"
author: "@mvanhorn"
---

# Fifteen Agent Loops People Run

## Summary
The sequel classifies practical agent loops into goals, loops, and routines, then catalogs examples people are actually running: build-test-fix, verifier loops, repository maintenance, post-commit review, email operations, approval queues, production error sweeps, quality streaks, adversarial model review, and completion contracts. It treats real loops as operational patterns with commands, provenance, and failure controls rather than abstract autonomy claims.

## Core Concepts
- [[concepts/Loop-Engineering]] -- the shared discipline behind recurring, verified agent workflows.
- [[concepts/Goal-Driven-Agents]] -- goal loops run until a verifiable condition is true.
- [[concepts/Completion-Contract]] -- done must be defined before work starts, with evidence required for every claim.
- [[concepts/Maker-Checker-Split]] -- build-test-fix and adversarial review loops separate production from verification.
- [[concepts/Human-AI-Orchestration]] -- approval queues make the human review step explicit inside the loop.

## Key Insights
- Goal, loop, and routine are distinct: goal runs until a condition, loop repeats while present, routine runs on a schedule while absent.
- The most reliable coding loops pair a builder with a checker and a hard cap on iterations.
- Production loops are mostly triage systems: they separate actionable work from noise before asking an agent to fix anything.
- Human approval queues are still loops; the stop condition is a human decision rather than a test result.
- Completion contracts prevent agents from declaring "done" without evidence mapped to prewritten acceptance criteria.

## Open Questions
- Should this vault model [[concepts/Completion-Contract]] as a subtype of [[concepts/Stop-Condition]] or a separate workflow primitive?
- Which loop patterns in the catalog are reusable across domains outside software?
- How should [[concepts/Human-AI-Orchestration]] expose queue state so humans are not reintroduced as invisible bottlenecks?

## Source
[[raw-notes/wtf-is-a-loop-part-2-the-15-loops-people-are-actually-running-and-the-commands-to-steal-them]]
