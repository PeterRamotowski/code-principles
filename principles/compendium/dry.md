---
id: dry
name: DRY
classification: principle
category: abstraction-and-reuse
status: candidate
source: principles/entries/dry.yaml
generated: true
---

# DRY

> Avoid duplicating authoritative knowledge, policy, and decisions.

## Canonical interpretation

Each important rule should have one authoritative representation, while similar syntax may remain separate when it represents different concepts.

## Purpose

Avoid duplicating authoritative knowledge, policy, and decisions.

## Apply when

- Knowledge or policy is duplicated in ways that can diverge.
- A stable variation axis or public extension boundary has been demonstrated.

## This does not mean

- Do not eliminate every repeated code shape.
- Do not create an abstraction after the first duplication.
- Do not merge concepts that are expected to change independently.

## Trade-offs

- An abstraction introduces coupling between its consumers.
- Premature reuse can make independently changing concepts harder to modify.

## Conflicts with canonical entries

- `locality-of-behaviour`
- `yagni`

## Broader policy tensions

- `independent-changeability`

## Reinforces canonical entries

- `single-source-of-truth`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `abstraction-and-reuse`

## Positive example

Centralize one tax rule used by several entry points.

## Counterexample

Force unrelated address formats through one generic mapper because their fields look similar.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/dry.yaml` and regenerate the compendium instead of editing this file directly.
