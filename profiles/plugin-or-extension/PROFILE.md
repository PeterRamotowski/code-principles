# Plugin or Extension Profile

## Purpose

Use for independently released code loaded through a host's supported extension contract. Host lifecycle, coexistence, authority, and version compatibility dominate; framework use alone does not select this profile.

## Priority and defaults

Compatibility and correctness precede isolation, security, maintainability, reliability, and measured performance.

| Core Skill | Mode | Rationale |
| --- | --- | --- |
| `code-clarity` | `balanced` | Make lifecycle and host interactions visible. |
| `abstraction-and-reuse` | `extensible-public-library` | Offer only supported extension variation. |
| `modular-design` | `library-oriented` | Keep the public extension surface cohesive. |
| `contracts-and-errors` | `strict-boundaries` | Treat host data and callbacks as contracts. |
| `dependencies-and-boundaries` | `component-based` | Separate provided and required host contracts. |
| `state-and-side-effects` | `single-owner-mutation` | Respect host-owned and extension-owned state. |
| `api-and-compatibility` | `public-library` | Govern independently upgraded consumers and hosts. |
| `testing-strategy` | `integration-balanced` | Exercise lifecycle and compatibility boundaries. |
| `safe-change` | `compatibility-first` | Preserve supported host behavior or migrate it. |

## Policy

Use supported registration, activation, deactivation, configuration, and cleanup paths. The extension MUST NOT assume ownership of host startup, global state, or unrelated extensions. Declare host compatibility and degrade only where behavior remains safe and explicit. Isolate failures and release registered resources.

Common modifiers are `public-api`, `strict-backward-compatibility`, and `security-sensitive`. This profile does not prescribe a host, marketplace, or plugin architecture.
