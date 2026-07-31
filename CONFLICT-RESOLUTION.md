# Conflict Resolution

## 1. Purpose

Software engineering principles frequently protect different quality attributes. A conflict is not evidence that one principle is wrong; it means the project context must determine which concern has priority.

This document defines the central procedure for resolving conflicts without treating principle names as absolute commands.

## 2. Normative rule

When two valid rules point toward different decisions, the model MUST:

1. identify the concrete decision under dispute;
2. identify the quality attribute protected by each rule;
3. apply decision precedence;
4. evaluate evidence and constraints;
5. compare failure consequences;
6. consider scope and reversibility;
7. distinguish public contracts from internal implementation;
8. select the least complex decision that satisfies the higher-priority constraints;
9. record significant trade-offs;
10. avoid claiming that the losing rule is universally invalid.

## 3. Conflict-resolution procedure

### Step 1: State the decision

Bad framing:

> Should we follow DRY or YAGNI?

Better framing:

> Should these two similar validation functions be unified behind a shared abstraction now?

Principle names are too broad to resolve without a concrete decision.

### Step 2: Identify protected qualities

Examples:

- DRY protects consistency of knowledge and reduces divergent updates;
- YAGNI protects simplicity and prevents speculative generalization;
- immutability protects reasoning and concurrency safety;
- controlled mutation may protect performance or framework compatibility;
- backward compatibility protects consumers;
- refactoring freedom protects maintainability.

### Step 3: Apply precedence

Use the precedence defined in `SPECIFICATION.md`.

A verified security requirement outranks a stylistic simplicity preference. An explicit public compatibility promise outranks a default desire to rename an API.

### Step 4: Evaluate evidence

Relevant evidence includes:

- existing consumers;
- documented roadmap;
- repeated change history;
- measured performance;
- repository conventions;
- known data scale;
- production incidents;
- framework lifecycle requirements;
- explicit user constraints.

A hypothetical future possibility is weak evidence.

### Step 5: Evaluate consequences

Consider:

- failure severity;
- blast radius;
- recoverability;
- security impact;
- data loss;
- compatibility breakage;
- operational cost;
- cognitive cost;
- future migration cost.

### Step 6: Evaluate reversibility

Prefer reversible choices when evidence is incomplete.

Examples:

- keep two small functions separate until their shared abstraction is understood;
- introduce an internal adapter before making it public;
- isolate an optimized implementation behind tests;
- avoid a repository-wide migration during a local fix.

### Step 7: Select and record

The resolution SHOULD state:

- selected rule or compromise;
- reason;
- scope;
- trigger for reconsideration.

Example:

> Keep the implementations separate for now because they encode different domain concepts. Reconsider extraction after a third use or when the business rule becomes shared.

## 4. Central conflict matrix

| Principle or policy A | Principle or policy B | Default resolution |
|---|---|---|
| DRY | YAGNI | Remove duplicated knowledge, not every textual similarity. Delay abstraction until the shared concept and variation axis are understood. |
| Open/Closed Principle | KISS | Add extension points for known or strongly evidenced variation. Do not create plugin systems for hypothetical futures. |
| Single Responsibility | Locality of behavior | Keep behavior and data together when they change for the same reason. Split only when responsibilities have distinct change drivers. |
| Small functions | Local readability | Extract coherent operations or abstraction levels, not arbitrary line ranges. A longer linear function may be clearer than fragmented indirection. |
| Composition over inheritance | Framework or language contract | Prefer composition by default. Use inheritance for true substitutability, mandatory framework extension, or carefully controlled polymorphism. |
| Interface Segregation | Simplicity | Introduce an interface only when there is a real consumer contract, variation, test boundary, or architecture boundary. Do not mirror every class with an interface. |
| Dependency Inversion | Framework-native design | Isolate unstable or independently evolving boundaries. Do not wrap every framework service merely to claim framework independence. |
| Hexagonal architecture | CRUD simplicity | Use domain isolation when business rules or infrastructure independence justify it. Prefer framework-native modules for simple data-driven features. |
| Tell, Don’t Ask | DTO and pipeline transparency | Apply behavior-oriented encapsulation to domain models. Permit transparent data structures for transfer, configuration, and transformation pipelines. |
| Encapsulation | Serialization and interoperability | Protect invariants internally, but provide explicit serialization boundaries rather than exposing unrestricted mutation. |
| Immutability | ORM or UI state conventions | Prefer immutable values; permit controlled mutation for lifecycle-managed entities and state where it improves clarity or compatibility. |
| Immutability | Performance | Require evidence before replacing immutable design. Isolate mutable hot paths and protect them with tests and ownership rules. |
| Fail Fast | Tolerant external input | Normalize harmless syntactic variation at the boundary, but reject ambiguous, unsafe, or semantically invalid data. Keep internal contracts strict. |
| Postel’s Law | Parse, Don’t Validate | Be tolerant only where meaning remains unambiguous. Parse accepted forms into a strict internal representation. |
| Defensive programming | Error visibility | Defend at trust boundaries and resource boundaries. Do not swallow errors or silently substitute values that hide broken invariants. |
| Command–Query Separation | Performance or convenience | Keep conceptual commands and queries distinct. A command may return identifiers, status, or resulting metadata when this improves safe use without hiding side effects. |
| CQRS | Simplicity | Use separate read and write models only when scale, domain, authorization, or workflow complexity justifies the operational cost. |
| Single Source of Truth | Local caching | Maintain one authoritative source and make derived caches explicit, disposable, and governed by invalidation rules. |
| Idempotency | Throughput and storage cost | Require idempotency where retries or duplicate delivery are realistic. Scope deduplication windows and storage to actual risk. |
| Backward compatibility | API cleanup | Preserve declared public contracts. Use deprecation and migration paths; change internal contracts atomically. |
| Semantic versioning | Hyrum’s Law | SemVer governs intentional API promises, but maintainers should also inspect observable behavior that consumers may rely on. |
| Boy Scout Rule | Minimal task scope | Permit small local improvements that reduce risk or improve clarity. Move unrelated or broad refactoring into separate work. |
| Chesterton’s Fence | Simplification | Understand the reason and consumers of an existing mechanism before removal. If the reason no longer applies, remove it with evidence and tests. |
| Test pyramid | Risk-based testing | Treat the pyramid as a cost heuristic, not a required shape. Use the cheapest test level that provides adequate confidence. |
| Unit isolation | Framework integration confidence | Unit-test pure logic and use real framework integration where mocks would reproduce implementation details. |
| One assertion per test | Complete behavior verification | Test one coherent behavior; allow multiple related assertions that describe the same result. |
| TDD | Exploratory design | TDD is optional. Use it where behavior can be expressed incrementally; allow spikes, then convert learning into tests and maintainable implementation. |
| Premature optimization warning | Known hard constraints | Measurement is preferred, but explicit latency, memory, throughput, or real-time budgets are sufficient evidence to design accordingly. |
| Clarity | Hot-path optimization | Optimize only the constrained path. Isolate complexity, document the budget, and maintain correctness tests or a reference implementation. |
| Framework conventions | Portability | Follow framework conventions for application code. Isolate framework dependence when the component has a real portability or independent-lifecycle requirement. |
| Package by feature | Layered architecture | Organize top-level application code by capability where useful; use technical layers inside features when they improve clarity. Libraries may organize by public concept instead. |
| Rich domain model | Data-oriented pipeline | Use behavior-rich models for complex invariants. Use transparent records and staged transformations for high-volume data processing. |
| Strict typing | Readability | Prefer types that expose meaningful states and contracts. Avoid type-level complexity that is harder to understand than the runtime behavior it protects. |
| Static typing | Runtime validation | Static types protect trusted code paths; external data still requires runtime parsing and validation. |
| General reusable component | Accessibility and semantics | Prefer explicit semantic components over excessively generic abstractions that make correct accessible behavior difficult. |
| Global state reuse | Local state ownership | Keep state as close as possible to its consumers. Promote it only when sharing, persistence, coordination, or synchronization requires it. |
| Eventual consistency | Immediate user expectations | Explicitly communicate pending state, define reconciliation behavior, and use synchronous consistency where the user action requires immediate guarantees. |
| Retry | Duplicate side effects | Retry only idempotent operations or operations protected by deduplication, transactional outbox, or equivalent safeguards. |
| Logging detail | Privacy and security | Log enough for diagnosis without exposing secrets, credentials, personal data, or sensitive payloads. |
| Generalization | Existing code consistency | Prefer the existing stable convention for local changes unless the user authorizes redesign or the convention causes a material defect. |

## 5. Profile-specific tie breakers

When the matrix does not fully resolve a conflict, use the base profile's priority order.

### Prototype

Typical order:

```text
learning and correctness
> speed of iteration
> simplicity
> local readability
> extensibility
> strict compatibility
```

### Reusable library

Typical order:

```text
correctness
> public contract stability
> predictable behavior
> usability
> maintainability
> extensibility
> implementation convenience
```

### Full-stack web application

Typical order:

```text
correctness and security
> user-visible behavior
> maintainability
> operational reliability
> performance within budgets
> architectural purity
```

### Legacy modernization

Typical order:

```text
behavior preservation
> correctness and risk reduction
> reversibility
> test coverage of changed behavior
> local maintainability
> broad architectural cleanup
```

### Real-time or embedded system

Typical order:

```text
correctness and safety
> determinism
> resource bounds
> reliability
> measurable performance
> readability
> flexibility
```

## 6. Escalation conditions

The model SHOULD ask for a decision or explicitly surface alternatives when:

- two options have materially different public compatibility consequences;
- architecture authority is unknown and a redesign would be difficult to reverse;
- a security or data-integrity trade-off cannot be safely inferred;
- the user’s stated requirements are internally contradictory;
- choosing a runtime, framework, persistence model, or protocol would commit substantial project cost;
- repository evidence strongly conflicts with the user's assumption.

For ordinary local work, the model SHOULD make the safest conservative choice instead of blocking progress.

## 7. Required conflict record

A resolved policy may record a conflict as:

```yaml
conflicts:
  - id: dry-vs-yagni-validator-abstraction
    decision: keep-separate
    protected_attributes:
      selected: simplicity
      deferred: consistency
    rationale: >-
      The functions are textually similar but represent different domain rules.
      No stable shared abstraction has been identified.
    reconsider_when:
      - a third consumer appears
      - the rules become governed by one authoritative specification
```

## 8. Anti-patterns

The following conflict-resolution behaviors are prohibited:

- selecting a principle because it is more famous;
- counting principles on each side;
- treating all `SHOULD` rules as `MUST` rules;
- using “clean code” as an unexplained verdict;
- introducing architecture solely to satisfy a diagram;
- hiding compatibility breakage inside a refactor;
- claiming performance benefits without evidence or constraints;
- using YAGNI to ignore explicit near-term requirements;
- using DRY to combine unrelated domain concepts;
- using framework convention to justify insecure behavior;
- using existing convention to preserve a correctness defect.


## Canonical relationship integration

The conflict matrix is operational guidance. Canonical entry-level relationships are also recorded in `principles/relationships.yaml` for navigation and tooling.

When a conflict involves a catalogue entry, the resolver MUST use that entry’s canonical interpretation and rejected meanings. It MUST NOT resolve a conflict by importing a third-party Skill’s interpretation.
