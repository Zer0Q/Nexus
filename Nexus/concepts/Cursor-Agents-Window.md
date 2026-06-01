# Cursor Agents Window

## Definition
A feature in Cursor 3 that lets you run multiple AI agents simultaneously across different parts of a codebase. Each agent runs in its own Git worktree, so they do not interfere with each other. You review and merge diffs when each is done.

## Why It Matters
Parallel agents compress development time: one refactors a module, one writes tests, one updates documentation, all simultaneously. Agent users now outnumber Tab autocomplete users 2:1 inside Cursor. The feature is available on the Pro plan ($20/month).

## Key Ideas
- Open project in Cursor, press Cmd+Shift+P, type "Agents Window"
- Click "New Agent" and type instructions directly in the agent input box
- Each agent runs in its own Git worktree -- no file conflicts
- Monitor progress in the Agents Window
- Review diffs and merge when each agent is done
- Example: one agent writes tests for auth.ts while another refactors the payment module

## Tradeoffs
- Requires Pro plan ($20/month) for full Agents Window access
- Parallel agents can produce conflicting changes that require manual merge resolution
- Each agent needs precise scoping to avoid working on overlapping files

## Related
- [[concepts/Cloud-Handoff]] -- extends Cursor agents to the cloud for long-running tasks
- [[concepts/Design-Mode-UI]] -- another Cursor 3 feature for UI editing
- [[concepts/Five-Layer-AI-Stack]] -- Cursor is the execution layer

## Source
[[source-notes/Damidefi-Five-Tool-AI-Stack-Full-Build]]
