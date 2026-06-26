# External AI Handoff

Use when the user wants another AI to review, implement, or validate. External AI output is not authoritative. It is evidence to verify.

## When To Generate A Prompt

Generate a no-context external AI prompt when:
- the user asks another AI to review spec/plan,
- the user asks another AI to implement a plan,
- the user asks another AI to validate an implementation,
- current context is too long and a handoff is useful,
- an adversarial second opinion is requested.

## Prompt Requirements

Every prompt must include:
- role and hard constraints,
- explicit statement that no conversation context is available,
- objective,
- in-scope and out-of-scope work,
- allowed and forbidden paths,
- relevant artifacts or full text snippets,
- required skills or equivalent manual workflow,
- ordered steps,
- required tests and expected evidence,
- drift checks,
- blocked protocol,
- completion bans,
- exact output template.

## User Instruction After Prompt

After generating the prompt, tell the user:

```text
Paste the external AI's complete output back here; do not paste only a summary. I will verify each finding, update the review ledger, and decide what to change or rerun.
```

## Importing Returned Output

When the user pastes external AI output:

1. Add it to `External Handoffs` in the state file.
2. Convert each finding into `Review Findings Ledger` format.
3. Verify each finding against repo artifacts.
4. Mark each finding accepted, rejected, or partial with rationale.
5. Add required tests and verification commands.
6. Implement only accepted findings.
7. Rerun fresh verification after changes.

## External Implementation Rule

If external AI implemented code, treat it as a candidate implementation:
- inspect the full diff,
- inspect untracked files,
- check allowed/forbidden paths,
- run tests yourself,
- check for mock-only shortcuts, weakened assertions, and skipped tests,
- generate a fresh evidence matrix before accepting.
