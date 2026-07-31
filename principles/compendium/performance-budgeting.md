---
id: performance-budgeting
name: Performance Budgets
classification: engineering-practice
category: performance-and-resources
status: candidate
source: principles/entries/performance-budgeting.yaml
generated: true
---

# Performance Budgets

> Define acceptable latency, throughput, memory, and determinism limits.

## Canonical interpretation

A budget turns performance from vague preference into a verifiable requirement.

## Purpose

Define acceptable latency, throughput, memory, and determinism limits.

## Apply when

- Measured behavior violates a budget or known scale constraint.
- Memory, latency, throughput, or determinism is a first-class requirement.

## This does not mean

- Do not choose arbitrary numbers without user or operational relevance.
- Do not optimize every component equally when only end-to-end budgets matter.

## Trade-offs

- Optimization usually increases complexity and narrows implementation freedom.
- Benchmarks can mislead when they do not represent production workloads.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `clarity`
- `portability`

## Reinforces canonical entries

- `measure-dont-guess`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `performance-and-resources`

## Positive example

Set a p95 response and memory ceiling for a worker and test against it.

## Counterexample

Call a system “fast” without a workload or target.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/performance-budgeting.yaml` and regenerate the compendium instead of editing this file directly.
