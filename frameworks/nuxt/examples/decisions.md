# Nuxt adapter decisions

## Positive example

A page uses SSR-aware data fetching with a stable key, reuses the transferred payload during hydration,
keeps private runtime configuration in a server route, and follows file routing and auto-import conventions.

## Negative example

A universal plugin reads browser globals during SSR, stores request data in process-global state, leaks a
secret through public configuration, and refetches the page payload immediately during hydration.
