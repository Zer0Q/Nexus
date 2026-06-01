# vLLM

## Definition
The default open-source production server for LLM inference. Offers PagedAttention, continuous batching, chunked prefill, prefix caching, extensive quantization, and multi-GPU parallelism.

## Why It Matters
First engine most teams should evaluate for serious open-source LLM serving. Best balance of performance, flexibility, and ecosystem maturity.

## Key Ideas
- PagedAttention-based KV memory management
- CUDA/HIP graphs, torch.compile, speculative decoding
- Quantization: FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ, AWQ, GGUF
- Parallelism: tensor, pipeline, data, expert, context
- APIs: OpenAI-compatible, Anthropic Messages, gRPC
- Multi-LoRA, structured outputs, tool calling
- Multi-node via Ray; without NVLink, pipeline parallelism may beat tensor

## Tradeoffs
- Still requires systems thinking: tuning batching, context, GPU utilization, parallelism layout
- Not the absolute fastest on NVIDIA-only hardware (TensorRT-LLM can beat it)

## Related
- [[frameworks/Inference-Engine-Families]]
- [[concepts/PagedAttention]]
- [[concepts/Continuous-Batching]]
- [[concepts/Disaggregated-Prefill-Decode]]

## Source
[[source-notes/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
