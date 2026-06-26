# Drift Detection

Run after every implementation task and before final delivery.

## File Scope

Check:

```bash
git diff --stat
git diff -- <allowed roots>
```

Also inspect whether forbidden roots changed. If the repo has no git, use filesystem timestamps and manual diff tools.

## Drift Checklist

Stop and resolve if any answer is yes:

- Did the task modify files outside the plan's allowed map?
- Did it touch explicitly forbidden roots?
- Did it add an unrequested feature?
- Did it change public API, CLI, UI, event, data, or config contracts without approval?
- Did it weaken auth, authorization, validation, error handling, or audit behavior?
- Did it remove, skip, or weaken tests?
- Did it introduce hardcoded secrets, mock-only behavior, fake production data, or temporary logic?
- Did it create migration or compatibility risk?
- Did it add user-visible text without localization or accessibility checks when relevant?
- Did it change deployment, CI, env vars, or build output unexpectedly?
- Did it leave unfinished markers or vague instructions?

## Drift Report

```text
Drift check:
- Changed roots:
- Forbidden roots touched: yes/no
- Public contracts changed: yes/no
- Security/validation weakened: yes/no
- Tests weakened or skipped: yes/no
- New user-visible strings checked: yes/no/not applicable
- Decision: continue | fix drift | ask user
```
