# Verification Matrix

Use when writing plans and before final delivery. Every command should have a purpose and prerequisite classification.

## Command Classification

```text
Command:
Purpose:
Scope: focused | regression | full | smoke | visual | security | build | lint | typecheck | manual
Requires external service: yes/no
Starts own services: yes/no
Requires credentials: yes/no
CI default: yes/no
Expected pass condition:
Failure interpretation:
```

## Default Gate Rule

Default quality gates should be self-contained. If a test requires a backend, database, browser, network, account, or external service that the command does not start itself, it should be a separate explicitly named smoke command.

Examples:
- `npm run e2e`: should not include live backend smoke unless it starts backend itself.
- `npm run e2e:live-backend`: may require backend readiness and must document it.

## Final Evidence Matrix

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
Untracked files:
Generated artifacts:
Known warnings:
Unrun tests and reasons:
Residual risks:
Delivery decision:
```

## Freshness Rule

Any source change invalidates verification that could be affected by it. Record stale evidence in the delivery state and rerun before final delivery.
