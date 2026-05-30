# Hermes Dashboard

## Definition
Web-based control panel for Hermes Agent accessible at localhost:9119. Provides visual management of models, cron jobs, skills, plugins, profiles, and the Kanban task board — all from a browser without touching the terminal.

## Why It Matters
Lowers the barrier to managing a running Hermes agent. Instead of CLI commands for every configuration change, the dashboard gives immediate visual feedback and bulk control over the agent's capabilities.

## Key Ideas
- **Models tab**: Swap models instantly per profile without terminal access
- **Cron tab**: View and create scheduled tasks with more control than Telegram input
- **Skills tab**: Browse, toggle, and read all learned skills (150+ for a well-used agent)
- **Plugins tab**: Manage API keys and toggle extra capabilities (browser-use, fire-crawl, etc.)
- **Profiles tab**: Create and manage multiple agent instances with distinct roles
- **Kanban board**: Visual task pipeline — Triage → To-Do → Ready → In Progress → Blocked → Done

## Tradeoffs
- Requires browser access (not available via messaging platforms)
- Dashboard state may lag behind CLI changes made in parallel
- Skills tab can overwhelm new users with 87+ bundled skills

## Related
- [[Kanban-Board-Workflow]] -- the most powerful dashboard screen
- [[Agent-Profiles]] -- managed through the Profiles tab
- [[Agent-Cron-Scheduler]] -- managed through the Cron tab
- [[Self-Improvement-Loop]] -- skills visible and editable in the Skills tab

## Source
[[IBuzovskyi-Hermes-Agent-Complete-Guide]]
