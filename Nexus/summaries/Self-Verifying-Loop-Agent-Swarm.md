---
type: article
title: "The Self-Verifying Loop: 300 agents, 4,000 steps, 5 live data feeds"
description: "A verify-then-retry loop that catches hallucination in agent swarms: Opus 4.8 plans and verifies, Kimi K2.6 swarm executes, loop runs until clean."
resource: "https://x.com/0xRicker/status/2067584599509651652"
timestamp: 2026-06-18
tags:
  - agent-swarms
  - verification
  - hallucination-prevention
  - kimik2.6
  - self-verifying-loop
---

## Synthesis

The author built a research system where a swarm of 300 parallel agents produces a research-grade report on 100 EV-market companies, with every figure traced to a live source. The key innovation: a self-verifying loop that refuses to stop while anything is wrong.

The system has four stages running in a cycle:
1. **Plan** (Opus 4.8): plans the work and defines the verification checklist
2. **Execute** (Kimi K2.6 swarm): 300 parallel agents execute research tasks
3. **Verify** (Opus 4.8): reads every agent's output back against the live source, rejects anything that fails
4. **Requeue**: rejected tasks go back into the queue with rejection reasons

On the first pass, Opus rejected 12 of 100 companies: revenue figures that didn't match the cited feed, a citation that didn't resolve, an empty margin field. Second pass: 3 still failed. Third pass: zero. The loop stopped on its own.

The five live feeds (Binance, Yahoo Finance, World Bank, IMF, live stock market) make verification strict rather than vague. Opus isn't asking the model if it feels confident — it's checking the claimed number against the actual feed.

The strategic insight: while closed labs ship single-agent chatbots, an open Chinese lab (DeepSeek, valued at $20B) shipped Kimi K2.6, the most-used LLM in the world, which is strongest where verification matters most: finance, academic research, and traceability.

## Key Insights

- "A swarm gives you speed. A loop gives you speed you can actually trust." The difference is the verify step.
- More agents usually means more confident nonsense. Volume scales the output and the error count at the same rate.
- The verification checklist is the most important part of the whole prompt — it's what the verify stage uses to reject bad work.
- Raw swarms ship errors and call it done. Self-verifying loops catch them automatically without human auditing.
- The five live feeds make verification strict (check against actual data) rather than vague (ask the model if it feels confident).

## Questions

- How does this self-verifying loop pattern relate to [[Agent-Loop]] architecture?
- Can the verify-then-retry pattern be generalized beyond research to other domains?
- What's the cost/benefit trade-off of multiple verification passes vs. single-pass with higher-quality agents?
