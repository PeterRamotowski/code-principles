---
id: stable-dependencies-principle
name: Stable Dependencies Principle
classification: principle
category: architecture-and-dependencies
status: candidate
source: principles/entries/stable-dependencies-principle.yaml
generated: true
---

# Stable Dependencies Principle

> Dependencies should generally point toward components that change less often.

## Canonical interpretation

A volatile module should not become a foundation for more stable policy without an isolating boundary.

## Purpose

Dependencies should generally point toward components that change less often.

## Apply when

- High-level policy must evolve independently from volatile infrastructure.
- Dependency direction affects testability, deployability, or independent ownership.

## This does not mean

- Do not assume low change frequency automatically means good design.
- Do not freeze unstable modules to satisfy the rule.

## Trade-offs

- Indirection and adapters have a maintenance cost.
- Framework isolation is valuable only where independent evolution is required.

## Conflicts with canonical entries

- `package-by-feature`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `acyclic-dependencies-principle`
- `dependency-inversion-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `dependencies-and-boundaries`

## Positive example

Domain policy does not depend on a vendor SDK that changes frequently.

## Counterexample

A public library exposes experimental framework internals in its API.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/stable-dependencies-principle.yaml` and regenerate the compendium instead of editing this file directly.
