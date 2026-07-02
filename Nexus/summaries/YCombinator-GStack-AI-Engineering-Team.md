---
type: Article
title: "How to Make Claude Code Your AI Engineering Team"
description: "Garry Tan demonstrates GStack as a skills-based operating system for product thinking, adversarial review, design, QA, and parallel AI engineering."
resource: "https://www.youtube.com/watch?v=wkv2ifxPpF8"
tags: [gstack, ai-engineering, claude-code, software-factory]
timestamp: "2026-06-23T00:00:00Z"
author: "Y Combinator"
---

# GStack as an AI Engineering Team

## Summary
GStack turns Claude Code, Codex, and browser tooling into a coordinated product team with skills for office hours, planning, adversarial review, design exploration, implementation, QA, and shipping. The core claim is that the model is already strong enough for much of the work; the leverage comes from structured roles, review loops, browser automation, and parallel worktrees.

## Core Concepts
- [[concepts/GStack-Software-Factory]] -- a skills-based software factory that maps product, design, engineering, and QA roles onto agent workflows.
- [[tools/Claude-Code]] -- the coding agent surface used as the main execution environment for GStack skills.
- [[concepts/Multi-Agent-Development]] -- multiple agent sessions can run parallel branches and PRs while the human manages direction and acceptance.
- [[concepts/Adversarial-Model-Spiral]] -- adversarial review improves plans by finding privacy, 2FA, failure-handling, and feasibility gaps before coding.
- [[concepts/Visual-to-Code-Generation]] -- design shotgun workflows generate multiple UI directions before implementation.

## Key Insights
- GStack's Office Hours skill encodes YC-style product pressure testing before any code is written, forcing evidence, wedge, market, and feasibility questions.
- The demo shows an idea mutating from a narrow Gmail 1099 finder into a browser-assisted tax document workflow because the skill challenges assumptions.
- Parallel agents raise throughput only when review, QA, browser testing, and shipping gates also scale.
- GStack's browser tools replace slow browser MCP interactions with a Playwright CLI so agents can inspect screenshots, click, fill forms, and evaluate UI bugs.
- The bottleneck shifts from typing code to choosing the right work, reviewing many PRs, and keeping supply-chain risk under control.

## Open Questions
- How much of [[concepts/GStack-Software-Factory]] is transferable to non-startup or regulated software contexts?
- What metrics distinguish useful multi-agent throughput from merely increasing review queue size?
- Where should [[concepts/Maker-Checker-Split]] sit in a GStack-like workflow: plan, design, code, QA, or all of them?

## Source
[[raw-notes/how-to-make-claude-code-your-ai-engineering-team]]
