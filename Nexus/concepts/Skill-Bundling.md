# Skill Bundling

## Definition
Treating skills as directories with SKILL.md + references/ + scripts/ instead of monolithic prompts. The pipeline logic stays lean (~100 lines in SKILL.md) while noise (endpoint URLs, field names, error codes) lives in reference files that load only when relevant.

## Why It Matters
Monolithic skill prompts grow into spaghetti walls of text. Every new session re-derives context from the growing prompt. Bundled skills cost ~500 tokens to load but save 5000+ tokens of re-explaining context per session.

## Key Ideas
- SKILL.md: pipeline logic and instructions (~100 lines, stays lean)
- references/: API specifics, endpoint shapes, field quirks, query templates
- scripts/: executable helpers for common operations
- Agent gets full context when skill loads, but noise is lazy-loaded
- Over 60+ days and hundreds of sessions, the savings compound significantly
- Early workflows as one giant prompt: 2000+ words covering everything
- Bundled approach: prompt stays lean because details live in reference files

## Tradeoffs
- Directory structure overhead vs monolithic simplicity
- Reference file maintenance -- keeping API docs and endpoints up to date
- Loading strategy -- when to lazy-load reference files vs eager-load all

## Related
- [[concepts/Skill-Curation-System]]
- [[concepts/Skill-Bundling]]
- [[concepts/Feedback-Loop-Training]]

## Source
[[summaries/0xJeff-Hermes-Analyst-60-Days]]
