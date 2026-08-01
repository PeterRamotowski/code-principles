# Go adapter decisions

## Positive example

A package returns a concrete parser, lets its consumer define a two-method interface, wraps parse failures
while preserving a documented error identity, and runs no background goroutine beyond the caller's context.

## Negative example

A package exports a provider-wide interface, compares error strings, stores contexts in structs, starts an
unbounded goroutine per input, and adds a pool because one synthetic benchmark appeared faster.

## Concurrency example

A service uses a mutex for one coherent in-memory index, a bounded channel for ownership transfer to workers,
and an owner that cancels and waits for every worker before shutdown.
