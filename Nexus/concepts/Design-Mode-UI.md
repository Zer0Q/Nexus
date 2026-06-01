# Design Mode UI

## Definition
A Cursor 3 feature that connects to your live app running in the browser. Instead of describing which UI element you want to change, you click on it. The agent sees exactly what you see and makes the targeted edit without touching anything else in the file.

## Why It Matters
Describing UI changes in text is error-prone and slow. Design Mode lets you point at the exact element and give a targeted instruction. The agent makes only that change -- nothing else in the file is touched.

## Key Ideas
- Start your app locally so it runs in the browser
- Open Agents Window in Cursor, click "Design Mode"
- Browser opens with an annotation layer over your app
- Click any UI element (button, card, nav item) -- it highlights with a blue outline
- Type your instruction directly next to the highlighted element
- The agent makes only that change, nothing else in the file is touched
- Example instructions: "Make this full-width on mobile", "Replace this text with data from /api/user endpoint"

## Tradeoffs
- Requires the app to be running locally
- Only works for UI changes visible in the browser
- Complex layout changes may still require text instructions

## Related
- [[concepts/Cursor-Agents-Window]] -- the interface where Design Mode is accessed
- [[concepts/Visual-to-Code-Generation]] -- alternative approach: describe UI and get code
- [[concepts/Five-Layer-AI-Stack]] -- part of Cursor's execution layer

## Source
[[source-notes/Damidefi-Five-Tool-AI-Stack-Full-Build]]
