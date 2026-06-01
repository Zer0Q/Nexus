# Agent Architecture over Intelligence

## Definition
AI agents tend to fail due to architectural issues — tool conflicts, integration problems, workflow misalignment — rather than model intelligence limitations. The model's reasoning capacity is rarely the bottleneck.

## Why It Matters
Most debugging time is spent resolving tools fighting each other (API incompatibilities, auth flow conflicts, timeout mismatches) rather than improving model quality. Open-weight models now match frontier labs in intelligence while costing less, making architecture the primary differentiator.

## Key Ideas
- Agent failures are 90% architecture, 10% AI
- Tool conflicts: API compatibility, auth flows, timeout settings
- Provider switching costs 2-3 debugging sessions per swap
- Direct API access avoids aggregator multi-hop latency (5-10s overhead)
- What separates useful from useless agents: tool/skill design, memory persistence, feedback loops, unit economics

## Tradeoffs
- Sticking with one provider means accepting its limitations vs the cost of switching
- Direct API gives better pricing/connectivity but requires more setup

## Related
- [[concepts/Tool-Selection-Hierarchy]]
- [[concepts/Skill-Bundling]]
- [[concepts/Model-Selection-Tiers]]

## Source
[[source-notes/0xJeff-Hermes-Analyst-60-Days]]
