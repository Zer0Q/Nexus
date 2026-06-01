# Hermes Agent Architecture

## Definition
Unified agent architecture where all entry points (CLI, messaging gateway, batch runner, IDE integration) flow through a single core agent class. ReAct-style synchronous loop: build system prompt, check compression, make API call, execute tools, repeat. Hard cap of 90 turns per task.

## Why It Matters
Platform-agnostic design means the same agent logic works across terminals, Telegram, Discord, and IDEs without code duplication. The unified core simplifies maintenance and ensures consistent behavior everywhere.

## Key Ideas
- Single AIAgent class in run_agent.py — all entry points converge here
- Execution backends: local terminal, Docker, SSH, Modal, Daytona, Singularity (config change, same code)
- Model translation layer: routes any provider through three API formats (Claude, GPT, Gemini, Ollama)
- ReAct loop: system prompt → compression check → API call → tool execution → repeat
- 90-turn hard cap prevents runaway loops (subagents share the same budget)
- "Gateway around a learning agent" (vs. OpenClaw: "agent around a messaging gateway")

## Tradeoffs
- Single core means changes affect all entry points
- 90-turn cap may be too restrictive for very complex tasks
- Synchronous loop blocks other work during API calls

## Related
- [[concepts/Agent-Multi-Tier-Memory]] -- memory layers loaded into the system prompt
- [[concepts/Agent-Identity-Layer]] -- SOUL.md as slot #1 in system prompt
- [[concepts/Multi-Agent-Development]] -- spawning subagents within the same architecture

## Source
[[source-notes/AkshayPachaar-Hermes-Agent-Masterclass]]
