# Dependency and Boundary Decision Examples

## Positive example — volatile integration boundary

- Context: stable policy uses a provider with independently changing failure semantics.
- Mode: `domain-centric`.
- Decision: define a consumer-owned port in policy terms and adapt the provider at composition time.
- Why it fits: volatility and translation justify the boundary.

## Negative example — interface per implementation

- Context: one stable internal implementation has no alternate consumer, lifecycle, or test need.
- Mode: `framework-native`.
- Bad decision: add forwarding interfaces and wrappers only to claim dependency inversion.
- Better decision: use the implementation directly and introduce a boundary when evidence appears.
