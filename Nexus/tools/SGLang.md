# SGLang

## Definition
Production serving engine optimized for complex workloads: structured outputs, long context, MoE, disaggregation, and routing. vLLM's "systems-brained cousin."

## Why It Matters
When the bottleneck shifts from "can we run the model?" to "can we run it under hostile traffic without torching latency, memory, and cost?"

## Key Ideas
- RadixAttention prefix caching (more aggressive than standard PagedAttention)
- Prefill-decode disaggregation: separate compute and memory phases into specialized instances
- KV cache transfer between prefill and decode instances prevents latency spikes
- Supports NVIDIA, AMD, Intel Xeon, Google TPUs, Ascend NPUs
- Continuous batching, speculative decoding, multi-LoRA

## Tradeoffs
- Younger ecosystem than vLLM
- Disaggregation adds operational complexity

## Related
- [[frameworks/Inference-Engine-Families]]
- [[concepts/Disaggregated-Prefill-Decode]]
- [[tools/vLLM]]

## Source
[[source-notes/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
