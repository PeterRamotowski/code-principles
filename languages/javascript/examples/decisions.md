# JavaScript adapter decisions

## Positive example

A package parses unknown JSON into a documented runtime shape, uses explicit conversion for its accepted
numeric grammar, exports only supported entry points, and awaits or explicitly owns every asynchronous job.

## Negative example

A package assumes parsed JSON matches a comment, defaults valid zero values with truthiness, mutates caller
objects, launches unobserved promises, and encourages consumers to import internal files directly.

## Module compatibility example

A library declares its supported ESM entry point and runtime versions, avoids import-time I/O, and treats a
future CommonJS compatibility layer as a separate tested consumer contract rather than a filename change.
