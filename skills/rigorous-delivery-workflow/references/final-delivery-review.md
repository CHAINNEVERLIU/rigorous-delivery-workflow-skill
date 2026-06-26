# Final Delivery Review

Use before final response.

## Evidence Gate

Run fresh verification commands. Do not rely on earlier or subagent-reported results.

Collect:
- full test command output summary,
- build/lint/typecheck output summary,
- integration/e2e/manual smoke evidence when relevant,
- drift check result,
- final diff review.

## Final Self-Review

Answer:

1. Does every spec requirement have implementation and evidence?
2. Is every plan checklist item complete?
3. Are public contracts preserved or intentionally versioned?
4. Are auth, permissions, validation, errors, and data safety covered?
5. Are migrations and rollback/recovery considered where relevant?
6. Are user-facing workflows verified?
7. Are docs/config/deployment impacts handled?
8. Are tests broad enough for the blast radius?
9. Are any tests unrun? Why?
10. Are any P0/P1 findings open?
11. Are P2 findings fixed or explicitly accepted?
12. Did drift detection pass?

## Final Response Format

```text
Summary:
- <short change summary>

Files changed:
- <path>: <purpose>

Verification:
- command: result
- command: result

Unrun tests:
- none
or
- command: reason and risk

Drift check:
- <scope and contract result>

Residual risk:
- <none, or specific accepted risk>

Delivery verdict:
- meets delivery bar | does not meet delivery bar
```

If the delivery bar is not met, state what remains and do not call the work complete.
