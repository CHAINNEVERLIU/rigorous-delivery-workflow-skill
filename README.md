# Rigorous Delivery Workflow Skill

A Codex skill for taking software work from request clarification to verified delivery with stateful long-task recovery, no-context implementation planning, external AI review/implementation handoff prompts, multi-round review ledgers, drift detection, testing, and final evidence gates.

## Install

Install the skill from this repository:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo CHAINNEVERLIU/rigorous-delivery-workflow-skill --path skills/rigorous-delivery-workflow
```

On macOS or Linux:

```bash
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo CHAINNEVERLIU/rigorous-delivery-workflow-skill --path skills/rigorous-delivery-workflow
```

Restart Codex after installation.

## Use

Ask Codex to use the skill when a software request needs commercial-grade delivery discipline:

```text
Use $rigorous-delivery-workflow to run this request through stateful planning, review, implementation, drift checks, external AI handoff when needed, and final verification.
```

The skill is technology-agnostic and applies to frontend, backend, full-stack, CLI, scripts, infrastructure, refactors, bugfixes, and security work.

It is designed for long or interruptible tasks. It includes delivery state templates, low-capability external AI prompt templates, skill-routing guidance, TDD RED/GREEN classification, failure-mode review, verification matrices, and scripts for red-flag, changed-file, drift, and state checks.

## Validate

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\rigorous-delivery-workflow"
python ".\skills\rigorous-delivery-workflow\scripts\scan-red-flags.py" ".\skills\rigorous-delivery-workflow" --include-code
python ".\skills\rigorous-delivery-workflow\scripts\state-check.py" "<path-to-delivery-state.md>"
python -m pytest ".\tests\test_rigorous_delivery_workflow_skill.py" -q
```

## Layout

```text
skills/rigorous-delivery-workflow/
  SKILL.md
  agents/openai.yaml
  references/
    delivery-state-template.md
    external-*-prompt-low-intelligence.md
    review-ledger.md
    verification-matrix.md
    ...
  scripts/
    scan-red-flags.py
    changed-files.py
    verify-drift.py
    state-check.py
tests/
  test_rigorous_delivery_workflow_skill.py
```
