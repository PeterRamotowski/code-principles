---
id: tell-dont-ask
name: Tell, Don’t Ask
classification: heuristic
category: modularity-and-object-design
status: candidate
source: principles/entries/tell-dont-ask.yaml
generated: true
---

# Tell, Don’t Ask

> Ask behavior-owning objects to perform operations instead of extracting state and deciding externally.

## Canonical interpretation

Use this heuristic for objects that protect behavior and invariants, not automatically for DTOs or query results.

## Purpose

Ask behavior-owning objects to perform operations instead of extracting state and deciding externally.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not hide orchestration inside entities.
- Do not force behavior into passive data structures used by multiple independent operations.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `command-query-separation`

## Broader policy tensions

- `data-oriented-design`

## Reinforces canonical entries

- `encapsulation`
- `locality-of-behaviour`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Tell an account to withdraw so it can enforce its invariant.

## Counterexample

Read private balance fields, calculate externally, then set the balance.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/tell-dont-ask.yaml` and regenerate the compendium instead of editing this file directly.
