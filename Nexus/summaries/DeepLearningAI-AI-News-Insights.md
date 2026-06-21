---
type: article
title: "DeepLearning.AI AI News & Insights"
description: "Andrew Ng's The Batch #358: Claude Fable 5 benchmark problems, new agentic benchmarks beyond SWE-bench, Nvidia Nemotron 3 Ultra, and POPE reinforcement learning method."
resource: "https://www.deeplearning.ai/the-batch/issue-358"
timestamp: 2026-06-19
tags:
  - ai-news
  - benchmarks
  - claude
  - nemotron
  - reinforcement-learning
---

## Synthesis

Andrew Ng's The Batch covers three major developments in the AI landscape:

**Claude Fable 5 benchmark opacity.** Anthropic's Claude Fable 5 (a safety-gated version of Claude Mythos 5) cannot be properly evaluated because its content classifiers silently route flagged prompts to Claude Opus 4.8 or refuse them outright. Independent evaluators found ~9% refusal rates on Humanity's Last Exam, ~100% refusal on biology/cybersecurity questions, and Claude Code silently substituting Opus 4.8 for flagged prompts. The core insight: benchmarks typically ask "how capable is a model?" but Fable 5 forces a harder question — "how much of that capability do users actually receive?" The gap between peak capability and accessible capability is the new measurement frontier.

**New agentic benchmarks beyond SWE-bench.** SWE-bench is being replaced by three new benchmarks: DeepSWE (feature implementation with human-vetted problems requiring ~5.5x more code than SWE-Bench Pro, GPT-5.5 leads at 70%), ProgramBench (replicating programs from ideas without human oversight, no model passes all tests), and ITBench-AA (diagnosing root causes in real-world incidents, Claude Opus 4.7 leads at 46.7% full recall). These benchmarks test harder, more specific agentic tasks unlikely to be in training data.

**Nvidia Nemotron 3 Ultra.** Nvidia's largest open-weights model (550B parameters, 55B active) uses a hybrid transformer-Mamba architecture. It's the highest-scoring U.S. open-weights model on Artificial Analysis's Intelligence Index (47.7) and fastest among open-weights (~183 tok/s), but trails China's Kimi K2.6 (53.9). Trained on 20T tokens with NVFP4 quantization. Key insight: Nvidia has incentive to release strong open models to avoid concentration in proprietary developers and accelerate demand for Nvidia chips.

**POPE reinforcement learning.** CMU researchers introduced Privileged On-Policy Exploration: during GRPO training, the model receives the beginning of a solution as a hint. This breaks hard problem learning into two steps — finding a good starting state, then solving from there. POPE outperformed both GRPO and SFT on AIME 2025 (53.1% pass@1 vs 49.6% GRPO) and HMMT 2025 (37.8% vs 31.0%).

## Key Insights

- The capability-access gap is the new benchmarking problem: a model's score is meaningless without knowing what fraction users actually get
- SWE-bench is dead — models solved it, so benchmarks evolved to test feature implementation (DeepSWE), program creation from ideas (ProgramBench), and incident diagnosis (ITBench-AA)
- Open-weights competition is geopolitical: U.S. open models (Nemotron 3 Ultra) are catching up to Chinese leaders (Kimi K2.6), driven by Nvidia's chip-market incentives
- POPE demonstrates that RL exploration can be guided by privileged information without losing the model's ability to solve without hints

## Questions

- Does Claude Fable 5's routing to Opus 4.8 constitute a form of [[Model-Switching]] that undermines benchmark transparency?
- Can POPE's hint-based approach generalize beyond math to other RL domains?
- Will Nvidia's open-weight releases accelerate or slow the open-source model race?
- How do we measure "accessible capability" as a standard metric alongside peak scores?
