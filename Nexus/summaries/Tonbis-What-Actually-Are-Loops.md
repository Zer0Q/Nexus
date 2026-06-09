---
title: "What Actually ARE Loops? (And Do I Need Them?)"
source: "https://x.com/tonbistudio/status/2063861151524643291"
author: "@tonbistudio"
published: "2026-06-08"
type: article
---

# What Actually ARE Loops?

## Summary
Two statements about "loops" went viral from Boris Cherny (Anthropic) and Peter Steinberger (openclaw), but the term was used so loosely that most people didn't know what they meant. A loop is a recurring, tool-using, self-verifying agent process: something kicks it off, the agent does work, checks its own work against a signal, then either runs again or stops and calls a human. The article contrasts two approaches — Boris sees loops as the next programming interface (Claude + cron + recurring prompt + tools + memory), while Peter's framing is "remove yourself from the feedback path" — every time you do repetitive observation for the agent, build a tool so the agent does it alone. Loops only pay off when work repeats and the agent can verify its own answer; for one-off or exploratory work, they're the wrong tool.

## Core Concepts
- [[concepts/Loop-Engineering]] — designing systems that prompt agents instead of humans doing it manually; the abstraction layer above harness engineering
- [[concepts/Agent-Loop]] — a recurring, self-verifying agent process with trigger, context, tools, verification, repeat condition, and stop rule
- [[concepts/Comprehension-Debt]] — gap between what code exists and what you understand; grows when loops ship code you didn't write
- [[concepts/Cognitive-Surrender]] — accepting loop output without judgment; the loop is the cure when designed with judgment, the accelerant when used to avoid thinking

## Key Insights
- Boris Cherny's abstraction ladder: punch cards -> assembly -> Python -> autocomplete -> IDE -> Claude Code -> 5-10 Claudes in parallel -> loops. Each step abstracts away manual prompting
- Peter Steinberger's method: "Every time you catch yourself doing repetitive observation, judgment, routing, or verification for the agent, build a tool that hands that job to the agent"
- The signal for finding loop opportunities: "Listen when you're annoyed. Annoyance means you're doing something a machine should be doing"
- Robo Bun (Jarred Sumner/Bun): production loop with proof gates — GitHub issue -> reproduce bug -> failing test -> fix -> PR with test that fails on old version and passes on fix -> review bots critique -> human merges
- Hill climbing: target + metric + ability to change things + ability to measure = autonomous improvement loop
- Boris's concrete loops: PR babysitter (CI failures, merge conflicts), CI health (flaky tests), feedback clustering (Twitter every 30 min), idea mining (200 Claudes reading Twitter/GitHub/Slack, ~20% good ideas)
- Peter's loops: Issue/PR reaper (reads vision.md, decides if request fits project direction), Maintainer report (Discord + issues + PRs -> top 5 complaints -> dispatch agents), Mantis (video proof loop: agent records bug, fixes it, records fix, watches video to verify), Auto Review (Codex calls Codex with fresh context before commit)
- A mature loop turns repeated steps into scripts rather than calling the model for the same operation a thousand times
- Vision.md (project constitution) and agents.md (invariants) are the policy layers that prevent loops from optimizing toward random noise
- "If I weren't reviewing the code myself or if I relied entirely on automated loops to fix it, my product's quality would suffer"
- Two people can build the exact same loop and get opposite results — one uses it to move faster on work they understand, the other to avoid understanding entirely

## Open Questions
- How do loops handle edge cases where verification is inherently subjective (UI design, UX quality)?
- What does a "loop budget" look like — token caps, max iterations, and when to escalate to a human?
- Can [[concepts/Loop-Engineering]] converge with [[concepts/Agentic-SDLC]] into a unified framework?

## Source
- **Raw note:** [[raw-notes/what-actually-are-loops-and-do-i-need-them]]
- **Original URL:** https://x.com/tonbistudio/status/2063861151524643291
