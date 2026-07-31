# Abstraction and Reuse Decision Examples

## Positive example — one policy owner

- Context: several entry points calculate the same governed eligibility rule and have begun to diverge.
- Mode: `balanced`.
- Decision: give the rule one authoritative owner and keep entry-point formatting local.
- Why it fits: shared knowledge changes together without coupling unrelated representations.
- Rejected alternative: leave policy copies in place because their surrounding code differs.

## Negative example — similarity trap

- Context: two workflows currently contain similar field-mapping steps but serve different consumers.
- Mode: `conservative`.
- Bad decision: introduce a configurable universal mapper after seeing the second shape.
- Why it fails: it couples independent concepts and predicts variation without evidence.
- Better decision: keep both mappings local until common knowledge and variation become stable.
