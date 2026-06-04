# Binary Embeddings

## Definition
Vector quantization technique that converts 32-bit float embeddings to 1-bit binary representations, achieving 32x memory reduction with minimal accuracy loss.

## Why It Matters
RAG systems storing millions of vectors face massive memory costs. Binary embeddings reduce storage from gigabytes to megabytes while maintaining ~95% retrieval accuracy. Used by Perplexity, Azure, and HubSpot in production.

## Key Ideas
- Float32 embedding (128 bits) → binary embedding (1 bit per dimension)
- 32x memory reduction: 4 bytes per dimension becomes 1 bit
- Dot product becomes simple bit operations (XOR + popcount)
- Tradeoff: small accuracy loss (~3-5% drop in recall@k)
- Best for large-scale retrieval where approximate similarity suffices

## Tradeoffs
- Accuracy loss vs float32 (acceptable for top-k retrieval)
- Not suitable for tasks requiring precise similarity scores
- Binary quantization works best with high-dimensional embeddings (128+)

## Related
- [[concepts/RAG-Retrieval-Augmented-Generation]]
- [[concepts/PagedAttention]]
- [[concepts/KV-Cache]]

## Source
[[summaries/avichawla-make-rag-32x-memory-efficient-explained-code]]
