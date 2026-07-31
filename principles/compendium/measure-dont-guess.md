---
id: measure-dont-guess
name: Measure, Don’t Guess
classification: performance-principle
category: performance-and-resources
status: candidate
source: principles/entries/measure-dont-guess.yaml
generated: true
---

# Measure, Don’t Guess

> Base performance decisions on representative measurement and explicit budgets.

## Canonical interpretation

Use profiling, benchmarks, and production telemetry to identify bottlenecks and verify improvement.

## Purpose

Base performance decisions on representative measurement and explicit budgets.

## Apply when

- Measured behavior violates a budget or known scale constraint.
- Memory, latency, throughput, or determinism is a first-class requirement.

## This does not mean

- Do not treat a microbenchmark as production truth.
- Do not delay obvious complexity analysis until after failure.

## Trade-offs

- Optimization usually increases complexity and narrows implementation freedom.
- Benchmarks can mislead when they do not represent production workloads.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `limited-observability`

## Reinforces canonical entries

- `premature-optimization`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `performance-and-resources`

## Positive example

Benchmark streaming and materialized processing with representative files.

## Counterexample

Rewrite code based on intuition without measuring before and after.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/measure-dont-guess.yaml` and regenerate the compendium instead of editing this file directly.
