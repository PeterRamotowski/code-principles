---
id: small-functions
name: Small Functions
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/small-functions.yaml
generated: true
---

# Small Functions

> Prefer functions that represent one coherent operation and can be understood locally.

## Canonical interpretation

Function size should follow conceptual cohesion, not a universal line limit.

## Purpose

Prefer functions that represent one coherent operation and can be understood locally.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not split cohesive logic into fragments that require constant jumping.
- Do not count lines as a substitute for reviewing responsibility.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- `locality-of-behaviour`
- `single-level-of-abstraction`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `single-responsibility-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

Extract a meaningful `calculateTax()` operation with its complete rule.

## Counterexample

Create ten one-line wrappers that hide a straightforward calculation.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/small-functions.yaml` and regenerate the compendium instead of editing this file directly.
