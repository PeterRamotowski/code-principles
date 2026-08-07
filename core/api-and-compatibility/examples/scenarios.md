# API and Compatibility Decision Examples

## Positive example — additive migration

- Context: independent consumers need a replacement for a supported operation.
- Mode: `external-api`.
- Decision: add the replacement, preserve the old behavior for a published window, provide migration evidence, then remove it in an allowed version.
- Why it fits: consumers can upgrade independently.

## Negative example — accidental public surface

- Context: internal helpers are reachable only through unsupported reflection.
- Mode: `public-library`.
- Bad decision: declare every observable helper permanently supported.
- Better decision: protect intentional contracts, assess real usage, and avoid expanding promises without evidence.
