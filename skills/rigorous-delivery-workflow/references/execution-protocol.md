# Execution Protocol

Use after a converged implementation plan exists. Keep the delivery state current while executing.

## Baseline

Before edits:
- read the spec, plan, and delivery state fully,
- inspect current repository state,
- identify allowed and forbidden paths,
- run or record baseline verification commands when useful,
- note existing failures separately from task-caused failures,
- identify dirty worktree changes and untracked files,
- select specialist skills using `skill-routing-matrix.md`.

## Task Loop

For each task:

1. Restate the task, allowed files, and expected behavior.
2. Confirm files are inside allowed scope.
3. Add or update tests first when practical.
4. Run the focused test and classify RED using `tdd-red-green-rules.md`.
5. If RED is invalid, fix the test/fixture/environment before implementation.
6. Implement the smallest correct change.
7. Run focused GREEN verification.
8. Run related regression verification.
9. Review failure modes using `failure-mode-review.md`.
10. Run drift detection.
11. Review the diff against spec, plan, contracts, security, dirty worktree, and commercial readiness.
12. Update the delivery state: execution checklist, verification ledger, drift ledger, invalidated verification, next single action.
13. Emit a checkpoint.

## Checkpoint Format

```text
Checkpoint: Task N
- Current phase:
- Files changed:
- Tests/commands run:
- RED classification:
- GREEN/regression result:
- Failure-mode review:
- Drift check:
- Diff/spec review:
- Skill routing:
- Risks or blockers:
- Next single action:
```

## Conflict Handling

If plan and code conflict:
- stop the task,
- describe the exact conflict,
- inspect current code and tests,
- record the conflict in delivery state,
- propose the smallest plan correction,
- do not silently change product goals.

## External Output Handling

If external AI or subagent output arrives during execution:
- pause the current task at a safe point,
- import findings into the review ledger,
- verify findings against repo artifacts,
- update state and invalidated verification,
- resume only accepted work.

## Required Completion Rule

Do not mark a task complete if:
- valid RED was not observed or skipped without reason,
- focused GREEN failed,
- related regression failed,
- drift check found unresolved scope changes,
- failure-mode review has unresolved P0/P1 risk,
- state was not updated.
