---
type: Article
title: "The Hermes Sensei Loop"
description: "A research-agent loop design using champion prompts, holdout evaluation, and feedback sweeps to improve Hermes cron output quality."
resource: "https://x.com/0xJeff/status/2069008589721932251"
tags: [hermes-agent, research-agents, prompt-improvement]
timestamp: "2026-06-23T00:00:00Z"
author: "@0xJeff"
---

# Hermes Sensei Loop

## Summary
The article adapts loop engineering from coding agents to research agents, specifically Hermes cron workflows. Its main pattern is a champion loop: keep the current best prompt, test challengers against held-out examples, and only promote changes that improve unseen outputs without breaking must-pass rules.

## Core Concepts
- [[tools/Hermes-Agent]] -- the research-agent runtime being improved through feedback loops.
- [[concepts/Champion-Loop]] -- a prompt improvement loop that promotes challengers only after beating the current champion on holdout data.
- [[concepts/Feedback-Sweep-Loop]] -- a collector loop that turns user complaints into ranked prompt improvement tasks.
- [[concepts/Self-Improvement-Loop]] -- the agent improves its own recurring outputs through structured feedback and evaluation.
- [[concepts/AI-Slop-Quality-Filtering]] -- adversarial evaluation reduces sycophantic, consensus-heavy, or generic research output.

## Key Insights
- Research loops need adversarial pressure because agreeable outputs can feel useful while avoiding thesis stress tests.
- Champion promotion on a working set overfits; the holdout set is the immune system that catches regressions.
- Feedback sweeps make vague user dissatisfaction actionable by grouping complaints by workflow and frequency.
- The same loop pattern can improve Equities Daily, Top 7 Synthesis, and Alpha Triage workflows if each has scored examples.
- Structured feedback from the human improves both the agent and the human's ability to manage the agent.

## Open Questions
- What scoring rubric makes [[concepts/Champion-Loop]] reliable for qualitative research outputs?
- How large must a holdout set be before promotion decisions are meaningful?
- Can [[concepts/Feedback-Sweep-Loop]] distinguish recurring quality issues from one-off user preference shifts?

## Source
[[raw-notes/the-hermes-sensei-loop]]
