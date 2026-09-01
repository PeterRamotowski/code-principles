# Code Principles

<div class="hero" markdown>

## Engineering guidance that adapts to the project

A self-contained, language-agnostic knowledge base and policy system for AI coding agents — presented here as a browsable engineering handbook.

[Browse the 72 principles](principles/index.md){ .md-button .md-button--primary }
[Explore the decision system](core/index.md){ .md-button }

</div>

<div class="home-grid" markdown>

<div class="home-card" markdown>

### Principles

Canonical engineering ideas with explicit applicability, rejected interpretations, trade-offs, conflicts, examples, and AI guidance.

[Browse principles →](principles/index.md)

</div>

<div class="home-card" markdown>

### Core Skills

Decision procedures that combine principles into practical modes for clarity, abstraction, testing, compatibility, reliability, performance, and more.

[Explore Core Skills →](core/index.md)

</div>

<div class="home-card" markdown>

### Project profiles

Start from what you are building: application, library, service, worker, pipeline, plugin, prototype, CLI, real-time system, infrastructure tool, and more.

[Choose a project profile →](profiles/index.md)

</div>

<div class="home-card" markdown>

### Technology refinements

See how generic policy is refined for JavaScript, TypeScript, Python, PHP, Go, C++, React, Next.js, Vue, Nuxt, Angular, Symfony, and Drupal.

[Browse languages →](languages/index.md) · [Browse frameworks →](frameworks/index.md)

</div>

</div>

## How the policy model works

<div class="resolution-flow" role="list" aria-label="Policy resolution flow">
  <div role="listitem"><strong>1</strong><span>Project evidence</span><small>task, repository, explicit context</small></div>
  <div class="resolution-flow__arrow" aria-hidden="true">→</div>
  <div role="listitem"><strong>2</strong><span>Project profile</span><small>dominant artifact and failure model</small></div>
  <div class="resolution-flow__arrow" aria-hidden="true">→</div>
  <div role="listitem"><strong>3</strong><span>Modifiers</span><small>verified cross-cutting constraints</small></div>
  <div class="resolution-flow__arrow" aria-hidden="true">→</div>
  <div role="listitem"><strong>4</strong><span>Core Skills</span><small>context-sensitive decision modes</small></div>
  <div class="resolution-flow__arrow" aria-hidden="true">→</div>
  <div role="listitem"><strong>5</strong><span>Technology adapters</span><small>language and framework semantics</small></div>
  <div class="resolution-flow__arrow" aria-hidden="true">→</div>
  <div role="listitem"><strong>6</strong><span>Resolved policy</span><small>explainable engineering decisions</small></div>
</div>

!!! info "The website is a generated view"
    Canonical YAML and normative Markdown in the repository remain authoritative. This site is rebuilt from those sources and is never an independent source of policy.

## Learn by example

The repository includes executable evaluation scenarios that test profile selection, modifiers, language and framework refinements, conflict decisions, and forbidden overengineering. They are useful both as tests and as worked examples of the policy model.

[Browse evaluation scenarios](evaluations/index.md){ .md-button }

## Reference

For the complete system contracts and architecture, continue with the [Specification](SPECIFICATION.md), [Architecture](ARCHITECTURE.md), [Knowledge Model](KNOWLEDGE-MODEL.md), and [Conflict Resolution](CONFLICT-RESOLUTION.md).
