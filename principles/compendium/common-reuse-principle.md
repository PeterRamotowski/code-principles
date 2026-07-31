---
id: common-reuse-principle
name: Common Reuse Principle
classification: principle
category: abstraction-and-reuse
status: candidate
source: principles/entries/common-reuse-principle.yaml
generated: true
---

# Common Reuse Principle

> Group reusable elements so consumers do not depend on things they do not use.

## Canonical interpretation

Package boundaries should align with actual reuse sets and release coupling.

## Purpose

Group reusable elements so consumers do not depend on things they do not use.

## Apply when

- Knowledge or policy is duplicated in ways that can diverge.
- A stable variation axis or public extension boundary has been demonstrated.

## This does not mean

- Do not split packages into tiny fragments without consumer value.
- Do not assume code used together today will always be versioned together.

## Trade-offs

- An abstraction introduces coupling between its consumers.
- Premature reuse can make independently changing concepts harder to modify.

## Conflicts with canonical entries

- `common-closure-principle`
- `package-by-feature`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `interface-segregation-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Publish a focused parsing package without unrelated storage dependencies.

## Counterexample

Require consumers of one utility to install an entire application framework.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/common-reuse-principle.yaml` and regenerate the compendium instead of editing this file directly.
