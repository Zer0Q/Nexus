---
type: Concept
title: Async Queue Pattern
description: An asynchronous communication pattern between human and AI using QUEUE
  and GENERATED folders. The human drops a file describing what they need into QUEUE.
  Th...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Async Queue Pattern

## Definition
An asynchronous communication pattern between human and AI using QUEUE and GENERATED folders. The human drops a file describing what they need into QUEUE. The system processes it on its next cycle. The output appears in GENERATED. Neither waits for the other.

## Why It Matters
Enables the vault to "run your business while you sleep." You capture tasks when they occur to you. The system executes them when it runs. You review results when convenient. No synchronous waiting.

## Key Ideas
- QUEUE: input folder -- drop request files (DRAFT-topic.md, RESEARCH-topic.md)
- GENERATED: output folder -- processed results appear here
- Naming conventions trigger specific workflows (DRAFT-, RESEARCH-, etc.)
- "You are never waiting for it. It is never waiting for you."
- Drop research requests at midnight, brief is ready at 6am
- Decouples capture from processing from review

## Tradeoffs
- Latency between request and output (depends on workflow schedule)
- Need to check GENERATED folder for results
- Risk of queue items being missed if workflow fails

## Related
- [[concepts/Three-Layer-Architecture]]
- [[concepts/Automated-Business-Workflows]]
- [[concepts/Daily-Synthesis-Workflow]]

## Source
[[summaries/CyrilXBT-Business-Operating-System]]
