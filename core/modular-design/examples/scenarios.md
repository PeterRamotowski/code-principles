# Modular Design Decision Examples

## Positive example — cohesive feature boundary

- Context: validation, state transition, and presentation for one capability change together.
- Mode: `feature-oriented`.
- Decision: keep them under one feature boundary with a focused external contract and hidden state details.
- Why it fits: ownership and coordinated change are visible while consumers know little.
- Rejected alternative: distribute each concern into repository-wide technical layers.

## Negative example — service per noun

- Context: a small application has cohesive modules and one deployment lifecycle.
- Mode: `service-oriented` was proposed without operational evidence.
- Bad decision: create an independently communicating service for each domain noun.
- Why it fails: network and operational coupling replace simple in-process collaboration.
- Better decision: retain module boundaries until deployment, ownership, scaling, or isolation requires more.
