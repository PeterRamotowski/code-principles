# Vue adapter decisions

## Positive example

A component treats props as read-only, derives display state with a computed value, emits an explicit edit
request, and extracts one composable that owns a shared subscription and scope cleanup.

## Negative example

A component mutates a prop, destructures a reactive object and loses updates, mirrors computed data through
a watcher, and puts component-local state into a global store.
