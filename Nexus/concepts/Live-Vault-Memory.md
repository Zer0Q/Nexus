# Live Vault Memory

## Definition
A memory model where the AI agent reads and writes to a knowledge vault that self-updates without manual intervention. When new captures land via QuickAdd, Telegram bot, or Readwise, the agent reads them in the next session automatically -- no context file curation required.

## Why It Matters
Manual context systems (Claude Projects, uploaded context files) require you to decide what goes in and when to update. Live vault memory eliminates this bottleneck -- the vault is always current because it is the same vault you use for daily work.

## Key Ideas
- Captures land in the vault immediately through existing pipelines
- Agent reads the vault at session start, picking up everything new
- The agent also writes to the vault, compounding the context layer
- No separate context management workflow needed
- Quality compounds faster than manual systems because updates are automatic

## Tradeoffs
- Larger vaults mean higher token costs per session
- Agent may read irrelevant files if vault structure is messy
- Requires trust in the agent's write permissions

## Related
- [[concepts/Hermes-Obsidian-Integration]] -- the technical mechanism enabling this
- [[concepts/Compounding-Knowledge-Context]] -- how quality improves over time
- [[concepts/Agent-Multi-Tier-Memory]] -- Hermes's broader memory architecture
- [[concepts/CLAUDE-MD-as-Context-Layer]] -- the manual alternative this replaces

## Source
[[summaries/DamiDefi-Hermes-Obsidian-Vault-Integration]]
