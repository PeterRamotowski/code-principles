# PHP adapter decisions

## Positive example

A package declares strict typing, parses an external string into a validated value object, exposes a small
Composer namespace and documented exception family, and validates the targets of its optional attributes.

## Negative example

A worker assumes `strict_types` validates request arrays, stores per-job identity in a static property, catches
every `Throwable`, scans reflection metadata repeatedly, and exposes framework internals through its package API.

## Long-running process example

A queue consumer owns one transaction per message, resets scoped services in `finally`, bounds its metadata
cache, records failed cleanup, and stops accepting work before graceful process shutdown.
