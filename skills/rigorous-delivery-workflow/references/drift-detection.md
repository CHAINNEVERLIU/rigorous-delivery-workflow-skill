# Drift Detection

Run after every implementation task and before final delivery.

## Inputs

Use the plan/state to identify:
- allowed roots,
- forbidden roots,
- public contracts,
- required tests,
- generated artifacts,
- external-service test boundaries.

## Recommended Commands

If git is available:

```bash
git status --short
git diff --stat
git diff --name-only
```

If `scripts/verify-drift.py` is available:

```bash
python path/to/scripts/verify-drift.py --allow <root> --forbid <root> [--forbid <root> ...]
```

If no git is available, use filesystem timestamps and manual diff tools.

## Drift Checklist

Stop and resolve if any answer is yes without an accepted rationale:

- Did the task modify files outside the plan's allowed map?
- Did it touch explicitly forbidden roots?
- Did it add an unrequested feature?
- Did it change public API, CLI, UI, event, data, config, or file contracts without approval?
- Did it weaken auth, authorization, validation, safe errors, audit behavior, or data boundaries?
- Did it remove, skip, weaken, or reclassify tests to pass?
- Did it introduce mock-only production behavior, hardcoded secrets, fake data, or temporary logic?
- Did it create migration, rollback, compatibility, or half-success state risk?
- Did it mix external-service smoke tests into default quality gates without self-starting services?
- Did it leave untracked source files unreported?
- Did it leave generated artifacts unreported or not gitignored?
- Did later edits invalidate earlier verification?
- Did it leave unfinished markers or vague instructions?

## Drift Report

```text
Drift check:
- Changed roots:
- Forbidden roots touched: yes/no
- Public contracts changed: yes/no
- Security/validation/audit weakened: yes/no
- Tests weakened or skipped: yes/no
- External-service tests separated: yes/no/not applicable
- Untracked files:
- Generated artifacts:
- Invalidated verification:
- Decision: continue | fix drift | ask user | accepted risk
```
