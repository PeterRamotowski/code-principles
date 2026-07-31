# Profile Selection

## 1. Purpose

This document defines how the orchestrator selects a language-independent base profile and composes it with modifiers.

## 2. Selection principle

The base profile represents the dominant engineering priorities of the affected software artifact.

Selection MUST be based primarily on what is being built and how it is consumed, not on the programming language.

## 3. Selection order

Evaluate in this order:

1. current task scope;
2. primary artifact type;
3. exposure and compatibility;
4. project stage;
5. domain complexity;
6. state and consistency model;
7. runtime and operational constraints;
8. existing architecture;
9. technology ecosystem.

## 4. Primary profile rule

Select one primary base profile for the current task.

Use modifiers for independent cross-cutting concerns.

Do not select multiple overlapping base profiles merely because a project has several characteristics.

Example:

```text
fullstack-web-application
+ public-api
+ security-sensitive
+ multi-tenant
```

is preferred over treating `backend-service`, `browser-web-application`, and `distributed-system` as three equal base profiles for an ordinary SaaS product.

## 5. Planned profile selection guide

### `browser-web-application`

Select when the primary deliverable is browser-executed user interface software without substantial server responsibility in the same artifact.

Typical priorities:

- user behavior;
- accessibility;
- state ownership;
- rendering correctness;
- browser security boundaries;
- component cohesion;
- interaction testing.

Do not select merely because a repository contains a small administrative UI inside another primary artifact.

### `fullstack-web-application`

Select when one product includes meaningful browser and server execution, such as Next.js, Nuxt, Remix, or an integrated frontend/backend application.

Typical priorities:

- client/server boundaries;
- authoritative server validation;
- secret protection;
- rendering and caching behavior;
- API contracts;
- authentication and authorization;
- operational reliability.

### `backend-service`

Select for a server process whose primary role is serving network requests or application operations.

Typical priorities:

- contracts;
- error handling;
- transactions;
- observability;
- dependency boundaries;
- reliability;
- controlled concurrency.

Do not automatically infer microservices.

### `reusable-library`

Select when the primary artifact is intended for reuse by independent consumers.

Typical priorities:

- small intentional public API;
- predictable behavior;
- compatibility;
- documentation;
- dependency discipline;
- portability appropriate to scope;
- strong edge-case testing.

This profile applies across TypeScript, Python, PHP, Go, C++, and other languages.

### `plugin-or-extension`

Select when the artifact runs inside and extends a host platform.

Typical priorities:

- host lifecycle compliance;
- version compatibility;
- extension-point stability;
- safe activation and deactivation;
- limited control over the host;
- integration testing.

Examples include Drupal modules, WordPress plugins, VS Code extensions, Vite plugins, and Nuxt modules.

### `data-pipeline`

Select for staged ingestion, parsing, transformation, enrichment, aggregation, or export of data.

Typical priorities:

- explicit stages;
- data contracts;
- streaming and memory behavior;
- restartability;
- observability;
- partial failure policy;
- reproducibility.

Do not force rich object models when transparent records and transformations are clearer.

### `background-worker`

Select for queue consumers, scheduled jobs, and daemonized processing.

Typical priorities:

- idempotency;
- retry policy;
- cancellation;
- lifecycle management;
- resource cleanup;
- poison-message handling;
- observability.

### `distributed-system`

Select only when distribution is fundamental to the task rather than incidental infrastructure.

Typical priorities:

- partial failure;
- consistency model;
- ordering;
- idempotency;
- retries;
- timeouts;
- observability;
- operational complexity.

Do not select solely because an application calls a database or third-party API.

### `real-time-system`

Select when correctness depends on explicit timing or determinism guarantees.

Typical priorities:

- safety and correctness;
- determinism;
- bounded resource use;
- latency budgets;
- predictable concurrency;
- failure containment.

A responsive web UI is not a real-time system in this sense.

### `prototype`

Select when learning and rapid iteration are the primary objective and compatibility is intentionally weak.

Typical priorities:

- correctness sufficient for learning;
- delivery speed;
- simplicity;
- observability of assumptions;
- easy replacement.

A prototype modifier or project stage may sometimes be more appropriate than a full profile. The final design should decide whether `prototype` remains a base profile or becomes a stage-driven overlay.

### `legacy-modernization`

Select when the central task is safely evolving an existing difficult system.

Typical priorities:

- behavior preservation;
- characterization tests;
- reversibility;
- bounded changes;
- compatibility;
- gradual simplification;
- understanding before removal.

## 6. Profile selection examples

### Example A: Next.js SaaS

Evidence:

- browser and server components;
- public API;
- payment webhooks;
- existing product.

Resolution:

```yaml
base_profile: fullstack-web-application
modifiers:
  - public-api
  - security-sensitive
```

Do not select `distributed-system` unless the task concerns distributed consistency or messaging.

### Example B: Python package for parsing logs

Evidence:

- published package;
- no primary executable;
- streaming API;
- third-party consumers.

Resolution:

```yaml
base_profile: reusable-library
modifiers:
  - public-api
  - memory-sensitive
```

### Example C: Python batch import

Evidence:

- scheduled process;
- reads large CSV files;
- writes normalized database records;
- internal tool.

Resolution:

```yaml
base_profile: data-pipeline
modifiers:
  - memory-sensitive
```

A `background-worker` profile may become primary if queue lifecycle and retries dominate the task.

### Example D: Go HTTP service

Resolution:

```yaml
base_profile: backend-service
language_adapters:
  - go
```

Do not add `public-api` if all callers are updated atomically and no compatibility promise exists.

### Example E: Drupal module

Resolution:

```yaml
base_profile: plugin-or-extension
language_adapters:
  - php
framework_adapters:
  - symfony
  - drupal
```

Add `public-api` only if the module intentionally exposes supported extension contracts.

### Example F: C++ embedded communication component

Evidence:

- hard deadline;
- constrained memory;
- hardware interface;
- safety implications.

Resolution:

```yaml
base_profile: real-time-system
modifiers:
  - memory-sensitive
  - real-time
language_adapters:
  - cpp
```

## 7. Modifiers versus profiles

Use a modifier when the concern:

- applies across several artifact types;
- changes policy intensity;
- does not define the primary lifecycle of the software.

Examples:

- public API;
- security sensitivity;
- memory sensitivity;
- accessibility;
- multi-tenancy.

Use a profile when the concern defines the dominant artifact lifecycle and failure model.

## 8. Ambiguous cases

### Library with a CLI

Use `reusable-library` when the library API is primary and the CLI is a convenience. Use `cli-application` when the executable is the supported product and internal packages are implementation details.

### Web application with workers

Use the profile relevant to the task. A UI change may use `fullstack-web-application`; queue-processing work may use `background-worker` within the same repository.

### Framework plugin that exposes a library

Use `plugin-or-extension` for host integration tasks. Use `reusable-library` for a separately consumable framework-independent package.

### Server-rendered frontend

Use `fullstack-web-application` when server execution affects data access, secrets, rendering, caching, or routing.

## 9. Prohibited selection shortcuts

Do not select:

- `backend-service` merely because code runs on a server;
- `reusable-library` merely because code has modules;
- `distributed-system` merely because a database or API exists;
- `real-time-system` merely because low latency is desirable;
- `legacy-modernization` merely because code is old;
- `prototype` merely because tests are absent;
- `fullstack-web-application` merely because a frontend build tool exists;
- a framework-named base profile.
