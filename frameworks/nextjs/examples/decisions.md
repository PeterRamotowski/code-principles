# Next.js adapter decisions

## Positive example

A product page renders on the server, passes a small serializable model to its interactive client control,
keeps credentials in a server-only module, and documents cache tags and invalidation after an update. Its
server action parses and authorizes every request.

## Negative example

A top-level client marker pulls data access toward the browser, a shared cache stores user-specific results,
and a server action trusts hidden form values because only the application's UI is expected to call it.
