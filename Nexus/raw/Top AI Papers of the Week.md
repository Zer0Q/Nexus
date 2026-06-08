---
title: "Top AI Papers of the Week"
source: "https://x.com/dair_ai/status/2063644231030214958"
author:
  - "[[@dair_ai]]"
published: 2026-06-07
created: 2026-06-08
description: "Welcome to The Top AI Papers of the Week (May 31 - June 7).1. Self-Revising Discovery SystemsFrom MIT, this paper argues that genuine scient..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HKJJ_mHXoAAwKog?format=jpg&name=large)

Welcome to The Top AI Papers of the Week (May 31 - June 7).

## 1\. Self-Revising Discovery Systems

![Imatge](https://pbs.twimg.com/media/HKJKBBiXIAALDL6?format=jpg&name=large)

From MIT, this paper argues that genuine scientific discovery is not answer generation but a change in the search space itself, and that an AI scientist must perceive that shift without being told. It develops a category-theoretic framework in which evidence, artifacts, operations, and verifiers are typed, and discovery is defined as a principled revision of that representational regime rather than more search within a fixed one.

- **Discovery means changing the regime:** The system is built to detect when the representational regime should change and to revise it autonomously. That reframes an AI scientist from a faster searcher into something that can move the boundaries of the space it searches.
- **A typed, categorical foundation:** Evidence, artifacts, operations, and verifiers are formally typed. Old results are carried into the new regime by functorial transport, and what counts as genuine discovery is the residual content that transport alone cannot explain.
- **Description-length gates keep it honest:** Proposed revisions are accepted only when they reduce total description length, which separates real structural gains from mere added complexity. In one run, 388 proposals yield just 25 accepted revisions, a deliberately strict 6.4% rate.
- **Why it matters:** Two concrete instantiations, protein-mechanics modeling and a knowledge-computation graph with typed skills and validation checkpoints, show category theory serving as both a formal language and an engineering spec. It is a more principled blueprint for autonomous discovery than search-only AI scientists.

[Paper](https://arxiv.org/abs/2606.01444) | [Tweet](https://x.com/ProfBuehlerMIT/status/2062865983459475830)

## 2\. Disentangling Agent Self-Evolution

![Imatge](https://pbs.twimg.com/media/HKJKCfgWYAEp-8d?format=png&name=large)

This paper asks a question every agent builder eventually hits: if an agent rewrites its own harness, does a stronger model make a better self-evolving agent? The answer is no, and the reason is that "self-evolution" is actually two separate abilities that scale very differently. The work separates harness-updating, where an evolver model writes edits to memory, tools, prompts, and skills, from harness-benefit, where a solver model actually exploits those edits on the task.

- **Updating is flat across model tiers:** The quality of harness edits barely depends on model strength. Updates written by Qwen3.5-9B yield gains comparable to those from Claude Opus 4.6, so paying for a frontier model on the evolver side buys almost nothing.
- **Benefit is non-monotonic:** The ability to use a better harness follows a curve. Weak models gain little, mid-tier models benefit most, and the strongest models benefit less than mid-tier ones, often because they already solve the task without the scaffold.
- **Failure modes are concrete:** Weaker solvers either fail to activate the relevant harness component or follow its instructions inconsistently, which is why their gains stay small even when the edits themselves are good.
- **Why it matters:** The practical lever is to put a cheap model on the evolver and spend your capability budget on the solver. System design, not raw model scale, is doing most of the work in agent self-improvement.

[Paper](https://arxiv.org/abs/2605.30621) | [Tweet](https://x.com/omarsar0/status/2061460266186125703)

## 3\. LEAP

![Imatge](https://pbs.twimg.com/media/HKJKI4XWcAAcDnb?format=jpg&name=large)

New research from Google shows how far a custom agent harness can push a general-purpose model on formal mathematics. LEAP wraps a general LLM in an agentic scaffold that grounds every step in the Lean compiler and iterates against verifier feedback. Rather than fine-tuning a specialized prover, it leans on informal reasoning, instruction following, and self-refinement, then forces every formal step through a compiler check before moving on.

- **Decompose, then verify:** The scaffold takes the natural form of proof decomposition and verifier-guided refinement. The model breaks a hard theorem into subgoals, drafts an informal blueprint, and the Lean compiler checks each formal step, turning vague reasoning into machine-checkable proof.
- **Putnam solved in full:** On the 2025 Putnam Competition, LEAP solves all 12 problems, matching recent breakthroughs from dedicated frontier math models without any math-specific training of the base LLM.
- **Large jump on IMO-level proofs:** On Lean-IMO-Bench, LEAP lifts the one-shot formal solve rate of general-purpose LLMs from below 10% to 70%, surpassing the 48% set by a specialized, gold-medal-caliber IMO system.
- **Why it matters:** This is strong evidence that a well-built harness, not a bespoke model, can close the gap on one of the hardest reasoning domains. The leverage sits in the scaffold and the verifier loop around a general model.

[Paper](https://arxiv.org/abs/2606.03303) | [Tweet](https://x.com/omarsar0/status/2062187813626675567)

## 4\. Scaling Laws for Agent Harnesses

![Imatge](https://pbs.twimg.com/media/HKJKL-zWYAAxFBm?format=png&name=large)

Most harness tuning treats every token and tool call as if volume is what counts. This paper shows that it mostly does not, and introduces Effective Feedback Compute (EFC), a trace-level scaling coordinate that credits feedback only when it is informative, valid, non-redundant, and retained for later decisions, then normalizes by task demand.

- **Raw budget barely predicts success:** In controlled scaling, raw tokens and tool calls explain limited variation in outcomes, with R-squared of 0.33 and 0.42. The usual cost proxies are weak predictors of whether the agent actually succeeds.
- **Effective feedback nearly explains everything:** Oracle-EFC normalized by task demand reaches an R-squared of 0.99. Once you measure feedback that is genuinely useful and retained, the scaling behavior becomes almost fully predictable.
- **Quality beats quantity at fixed budget:** In matched-budget interventions, improving feedback quality raises success from 0.27 to 0.90 while raw cost and tool calls stay fixed. The win comes from better feedback, not more of it.
- **Why it matters:** Harness scaling is governed less by how much compute you spend than by how efficiently raw budget converts into durable, task-sufficient feedback. That reframes harness engineering as a feedback-quality problem and gives a coordinate to optimize against.

[Paper](https://arxiv.org/abs/2605.29682) | [Tweet](https://x.com/omarsar0/status/2060371848010019001)

## 5\. AutoLab

![Imatge](https://pbs.twimg.com/media/HKJKQFQXsAA5PF4?format=jpg&name=large)

Can frontier models actually grind on a hard engineering problem the way a good researcher does? AutoLab is a benchmark for ultra long-horizon, closed-loop optimization built to answer that. It contains 36 realistic, expert-curated tasks across four domains: system optimization, puzzle and challenge, model development, and CUDA kernel optimization. Each task hands the agent a correct but deliberately suboptimal baseline and asks it to improve within a strict wall-clock budget.

- **Persistence beats a strong start:** The dominant predictor of final performance is not the quality of the initial solution but the agent's persistence in iterative refinement. Models that keep probing and improving win, regardless of where they began.
- **Most models quit early:** While Claude Opus 4.6 shows strong long-horizon optimization, most frontier models, including several proprietary ones, either terminate prematurely or burn their budget with minimal progress.
- **Time awareness is the gap:** The results point to time-awareness and sustained iteration, not raw single-shot capability, as the missing ingredient for truly capable long-horizon agents.
- **Why it matters:** Day-one benchmarks reward clever first attempts, but real research and engineering reward stamina. AutoLab measures the thing that actually separates agents on multi-hour tasks, and the benchmark, harness, and task artifacts are open-sourced.

[Paper](https://arxiv.org/abs/2606.05080) | [Tweet](https://x.com/dair_ai/status/2062570078705688777)

## 6\. Reusable Context Engineering

![Imatge](https://pbs.twimg.com/media/HKJKSvOWcAAztnc?format=jpg&name=large)

Context bloat quietly kills long-horizon runs, and the usual fixes are baked into an agent's own prompt or weights, so they do not transfer. AdaCoM takes a different route: it trains a separate external model to manage the context of a frozen agent through flexible modification actions, optimized end-to-end with reinforcement learning. The agent never changes; only the context flowing into it does.

- **An external context manager:** A dedicated model edits the agent's working context, deciding what to keep, compress, or drop. Because it sits outside the agent, it can be reused as a drop-in component rather than re-engineered per backbone.
- **Trained with reinforcement learning:** The manager is optimized end-to-end against task outcomes, learning context-editing policies instead of relying on hand-written heuristics or fixed truncation rules.
- **Transfers across similar agents:** Transfer experiments show AdaCoM generalizes most effectively across agents of similar capability, pointing toward genuinely reusable context managers. It improves web search and deep research by preserving task constraints and progress while pruning stale content.
- **Why it matters:** Treating context management as a separate, trainable, transferable module decouples it from the agent itself. That is a cleaner abstraction than stuffing context logic into every prompt, and it fixes bloat from the outside without touching the underlying model.

[Paper](https://arxiv.org/abs/2605.30785) | [Tweet](https://x.com/dair_ai/status/2061455253325971789)

## 7\. Learn From Your Own Latents

![Imatge](https://pbs.twimg.com/media/HKJKUoFWwAAn8bw?format=jpg&name=large)

LLMs learn by predicting tokens, while world models like JEPA and data2vec learn by predicting their own internal representations. This paper provides a sample-complexity theory for why the second approach can be dramatically more data-efficient, using a tractable probabilistic context-free grammar as the analytical setting where compositional structure can be measured exactly.

- **Exponential gap in data efficiency:** Predicting your own latents requires a number of samples that is constant in the tree depth L, whereas supervised and token-based self-supervised learning need samples that grow exponentially in L. The advantage is structural, not incidental.
- **Why latents win:** Latent targets expose the compositional, hierarchical structure of the data directly, so the learner does not have to reconstruct it from surface tokens. That is the mechanism behind the data-efficiency gain.
- **Hierarchy may be implicit:** The analysis suggests that explicit hierarchical stacking, as in H-JEPA, can be largely redundant, because methods like data2vec already learn hierarchical structure implicitly.
- **Why it matters:** As token-prediction scaling laws press against data limits, this gives a principled argument for self-supervised objectives that predict abstractions instead of tokens. It is a theoretical foundation for why world-model-style training could beat brute-force next-token prediction on sample efficiency.

[Paper](https://arxiv.org/abs/2605.27734) | [Tweet](https://x.com/MatthieuWyart/status/2061317203857739846)

## 8\. A Primer on Post-Training Reasoning Data

This primer is the first to pull the scattered post-training reasoning-data literature into one place, synthesizing over 150 public studies and system reports that previously lived across dataset papers, RL write-ups, and lab reports. It organizes the field around four questions: what data objects exist, what makes them useful, how they are constructed, and how they scale. The key reframing is that a reasoning-data item is more than a prompt-response pair: it packages a problem or state, model behavior, judging feedback, and attribution metadata, with usefulness defined relative to the verifier and the rest of the corpus rather than in isolation.

[Paper](https://arxiv.org/abs/2606.02113) | [Tweet](https://x.com/dair_ai/status/2062189321697083768)

## 9\. State-Externalizing Harnesses

Harness-1 is a 20B search agent trained with reinforcement learning inside a stateful harness that offloads routine bookkeeping to the environment. The argument is that search agents are usually trained as policies over a growing transcript, forcing RL to optimize both genuine search decisions and recoverable state like which evidence is useful or which claims are checked. Harness-1 moves that state out of the policy and into an environment-side working memory of candidate pools, an importance-tagged curated set, compact evidence links, and verification records. The 20B agent reaches an average curated recall of 0.730 across eight retrieval benchmarks, beating open-source baselines by 11.4 points and matching or outperforming much larger frontier searchers, with stronger generalization on unseen domains.

[Paper](https://arxiv.org/abs/2606.02373) | [Tweet](https://x.com/dair_ai/status/2061825437693841651)

## 10\. Do More Agents Help?

This paper studies whether adding agents actually makes a single LLM-driven multi-agent system better, using a Sequential Iterative Multi-Agent System (SIMAS) framework. The finding is that performance does not scale monotonically with agent count but follows a pattern of diminishing returns, with degradation eventually driven by coordination overhead. Effective systems still require a capable base model, the optimal number of agents depends on the task type, and collective intelligence turns out to be a product of strategic interaction design rather than a guaranteed outcome of agent plurality. The takeaway for builders is to design the interaction, not just stack more agents.

[Paper](https://arxiv.org/abs/2606.00655) | [Tweet](https://x.com/omarsar0/status/2061826427461464405)