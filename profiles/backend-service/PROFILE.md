# Backend Service Profile

## Purpose and intended artifacts

Use this profile for a long-running server artifact whose primary role is serving network requests or application operations. Intended artifacts own service contracts, transactions, integrations, concurrency, and operational behavior.

Server execution alone is insufficient when another artifact type controls the task's lifecycle and risks.

## Priority order

1. correctness;
2. data integrity;
3. reliability under failure;
4. security;
5. operability;
6. maintainability;
7. measured performance.

## Default Core Skill modes

| Core Skill | Mode | Profile rationale |
| --- | --- | --- |
| `code-clarity` | `balanced` | Keep transactions, effects, and failure paths visible. |
| `abstraction-and-reuse` | `balanced` | Centralize verified service policy without designing speculative service platforms. |
| `modular-design` | `service-oriented` | Align boundaries with cohesive ownership and an independently operated lifecycle. |
| `contracts-and-errors` | `strict-boundaries` | Parse untrusted requests and integration results at their boundaries. |
| `state-and-side-effects` | `single-owner-mutation` | Give consequential state transitions a clear owner. |
| `testing-strategy` | `integration-balanced` | Exercise contracts, transactions, and integrations as well as local logic. |
| `distributed-reliability` | `synchronous-transactional` | Prefer the simplest verified consistency model until distributed behavior is required. |
| `safe-change` | `local-safe-change` | Limit ordinary changes and verify observable service behavior. |

## Typical risks

- partial failure across state and external effects;
- unsafe retry, timeout, cancellation, and concurrency behavior;
- accepting invalid or unauthorized requests;
- leaking implementation failures through unstable contracts;
- insufficient operational evidence for diagnosis and recovery;
- premature distribution of cohesive responsibilities.

## Common modifiers

- `security-sensitive` and `multi-tenant` strengthen authority and isolation;
- `high-throughput` and `latency-sensitive` activate measured resource budgets;
- `public-api` governs externally consumed contracts.

## Prohibited default assumptions

- Do not infer microservices from the word service, repository size, or domain vocabulary.
- Do not infer asynchronous processing from possible future scale.
- Do not retry an operation until duplicate effects and ownership are understood.
- Do not make internal modules remote merely to strengthen separation.
- Do not treat logs as a substitute for explicit error and recovery semantics.

## Non-goals

This profile does not prescribe microservices, message-driven architecture, a transport, a persistence model, or a deployment platform.

## Profile decision example

When two operations repeat one transaction policy, `abstraction-and-reuse: balanced` permits centralizing the verified policy while `modular-design: service-oriented` keeps it inside the cohesive service owner. It does not create a public extension point: the reusable-library profile resolves that same DRY-versus-YAGNI conflict differently when independent consumers need supported variation.
