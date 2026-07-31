---
id: encapsulation
name: Encapsulation
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/encapsulation.yaml
generated: true
---

# Encapsulation

> Control access to state and preserve invariants through a deliberate interface.

## Canonical interpretation

Encapsulation protects valid transitions; it is not merely private fields with unrestricted setters.

## Purpose

Control access to state and preserve invariants through a deliberate interface.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not equate encapsulation with object-oriented syntax.
- Do not hide data that is intentionally a transparent value record.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `data-transfer-objects`
- `serialization`

## Reinforces canonical entries

- `information-hiding`
- `make-illegal-states-unrepresentable`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

A domain object exposes operations that preserve its valid status transitions.

## Counterexample

Private fields are paired with setters that permit every invalid state.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/encapsulation.yaml` and regenerate the compendium instead of editing this file directly.
