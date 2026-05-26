---
name: obsidian-vault-processor
description: "Processes raw articles into a compressed, interconnected Obsidian knowledge vault following Karpathy's atomic note-taking philosophy."
version: 1.0.0
author: Nexus
license: MIT
metadata:
  hermes:
    tags: [obsidian, knowledge-vault, atomic-notes, karpathy, second-brain]
    related_skills: []
---

# Obsidian Vault Processor

## Overview

Processes raw articles into a compressed, interconnected knowledge vault following Andrej Karpathy's note-taking philosophy: dense knowledge over verbose explanations, atomic notes over large documents, semantic links over hierarchical folders.

## When to Use
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

### Step 4: Extract atomic knowledge notes
For each article, extract 10-25 atomic notes. Each note represents ONE idea and follows this structure:

**File naming:** `Folder/Concept-Name.md` (kebab-case, no accents, no spaces, max 64 chars)

**Wikilink rule:** `[[wikilinks]]` must match the EXACT filename (without `.md`). Example: `[[Concept-Name]]` points to `Concept-Name.md`. Never use spaces or accents inside `[[...]]`.

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
- DO NOT create notes for terms that appear only once
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
    n = n.replace('.md','')
    nfkd = unicodedata.normalize('NFKD', n)
    return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower().replace(' ','-').replace('_','-')
fmap = {}
for r,_,fs in os.walk(vault):
    for f in fs:
        if f.endswith('.md'):
            fmap[norm(f)] = f.replace('.md','')
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
    n = n.replace('.md','')
    nfkd = unicodedata.normalize('NFKD', n)
    return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower().replace(' ','-').replace('_','-')
existing = {}
for r,_,fs in os.walk(vault):
    if '.obsidian' in r or '/raw/' in r: continue
    for f in fs:
        if f.endswith('.md'):
            existing[norm(f)] = f.replace('.md','')
broken = []
for r,_,fs in os.walk(vault):
    if '.obsidian' in r or '/raw/' in r: continue
    for f in fs:
        if not f.endswith('.md'): continue
        with open(os.path.join(r,f)) as fh:
            for link in re.findall(r'\[\[([^\]]+)\]\]', fh.read()):
                target = link.split('|')[0].strip()
                if target and norm(target) not in existing:
                    broken.append((f, target))
if broken:
    print(f"BROKEN ({len(broken)}): {broken}")
else:
    print("All links coherent.")
```
If broken links exist, create missing notes or fix references.

### Step 9: Clean raw/
After successful processing, delete processed articles from `raw/`.

## Key Principles
- **Dense over verbose** -- compress knowledge, don't summarize
- **Atomic over large** -- one idea per note
- **Reusable over specific** -- extract abstractions, not course summaries
- **Linked over archived** -- semantic wikilinks beat folder hierarchies
- **Signal over completeness** -- prefer fewer high-quality notes
- **Merge overlapping concepts** -- no duplication
- **Every note provides standalone value** -- a reader must understand the note without reading anything else

## Common Pitfalls
1. DO NOT generate giant summaries -- source notes must be compact
2. DO NOT create notes for terms that appear only once
3. DO NOT overuse tags -- wikilinks are the primary connection mechanism
4. DO NOT create generic AI-fluff notes -- every note must have technical specificity
5. DO NOT skip the wikilink normalization step (Step 7)
6. DO NOT skip the cross-link verification step
7. `[[wikilinks]]` must use EXACTLY the filename: kebab-case, no accents, no spaces
8. If two articles cover the same concept, UPDATE the existing note instead of creating a duplicate
9. Source notes should reference concepts, not contain complete explanations
10. Glossary entries should be quick reference, not full notes

## Verification Checklist
- [ ] Source note created in `source_notes/`
- [ ] Atomic notes created in appropriate folders
- [ ] Wikilinks normalized (Step 7)
- [ ] Cross-link verification passed (Step 8)
- [ ] Raw article cleaned (Step 9)
