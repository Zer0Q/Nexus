# DGX Spark Specs

## Definition
Detailed hardware specifications for the NVIDIA DGX Spark: GB10 Grace Blackwell superchip delivering 1 PFLOP FP4 throughput with 128GB LPDDR5x unified memory, 20-core ARM CPU, Blackwell GPU cores, 4TB Gen5 NVMe storage, and ConnectX-7 networking in a 150x150x50mm form factor.

## Why It Matters
The spec sheet reveals why the DGX Spark is transformative: 128GB of unified memory is the game-changer, not the petaflop rating. This is what lets it load models a $2,000 consumer GPU physically cannot open.

## Key Ideas
- **Chip**: NVIDIA GB10 Grace Blackwell Superchip
- **AI throughput**: 1 PFLOP FP4 (a quadrillion operations/second)
- **CPU**: 20-core ARM (Grace)
- **GPU**: Blackwell architecture, roughly RTX 5070-class cores
- **Memory**: 128GB LPDDR5x, unified across CPU + GPU — the spec that changes everything
- **Storage**: 4TB Gen5 NVMe, self-encrypting
- **Networking**: ConnectX-7 — chain two units into one logical system
- **Power**: ~150-240W under load
- **Physical**: 150 x 150 x 50mm, 1.2kg — a thick paperback
- **Price**: $2,999 at launch

## Tradeoffs
- Blackwell GPU cores are ~RTX 5070-class, not 5090-class — raw speed trails top consumer GPUs
- LPDDR5x bandwidth lower than HBM on data-center GPUs
- Single-unit limit around 200B parameters; 405B requires two boxes

## Related
- [[concepts/DGX-Spark]] -- the product overview
- [[concepts/Unified-Memory-Advantage-DGX]] -- why 128GB matters more than raw speed
- [[concepts/Hardware-Reality-of-Local-AI]] -- broader hardware comparison context

## Source
[[source-notes/w1nklerr-DGX-Spark-Cost-Recovery]]
