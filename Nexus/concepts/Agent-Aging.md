# Agent Aging

## Definition
Longitudinal reliability degradation in long-lived agents, organized into four mechanisms: compression aging (write-time summarization drops future-relevant details), interference aging (accumulated similar memories crowd out target facts), revision aging (changed/derived state not updated correctly), and maintenance aging from routine lifecycle events.

## Why It Matters
Long-lived agents are evaluated like freshly initialized models, ignoring the reality that agents accumulate state over time. AgingBench produces aging curves over operational lifetimes rather than single day-one scores, pointing to where repair should target.

## Key Ideas
- Compression aging: summarization loses details needed later
- Interference aging: similar memories crowd each other out
- Revision aging: state changes not propagated to dependent facts
- Maintenance aging: routine lifecycle events (updates, migrations) introduce errors
- Temporal dependency DAG encodes cross-session structure
- Aging curves show degradation over time, not just initial performance

## Tradeoffs
- Summarization aggressiveness (compression aging) vs memory efficiency
- Memory capacity (interference aging) vs retrieval precision
- Update frequency (revision aging) vs consistency overhead

## Related
- [[concepts/Sleep-Consolidation]]
- [[concepts/Agent-Multi-Tier-Memory]]
- [[concepts/Agent-Decay]]

## Source
[[source-notes/DAIR-Top-AI-Papers-of-the-Week]]
