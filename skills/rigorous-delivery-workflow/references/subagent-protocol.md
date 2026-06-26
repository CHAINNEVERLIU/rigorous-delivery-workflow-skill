# Subagent Protocol

Use subagents only for independent work with clear boundaries or independent review. The main agent remains responsible for correctness.

## Good Subagent Tasks

- no-context spec or plan review,
- security review,
- test coverage audit,
- frontend impact scan,
- backend contract scan,
- implementation slice with disjoint files and exact acceptance tests.

## Bad Subagent Tasks

- final completion judgment,
- shared-file implementation without coordination,
- architectural decisions without main-agent review,
- debugging a tightly coupled single failure,
- work that requires credentials, production access, or user decisions.

## Handoff Format

```text
Task:
Objective:
Files allowed:
Files forbidden:
Spec/plan/state paths:
Required tests:
Drift checks:
Output required:
Do not:
```

## Required Subagent Output

```text
Scope reviewed:
Files inspected:
Commands run:
Findings:
- ID:
  Severity:
  Evidence:
  Required change:
  Required test:
Residual risks:
Next recommended action:
```

## Acceptance Rule

The main agent must:
- read the output,
- inspect any changed files,
- rerun or independently verify evidence,
- import valid findings into the review ledger,
- reject unsupported claims.
