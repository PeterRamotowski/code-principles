---
id: kiss
name: KISS
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/kiss.yaml
generated: true
---

# KISS

> Prefer the simplest design that correctly satisfies verified requirements.

## Canonical interpretation

Choose the least complicated solution that preserves correctness, safety, and required quality attributes.

## Purpose

Prefer the simplest design that correctly satisfies verified requirements.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not equate simplicity with the fewest lines of code.
- Do not remove necessary validation, error handling, or domain rules.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- `backward-compatibility`
- `open-closed-principle`
- `performance-budgeting`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `avoid-accidental-complexity`
- `yagni`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

Use a direct function and explicit validation for a small stable workflow.

## Counterexample

Introduce a plugin framework for one known implementation.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/kiss.yaml` and regenerate the compendium instead of editing this file directly.
