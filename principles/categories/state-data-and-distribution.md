# State, Side Effects, Data, and Distribution

This category groups related concepts for navigation. Category membership does not make every item equally normative.

| Entry | Classification | Summary |
|---|---|---|
| [Command Query Responsibility Segregation](../compendium/cqrs.md) | `architecture-pattern` | Use different models or paths for reads and writes when their requirements materially diverge. |
| [Command–Query Separation](../compendium/command-query-separation.md) | `principle` | An operation should either change state or return information, with exceptions made explicit. |
| [Eventual Consistency](../compendium/eventual-consistency.md) | `system-property` | Replicated or derived state may be temporarily inconsistent but converges under defined conditions. |
| [Idempotency](../compendium/idempotency.md) | `system-property` | Repeated execution of the same operation has the same intended effect as one execution. |
| [Immutability](../compendium/immutability.md) | `design-property` | Prefer values that do not change after construction where this reduces reasoning and concurrency risk. |
