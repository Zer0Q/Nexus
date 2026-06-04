# Skill Curation System

## Definition
Automated system where an agent executor runs tasks using skills from a repository, and a separate curator agent evaluates outcomes to improve, create, or deprecate skills based on performance data.

## Why It Matters
Skills degrade as tasks evolve. Manual curation doesn't scale. An automated curator continuously optimizes the skill library based on real execution results.

## Key Ideas
- SkillRepo: central repository of reusable skill definitions
- Agent Executor: frozen agent that runs tasks using skills
- Skill Curator: trainable agent that evaluates and updates skills
- Three-stage cycle: Execute → Evaluate → Update
- Skills follow standard format: trigger, steps, pitfalls, verification

## Tradeoffs
- Curator can introduce regressions
- Skill evaluation metrics are hard to define
- Frozen executor limits adaptability during runs

## Related
- [[concepts/Self-Evolving-Skills]]
- [[concepts/Skill-Based-AI-Agents]]
- [[concepts/Self-Improvement-Loop]]

## Source
[[summaries/neuralavb-skill-curation-self-evolving-agents-explained-clearly]]
