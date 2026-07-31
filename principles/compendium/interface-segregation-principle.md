---
id: interface-segregation-principle
name: Interface Segregation Principle
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/interface-segregation-principle.yaml
generated: true
---

# Interface Segregation Principle

> Prefer focused consumer-oriented contracts over broad interfaces.

## Canonical interpretation

Consumers should not depend on operations they cannot or should not use.

## Purpose

Prefer focused consumer-oriented contracts over broad interfaces.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not create a separate one-method interface for every method automatically.
- Do not fragment a cohesive protocol that is always implemented and consumed together.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `common-reuse-principle`

## Broader policy tensions

- `api-stability`

## Reinforces canonical entries

- `dependency-inversion-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

A reporting consumer depends only on read operations.

## Counterexample

A cache client must implement unrelated queue and metrics methods.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/interface-segregation-principle.yaml` and regenerate the compendium instead of editing this file directly.
