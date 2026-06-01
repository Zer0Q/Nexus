# Business Operating System

## Definition
An Obsidian vault structured as a continuous business processor with six interconnected systems: client intelligence, project operations, content production, financial operations, research/intelligence, and performance/review. Runs on schedule and trigger without manual initiation.

## Why It Matters
Removes the knowledge worker from 4-6 hours/day of administrative overhead. The system operates continuously -- you direct it, it maintains your business. After 6 months, the vault knows your business deeper than a new employee.

## Key Ideas
- Six systems, each owning a specific function, passing info through shared vault structure
- N8N handles scheduling (cron), events (file watch), and external triggers (webhooks)
- CLAUDE.md is the business constitution -- read before every operation
- QUEUE/GENERATED async pattern for request/response workflow
- Weekly Focus section weights all actions toward current priorities
- Compounding: every logged interaction makes future briefs richer

## Tradeoffs
- Complex initial setup across three layers (Obsidian, Claude, N8N)
- Ongoing token costs for daily/weekly AI processing
- Risk of automated errors if outputs not reviewed

## Related
- [[concepts/Three-Layer-Architecture]]
- [[concepts/Automated-Business-Workflows]]
- [[concepts/Async-Queue-Pattern]]

## Source
[[source-notes/CyrilXBT-Business-Operating-System]]
