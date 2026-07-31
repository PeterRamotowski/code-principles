---
id: open-closed-principle
name: Open/Closed Principle
classification: principle
category: abstraction-and-reuse
status: candidate
source: principles/entries/open-closed-principle.yaml
generated: true
---

# Open/Closed Principle

> Allow known variation through stable extension points without repeatedly editing stable policy.

## Canonical interpretation

Design for extension where evidence identifies a durable axis of variation; do not generalize for imaginary cases.

## Purpose

Allow known variation through stable extension points without repeatedly editing stable policy.

## Apply when

- Knowledge or policy is duplicated in ways that can diverge.
- A stable variation axis or public extension boundary has been demonstrated.

## This does not mean

- Do not make every class extensible.
- Do not forbid modification of internal code.
- Do not use inheritance as the default extension mechanism.

## Trade-offs

- An abstraction introduces coupling between its consumers.
- Premature reuse can make independently changing concepts harder to modify.

## Conflicts with canonical entries

- `backward-compatibility`
- `kiss`
- `yagni`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `dependency-inversion-principle`
- `information-hiding`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `abstraction-and-reuse`

## Positive example

A public formatter accepts registered output strategies with a stable contract.

## Counterexample

Add factories, registries, and hooks to a private one-case helper.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/open-closed-principle.yaml` and regenerate the compendium instead of editing this file directly.
