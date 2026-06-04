# SOUL-MD Negative Constraints

## Definition
Hard rules in SOUL.md specifying what the agent must never produce -- generic commentary, recaps of known information, flattery before answers, hedging buried at the end of responses, or confident guessing when uncertain.

## Why It Matters
AI models have default behaviors that waste tokens and degrade trust: padding, hedging, flattery, and generic summaries. Negative constraints eliminate these patterns at the system level, so you never see them regardless of the query or context.

## Key Ideas
- Examples: "Do not produce generic market commentary", "No flattery before answers", "Say uncertainty at the start, not buried at the end"
- Acts as a filter on all agent output
- More effective than asking nicely in individual prompts
- Should be specific and actionable, not vague ("be concise" is weak; "no padding" is strong)
- Once set, the agent has not produced forbidden patterns since

## Tradeoffs
- Overly strict constraints may clip legitimate nuance
- Some constraints conflict with the model's training (e.g., "never hedge" vs. honest uncertainty)
- Requires testing to find the right balance

## Related
- [[concepts/SOUL-MD-Configuration]] -- the broader SOUL.md framework
- [[concepts/Agent-Identity-Layer]] -- identity includes boundaries
- [[concepts/SOUL-MD-Challenge-Instructions]] -- the positive complement to negative constraints

## Source
[[summaries/DamiDefi-Hermes-Obsidian-Vault-Integration]]
