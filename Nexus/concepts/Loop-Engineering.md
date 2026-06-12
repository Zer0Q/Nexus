# Loop Engineering

## Definition
Designing systems that prompt agents instead of humans doing it manually. A loop is a recursive goal where you define a purpose and the AI iterates until complete. It sits one floor above harness engineering — the harness is the environment, the loop is the system that runs on a timer, spawns helpers, and feeds itself.

## Why It Matters
The shift from manual prompting to loop design moves the leverage point: instead of typing prompts one turn after another, you build a small system that finds work, hands it out, checks it, records progress, and decides the next step. Both Claude Code and Codex now ship the five primitives natively, making loop design tool-agnostic.

## The Five-Stage Cycle
Every loop moves through: DISCOVER → PLAN → EXECUTE → VERIFY → ITERATE. Pass verification → ship. Fail → loop again.

## The Six Building Blocks
1. **Automations** — the heartbeat; triggers discovery on a cadence (Claude Code: /loop, /goal; Codex: Automations tab)
2. **Worktrees** — git worktrees for parallel isolation so agents don't collide
3. **Skills** — project knowledge written once, read every run; prevents re-deriving context from zero each cycle
4. **Plugins and connectors** — MCP-based integrations to issue trackers, databases, Slack, staging APIs
5. **Sub-agents** — [[concepts/Maker-Checker-Split]]: one agent writes, a different one (sometimes different model) checks
6. **Memory** — a markdown file or Linear board that lives outside the conversation; the spine of the whole loop

## Key Ideas
- "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger
- "My job is to write loops." — Boris Cherny, head of Claude Code at Anthropic
- The verification piece is the part people skip, and it's the part that matters most
- [[concepts/Token-Burn]] is the hidden blocker: single loops cost 50K-200K tokens, fleet loops 500K-2M
- Cheap models (DeepSeek V4: 1.7B tokens for $20) remove the last real blocker
- [[concepts/Open-vs-Closed-Loop]]: start with closed loops (bounded, reliable, affordable), open them up once quality gates are proven
- [[concepts/Single-vs-Fleet-Loop]]: single-agent = one brain self-improving; fleet = orchestrator + specialists + subagents
- "One reliable loop is worth a thousand perfect prompts"

## Tradeoffs
- Token costs vary wildly depending on whether you're token-rich or token-poor
- Loops only pay off for repetitive, verifiable work
- For one-off, exploratory, or hard-to-verify work, a loop is the wrong tool
- Three problems get sharper as loops get better: verification, comprehension debt, cognitive surrender
- The loop does not know whether you use it to move faster on work you understand or to avoid understanding the work

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/Agent-Harness-Layers]]
- [[concepts/Comprehension-Debt]]
- [[concepts/Cognitive-Surrender]]
- [[concepts/Evaluator-Optimizer-Workflow]]
- [[concepts/Agent-Skills-Standard]]
- [[concepts/Goal-Driven-Agents]]
- [[concepts/Maker-Checker-Split]]
- [[concepts/Token-Burn]]
- [[concepts/Open-vs-Closed-Loop]]
- [[concepts/Single-vs-Fleet-Loop]]

## Source
[[summaries/AddyOsmani-Loop-Engineering]], [[summaries/Tonbis-What-Actually-Are-Loops]], [[summaries/Sairahul1-Loops-What-Every-AI-Engineer-Needs-to-Know]]
