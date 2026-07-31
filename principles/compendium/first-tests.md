---
id: first-tests
name: FIRST Tests
classification: umbrella-concept
category: testing-and-verification
status: candidate
source: principles/entries/first-tests.yaml
generated: true
---

# FIRST Tests

> Tests should be fast, independent, repeatable, self-verifying, and timely.

## Canonical interpretation

Use FIRST as a quality lens while recognizing that some integration tests are necessarily slower.

## Purpose

Tests should be fast, independent, repeatable, self-verifying, and timely.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not reject valuable tests because they are not unit-fast.
- Do not interpret independence as forbidding shared fixture construction.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `real-system-integration`

## Reinforces canonical entries

- `test-pyramid`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

A test controls its data, reports a clear result, and can run repeatedly.

## Counterexample

A test depends on execution order and a developer’s local clock.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/first-tests.yaml` and regenerate the compendium instead of editing this file directly.
