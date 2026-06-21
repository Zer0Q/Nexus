---
type: concept
title: "Capability-Access-Gap"
description: "The gap between a model's peak benchmark capability and the fraction of that capability users actually receive, caused by safety filters, routing, and refusals."
resource: "https://www.deeplearning.ai/the-batch/issue-358"
timestamp: 2026-06-19
tags:
  - benchmarking
  - model-access
  - safety-filters
---

## Definition

The capability-access gap measures the difference between a model's peak performance (on benchmarks with safeguards bypassed) and the performance users actually experience in practice (with safety classifiers, routing, and refusals active).

## Origin

Identified in analysis of [[Claude-Fable-5]] by Andrew Ng's DeepLearning.AI The Batch. Independent evaluators found Claude Fable 5 routed ~9% of prompts to Claude Opus 4.8 or refused them outright, making direct measurement of its capabilities impossible.

## Key Insight

Benchmarks typically ask "how capable is a model?" but safety-gated models force a harder question: "how much of that capability do users actually receive?" The gap between peak score and accessible score is the new measurement frontier.

## Related Concepts

- [[Claude-Fable-5]]
- [[Benchmark-Transparency]]
- [[Model-Routing]]
- [[Accessible-Capability]]
