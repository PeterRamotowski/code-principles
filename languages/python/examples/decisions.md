# Python adapter decisions

## Positive example

A backend service parses request mappings into validated frozen domain records, owns its transaction with a
context manager, and uses bounded async tasks only for independent I/O. Domain services depend on a small
consumer-owned `Protocol` for the integration they call.

## Negative example

A request mapping is cast to a typed dictionary and assumed valid, all service classes inherit a speculative
base class, and CPU-heavy work is moved into `async def`. None of those choices changes runtime validity,
substitutability, or CPU scheduling.

## Public package example

A package re-exports its supported functions and exception types from a stable module, keeps implementation
modules private, and verifies that type annotations do not expose an optional dependency as a required
consumer contract.
