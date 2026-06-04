# Interconnect Bottleneck

## Definition
When a model spans multiple GPUs, communication between GPUs via interconnect (PCIe, NVLink, RDMA, Ethernet) becomes the dominant bottleneck, not individual GPU performance.

## Why It Matters
Tensor parallelism requires frequent all-reduce collectives. Pipeline parallelism communicates at stage boundaries. Expert parallelism needs all-to-all traffic for MoE. Weak interconnect kills multi-GPU scaling.

## Key Ideas
- Without NVLink/NVSwitch, pipeline parallelism can outperform tensor parallelism
- NVLink: ~900 GB/s bidirectional, PCIe Gen4 x16: ~32 GB/s
- RDMA over Thunderbolt (JACCL) enables Apple multi-node at ~40 GB/s
- Interconnect quality determines whether tensor or pipeline parallelism is viable

## Tradeoffs
- Tensor parallelism: lower latency per step but higher communication frequency
- Pipeline parallelism: less communication but risk of GPU idle time (bubble)

## Related
- [[concepts/Memory-Bandwidth-Bottleneck]]
- [[concepts/Prefill-vs-Decode]]
- [[concepts/Unified-Memory-Tradeoff]]

## Source
[[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
