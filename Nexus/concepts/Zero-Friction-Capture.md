# Zero-Friction Capture

## Definition
A capture system where one keyboard shortcut opens a floating input box, you type the idea, and it lands in the correct section of today's daily note automatically. No navigation, no categorization at capture time. Claude does the categorization and connection-finding later.

## Why It Matters
The problem with every other note-taking system is retrieval: you save things but never find them. Zero-friction capture solves the intake problem by making capture instantaneous. QuickAdd in Obsidian implements this with four typed capture workflows routed by keyboard shortcut.

## Key Ideas
- One keyboard shortcut opens a floating input box
- Four capture workflows: General Capture (Ctrl+Shift+C), Research Signal (Ctrl+Shift+R), Content Idea (Ctrl+Shift+I), Link (Ctrl+Shift+L)
- Each workflow appends to today's daily note under the matching heading
- No categorization at capture time -- Claude classifies later
- A Telegram bot via N8N extends this to any device, any context, forwarding messages to the vault inbox within 30 seconds

## Tradeoffs
- Daily notes can become unwieldy without a nightly processing workflow
- Multiple capture types require QuickAdd configuration
- Telegram bot requires N8N or similar automation infrastructure

## Related
- [[Three-Capture-Surfaces]] -- the three channels that implement zero-friction capture
- [[Automated-Capture-Pipeline]] -- processes the captures after they land
- [[Inbox-First-Capture]] -- all captures land in an inbox-first daily note

## Source
[[Damidefi-Five-Tool-AI-Stack-Full-Build]]
