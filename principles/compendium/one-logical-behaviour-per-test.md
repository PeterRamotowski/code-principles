---
id: one-logical-behaviour-per-test
name: One Logical Behaviour per Test
classification: testing-heuristic
category: testing-and-verification
status: candidate
source: principles/entries/one-logical-behaviour-per-test.yaml
generated: true
---

# One Logical Behaviour per Test

> Keep each test focused on one coherent behavior, allowing multiple related assertions.

## Canonical interpretation

A test may assert several facets of one outcome; assertion count alone does not define focus.

## Purpose

Keep each test focused on one coherent behavior, allowing multiple related assertions.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not require exactly one assertion statement.
- Do not split one behavior into many tests that duplicate expensive setup without benefit.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `test-runtime-cost`

## Reinforces canonical entries

- `arrange-act-assert`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

Assert status, payload, and audit event produced by one command.

## Counterexample

Test successful creation, deletion, permissions, and retries in one case.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/one-logical-behaviour-per-test.yaml` and regenerate the compendium instead of editing this file directly.
