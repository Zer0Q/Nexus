# QJL

## Definition
Quantized Johnson-Lindenstrauss — reduces each vector number to a single sign bit (+1 or -1) with zero memory overhead, acting as a mathematical error-checker that eliminates bias in attention scores. Presented at AAAI 2026.

## Why It Matters
Provides the zero-overhead error correction stage in TurboQuant. Traditional quantization adds 1-2 bits of overhead per number for quantization constants; QJL achieves error elimination using exactly 1 bit with no additional storage cost.

## Key Ideas
- Based on Johnson-Lindenstrauss Transform: shrinks high-dimensional data while preserving distances and relationships
- Reduces each number to a sign bit (+1/-1) — the ultimate compression
- Special estimator balances high-precision queries with low-precision simplified data for accurate attention scores
- Eliminates bias from the first-stage quantization (PolarQuant) using just 1 residual bit per dimension
- Zero memory overhead: no quantization constants needed

## Tradeoffs
- Only effective as a residual correction step; not a standalone quantization method
- Requires the Johnson-Lindenstrauss random projection which adds encoding overhead
- Theoretical guarantees hold asymptotically; finite-dimensional performance depends on dimensionality

## Related
- [[concepts/TurboQuant]]
- [[concepts/PolarQuant]]
- [[concepts/Vector-Quantization]]

## Source
[[summaries/google-TurboQuant-Extreme-KV-Compression]]
