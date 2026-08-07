# Offline First Modifier

## Activation

Activate when core behavior must remain useful without connectivity and local changes synchronize after interruptions.

## Required effects

Select `distributed-reliability: eventually-consistent` and `state-and-side-effects: single-owner-mutation`. Define locally authoritative operations, stable identities, durable pending work, ordering, duplicate handling, conflict semantics, convergence, rejection, retry, repair, retention, and schema evolution. The interface MUST distinguish local acceptance, pending synchronization, rejection, and confirmed remote state.

## Prohibitions and review

Do not use last-write-wins without domain justification, discard conflicts silently, or show remote confirmation before durable acknowledgement. Test interruption and recovery at each synchronization boundary.
