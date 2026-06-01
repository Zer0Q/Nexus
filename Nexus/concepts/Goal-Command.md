# Goal Command

## Definition
The /goal command system in Hermes Agent that transforms the agent from a reactive chatbot into an autonomous background worker. You set an objective, Hermes breaks it into subtasks, executes independently, and continues until completion without requiring further input.

## Why It Matters
This is the primary mechanism for turning Hermes into a proactive employee rather than a passive chatbot. It enables the agent to work on complex multi-step tasks without the user needing to babysit each step.

## Key Ideas
- `/goal [description]` — start autonomous execution of a task
- `/goal status` — check what's currently running
- `/goal pause` — pause without losing context
- `/goal resume` — continue after pause
- `/goal clear` — end the current goal
- `/subgoal [text]` — add conditions or constraints mid-execution
- Default max turns: 5-10; configurable higher for complex tasks
- Agent breaks goals into subtasks, executes, and reports completion

## Tradeoffs
- Each turn costs tokens — raising max_turns increases cost
- Complex goals may need careful scoping to avoid scope creep
- No real-time visibility without checking status or using the dashboard

## Related
- [[concepts/Max-Turns-Configuration]] -- controlling goal complexity
- [[concepts/Overnight-Goal-Runs]] -- using /goal for long-running tasks during sleep
- [[concepts/Kanban-Board-Workflow]] -- automated goal execution via the task board
- [[concepts/Hermes-Dashboard]] -- visual status of running goals

## Source
[[source-notes/IBuzovskyi-Hermes-Agent-Complete-Guide]]
