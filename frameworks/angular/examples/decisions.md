# Angular adapter decisions

## Positive example

A standalone component owns synchronous UI state in signals, receives a feature-scoped service through
dependency injection, consumes its asynchronous stream with lifecycle-aware teardown, and uses a reactive
form because fields and validators are dynamic.

## Negative example

A root-scoped mutable service stores one component's form, copies every stream into a signal through manual
subscriptions, never tears them down, and locates dependencies through a global injector.
