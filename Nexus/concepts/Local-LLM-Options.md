---
type: Concept
title: Local LLM Options
description: Options for running LLMs locally without cloud API dependencies. Includes
  Ollama, LM Studio, llama.cpp, and various model architectures optimized for local
  i...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Local LLM Options

## Definition
Options for running LLMs locally without cloud API dependencies. Includes Ollama, LM Studio, llama.cpp, and various model architectures optimized for local inference.

## Why It Matters
Local LLMs provide privacy, cost control, and offline capability. Essential for experimentation without API costs and for production systems with data sensitivity requirements.

## Key Ideas
- Ollama: easiest local serving, model library, REST API
- LM Studio: GUI + API, model marketplace
- llama.cpp: CPU-optimized inference, GGUF format
- Model selection: 7B-13B for consumer hardware, 70B+ for GPU servers
- Quantization (Q4, Q5, Q8) trades quality for memory usage
- Key models: Qwen, Llama, Mistral, Gemma

## Tradeoffs
- Local models lag behind frontier cloud models in quality
- Hardware requirements limit model size and speed
- Maintenance overhead (model updates, driver issues)

## Related
- [[concepts/Local-LLM]]
- [[concepts/GGUF]]
- [[tools/llama-cpp]]
- [[tools/LM-Studio]]

## Source
[[summaries/KusCamara-PydanticAI-Agent-Creation]]
