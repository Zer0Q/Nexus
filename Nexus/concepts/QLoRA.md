---
type: Concept
title: QLoRA
description: LoRA applied to a 4-bit quantized base model, combining parameter efficiency
  (low-rank adaptation) with memory efficiency (quantization) to enable fine-tunin...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# QLoRA

## Definition
LoRA applied to a 4-bit quantized base model, combining parameter efficiency (low-rank adaptation) with memory efficiency (quantization) to enable fine-tuning large models on consumer hardware.

## Why It Matters
Makes fine-tuning 65B+ parameter models feasible on a single consumer GPU by reducing memory footprint through both quantization and parameter-efficient adaptation.

## Key Ideas
- Base model quantized to 4-bit (NF4 — NormalFloat4) using bitsandbytes
- LoRA adapters applied on top of quantized weights
- Gradient checkpointing further reduces memory usage
- Used in ART framework for agent fine-tuning with GRPO + RULER

## Tradeoffs
- 4-bit quantization introduces small accuracy degradation vs. full-precision LoRA
- Requires specific GPU support (NVIDIA with bitsandbytes compatibility)
- Quantization-aware training nuances: double quantization, paged optimizers

## Related
- [[concepts/LoRA]]
- [[concepts/GGUF]]
- [[concepts/ART-Framework]]

## Source
[[summaries/avichawla-Top-15-Fine-Tuning-Techniques]]
