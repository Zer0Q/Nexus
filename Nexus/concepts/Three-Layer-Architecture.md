# Three-Layer Architecture

## Definition
A business operating system architecture with three layers: knowledge (Obsidian -- plain text markdown), intelligence (Claude via MCP -- active reasoning), and automation (N8N -- scheduling and routing). Together create a business that operates continuously.

## Why It Matters
Separates storage, thinking, and execution -- each layer has a distinct role. The knowledge layer is passive storage, the intelligence layer does reasoning, the automation layer handles timing and routing. Removing any layer degrades the system.

## Key Ideas
- Knowledge layer: Obsidian vault -- human-readable AND machine-navigable
- Intelligence layer: Claude via MCP -- reads files, processes info, makes connections
- Automation layer: N8N -- clock and nervous system, fires workflows on schedule/trigger
- Business OS, not personal KM: structure reflects process flow, not topic relationships
- QUEUE folder: async communication with intelligence layer
- GENERATED folder: output from processed requests

## Tradeoffs
- Three dependencies to maintain (Obsidian, Claude API, N8N)
- Complexity increases with number of workflows
- Requires initial architecture design before tool setup

## Related
- [[Four-Layer-Vault-Architecture]]
- [[Automated-Business-Workflows]]
- [[Async-Queue-Pattern]]

## Source
[[CyrilXBT-Business-Operating-System]]
