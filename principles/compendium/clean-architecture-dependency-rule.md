---
id: clean-architecture-dependency-rule
name: Clean Architecture Dependency Rule
classification: architecture-rule
category: architecture-and-dependencies
status: candidate
source: principles/entries/clean-architecture-dependency-rule.yaml
generated: true
---

# Clean Architecture Dependency Rule

> Source-code dependencies should point toward higher-level policy.

## Canonical interpretation

Use inward dependency direction where protecting policy from frameworks and infrastructure provides measurable independence.

## Purpose

Source-code dependencies should point toward higher-level policy.

## Apply when

- High-level policy must evolve independently from volatile infrastructure.
- Dependency direction affects testability, deployability, or independent ownership.

## This does not mean

- Do not require the complete Clean Architecture template.
- Do not prohibit useful framework types from all application code by default.

## Trade-offs

- Indirection and adapters have a maintenance cost.
- Framework isolation is valuable only where independent evolution is required.

## Conflicts with canonical entries

- `yagni`

## Broader policy tensions

- `framework-native-design`

## Reinforces canonical entries

- `dependency-inversion-principle`
- `ports-and-adapters`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `dependencies-and-boundaries`

## Positive example

Keep complex domain rules independent of a specific database driver.

## Counterexample

Build five layers around a simple framework-native form handler.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/clean-architecture-dependency-rule.yaml` and regenerate the compendium instead of editing this file directly.
