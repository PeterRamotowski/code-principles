---
id: premature-optimization
name: Avoid Premature Optimization
classification: heuristic
category: performance-and-resources
status: candidate
source: principles/entries/premature-optimization.yaml
generated: true
---

# Avoid Premature Optimization

> Do not add complexity for unmeasured or irrelevant performance gains.

## Canonical interpretation

Optimize when evidence, scale analysis, or explicit budgets identify a real constraint.

## Purpose

Do not add complexity for unmeasured or irrelevant performance gains.

## Apply when

- Measured behavior violates a budget or known scale constraint.
- Memory, latency, throughput, or determinism is a first-class requirement.

## This does not mean

- Do not ignore known algorithmic explosions or hard real-time requirements.
- Do not use the maxim to dismiss inexpensive efficient choices.

## Trade-offs

- Optimization usually increases complexity and narrows implementation freedom.
- Benchmarks can mislead when they do not represent production workloads.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `hard-real-time-constraints`
- `memory-limits`

## Reinforces canonical entries

- `make-it-work-right-fast`
- `measure-dont-guess`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `performance-and-resources`

## Positive example

Profile a request path before introducing cache invalidation complexity.

## Counterexample

Add caching layers everywhere because they might be faster.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/premature-optimization.yaml` and regenerate the compendium instead of editing this file directly.
