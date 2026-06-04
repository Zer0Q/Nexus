# DGX Spark

## Definition
NVIDIA's desktop AI supercomputer: a paperback-sized machine ($2,999) running the GB10 Grace Blackwell superchip with 128GB unified memory, capable of loading models up to 200B parameters. Originally teased as Project DIGITS at CES 2025, rebadged DGX Spark at GTC, available October 2025.

## Why It Matters
Democratizes access to frontier-class model sizes. Where a $2,000 consumer GPU tops out at ~30B parameters, the DGX Spark loads 70B at full precision and stretches toward 200B quantized — models that previously required renting data-center GPUs by the hour.

## Key Ideas
- Chip: NVIDIA GB10 Grace Blackwell Superchip
- AI throughput: 1 PFLOP (quadrillion FP4 ops/second)
- CPU: 20-core ARM (Grace)
- GPU: Blackwell, roughly RTX 5070-class cores
- Memory: 128GB LPDDR5x, unified across CPU + GPU
- Storage: 4TB Gen5 NVMe, self-encrypting
- Networking: ConnectX-7 (chain two units into one)
- Draw: ~150-240W under load
- Footprint: 150 x 150 x 50mm, 1.2kg
- OEM builds: ASUS, Dell, HP, Lenovo, Acer, MSI, GIGABYTE

## Tradeoffs
- Not the fastest box — a 5090 is faster on models that fit in its VRAM
- Single box strains past ~405B parameters (requires two-unit setup)
- Serving thousands of live users is still data-center territory
- $2,999 upfront is a real check, even if it pays back fast

## Related
- [[concepts/DGX-Spark-Specs]] -- detailed hardware specifications
- [[concepts/Cloud-GPU-Cost-Recovery]] -- ROI calculation vs cloud GPU rental
- [[concepts/Unified-Memory-Advantage-DGX]] -- the 128GB memory advantage
- [[concepts/Hardware-Reality-of-Local-AI]] -- broader hardware landscape

## Source
[[summaries/w1nklerr-DGX-Spark-Cost-Recovery]]
