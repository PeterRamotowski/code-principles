---
id: immutability
name: Immutability
classification: design-property
category: state-data-and-distribution
status: candidate
source: principles/entries/immutability.yaml
generated: true
---

# Immutability

> Prefer values that do not change after construction where this reduces reasoning and concurrency risk.

## Canonical interpretation

Use immutability selectively for values, messages, and shared state; controlled mutation may be clearer or more efficient for entities and hot paths.

## Purpose

Prefer values that do not change after construction where this reduces reasoning and concurrency risk.

## Apply when

- State changes, retries, concurrency, or distribution can affect correctness.
- The system needs explicit semantics for commands, queries, and consistency.

## This does not mean

- Do not clone large structures blindly.
- Do not pretend mutable frameworks or ORMs are immutable through superficial wrappers.

## Trade-offs

- Immutability and separation can increase allocation or coordination cost.
- Distributed guarantees usually require operational complexity and failure handling.

## Conflicts with canonical entries

- `performance-budgeting`

## Broader policy tensions

- `orm-conventions`

## Reinforces canonical entries

- `command-query-separation`
- `make-illegal-states-unrepresentable`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `state-and-side-effects`

## Positive example

Use an immutable Money value and replace it as a whole.

## Counterexample

Copy a multi-gigabyte buffer for every small update without a budget.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/immutability.yaml` and regenerate the compendium instead of editing this file directly.
