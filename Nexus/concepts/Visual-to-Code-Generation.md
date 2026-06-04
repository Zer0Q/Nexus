# Visual to Code Generation

## Definition
Converting structured design data (components, tokens, layout) directly into production code via MCP connection, rather than interpreting screenshots or text descriptions. The code generator reads actual design specifications and rebuilds them faithfully.

## Why It Matters
Screenshot-based code generation is lossy -- the model guesses at spacing, colors, and interactions. Structured design data preserves the designer's intent exactly, producing production-grade UI matching the design in minutes.

## Key Ideas
- MCP connection gives code generator direct access to design output
- Not screenshots -- actual design data: components, tokens, layout, everything
- Code generator references design system and writes code matching it exactly
- Adds hover states, transitions, edge-case handling from real design data
- Replaces the Figma-to-designer-to-developer pipeline with a single workflow
- Interactive preview catches flow issues before code is written

## Tradeoffs
- Tool lock-in -- MCP connection ties you to specific design/code tool pairs
- Complex interactions -- animated states and custom patterns need manual passes
- Design system dependency -- output quality depends entirely on system quality

## Related
- [[concepts/Design-System-First]]
- [[tools/Moonchild]]
- [[concepts/PRD-to-UI]]

## Source
[[summaries/PrajwalTomar-Codex-Moonchild-Design-Workflow]]
