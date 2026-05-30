---
type: concept
related: [Spaced-Repetition-System, Concept-Note-Template, Active-Recall-Learning]
---

# Mastery-Score-Tracking

## Definition
A frontmatter-based scoring system (0-5 scale) that tracks how well a learner has internalized each concept. The score drives review interval adjustments: correct recall advances to the next interval, incorrect recall resets to the previous interval.

## Why It Matters
Provides a quantitative signal for the [[Spaced-Repetition-System]] to adjust review timing. Concepts with mastery scores of 5 or above move to longer intervals. Concepts consistently answered incorrectly are flagged for [[Synthesis-Session]] rather than more repetition.

## Key Ideas
- Score stored in frontmatter of each concept note: mastery: 0-5
- Updated after every recall session based on performance
- Correct answer: move to next review interval
- Incorrect answer: reset to previous interval
- Score of 5+: concept is well-retained, moves to longer interval
- Consistently low score: flagged for synthesis session instead of repetition

## Tradeoffs
- 0-5 scale may be too coarse for fine-grained calibration
- Self-evaluation of correctness may be biased; Claude evaluation reduces this

## Related
- [[Spaced-Repetition-System]]
- [[Concept-Note-Template]]
- [[Active-Recall-Learning]]
- [[Synthesis-Session]]
- [[Note-Contribution-Rate]]

## Source
[[NeilXBT-Obsidian-Knowledge-Graph-Learning]]
