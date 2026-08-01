# C++ adapter decisions

## Positive example

A backend operation owns its handle and transaction in RAII values, passes dependencies by non-owning
reference, and returns the subsystem's explicit result type. Shared state has one synchronized owner and no
resource escapes its required scope.

## Negative example

The same operation places every object in `shared_ptr`, catches all exceptions after partial mutation, and
returns raw owning pointers across a shared-library boundary. Ownership, recovery, and allocator responsibility
are all ambiguous.

## Stable ABI example

A public native library documents its supported toolchains and ABI boundary, hides private layout behind an
opaque implementation, and provides matching creation/destruction functions. Its template conveniences are
header-only source APIs and are not mislabeled as ABI-stable symbols.
