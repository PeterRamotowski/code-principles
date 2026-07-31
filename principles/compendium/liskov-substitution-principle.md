---
id: liskov-substitution-principle
name: Liskov Substitution Principle
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/liskov-substitution-principle.yaml
generated: true
---

# Liskov Substitution Principle

> Subtypes must preserve the behavioral contract expected of the base abstraction.

## Canonical interpretation

A substitutable implementation must not strengthen preconditions, weaken guarantees, or violate observable invariants.

## Purpose

Subtypes must preserve the behavioral contract expected of the base abstraction.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not reduce LSP to matching method signatures.
- Do not force inheritance where implementations have incompatible semantics.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `performance-specialization`

## Reinforces canonical entries

- `design-by-contract`
- `principle-of-least-astonishment`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Every storage implementation preserves documented transaction and error semantics.

## Counterexample

A read-only subclass inherits a mutable base type and throws for required operations.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/liskov-substitution-principle.yaml` and regenerate the compendium instead of editing this file directly.
