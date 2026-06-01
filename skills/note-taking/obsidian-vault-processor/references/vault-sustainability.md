# Vault Sustainability — Lessons from 2026-05-27

## Problem: Vault Inflation

After processing 15 articles, the vault had 123 notes and 37 broken wikilinks. The original skill would auto-create notes for ALL broken links, leading to uncontrolled growth — many notes for concepts that appeared in only one article.

## Solution: Three-Category Triage

Instead of blindly creating notes for broken links, classify each one:

| Category | Criteria | Action | Example |
|----------|----------|--------|---------|
| A: Reusable | Appears in 2+ source notes | Create note | `[[Knowledge-Mapping]]` (3 refs) |
| B: Single-use | Appears in only 1 source note | Remove `[[ ]]`, keep text | `[[Trade-Capture-System]]` -> `Trade Capture System` |
| C: Placeholder | Template placeholder or author name | Remove entirely | `[[topic-name]]` -> `topic-name` |

Result: 8 notes created, 15 links unwrapped, 1 placeholder cleaned. 146 total notes, zero broken links.

## Key Rule: Cross-Article Reuse Threshold

A concept only merits a standalone note if it appears meaningfully in 2+ articles OR is a foundational concept (RAG, LLM, embeddings). Single-article concepts are mentioned as plain text, not linked.

## Orphan Detection

Run periodically (every 10-15 articles). Notes unreferenced by any other note are "orphans." Not necessarily bad — leaf concepts exist — but if orphaned across multiple cycles, consider merging into a parent concept.

## Pre-Creation Duplicate Check (Step 0)

Before creating ANY notes, scan existing concepts/frameworks/tools. If a concept already exists, UPDATE it with new insights rather than creating a duplicate. This is the single most effective anti-inflation measure.

## Workflow: Skill Improvement -> Apply -> Commit

When discovering skill gaps during a session:
1. Patch the in-repo SKILL.md with the improvement
2. Sync to global skills (`~/.hermes/skills/...`)
3. Apply the new rules to the current vault
4. Commit both changes (skill update + vault changes)

## Session 2026-05-27: BMAD + SDD Frameworks (2 articles -> 19 notes)

- Step 0 (duplicate prevention) confirmed: zero overlap with existing 105 notes across knowledge management / local AI domains
- New thematic cluster (AI development frameworks) warranted a new index: `AI-Development-Index`
- Rule of thumb: when articles introduce a genuinely new domain not covered by existing indexes, create a new index rather than forcing fit
- 19 notes from 2 articles is a healthy ratio — both articles were dense with distinct concepts
- Glossary entries (SDD, PRD, BDD, TDD) are lightweight and cross-reference the full notes
