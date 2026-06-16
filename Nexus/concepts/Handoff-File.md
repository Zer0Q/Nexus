---
type: Concept
title: Handoff File
description: '- Lives in shared pipeline directory (e.g., .pipeline/) - Format: Markdown
  with YAML frontmatter - Examples: spec.md, changes.md, test-results.md - Enables
  s...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Handoff File

Structured artifact passed between agents in a pipeline, containing the output of one stage and instructions for the next.

- Lives in shared pipeline directory (e.g., .pipeline/)
- Format: Markdown with YAML frontmatter
- Examples: spec.md, changes.md, test-results.md
- Enables sequential agent chains without shared memory

See also: [[concepts/Agent-Pipeline-Pattern]], [[concepts/Multi-Agent-Development]]
