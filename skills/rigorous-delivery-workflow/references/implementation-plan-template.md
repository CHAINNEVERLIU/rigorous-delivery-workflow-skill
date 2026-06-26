# No-Context Implementation Plan Template

Use this template after the spec has converged.

## Header

```markdown
# <Feature Name> Implementation Plan

> For agentic workers: execute task-by-task. Update checklist status only after verification evidence exists.

Goal: <one sentence>
Architecture: <2-4 sentences>
Tech stack discovered: <languages/frameworks/test tools>
Approved spec: <path>
```

## Execution Rules

Include:
- allowed file roots,
- forbidden file roots,
- public contracts that must not break,
- security rules,
- compatibility rules,
- required verification commands,
- drift checks,
- completion criteria.

## File Map

List exact files:

| File | Action | Responsibility |
| --- | --- | --- |
| path | create/modify/test/docs | reason |

## Commands

Prefer project-native commands. Include OS variants when needed.

```bash
<focused test command>
<full verification command>
```

## Task Structure

Every task must include:

- files,
- test to add or update,
- implementation instructions,
- focused verification,
- regression verification,
- drift check,
- checklist update.

Example:

````markdown
### Task N: <name>

Purpose: <why this task exists>

Files:
- Test: <exact test file>
- Modify: <exact source file>

- [ ] Add failing test:

```<language>
<exact or near-exact test code>
```

- [ ] Run:

```bash
<command>
```

Expected before implementation: fail for <specific reason>.

- [ ] Implement:
  - exact function/class/module to change,
  - constraints,
  - compatibility rule.

- [ ] Run focused tests:

```bash
<command>
```

- [ ] Run related regressions:

```bash
<command>
```

- [ ] Drift check:
  - git diff --stat
  - inspect changed files against allowed map
  - verify no forbidden scope touched
````

## Acceptance Matrix

| Area | Evidence | Pass Condition |
| --- | --- | --- |
| contract | command/test | expected result |
| security | command/test | expected result |
| user path | browser/manual/CLI | expected result |

## Self-Review

End with:
- traceability to spec,
- ambiguity audit,
- risk review,
- multi-round review log,
- final verdict.

Use `READY FOR IMPLEMENTATION` only after scans and review pass.
