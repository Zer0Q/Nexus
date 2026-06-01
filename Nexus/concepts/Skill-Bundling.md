# Skill Bundling

## Definition
Structuring agent skills as directories containing a lean SKILL.md pipeline file plus supporting reference files and scripts, rather than monolithic prompts. The SKILL.md stays ~100 lines while noise (endpoints, field names, error codes) lives in separate reference files.

## Why It Matters
Monolithic skill prompts grow into unmaintainable spaghetti with each bug fix. Bundled skills cost ~500 tokens to load but save 5000+ tokens of re-explaining context every session. Over 60+ days and hundreds of sessions, the savings compound significantly.

## Key Ideas
- SKILL.md contains pipeline logic only (~100 lines)
- `references/` holds API-specific details: endpoint shapes, field quirks, RPC patterns
- `scripts/` contains executable helpers (shell scripts, validation tools)
- Agent loads full context on skill activation — pipeline + references + scripts
- Reference files only load when relevant, keeping the prompt lean
- Each new session starts with full context instead of re-deriving from scratch

## Tradeoffs
- More files to maintain vs single prompt
- Reference files must stay in sync with actual API changes
- Initial setup cost is higher; pays off after ~10+ sessions

## Related
- [[concepts/Agent-Architecture-over-Intelligence]]
- [[concepts/Self-Evolving-Skills]]
- [[concepts/Progressive-Disclosure-Skills]]

## Source
[[source-notes/0xJeff-Hermes-Analyst-60-Days]]
