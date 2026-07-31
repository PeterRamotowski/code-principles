---
id: avoid-accidental-complexity
name: Avoid Accidental Complexity
classification: principle
category: simplicity-and-clarity
status: candidate
source: principles/entries/avoid-accidental-complexity.yaml
generated: true
---

# Avoid Accidental Complexity

> Minimize complexity introduced by implementation choices rather than the problem itself.

## Canonical interpretation

Distinguish essential domain complexity from avoidable tooling, layering, and coordination overhead.

## Purpose

Minimize complexity introduced by implementation choices rather than the problem itself.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not label difficult business rules as accidental complexity.
- Do not remove abstractions that protect real boundaries.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `architecture-isolation`
- `extensibility`

## Reinforces canonical entries

- `kiss`
- `yagni`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

Represent a simple workflow with explicit steps rather than a generic rule engine.

## Counterexample

Introduce event sourcing to avoid writing a small transactional update.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/avoid-accidental-complexity.yaml` and regenerate the compendium instead of editing this file directly.
