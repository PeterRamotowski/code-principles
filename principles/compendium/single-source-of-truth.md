---
id: single-source-of-truth
name: Single Source of Truth
classification: principle
category: abstraction-and-reuse
status: candidate
source: principles/entries/single-source-of-truth.yaml
generated: true
---

# Single Source of Truth

> Give each authoritative fact or policy one canonical owner.

## Canonical interpretation

Derived views may be duplicated, but authority and synchronization rules must be explicit.

## Purpose

Give each authoritative fact or policy one canonical owner.

## Apply when

- Knowledge or policy is duplicated in ways that can diverge.
- A stable variation axis or public extension boundary has been demonstrated.

## This does not mean

- Do not require all data to live in one physical database.
- Do not confuse caching or denormalization with multiple authorities when reconciliation is defined.

## Trade-offs

- An abstraction introduces coupling between its consumers.
- Premature reuse can make independently changing concepts harder to modify.

## Conflicts with canonical entries

- `eventual-consistency`

## Broader policy tensions

- `availability`

## Reinforces canonical entries

- `dry`
- `information-hiding`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `abstraction-and-reuse`

## Positive example

Store the canonical status once and derive presentation labels.

## Counterexample

Allow two services to independently decide the same business status without reconciliation.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/single-source-of-truth.yaml` and regenerate the compendium instead of editing this file directly.
