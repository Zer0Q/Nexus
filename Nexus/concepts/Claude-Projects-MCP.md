# Claude Projects with MCP

## Definition
Claude Projects provide persistent memory across every conversation within a project, while MCP (Model Context Protocol) connections give Claude live access to external tools and data sources. Together they transform Claude from a chat interface into a system that compounds context over time and acts on the world.

## Why It Matters
No other model has an equivalent native implementation. Projects give Claude persistent memory so every conversation starts with full system context. MCP connections let it act on external tools and data sources. The combination turns a chatbot into a compounding knowledge system.

## Key Ideas
- Create a Claude Project named for the system you are building
- Upload CLAUDE.md context file as project knowledge
- Install relevant MCP servers via Claude Code: research (Exa, Tavily), data (CoinGecko, LunarCrush), productivity (Notion, Linear)
- Paste operating rules and context in Project Instructions
- Every conversation inside that project starts with full system context loaded automatically
- The system compounds: more conversations = more context = better output

## Tradeoffs
- Project context has a size limit
- MCP servers require API keys and configuration
- Persistent memory means errors or bad context can compound negatively

## Related
- [[CLAUDE-MD-as-Context-Layer]] -- the context file uploaded to projects
- [[Five-Layer-AI-Stack]] -- Claude Projects enable the reasoning layer to persist
- [[Compounding-Knowledge-Context]] -- the compounding effect of persistent memory

## Source
[[Damidefi-Five-Tool-AI-Stack-Full-Build]]
