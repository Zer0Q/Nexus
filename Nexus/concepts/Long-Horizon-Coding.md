# Long-Horizon Coding

## Definition
The ability of an AI coding agent to run a coding task for hours without human intervention, completing entire projects rather than individual functions. Kimi K2.6 demonstrates this with traces of a 5-day continuous-ops agent, a 12-hour Zig port, and a 13-hour exchange-core refactor.

## Why It Matters
Most AI coding tools complete a function or a file. Long-horizon agents complete a project: planning, implementing in phases, testing each phase, documenting architectural decisions, and handling blockers explicitly. This compresses weeks of work into hours.

## Key Ideas
- The agent plans the full implementation before writing any code
- Implements in logical phases, testing each before moving on
- Documents every decision with architectural implications
- If it hits a blocker, it describes it explicitly rather than working around it silently
- Does not ask for confirmation between steps -- completes the full task autonomously
- The prompt structure: describe full project scope, instruct systematic work, no confirmation between steps

## Tradeoffs
- Hours-long sessions cost significant API tokens
- Architectural mistakes early in the session compound through the rest
- Requires careful scoping to prevent the agent from going off-track

## Related
- [[tools/Kimi-K26-Model]] -- the model that enables this capability
- [[concepts/Swarm-Orchestration]] -- parallel execution at scale
- [[concepts/Five-Layer-AI-Stack]] -- the coding layer of the stack

## Source
[[summaries/Damidefi-Five-Tool-AI-Stack-Full-Build]]
