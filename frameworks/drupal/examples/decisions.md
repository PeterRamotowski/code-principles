# Drupal adapter decisions

## Positive example

A module implements the documented plugin contract, stores deployable definitions as typed configuration,
uses entity storage and access APIs, ships a post-update path, and returns render arrays with precise cache
tags, contexts, and max-age.

## Negative example

A module patches core, edits only its install schema on an existing site, bypasses entity access, stores
content in active configuration, and fixes personalized cache leakage by flushing every cache globally.
