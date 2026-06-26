# Skill Routing Matrix

Use before each major phase. Load the smallest useful set of skills/tools. If a matching skill is unavailable, use the manual equivalent and record that in the checkpoint.

| Situation | Load or emulate |
| --- | --- |
| Create or revise a skill | skill-creator |
| Write or revise spec/plan | writing-plans, domain-specific docs |
| Receive review feedback | receiving-code-review, review-ledger |
| Execute a written plan | executing-plans, test-driven-development |
| Add features or bug fixes | test-driven-development |
| Any unexpected failure | systematic-debugging |
| Multi-surface independent work | subagent-driven-development, dispatching-parallel-agents |
| External AI prompt generation | external-ai-handoff references |
| Frontend UI/React work | frontend-testing-debugging, React best practices |
| Browser/e2e/visual verification | playwright or equivalent browser verification skill |
| Backend/API/database/security work | framework docs, database/security/auth skills if available |
| Completion claim | verification-before-completion, final-delivery-review |

## Routing Rules

- Record selected skills/tools at the start of each major phase.
- Do not load all skills by default.
- Do not invent tools that are not available.
- Use domain skills only after inspecting the repo enough to know they apply.
- For OpenAI product questions, use OpenAI docs skill or official docs as required by the environment.

## Checkpoint Field

```text
Skill routing:
- Loaded:
- Manual equivalents:
- Reason:
```
