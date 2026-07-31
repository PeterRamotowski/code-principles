---
id: worse-is-better
name: Worse Is Better
classification: design-philosophy
category: simplicity-and-clarity
status: candidate
source: principles/entries/worse-is-better.yaml
generated: true
---

# Worse Is Better

> A simpler, sufficiently correct design can achieve wider adoption and evolve more effectively than a theoretically perfect one.

## Canonical interpretation

Prefer a smaller coherent solution when completeness would impose disproportionate implementation and adoption cost.

## Purpose

A simpler, sufficiently correct design can achieve wider adoption and evolve more effectively than a theoretically perfect one.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not use the phrase to justify known correctness or security defects.
- Do not treat popularity as proof of technical quality.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- `clean-architecture-dependency-rule`

## Broader policy tensions

- `completeness`

## Reinforces canonical entries

- `galls-law`
- `kiss`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Ship a narrow interoperable format that can evolve through versions.

## Counterexample

Ignore data-loss cases because the simpler implementation is easier to release.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/worse-is-better.yaml` and regenerate the compendium instead of editing this file directly.
