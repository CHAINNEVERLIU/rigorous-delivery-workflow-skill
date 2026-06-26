# Rigorous Delivery Workflow Skill

A Codex skill for taking software work from request clarification to verified delivery with strict spec writing, no-context implementation planning, multi-round review, drift detection, testing, and final handoff.

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
Use $rigorous-delivery-workflow to turn this request into a verified delivery.
```

The skill is technology-agnostic and applies to frontend, backend, full-stack, CLI, scripts, infrastructure, refactors, bugfixes, and security work.

## Validate

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\rigorous-delivery-workflow"
python ".\skills\rigorous-delivery-workflow\scripts\scan-red-flags.py" ".\skills\rigorous-delivery-workflow\SKILL.md" ".\skills\rigorous-delivery-workflow\references" ".\skills\rigorous-delivery-workflow\scripts\scan-red-flags.py"
python -m pytest ".\tests\test_rigorous_delivery_workflow_skill.py" -q
```

## Layout

```text
skills/rigorous-delivery-workflow/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/scan-red-flags.py
tests/
  test_rigorous_delivery_workflow_skill.py
```
