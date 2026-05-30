---
title: "8 Claude Code Agents You Can Build in Under 10 Minutes Each"
source: "https://x.com/zodchiii/status/2054853752587235778"
author:
  - "[[@zodchiii]]"
published: 2026-05-14
created: 2026-05-31
description: "You write code, review it, test it, write the PR, check coverage, update the changelog, and analyze logs. Every day. All manually.Each of th..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HIRAZhSXEAAubsM?format=jpg&name=large)

You write code, review it, test it, write the PR, check coverage, update the changelog, and analyze logs. Every day. All manually.

Each of these is a one-file agent that runs in its own context window and returns a clean summary. 10 minutes to set up, runs forever.

Here are all 8 agent files 👇

Before we dive in, I share daily notes on AI & vibe coding in my Telegram channel: [https://t.me/zodchixquant](https://t.me/zodchixquant)🧠

![Imatge](https://pbs.twimg.com/media/HIQ-31IWMAANk1k?format=jpg&name=large)

## How agents work (30-second version)

Create a markdown file in **.claude/agents/** with YAML frontmatter. That's it.

```text
.claude/agents/
├── pr-summarizer.md
├── dep-updater.md
├── changelog.md
├── coverage-checker.md
├── dead-code.md
├── migration-gen.md
├── api-docs.md
└── error-analyzer.md
```

Each file has a name, description, model, tools, and instructions. Claude auto-delegates when a task matches the description, or you invoke it manually with [@agent](https://x.com/@agent)\-name.

```yaml
---
name: agent-name
description: When to use this agent
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Grep
  - Glob
---
```

Instructions for what this agent does.

Key settings:

- **model**: route agents to Sonnet for cost savings (Opus is 5x more expensive)
- **tools**: limit what the agent can access (read-only for reviewers, full access for writers)
- **memory scope**: set to user for persistent learnings across sessions, none for one-off tasks

## Agent 1: PR Summarizer

Reads your branch diff and writes a structured PR description ready to paste into GitHub.

```yaml
---
name: pr-summarizer
description: Generate a PR description from current branch changes. Use when creating pull requests.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Grep
  - Glob
  - Bash
---

1. Run \`git log main..HEAD --oneline\` to get all commits
2. Run \`git diff main...HEAD --stat\` for changed files summary
3. Read the key changed files to understand full context

Generate PR description in this format:

## What
[One paragraph: what this PR does]

## Why
[One paragraph: why this change is needed]

## Changes
[Bullet list of key changes, grouped by area]

## Testing
[How this was tested]

Output ready to paste into GitHub. Nothing else.
```

## Agent 2: Dependency Updater

Checks for outdated dependencies and creates upgrade PRs with context on breaking changes.

```yaml
---
name: dep-updater
description: Check for outdated dependencies and suggest safe updates. Use when maintaining packages.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Bash
  - Grep
---

1. Run \`npm outdated\` or equivalent for the project's package manager
2. For each outdated package, categorize:
   - PATCH updates (safe, auto-update)
   - MINOR updates (usually safe, check changelog)
   - MAJOR updates (breaking changes, needs review)
3. For MAJOR updates, search for the package's CHANGELOG or release notes
4. Output a prioritized list:

## Safe to update now
[Package]: current → latest (patch/minor, no breaking changes)

## Needs review
[Package]: current → latest (major, breaking changes: [summary])

## Skip for now
[Package]: current → latest (reason to skip)
```

## Agent 3: Changelog Writer

Reads your commits since last release and generates a formatted changelog.

```yaml
---
name: changelog
description: Generate a changelog from recent commits. Use after finishing a sprint or before a release.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Bash
  - Grep
---

1. Find the latest tag or release: \`git describe --tags --abbrev=0\`
2. Get all commits since: \`git log [tag]..HEAD --oneline\`
3. Read commit messages and categorize by type

Generate changelog in this format:

## [version] - [date]

### Added
- [feat commits]

### Fixed
- [fix commits]

### Changed
- [refactor commits]

### Documentation
- [docs commits]

Group related changes. Skip merge commits and chore commits.
Write in past tense. Each entry is one clear sentence.
```

## Agent 4: Test Coverage Checker

Runs your test suite, analyzes coverage gaps, and suggests what to test next.

```yaml
---
name: coverage-checker
description: Analyze test coverage and find untested code. Use when improving test quality.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Bash
  - Grep
  - Glob
---

1. Run the test suite with coverage: \`npm test -- --coverage\` or equivalent
2. Parse the coverage report
3. Identify files with lowest coverage
4. For each low-coverage file, read the source and identify:
   - Untested functions
   - Untested branches (if/else paths)
   - Edge cases not covered

Output:

## Coverage Summary
Total: [X]% | Statements: [X]% | Branches: [X]%

## Lowest Coverage Files
[file]: [X]% - missing tests for [specific functions]

## Recommended Next Tests
Priority 1: [file] - [function] (handles [critical path])
Priority 2: [file] - [function] (handles [error case])
Priority 3: [file] - [function] (handles [edge case])

Keep recommendations specific and actionable.
```

## Agent 5: Dead Code Finder

Scans for unused exports, unreachable functions, and orphaned files.

```yaml
---
name: dead-code
description: Find unused code, unreachable functions, and orphaned files. Use during cleanup.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Grep
  - Glob
---

1. Find all exported functions/classes across the codebase
2. For each export, grep for imports/usage in other files
3. Identify:
   - Exported functions never imported anywhere
   - Files never imported by any other file
   - Functions defined but never called within their own file
   - Console.log statements left in production code
   - Commented-out code blocks longer than 5 lines

Output:

## Unused Exports
[file]: [export name] - not imported anywhere

## Orphaned Files
[file] - never imported by any other file

## Dead Functions
[file]: [function name] - defined but never called

## Cleanup Candidates
[file]: [description of what can be removed]

Be conservative. If uncertain, mark as "verify before removing."
```

## Agent 6: Migration Generator

Creates database migrations from schema change descriptions.

```text
---
name: migration-gen
description: Generate database migrations. Use when adding tables, columns, or changing schema.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Write
  - Glob
  - Bash
---

1. Read existing migrations to understand:
   - Migration tool (Prisma, Drizzle, Knex, raw SQL)
   - Naming convention
   - File structure
2. Read the current schema file if one exists
3. Create the migration file following project conventions

Rules:
- Always include both UP and DOWN migrations
- Add indexes for foreign keys and frequently queried columns
- Never add NOT NULL without a DEFAULT value
- Use the project's exact naming convention for files

After creating, run the migration locally and verify it applies cleanly.
```

## Agent 7: API Doc Builder

Reads your API routes and generates OpenAPI-style documentation.

```text
---
name: api-docs
description: Generate API documentation from route files. Use when documenting endpoints.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Grep
  - Glob
---

1. Find all API route files (src/app/api/, routes/, etc.)
2. For each endpoint, extract:
   - HTTP method
   - Path and parameters
   - Request body shape (from validation schemas or types)
   - Response shape (from return types)
   - Auth requirements (middleware checks)
   - Error responses

3. Generate documentation:

## [METHOD] /api/[path]

**Auth:** Required / Public
**Request body:**
json
{ "field": "type" }
Response:
{ "field": "type" }
Errors:
400: [description]
401: [description]
404: [description]
Match documentation style if existing docs exist in the project.
---
```

## Agent 8: Error Log Analyzer

Reads error logs, groups by pattern, identifies root causes.

```text
---
name: error-analyzer
description: Analyze error logs and identify patterns. Use when debugging production issues.
model: claude-sonnet-4-5-20250929
tools:
  - Read
  - Bash
  - Grep
---

1. Read the log file (filter for ERROR and WARN only):
   \`grep -n 'ERROR\|WARN\|Exception\|FATAL' $ARGUMENTS | head -200\`
2. Group errors by type/pattern
3. For each group, identify:
   - Frequency (how many times)
   - First and last occurrence
   - Common stack trace elements
   - Likely root cause

Output:

## Error Summary
Total errors: [N] | Unique patterns: [N] | Time span: [range]

## Pattern 1: [Error Type] (occurred [N] times)
First seen: [timestamp]
Last seen: [timestamp]
Stack: [key frames]
Likely cause: [explanation]
Suggested fix: [action]

## Pattern 2: ...

Prioritize by frequency and severity. Most frequent pattern first.
```

## How to use them

**Manual invocation:**

```text
@agent-pr-summarizer summarize changes on this branch
@agent-dead-code scan src/ for unused exports
@agent-error-analyzer check logs/app.log
```

**Auto-delegation:** Claude reads agent descriptions and delegates automatically when your task matches. Ask "generate a changelog for this sprint" and Claude invokes the changelog agent without you mentioning it.

**Parallel execution:** Run multiple agents at once:

```text
Run @agent-coverage-checker and @agent-dead-code in parallel on the src/ directory
```

Each agent works in its own context window. Results return to your main session as clean summaries.

## The cost math

All 8 agents run on Sonnet by default (5x cheaper than Opus). Each agent maintains its own isolated context, so verbose output from log analysis or file scanning stays contained and doesn't bloat your main session.

```text
Without agents:
- Error log analysis dumps 10,000 lines into your main context
- PR description requires reading 15 files in your main session
- Dead code search runs 50+ grep commands in your main context
- Total: 300,000+ tokens in one session

With agents:
- Each agent works in isolation
- Only summaries return to main context
- Total main context: ~30,000 tokens
- Each agent: ~20,000 tokens in their own window
```

Same work done. 90% less token waste in your main session.

Thanks for reading!

I share daily notes on AI, finance, and vibe coding in my Telegram channel: [https://t.me/zodchixquant](https://t.me/zodchixquant)

![Imatge](https://pbs.twimg.com/media/HIQ-DrsXYAAWgkl?format=jpg&name=large)