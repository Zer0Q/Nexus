# Hermes-Obsidian Integration

## Definition
Connecting Hermes Agent to an Obsidian vault via the Obsidian Local REST API plugin on localhost:27124, giving the agent programmatic read and write access to vault markdown files during execution, not just at boot.

## Why It Matters
This transforms Hermes from a stateless Q&A tool into a persistent research partner. The agent reads and writes the same markdown files Obsidian manages, so every capture, note, and connection is immediately available to Hermes without manual context loading.

## Key Ideas
- Setup: `hermes memory setup --provider obsidian --path ~/path/to/vault`
- Requires Obsidian Local REST API plugin enabled
- Agent reads and writes normal .md files -- no special format needed
- Works alongside existing vault structure (no reorganization required)
- Hermes v0.14 (May 2026) shipped first-class Obsidian provider support

## Tradeoffs
- Requires Obsidian running on the same machine (localhost dependency)
- Full vault access means the agent can read everything -- scoped access recommended first
- REST API plugin adds a network service on your local machine

## Related
- [[Live-Vault-Memory]] -- the memory model this integration enables
- [[Scoped-Vault-Access]] -- safe onboarding pattern
- [[Vault-Aware-Automation]] -- broader category of vault-interacting systems
- [[Hermes-Agent-Architecture]] -- Hermes's overall design

## Source
[[DamiDefi-Hermes-Obsidian-Vault-Integration]]
