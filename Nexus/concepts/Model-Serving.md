# Model Serving

## Definition
The infrastructure layer between downloaded models and API endpoints, responsible for request parallelization, memory management, inference optimization, and format handling. vLLM is the dominant framework for LLM serving, handling PagedAttention, continuous batching, and speculative decoding.

## Why It Matters
Raw model weights are not an API. Model serving translates neural networks into production endpoints with concurrency, memory efficiency, and latency optimization. The serving layer determines whether a 35B model responds in seconds or minutes under load.

## Key Ideas
- vLLM configuration parameters control context window (`--max-model-len`), reasoning parsers (`--reasoning-parser`), multimodal backends (`--mm-encoder-attn-backend`), and chat templates
- Speculative decoding via MTP (Multi-Token Prediction): predicts 2 extra tokens per step, 80-92% acceptance rate, ~2x throughput boost
- Only the primary LLM loads in vRAM; secondary models (embedding, reranking) can run on CPU/RAM
- Chat templates define how the model interprets XML tags like thinking tokens — bugs here affect entire model families
- HuggingFace provides recommended serving parameters per model

## Tradeoffs
- vLLM optimization parameters are model-specific — a config that works for Qwen3.6 may break Kimi
- CPU-offloaded models have higher latency but free up vRAM for the primary LLM
- Custom chat templates need maintenance as models evolve

## Related
- [[concepts/Local-Inference-Server]]
- [[concepts/Speculative-Decoding]]
- [[concepts/PagedAttention]]
- [[concepts/Continuous-Batching]]

## Source
[[summaries/Barckcode-Como-Montar-un-Server-de-Inferencia]]
