---
type: Concept
title: LoRA
description: Low-Rank Adaptation — freezes the base model weights and trains two low-rank
  matrices (A and B) as the update, resulting in 95-99% fewer parameters to fine-t...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# LoRA

## Definition
Low-Rank Adaptation — freezes the base model weights and trains two low-rank matrices (A and B) as the update, resulting in 95-99% fewer parameters to fine-tune compared to full fine-tuning.

## Why It Matters
The dominant parameter-efficient fine-tuning method. Enables fine-tuning large models on consumer hardware by only updating a tiny fraction of parameters while maintaining performance close to full fine-tuning.

## Key Ideas
- Base weights frozen; update applied as low-rank decomposition: delta_W = A * B where A is d x r and B is r x d (r << d)
- Can be merged back into base weights for inference (no runtime overhead)
- Works with any transformer architecture
- Foundation for QLoRA (LoRA + 4-bit quantization)

## Tradeoffs
- Rank (r) is a hyperparameter: too low loses capacity, too high approaches full fine-tuning cost
- May not match full fine-tuning on very complex domain adaptations
- Multiple LoRA adapters can be stacked but increase memory during training

## Related
- [[concepts/QLoRA]]
- BitFit
- Adapter-Tuning
- [[concepts/ART-Framework]]

## Source
[[summaries/avichawla-Top-15-Fine-Tuning-Techniques]]
