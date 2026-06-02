# Feedback Loop Training

## Definition
The six-step cycle for training personal agents through iterative feedback: (1) agent produces output, (2) user reads and flags what's wrong, (3) user gives specific correction/next steps, (4) agent encodes correction as permanent rule, (5) next output becomes tighter, (6) repeat.

## Why It Matters
This is the easiest and most direct way to train a personal agent. Unlike fine-tuning, which requires datasets and infrastructure, feedback loop training happens naturally in daily usage -- every correction improves future outputs.

## Key Ideas
- Step 1: Agent produces something (brief, analysis, summary)
- Step 2: User reads immediately and flags what's wrong
- Step 3: User gives specific correction, not vague feedback
- Step 4: Agent encodes correction as permanent rule (memory, skill, preference)
- Step 5: Next output becomes tighter and more relevant
- Step 6: Repeat -- compounding improvements over time
- Biggest challenge: echo chamber bias where sources gravitate toward same topics

## Tradeoffs
- Specificity of corrections -- vague feedback produces vague improvements
- Encoding mechanism -- where do corrections live (memory, skills, preferences)?
- Correction drift -- old corrections may conflict with new ones over time

## Related
- [[concepts/Self-Improvement-Loop]]
- [[concepts/SkillOptimization]]
- [[concepts/Echo-Chamber-Bias]]

## Source
[[source-notes/0xJeff-Hermes-Analyst-60-Days]]
