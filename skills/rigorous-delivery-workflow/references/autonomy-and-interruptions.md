# Autonomy And Interruptions

Use this when the task is long, the user interrupts, context was compacted, external AI is involved, or the agent is tempted to ask repeated questions.

## Ask The User Only For Real Blockers

Ask before:
- destructive filesystem, git, database, or production actions,
- credential, secret, account, or payment decisions,
- production deployment or public release,
- explicit scope conflicts,
- security or compliance tradeoffs that cannot be inferred from repo context.

Do not ask for:
- ordinary file organization,
- how to fix lint/typecheck/test failures,
- how to add planned tests,
- non-destructive debugging,
- code style decisions covered by the repo,
- whether to run planned verification.

If input would help but is not blocking, record an assumption in state and continue.

## User Interruption Protocol

- Short side question: answer briefly, then state the next action from the delivery state and continue.
- New unrelated task: ask whether to pause the active delivery workflow.
- Scope change: update state, mark affected plan/test evidence invalidated, and continue only after the new scope is explicit.
- External AI result pasted back: import findings into the review ledger before accepting or rejecting them.
- Status request: report current phase, latest evidence, next action, and keep moving unless the user asks to pause.

## Resume Protocol

Before resuming after interruption or compaction:

1. Read the state file.
2. Confirm the latest user instruction.
3. Check whether any verification is stale.
4. Check dirty worktree and untracked files if code changed.
5. Continue from `Next Single Action`.

Do not restart from memory if state exists.
