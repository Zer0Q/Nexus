---
title: Post by @_avichawla on X
author: '@_avichawla'
published: '2026-04-28'
type: article
resource: https://x.com/_avichawla/status/2063210446686146750
timestamp: '2026-04-28T00:00:00Z'
description: Avi Chawla lists 15 fine-tuning techniques ranked by what he'd learn
  if starting fresh, spanning parameter-efficient methods (LoRA, QLoRA, BitFit), prompt-ba...
tags:
- summaries
---


# Top 15 Fine-Tuning Techniques

## Summary
Avi Chawla lists 15 fine-tuning techniques ranked by what he'd learn if starting fresh, spanning parameter-efficient methods (LoRA, QLoRA, BitFit), prompt-based approaches (prefix tuning, P-tuning, soft prompts), and alignment methods (RLHF, RLAIF, DPO, GRPO, RLVR). The post highlights the RULER approach from OpenPipe's ART framework as the solution for non-verifiable tasks where hand-written reward functions are brittle and expensive to maintain.

## Core Concepts
- [[concepts/LoRA]] -- Low-Rank Adaptation, freezes base weights and trains two low-rank matrices as the update, reducing fine-tuning params by 95-99%
- [[concepts/QLoRA]] -- LoRA applied to a 4-bit quantized base model, combining parameter efficiency with memory efficiency
- Prefix-Tuning -- prepends trainable vectors to keys and values at every layer while keeping base weights frozen
- Adapter-Tuning -- inserts small trainable modules between transformer layers instead of updating the full model
- Instruction-Tuning -- supervised tuning on (instruction, response) pairs so the model follows directions rather than continuing text
- P-Tuning -- optimizes continuous prompt embeddings through a small encoder, mainly for NLU tasks where discrete prompts are unstable
- BitFit -- trains only bias terms (~0.08% of params), still rivals full fine-tuning on small-to-medium datasets
- Soft-Prompts -- steers a frozen model with learned vectors instead of handcrafted tokens
- Multi-Task-Fine-Tuning -- trains on several tasks simultaneously so one model generalizes and shares representations
- Federated-Fine-Tuning -- tunes across decentralized clients sharing only weight updates, never raw data

## Key Insights
- GRPO needs exactly one scalar reward per response; RLVR produces that for free on math/code via checkers/compilers
- Tasks like RAG answers, support replies, or summaries have no gold label — the fallback is hand-written reward functions scoring faithfulness, hallucination, completeness
- Hand-written reward functions take days to calibrate, reward wrong behavior when weights are off, and break when you add tools or edit the system prompt
- RULER (in OpenPipe's ART, open-source) passes N sampled trajectories to a judge LLM, which ranks them relative to each other against the agent's system prompt
- Relative ranking is more stable than absolute scoring, and GRPO normalizes within the group anyway, so rankings feed directly into the pipeline
- ART repo: https://github.com/OpenPipe/ART

## Open Questions
- How does BitFit compare to [[concepts/LoRA]] in practice for modern LLMs beyond small-to-medium datasets?
- Is Federated-Fine-Tuning practically viable for LLMs given the communication overhead of sharing weight updates?

## Source
- **Raw note:** [[raw-notes/post-by-avichawla-on-x]]
- **Original URL:** https://x.com/_avichawla/status/2063210446686146750
