# Framework Adapters

Framework adapters refine language-independent profiles and Core Skill modes with framework lifecycle,
boundary, state, extension, and convention decisions. They do not replace their required language or parent
framework adapters.

## Implemented adapters

- [React](react/SKILL.md) — components, composition, state locality, effects, and behavior-focused testing;
- [Next.js](nextjs/SKILL.md) — server/client execution, rendering, caching, actions, routing, and secrets;
- [Vue](vue/SKILL.md) — reactivity, composables, component scope, local state, and effects;
- [Nuxt](nuxt/SKILL.md) — Vue refinement for SSR, boundaries, fetching, caching, routes, and auto-imports;
- [Angular](angular/SKILL.md) — DI, standalone components, signals/RxJS, forms, and services;
- [Symfony](symfony/SKILL.md) — container and request lifecycles, Messenger, Doctrine, and configuration;
- [Drupal](drupal/SKILL.md) — extension APIs, plugins, hooks, entities, cacheability, and configuration.

Each package contains schema-validated `adapter.yaml`, normative `SKILL.md`, and positive and negative
decision examples. Evaluation scenarios live in [`evaluations/scenarios/`](../evaluations/scenarios/).

React owns no TypeScript rules. Next.js combines React and TypeScript while defining its server/client
boundary. Nuxt refines Vue. Drupal builds on PHP and Symfony while retaining Drupal-specific host contracts.
