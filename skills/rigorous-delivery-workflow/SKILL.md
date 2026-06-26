---
name: rigorous-delivery-workflow
description: Use when a software request needs commercial-grade delivery quality, no-context execution readiness, long-task continuity, external AI review/implementation handoff, production hardening, strict review, verified handoff, or resilient execution across frontend, backend, full-stack, CLI, scripts, infrastructure, refactors, bugfixes, or security work.
---

# Rigorous Delivery Workflow

Use this skill as a delivery controller, not as a long checklist. Keep state explicit, route to the right specialist skills, verify with fresh evidence, and make every external review or implementation result auditable.

## Non-Negotiables

- Maintain a delivery state artifact for non-trivial or interruptible work.
- Do not rely on conversation memory when a state artifact exists. Read it before resuming.
- Do not start implementation until the spec and implementation plan have converged, unless the user explicitly asks for exploratory code.
- Prefer autonomous progress over repeated confirmation. Ask the user only for real blockers, destructive actions, credentials, production release, paid external actions, or explicit scope conflicts.
- Do not let external AI, subagents, or previous summaries decide completion. Treat their output as evidence to verify.
- Do not claim completion without fresh verification after the last relevant change.
- Do not weaken security, authorization, validation, error handling, audit behavior, or existing tests to pass a task.
- Do not expand scope silently. If scope changes, update state and mark invalidated verification.

## State Machine

For substantial work, create or update a state file before deep work:

```text
docs/superpowers/plans/YYYY-MM-DD-<slug>.state.md
```

If the repository uses another planning location, use the local convention. Load `references/delivery-state-template.md`.

Phases:

1. `bootstrap_state`: capture objective, latest user instruction, scope, allowed/forbidden paths, assumptions, and next single action.
2. `clarify_or_assume`: ask only blocking questions; otherwise record assumptions and continue.
3. `draft_spec`: load `references/spec-template.md`.
4. `self_review_spec`: load `references/spec-self-review.md`; converge P0/P1 to zero.
5. `external_review_handoff`: when requested, load `references/external-ai-handoff.md` and the low-intelligence review prompt.
6. `draft_plan`: load `references/implementation-plan-template.md`; make it no-context executable.
7. `execute_plan`: load `references/execution-protocol.md`, `references/skill-routing-matrix.md`, `references/tdd-red-green-rules.md`, and domain skills as needed.
8. `drift_check`: load `references/drift-detection.md`; run after each task and before final delivery.
9. `final_review`: load `references/final-delivery-review.md`, `references/verification-matrix.md`, and `references/failure-mode-review.md`.
10. `external_validation_handoff`: when requested, generate a low-intelligence validation prompt and ask the user to paste the full result back.

At every phase transition, update the state file's `Current Phase`, `Verification Ledger`, `Drift Ledger`, `Review Findings Ledger`, and `Next Single Action`.

## Interruptions And Autonomy

Load `references/autonomy-and-interruptions.md` when:

- the user asks unrelated questions mid-task,
- the user changes scope,
- context was compacted or another agent resumes,
- external AI results are expected or returned,
- the work is long enough that state drift is plausible.

Default behavior:

- Answer short side questions, then return to `Next Single Action`.
- If the user starts a new task, ask whether to pause the active delivery workflow.
- If a new instruction conflicts with scope, update state and mark stale plan/test evidence.
- If the user asks for an external AI prompt, generate it and explicitly tell the user to paste back the complete external AI output.

## External AI And Subagents

Use external AI prompts when the user wants another AI to review, implement, or validate. Load:

- `references/external-ai-handoff.md`
- `references/external-review-prompt-low-intelligence.md`
- `references/external-implementation-prompt-low-intelligence.md`
- `references/external-validation-prompt-low-intelligence.md`
- `references/review-ledger.md`

Rules:

- Prompts must be no-context and strong enough for a low-capability AI: explicit role, scope, forbidden paths, exact artifacts, step machine, output template, blocked protocol, and completion bans.
- After emitting an external AI prompt, tell the user: "Paste the external AI's complete output back here; do not paste only a summary. I will verify it and import valid findings into the review ledger."
- External AI implementation is only a candidate implementation. Re-read diffs, run tests, check drift, and verify evidence before accepting it.

Use subagents only for independent work with clear boundaries. Load `references/subagent-protocol.md`. The main agent must review outputs and evidence before accepting them.

## Skill Routing

Before each major phase, load the smallest useful skill set. Load `references/skill-routing-matrix.md`.

Required routing examples:

- Review feedback: use receiving-code-review or an equivalent manual ledger.
- Implementation: use executing-plans and test-driven-development when available.
- Test failure or unexpected behavior: use systematic-debugging before fixing.
- Frontend/browser work: use frontend-testing-debugging, React best-practice, Playwright, or equivalent skills when available.
- Completion claim: use verification-before-completion or the final delivery review manually.

If a matching skill is unavailable, record the manual equivalent in the checkpoint.

## Execution Gates

Each implementation task must:

1. Restate the task and allowed files.
2. Add or update tests first.
3. Run the focused test and classify RED using `references/tdd-red-green-rules.md`.
4. Fix invalid REDs before implementation.
5. Implement the smallest correct change.
6. Run focused GREEN verification.
7. Run related regression verification.
8. Run drift detection.
9. Review failure modes, security, contracts, and dirty worktree impact.
10. Update state and emit a checkpoint.

## Final Completion Gate

Do not claim completion if any of these is true:

- Required verification was not run and no accepted reason is recorded.
- Any P0/P1 finding remains unresolved.
- Public contracts changed without approval or versioning.
- Security, validation, authorization, or audit behavior is weakened.
- Default quality gates depend on external services they do not start themselves.
- External AI or subagent findings were not mapped into the review ledger.
- Untracked source files, generated artifacts, or dirty worktree changes are not reported.
- Drift detection has unresolved forbidden-path, scope, or test-weakening findings.
- The final evidence matrix is missing.

Load `references/final-delivery-review.md` and `references/verification-matrix.md` before final response.

## Resource Guide

- `references/delivery-state-template.md`: create or resume a delivery state.
- `references/autonomy-and-interruptions.md`: handle user interruptions, scope changes, and long-task recovery.
- `references/spec-template.md`: draft a behavior/contract/security/test spec.
- `references/spec-self-review.md`: self-review spec and plan until convergence.
- `references/implementation-plan-template.md`: write a no-context implementation plan.
- `references/execution-protocol.md`: execute task-by-task with evidence.
- `references/skill-routing-matrix.md`: select specialist skills and tools.
- `references/tdd-red-green-rules.md`: classify valid and invalid RED/GREEN cycles.
- `references/failure-mode-review.md`: review write ordering, half-success, auth, idempotency, and contract failure paths.
- `references/drift-detection.md`: detect scope, contract, security, and artifact drift.
- `references/verification-matrix.md`: classify required verification and external-service prerequisites.
- `references/final-delivery-review.md`: produce the final evidence and delivery verdict.
- `references/external-ai-handoff.md`: coordinate external AI review/implementation/validation.
- `references/external-review-prompt-low-intelligence.md`: generate robust external review prompts.
- `references/external-implementation-prompt-low-intelligence.md`: generate robust external implementation prompts.
- `references/external-validation-prompt-low-intelligence.md`: generate robust external validation prompts.
- `references/review-ledger.md`: import review findings skeptically and close them with evidence.
- `references/subagent-protocol.md`: delegate independent work without losing control.
- `scripts/scan-red-flags.py`: scan changed or explicit files for unfinished markers.
- `scripts/changed-files.py`: list changed and untracked files for handoff or final review.
- `scripts/verify-drift.py`: check changed files against allowed/forbidden roots.
- `scripts/state-check.py`: check delivery state completeness.
