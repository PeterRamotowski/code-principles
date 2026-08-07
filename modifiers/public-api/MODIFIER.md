# Public API Modifier

## Activation

Activate when independently changing external consumers rely on an API, published library, extension point, command contract, or integration behavior. Mere visibility inside one atomically changed application is insufficient.

## Required effects

Select `api-and-compatibility: external-api` and `contracts-and-errors: strict-boundaries`. Identify consumer classes and supported names, data, errors, side effects, ordering, timing, and authorization. Document the contract and classify changes before implementation. Breaking changes require an explicit version, negotiation, deprecation, or coordinated migration path.

## Prohibitions and review

Do not expose internals accidentally, trust static declarations as runtime evidence, or silently change supported semantics. Review documentation, compatibility evidence, runtime validation, error stability, migration, and removal criteria.
