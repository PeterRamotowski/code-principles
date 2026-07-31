---
id: acyclic-dependencies-principle
name: Acyclic Dependencies Principle
classification: principle
category: architecture-and-dependencies
status: candidate
source: principles/entries/acyclic-dependencies-principle.yaml
generated: true
---

# Acyclic Dependencies Principle

> Keep component dependency graphs free of cycles at meaningful architectural boundaries.

## Canonical interpretation

Cycles between independently evolving modules signal unclear ownership or misplaced abstractions.

## Purpose

Keep component dependency graphs free of cycles at meaningful architectural boundaries.

## Apply when

- High-level policy must evolve independently from volatile infrastructure.
- Dependency direction affects testability, deployability, or independent ownership.

## This does not mean

- Do not treat every runtime object reference as an architectural cycle.
- Do not introduce a shared junk module merely to break a cycle.

## Trade-offs

- Indirection and adapters have a maintenance cost.
- Framework isolation is valuable only where independent evolution is required.

## Conflicts with canonical entries

- `locality-of-behaviour`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `high-cohesion-low-coupling`
- `stable-dependencies-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `dependencies-and-boundaries`

## Positive example

Extract a stable contract or relocate ownership to remove a feature-module cycle.

## Counterexample

Create mutual imports between billing and orders that require coordinated releases.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/acyclic-dependencies-principle.yaml` and regenerate the compendium instead of editing this file directly.
