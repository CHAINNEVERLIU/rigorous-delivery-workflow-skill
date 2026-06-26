---
name: rigorous-delivery-workflow
description: Use when a software request needs commercial-grade delivery quality, no-context execution readiness, production hardening, strict review, or verified handoff across frontend, backend, full-stack, CLI, scripts, infrastructure, refactors, bugfixes, or security work.
---

# Rigorous Delivery Workflow

## Purpose

Use this skill to run software work from request to delivery with explicit gates. It is technology-agnostic: discover the repo, stack, tests, and risks before selecting project-specific commands.

## Non-Negotiables

- Do not start implementation until the spec and implementation plan have converged, unless the user explicitly asks for exploratory code.
- Do not claim completion without fresh verification evidence.
- Do not review only what the user names. Review commercial readiness, regressions, security, compatibility, operations, tests, docs, and future extension.
- Do not let a local pass hide cross-surface impact. Check any affected API, CLI, UI, data format, config, docs, deployment, and tests.
- Do not weaken security, authorization, validation, error handling, or existing tests to pass a task.
- Do not expand scope silently. If scope changes, stop and record the decision needed.

## Workflow

### 1. Clarify Request

Identify:
- goal and user value,
- in-scope and out-of-scope work,
- target users and key workflows,
- existing constraints and compatibility promises,
- likely affected surfaces,
- acceptance criteria and required evidence.

If the user asks to proceed without answers, record assumptions and risks.

Set artifact paths before drafting. Prefer the repository's existing spec/plan location. If none exists, use `docs/specs/YYYY-MM-DD-<slug>-spec.md` and `docs/specs/YYYY-MM-DD-<slug>-implementation-plan.md`. Do not overwrite unrelated planning artifacts.

### 2. Write Spec

Create a spec before implementation for non-trivial work. Load `references/spec-template.md`.

The spec must define behavior, contracts, errors, data, security, compatibility, tests, rollout, and non-goals.

### 3. Self-Review Spec Until Converged

Load `references/spec-self-review.md`. Run repeated review passes until:
- P0 = 0,
- P1 = 0,
- every P2 is fixed or explicitly accepted with rationale,
- every success criterion has verification evidence planned,
- `scripts/scan-red-flags.py` reports no hits on the spec.

Revise the spec after each pass. Record the review rounds.

### 4. Write No-Context Implementation Plan

Load `references/implementation-plan-template.md`.

The plan must be executable by an agent with no conversation history. Include:
- exact files to inspect, create, or modify,
- exact tests to add,
- exact commands to run,
- order of tasks,
- focused and regression verification,
- drift checks,
- final handoff format.

Avoid vague instructions. Include code examples where incorrect implementation is likely.

Then self-review the plan against `references/spec-self-review.md` (it covers both spec and plan) until the same convergence rule is met and `scripts/scan-red-flags.py` reports no hits on the plan. Do not advance to external review with an unreviewed plan.

### 5. Request External Review

Load `references/external-review-prompt.md`.

Generate a prompt for another reviewer to adversarially inspect the spec and plan for:
- no-context executability,
- commercial delivery gaps,
- missing tests,
- compatibility regressions,
- security or data risks,
- scope creep,
- future rework risk.

Ingest review feedback with technical skepticism. Verify each finding against the repo. Fix valid findings and rerun self-review.

### 6. Execute Plan

Load `references/execution-protocol.md` and `references/skill-selection.md`.

At the start of each major phase:
- inspect available skills/tools,
- load the smallest useful set,
- do not invent unavailable tools,
- use manual equivalents when a tool is absent.

Execute task-by-task:
1. write or update tests first,
2. run the focused failing test when practical,
3. implement the smallest correct change,
4. run focused verification,
5. run related regression verification,
6. run drift checks,
7. review the diff against the spec, plan, contracts, security, and commercial readiness risks,
8. update the plan checklist,
9. emit a checkpoint.

Use subagents only for independent work with clear file boundaries or independent review. Main agent must review diffs, evidence, and scope before accepting any subagent output.

### 7. Detect Drift

Load `references/drift-detection.md`.

Run drift checks after every task and before final delivery. Stop if implementation:
- touches excluded areas,
- adds unrequested features,
- changes public contracts without approval,
- weakens security or validation,
- skips planned tests,
- leaves vague markers,
- breaks non-code surfaces.

### 8. Final Delivery Review

Load `references/final-delivery-review.md`.

Before final response:
- run full verification commands and capture fresh evidence (do not reuse earlier or subagent-reported results),
- review diff scope,
- rerun self-review until convergence,
- run `scripts/scan-red-flags.py` on the spec, plan, and any new delivery artifacts,
- list unrun tests and reasons,
- report residual risks,
- state whether the work meets the delivery bar.

## Severity Scale

- P0: security breach, data loss, authorization bypass, destructive action, production unusable, or explicit out-of-scope implementation.
- P1: core workflow broken, contract regression, missing critical test, or major user-visible failure.
- P2: deliverable but with clear maintainability, coverage, compatibility, or future-extension risk.
- P3: wording, organization, polish, or minor robustness improvement.

## Resource Guide

- `references/spec-template.md`: use when drafting a spec.
- `references/spec-self-review.md`: use when reviewing a spec or plan for convergence.
- `references/implementation-plan-template.md`: use when writing a no-context execution plan.
- `references/external-review-prompt.md`: use when asking another AI or human to review a spec/plan.
- `references/execution-protocol.md`: use when executing a plan.
- `references/drift-detection.md`: use after every implementation task.
- `references/final-delivery-review.md`: use before claiming delivery.
- `references/skill-selection.md`: use when deciding which skills/tools/subagents to load.
- `scripts/scan-red-flags.py`: run on specs/plans/reports to catch vague wording and unfinished markers.

## Red-Flag Scan

Run the scanner on generated specs and plans when Python is available:

```bash
python path/to/rigorous-delivery-workflow/scripts/scan-red-flags.py path/to/spec.md path/to/plan.md
```

The scanner fails on missing paths and is case-insensitive by default. Fix every hit unless it is inside a deliberate quoted example or a documented false positive.
