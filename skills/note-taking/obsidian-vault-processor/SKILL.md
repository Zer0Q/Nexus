---
name: obsidian-vault-processor
description: "Processes raw articles into a compressed, interconnected Obsidian knowledge vault following Karpathy's atomic note-taking philosophy."
---
## Overview

Processes raw articles into a compressed, interconnected knowledge vault following Andrej Karpathy's note-taking philosophy: dense knowledge over verbose explanations, atomic notes over large documents, semantic links over hierarchical folders.

**Canonical in-repo copy:** `skills/note-taking/obsidian-vault-processor/SKILL.md` in the Nexus GitHub repo. Keep both copies in sync — edit the in-repo version and replicate changes here.

## Trigger
- User drops articles into the `raw/` folder
- User asks to process new content
- User says "process the vault", "ingest notes", "build second brain"

## Vault Structure
```
vault/
  concepts/       -- atomic technical concepts (one idea per note)
  frameworks/     -- reusable workflow abstractions and mental models
  tools/          -- specific software, plugins, APIs, hardware
  architectures/  -- system design patterns
  workflows/      -- procedural pipelines and step-by-step workflows
  glossary/       -- quick-reference term definitions
  source_notes/   -- one note per source, tied to a specific article
  indexes/        -- index notes mapping related concepts
  raw/            -- incoming unprocessed articles
```

## Processing Flow

### Step 0: Scan existing vault (duplicate prevention)
Before creating any new notes, scan the existing vault to prevent duplicates:
```python
import os
vault = "path_to_vault"
existing = {}
for folder in ["concepts", "frameworks", "tools", "architectures", "workflows", "glossary"]:
    path = os.path.join(vault, folder)
    if os.path.isdir(path):
        for f in os.listdir(path):
            if f.endswith('.md'):
                existing[f[:-3].lower()] = os.path.join(folder, f)
# Print for reference
for k, v in sorted(existing.items()):
    print(f"  {v}")
```
When extracting concepts from a new article, compare against this list. If a concept already exists (exact match or semantic overlap), UPDATE the existing note with new insights instead of creating a duplicate.

### Step 1: Scan raw/ for new articles
```
search_files(pattern="*.md", target="files", path="vault/raw")
```
If empty, report "No new articles to process." and stop.

### Step 2: Read each article
```
read_file(path="vault/raw/<filename>.md")
```
Read ALL articles in raw/. If an article is very long (>500 lines), read in chunks with offset/limit.

### Step 3: Create source note per article
For each article, create `source_notes/<Author>-<Short-Topic>.md`:
```markdown
---
title: "<original title>"
source: "<url or source>"
author: "<author handle>"
published: "<date>"
type: article
---

# <Short Title>

## Summary
Compressed 2-3 sentence summary.

## Core Concepts
- [[Concept A]] -- one-line description
- [[Concept B]] -- one-line description

## Key Insights
- insight 1
- insight 2

## Open Questions
- question 1
```

**Wikilink validation in source notes:** Only create `[[wikilinks]]` for concepts that:
- Will have a corresponding note created (in this batch or already exist)
- Are NOT template placeholders (e.g., `[[topic-name]]`)
- Are NOT author names, team names, or organizational entities masquerading as concepts
- Appear in at least 2 different articles (cross-article reuse threshold)

### Step 4: Extract atomic knowledge notes
For each article, extract 10-25 atomic notes. Each note represents ONE idea and follows this structure:

**File naming:** `Folder/Concept-Name.md` (kebab-case, no accents, no spaces, NO dots except the final `.md` extension, max 64 chars). If a tool name contains a dot (e.g., `CLAUDE.md`), replace it with `-MD-` (e.g., `CLAUDE-MD-Project-Knowledge.md`).

**Wikilink rule:** `[[wikilinks]]` must match the EXACT filename (without `.md`). Example: `[[Concept-Name]]` points to `Concept-Name.md`. Never use spaces, accents, or dots inside `[[...]]`.

**Template:**
```markdown
# Concept Name

## Definition
Short compressed explanation.

## Why It Matters
Why this concept is important.

## Key Ideas
- point
- point
- point

## Tradeoffs
Optional. List tradeoffs if relevant.

## Related
- [[Related Concept]]
- [[Another Concept]]

## Source
[[Source-Note-Name]]
```

**Folder placement rules:**
- `concepts/` -- technical concepts, principles, ideas
- `frameworks/` -- reusable workflows, mental models, methodologies
- `tools/` -- specific software, plugins, APIs, hardware
- `architectures/` -- system design patterns, infrastructure
- `workflows/` -- step-by-step procedures, pipelines

**Atomic note rules:**
- ONE single idea per note
- Should fit on one screen if possible
- Avoid long prose, avoid generic explanations
- High signal density
- DO NOT duplicate concepts across notes -- merge overlapping ideas
- DO NOT create notes for terms that appear only once in a single article
- **Cross-article reuse threshold:** Only create a standalone note if the concept appears meaningfully in 2+ articles OR is a foundational concept (e.g., RAG, LLM, embeddings)
- Prefer fewer high-quality notes over many shallow ones

### Step 5: Create glossary entries
For each key technical term used across multiple notes, create a glossary entry:
```markdown
# Term Name

One-sentence definition.

- key fact 1
- key fact 2
- key fact 3

See also: [[Related Note]], [[Another Note]]
```

### Step 6: Create index notes
Create index notes that map related concepts. One index per important thematic cluster:
```markdown
# Topic Index

## Overview
One-line description.

## Core Concepts
- [[Concept A]] -- description
- [[Concept B]] -- description

## Frameworks
- [[Framework A]] -- description

## Tools
- [[Tool A]] -- description

## Glossary
- [[Term A]]

## Sources
- [[Source-Note]]
```

### Step 7: Normalize wikilinks
Before verifying, run a normalization script that fixes all `[[wikilinks]]` to match actual filenames. The script must:
1. Collect all `.md` files in the vault and build a normalized map (strip accents, lowercase, spaces->hyphens)
2. Walk each file and replace `[[link]]` with the correct name
3. Report unresolved links

```python
import os, re, unicodedata
vault = "path_to_vault"
def norm(n):
    # Strip ONLY the final .md extension (not all .md occurrences)
    if n.endswith('.md'):
        n = n[:-3]
    nfkd = unicodedata.normalize('NFKD', n)
    return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower().replace(' ','-').replace('_','-')
fmap = {}
for r,_,fs in os.walk(vault):
    for f in fs:
        if f.endswith('.md'):
            fmap[norm(f)] = f[:-3]
fixed = 0
for r,_,fs in os.walk(vault):
    for f in fs:
        if not f.endswith('.md'): continue
        p = os.path.join(r,f)
        with open(p) as fh: content = fh.read()
        def fix(m):
            nonlocal fixed
            lk = m.group(1).split('|')[0]
            if norm(lk) in fmap and lk != fmap[norm(lk)]:
                fixed += 1
                return '[[{0}]]'.format(fmap[norm(lk)])
            return m.group(0)
        nc = re.sub(r'\[\[([^\]]+)\]\]', fix, content)
        if nc != content:
            with open(p,'w') as fh: fh.write(nc)
print(f"Normalized: {fixed} links")
```

### Step 8: Verify cross-link coherence
Run a Python script to verify all `[[wikilinks]]` resolve to existing files:
```python
import os, re, unicodedata
vault = "path_to_vault"
def norm(n):
    if n.endswith('.md'):
        n = n[:-3]
    nfkd = unicodedata.normalize('NFKD', n)
    return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower().replace(' ','-').replace('_','-')
existing = {}
for r,_,fs in os.walk(vault):
    if '.obsidian' in r or '/raw/' in r: continue
    for f in fs:
        if f.endswith('.md'):
            existing[norm(f)] = f[:-3]
broken = []
for r,_,fs in os.walk(vault):
    if '.obsidian' in r or '/raw/' in r: continue
    for f in fs:
        if not f.endswith('.md'): continue
        with open(os.path.join(r,f)) as fh:
            for link in re.findall(r'\[\[([^\]]+)\]\]', fh.read()):
                target = link.split('|')[0].strip()
                # Skip external refs: @mentions, URLs, email addresses
                if not target or target.startswith('@') or target.startswith('http') or target.startswith('mailto:'):
                    continue
                if norm(target) not in existing:
                    broken.append((f, target))
if broken:
    print(f"BROKEN ({len(broken)}): {broken}")
else:
    print("All links coherent.")
```

### Step 9: Triage broken links
When broken links are found, classify each one and apply the appropriate fix:

**Category A: Reusable concept (appears in 2+ source notes)**
- Create the missing note. This is a concept that transcends a single article.

**Category B: Single-use reference (appears in only 1 source note)**
- Remove the `[[wikilink]]` wrapper and leave the text as plain text.
- Example: `[[Human-AI-Orchestration]]` -> `Human-AI-Orchestration`
- The concept is worth mentioning but not worth a standalone note.

**Category C: Placeholder or false reference**
- Template placeholders: `[[topic-name]]`, `[[your-topic]]`
- Author/team names: `[[Open-source Projects Team]]`, `[[Author Name]]`
- Remove the `[[wikilink]]` wrapper entirely.

**Triage script:**
```python
import os, re, collections
vault = "path_to_vault"
# Count how many files reference each broken target
broken_counts = collections.Counter()
broken_sources = collections.defaultdict(list)
for r,_,fs in os.walk(vault):
    if '.obsidian' in r or '/raw/' in r: continue
    for f in fs:
        if not f.endswith('.md'): continue
        with open(os.path.join(r,f)) as fh:
            for link in re.findall(r'\[\[([^\]]+)\]\]', fh.read()):
                target = link.split('|')[0].strip()
                if target and not target.startswith('@') and not target.startswith('http'):
                    broken_counts[target] += 1
                    broken_sources[target].append(f)

# Classify
reusable = {k:v for k,v in broken_counts.items() if v >= 2}  # Create note
single_use = {k:v for k,v in broken_counts.items() if v == 1}  # Remove [[ ]]
placeholders = {k for k in broken_counts if k.lower() in ['topic-name', 'your-topic', 'insert-topic']}

print(f"CREATE NOTES ({len(reusable)}): {dict(reusable)}")
print(f"REMOVE LINKS ({len(single_use)}): {dict(single_use)}")
print(f"PLACEHOLDERS ({len(placeholders)}): {placeholders}")
```

### Step 10: Clean raw/
After successful processing and zero broken links, delete processed articles from `raw/`.

## Maintenance (periodic)

Run these checks every 10-15 new articles processed:

### Orphan detection
Find notes that are not referenced by any other note:
```python
import os, re
vault = "path_to_vault"
all_notes = set()
referenced = set()
for r,_,fs in os.walk(vault):
    if '.obsidian' in r or '/raw/' in r: continue
    for f in fs:
        if f.endswith('.md'):
            all_notes.add(f[:-3])
            with open(os.path.join(r,f)) as fh:
                for link in re.findall(r'\[\[([^\]]+)\]\]', fh.read()):
                    target = link.split('|')[0]
                    referenced.add(target)
orphans = all_notes - referenced - {'AI-Vault-Integration-Index', 'Knowledge-Management-Index',
    'Local-AI-Index', 'Research-Workflow-Index'}  # indexes are entry points
if orphans:
    print(f"ORPHANS ({len(orphans)}): {sorted(orphans)}")
else:
    print("No orphans.")
```
Orphaned notes are not necessarily bad — they may be leaf concepts. But if a note has been orphaned for multiple processing cycles, consider whether it should be merged into a parent concept or removed.

## Key Principles
- **Dense over verbose** -- compress knowledge, don't summarize
- **Atomic over large** -- one idea per note
- **Reusable over specific** -- extract abstractions, not course summaries
- **Linked over archived** -- semantic wikilinks beat folder hierarchies
- **Signal over completeness** -- prefer fewer high-quality notes
- **Merge overlapping concepts** -- no duplication
- **Every note provides standalone value** -- a reader must understand the note without reading anything else
- **Growth is controlled** -- every new note must justify its existence through reuse or foundational importance

## Pitfalls
- DO NOT generate giant summaries -- source notes must be compact
- DO NOT create notes for terms that appear only once in a single article
- DO NOT overuse tags -- wikilinks are the primary connection mechanism
- DO NOT create generic AI-fluff notes -- every note must have technical specificity
- DO NOT skip the wikilink normalization step (Step 7)
- DO NOT skip the cross-link verification step (Step 8)
- DO NOT skip the broken link triage (Step 9) — this is where sustainability is enforced
- `[[wikilinks]]` must use EXACTLY the filename: kebab-case, no accents, no spaces
- **NEVER use dots in filenames** (except the final `.md` extension). A file named `CLAUDE.md-Project-Knowledge.md` will break the normalization script because `n.replace('.md','')` strips ALL `.md` occurrences. Use `CLAUDE-MD-Project-Knowledge.md` instead.
- If two articles cover the same concept, UPDATE the existing note instead of creating a duplicate
- Source notes should reference concepts, not contain complete explanations
- Glossary entries should be quick reference, not full notes
- **Do not create notes for broken links automatically** — triage first (Step 9). A broken link from a single article does not justify a new note.
