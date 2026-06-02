# Echo Chamber Bias

## Definition
The tendency of agent-curated research feeds to gravitate toward the same sources, topics, and big-cap names, reinforcing existing holdings and perspectives. Sources/analysts mention the same names (NVIDIA, TSMC, etc.), exacerbating the chamber effect.

## Why It Matters
When an agent's research feeds its own outputs, which then influence future research queries, the system creates a self-reinforcing loop. This is especially dangerous in investment analysis where confirmation bias leads to poor decisions.

## Key Ideas
- Sources gravitate toward same big-cap names and popular narratives
- "Why it matters" sections tend to align with existing holdings
- The problem compounds over time as the agent's memory reinforces the bias
- No reliable solution yet -- acknowledged as an open problem
- Countermeasures: diverse source selection, contrarian analysis prompts, explicit diversity requirements

## Tradeoffs
- Source diversity vs signal quality -- niche sources may be noisy
- Contrarian prompts vs natural analysis -- forced contrarianism can be artificial
- Manual curation vs automated diversity -- who decides what "diverse" means?

## Related
- [[concepts/Research-First-Architecture]]
- [[concepts/Feedback-Loop-Training]]
- [[concepts/Vault-Aware-Research]]

## Source
[[source-notes/0xJeff-Hermes-Analyst-60-Days]]
