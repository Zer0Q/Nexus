# Tool Selection Hierarchy

## Definition
A ranking of tool access methods by effectiveness: direct API > MCP > skill file > Browser CDP > manual web search. Direct tool access yields far better outputs and saves time and cost compared to indirect methods.

## Why It Matters
The tool you choose determines the quality, speed, and cost of agent operations. Using the wrong tool for the job wastes inference tokens, time, and money. Understanding the hierarchy helps route tasks to the right tool.

## Key Ideas
- Direct API: best output quality, lowest latency, structured data
- MCP: structured access to external tools, good for recurring workflows
- Skill file: markdown instructions, good for one-off or domain-specific tasks
- Browser CDP: interactive exploration, good for JS-heavy sites
- Manual web search: fallback when no direct tool exists
- For recurring workflows/cron jobs, having the right tool is best
- For one-off scraping or interactive exploration, Browser CDP/agentic search is great

## Tradeoffs
- Setup cost of direct APIs/MCPs vs convenience of web search
- Tool maintenance -- APIs change, MCPs break, skills need updates
- Coverage -- not every task has a direct tool available

## Related
- [[concepts/Cost-Tracking]]
- [[concepts/Research-First-Architecture]]
- [[tools/Firecrawl]]

## Source
[[summaries/0xJeff-Hermes-Analyst-60-Days]]
