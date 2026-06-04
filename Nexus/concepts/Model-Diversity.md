# Model Diversity

## Definition
Using multiple model providers and backbones for resilience against downtime, pricing changes, restrictions, and sudden quality drops. Model diversity is not just a convenience -- it's infrastructure resilience for agent systems.

## Why It Matters
Depending on a single model/provider creates single points of failure. Outages, API changes, pricing increases, or quality regressions can break entire agent workflows. Diversity spreads risk across the model landscape.

## Key Ideas
- Protection against: downtime, restrictions, pricing changes, quality drops
- Mix of frontier models (GPT-5.5), specialized models (Minimax for tool calling), and local models (Qwen)
- Local LLMs as the always-on layer for 24/7 background cognition
- RAM/VRAM tier decides what work you can run cheaply on local hardware
- Direct API providers often give better discounts than aggregators
- Multi-hop inference (via aggregators) adds 5-10 sec latency

## Tradeoffs
- Provider management overhead vs resilience
- Performance variance across models -- consistent output quality is harder with multiple backbones
- Cost optimization -- some providers are cheaper but less capable

## Related
- [[concepts/Cost-Tracking]]
- [[concepts/Model-Selection-Tiers]]
- [[concepts/Local-AI-Mindset-Shift]]

## Source
[[summaries/gkisokay-21-Mistakes-Building-AI-Agents]]
