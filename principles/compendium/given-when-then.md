---
id: given-when-then
name: Given–When–Then
classification: testing-pattern
category: testing-and-verification
status: candidate
source: principles/entries/given-when-then.yaml
generated: true
---

# Given–When–Then

> Describe behavior through context, event, and outcome.

## Canonical interpretation

Use the structure when scenario language improves shared understanding, especially for acceptance behavior.

## Purpose

Describe behavior through context, event, and outcome.

## Apply when

- Behavior must remain correct through change.
- Risk, complexity, or public contracts justify automated verification.

## This does not mean

- Do not duplicate a verbose scenario DSL for trivial unit tests.
- Do not mistake readable wording for complete assertions.

## Trade-offs

- Tests can over-couple to implementation details.
- A testing method that improves one feedback loop can slow another.

## Conflicts with canonical entries

- `arrange-act-assert`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `test-behaviour-not-implementation`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `testing-strategy`

## Positive example

Given an expired token, when a request is made, then access is denied.

## Counterexample

Write a scenario that asserts internal method-call order rather than user-visible behavior.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/given-when-then.yaml` and regenerate the compendium instead of editing this file directly.
