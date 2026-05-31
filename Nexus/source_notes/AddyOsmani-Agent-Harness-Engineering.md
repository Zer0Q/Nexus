---
title: "Agent Harness Engineering"
source: "https://x.com/addyosmani/status/2053231239721885918"
author: "@addyosmani"
published: 2026-05-09
type: source-note
---

# Agent Harness Engineering

## Summary

A deep dive into harness engineering — the discipline of building and refining the scaffolding around AI models. Core thesis: "A decent model with a great harness consistently beats a great model with a bad harness." A harness includes system prompts, tools, MCP servers, sandboxes, orchestration logic, hooks, and observability. The most vital habit is the "ratchet" — treating every agent mistake as a permanent signal that becomes a rule. Key harness components: filesystem + Git for durable state, bash for general-purpose tooling, sandboxes for safety, memory + search for continual learning, context management techniques (compaction, offloading, progressive disclosure), hooks as enforcement layer, and long-horizon execution patterns (loops, planning, splits).

## Core Concepts

- [[LLM-Harness]] — Everything around the model: prompts, tools, context policies, hooks, sandboxes, subagents, feedback loops
- Harness-Ratchet-Pattern — Every agent mistake becomes a permanent rule; every system prompt line traces to a historical failure
- Context-Rot-Management — Three techniques: compaction, tool-call offloading, progressive disclosure
- Long-Horizon-Execution — Loops (intercept exit), planning (decompose to steps), splits (separate generation/evaluation)
- Hook-Based-Enforcement — Deterministic execution at specific lifecycles: before tool call, after file edit, before commit
- Harness-as-a-Service — Industry shifting from LLM APIs (completions) to Harness APIs (runtime)

## Key Insights

- "If you're not the model, you're the harness" — Trivedy's core definition
- The gap between what models can theoretically do and what you actually see is largely a harness gap
- Ten highly focused tools outperform fifty overlapping ones
- As models improve, harness needs shift rather than disappear — new failure modes emerge at higher ceilings
- Top coding agents look more like each other than their underlying models do

## Open Questions

- How do harness patterns converge across different model providers?
- What does self-healing harness look like (agents analyzing their own traces)?
- How does the training loop feedback between harness design and model post-training evolve?
