# Industrialized Software Development

## Definition
Production-line approach to building software where agents write, review, test, and ship code, while humans design the pipeline and handle exceptions. Contrasts with the craft model where humans write code by hand.

## Why It Matters
The factory model shifts humans from doing the work to directing it. Output scales with pipeline efficiency, not headcount. Requires upfront investment in processes, tools, and safety nets.

## Key Ideas
- Craft model: human writes code, human reviews, human tests, human deploys
- Factory model: standardized pipeline, automated quality checks, minimal manual labor
- Humans design the line and handle exceptions; machines do the reps
- Extreme version: "Code must not be written by humans. Code must not be reviewed by humans." (StrongDM)
- Key enablers: automated tests, internal developer platform, agent tool access to codebase
- DORA report: quality internal platform is the biggest differentiator between AI winners and losers
- Not "engineers using AI" -- it's a system where agents do the work and humans direct

## Tradeoffs
- Upfront infrastructure investment required
- Requires test coverage you'd actually bet on
- Cultural shift: engineers must trust the pipeline over manual review

## Related
- [[concepts/Software-Factory-Ladder]]
- [[concepts/Verifiable-Automation]]

## Source
[[source-notes/BusinessBarista-Software-Factory]]
