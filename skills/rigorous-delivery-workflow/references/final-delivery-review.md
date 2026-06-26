# Final Delivery Review

## Contents

- Fresh evidence gate
- Final self-review
- Evidence matrix
- Completion ban
- Final response format

Use before final response. Do not rely on earlier or external-agent reported results if later changes could affect them.

## Fresh Evidence Gate

Collect fresh evidence after the last relevant change:
- focused tests for changed behavior,
- full or blast-radius regression tests,
- lint/typecheck/build when relevant,
- integration/e2e/browser/manual smoke when relevant,
- external-service smoke tests separately named when needed,
- drift check,
- red-flag scan,
- final diff review,
- state completeness check.

## Final Self-Review

Answer:

1. Does every spec requirement have implementation and evidence?
2. Is every plan checklist item complete?
3. Is every accepted review finding fixed and verified?
4. Are rejected/partial findings recorded with rationale?
5. Are public contracts preserved or intentionally versioned?
6. Are auth, authorization, validation, errors, audit, and data safety covered?
7. Are write ordering, half-success, rollback/recovery, idempotency, and retry behavior reviewed?
8. Are migrations and deployment/config changes handled when relevant?
9. Are user-facing workflows verified?
10. Are default quality gates separated from external-service smoke tests?
11. Are untracked files and generated artifacts reported?
12. Are any tests unrun? Why?
13. Are any P0/P1 findings open?
14. Are P2 findings fixed or explicitly accepted?
15. Did drift detection pass?

## Evidence Matrix

Use `verification-matrix.md` and fill:

```text
Backend focused:
Backend full:
Frontend lint:
Frontend typecheck:
Frontend unit:
Frontend coverage:
Frontend build:
Default e2e:
Security e2e:
Visual e2e:
Live backend smoke:
OpenAPI/schema check:
Migration check:
Manual/browser smoke:
Drift check:
Red-flag scan:
State check:
Untracked files:
Generated artifacts:
Known warnings:
Unrun tests and reasons:
Residual risks:
Delivery decision:
```

Omit irrelevant lines only if the reason is obvious or stated.

## Completion Ban

Do not say complete if:
- required tests failed,
- required tests were skipped without reason,
- external AI/subagent findings were not imported into the review ledger,
- P0/P1 findings remain,
- drift check found unresolved scope/security/test drift,
- default gates hide external-service prerequisites,
- state file lacks current phase, review ledger, verification ledger, or next single action,
- untracked source files are unreported.

## Final Response Format

```text
Summary:
- <short change summary>

Files changed:
- <path>: <purpose>

Verification:
- command: result

External AI/subagent review:
- none
or
- source: imported findings and status

Drift and artifacts:
- changed scope:
- forbidden paths:
- untracked files:
- generated artifacts:

Unrun tests:
- none
or
- command: reason and risk

Residual risk:
- none
or
- specific accepted risk

Delivery verdict:
- meets delivery bar | does not meet delivery bar
```
