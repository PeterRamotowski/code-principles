---
id: single-level-of-abstraction
name: Single Level of Abstraction
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/single-level-of-abstraction.yaml
generated: true
---

# Single Level of Abstraction

> Keep a function or section focused on one primary conceptual level.

## Canonical interpretation

Do not mix orchestration with low-level parsing, transport, or storage details unless that combination is locally clearer.

## Purpose

Keep a function or section focused on one primary conceptual level.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not extract every statement into another function.
- Do not use abstraction level as an arbitrary line-count rule.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- `locality-of-behaviour`
- `small-functions`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `separation-of-concerns`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

A use-case function coordinates named validation, persistence, and notification operations.

## Counterexample

A use-case function contains SQL formatting, HTTP retry loops, and business decisions inline.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/single-level-of-abstraction.yaml` and regenerate the compendium instead of editing this file directly.
