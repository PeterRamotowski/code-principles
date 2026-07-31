# Context Detection

## 1. Purpose

This document defines how the orchestrator extracts project context from user instructions and repository evidence.

Context detection is a normalization task, not an architecture-design task. Its purpose is to identify what is known, how strongly it is known, and which unknowns matter.

## 2. Evidence sources

Use evidence in this order of trust, subject to current-task relevance:

1. explicit current user statements;
2. explicit repository configuration;
3. source code and manifests;
4. tests and public documentation;
5. deployment and runtime configuration;
6. directory and naming conventions;
7. weak ecosystem conventions.

A convention such as `cmd/`, `internal/`, or `src/app/` is useful evidence but MUST NOT override explicit project information.

## 3. Confidence model

Every material detected value uses one confidence level.

### `explicit`

Directly stated or configured.

Examples:

- “This is a public library.”
- `artifact_type: reusable-library` in `engineering-context.yaml`.

### `observed`

Directly supported by project artifacts.

Examples:

- package publishing configuration;
- exported package entry points;
- a Next.js configuration file;
- a CMake project producing a shared library;
- a Drupal module descriptor.

### `inferred-high`

Strongly implied by several independent signals.

Example:

- `package.json`, `next.config.*`, `app/`, and server routes strongly imply a full-stack Next.js application.

### `inferred-low`

Plausible but uncertain.

Example:

- a folder named `domain/` weakly suggests domain modeling but does not prove high domain complexity.

### `unknown`

No reliable evidence.

Unknown MUST remain unknown.

## 4. Detection sequence

### 4.1 Determine task boundary

Identify which files, package, service, or subsystem the task affects.

Repository-wide context should not be applied indiscriminately to a narrow independent package.

### 4.2 Detect artifact type

Use the deliverable's purpose, not merely its runtime.

Signals:

| Artifact type | Typical signals |
|---|---|
| `frontend-application` | browser UI, client routing, component tree, no material server responsibility |
| `fullstack-application` | browser and server code in one product, SSR/server routes/server actions |
| `backend-service` | long-running network service, HTTP/RPC handlers, service deployment |
| `reusable-library` | package exports, publishing metadata, consumer-facing API, no primary executable |
| `plugin-or-extension` | host lifecycle, manifest for an extension, hooks, plugin APIs |
| `data-pipeline` | staged ingestion/transformation/output, batch or streaming records |
| `background-worker` | queue consumer, scheduler, daemonized job execution |
| `embedded-system` | hardware interfaces, firmware build, constrained runtime |
| `cli-application` | command definitions, executable entry point, terminal interface |
| `infrastructure-tool` | deployment, build, environment, provisioning, repository automation |

A library may also contain CLI tooling. Select the primary artifact for the current task and record secondary types when useful.

### 4.3 Detect project stage

Signals:

- `prototype`: disposable or exploratory intent, unstable requirements;
- `greenfield`: new production-intended project without established architecture;
- `active-product`: maintained product receiving features;
- `mature-system`: established consumers, stable behavior, operational history;
- `legacy-modernization`: explicit modernization of difficult or outdated code;
- `maintenance-only`: fixes with minimal feature development.

Age alone does not make a project legacy.

### 4.4 Detect exposure

Look for intentional consumers and compatibility promises.

Evidence:

- published package metadata;
- documented API;
- exported modules;
- SDK generation;
- external webhook or protocol consumers;
- extension points;
- versioning and deprecation policy;
- separate teams or repositories consuming the interface.

Do not treat every `public` class or exported symbol as a stable API without evidence of consumer intent.

### 4.5 Detect domain complexity

Use:

- number and interaction of business invariants;
- terminology and workflows;
- authorization rules;
- state transitions;
- regulatory or financial constraints;
- change history;
- consequences of invalid states.

Do not infer high complexity from:

- many files;
- a large database;
- a framework convention;
- the presence of entities or models alone.

### 4.6 Detect architecture authority

Use the task wording first.

| User intent | Default authority |
|---|---|
| fix a bug | `preserve-existing` |
| add a small feature | `incremental-improvement` |
| refactor this module | `incremental-improvement` |
| redesign the architecture | `redesign-allowed` |
| design a new project | `greenfield` |

If the user explicitly forbids broad refactoring, use `preserve-existing`.

### 4.7 Detect operational constraints

Only elevate a constraint when supported by evidence.

Examples:

- memory limit or huge data files → memory sensitivity;
- response-time SLO → latency sensitivity;
- messages per second or batch deadline → throughput sensitivity;
- hard deadline per control cycle → determinism or real-time;
- payment, credentials, personal data, authorization → elevated security;
- package used by third parties → elevated compatibility;
- safety-related hardware control → critical reliability or safety.

### 4.8 Detect state model

Inspect state ownership and consistency requirements.

Examples:

- request handlers without durable coordination → request-scoped;
- database transactions → transactional;
- queues and event handlers → event-driven;
- replicated read models → eventually-consistent;
- browser offline cache and later synchronization → offline-synchronized;
- shared UI store or multi-threaded mutable object → shared-mutable.

### 4.9 Detect language and framework

Use:

- file extensions;
- manifest files;
- lock files;
- imports;
- framework configuration;
- build scripts;
- generated code markers.

A framework adapter should be activated only when the task touches framework behavior.

## 5. Representative repository signals

### TypeScript and JavaScript

Potential signals:

- `package.json`;
- `tsconfig.json`;
- `.ts`, `.tsx`, `.js`, `.jsx`;
- package exports;
- Vite, Webpack, or other build configuration.

### React

Potential signals:

- `react` dependency;
- JSX/TSX components;
- hooks;
- React test utilities.

### Next.js

Potential signals:

- `next` dependency;
- `next.config.*`;
- `app/` or `pages/`;
- server components, route handlers, server actions.

### Vue and Nuxt

Potential signals:

- `.vue` files;
- `vue` or `nuxt` dependency;
- `nuxt.config.*`;
- composables, plugins, server routes.

### Angular

Potential signals:

- `angular.json`;
- `@angular/*` dependencies;
- components, services, signals, RxJS.

### Python

Potential signals:

- `pyproject.toml`;
- `requirements*.txt`;
- `.py` files;
- package exports;
- console scripts;
- type-checker configuration;
- data or web framework dependencies.

### PHP

Potential signals:

- `composer.json`;
- `.php` files;
- PSR-4 autoloading;
- package type and framework dependencies.

### Symfony

Potential signals:

- Symfony packages;
- `config/services.*`;
- bundles;
- console, Messenger, Doctrine, or HTTP kernel usage.

### Drupal

Potential signals:

- `*.info.yml`;
- `*.module`;
- `*.services.yml`;
- plugin annotations or attributes;
- Drupal core dependencies;
- entity, hook, cache metadata, or configuration APIs.

### Go

Potential signals:

- `go.mod`;
- `.go` files;
- `cmd/`, `internal/`, `pkg/`;
- HTTP, gRPC, worker, or CLI packages.

Directory names are conventions, not proof of architecture.

### C++

Potential signals:

- `CMakeLists.txt`;
- `.cpp`, `.cc`, `.cxx`, `.h`, `.hpp`;
- shared/static library targets;
- embedded toolchains;
- real-time or hardware-specific build flags.

## 6. Mixed repositories

A monorepo or multi-package repository may contain several artifact types and languages.

The orchestrator SHOULD:

1. identify the affected package or subsystem;
2. select a primary profile for that scope;
3. select adapters only for relevant languages and frameworks;
4. record cross-boundary contracts when the task spans packages;
5. avoid applying frontend rules to backend-only code or vice versa.

## 7. Contradictory evidence

When evidence conflicts:

1. prefer explicit current user instructions;
2. prefer explicit repository configuration over conventions;
3. prefer direct manifests and source evidence over directory names;
4. retain the contradiction if it affects the decision;
5. choose a conservative action when safe;
6. surface the conflict if it changes compatibility, security, or architecture.

Example:

- User says “internal package,” but package publishing configuration exists.
- Record both facts.
- Avoid breaking exported contracts until intent is clarified if the change is difficult to reverse.

## 8. Detection output example

```yaml
project:
  artifact_type:
    value: fullstack-application
    confidence: inferred-high
    evidence:
      - next dependency
      - app directory with server and client components
      - route handlers
  project_stage:
    value: active-product
    confidence: inferred-high
    evidence:
      - production deployment configuration
      - migration history
  architecture_authority:
    value: preserve-existing
    confidence: explicit
    evidence:
      - user requested a local bug fix

languages:
  - value: typescript
    confidence: observed
    evidence:
      - tsconfig.json
      - ts and tsx source files

frameworks:
  - value: nextjs
    confidence: observed
    evidence:
      - next.config.ts
      - next dependency
```

## 9. Detection anti-patterns

Do not:

- infer microservices from multiple directories;
- infer DDD from a `domain` folder;
- infer public API from visibility keywords;
- infer strict runtime validation from TypeScript or Python annotations;
- infer a real-time system because users expect the UI to feel fast;
- infer a prototype because test coverage is low;
- infer legacy solely from project age;
- infer high domain complexity from code volume;
- infer redesign authority from a refactoring request limited to one module.
