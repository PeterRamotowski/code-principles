---
id: conways-law
name: Conway’s Law
classification: law
category: change-and-engineering-systems
status: candidate
source: principles/entries/conways-law.yaml
generated: true
---

# Conway’s Law

> System structures tend to reflect communication structures of their organizations.

## Canonical interpretation

Use organizational boundaries as an architectural input and review misalignment between ownership and dependencies.

## Purpose

System structures tend to reflect communication structures of their organizations.

## Apply when

- The project is being evolved, modernized, reviewed, or reorganized.
- Organizational and historical context affects technical outcomes.

## This does not mean

- Do not treat the law as deterministic.
- Do not restructure teams solely to mimic a fashionable architecture.

## Trade-offs

- Local improvement can enlarge the scope and risk of a change.
- Organizational laws are diagnostic lenses, not deterministic commands.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `idealized-architecture`

## Reinforces canonical entries

- `high-cohesion-low-coupling`
- `package-by-feature`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Align module ownership with teams that can change and deploy it coherently.

## Counterexample

Design tightly coupled services owned by teams that cannot coordinate effectively.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/conways-law.yaml` and regenerate the compendium instead of editing this file directly.
