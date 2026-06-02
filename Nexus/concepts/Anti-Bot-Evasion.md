# Anti-Bot Evasion

## Definition
Techniques and tools for surviving anti-bot systems (Cloudflare, DataDome, Kasada, PerimeterX) in web scraping workflows. The anti-bot market hit $11B in 2025 and now blocks well-built in-house scrapers within seconds on protected domains.

## Why It Matters
The scraping problem in 2026 is not writing the code -- it's surviving the anti-bot arms race. Every major site has bot detection, and the systems are getting smarter. Purpose-built anti-detection tools are now essential infrastructure for scraping workflows.

## Key Ideas
- Anti-bot market: $11B in 2025, blocking well-built scrapers within seconds
- Stealth browsers: Hyperbrowser (drop-in Playwright replacement), Scrapling (adaptive selectors)
- Proxy rotation: automatic IP rotation when flagged
- Fingerprint management: avoiding headless detection and browser fingerprinting
- Rate limiting: automatic throttling to avoid triggering alerts
- Vision-based tools (Skyvern) bypass selector-based detection entirely

## Tradeoffs
- Cost of anti-detection tools vs value of scraped data
- Legal/ethical considerations of bypassing bot protection
- Detection arms race -- today's evasion may be tomorrow's detected pattern

## Related
- [[tools/Hyperbrowser]]
- [[tools/Firecrawl]]
- [[concepts/Tool-Selection-Hierarchy]]

## Source
[[source-notes/DamiDefi-20-GitHub-Scraping-Repos]]
