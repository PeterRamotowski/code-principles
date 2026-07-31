---
id: cqrs
name: Command Query Responsibility Segregation
classification: architecture-pattern
category: state-data-and-distribution
status: candidate
source: principles/entries/cqrs.yaml
generated: true
---

# Command Query Responsibility Segregation

> Use different models or paths for reads and writes when their requirements materially diverge.

## Canonical interpretation

Adopt CQRS only when scale, security, workflow, or representation differences justify operational complexity.

## Purpose

Use different models or paths for reads and writes when their requirements materially diverge.

## Apply when

- State changes, retries, concurrency, or distribution can affect correctness.
- The system needs explicit semantics for commands, queries, and consistency.

## This does not mean

- Do not apply CQRS to every CRUD application.
- Do not assume CQRS requires event sourcing.

## Trade-offs

- Immutability and separation can increase allocation or coordination cost.
- Distributed guarantees usually require operational complexity and failure handling.

## Conflicts with canonical entries

- `kiss`

## Broader policy tensions

- `immediate-consistency`
- `transactional-simplicity`

## Reinforces canonical entries

- `command-query-separation`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `state-and-side-effects`

## Positive example

Use a dedicated read model for a high-volume analytical view with different authorization.

## Counterexample

Split every table operation into command buses and projections without a demonstrated need.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/cqrs.yaml` and regenerate the compendium instead of editing this file directly.
