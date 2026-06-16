---
title: Top AI Papers of the Week (June 7, 2026)
author: '@dair_ai'
published: '2026-06-07'
type: article
resource: https://x.com/dair_ai/status/2063644231030214958
timestamp: '2026-06-07T00:00:00Z'
description: 'Weekly roundup of 10 AI papers: self-revising discovery systems using
  category theory for regime changes, disentangling agent self-evolution into harness-upd...'
tags:
- summaries
---


# Top AI Papers of the Week (June 7)

## Summary
Weekly roundup of 10 AI papers: self-revising discovery systems using category theory for regime changes, disentangling agent self-evolution into harness-updating vs harness-benefit, LEAP solving all 12 Putnam problems via agentic Lean verification, Effective Feedback Compute (EFC) as the true scaling coordinate for harnesses, AutoLab benchmarking ultra long-horizon agent persistence, AdaCoM as external trainable context management, latent prediction theory showing exponential data efficiency gaps, a primer on post-training reasoning data, state-externalizing harnesses for search agents, and SIMAS showing diminishing returns on agent count.

## Core Concepts
- [[concepts/Self-Revising-Discovery]] -- scientific discovery as changing the representational regime itself, not just searching within a fixed space; uses category theory to type evidence/artifacts/operations/verifiers and accepts revisions only when they reduce description length (6.4% acceptance rate: 25/388 proposals)
- [[concepts/Harness-Updating-vs-Benefit]] -- agent self-evolution splits into two abilities: harness-updating (writing edits to memory/tools/prompts, flat across model tiers) and harness-benefit (exploiting those edits, non-monotonic with peak at mid-tier models); cheap evolver + capable solver is the optimal design
- [[concepts/LEAP]] -- agentic scaffold wrapping a general LLM in Lean compiler verification, decomposing proofs into subgoals with informal blueprints; solves all 12 Putnam 2025 problems and lifts Lean-IMO-Bench from <10% to 70% one-shot formal solve rate without math-specific training
- [[concepts/Effective-Feedback-Compute]] -- trace-level scaling coordinate that credits feedback only when informative, valid, non-redundant, and retained; normalized by task demand achieves R-squared of 0.99 vs. 0.33-0.42 for raw tokens/tool calls; improving feedback quality raises success from 0.27 to 0.90 at fixed budget
- AutoLab -- benchmark of 36 ultra long-horizon closed-loop optimization tasks across system optimization, puzzles, model development, CUDA kernels; persistence in iterative refinement predicts final performance better than initial solution quality; most frontier models terminate prematurely or burn budget
- [[concepts/AdaCoM]] -- external context manager trained with RL to edit a frozen agent's working context (keep/compress/drop); transfers across similar agents, improving web search and deep research by preserving constraints while pruning stale content
- [[concepts/Latent-Prediction-Learning]] -- predicting internal representations (JEPA/data2vec style) requires samples constant in tree depth L, while token-based learning needs samples exponential in L; latent targets expose compositional structure directly, providing theoretical foundation for world-model training efficiency
- [[concepts/State-Externalizing-Harnesses]] -- offloading routine bookkeeping from agent policy to environment-side working memory (candidate pools, curated sets, evidence links, verification records); Harness-1 (20B) reaches 0.730 curated recall across 8 benchmarks, beating open-source baselines by 11.4 points

## Key Insights
- The theme across all 10 papers is that system design (harnesses, scaffolds, verification loops) matters more than raw model scale for agent capability
- LEAP proves that a well-built harness around a general model can match dedicated frontier math models without any domain-specific training
- EFC reframes harness engineering as a feedback-quality problem: quality beats quantity at fixed budget (0.27 -> 0.90 success rate)
- Self-evolution research shows paying for frontier models on the evolver side buys almost nothing; the budget should go to the solver
- AutoLab reveals that time-awareness and sustained iteration, not single-shot capability, separates agents on multi-hour tasks
- AdaCoM treats context management as a separate, trainable, transferable module -- decoupling it from the agent itself
- Latent prediction theory provides a principled argument for self-supervised objectives that predict abstractions instead of tokens as scaling laws press against data limits
- SIMAS shows performance does not scale monotonically with agent count; coordination overhead eventually degrades results

## Open Questions
- How does the category-theoretic framework in Self-Revising-Discovery scale beyond the two tested instantiations (protein-mechanics, knowledge-computation graphs)?
- Can EFC be measured in real-time during agent runs, or does it require oracle access to feedback quality?
- Does the non-monotonic benefit curve in harness-benefit imply an optimal "sweet spot" model tier for specific task domains?

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/Context-Engineering]]
- [[concepts/Scaling-Laws]]
- [[concepts/RLVR]]
- [[concepts/World-Models]]
- [[summaries/DAIR-Top-AI-Papers-of-the-Week]]
- **Raw note:** [[raw-notes/top-ai-papers-of-the-week-june-7]]
- **Original URL:** https://x.com/dair_ai/status/2063644231030214958
