# Grounded Research Loop

## Definition
Closed automation loop where sources captured in a local vault (Obsidian) are pushed to a bounded-research sandbox (NotebookLM), grounded answers with inline citations are written back to the vault, and scheduled operators (Hermes cron) orchestrate the cycle without manual intervention.

## Why It Matters
Turns two static tools (vault + research sandbox) into an observable, re-runnable research pipeline. The loop is the product, not the individual notes. Future-you can grep the vault and find every research question asked, with source lists attached for re-verification.

## Key Ideas
- Three non-overlapping roles: Obsidian (durable substrate), NotebookLM (bounded-research sandbox), Hermes (scheduled operator)
- No-agent cron mode proves the wire works with zero LLM tokens before adding expensive skills
- Four failure modes: citation hallucination, notebook ID drift, vault-rename-desync, hardcoded secrets
- Templater for deterministic file naming ensures idempotent cron runs (find -newer + .last-pushed sentinel)
- The wiring pattern (cron -> skill -> MCP -> vault) is operator-agnostic (Claude Code, Cursor, Claude Desktop)

## Tradeoffs
- NotebookLM has no public consumer API; automation relies on fragile Playwright wrappers
- Requires initial setup: Local REST API plugin, MCP configuration, notebooklm-py installation
- Loop quality depends on the substrate -- empty Sources/ folder means no research output

## Related
- [[concepts/Hermes-Obsidian-Integration]]
- [[tools/NotebookLM]]
- [[concepts/Vault-Aware-Automation]]

## Source
[[summaries/tonysimons-Hermes-Obsidian-NotebookLM-Integration]]
