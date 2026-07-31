# Architecture and Dependency Direction

This category groups related concepts for navigation. Category membership does not make every item equally normative.

| Entry | Classification | Summary |
|---|---|---|
| [Acyclic Dependencies Principle](../compendium/acyclic-dependencies-principle.md) | `principle` | Keep component dependency graphs free of cycles at meaningful architectural boundaries. |
| [Clean Architecture Dependency Rule](../compendium/clean-architecture-dependency-rule.md) | `architecture-rule` | Source-code dependencies should point toward higher-level policy. |
| [Dependency Injection](../compendium/dependency-injection.md) | `technique` | Supply collaborators from outside a component instead of constructing hidden dependencies internally. |
| [Dependency Inversion Principle](../compendium/dependency-inversion-principle.md) | `principle` | High-level policy should not depend directly on volatile low-level details. |
| [Inversion of Control](../compendium/inversion-of-control.md) | `architecture-pattern` | Delegate control of lifecycle or flow to a framework, runtime, or coordinating component. |
| [Ports and Adapters](../compendium/ports-and-adapters.md) | `architecture-style` | Place application policy behind explicit ports and implement external interactions through adapters. |
| [Stable Dependencies Principle](../compendium/stable-dependencies-principle.md) | `principle` | Dependencies should generally point toward components that change less often. |
