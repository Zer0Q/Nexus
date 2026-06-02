# Agent Dependency Injection

## Definition
Type-safe mechanism for passing runtime data, connections, and configuration into agent tools and instructions. Dependencies are declared via deps_type and accessed through RunContext in tool/instruction functions.

## Why It Matters
Agents need access to databases, APIs, user sessions, and configuration. Dependency injection provides a structured, type-checked way to pass these without global state or singleton patterns.

## Key Ideas
- deps_type declares the dependency schema (dataclass or Pydantic model)
- RunContext[DepType] provides typed access in @agent.tool and @agent.instructions
- Dependencies injected at run time: agent.run(prompt, deps=my_deps)
- Enables testing: swap real DB for mock in test dependencies
- Type checking catches wrong dependency types at compile time
- Common patterns: database connections, API clients, user sessions, config objects

## Tradeoffs
- Adds boilerplate for simple agents
- Overhead not justified for stateless agents with no external dependencies

## Related
- [[tools/PydanticAI]]
- [[concepts/Agent-Tool-Use]]

## Source
[[source-notes/Pydantic-Team-Pydantic-AI-Overview]]
