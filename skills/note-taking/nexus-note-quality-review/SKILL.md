---
type: Workflow
title: Nexus Note Quality Review
description: Audit and remediate low-quality extracted notes in the Nexus vault. Scores each summary on a 1-5 scale across 5 criteria, identifies degradation patterns, and re-processes failing notes.
resource: https://github.com/Zer0Q/Nexus/tree/main/skills/note-taking/nexus-note-quality-review
tags: [nexus, quality, audit, review, summaries]
timestamp: "2026-06-16T14:00:00Z"
name: nexus-note-quality-review
---

## Overview

Quality gate for notes extracted into `Nexus/summaries/`. Detects degradation patterns where the extraction model produced shallow, templated, or copy-paste summaries instead of genuine synthesis. Scores each note, generates a report, and optionally re-processes failing notes.

**Trigger:**
- User asks to "review note quality", "audit summaries", "check extraction quality"
- After a batch ingestion, as a validation step
- User says "revisar calidad de notas", "auditar vault"

## Vault Structure

```
Nexus/
  summaries/        -- compressed summaries (one per article) -- TARGET of this audit
  concepts/         -- atomic concept notes
  tools/            -- tool notes
  indexes/          -- index notes
  raw/              -- incoming unprocessed articles
  raw-notes/        -- raw article copies (reference material)
```

## Quality Criteria (5 dimensions, 1-5 scale each)

### 1. SYNTHESIS (¿el summary sintetiza o copia?)

| Score | Signal |
|-------|--------|
| 5 | 2-3 sentences of original synthesis. Captures the essence without copying phrases from the source. |
| 4 | Good synthesis but slightly verbose or includes one copied phrase. |
| 3 | Partial synthesis — some original framing but heavy reliance on source text. |
| 2 | Mostly copied from source. Reads like a truncated intro or marketing blurb. |
| 1 | Verbatim copy of source text. No synthesis whatsoever. |

**Red flags:** Summary starts with "Today, we're launching...", "Artículo sobre...", summary is a single fragmented sentence, summary contains marketing language.

### 2. CONCEPTS (¿los conceptos están wikilinked y definidos?)

| Score | Signal |
|-------|--------|
| 5 | Every concept is a folder-qualified `[[wikilink]]` with a concrete description explaining WHAT it is and WHY it matters. |
| 4 | All concepts wikilinked and defined, but some descriptions are brief. |
| 3 | Most concepts wikilinked and defined. Some use `-- related concept` or vague placeholders. |
| 2 | Mix of wikilinked and plain text. Some concepts are NOT wrapped in `[[ ]]`. |
| 1 | All concepts are placeholders (`-- related concept`), plain text without wikilinks, or completely generic. |

**Red flags:** `-- related concept`, `-- see article`, `-- mentioned in source`, concepts written as plain text (not wikilinked), descriptions that don't say what the concept IS.

**Insufficient source info:** If the original article mentions a concept but doesn't provide enough detail to define it, use this format:
```markdown
- [[concepts/Concept-Name]] -- needs research: article mentions this but lacks detail for a proper definition
```
This creates a research task for a future agent pass. Never leave concepts as plain text or use vague placeholders — either define them or mark them as needing research.

### 3. INSIGHTS (¿hay insights concretos?)

| Score | Signal |
|-------|--------|
| 5 | 5+ insights with specific data, quotes, numbers, or actionable takeaways. Each insight is a complete thought. |
| 4 | 3-5 solid insights. Mostly concrete, one or two could be sharper. |
| 3 | 2-3 insights, some concrete, some generic. |
| 2 | Insights are just section headers or incomplete phrases (e.g., `"Reasoning layer:"` with no content). |
| 1 | Empty section, or contains `"Refer to extracted concepts for details"`, or just headers without substance. |

**Red flags:** Empty section, `"Refer to extracted concepts"`, incomplete phrases ending in `:`, section headers copied as insights.

### 4. QUESTIONS (¿las preguntas son relevantes?)

| Score | Signal |
|-------|--------|
| 5 | 2-3 questions specific to the article's topic. Reference concepts from the note. Show genuine curiosity about gaps. |
| 4 | Relevant questions but slightly generic. |
| 3 | Questions are tangentially related but could apply to many articles. |
| 2 | Generic template questions: "How does this approach scale in production?", "What are the tradeoffs compared to alternatives?" |
| 1 | Identical questions to other notes (template copy-paste). |

**Red flags:** Same 2 questions appearing across multiple notes, questions that could apply to any article.

### 5. DENSITY (¿la nota tiene densidad de señal?)

| Score | Signal |
|-------|--------|
| 5 | Every line carries information. No filler, no repetition, no empty sections. |
| 4 | High density, minor filler. |
| 3 | Some empty sections or redundant content. |
| 2 | Large portions are empty or placeholder. |
| 1 | Mostly empty structure — frontmatter + section headers + nothing else. |

**Red flags:** Empty `## Key Insights`, empty `## Open Questions`, blank lines between sections, note is under 500 bytes.

## Audit Process

### Step 1: Scan summaries/

```python
import os
summaries_dir = "Nexus/summaries"
notes = sorted([f for f in os.listdir(summaries_dir) if f.endswith('.md')], key=lambda f: os.path.getmtime(os.path.join(summaries_dir, f)), reverse=True)
print(f"Total: {len(notes)} notes")
for n in notes[:10]:
    size = os.path.getsize(os.path.join(summaries_dir, n))
    print(f"  {n} ({size} bytes)")
```

Read each note with `read_file`. For large batches, prioritize the most recent N notes or notes under a size threshold.

### Step 2: Score each note

For each note, evaluate all 5 criteria and assign a score (1-5). Calculate total and average:

```
Note: Author-Topic.md
  SYNTHESIS:  1/5  (verbatim copy of source intro)
  CONCEPTS:   2/5  (all use "-- related concept")
  INSIGHTS:   1/5  (empty section)
  QUESTIONS:  2/5  (generic template questions)
  DENSITY:    1/5  (mostly empty structure)
  TOTAL:      7/25  (FAIL — threshold: 15/25)
  EVIDENCE:   "Summary copies source text", "5 concepts with '-- related concept'"
```

**Thresholds:**
- **PASS (15-25):** Note is acceptable quality
- **WARN (11-14):** Note has issues but salvageable — flag for review
- **FAIL (1-10):** Note needs re-processing

### Step 3: Generate report

Produce a structured report:

```markdown
# Quality Audit Report

## Summary
- Notes scanned: N
- PASS: X (YY%)
- WARN: Y (ZZ%)
- FAIL: Z (WW%)

## Failed Notes (detailed)
### Note 1: filename.md — Score: X/25
- SYNTHESIS: 1/5 — evidence
- CONCEPTS: 2/5 — evidence
- ...

## Warnings
### Note N: filename.md — Score: X/25
- ...

## Patterns Detected
- Pattern 1: description (affected notes: N)
- Pattern 2: description (affected notes: M)
```

### Step 4: Identify common patterns

Group failures by pattern:

| Pattern | Description | Fix |
|---------|-------------|-----|
| `copy-paste-summary` | Summary copies source text | Re-process with explicit "synthesize, don't copy" instruction |
| `placeholder-concepts` | All concepts use `-- related concept` | Re-process with concept definitions required |
| `plain-text-concepts` | Concepts mentioned as plain text, NOT wikilinked | Wrap in `[[ ]]` or mark as `needs research` |
| `empty-insights` | Key Insights section empty or headers only | Re-process with insight extraction required |
| `template-questions` | Same questions across notes | Re-process with article-specific questions |
| `thin-note` | Note under 500 bytes | Re-process with raw article for context |
| `needs-research` | Concepts marked with `needs research` | Run research pass to augment definitions |

### Step 5: Remediation (if user approves)

For each FAIL note:
1. Find the corresponding raw article in `raw-notes/` (match by title or filename pattern)
2. Re-process the note following the `obsidian-vault-processor` skill, with these **additional quality constraints**:

```
QUALITY CONSTRAINTS (add to re-processing prompt):
- Summary: Write 2-3 sentences of YOUR OWN synthesis. Do NOT copy phrases from the source.
- Core Concepts: Every concept MUST be a folder-qualified `[[wikilink]]` with a concrete description explaining WHAT it is and WHY it matters.
  - If the source article mentions a concept but lacks detail, use: `[[concepts/Concept-Name]] -- needs research: article mentions this but lacks detail`
  - Never use "-- related concept" or leave concepts as plain text without wikilinks.
  - Concepts written as plain text (not wikilinked) are broken links — Obsidian will NOT resolve them.
- Key Insights: Extract 5+ specific insights with data, quotes, numbers, or actionable takeaways. Each insight must be a complete sentence.
- Open Questions: Write 2-3 questions specific to THIS article's content. Reference concepts from the note with folder-qualified `[[wikilinks]]`.
- Every section must have substantive content. No empty sections.
```

3. Dry-run the improved note diff before overwriting the old one
4. Re-score to confirm improvement

## Quick Checks (for spot audits)

When the user wants a fast check without a full audit, run these heuristic checks:

```python
import os, re
summaries_dir = "Nexus/summaries"
issues = []
for f in os.listdir(summaries_dir):
    if not f.endswith('.md'): continue
    path = os.path.join(summaries_dir, f)
    with open(path) as fh:
        content = fh.read()
    # Check 1: "-- related concept" placeholder
    if '-- related concept' in content:
        issues.append(f"  {f}: placeholder concepts ('-- related concept')")
    # Check 1b: concepts as plain text (not wikilinked)
    concepts_match = re.search(r'## Core Concepts\n+(.*?)(?:\n##|\Z)', content, re.DOTALL)
    if concepts_match:
        concept_lines = [l.strip() for l in concepts_match.group(1).split('\n') if l.strip().startswith('- ')]
        for cl in concept_lines:
            # Line has a concept name but NOT wrapped in [[ ]]
            if '--' in cl and '[[' not in cl:
                plain_text = cl.split('--')[0].strip().lstrip('- ').strip()
                issues.append(f"  {f}: plain text concept (not wikilinked): '{plain_text}'")
    # Check 2: empty Key Insights
    if '## Key Insights\n\n' in content or '## Key Insights\n\n##' in content:
        issues.append(f"  {f}: empty Key Insights")
    # Check 3: generic questions
    if 'How does this approach scale in production?' in content:
        issues.append(f"  {f}: generic template questions")
    # Check 4: thin note
    if len(content) < 500:
        issues.append(f"  {f}: thin note ({len(content)} bytes)")
    # Check 5: "Refer to extracted concepts"
    if 'Refer to extracted concepts' in content:
        issues.append(f"  {f}: lazy insights ('Refer to extracted concepts')")
    # Check 6: "Artículo sobre"
    if 'Artículo sobre' in content:
        issues.append(f"  {f}: lazy summary ('Artículo sobre...')")
    # Check 7: "needs research" markers (info, not error)
    if 'needs research' in content:
        issues.append(f"  {f}: has concepts marked 'needs research' (research task pending)")
if issues:
    print(f"ISSUES ({len(issues)}):")
    for i in issues:
        print(i)
else:
    print("Quick check: no obvious issues found.")
```

## Integration with obsidian-vault-processor

This skill is a **companion** to `obsidian-vault-processor`. Run the quality review:
1. **After** a batch ingestion (validation step)
2. **Before** cleaning `raw/` (gate — don't delete source if quality is bad)
3. **Periodically** as a health check on the vault

The quality constraints from Step 5 can be folded into the `obsidian-vault-processor` skill itself as a permanent fix.
