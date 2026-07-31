---
id: hyrums-law
name: Hyrum’s Law
classification: law
category: api-and-evolution
status: candidate
source: principles/entries/hyrums-law.yaml
generated: true
---

# Hyrum’s Law

> With enough users, every observable behavior will be depended on by somebody.

## Canonical interpretation

Treat observable behavior as potential compatibility surface while still distinguishing intentional guarantees from accidental behavior.

## Purpose

With enough users, every observable behavior will be depended on by somebody.

## Apply when

- Consumers cannot be updated atomically with the implementation.
- Observable behavior or data formats form an external contract.

## This does not mean

- Do not conclude that change is impossible.
- Do not promise all incidental timing or formatting forever.

## Trade-offs

- Compatibility limits refactoring freedom.
- Preserving accidental behavior can accumulate long-term complexity.

## Conflicts with canonical entries

- `semantic-versioning`

## Broader policy tensions

- `refactoring-freedom`

## Reinforces canonical entries

- `backward-compatibility`
- `principle-of-least-astonishment`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Measure ecosystem usage and stage a compatibility-sensitive change.

## Counterexample

Assume an undocumented response ordering has no consumers in a mature API.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/hyrums-law.yaml` and regenerate the compendium instead of editing this file directly.
