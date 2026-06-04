---
name: nexus-note-quality-review
description: "Audit and remediate low-quality extracted notes in the Nexus vault. Scores each summary on a 1-5 scale across 5 criteria, identifies degradation patterns, and re-processes failing notes."
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
  summaries/        -- source notes (one per article) — TARGET of this audit
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

### 2. CONCEPTS (¿los conceptos están definidos?)

| Score | Signal |
|-------|--------|
| 5 | Every concept has a specific, concrete description. Descriptions explain WHAT and WHY. |
| 4 | Concepts defined, but some descriptions are brief or could be more specific. |
| 3 | Mix of good definitions and vague ones. Some concepts feel generic. |
| 2 | Most concepts use `-- related concept` or equally vague placeholders. |
| 1 | All concepts are placeholders (`-- related concept`) or completely generic. |

**Red flags:** `-- related concept`, `-- see article`, `-- mentioned in source`, descriptions that don't say what the concept IS.

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
| `empty-insights` | Key Insights section empty or headers only | Re-process with insight extraction required |
| `template-questions` | Same questions across notes | Re-process with article-specific questions |
| `thin-note` | Note under 500 bytes | Re-process with raw article for context |

### Step 5: Remediation (if user approves)

For each FAIL note:
1. Find the corresponding raw article in `raw-notes/` (match by title or filename pattern)
2. Re-process the note following the `obsidian-vault-processor` skill, with these **additional quality constraints**:

```
QUALITY CONSTRAINTS (add to re-processing prompt):
- Summary: Write 2-3 sentences of YOUR OWN synthesis. Do NOT copy phrases from the source.
- Core Concepts: Each concept MUST have a concrete description explaining WHAT it is and WHY it matters. Never use "-- related concept".
- Key Insights: Extract 5+ specific insights with data, quotes, numbers, or actionable takeaways. Each insight must be a complete sentence.
- Open Questions: Write 2-3 questions specific to THIS article's content. Reference concepts from the note.
- Every section must have substantive content. No empty sections.
```

3. Write the improved note, overwriting the old one
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
