---
id: common-closure-principle
name: Common Closure Principle
classification: principle
category: abstraction-and-reuse
status: candidate
source: principles/entries/common-closure-principle.yaml
generated: true
---

# Common Closure Principle

> Group elements that change for the same reasons and at the same times.

## Canonical interpretation

A package should concentrate the impact of a likely class of change.

## Purpose

Group elements that change for the same reasons and at the same times.

## Apply when

- Knowledge or policy is duplicated in ways that can diverge.
- A stable variation axis or public extension boundary has been demonstrated.

## This does not mean

- Do not group code only because it has the same technical layer.
- Do not predict remote future changes without evidence.

## Trade-offs

- An abstraction introduces coupling between its consumers.
- Premature reuse can make independently changing concepts harder to modify.

## Conflicts with canonical entries

- `common-reuse-principle`
- `package-by-feature`

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

Keep a feature’s policy, validation, and related adapters in one module when they evolve together.

## Counterexample

Place all validators in one global package despite unrelated business ownership.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/common-closure-principle.yaml` and regenerate the compendium instead of editing this file directly.
