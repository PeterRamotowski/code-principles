# Drupal Framework Adapter

## Purpose

Apply this adapter after PHP and Symfony. Drupal may use their runtime and container guidance, but it defines
its own extension, plugin, hook, entity, cacheability metadata, configuration, and host-compatibility policy.

## Extension APIs, plugins, and hooks

Use a documented Drupal extension API before patching core or depending on an internal service. Plugins are
appropriate for discoverable, configurable implementations of a defined plugin contract. Keep annotations
or attributes, derivatives, and plugin definitions compatible with discovery and cache rebuild behavior.

Hooks and event subscribers SHOULD delegate quickly to cohesive services. A hook is preferable when it is the
stable host extension point; a Symfony event is preferable when that is Drupal's supported lifecycle seam.
Do not duplicate one behavior across both. Public module APIs, alter hooks, plugin IDs, routes, permissions,
and service IDs require explicit compatibility review.

## Entities and configuration

Use content entities for fieldable, revisionable, translatable, or user-managed content and configuration
entities for deployable definitions. Do not treat entity objects as generic arrays or bypass access checks.
Query access MUST be intentional, and entity updates SHOULD use the storage and field APIs so caches,
translations, revisions, and hooks remain correct.

Separate shipped default configuration, optional configuration, and mutable active configuration. Define
configuration schema for typed values and translations. Installation, update hooks, post-updates, and entity
schema changes MUST form a deployable upgrade path; never assume editing an install file updates a site.

## Rendering and cacheability metadata

Render arrays carry output and cacheability metadata together. Every result MUST bubble all relevant cache
tags, cache contexts, and max-age. Personalized output needs the context that varies it; entity-derived
output needs the entity's tags. Setting max-age zero is a last resort, not a substitute for dependency
modeling. Invalidate by the narrowest correct tags rather than flushing broad caches.

## Host compatibility and review checklist

Preserve Drupal routing, services, plugins, hooks, forms, render arrays, and update conventions for ordinary
module code. Confirm supported core/PHP versions and deprecation paths before changing an extension contract.

1. Is the implementation on a documented extension API with a stable owner?
2. Are plugins and hooks cohesive, discoverable, and free of duplicated dispatch?
3. Are entity access, revisions, translations, and storage lifecycle preserved?
4. Is configuration typed and accompanied by a safe install/update path?
5. Does render output carry complete cacheability metadata?

## Non-goals

This adapter does not reduce Drupal to generic Symfony, bypass host APIs, or restate PHP and Composer policy.
