# CLAUDE.md Five-Section Template

## Definition
A five-section structure for CLAUDE.md configuration files: Role, Style, Constraints, Workflow, Quality. Covers all dimensions of AI behavior in a single persistent file.

## Why It Matters
Provides a complete but minimal framework for project-level AI configuration. Each section addresses a different behavioral dimension, and together they create a self-contained instruction set that replaces repeated prompting.

## Key Ideas
- **Section 1 — Role:** Tell the AI what it is. Be specific, not "helpful assistant." Example: "You are my investment research analyst. You are not a chatbot. You are a workflow operator."
- **Section 2 — Style:** Concise, no preamble, bullet points over paragraphs, specific numbers over vague statements
- **Section 3 — Constraints:** Negative rules — "never invent data," "never reformat without asking," "never commit without tests"
- **Section 4 — Workflow:** Procedural triggers — "when I drop a file in raw/, process it: read → identify → summarize → file → index"
- **Section 5 — Quality:** Pre-delivery checklist — verify claims include sources, check formatting, remove filler

## Tradeoffs
- Five sections may be overkill for simple projects
- Quality section adds latency (pre-delivery checks) but improves output reliability

## Related
- [[tools/CLAUDE-MD-Project-Knowledge]]
- [[concepts/CLAUDE-MD-as-Context-Layer]]
- [[concepts/Agent-Identity-Layer]]
- [[frameworks/Spec-Driven-Development]]

## Source
[[source-notes/Hanakoxbt-CLAUDE-MD-Second-Employee]]
