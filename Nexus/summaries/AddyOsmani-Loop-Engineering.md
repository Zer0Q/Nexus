---
title: "Loop Engineering"
source: "https://x.com/addyosmani/status/2064127981161959567"
author: "@addyosmani"
published: "2026-06-09"
type: article
---

# Loop Engineering

## Summary
Loop engineering replaces the human as the person prompting agents — you design the system that does it instead. A loop is a recursive goal where you define a purpose and the AI iterates until complete, built on five primitives: automations (scheduled discovery), worktrees (parallel isolation), skills (project knowledge), plugins/connectors (external tools), and sub-agents (maker-checker split), plus persistent memory on disk. Both Claude Code and Codex now ship all five primitives natively, making loop design tool-agnostic. The verification piece is the most critical — without it, a loop is just a token bonfire.

## Core Concepts
- [[concepts/Loop-Engineering]] — designing systems that prompt agents instead of humans doing it manually; the abstraction layer above harness engineering
- [[concepts/Agent-Loop]] — a recurring, self-verifying agent process with a trigger, tools, verification, repeat condition, and stop rule
- [[concepts/Comprehension-Debt]] — the gap between what code exists and what you actually understand; grows faster when loops ship code you didn't write
- [[concepts/Cognitive-Surrender]] — accepting loop output without judgment; the loop is the cure when designed with judgment, the accelerant when used to avoid thinking

## Key Insights
- Boris Cherny (Anthropic): "I don't prompt Claude anymore. I have loops running that prompt Claude and figure out what to do. My job is to write loops."
- Peter Steinberger: "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."
- A year ago, loops meant writing bash scripts; now the primitives ship inside Claude Code and Codex natively
- The five pieces map almost identically across both tools — once you notice the shape, you stop arguing about which tool
- Sub-agents are the most useful structural innovation: the model that wrote the code is "way too nice grading its own homework"
- /goal keeps iterating until a verifiable stopping condition holds, with a separate model checking completion — the maker-checker split applied to the stop condition itself
- Skills prevent the loop from re-deriving your project from zero every cycle; without them, intent debt compounds
- The loop "changes the work, it does not delete you from it" — three problems get sharper: verification, comprehension debt, cognitive surrender
- Token costs vary wildly depending on whether you're token-rich or token-poor; slop concerns are valid
- Two people can build the exact same loop and get opposite results — one uses it to move faster on work they understand, the other to avoid understanding entirely

## Open Questions
- How do loops handle edge cases where verification is inherently subjective (UI design, UX quality)?
- What does a "loop budget" look like — token caps, max iterations, and when to escalate to a human?
- Can [[concepts/Loop-Engineering]] converge with [[concepts/Agentic-SDLC]] into a unified framework?

## Source
- **Raw note:** [[concepts/Loop-Engineering]]
- **Original URL:** https://x.com/addyosmani/status/2064127981161959567
