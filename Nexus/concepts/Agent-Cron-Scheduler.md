# Agent Cron Scheduler

## Definition
Built-in task scheduler for AI agents that runs jobs on recurring or one-shot schedules. Jobs execute in isolated agent sessions, survive restarts, and deliver output to configured messaging platforms. Supports plain English scheduling (converted to cron expressions automatically).

## Why It Matters
Agents that only respond to prompts require the user to remember to ask. Scheduled jobs let agents proactively deliver value — daily digests, periodic monitoring, recurring reminders — without user intervention.

## Key Ideas
- Gateway daemon ticks every 60 seconds, runs due jobs in isolated sessions
- Jobs stored in jobs.json, output in cron/output/
- Plain English scheduling: "every weekday at 8am India time" → cron expression
- Patterns: one-shot delays (30m), recurring intervals (every 2h), standard cron expressions
- Skill attachment: load a skill before running the prompt
- Job chaining: one job's output becomes the next job's input via context_from

## Tradeoffs
- Jobs run in fresh sessions with no current-chat context — prompts must be self-contained
- Recursive cron scheduling is blocked (jobs can't spawn new jobs)
- Isolated sessions mean jobs can't see intermediate conversation state

## Related
- [[concepts/Agent-Profiles]] -- each profile has its own cron jobs
- [[concepts/Automated-Business-Workflows]] -- broader concept of automated agent workflows
- [[concepts/Daily-Synthesis-Workflow]] -- example use case: daily digest

## Source
[[source-notes/AkshayPachaar-Hermes-Agent-Masterclass]]
