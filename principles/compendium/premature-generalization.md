---
id: premature-generalization
name: Avoid Premature Generalization
classification: heuristic
category: abstraction-and-reuse
status: candidate
source: principles/entries/premature-generalization.yaml
generated: true
---

# Avoid Premature Generalization

> Delay general-purpose abstractions until commonality and variation are understood.

## Canonical interpretation

Prefer concrete duplication over a wrong shared abstraction when the concepts are still evolving independently.

## Purpose

Delay general-purpose abstractions until commonality and variation are understood.

## Apply when

- Knowledge or policy is duplicated in ways that can diverge.
- A stable variation axis or public extension boundary has been demonstrated.

## This does not mean

- Do not ignore obvious stable platform boundaries.
- Do not use this heuristic to avoid refactoring proven duplication.

## Trade-offs

- An abstraction introduces coupling between its consumers.
- Premature reuse can make independently changing concepts harder to modify.

## Conflicts with canonical entries

- `dry`
- `open-closed-principle`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `yagni`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `abstraction-and-reuse`

## Positive example

Keep two evolving importers separate until their shared protocol is stable.

## Counterexample

Build a universal importer framework from one data source.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/premature-generalization.yaml` and regenerate the compendium instead of editing this file directly.
