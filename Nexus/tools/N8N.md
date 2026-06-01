# N8N

## Definition
Open-source automation tool that connects capture sources to vault destinations. Runs workflows on schedule (cron), event (file watch), and external triggers (webhook). Self-hosted or cloud version.

## Why It Matters
The "clock and nervous system" of automated knowledge systems. Routes information from Readwise, Telegram, Whisper into Obsidian vaults. Triggers AI synthesis workflows. Free to self-host, unlimited workflow runs.

## Key Ideas
- Workflow pattern: trigger -> read CLAUDE.md -> read vault -> call AI -> write output -> notify -> log
- Three trigger types: cron (scheduled), file watch (event-based), webhook (external)
- Self-hosted on $5 DigitalOcean droplet: unlimited runs, no per-execution pricing
- Connects Readwise -> Obsidian, Telegram -> Obsidian, Obsidian -> Claude API
- Nightly sweep: checks inbox, categorizes items, moves to correct subfolder

## Tradeoffs
- Self-hosting requires maintenance
- Workflow debugging can be complex
- Cloud version has execution limits

## Related
- [[concepts/Four-Layer-Vault-Architecture]]
- [[concepts/Automated-Capture-Pipeline]]
- [[concepts/Automated-Business-Workflows]]

## Source
[[source-notes/CyrilXBT-Business-Operating-System]]
