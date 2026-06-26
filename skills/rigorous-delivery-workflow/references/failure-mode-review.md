# Failure Mode Review

Use during implementation review and final delivery review, especially for write paths, permissions, public contracts, and multi-step operations.

## Write Ordering

Check every write path:
- Are authentication and authorization checks before writes?
- Are validation, size limits, and type checks before writes?
- Are filesystem writes after permission checks?
- Are database updates ordered so later failure cannot leave false success state?
- Is there a transaction or compensating behavior for multi-step writes?
- Does idempotency return the same semantic result on replay?

## Half-Success And Recovery

Ask:
- If step 2 fails after step 1 succeeds, what state remains?
- Can users see false `running`, `completed`, `approved`, or `uploaded` states?
- Can retry duplicate records, files, audit entries, notifications, or runs?
- Is stale verification invalidated after later changes?
- Are temporary artifacts cleaned or harmless?

## Contract And Client Safety

Check:
- response envelope shape,
- OpenAPI/schema presence when applicable,
- frontend/client type compatibility,
- error code and retry semantics,
- backward compatibility for existing consumers,
- default quality gates versus external-service smoke tests.

## Security And Data Boundary

Check:
- tenant/project/user boundary,
- forbidden cross-project reads/writes,
- safe error redaction,
- no direct secret exposure,
- no mock-only production behavior,
- audit for security-sensitive operations.

## Required Output

```text
Failure-mode review:
- Write ordering reviewed:
- Half-success risk:
- Idempotency risk:
- Contract/client risk:
- Security/data-boundary risk:
- Required tests added:
- Verdict: pass | fix required | accepted risk
```
