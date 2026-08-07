# CLI Application Profile

## Purpose

Use when arguments, environment, standard streams, exit status, filesystem effects, and process behavior define the product contract for people or automation.

## Priority and defaults

Correctness and usability precede compatibility, reliability, security, maintainability, and performance.

| Core Skill | Mode | Rationale |
| --- | --- | --- |
| `code-clarity` | `balanced` | Keep command flow and effects visible. |
| `contracts-and-errors` | `strict-boundaries` | Parse external invocation and inputs. |
| `state-and-side-effects` | `single-owner-mutation` | Coordinate filesystem and remote effects. |
| `api-and-compatibility` | `external-api` | Treat automation-visible behavior as contract. |
| `dependencies-and-boundaries` | `framework-native` | Prefer direct process conventions. |
| `testing-strategy` | `integration-balanced` | Exercise process-level behavior. |
| `safe-change` | `compatibility-first` | Protect documented automation contracts. |

## Policy

Define argument, environment, input, output, diagnostic, and exit contracts. Machine output MUST be separable from diagnostics. Noninteractive operation MUST NOT depend on prompts. Consequential actions SHOULD support preview, explicit scope, interruption handling, and actionable partial-failure reporting. Secrets MUST NOT be exposed through diagnostics or unsafe invocation channels.

Common modifiers are `public-api`, `strict-backward-compatibility`, and `security-sensitive`. This profile does not prescribe command syntax or a terminal interface.
