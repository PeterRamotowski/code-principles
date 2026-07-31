---
id: arrange-act-assert
name: Arrange–Act–Assert
classification: testing-pattern
category: testing-and-verification
status: candidate
source: principles/entries/arrange-act-assert.yaml
generated: true
---

# Arrange–Act–Assert

> Structure a test around preparation, one primary action, and verification.

## Canonical interpretation

Use AAA to make intent and the behavior under test visible.

## Purpose

Structure a test around preparation, one primary action, and verification.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not force asynchronous or property-based tests into unnatural formatting.
- Do not treat comments for each section as mandatory.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- `given-when-then`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `one-logical-behaviour-per-test`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

Prepare an account, perform withdrawal, then verify balance and event.

## Counterexample

Interleave many unrelated actions and assertions with no clear focus.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/arrange-act-assert.yaml` and regenerate the compendium instead of editing this file directly.
