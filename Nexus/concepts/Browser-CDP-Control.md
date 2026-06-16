---
type: Concept
title: Browser CDP Control
description: Using Chrome DevTools Protocol (CDP) to give AI agents direct browser
  control — navigating, clicking, filling forms, and extracting data from web pages
  progr...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Browser CDP Control

## Definition
Using Chrome DevTools Protocol (CDP) to give AI agents direct browser control — navigating, clicking, filling forms, and extracting data from web pages programmatically.

## Why It Matters
Agents limited to API calls can't interact with the open web. Browser control via CDP enables agents to scrape, fill forms, navigate SPAs, and automate web workflows.

## Key Ideas
- CDP provides programmatic access to Chrome internals
- Agents can navigate, click, type, screenshot, and extract DOM
- Essential for web research, form automation, and testing
- Hermes Agent's browser toolset uses CDP under the hood
- Security: agents can escape to browser, need sandboxing

## Tradeoffs
- Security risks (agents can access any website)
- Slower than API calls
- Fragile to website structure changes
- Rate limiting and bot detection

## Related
- [[concepts/Hermes-Agent-Architecture]]
- [[concepts/Scoped-Vault-Access]]
- [[concepts/Read-Only-Vault-Safety]]

## Source
[[summaries/NeoAIForecast-hermes-has-browser-escape-hatch-agents-don]]
