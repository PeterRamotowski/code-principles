---
id: test-pyramid
name: Test Pyramid
classification: testing-strategy
category: testing-and-verification
status: candidate
source: principles/entries/test-pyramid.yaml
generated: true
---

# Test Pyramid

> Use many fast focused tests, fewer integration tests, and a small number of broad end-to-end tests as a starting heuristic.

## Canonical interpretation

Choose the test distribution according to architecture and failure risk rather than enforcing a fixed geometric ratio.

## Purpose

Use many fast focused tests, fewer integration tests, and a small number of broad end-to-end tests as a starting heuristic.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not mock every boundary merely to increase unit-test count.
- Do not treat slow end-to-end coverage as a substitute for focused diagnostics.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `framework-integration`
- `testing-trophy`

## Reinforces canonical entries

- `first-tests`
- `test-behaviour-not-implementation`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

Test pure rules directly, database boundaries through integration tests, and critical journeys end to end.

## Counterexample

Replace all meaningful integration tests with mocks to preserve a pyramid shape.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/test-pyramid.yaml` and regenerate the compendium instead of editing this file directly.
