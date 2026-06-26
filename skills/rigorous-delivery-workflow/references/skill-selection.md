# Skill and Tool Selection

Use before each major phase.

## Selection Rule

Load the smallest useful set of available skills/tools. Do not load everything. Do not invent unavailable tools.

If a matching skill is unavailable, follow the equivalent manual process and mention that in the checkpoint.

## Suggested Mapping

| Phase | Useful skills/tools if available |
| --- | --- |
| requirement shaping | brainstorming, domain-specific skills |
| spec writing | writing-plans, domain-specific docs |
| plan writing | writing-plans |
| review ingestion | receiving-code-review |
| external review request | requesting-code-review, subagent tools |
| implementation | executing-plans, test-driven-development |
| debugging | systematic-debugging |
| parallel execution | subagent-driven-development, dispatching-parallel-agents |
| browser/frontend | frontend-testing-debugging, playwright, framework-specific skills |
| backend/database | framework docs, database skills, security/auth skills |
| final proof | verification-before-completion |

## Subagent Rules

Allowed:
- independent review of spec or plan,
- independent test audit,
- independent security review,
- independent frontend impact scan,
- implementation slices with disjoint files and clear acceptance tests.

Forbidden:
- delegating final completion judgment,
- accepting subagent claims without evidence,
- letting multiple agents edit the same files without coordination,
- letting subagents expand scope,
- skipping main-agent diff review.

## Subagent Handoff Format

```text
Task:
Files allowed:
Files forbidden:
Spec/plan paths:
Required tests:
Drift checks:
Output required:
```

The main agent must read the subagent output, inspect diffs, and rerun or verify evidence before accepting it.
