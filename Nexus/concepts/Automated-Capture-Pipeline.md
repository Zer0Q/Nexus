# Automated Capture Pipeline

## Definition
A system where information flows into the vault automatically from multiple sources (Readwise, Telegram bot, Whisper transcription) without manual copy-pasting, tagging, or categorizing. Zero-friction ingestion: if saving takes >3 seconds, the system fails.

## Why It Matters
Capture friction is the #1 reason knowledge systems fail. Every friction point in capture is a future gap in your knowledge base. Automated capture ensures consistent data flow without relying on willpower.

## Key Ideas
- Readwise: highlights from articles, books, PDFs, newsletters flow automatically
- Telegram bot: forward anything worth saving, it writes the note and files it
- Whisper: voice notes transcribed before hitting the vault
- N8N routes content to correct locations with date, source tag, content type
- Rule: if saving takes >3 seconds, friction is too high
- Nothing in capture layer requires categorization, tagging, or summarizing

## Tradeoffs
- Initial setup time (Readwise account, Telegram bot, N8N workflows)
- Automated captures may need periodic cleanup
- Readwise subscription cost (~$7/month)

## Related
- [[concepts/Four-Layer-Vault-Architecture]]
- [[glossary/Inbox-First-Capture]]
- [[concepts/Anti-Graveyard-Capture]]

## Source
[[source-notes/CyrilXBT-Self-Improving-Vault]]
