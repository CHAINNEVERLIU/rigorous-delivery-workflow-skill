# Spec Template

Use this template for non-trivial software work before implementation.

## Title

`<feature-or-change-name>` Spec

## Goal

State the user-visible outcome in one paragraph.

## Background

- Existing system behavior:
- Current pain or gap:
- Stakeholders or users:
- Why now:

## Scope

In scope:
- <specific deliverable or behavior>

Out of scope:
- <explicitly excluded behavior or surface>

Do not leave scope implicit. If a surface might be affected, list whether it is in or out.

## Affected Surfaces

Check all that apply and name exact files or modules when known:

- UI:
- API:
- CLI:
- database/schema:
- background jobs:
- config/env:
- auth/security:
- observability/logging:
- documentation:
- tests/CI:
- deployment:

## Functional Requirements

Use numbered, testable statements.

1. The system must <positive behavior>.
2. The system must reject <invalid or unsafe behavior>.
3. The system must preserve <existing contract or workflow>.

## Non-Functional Requirements

- Security:
- Privacy:
- Performance:
- Reliability:
- Accessibility:
- Internationalization/localization:
- Backward compatibility:
- Operational safety:

## Contracts

Define any public API, CLI, event, file, data, database, config, or UI contract.

For each contract:
- name:
- owner:
- consumers:
- request/input:
- response/output:
- error behavior:
- backward compatibility rule:

## State, Data, and Migration

- Existing data model:
- New fields or tables:
- Migration strategy:
- Rollback or recovery:
- Idempotency:
- Data retention:

## Error Handling

For each major failure mode:
- condition:
- user-visible behavior:
- machine-readable code:
- retry behavior:
- logging/observability:
- security redaction:

## Security and Authorization

- Authentication requirements:
- Authorization checks:
- Tenant/project/user boundaries:
- Abuse cases:
- Secrets handling:
- Audit requirements:

## Rollout, Deployment, and Operations

- Feature flags or configuration:
- Deployment steps:
- Backward/forward compatibility:
- Monitoring and alerts:
- Rollback or recovery:
- Runbook or operator action:

## Testing Requirements

List exact categories:

- unit:
- contract:
- integration:
- end-to-end:
- browser/UI:
- migration:
- security:
- regression:
- performance:
- manual smoke:

## Acceptance Criteria

Each criterion must map to evidence:

| Criterion | Evidence |
| --- | --- |
| <criterion> | <test, command, review, or manual smoke evidence> |

## Risks and Open Questions

| Risk or Question | Severity | Required Resolution |
| --- | --- | --- |
| <risk or question> | P0/P1/P2/P3 | <decision, fix, or owner> |

## Delivery Bar

Define what must be true before the task is considered deliverable.
