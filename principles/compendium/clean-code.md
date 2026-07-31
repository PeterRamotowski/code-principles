---
id: clean-code
name: Clean Code
classification: umbrella-concept
category: umbrella-concepts
status: candidate
source: principles/entries/clean-code.yaml
generated: true
---

# Clean Code

> A broad label for readable, maintainable, intention-revealing code.

## Canonical interpretation

Translate the label into precise rules such as naming, cohesion, explicit contracts, and bounded complexity.

## Purpose

A broad label for readable, maintainable, intention-revealing code.

## Apply when

- A broad family of related practices needs a shared vocabulary.
- The concept is used as an index into more precise rules.

## This does not mean

- Do not treat one author’s style preferences as universal law.
- Do not cite “clean code” instead of identifying a concrete problem.

## Trade-offs

- Umbrella labels can hide disagreements about their actual meaning.
- They must not replace concrete context-sensitive guidance.

## Conflicts with canonical entries

- `performance-budgeting`

## Broader policy tensions

- `framework-convention`

## Reinforces canonical entries

- `boy-scout-rule`
- `meaningful-names`
- `small-functions`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Explain that a method hides a side effect and propose an explicit command.

## Counterexample

Reject code solely because a function exceeds an arbitrary length.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/clean-code.yaml` and regenerate the compendium instead of editing this file directly.
