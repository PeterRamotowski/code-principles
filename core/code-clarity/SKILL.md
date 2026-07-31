# Code Clarity and Simplicity

## Purpose

Turn verified behavior into code that a maintainer can understand and change safely. This Skill governs
local naming, explicitness, control flow, conceptual level, and accidental complexity. It does not choose
system architecture or impose syntax-specific style.

## Activation and inputs

Activate when code is created, modified, refactored, or reviewed and local comprehension is material.
Use the task scope, architecture authority, existing conventions, criticality, and measured constraints.
Generated artifacts not intended for manual maintenance are excluded.

## Decision procedure

1. State the behavior, invariants, side effects, and failure outcomes that a reader must see.
2. Remove complexity that is neither required by the problem nor justified by evidence.
3. Choose names that communicate domain role, units, and distinctions; do not encode incidental mechanics.
4. Keep one primary conceptual level per operation, but extract only when the new name and boundary improve
   understanding.
5. Make consequential defaults, dependencies, state transitions, and side effects explicit.
6. Follow established conventions unless they hide material behavior or violate a higher-priority rule.
7. Record any clarity sacrificed for compatibility, measured performance, or generated-code constraints.

The result MUST preserve required behavior. It MUST NOT use brevity, function length, or a named principle
as a substitute for a concrete comprehension benefit.

## Modes

### `minimal`

Use for narrow fixes and low-risk maintenance. Change only what is necessary for the requested behavior;
small directly supporting name or dead-code improvements MAY accompany it. Do not reorganize unrelated code.

### `balanced`

Use by default. Improve names, visible flow, and conceptual structure inside the touched behavior. Repetition
MAY remain when it preserves locality or represents independently changing concepts.

### `explicit-critical-path`

Use when safety, authorization, money, data integrity, or difficult recovery makes hidden behavior costly.
Dependencies, state transitions, defaults, validation, and failures MUST be directly traceable. Concision is
secondary to auditability.

## Conflict decisions

### Clarity versus abstraction

- Decision: whether to extract repeated-looking code.
- Protected qualities: local comprehension and authoritative knowledge ownership.
- Default: keep syntax local until shared knowledge and common change are demonstrated.
- Change the resolution when duplicated policy can diverge or a stable shared boundary already exists.

### Clarity versus modular separation

- Decision: whether to move behavior away from the data or workflow it explains.
- Protected qualities: locality and cohesive ownership.
- Default: keep behavior near its primary concept and introduce the smallest meaningful boundary.
- Change the resolution when separate change drivers, access control, or deployment boundaries are verified.

### Clarity versus optimization

- Decision: whether measured resource needs justify a less direct implementation.
- Protected qualities: maintainability and required performance or resource bounds.
- Default: retain the clearest correct implementation.
- Change the resolution when representative measurements show a budget violation and the optimized behavior
  can be isolated, explained, and verified.

## Outputs and review

Produce the chosen mode, key comprehension decisions, suppressed complexity, and any explicit trade-off.
Review that names carry meaning, control flow is traceable, hidden side effects are absent, abstraction levels
are coherent, and every non-obvious complexity has evidence.

See [decision examples](examples/scenarios.md). Evaluations:
`code-clarity-balanced-local-change`, `code-clarity-critical-path-boundary`, and
`code-clarity-helper-overengineering`.

## Non-goals

This Skill MUST NOT mandate small functions, comments, object orientation, design patterns, or repository-wide
cleanup. It MUST NOT override compatibility, safety, or measured resource requirements.
