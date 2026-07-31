---
id: dependency-inversion-principle
name: Dependency Inversion Principle
classification: principle
category: architecture-and-dependencies
status: candidate
source: principles/entries/dependency-inversion-principle.yaml
generated: true
---

# Dependency Inversion Principle

> High-level policy should not depend directly on volatile low-level details.

## Canonical interpretation

Both policy and details should meet at an abstraction justified by an independent evolution boundary.

## Purpose

High-level policy should not depend directly on volatile low-level details.

## Apply when

- High-level policy must evolve independently from volatile infrastructure.
- Dependency direction affects testability, deployability, or independent ownership.

## This does not mean

- Do not create an interface for every class.
- Do not invert stable language or framework primitives without value.

## Trade-offs

- Indirection and adapters have a maintenance cost.
- Framework isolation is valuable only where independent evolution is required.

## Conflicts with canonical entries

- `kiss`
- `performance-budgeting`

## Broader policy tensions

- `framework-native-design`

## Reinforces canonical entries

- `information-hiding`
- `open-closed-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `dependencies-and-boundaries`

## Positive example

A billing use case depends on a payment port because providers vary independently.

## Counterexample

A private date formatter gets an interface, factory, and container registration.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/dependency-inversion-principle.yaml` and regenerate the compendium instead of editing this file directly.
