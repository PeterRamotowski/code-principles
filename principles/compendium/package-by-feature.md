---
id: package-by-feature
name: Package by Feature
classification: organizational-principle
category: modularity-and-object-design
status: candidate
source: principles/entries/package-by-feature.yaml
generated: true
---

# Package by Feature

> Organize top-level code around capabilities or business features rather than only technical layers.

## Canonical interpretation

Feature-oriented grouping improves ownership and change locality when features evolve independently.

## Purpose

Organize top-level code around capabilities or business features rather than only technical layers.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not forbid technical sublayers inside a feature.
- Do not apply feature packaging to a small library whose public concepts are not application features.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `common-reuse-principle`

## Broader policy tensions

- `shared-infrastructure`

## Reinforces canonical entries

- `common-closure-principle`
- `high-cohesion-low-coupling`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Place order use cases, policies, and adapters under an orders module.

## Counterexample

Put all controllers, all services, and all repositories in global folders in a large domain application.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/package-by-feature.yaml` and regenerate the compendium instead of editing this file directly.
