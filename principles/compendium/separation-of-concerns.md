---
id: separation-of-concerns
name: Separation of Concerns
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/separation-of-concerns.yaml
generated: true
---

# Separation of Concerns

> Separate responsibilities that represent different concerns or change drivers.

## Canonical interpretation

A component should not combine unrelated policy, presentation, persistence, and infrastructure decisions without a clear reason.

## Purpose

Separate responsibilities that represent different concerns or change drivers.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not require one layer or class per concern.
- Do not separate code that must be understood and changed together.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `locality-of-behaviour`
- `performance-budgeting`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `high-cohesion-low-coupling`
- `single-responsibility-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Keep rendering separate from payment authorization policy.

## Counterexample

Mix database queries, HTML rendering, and authorization decisions in one handler.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/separation-of-concerns.yaml` and regenerate the compendium instead of editing this file directly.
