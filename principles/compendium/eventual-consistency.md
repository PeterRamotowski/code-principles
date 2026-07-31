---
id: eventual-consistency
name: Eventual Consistency
classification: system-property
category: state-data-and-distribution
status: candidate
source: principles/entries/eventual-consistency.yaml
generated: true
---

# Eventual Consistency

> Replicated or derived state may be temporarily inconsistent but converges under defined conditions.

## Canonical interpretation

Use eventual consistency only with explicit convergence, conflict, observability, and user-experience semantics.

## Purpose

Replicated or derived state may be temporarily inconsistent but converges under defined conditions.

## Apply when

- State changes, retries, concurrency, or distribution can affect correctness.
- The system needs explicit semantics for commands, queries, and consistency.

## This does not mean

- Do not use the phrase to excuse indefinite or silent divergence.
- Do not choose it when atomic consistency is affordable and required.

## Trade-offs

- Immutability and separation can increase allocation or coordination cost.
- Distributed guarantees usually require operational complexity and failure handling.

## Conflicts with canonical entries

- `principle-of-least-astonishment`
- `single-source-of-truth`

## Broader policy tensions

- `immediate-consistency`

## Reinforces canonical entries

- `idempotency`

## Supports broader concerns

- `distributed-reliability`

## Core Skill ownership

Primary owner: `distributed-reliability`

## Positive example

A search index updates asynchronously with visible freshness expectations and retries.

## Counterexample

Return contradictory balances with no reconciliation or stale-data indication.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/eventual-consistency.yaml` and regenerate the compendium instead of editing this file directly.
