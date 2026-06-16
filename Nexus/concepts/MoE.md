---
type: Concept
title: MoE (Mixture of Experts)
description: '- Requires expert parallelism and all-to-all interconnect traffic -
  Stresses engine routing more than dense models - Supported by ExLlamaV3, SGLang,
  vLLM, Te...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# MoE (Mixture of Experts)

Model architecture where different "expert" subnetworks handle different inputs, activating only a subset of parameters per token.

- Requires expert parallelism and all-to-all interconnect traffic
- Stresses engine routing more than dense models
- Supported by ExLlamaV3, SGLang, vLLM, TensorRT-LLM

See also: [[tools/Inference-Engine-Families]], [[concepts/Interconnect-Bottleneck]]
