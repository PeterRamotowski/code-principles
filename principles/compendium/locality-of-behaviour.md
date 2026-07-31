---
id: locality-of-behaviour
name: Locality of Behaviour
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/locality-of-behaviour.yaml
generated: true
---

# Locality of Behaviour

> Place behavior near the data, UI, or concept it primarily affects.

## Canonical interpretation

Optimize for local understanding while preserving meaningful module boundaries.

## Purpose

Place behavior near the data, UI, or concept it primarily affects.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not duplicate authoritative business rules in every caller.
- Do not use locality to bypass encapsulation or security boundaries.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `dry`
- `separation-of-concerns`
- `small-functions`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `high-cohesion-low-coupling`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Keep component-specific state transitions with the component or its composable.

## Counterexample

Move every small behavior into a distant global utility package.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/locality-of-behaviour.yaml` and regenerate the compendium instead of editing this file directly.
