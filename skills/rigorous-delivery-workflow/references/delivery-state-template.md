# Delivery State Template

Use this for any long, interruptible, externally reviewed, or no-context handoff task. Keep it current. Read it before resuming after user interruption, context compaction, external AI output, or subagent output.

```markdown
# <Task Name> Delivery State

Objective:

Latest User Instruction:

Current Phase:
- bootstrap_state | clarify_or_assume | draft_spec | self_review_spec | external_review_handoff | draft_plan | execute_plan | drift_check | final_review | external_validation_handoff | complete | blocked

In Scope:
- 

Out of Scope:
- 

Allowed Paths:
- 

Forbidden Paths:
- 

Accepted Assumptions:
- 

Decision Log:
| Date/Turn | Decision | Reason | Made By |
| --- | --- | --- | --- |

External Handoffs:
| ID | Type | Prompt Path/Content | Sent | Returned | Imported Findings | Status |
| --- | --- | --- | --- | --- | --- | --- |

Review Findings Ledger:
| ID | Source | Severity | Finding | Accepted | Required Change | Required Test | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Execution Checklist:
| Step | Status | Evidence | Notes |
| --- | --- | --- | --- |

Verification Ledger:
| Command/Check | Purpose | Result | Fresh After Last Relevant Change | Notes |
| --- | --- | --- | --- | --- |

Drift Ledger:
| Check | Result | Evidence | Action |
| --- | --- | --- | --- |

Invalidated Verification:
| Evidence | Invalidated By | Needs Rerun |
| --- | --- | --- |

Dirty Worktree / Untracked Files:
- 

Current Blocker:
- none

Next Single Action:
- 

Completion Criteria:
- P0/P1 findings closed.
- Required verification matrix complete.
- Drift check passes or accepted risks are explicit.
- Final delivery review complete.
```

## Update Rules

- Update `Latest User Instruction` whenever the user changes direction.
- Update `Current Phase` before starting a new phase.
- Add every external AI or subagent handoff to `External Handoffs`.
- Add every review finding to `Review Findings Ledger` before implementing fixes.
- Mark verification stale in `Invalidated Verification` after any later change that could affect it.
- Keep `Next Single Action` to one concrete action, not a broad plan.
