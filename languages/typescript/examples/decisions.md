# TypeScript adapter decisions

## Positive example

A backend handler accepts decoded JSON as `unknown`, parses it once into a tagged command union, and passes
that union to the transaction owner. Exhaustive handling rejects newly introduced variants at compile time,
while runtime parsing protects the actual trust boundary.

## Negative example

A handler casts request JSON to `CreateOrder`, uses `any` for a mismatched field, and adds a recursive generic
mapper to make the compiler accept it. The cast supplies no runtime evidence and the generic hides rather
than resolves the contract mismatch.

## Public package example

A library names its exported result types and exposes them from its package entry point. Implementation-only
dependency types stay private, and a release review checks emitted declarations together with runtime
behavior.
