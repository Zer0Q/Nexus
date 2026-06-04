# PRD to UI

## Definition
Feeding a product requirements document directly to an AI design tool to generate full screen designs. Instead of prompting for individual screens, you paste a structured PRD (product intro, objectives, user flows, features, tech stack) and the tool generates the complete UI against your design system.

## Why It Matters
PRD-to-UI eliminates the iterative screen-by-screen design process. A single structured document gives the AI enough context to generate consistent, coherent screens that follow the product's navigation and hierarchy.

## Key Ideas
- Paste a one-page PRD instead of prompting screen by screen
- Brainstorm in chat mode before generating -- confirm screen list, navigation, hierarchy
- PRD should cover: product intro, objectives, target users, key features, user journeys, tech stack, design direction
- Specific enough for real context, structured enough for the tool to extract details
- Quality of PRD determines quality of generated screens

## Tradeoffs
- PRD quality dependency -- vague PRD gets generic screens
- Upfront thinking time vs iterative design
- May need refinement passes for complex flows

## Related
- [[concepts/Design-System-First]]
- [[concepts/Visual-to-Code-Generation]]
- [[tools/Moonchild]]

## Source
[[summaries/PrajwalTomar-Codex-Moonchild-Design-Workflow]]
