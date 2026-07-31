---
id: command-query-separation
name: Command–Query Separation
classification: principle
category: state-data-and-distribution
status: candidate
source: principles/entries/command-query-separation.yaml
generated: true
---

# Command–Query Separation

> An operation should either change state or return information, with exceptions made explicit.

## Canonical interpretation

Separate observation from mutation so callers can reason about effects.

## Purpose

An operation should either change state or return information, with exceptions made explicit.

## Apply when

- State changes, retries, concurrency, or distribution can affect correctness.
- The system needs explicit semantics for commands, queries, and consistency.

## This does not mean

- Do not prohibit useful atomic operations that must return a result.
- Do not confuse CQS with CQRS.

## Trade-offs

- Immutability and separation can increase allocation or coordination cost.
- Distributed guarantees usually require operational complexity and failure handling.

## Conflicts with canonical entries

- `tell-dont-ask`

## Broader policy tensions

- `atomic-update-result`

## Reinforces canonical entries

- `explicit-over-implicit`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `state-and-side-effects`

## Positive example

A query retrieves account status; a command changes it.

## Counterexample

A method named `getStatus` mutates persistence and sends notifications.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/command-query-separation.yaml` and regenerate the compendium instead of editing this file directly.
