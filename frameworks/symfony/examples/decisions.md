# Symfony adapter decisions

## Positive example

A controller parses input and invokes an injected application service. One Doctrine transaction owns the
write, and the resulting Messenger message carries stable IDs to an idempotent handler with explicit retry
and failure policy.

## Negative example

A controller fetches services from the container, passes managed entities into an asynchronous message,
assumes exactly-once delivery, and relies on lazy loading after the request transaction ends.
