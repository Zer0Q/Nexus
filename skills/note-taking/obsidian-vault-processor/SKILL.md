---
name: obsidian-vault-processor
description: "Processes raw articles into the Nexus Obsidian vault knowledge model: immutable raw notes, compressed summaries, reusable concepts/tools, and folder-qualified wikilinks."
---

## Overview

Processes raw articles into the Nexus knowledge vault described in `README.md`: dense reusable knowledge, immutable originals, compressed summaries, semantic wikilinks, and controlled note growth.

**Canonical in-repo copy:** `skills/note-taking/obsidian-vault-processor/SKILL.md` in the Nexus GitHub repo. Keep both copies in sync by editing the in-repo version first.

## Trigger

- User drops articles into `Nexus/raw/`
- User asks to process new content
- User says "process the vault", "ingest notes", "build second brain"

## Vault Structure

```text
Nexus/
  concepts/       -- atomic ideas, principles, definitions, patterns, and procedures
  tools/          -- specific tools, platforms, libraries, plugins, APIs, hardware, and methodologies
  summaries/      -- compressed summaries of original sources with wikilinks
  raw-notes/      -- immutable copies of original raw articles
  indexes/        -- thematic maps across related notes
  raw/            -- temporary inbox for unprocessed markdown
```

## Processing Flow

### Step 0: Scan existing vault

Before creating any note, scan existing `concepts/`, `tools/`, `summaries/`, and `indexes/` to prevent duplicates and learn current naming/linking conventions.

```python
import os

vault = "Nexus"
knowledge_dirs = ["concepts", "tools", "summaries", "indexes"]
existing = {}
convention_issues = []

for folder in knowledge_dirs:
    path = os.path.join(vault, folder)
    if not os.path.isdir(path):
        continue
    for f in os.listdir(path):
        if not f.endswith(".md"):
            continue
        stem = f[:-3]
        existing[stem.lower()] = os.path.join(folder, f)
        if " " in f or "_" in f or any(c in "áéíóúñÁÉÍÓÚÑ" for c in f):
            convention_issues.append(os.path.join(folder, f))

for _, rel in sorted(existing.items()):
    print(f"  {rel}")

if convention_issues:
    print(f"\nCONVENTION ISSUES ({len(convention_issues)} files):")
    for issue in convention_issues:
        print(f"  {issue}")
else:
    print("\nPASS: all scanned filenames follow Nexus naming conventions")
```

When extracting concepts from a new article, compare against this list. If a concept/tool already exists by exact match or semantic overlap, update the existing note with new insights instead of creating a duplicate.

### Step 1: Scan raw/ for new articles

```text
search_files(pattern="*.md", target="files", path="Nexus/raw")
```

If empty, report "No new articles to process." and stop.

### Step 2: Read each article

```text
read_file(path="Nexus/raw/<filename>.md")
```

Read all articles in `raw/`. If an article is very long, read it in chunks with offset/limit.

### Step 3: Preserve raw articles and create summaries

For each article:

1. Copy the raw article unchanged to `raw-notes/<normalized-original-filename>.md`.
2. Create one compressed summary in `summaries/<Author>-<Short-Topic>.md`.
3. Link the summary to its raw copy with `[[raw-notes/<normalized-original-filename>]]`.
4. Link concepts/tools from the summary using folder-qualified wikilinks.
5. Link concepts/tools back to the summary in their `## Source` section.

Do not modify the copied raw note. The processed layer is the summary and the reusable notes.

Summary template:

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
- [[concepts/Knowledge-Graph]] -- one-line description
- [[tools/Obsidian]] -- one-line description

## Key Insights
- insight 1
- insight 2

## Open Questions
- question 1

## Source
[[raw-notes/original-article-filename]]
```

Every bullet in `## Core Concepts` must be a folder-qualified `[[wikilink]]`. Only link notes that exist or will be created in this batch.

### Step 4: Create or update reusable notes adaptively

Create standalone notes only when the concept or tool:

- appears meaningfully in 2+ sources,
- is foundational to the vault's knowledge model, or
- connects or clarifies an existing cluster.

Prefer updating existing notes over creating new ones. Do not target a fixed number of notes per article. Prefer fewer high-quality notes over many shallow notes.

Atomic note template:

```markdown
# Knowledge Graph

## Definition
Short compressed explanation.

## Why It Matters
Why this concept is important.

## Key Ideas
- point
- point
- point

## Tradeoffs
Optional tradeoffs.

## Related
- [[concepts/Semantic-Similarity]]
- [[concepts/Entity-Resolution]]

## Source
[[summaries/Author-Topic]]
```

Folder placement rules:

- `concepts/` for reusable ideas, principles, definitions, system patterns, and procedures.
- `tools/` for named software, platforms, libraries, plugins, APIs, hardware, and methodologies.
- `indexes/` for thematic maps across clusters.

### Step 5: Create or update index notes

Create or update index notes when a batch introduces or expands an important thematic cluster.

```markdown
# Knowledge Systems Index

## Overview
One-line description.

## Core Concepts
- [[concepts/Knowledge-Graph]] -- description
- [[concepts/Semantic-Similarity]] -- description

## Tools
- [[tools/Obsidian]] -- description

## Sources
- [[summaries/Author-Topic]]
```

## Naming and Wikilink Rules

Filenames:

- Use hyphenated filenames.
- Do not use spaces.
- Do not use underscores.
- Do not use accents or diacritics.
- Do not use dots except the final `.md` extension.
- Keep names stable and reusable, not source-specific.

Wikilinks:

- Always include the folder path.
- Match the exact filename stem.
- Use hyphens, no spaces, no underscores, no accents.
- Preserve filename case.

Good examples:

- `[[concepts/Knowledge-Graph]]`
- `[[concepts/Agent-Swarm-Architecture]]`
- `[[tools/CLAUDE-MD-Project-Knowledge]]`
- `[[summaries/AddyOsmani-Agent-Harness-Engineering]]`
- `[[raw-notes/building-effective-ai-agents]]`

Invalid patterns:

- Bare links without folder paths.
- Links containing spaces.
- Links containing underscores.
- Links containing accents or diacritics.
- Links containing dots inside the filename stem.

## Validation Flow

Run validation in this order:

1. Normalize filenames and wikilinks.
2. Verify link resolution and source connectivity.
3. Detect plain-text references.
4. Produce validation report.

All operations that rename, delete, unwrap, merge, or otherwise remove information must support an explicit dry-run phase before an apply phase.

### Step 6: Normalize filenames and wikilinks

Dry-run first:

```python
import os, re, unicodedata

vault = "Nexus"
SKIP_DIRS = {".obsidian", "raw"}

def strip_accents(text):
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

def normalize_stem(stem):
    stem = strip_accents(stem)
    stem = stem.replace(" ", "-").replace("_", "-").replace(".", "-")
    stem = re.sub(r"-+", "-", stem).strip("-")
    return stem

def should_skip(root):
    parts = set(os.path.normpath(root).split(os.sep))
    return bool(parts & SKIP_DIRS)

renames = []
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if should_skip(root):
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        stem = f[:-3]
        normalized = normalize_stem(stem)
        if normalized != stem:
            old = os.path.join(root, f)
            new = os.path.join(root, normalized + ".md")
            renames.append((old, new))

print("DRY RUN: filename renames")
for old, new in renames:
    print(f"  {os.path.relpath(old, vault)} -> {os.path.relpath(new, vault)}")
```

Apply only after reviewing the dry-run output:

```python
APPLY = False

if APPLY:
    for old, new in renames:
        if os.path.exists(new):
            print(f"SKIP collision: {old} -> {new}")
            continue
        os.rename(old, new)
```

After filename normalization, normalize wikilinks to actual folder-qualified paths. Run dry-run first, then set `APPLY = True` only after reviewing the replacement list.

```python
import os, re, unicodedata

vault = "Nexus"
APPLY = False
SKIP_DIRS = {".obsidian", "raw"}

def norm(value):
    value = value[:-3] if value.endswith(".md") else value
    nfkd = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in nfkd if not unicodedata.combining(c))
    return value.lower().replace(" ", "-").replace("_", "-")

def should_skip(root):
    parts = set(os.path.normpath(root).split(os.sep))
    return bool(parts & SKIP_DIRS)

by_path = {}
by_name = {}
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if should_skip(root):
        continue
    for f in files:
        if f.endswith(".md"):
            rel = os.path.relpath(os.path.join(root, f), vault)[:-3].replace(os.sep, "/")
            by_path[norm(rel)] = rel
            by_name[norm(os.path.basename(rel))] = rel

changes = []
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if should_skip(root):
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        with open(path, encoding="utf-8") as fh:
            content = fh.read()

        replacements = []
        def fix(match):
            raw = match.group(1)
            target, suffix = raw, ""
            if "|" in target:
                target, label = target.split("|", 1)
                suffix = "|" + label
            if "#" in target:
                target, anchor = target.split("#", 1)
                suffix = "#" + anchor + suffix
            target = target.strip()
            key_path = norm(target)
            key_name = norm(os.path.basename(target))
            resolved = by_path.get(key_path) or by_name.get(key_name)
            if not resolved:
                return match.group(0)
            new_link = f"[[{resolved}{suffix}]]"
            if new_link != match.group(0):
                replacements.append((match.group(0), new_link))
            return new_link

        new_content = re.sub(r"\[\[([^\]]+)\]\]", fix, content)
        if replacements:
            changes.append((path, replacements, content, new_content))

print("DRY RUN: wikilink replacements")
for path, replacements, _, _ in changes:
    rel = os.path.relpath(path, vault)
    for old, new in replacements:
        print(f"  {rel}: {old} -> {new}")

if APPLY:
    for path, _, _, new_content in changes:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_content)
```

### Step 7: Verify link resolution and source connectivity

Verify all `[[wikilinks]]` resolve to existing files and every summary links to its raw note. Also verify concepts/tools link back to summaries rather than raw notes.

```python
import os, re, unicodedata

vault = "Nexus"
SKIP_DIRS = {".obsidian", "raw"}

def norm(value):
    value = value[:-3] if value.endswith(".md") else value
    nfkd = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in nfkd if not unicodedata.combining(c))
    return value.lower().replace(" ", "-").replace("_", "-")

def should_skip(root):
    parts = set(os.path.normpath(root).split(os.sep))
    return bool(parts & SKIP_DIRS)

existing_by_path = {}
existing_by_name = {}
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if should_skip(root):
        continue
    for f in files:
        if f.endswith(".md"):
            rel = os.path.relpath(os.path.join(root, f), vault)[:-3].replace(os.sep, "/")
            existing_by_path[norm(rel)] = rel
            existing_by_name[norm(os.path.basename(rel))] = rel

broken = []
bare_links = []
wrong_folder = []
summary_without_raw = []
knowledge_without_summary = []

for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if should_skip(root):
        continue
    folder = os.path.basename(root)
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        rel_file = os.path.relpath(path, vault).replace(os.sep, "/")
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        links = []
        for raw in re.findall(r"\[\[([^\]]+)\]\]", content):
            target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            if not target or target.startswith("http") or target.startswith("mailto:"):
                continue
            links.append(target)
            if "/" not in target:
                bare_links.append((rel_file, target))
            if norm(target) in existing_by_path:
                actual = existing_by_path[norm(target)]
                if target != actual:
                    wrong_folder.append((rel_file, target, actual))
            elif norm(os.path.basename(target)) in existing_by_name:
                actual = existing_by_name[norm(os.path.basename(target))]
                wrong_folder.append((rel_file, target, actual))
            else:
                broken.append((rel_file, target))

        if folder == "summaries" and not any(link.startswith("raw-notes/") for link in links):
            summary_without_raw.append(rel_file)
        if folder in {"concepts", "tools"} and not any(link.startswith("summaries/") for link in links):
            knowledge_without_summary.append(rel_file)

print(f"BROKEN LINKS: {len(broken)}")
for item in broken:
    print(f"  {item[0]} -> [[{item[1]}]]")
print(f"BARE LINKS: {len(bare_links)}")
for item in bare_links:
    print(f"  {item[0]} -> [[{item[1]}]]")
print(f"WRONG FOLDER LINKS: {len(wrong_folder)}")
for src, bad, good in wrong_folder:
    print(f"  {src}: [[{bad}]] -> [[{good}]]")
print(f"SUMMARIES WITHOUT RAW-NOTES LINK: {len(summary_without_raw)}")
for item in summary_without_raw:
    print(f"  {item}")
print(f"CONCEPTS/TOOLS WITHOUT SUMMARY LINK: {len(knowledge_without_summary)}")
for item in knowledge_without_summary:
    print(f"  {item}")
```

### Step 8: Detect plain-text references

Scan structured relationship sections for references that look like note names but are not wrapped in `[[ ]]`.

```python
import os, re

vault = "Nexus"
SKIP_DIRS = {".obsidian", "raw", "raw-notes"}
section_names = {"Related", "Core Concepts", "Tools", "Sources", "Source"}
plain_refs = []
heading = None

def should_skip(root):
    parts = set(os.path.normpath(root).split(os.sep))
    return bool(parts & SKIP_DIRS)

candidate = re.compile(r"^- ([A-Z][A-Za-z0-9]+(?:-[A-Z0-9][A-Za-z0-9]+)+)(?:\s|$)")

for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if should_skip(root):
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(root, f), vault)
        heading = None
        with open(os.path.join(root, f), encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, 1):
                line = line.rstrip("\n")
                m_heading = re.match(r"^##\s+(.+)$", line)
                if m_heading:
                    heading = m_heading.group(1).strip()
                    continue
                if heading not in section_names:
                    continue
                if "[[" in line:
                    continue
                m = candidate.match(line.strip())
                if m:
                    plain_refs.append((rel, line_no, m.group(1)))

print(f"PLAIN TEXT REFERENCES: {len(plain_refs)}")
for rel, line_no, text in plain_refs:
    print(f"  {rel}:{line_no} -> {text}")
```

### Step 9: Produce validation report

Summarize the validation result before any destructive apply phase:

```text
Validation report:
- Filename normalization pending: <count>
- Wikilink normalization pending: <count>
- Broken links: <count>
- Bare links: <count>
- Wrong-folder links: <count>
- Summaries without raw-notes link: <count>
- Concepts/tools without summary link: <count>
- Plain-text references: <count>
- Raw files eligible for cleanup: yes/no
- Destructive actions proposed: <list>
```

## Destructive Operations Policy

The following operations must always be split into explicit dry-run and apply phases:

- Rename files.
- Delete processed files from `raw/`.
- Unwrap wikilinks for single-use or false references.
- Merge orphan notes.
- Delete orphan notes or stale duplicate notes.

Dry-run output must list exact file paths and replacements/deletions. Apply only when the dry-run report is clean and the user has asked to proceed.

### Broken link triage

When broken links are found, classify each one:

- **Reusable concept/tool:** Appears in 2+ sources, is foundational, or connects a cluster. Create the missing note or update an existing overlapping note.
- **Single-use reference:** Appears in only 1 source and is not foundational. Dry-run unwrapping `[[concepts/Trade-Capture-System]]` to `Trade Capture System`.
- **Placeholder or false reference:** Template placeholder, author name, team name, or organization. Dry-run removal or unwrapping.
- **Wrong folder path:** File exists but link points elsewhere. Normalize to the actual folder-qualified path.

### Raw cleanup

Only delete processed files from `raw/` after:

- filename and wikilink normalization has been applied,
- all wikilinks resolve,
- no bare or wrong-folder links remain,
- every summary links to `raw-notes/`,
- every new concept/tool links to `summaries/`,
- no plain-text references remain in structured relationship sections, and
- the validation report lists the exact raw files to delete.

Deletion must be dry-run first:

```python
processed_raw_files = [
    "Nexus/raw/example-article.md",
]

print("DRY RUN: raw files to delete")
for path in processed_raw_files:
    print(f"  DELETE {path}")

APPLY = False
if APPLY:
    for path in processed_raw_files:
        os.remove(path)
```

## Maintenance

Run these checks every 10-15 processed articles.

### Filename convention audit

```python
import os

vault = "Nexus"
bad = []
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in {".obsidian", "raw"}]
    if ".obsidian" in root.split(os.sep) or "raw" in root.split(os.sep):
        continue
    for f in files:
        if f.endswith(".md") and (" " in f or "_" in f or any(c in "áéíóúñÁÉÍÓÚÑ" for c in f)):
            bad.append(os.path.join(os.path.relpath(root, vault), f))

if bad:
    print(f"FAIL: {len(bad)} files violate naming convention:")
    for item in bad:
        print(f"  {item}")
else:
    print("PASS: all filenames use hyphens, no accents, no spaces, no underscores")
```

### Orphan detection

Find notes that are not referenced by any other note. Orphans are not always bad, but persistent orphans should be reviewed.

```python
import os, re

vault = "Nexus"
SKIP_DIRS = {".obsidian", "raw", "raw-notes"}
all_notes = set()
referenced = set()
index_notes = set()

for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    if set(os.path.normpath(root).split(os.sep)) & SKIP_DIRS:
        continue
    folder = os.path.basename(root)
    for f in files:
        if not f.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(root, f), vault)[:-3].replace(os.sep, "/")
        all_notes.add(rel)
        if folder == "indexes":
            index_notes.add(rel)
        with open(os.path.join(root, f), encoding="utf-8") as fh:
            for link in re.findall(r"\[\[([^\]]+)\]\]", fh.read()):
                target = link.split("|", 1)[0].split("#", 1)[0].strip()
                referenced.add(target)

orphans = all_notes - referenced - index_notes
print(f"ORPHANS: {len(orphans)}")
for item in sorted(orphans):
    print(f"  {item}")
```

Orphan resolution must be dry-run first:

- Add missing links from related notes or indexes.
- Merge content into a broader note when the orphan overlaps an existing concept/tool.
- Delete only stale duplicates or notes that clearly fail the knowledge model.

### Index consolidation

After every 15-20 new articles, audit indexes:

- List all indexes with link counts.
- Detect overlapping indexes that share 3+ concepts/tools.
- Merge small indexes only after a dry-run report.
- Keep `indexes/Vault-Index.md` as the map of maps.
- Remove stale entries caught by link validation.

## Key Principles

- **Dense over verbose:** compress knowledge, do not archive everything.
- **Atomic over large:** one reusable idea per note.
- **Reusable over specific:** extract abstractions, not article-shaped notes.
- **Linked over archived:** semantic wikilinks beat folder hierarchy.
- **Signal over completeness:** prefer fewer high-quality notes.
- **Merge overlapping concepts:** no duplicate notes for the same idea.
- **Source traceability:** concepts/tools link to summaries; summaries link to raw-notes.
- **Immutable originals:** raw articles copied to `raw-notes/` are never modified.
- **Controlled growth:** every new note must justify itself through reuse, foundation, or cluster connectivity.

## Pitfalls

- Do not create a standalone note just because a term appears in one article.
- Do not create notes automatically from broken links; triage first.
- Do not write bare wikilinks; use folder-qualified links such as `[[concepts/Knowledge-Graph]]`.
- Do not write plain-text references in `## Related`, `## Core Concepts`, `## Sources`, or `## Source`.
- Do not modify copied files in `raw-notes/`.
- Do not delete `raw/` files until validation passes and deletion has been dry-run.
- Do not use spaces, underscores, accents, or dots in filenames or wikilinks.
- Do not shorten summary links; use the full folder-qualified filename stem, such as `[[summaries/AddyOsmani-Agent-Harness-Engineering]]`.
