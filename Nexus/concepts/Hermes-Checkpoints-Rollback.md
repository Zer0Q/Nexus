# Hermes Checkpoints and Rollback

## Definition
Version control for agent sessions — Hermes creates checkpoints at key points, allowing users to roll back to previous states if an agent makes destructive changes.

## Why It Matters
Autonomous agents can make irreversible mistakes. Checkpoints provide safety nets, letting users revert to known-good states without manual recovery.

## Key Ideas
- Checkpoints capture file system state at key milestones
- /rollback command restores previous checkpoint
- Automatic checkpoints on major operations (file writes, git commits)
- Manual checkpoints via /checkpoint command
- Essential for production agent operations

## Tradeoffs
- Storage overhead for checkpoint snapshots
- Checkpoint frequency vs granularity tradeoff
- In-memory state not captured (only file system)

## Related
- [[concepts/Read-Only-Vault-Safety]]
- [[concepts/Scoped-Vault-Access]]
- [[concepts/Shipping-Discipline]]

## Source
[[summaries/NeoAIForecast-checkpoints-rollback-make-hermes-safer-use-real]]
