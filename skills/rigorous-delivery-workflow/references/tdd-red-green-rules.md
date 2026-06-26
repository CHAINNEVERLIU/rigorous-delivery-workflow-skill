# TDD RED/GREEN Rules

Use when adding or changing behavior. The point is not merely to see a failure. The failure must prove the intended missing behavior.

## RED Classification

Valid RED:
- fails on the target behavior assertion,
- uses real project fixtures or faithful fakes,
- would pass if the intended implementation existed,
- does not depend on unrelated environment breakage.

Invalid RED:
- fixture is wrong,
- payload/schema is malformed unintentionally,
- command path is wrong,
- dependency or service is missing,
- test imports fail before exercising target behavior,
- failure is caused by the test's own bug.

Environment RED:
- service not running,
- port conflict,
- missing database,
- missing browser,
- missing credentials,
- network/external dependency unavailable.

Regression RED:
- unrelated existing test fails.

## Required Step Record

```text
Test:
Target behavior:
Expected RED:
Actual RED:
Classification: valid | invalid | environment | regression
Action:
Focused GREEN:
Related regression:
```

If RED is invalid, fix the test and rerun before implementation. If RED is environment, fix environment or record an accepted reason. If RED is regression, investigate before continuing.

## Completion Rule

Do not mark a task complete until:
- valid RED was observed when practical,
- focused GREEN passed after implementation,
- related regression passed,
- any skipped RED/GREEN step has a recorded reason.
