#!/usr/bin/env python3
"""
OKF v0.1 Normalization Script for Nexus vault
- Adds YAML frontmatter to files without it
- Renames source→resource, published→timestamp
- Adds description and tags where possible
- Updates README.md with OKF reference
- Creates index.md files per directory
"""

import os
import re
import yaml
from datetime import datetime, timezone

VAULT = "/home/zeroq/projects/Nexus/Nexus"
README = "/home/zeroq/projects/Nexus/README.md"

# Type mapping by directory
TYPE_MAP = {
    "concepts": "Concept",
    "indexes": "Index",
    "summaries": "Article",
    "tools": "Tool",
}

# Directory mapping for relative paths
DIR_TO_TYPE = {
    "concepts": "Concept",
    "indexes": "Index",
    "summaries": "Article",
    "tools": "Tool",
}

# Skip directories
SKIP_DIRS = {".obsidian", "raw", "raw-notes"}


def in_dir(r, name):
    return os.path.basename(r) == name


def derive_type(rel_path):
    """Derive OKF type from directory."""
    dirname = os.path.dirname(rel_path)
    # Check direct directory
    for d, t in TYPE_MAP.items():
        if dirname == d or dirname.endswith("/" + d):
            return t
    return "Reference"


def extract_title_from_content(content):
    """Extract title from content (first # heading or filename)."""
    # Try first H1
    h1 = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1:
        return h1.group(1).strip()
    return None


def extract_description_from_content(content):
    """Extract a short description from content."""
    # Look for ## Definition or ## Summary or first paragraph
    for pattern in [
        r'##\s+(?:Definition|Summary|Descripción)\s*\n\s*(.+?)(?:\n\s*\n|\n\s*##|\Z)',
        r'^#\s+.+\n\s*\n\s*(.+?)(?:\n\s*\n|\n\s*##)',
    ]:
        m = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if m:
            desc = m.group(1).strip().replace('\n', ' ')
            # Truncate to ~160 chars
            if len(desc) > 160:
                desc = desc[:157] + "..."
            return desc
    return None


def add_frontmatter_to_file(filepath, rel_path, fm_type):
    """Add frontmatter to a file that doesn't have one."""
    with open(filepath) as f:
        content = f.read()

    # Derive metadata
    title = extract_title_from_content(content)
    if not title:
        # Use filename stem
        fname = os.path.basename(filepath)
        title = fname.replace('.md', '').replace('-', ' ').title()

    description = extract_description_from_content(content)
    if not description:
        description = f"Atomic note about {title.lower()}."

    # Generate tags from directory
    dirname = os.path.dirname(rel_path)
    tags = [dirname] if dirname else []

    # Current timestamp
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Build frontmatter
    fm = {
        'type': fm_type,
        'title': title,
        'description': description,
        'tags': tags,
        'timestamp': timestamp,
    }

    # Write frontmatter
    fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f"---\n{fm_str}---\n\n{content}"

    with open(filepath, 'w') as f:
        f.write(new_content)

    return True


def normalize_existing_frontmatter(filepath, rel_path):
    """Rename fields and add missing ones to existing frontmatter."""
    with open(filepath) as f:
        content = f.read()

    # Parse frontmatter
    fm_end = content.index('---', 3)
    fm_str = content[3:fm_end]
    fm = yaml.safe_load(fm_str)

    if not fm:
        return False

    changed = False

    # Rename source → resource
    if 'source' in fm and 'resource' not in fm:
        fm['resource'] = fm.pop('source')
        changed = True

    # Rename published → timestamp
    if 'published' in fm and 'timestamp' not in fm:
        # Convert to ISO 8601 if needed
        ts = fm['published']
        if isinstance(ts, str) and len(ts) == 10:  # YYYY-MM-DD
            ts = ts + 'T00:00:00Z'
        fm['timestamp'] = ts
        changed = True

    # Add description if missing
    if 'description' not in fm:
        # Try to derive from content body
        body = content[fm_end + 4:]
        desc = extract_description_from_content(body)
        if desc:
            fm['description'] = desc
        else:
            # Use title as description
            title = fm.get('title', '')
            if title:
                fm['description'] = f"Note about {title.lower()}."
            else:
                fm['description'] = f"Atomic note about {os.path.basename(filepath).replace('.md', '').lower()}."
        changed = True

    # Add tags if missing
    if 'tags' not in fm:
        dirname = os.path.dirname(rel_path)
        fm['tags'] = [dirname]
        changed = True

    if not changed:
        return False

    # Rebuild file
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    body = content[fm_end + 4:]
    new_content = f"---\n{new_fm}---\n\n{body}"

    with open(filepath, 'w') as f:
        f.write(new_content)

    return True


def create_index_md(vault_dir, rel_dir):
    """Create an index.md file for a directory."""
    full_dir = os.path.join(VAULT, vault_dir)
    if not os.path.exists(full_dir):
        return False

    index_path = os.path.join(full_dir, 'index.md')
    if os.path.exists(index_path):
        return False  # Already exists

    # Collect md files in this directory
    md_files = []
    for f in sorted(os.listdir(full_dir)):
        if f.endswith('.md') and f != 'index.md':
            fp = os.path.join(full_dir, f)
            if os.path.isfile(fp):
                md_files.append(f)

    if not md_files:
        return False

    # Read titles from frontmatter or filename
    entries = []
    for f in md_files:
        fp = os.path.join(full_dir, f)
        with open(fp) as fh:
            content = fh.read()
        title = None
        desc = None
        if content.startswith('---'):
            try:
                fm_end = content.index('---', 3)
                fm = yaml.safe_load(content[3:fm_end])
                if fm:
                    title = fm.get('title', '')
                    desc = fm.get('description', '')
            except:
                pass
        if not title:
            title = f.replace('.md', '').replace('-', ' ').title()
        entries.append((title, f, desc))

    # Build index content
    lines = [f"# {vault_dir.title()}"]
    lines.append("")
    for title, fname, desc in entries:
        desc_str = f" - {desc}" if desc else ""
        lines.append(f"* [{title}]({fname}){desc_str}")

    index_content = '\n'.join(lines) + '\n'

    with open(index_path, 'w') as f:
        f.write(index_content)

    return True


def update_readme():
    """Update README.md with OKF reference and correct field names."""
    with open(README) as f:
        content = f.read()

    # Add OKF reference to "Knowledge Model" section
    old_knowledge_model = """## Knowledge Model

Nexus uses a lightweight semantic model:"""

    new_knowledge_model = """## Knowledge Model

Nexus follows the [Open Knowledge Format (OKF) v0.1](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) specification for knowledge representation. All concept documents include YAML frontmatter with standardized fields (`type`, `title`, `description`, `resource`, `tags`, `timestamp`).

Nexus uses a lightweight semantic model:"""

    content = content.replace(old_knowledge_model, new_knowledge_model)

    # Update the summary format example to use OKF fields
    old_summary_fm = """```text
---
title: "Original title"
source: "URL or source reference"
author: "Author"
published: "YYYY-MM-DD"
type: article
---"""

    new_summary_fm = """```text
---
type: Article
title: "Original title"
description: "One-line summary of the source."
resource: "URL or source reference"
tags: [tag1, tag2]
timestamp: "YYYY-MM-DDT00:00:00Z"
author: "Author"
---"""

    content = content.replace(old_summary_fm, new_summary_fm)

    # Add OKF conformance note to "Current Status"
    old_status = """## Current Status

This repository is an evolving knowledge vault."""

    new_status = """## Current Status

This repository follows the [Open Knowledge Format (OKF) v0.1](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) specification. All concept documents include standardized YAML frontmatter.

This repository is an evolving knowledge vault."""

    content = content.replace(old_status, new_status)

    with open(README, 'w') as f:
        f.write(content)

    return True


def main():
    print("=== OKF v0.1 Normalization ===\n")

    # Phase 1: Add frontmatter to files without it
    print("Phase 1: Adding frontmatter to files without it...")
    added_count = 0
    for vault_dir in ['concepts', 'indexes', 'tools']:
        full_dir = os.path.join(VAULT, vault_dir)
        if not os.path.exists(full_dir):
            continue
        for fname in sorted(os.listdir(full_dir)):
            if not fname.endswith('.md'):
                continue
            fp = os.path.join(full_dir, fname)
            if not os.path.isfile(fp):
                continue
            rel_path = f"{vault_dir}/{fname}"
            with open(fp) as f:
                content = f.read()
            if not content.startswith('---'):
                fm_type = DIR_TO_TYPE.get(vault_dir, "Reference")
                add_frontmatter_to_file(fp, rel_path, fm_type)
                added_count += 1
                if added_count % 100 == 0:
                    print(f"  Added {added_count} frontmatters...")

    print(f"  ✓ Added {added_count} frontmatters\n")

    # Phase 2: Normalize existing frontmatter
    print("Phase 2: Normalizing existing frontmatter...")
    normalized_count = 0
    for vault_dir in ['summaries']:
        full_dir = os.path.join(VAULT, vault_dir)
        if not os.path.exists(full_dir):
            continue
        for fname in sorted(os.listdir(full_dir)):
            if not fname.endswith('.md'):
                continue
            fp = os.path.join(full_dir, fname)
            if not os.path.isfile(fp):
                continue
            rel_path = f"{vault_dir}/{fname}"
            with open(fp) as f:
                content = f.read()
            if content.startswith('---'):
                if normalize_existing_frontmatter(fp, rel_path):
                    normalized_count += 1

    # Also check concepts, indexes, tools for existing frontmatter
    for vault_dir in ['concepts', 'indexes', 'tools']:
        full_dir = os.path.join(VAULT, vault_dir)
        if not os.path.exists(full_dir):
            continue
        for fname in sorted(os.listdir(full_dir)):
            if not fname.endswith('.md'):
                continue
            fp = os.path.join(full_dir, fname)
            if not os.path.isfile(fp):
                continue
            rel_path = f"{vault_dir}/{fname}"
            with open(fp) as f:
                content = f.read()
            if content.startswith('---'):
                if normalize_existing_frontmatter(fp, rel_path):
                    normalized_count += 1

    print(f"  ✓ Normalized {normalized_count} existing frontmatters\n")

    # Phase 3: Create index.md files
    print("Phase 3: Creating index.md files...")
    index_created = 0
    for vault_dir in ['concepts', 'indexes', 'summaries', 'tools']:
        if create_index_md(vault_dir, vault_dir):
            index_created += 1
            print(f"  ✓ Created {vault_dir}/index.md")
    print(f"  ✓ Created {index_created} index files\n")

    # Phase 4: Update README.md
    print("Phase 4: Updating README.md...")
    update_readme()
    print("  ✓ README.md updated\n")

    # Summary
    print("=== SUMMARY ===")
    print(f"  Frontmatters added: {added_count}")
    print(f"  Frontmatters normalized: {normalized_count}")
    print(f"  Index files created: {index_created}")
    print(f"  README.md updated: YES")
    print("\nDone! Run git status to see changes.")


if __name__ == '__main__':
    main()
