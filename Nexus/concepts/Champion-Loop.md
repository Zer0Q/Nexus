# Champion Loop

## Definition
A Champion Loop is a controlled improvement loop where the current best prompt, model, or workflow remains the champion until a challenger beats it on held-out examples without breaking must-pass rules.

## Why It Matters
Ad-hoc prompt tweaks often overfit to examples the human is staring at or silently regress other behaviors. Champion promotion makes improvement evidence-based and protects recurring workflows from quality drift.

## Key Ideas
- Split examples into working data and holdout data.
- Fix one recorded failure at a time.
- Promote only if the challenger beats the champion on unseen holdouts by a defined margin.
- Stop when score is reached, budget is exhausted, or no holdout improvement appears.

## Related
- [[concepts/Champion-Gate]]
- [[concepts/Self-Improvement-Loop]]
- [[concepts/Evidence-Validation]]
- [[concepts/AI-Slop-Quality-Filtering]]

## Source
[[summaries/0xJeff-Hermes-Sensei-Loop]]
