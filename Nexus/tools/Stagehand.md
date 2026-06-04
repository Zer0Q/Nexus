# Stagehand

## Definition
TypeScript-native browser automation built on Playwright. Tell it what to do in plain English ("click the login button", "extract the price") and it figures out the selectors itself. Built for production agent workflows.

## Why It Matters
Stagehand bridges the gap between brittle CSS selectors and full browser control. It understands page semantics and adapts to structural changes, making it reliable for production scraping and automation workflows.

## Key Ideas
- TypeScript-native, built on Playwright
- Plain English instructions instead of manual selector writing
- Auto-discovers selectors based on semantic descriptions
- Built for production agent workflows
- Good middle ground between selector-based scrapers and full browser control

## Tradeoffs
- TypeScript-focused -- less accessible for Python teams
- May not handle all anti-bot systems
- Overhead vs direct API scraping for simple tasks

## Related
- [[tools/Browser-Use]]
- [[tools/AgentQL]]
- [[concepts/Tool-Selection-Hierarchy]]

## Source
[[summaries/DamiDefi-20-GitHub-Scraping-Repos]]
