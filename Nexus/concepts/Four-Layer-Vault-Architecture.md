# Four-Layer Vault Architecture

## Definition
A knowledge system architecture with four distinct layers: capture (zero-friction ingestion), automation/pipeline (routing and formatting), memory/storage (Obsidian vault), and intelligence (AI reasoning across accumulated data). Each layer has exactly one job; nothing overlaps.

## Why It Matters
Separating concerns prevents the system from collapsing under its own complexity. Each layer can be upgraded independently. Removing any one layer degrades the system into a "slightly fancier note-taking app."

## Key Ideas
- Layer 1 (Capture): Readwise, Whisper, Telegram bot -- raw information in, no categorization
- Layer 2 (Pipeline): N8N routes content, formats notes, triggers AI workflows
- Layer 3 (Memory): Obsidian vault -- permanent storage, organized by type not topic
- Layer 4 (Intelligence): Claude/Vellum reads across everything, surfaces connections
- Capture friction kills systems: if saving takes >3 seconds, the habit breaks
- Intelligence layer transforms vault from library to researcher

## Tradeoffs
- More moving parts = more things that can break
- Requires initial setup investment (N8N, API keys, bot configuration)
- Token costs for daily/weekly AI processing

## Related
- [[Inbox-First-Capture]]
- [[Automated-Capture-Pipeline]]
- [[Organize-by-Type-not-Topic]]

## Source
[[DamiDefi-Claude-Vault-Integration]]
