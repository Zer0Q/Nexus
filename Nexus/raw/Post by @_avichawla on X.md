---
title: "Post by @_avichawla on X"
source: "https://x.com/_avichawla/status/2063210446686146750"
author:
  - "[[@_avichawla]]"
published: 2026-04-28
created: 2026-06-08
description: "I have been fine-tuning LLMs for over 2 years now! Here are the top 15 techniques I'd learn if I were to fine-tune them: Bookmark this. 1"
tags:
  - "clippings"
summary:
---
I have been fine-tuning LLMs for over 2 years now!

Here are the top 15 techniques I'd learn if I were to fine-tune them:

Bookmark this.

1\. LoRA

\> Freezes the base weights and trains two low-rank matrices as the update, resulting in ~95-99% fewer params to fine-tune.

2\. QLoRA

\> LoRA on top of a 4-bit quantized base model.

3\. Prefix tuning

\> Prepends trainable vectors to keys and values at every layer, weights frozen.

4\. Adapter tuning

\> Inserts small trainable modules between transformer layers.

5\. Instruction tuning

\> Supervised tuning on (instruction, response) pairs so the model follows directions instead of just continuing text.

6\. P-tuning

\> Optimizes continuous prompt embeddings through a small encoder, mainly for NLU tasks where discrete prompts are unstable.

7\. BitFit

\> Trains only the bias terms, ~0.08% of params, and still rivals full fine-tuning on small-to-medium datasets.

8\. Soft prompts

\> Steer a frozen model with learned vectors instead of handcrafted tokens.

9\. RLHF

\> Train a reward model on human preference rankings, then PPO against it. The pipeline behind the first ChatGPT.

10\. RLAIF

\> Swaps the human labeler for an LLM judging. RLHF-level quality at a fraction of the cost.

11\. DPO (Direct Preference Optimization)

\> Skips the reward model and optimizes preference pairs directly with a classification-style loss. Simpler than PPO.

12\. GRPO (Group Relative Policy Optimization)

\> Samples a group of responses per prompt and normalizes their rewards within the group. DeepSeek R1 ran on it.

13\. RLVR (Reinforcement Learning with Verifiable Rewards)

\> Replaces the learned reward model with a checker or compiler returning verifiable scores. The free signal behind R1's math and code.

14\. Multi-task fine-tuning

\> Trains on several tasks at once, so one model generalizes and shares representations instead of overfitting to one objective.

15\. Federated fine-tuning

\> Tunes across decentralized clients that share only weight updates, never raw data. For when data can't leave the device.

GRPO needs exactly one scalar reward per response. RLVR (13) produces that for free on math and code by running the answer through a checker or compiler.

But tasks like a RAG answer, a support reply, or a summary have no gold label to match against.

The usual fallback is a hand-written reward function scoring faithfulness, hallucination, and completeness.

It takes days to calibrate, rewards the wrong behavior when the weights are off, and breaks every time you add a tool or edit the system prompt.

RULER, implemented in OpenPipe's ART (open-source), solves this.

During training, it passes the N sampled trajectories to a judge LLM, which ranks them relative to each other against the agent's system prompt and returns the scores.

Relative ranking is more stable than absolute scoring, and GRPO normalizes within the group anyway, so the rankings feed straight into the pipeline like with RLVR.

Here's the GitHub Repo: https://github.com/OpenPipe/ART

(don't forget to star it ⭐ )

I wrote a full breakdown recently on how exactly this works, with the training loop and code.

Read it below.

> **Avi Chawla @\_avichawla** · 2026-04-28
> 
> ![Imatge de portada de l'article](https://pbs.twimg.com/media/HG-kPGeaAAAQgjY?format=jpg&name=large)