# Harness Engineering

## Definition
Fixing agent failures at the runtime interface layer without retraining the model or modifying the evaluation environment. Life-Harness is a lifecycle-aware harness that turns recurring errors into reusable runtime fixes across four areas: action realization, environment contracts, trajectory regulation, and procedural skills.

## Why It Matters
Many agent failures come from mismatches at the model-environment interface, not from the model's reasoning. Harness engineering fixes these without the cost and risk of fine-tuning, keeping the approach drop-in for any backbone.

## Key Ideas
- Failures become reusable interventions -- harness-level patches the agent reuses on later attempts
- Model frozen, environment intact -- only the interface between them adapts
- Life-Harness improves 116/126 model-environment settings (88.5% average relative improvement)
- Effect holds across model scales -- not just helping weak models
- Evidence for the code-as-harness thesis: large share of agent failures are interface problems
- Partial harnesses (initial steps only) can outperform fully structured workflows

## Tradeoffs
- Harness complexity vs coverage -- more fixes mean more harness code to maintain
- Generalization -- harness fixes trained on one environment may not transfer
- Over-harnessing risk -- too much guidance can reduce agent autonomy

## Related
- [[concepts/SkillOptimization]]
- [[concepts/Workflow-Compilation]]
- [[concepts/Agent-Logic]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week]]
