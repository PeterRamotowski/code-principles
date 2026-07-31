# Principle Selection and Interpretation

## Purpose

The orchestrator does not activate all catalogue entries equally. It selects Core Skills first, then uses their modes to determine which principles are active, constrained, or suppressed for the task.

## Procedure

1. Select task-relevant Core Skills.
2. Resolve each Skill mode from profile, modifiers, adapters, and overrides.
3. Load primary and supporting principle IDs owned by those Skills.
4. Apply canonical rejected interpretations.
5. Resolve conflicts using protected quality attributes and precedence.
6. Record material interpretations in the resolved policy.

## Status values

- `active` — directly guides the task.
- `constrained` — applies, but a conflict or stronger requirement limits its use.
- `suppressed` — a normally relevant heuristic is intentionally not applied in this context.

## Example

For a small internal prototype, `yagni` may be active, `dry` constrained to duplicated authoritative knowledge, and `open-closed-principle` suppressed for speculative extension points.
