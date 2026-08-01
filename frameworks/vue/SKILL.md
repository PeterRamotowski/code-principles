# Vue Framework Adapter

## Purpose

Apply this adapter after the project profile and JavaScript adapter when Vue semantics affect the work.
Nuxt-specific SSR and routing decisions belong to the Nuxt adapter.

## Reactivity and state locality

Choose `ref` for an independently replaceable value and `reactive` for an intentionally proxied object.
Preserve ref or proxy identity across a public boundary; destructuring MUST NOT silently disconnect a value
from reactivity. Treat props as read-only input and emit an event or call an explicit owner operation to
request mutation.

Keep state in component scope while its lifetime and consumers are local. Lift it to a composable, provider,
or store only when shared ownership, persistence, or navigation requires that lifetime. Use computed values
for pure derivation. Watchers and watch effects are for synchronization or side effects, not duplicated state.

## Components and composables

Components SHOULD expose clear props, events, and slots while keeping incidental implementation private.
Preserve Vue template and single-file-component conventions for ordinary application code. Avoid dynamic
component machinery when direct composition communicates the supported variants.

Composables SHOULD represent cohesive reusable behavior with explicit inputs, outputs, side effects, and
cleanup. They MUST NOT become hidden global state by accident. When a composable acquires a listener, timer,
or subscription, tie cleanup to its owning scope.

Provide/inject is appropriate for subtree capabilities or stable context. Use explicit keys and defaults;
do not use injection to conceal arbitrary cross-application dependencies.

## Testing and review checklist

Test observable component behavior, emitted contracts, and composable results. Avoid assertions about proxy
internals or private component instances.

1. Is reactive identity preserved and mutation owned?
2. Is each derived value computed rather than mirrored?
3. Does every watcher own a necessary effect and cleanup?
4. Does each composable package a cohesive behavior rather than incidental reuse?
5. Are component contracts and user results tested instead of internals?

## Non-goals

This adapter does not select a store, router, UI library, or TypeScript policy and does not duplicate Nuxt.
