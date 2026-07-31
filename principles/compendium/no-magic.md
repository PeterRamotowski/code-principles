---
id: no-magic
name: No Magic
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/no-magic.yaml
generated: true
---

# No Magic

> Avoid unexplained values, hidden side effects, and non-obvious conventions.

## Canonical interpretation

Behavior that materially affects correctness should be discoverable from code, types, configuration, or documented conventions.

## Purpose

Avoid unexplained values, hidden side effects, and non-obvious conventions.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not reject metaprogramming categorically.
- Do not replace every literal with a constant when it has no independent meaning.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `framework-convention`

## Reinforces canonical entries

- `explicit-over-implicit`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

Use a named timeout constant tied to an external protocol requirement.

## Counterexample

Use `86417` in several places with no explanation or unit.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/no-magic.yaml` and regenerate the compendium instead of editing this file directly.
