# Local LLM API Compatibility

## Definition
The ability of local model runners (like LM Studio) to expose an OpenAI-compatible API endpoint at localhost, allowing any tool designed for cloud AI to connect to local models instead with minimal configuration.

## Why It Matters
This compatibility layer means you do not need to rewrite your tools to go local. Any plugin, script, or application that connects to OpenAI's API can be pointed at your local model by changing one URL from `api.openai.com` to `localhost:1234`.

## Key Ideas
- LM Studio exposes `http://localhost:1234/v1` in OpenAI API format
- Model name is the only other configuration change needed
- Works with Obsidian plugins, scripts, CI pipelines, and custom applications
- Standardised format enables tool portability between cloud and local
- Eliminates vendor lock-in at the integration layer

## Tradeoffs
- Local models may not support all API features (e.g., streaming, function calling)
- Performance depends on local hardware, not guaranteed SLA
- Model updates are manual, not automatic

## Related
- [[LM-Studio]]
- [[Smart-Connections-Plugin]]
- [[On-Device-Knowledge-Base]]

## Source
[[KanikaBK-Offline-AI-Workflow]]
