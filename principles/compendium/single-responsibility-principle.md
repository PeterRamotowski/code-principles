---
id: single-responsibility-principle
name: Single Responsibility Principle
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/single-responsibility-principle.yaml
generated: true
---

# Single Responsibility Principle

> Give a module one cohesive responsibility or primary reason to change.

## Canonical interpretation

Responsibility is defined by change ownership and purpose, not by method count or file size.

## Purpose

Give a module one cohesive responsibility or primary reason to change.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not interpret SRP as one method per class.
- Do not split a cohesive domain concept across arbitrary layers.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `locality-of-behaviour`
- `small-functions`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `common-closure-principle`
- `separation-of-concerns`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

A pricing policy changes for pricing rules, not email formatting.

## Counterexample

A `UserManager` handles authentication, billing, exports, and notifications.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/single-responsibility-principle.yaml` and regenerate the compendium instead of editing this file directly.
