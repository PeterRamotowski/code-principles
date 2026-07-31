---
id: make-it-work-right-fast
name: Make It Work, Make It Right, Make It Fast
classification: process-model
category: simplicity-and-clarity
status: candidate
source: principles/entries/make-it-work-right-fast.yaml
generated: true
---

# Make It Work, Make It Right, Make It Fast

> Sequence development through correctness, design quality, and measured optimization.

## Canonical interpretation

Establish correct behavior, improve structure, then optimize verified bottlenecks.

## Purpose

Sequence development through correctness, design quality, and measured optimization.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not ship unsafe or unmaintainable code as merely “working.”
- Do not postpone known performance constraints that shape the architecture.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `hard-real-time-constraints`

## Reinforces canonical entries

- `measure-dont-guess`
- `premature-optimization`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `performance-and-resources`

## Positive example

Implement a correct parser, add tests, then profile large files.

## Counterexample

Micro-optimize an unverified algorithm before its behavior is defined.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/make-it-work-right-fast.yaml` and regenerate the compendium instead of editing this file directly.
