# AI-Generated Code Review

## Definition
AI-generated code review is the practice of treating generated code as a fast, confident draft whose requirement fit, assumptions, security, performance, and maintainability must be independently checked.

## Why It Matters
Generated code often looks clean on the happy path while hiding missing authorization, bad defaults, dependency risk, performance problems, and failure-path gaps. The skill shifts from writing code to proving that the draft is safe and correct to ship.

## Key Ideas
- Start with the requirement, not the implementation.
- Interrogate architectural defaults because models often choose the common pattern rather than the fitting one.
- Trace data flow, edge cases, failure paths, and concurrency risks.
- Run an explicit security pass for auth, authorization, validation, secrets, injection, and dependencies.
- Review maintainability as a shipping criterion, not polish.

## Related
- [[concepts/Evidence-Validation]]
- [[concepts/Harness-Engineering]]
- [[concepts/Supply-Chain-Security]]
- [[concepts/Prompt-Validation-Over-Construction]]

## Source
[[summaries/Techgirlll-AI-Generated-Code-Review]]
