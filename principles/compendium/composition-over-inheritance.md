---
id: composition-over-inheritance
name: Composition over Inheritance
classification: heuristic
category: modularity-and-object-design
status: candidate
source: principles/entries/composition-over-inheritance.yaml
generated: true
---

# Composition over Inheritance

> Prefer assembling behavior from collaborators over deep implementation inheritance.

## Canonical interpretation

Use inheritance when there is genuine behavioral substitutability or a required framework contract; otherwise prefer composition.

## Purpose

Prefer assembling behavior from collaborators over deep implementation inheritance.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not prohibit inheritance categorically.
- Do not replace a simple subtype with excessive delegation ceremony.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `performance-budgeting`

## Broader policy tensions

- `framework-inheritance`

## Reinforces canonical entries

- `information-hiding`
- `liskov-substitution-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Compose validation strategies into a service.

## Counterexample

Create a six-level class hierarchy to share a few helper methods.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/composition-over-inheritance.yaml` and regenerate the compendium instead of editing this file directly.
