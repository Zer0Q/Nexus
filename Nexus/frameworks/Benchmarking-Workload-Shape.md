# Benchmarking Workload Shape

## Definition
Proper inference benchmarking requires specifying model, weights, engine, hardware, workload distribution, and measuring multiple metrics (TTFT, TPOT, p50/p95/p99, memory, cost).

## Why It Matters
A single "180 tok/s" number is meaningless without context. Benchmarks that ignore workload shape mislead purchasing and deployment decisions.

## Key Ideas
- Must specify: model arch/params, quant format, engine version, GPU SKU, interconnect, workload distribution, concurrency
- Separate prefill from decode metrics
- Track p95/p99, not only averages
- Test cache reuse if app has repeated prefixes
- Benchmark structured output separately (grammar adds overhead)
- Re-test after every driver/CUDA/engine upgrade

## Tradeoffs
- Comprehensive benchmarking takes time; single-number benchmarks are tempting but misleading

## Related
- [[Prefill-vs-Decode]]
- [[Runtime-Overhead]]

## Source
[[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
