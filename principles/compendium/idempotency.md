---
id: idempotency
name: Idempotency
classification: system-property
category: state-data-and-distribution
status: candidate
source: principles/entries/idempotency.yaml
generated: true
---

# Idempotency

> Repeated execution of the same operation has the same intended effect as one execution.

## Canonical interpretation

Design retried commands and integrations so duplicate delivery does not duplicate business effects.

## Purpose

Repeated execution of the same operation has the same intended effect as one execution.

## Apply when

- State changes, retries, concurrency, or distribution can affect correctness.
- The system needs explicit semantics for commands, queries, and consistency.

## This does not mean

- Do not assume HTTP method names guarantee application idempotency.
- Do not ignore the storage and retention policy for idempotency keys.

## Trade-offs

- Immutability and separation can increase allocation or coordination cost.
- Distributed guarantees usually require operational complexity and failure handling.

## Conflicts with canonical entries

- `performance-budgeting`

## Broader policy tensions

- `at-least-once-delivery`

## Reinforces canonical entries

- `defensive-programming`
- `eventual-consistency`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `distributed-reliability`

## Positive example

Store a provider event identifier and process each payment event once.

## Counterexample

Send duplicate invoices whenever a queue retries a message.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/idempotency.yaml` and regenerate the compendium instead of editing this file directly.
