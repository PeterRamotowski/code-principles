---
id: red-green-refactor
name: Red–Green–Refactor
classification: development-cycle
category: testing-and-verification
status: candidate
source: principles/entries/red-green-refactor.yaml
generated: true
---

# Red–Green–Refactor

> Create a failing test, make it pass minimally, then improve structure while preserving behavior.

## Canonical interpretation

Use the cycle as a disciplined feedback loop where TDD is active.

## Purpose

Create a failing test, make it pass minimally, then improve structure while preserving behavior.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not skip refactoring indefinitely.
- Do not implement unsafe shortcuts in the green phase that violate nonfunctional requirements.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- `performance-budgeting`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `boy-scout-rule`
- `test-driven-development`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

Add a failing edge case, implement it, then remove duplication.

## Counterexample

Add implementation without observing the test fail, leaving uncertainty that the test is meaningful.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/red-green-refactor.yaml` and regenerate the compendium instead of editing this file directly.
