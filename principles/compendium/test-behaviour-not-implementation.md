---
id: test-behaviour-not-implementation
name: Test Behaviour, Not Implementation
classification: testing-principle
category: testing-and-verification
status: candidate
source: principles/entries/test-behaviour-not-implementation.yaml
generated: true
---

# Test Behaviour, Not Implementation

> Prefer assertions on observable contracts over private structure.

## Canonical interpretation

Tests should protect behavior while allowing safe refactoring of implementation details.

## Purpose

Prefer assertions on observable contracts over private structure.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not avoid verifying important interactions at architectural boundaries.
- Do not interpret “behavior” as only UI output.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `interaction-testing`
- `white-box-performance-testing`

## Reinforces canonical entries

- `backward-compatibility`
- `hyrums-law`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

Verify returned value, persisted state, and published event.

## Counterexample

Assert the exact sequence of private helper calls in a pure calculation.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/test-behaviour-not-implementation.yaml` and regenerate the compendium instead of editing this file directly.
