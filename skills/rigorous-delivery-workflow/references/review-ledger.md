# Review Ledger

Use this for self-review, user review, external AI review, subagent review, and post-implementation validation. Do not absorb review feedback as prose. Convert it into trackable findings.

## Finding Format

```markdown
### <ID>: <short title>

Source: self | user | external-ai | subagent | test-failure
Severity: P0 | P1 | P2 | P3
Status: open | accepted | rejected | fixed | verified | accepted-risk

Finding:

Evidence:

Why it matters:

Accepted:
- yes | no | partial

Rationale:

Required code change:

Required test:

Verification command:

Verification result:

Residual risk:
```

## Import Rules

- Verify each finding against repo artifacts before accepting.
- Reject findings that are unsupported, stale, or out of scope, but record the rationale.
- A valid finding without a test plan is incomplete unless it is documentation-only.
- Do not mark fixed until code/docs/tests are updated.
- Do not mark verified until fresh verification runs after the fix.

## Severity Reminder

- P0: security breach, data loss, destructive action, auth bypass, production unusable, or explicit out-of-scope implementation.
- P1: core workflow broken, public contract regression, missing critical test, or major user-visible failure.
- P2: deliverable but with clear coverage, maintainability, compatibility, or future-extension risk.
- P3: wording, organization, polish, or minor robustness improvement.
