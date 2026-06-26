# No-Context Implementation Plan Template

## Contents

- Header
- Execution rules
- State and ledger requirements
- File map
- Verification matrix
- Task structure
- External AI implementation hook
- Acceptance matrix
- Self-review

Use after the spec has converged. The plan must be executable by an agent with no conversation history and robust enough for low-capability external AI if copied into a handoff prompt.

## Header

```markdown
# <Feature Name> Implementation Plan

Goal:
Approved spec:
Delivery state:
Current repo roots:
Tech stack discovered:
Primary user workflows:
```

## Execution Rules

Include:
- allowed file roots,
- forbidden file roots,
- public contracts that must not break,
- security and authorization rules,
- data safety and failure-mode rules,
- compatibility rules,
- required specialist skills or manual equivalents,
- required verification commands,
- external-service prerequisites,
- drift checks,
- completion criteria.

## State And Ledger Requirements

Require the implementer to update:
- delivery state,
- review findings ledger,
- execution checklist,
- verification ledger,
- drift ledger,
- invalidated verification.

## File Map

| File | Action | Responsibility | Risk |
| --- | --- | --- | --- |
| path | create/modify/test/docs | reason | low/medium/high |

## Verification Matrix

For every command:

| Command | Purpose | Scope | Starts Own Services | Requires External Service | CI Default | Pass Condition |
| --- | --- | --- | --- | --- | --- | --- |

Default quality gates must not depend on external services unless they start them.

## Task Structure

Every task must include:

- purpose,
- files,
- tests to add/update,
- expected RED,
- implementation instructions,
- focused GREEN,
- regression verification,
- failure-mode review,
- drift check,
- state updates.

Example:

````markdown
### Task N: <name>

Purpose:

Files:
- Test:
- Modify:

Allowed paths:
- 

Forbidden paths:
- 

- [ ] Add/update test first.

```<language>
<exact or near-exact test sketch when useful>
```

- [ ] Run focused RED:

```bash
<command>
```

Expected RED:
Actual RED classification: valid | invalid | environment | regression

- [ ] Implement:
  - exact function/class/module to change,
  - contract/security constraints,
  - failure-mode constraints,
  - compatibility rule.

- [ ] Run focused GREEN:

```bash
<command>
```

- [ ] Run related regressions:

```bash
<command>
```

- [ ] Failure-mode review:
  - auth/validation before writes,
  - half-success state,
  - idempotency/retry,
  - contract/client compatibility.

- [ ] Drift check:
  - changed files,
  - forbidden paths,
  - untracked files,
  - generated artifacts,
  - public contract changes.

- [ ] Update delivery state and evidence.
````

## External AI Implementation Prompt Hook

If the plan may be handed to another AI, add:

```text
Use references/external-implementation-prompt-low-intelligence.md. Paste the external AI's complete result back into the primary thread for verification. External implementation is a candidate only.
```

## Acceptance Matrix

| Requirement | Implementation Evidence | Verification Evidence | Status |
| --- | --- | --- | --- |

## Self-Review

End with:
- traceability to spec,
- ambiguity audit,
- no-context executability audit,
- failure-mode audit,
- external-service test audit,
- scope drift audit,
- multi-round review log,
- final verdict.

Use `READY FOR IMPLEMENTATION` only after P0/P1 are zero, P2 is fixed or accepted, and red-flag/drift checks pass.
