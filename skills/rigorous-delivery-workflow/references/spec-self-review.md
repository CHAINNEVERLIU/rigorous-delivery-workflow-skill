# Spec and Plan Self-Review

Run this review repeatedly until convergence. Do not treat self-review as a single pass.

## Convergence Rule

- P0 = 0.
- P1 = 0.
- P2 items are either fixed or explicitly accepted with owner/rationale.
- P3 items do not block execution unless they create ambiguity.
- Every requirement has a verification method.
- Every changed surface has a drift check.

## Review Passes

### Pass 1: Requirement Coverage

Ask:
- Does every user request map to an explicit requirement?
- Are non-goals explicit?
- Are assumptions documented?
- Are all affected surfaces listed?
- Are compatibility promises clear?

### Pass 2: Commercial Delivery Risk

Ask:
- Could a real user fail the main workflow?
- Could data be lost, leaked, corrupted, or made inaccessible?
- Could auth or permissions be bypassed?
- Could existing integrations or clients break?
- Could deployment or configuration fail?
- Is observability sufficient to diagnose failure?
- Could a multi-step write leave a false success or half-success state?
- Are retries and idempotent replays safe?

### Pass 3: Testability

Ask:
- Does each requirement have a test or verification command?
- Are critical paths tested at the right level?
- Are regression tests named?
- Are failure modes tested?
- Are browser/manual checks included when user experience matters?
- Are default quality gates separated from external-service smoke tests?
- Does each new test describe expected RED and valid GREEN evidence?

### Pass 4: No-Context Executability

Ask:
- Can an agent with no conversation history execute this?
- Are exact files, commands, and expected outcomes provided?
- Are examples accurate against current code?
- Are fixture names, route names, selectors, and method names real?
- Are vague phrases removed?
- Are delivery state, review ledger, and verification matrix expectations explicit?
- Are prompts strong enough if copied to a low-capability external AI?

### Pass 5: Scope Drift and Future Extension

Ask:
- Could the plan encourage out-of-scope work?
- Are future extension points preserved?
- Are temporary shortcuts forbidden or clearly isolated?
- Are data migrations and compatibility paths considered?
- Are allowed and forbidden paths explicit?
- Are untracked/generated artifacts handled?

### Pass 6: External Handoff and Recovery

Ask:
- If an external AI reviews or implements this, is the prompt no-context and constrained?
- Does the plan instruct the user to paste complete external AI output back?
- Is there a review ledger for imported findings?
- Can the task resume after interruption from the state file?
- Are stale verification and scope changes recorded?

## Output Format

Record each review round:

```text
Round N:
- Focus:
- Findings:
- Fixes applied:
- Remaining accepted risks:
- Verdict:
```

Use `READY FOR PLAN`, `READY FOR IMPLEMENTATION`, or `REVISE BEFORE EXECUTION`.
