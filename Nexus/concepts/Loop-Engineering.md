# Loop Engineering

## Definition
Designing systems that prompt agents instead of humans doing it manually. A loop is a recursive goal where you define a purpose and the AI iterates until complete. It sits one floor above harness engineering — the harness is the environment, the loop is the system that runs on a timer, spawns helpers, and feeds itself.

## Why It Matters
The shift from manual prompting to loop design moves the leverage point: instead of typing prompts one turn after another, you build a small system that finds work, hands it out, checks it, records progress, and decides the next step. Both Claude Code and Codex now ship the five primitives natively, making loop design tool-agnostic.

## The Five Primitives
1. **Automations** — scheduled tasks that do discovery and triage (Claude Code: /loop, /goal; Codex: Automations tab, /goal)
2. **Worktrees** — git worktrees for parallel isolation so agents don't collide
3. **Skills** — project knowledge written once, read every run; prevents re-deriving context from zero each cycle
4. **Plugins and connectors** — MCP-based integrations to issue trackers, databases, Slack, staging APIs
5. **Sub-agents** — maker-checker split: one agent writes, a different one (sometimes different model) checks

Plus memory: a markdown file or Linear board that lives outside the conversation and holds what's done and what's next.

## Key Ideas
- "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger
- "My job is to write loops." — Boris Cherny, Anthropic
- The verification piece is the part people skip, and it's the part that matters most. Skip it and you have a token bonfire with a calendar invite
- A mature loop turns repeated steps into scripts rather than calling the model for the same operation a thousand times
- Loops compound through memory: every failure becomes future context in CLAUDE.md/AGENTS.md

## Tradeoffs
- Token costs vary wildly depending on whether you're token-rich or token-poor
- Loops only pay off for repetitive, verifiable work (PR maintenance, flaky tests, profiling)
- For one-off, exploratory, or hard-to-verify work, a loop is the wrong tool
- Three problems get sharper as loops get better: verification, comprehension debt, cognitive surrender

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/Agent-Harness-Layers]]
- [[concepts/Comprehension-Debt]]
- [[concepts/Cognitive-Surrender]]
- [[concepts/Evaluator-Optimizer-Workflow]]
- [[concepts/Agent-Skills-Standard]]
- [[concepts/Goal-Driven-Agents]]

## Source
[[summaries/AddyOsmani-Loop-Engineering]], [[summaries/Tonbis-What-Actually-Are-Loops]]
