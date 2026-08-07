# Infrastructure Tool Profile

## Purpose

Use for provisioning, deployment, migration, or operational automation that observes and mutates consequential shared infrastructure.

## Priority and defaults

Safety and correctness precede reliability, security, operability, and maintainability.

| Core Skill | Mode | Rationale |
| --- | --- | --- |
| `code-clarity` | `explicit-critical-path` | Expose plans, effects, and rollback limits. |
| `contracts-and-errors` | `safety-critical` | Validate authority and consequential input. |
| `dependencies-and-boundaries` | `component-based` | Isolate provider and environment contracts. |
| `state-and-side-effects` | `single-owner-mutation` | Coordinate plans and shared state changes. |
| `api-and-compatibility` | `external-api` | Protect automation-visible plans and results. |
| `distributed-reliability` | `idempotent-ingress` | Make repeat application safe where promised. |
| `testing-strategy` | `integration-balanced` | Exercise plans and provider boundaries. |
| `safe-change` | `compatibility-first` | Preserve state and provide migration paths. |

## Policy

Separate observation, planning, approval, application, and verification. A plan MUST expose target, scope, authority, destructive effects, assumptions, and rollback limits. Revalidate material preconditions before applying stale plans. Operations MUST be idempotent or clearly report why repetition is unsafe. Use least privilege and preserve an audit trail without secrets.

Common modifiers are `security-sensitive`, `strict-backward-compatibility`, and `public-api`. This profile does not prescribe a provider or configuration language.
