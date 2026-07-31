---
id: yagni
name: YAGNI
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/yagni.yaml
generated: true
---

# YAGNI

> Avoid implementing capabilities that are not required by current evidence.

## Canonical interpretation

Do not pay present complexity for speculative future needs.

## Purpose

Avoid implementing capabilities that are not required by current evidence.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not ignore known near-term requirements.
- Do not use YAGNI to avoid inexpensive compatibility seams at public boundaries.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- `dry`
- `open-closed-principle`

## Broader policy tensions

- `public-api-extensibility`

## Reinforces canonical entries

- `kiss`
- `premature-optimization`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `abstraction-and-reuse`

## Positive example

Keep one concrete storage implementation until a second implementation or boundary is real.

## Counterexample

Design a generic distributed storage abstraction for a local prototype.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/yagni.yaml` and regenerate the compendium instead of editing this file directly.
