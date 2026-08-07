# Strict Backward Compatibility Modifier

## Activation

Activate when supported consumers cannot upgrade atomically or a declared support window requires existing observable behavior.

## Required effects

Select `safe-change: compatibility-first` while retaining the base profile's API mode. Inventory supported signatures and observable semantics, including errors, ordering, defaults, serialization, and side effects. Prefer additive evolution and internal translation. Any deprecation MUST name an alternative, window, verification method, and removal condition.

## Prohibitions and review

Do not break consumers for internal cleanup or infer compatibility from compilation alone. Compatibility is not permission to retain unsafe ambiguity forever; use explicit normalization and a migration when tightening is necessary. Review evidence across every supported consumer and version.
