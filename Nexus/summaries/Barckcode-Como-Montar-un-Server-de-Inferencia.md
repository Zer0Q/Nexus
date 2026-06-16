---
title: Cómo montar un server de inferencia para servir modelos de IA | My Blog
author: '@barckcode'
published: '2026-04-24'
type: article
resource: https://helmcode.com/posts/server-de-ia
timestamp: '2026-04-24T00:00:00Z'
description: Barckcode documents the four-layer architecture of NaN, a community-run
  inference server providing unlimited token access to local AI models. The stack
  uses ...
tags:
- summaries
---


# Cómo montar un server de inferencia para servir modelos de IA

## Summary
Barckcode documents the four-layer architecture of NaN, a community-run inference server providing unlimited token access to local AI models. The stack uses vLLM for model serving with speculative decoding via MTP (2x throughput boost, 80-92% acceptance rate), LiteLLM as an API gateway with per-key rate limits but no token caps, and Prometheus/Grafana for monitoring. The post emphasizes zero data retention — no input/output logging, no training — and VPN-only access to admin panels.

## Core Concepts
- [[concepts/Local-Inference-Server]] -- self-hosted GPU infrastructure serving open-weight models via OpenAI-compatible API, eliminating token limits and vendor lock-in
- [[concepts/LiteLLM-API-Gateway]] -- unified API layer that serves multiple models under a single endpoint with authentication, rate limiting, and usage metrics
- [[concepts/Speculative-Decoding]] -- technique that predicts extra tokens per generation step; NaN uses MTP (Multi-Token Prediction) built into Qwen3.6 for ~2x throughput with 80-92% acceptance rate
- [[concepts/Model-Serving]] -- the layer between models and APIs; vLLM handles request parallelization, memory management, and inference optimization
- [[concepts/Local-AI-Privacy]] -- zero data retention policy where no inputs or outputs are logged or used for training, unlike closed providers

## Key Insights
- NaN community members burn 300M+ tokens daily without hitting limits — the constraint that private providers impose
- vLLM configuration for Qwen3.6-35B-A3B: `--max-model-len 131072`, `--reasoning-parser qwen3`, `--mm-encoder-attn-backend TORCH_SDPA`, `--speculative-config '{"method":"mtp","num_speculative_tokens": 2}'`
- LiteLLM rate limits: 100 RPM, 5 parallel requests max per API key — prevents single users from monopolizing the GPU
- Hardware uses Blackwell GPUs with `nvidia-driver-570-open` and `cuda-toolkit`; only the LLM loads in vRAM, other models run on CPU/RAM
- Monitoring stack: Prometheus for metrics, Grafana for dashboards/alerts, LiteLLM built-in metrics for tokens/requests/models
- Security layers: Cloudflare (SSL + tunnels), VPN for all admin panels, basic Linux hardening — only the inference endpoint is exposed to the internet
- Models are rotated every 3 months via community voting

## Open Questions
- How does [[concepts/Local-Inference-Server]] economics scale when a community needs to add more GPUs to handle peak concurrent load?
- What happens to [[concepts/Speculative-Decoding]] acceptance rates when serving multiple model families through the same vLLM instance?
- Can [[concepts/LiteLLM-API-Gateway]] handle fair scheduling when some users run long agent loops vs short one-off queries?

## Source
- **Raw note:** [[raw-notes/como-montar-un-server-de-inferencia-para-servir-modelos-de-ia-my]]
- **Original URL:** https://helmcode.com/posts/server-de-ia
