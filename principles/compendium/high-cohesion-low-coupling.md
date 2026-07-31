---
id: high-cohesion-low-coupling
name: High Cohesion, Low Coupling
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/high-cohesion-low-coupling.yaml
generated: true
---

# High Cohesion, Low Coupling

> Keep related behavior together while minimizing knowledge between modules.

## Canonical interpretation

A strong module owns a coherent concept and exposes a small explicit contract.

## Purpose

Keep related behavior together while minimizing knowledge between modules.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not eliminate all coupling; software components must collaborate.
- Do not maximize cohesion by creating an oversized module around an entire application.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `single-source-of-truth`

## Broader policy tensions

- `distribution`

## Reinforces canonical entries

- `information-hiding`
- `separation-of-concerns`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

A feature module owns its workflow and exposes a narrow application API.

## Counterexample

Every class imports shared globals and reaches into other modules’ internals.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/high-cohesion-low-coupling.yaml` and regenerate the compendium instead of editing this file directly.
