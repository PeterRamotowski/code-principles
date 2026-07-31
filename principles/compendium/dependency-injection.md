---
id: dependency-injection
name: Dependency Injection
classification: technique
category: architecture-and-dependencies
status: candidate
source: principles/entries/dependency-injection.yaml
generated: true
---

# Dependency Injection

> Supply collaborators from outside a component instead of constructing hidden dependencies internally.

## Canonical interpretation

Use DI to make required dependencies explicit and lifecycle-controlled; do not use it as ceremonial indirection.

## Purpose

Supply collaborators from outside a component instead of constructing hidden dependencies internally.

## Apply when

- High-level policy must evolve independently from volatile infrastructure.
- Dependency direction affects testability, deployability, or independent ownership.

## This does not mean

- Do not inject simple immutable values through a container when direct parameters are clearer.
- Do not use service locators disguised as injection.

## Trade-offs

- Indirection and adapters have a maintenance cost.
- Framework isolation is valuable only where independent evolution is required.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `construction-simplicity`
- `framework-convention`

## Reinforces canonical entries

- `dependency-inversion-principle`
- `explicit-over-implicit`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `dependencies-and-boundaries`

## Positive example

Pass a repository into an application service constructor.

## Counterexample

Resolve a global container inside every method.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/dependency-injection.yaml` and regenerate the compendium instead of editing this file directly.
