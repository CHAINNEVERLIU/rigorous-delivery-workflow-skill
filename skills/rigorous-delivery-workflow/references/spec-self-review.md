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

### Pass 3: Testability

Ask:
- Does each requirement have a test or verification command?
- Are critical paths tested at the right level?
- Are regression tests named?
- Are failure modes tested?
- Are browser/manual checks included when user experience matters?

### Pass 4: No-Context Executability

Ask:
- Can an agent with no conversation history execute this?
- Are exact files, commands, and expected outcomes provided?
- Are examples accurate against current code?
- Are fixture names, route names, selectors, and method names real?
- Are vague phrases removed?

### Pass 5: Scope Drift and Future Extension

Ask:
- Could the plan encourage out-of-scope work?
- Are future extension points preserved?
- Are temporary shortcuts forbidden or clearly isolated?
- Are data migrations and compatibility paths considered?

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
