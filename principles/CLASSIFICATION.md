# Principle Classification Model

The catalogue uses explicit classifications because lists of “best practices” often mix unlike concepts.

| Classification | Meaning | Normative role |
|---|---|---|
| `principle` | General design rule expressing a desired relationship or property. | Usually context-sensitive and interpreted by a Core Skill. |
| `heuristic` | Useful default that may be overridden by evidence. | SHOULD-level guidance, rarely MUST. |
| `technique` | A concrete implementation mechanism. | Selected only when it realizes an active policy. |
| `method` | A structured way of working or specifying behavior. | Optional unless a profile or user requires it. |
| `development-method` | A development workflow such as TDD. | Never universal by default. |
| `development-cycle` | A repeated sequence inside a method. | Active only with its parent method or explicit selection. |
| `architecture-pattern` | A recurring structural arrangement. | Requires architectural justification. |
| `architecture-style` | A broader system organization. | Must not be imposed on small tasks without authority. |
| `architecture-rule` | A directional or boundary rule from an architecture family. | May be used without adopting the entire family. |
| `system-property` | A property such as idempotency or eventual consistency. | Required when the system’s semantics demand it. |
| `design-property` | A local or systemic quality such as immutability. | Applied selectively according to costs. |
| `security-principle` | A rule governing authority or trust. | May become mandatory under a security modifier. |
| `testing-principle` | A rule about what tests protect. | Interpreted through testing strategy. |
| `testing-pattern` | A test-structure convention. | Optional structure, not a correctness guarantee. |
| `testing-heuristic` | A default for test scope or organization. | Must not be reduced to a numeric rule. |
| `testing-strategy` | A distribution or portfolio of test types. | Chosen according to architecture and risk. |
| `versioning-method` | A convention for communicating evolution. | Requires a defined public API. |
| `evolution-principle` | Guidance for changing public or shared systems. | Stronger when consumers cannot update atomically. |
| `organizational-principle` | Guidance for code organization and ownership. | Applied at module or repository scale. |
| `change-principle` | Guidance for safe incremental modification. | Bounded by task scope and architecture authority. |
| `law` | An empirical or rhetorical observation about engineering systems. | Used as a review lens, never as a direct command. |
| `design-philosophy` | A broad stance on trade-offs and adoption. | Requires translation into specific decisions. |
| `process-model` | A sequence for implementation and improvement. | Adapted to known constraints. |
| `umbrella-concept` | A label that groups multiple practices. | Cannot be used as standalone justification. |

A Core Skill MUST preserve the classification of its entries. It MUST NOT turn every heuristic into a mandatory rule or every law into an implementation instruction.
