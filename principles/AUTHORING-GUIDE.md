# Principle Entry Authoring Guide

Each canonical entry MUST answer the following questions:

1. What kind of concept is this?
2. What is its narrow canonical interpretation in this project?
3. Which problem is it intended to reduce?
4. Under which conditions is it useful?
5. What common interpretations are explicitly rejected?
6. What costs or trade-offs does it introduce?
7. Which other entries can conflict with it?
8. Which entries reinforce it?
9. Which Core Skill owns its operational interpretation?
10. What is one positive example and one counterexample?

## Normative quality requirements

An entry MUST NOT:

- claim universal applicability unless it describes a safety or correctness invariant whose scope is explicit;
- use a slogan as the complete definition;
- define correctness by line count, class count, interface count, test count, or another context-free metric;
- prescribe a language-specific technique in the canonical language-agnostic statement;
- cite an external Skill as authority;
- duplicate full operational rules owned by a Core Skill.

## External references

References MAY document historical attribution or further reading. They are supplementary. A reference MUST NOT be required for the installed plugin to function, and changes in an external source MUST NOT silently change this project’s policy.

## Change review

A change to a canonical statement, rejected interpretation, conflict, or Core Skill ownership is behaviorally significant and requires:

- a changelog entry;
- review of affected relationships;
- review of generated compendium output;
- at least one evaluation scenario update when model behavior may change.
