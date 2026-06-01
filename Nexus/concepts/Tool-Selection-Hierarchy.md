# Tool Selection Hierarchy

## Definition
A ranked hierarchy for selecting tools when building agent workflows, ordered by reliability, output quality, and cost efficiency: Direct API > MCP > Markdown skill files > Browser CDP > Headless browser.

## Why It Matters
Choosing the right tool tier for each task significantly impacts output quality, latency, and cost. Using the wrong tier (e.g., headless browser when an API exists) wastes resources and introduces failure points.

## Key Ideas
- **Direct API access**: Best outputs, lowest latency, saves time and cost. Use for recurring workflows and cron jobs.
- **MCP (Model Context Protocol)**: Standardized tool integration, good for structured data access.
- **Markdown skill files**: Self-contained context for specific tasks, no runtime overhead.
- **Browser CDP**: Better than headless browsers for interactive exploration; avoids Cloudflare blocks. Good for one-off scraping.
- **Headless browser (Playwright)**: Most fragile — blocked by Cloudflare, highest maintenance. Last resort.

## Tradeoffs
- Direct APIs require authentication setup and rate limit management
- Browser CDP is slower but handles JS-heavy sites that APIs don't cover
- One-off tasks justify higher-friction tools; recurring tasks demand the highest tier

## Related
- [[concepts/Agent-Architecture-over-Intelligence]]
- [[concepts/Browser-CDP-Control]]
- [[concepts/Skill-Bundling]]

## Source
[[source-notes/0xJeff-Hermes-Analyst-60-Days]]
