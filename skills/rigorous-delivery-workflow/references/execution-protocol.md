# Execution Protocol

Use this after a converged implementation plan exists.

## Baseline

Before edits:
- read spec and plan fully,
- inspect current repository state,
- run or record baseline verification commands,
- note existing failures separately from task-caused failures,
- identify dirty worktree changes and do not revert user work.

## Task Loop

For each task:

1. Read task instructions.
2. Confirm files are within allowed scope.
3. Add or update tests first.
4. Run the focused test.
5. Implement the smallest correct change.
6. Run focused verification.
7. Run related regression verification.
8. Run drift detection.
9. Review the diff against the spec, plan, public contracts, security rules, and commercial readiness risks.
10. Update task checklist only after evidence exists.
11. Emit checkpoint.

## Checkpoint Format

```text
Checkpoint: Task N
- Files changed:
- Tests/commands run:
- Results:
- Drift check:
- Diff/spec review:
- Risks or blockers:
- Next task:
```

## Conflict Handling

If plan and code conflict:
- stop the task,
- describe exact conflict,
- inspect current code and tests,
- propose the smallest plan correction,
- do not silently change the product goal.

## Required Completion Rule

Do not claim completion if:
- any required test failed,
- any required test was skipped without accepted reason,
- drift check found unresolved scope changes,
- plan checklist is incomplete,
- final self-review has open P0/P1 items.
