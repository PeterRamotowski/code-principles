---
id: explicit-over-implicit
name: Explicit Is Better Than Implicit
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/explicit-over-implicit.yaml
generated: true
---

# Explicit Is Better Than Implicit

> Make important dependencies, state changes, defaults, and control flow visible.

## Canonical interpretation

Prefer explicit behavior when hidden conventions would make correctness or maintenance harder to reason about.

## Purpose

Make important dependencies, state changes, defaults, and control flow visible.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not reject well-established language or framework conventions merely because they are implicit.
- Do not make every default noisy when it is safe and universally understood.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `conciseness`
- `framework-convention`

## Reinforces canonical entries

- `no-magic`
- `principle-of-least-astonishment`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

Inject a required dependency and name a transaction boundary.

## Counterexample

Create a dependency through a hidden global lookup during method execution.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/explicit-over-implicit.yaml` and regenerate the compendium instead of editing this file directly.
