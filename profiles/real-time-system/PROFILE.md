# Real-time or Embedded System Profile

## Purpose

Use when timing and bounded resource use are part of correctness. Ordinary user-facing responsiveness does not select this profile.

## Priority and defaults

Correctness, determinism, reliability, and safety precede memory efficiency, performance, and maintainability.

| Core Skill | Mode | Rationale |
| --- | --- | --- |
| `code-clarity` | `explicit-critical-path` | Make timing and ownership constraints visible. |
| `contracts-and-errors` | `safety-critical` | Contain invariant and authority failures. |
| `dependencies-and-boundaries` | `component-based` | Make component resource contracts explicit. |
| `state-and-side-effects` | `single-owner-mutation` | Prevent critical-path ownership ambiguity. |
| `performance-and-resources` | `hard-real-time` | Verify worst-case bounded behavior. |
| `testing-strategy` | `hardware-integration` | Include target timing and integration evidence. |
| `safe-change` | `compatibility-first` | Preserve system contracts and verification assumptions. |

## Policy

Critical paths MUST define deadlines, worst-case work, blocking, allocation, synchronization, and failure state. Average latency is not deadline evidence. Resources SHOULD be acquired and sized outside critical paths where possible. Ownership and lifetime MUST be explicit across interrupts, callbacks, threads, devices, and shutdown.

Common modifiers are `real-time`, `memory-sensitive`, `latency-sensitive`, and `security-sensitive`. This profile does not provide certification or prescribe hardware, scheduling, or implementation language.
