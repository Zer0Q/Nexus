# Stateless Agent Loop

## Definition
A stateless agent loop restarts the agent on each iteration and stores progress in files, git, logs, or structured state instead of accumulating a long conversation.

## Why It Matters
Long agent conversations suffer from context rot and rising cost. Stateless loops keep each iteration focused on current state, current failure, and relevant files, making quality and cost more predictable.

## Key Ideas
- State lives on disk, not in the chat window.
- Each iteration rebuilds a narrow context slice from machine state, failures, changed files, and relevant paths.
- Token budgets prevent the loop from smuggling its own history back into context.
- Works best with deterministic checks and explicit stop conditions.

## Related
- [[concepts/Loop-Engineering]]
- [[concepts/Context-Rot]]
- [[concepts/State-Externalizing-Harnesses]]
- [[concepts/Stop-Condition]]

## Source
[[summaries/H100envy-Autonomous-Loop-Roadmap]]
