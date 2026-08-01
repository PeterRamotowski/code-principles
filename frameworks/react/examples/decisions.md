# React adapter decisions

## Positive example

A searchable list keeps the query beside the list, derives filtered rows during rendering, uses stable item
IDs as keys, and places the network subscription in one effect with complete cleanup. Tests type in the
labelled search box and assert the visible results.

## Negative example

The same screen copies filtered rows into state, synchronizes them through chained effects, keys rows by
position, moves all values into a global store, and tests private hook calls.
