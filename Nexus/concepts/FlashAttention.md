# FlashAttention

## Definition
Algoritmo de attention optimizado que reduce reads/writes de high-bandwidth memory (HBM), haciendo attention órdenes de magnitud más rápido sin cambiar el resultado matemático.

## Why It Matters
La misma operación matemática de attention puede tener runtime radicalmente diferente dependiendo de memory access patterns. FlashAttention-3 further optimiza para NVIDIA Hopper GPUs con hardware-aware scheduling, async operations y FP8 support.

## Key Ideas
- Reduce HBM reads/writes — el bottleneck no es FLOPs sino memory bandwidth
- FlashAttention-3 optimiza para NVIDIA Hopper con FP8
- Alternativas: naive attention, PyTorch SDPA (Scaled Dot-Product Attention)
- Parte del stack de serving: vLLM usa PagedAttention, TensorRT-LLM incluye paged attention + quantization, SGLang usa RadixAttention + prefix caching
- Critical para long context — attention naive escala cuadráticamente en memory

## Related
- [[concepts/KV-Cache]]
- [[concepts/Transformer-Architecture]]
- [[concepts/Memory-Bandwidth-Bottleneck]]

## Source
[[summaries/TheAhmadOsman-Step-By-Step-LLM-Engineering-Projects]]
