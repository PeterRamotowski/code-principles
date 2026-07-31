---
id: test-driven-development
name: Test-Driven Development
classification: development-method
category: testing-and-verification
status: candidate
source: principles/entries/test-driven-development.yaml
generated: true
---

# Test-Driven Development

> Use tests to drive small design and implementation increments.

## Canonical interpretation

Choose TDD when it improves feedback and design; it is a method, not a universal moral requirement.

## Purpose

Use tests to drive small design and implementation increments.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not require test-first work for exploratory spikes or generated migrations.
- Do not confuse TDD with comprehensive testing by itself.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `exploratory-design`
- `legacy-constraints`
- `ui-experimentation`

## Reinforces canonical entries

- `red-green-refactor`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

Drive a parser rule through a failing example, minimal implementation, and refactoring.

## Counterexample

Write brittle tests first for an interface that is still being experimentally discovered.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/test-driven-development.yaml` and regenerate the compendium instead of editing this file directly.
