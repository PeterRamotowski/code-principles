# Manual Testing

## Purpose

Manual testing verifies that Code Principles improves an agent's implementation or review of a real task. It
complements deterministic resolver evaluations; it does not replace the target repository's own verification.

## Generate a task bundle

Run the orchestrator from this repository and point it at the repository under test:

```bash
python3 tools/orchestrate.py \
  --repository /absolute/path/to/target \
  --task "Describe one concrete implementation or review task" \
  --format manual \
  --output /tmp/code-principles-manual.md
```

Give the generated Markdown bundle and access to the target repository to the coding agent. The bundle is
self-contained: it includes the resolved policy, selected Core Skills, profile, modifiers, inherited language
policy, and framework refinements. Do not preload unrelated adapters.

Before using a result, inspect the bundle header. If the detected profile or adapters are wrong, add an
`engineering-context.yaml` to the target or pass `--user-context`; do not test with a knowingly incorrect policy.

## Priority technology paths

Use these as starting tasks, replacing the paths and task wording with real work from the target project.

### PHP library

```bash
python3 tools/orchestrate.py --repository /path/to/php-library \
  --task "Add a value object to this public library without breaking supported consumers" \
  --format manual --output /tmp/code-principles-php.md
```

Expected chain: PHP, reusable-library profile, public API policy when public exposure is stated.

### Symfony application

```bash
python3 tools/orchestrate.py --repository /path/to/symfony-app \
  --task "Implement an approval workflow in this Symfony backend service" \
  --format manual --output /tmp/code-principles-symfony.md
```

Expected chain: PHP then Symfony. Exercise container conventions, Doctrine transaction ownership, or Messenger
redelivery rather than testing framework-neutral syntax.

### Drupal module

```bash
python3 tools/orchestrate.py --repository /path/to/drupal-module \
  --task "Add a configurable personalized entity summary to this Drupal module" \
  --format manual --output /tmp/code-principles-drupal.md
```

Expected chain: PHP, Symfony, then Drupal. Exercise an extension API, cacheability metadata, configuration schema,
entity access, or update path.

### JavaScript package

```bash
python3 tools/orchestrate.py --repository /path/to/javascript-package \
  --task "Add an asynchronous parser to this public JavaScript package" \
  --format manual --output /tmp/code-principles-javascript.md
```

Expected chain: JavaScript. Exercise runtime parsing, promise ownership, module exports, or observable errors.

### TypeScript package

```bash
python3 tools/orchestrate.py --repository /path/to/typescript-package \
  --task "Add an unknown-input parser and exported result type without breaking consumers" \
  --format manual --output /tmp/code-principles-typescript.md
```

Expected chain: inherited JavaScript runtime policy followed by TypeScript, while the concise selected language is
TypeScript. Exercise runtime validation, discriminated unions, declaration output, or generic complexity.

### Vue application

```bash
python3 tools/orchestrate.py --repository /path/to/vue-app \
  --task "Extract shared online-presence behavior into a Vue composable" \
  --format manual --output /tmp/code-principles-vue.md
```

Expected chain: JavaScript or TypeScript, then Vue. Exercise reactive identity, computed derivation, effect cleanup,
and local state ownership.

### Nuxt application

```bash
python3 tools/orchestrate.py --repository /path/to/nuxt-app \
  --task "Render a personalized page using a private provider credential in this Nuxt application" \
  --format manual --output /tmp/code-principles-nuxt.md
```

Expected chain: JavaScript or TypeScript, Vue, then Nuxt. Exercise SSR safety, server-only authority, data cache
identity, and hydration reuse.

## Review protocol

Run each task once without the bundle and once with it when a fair comparison is possible. Keep the model, target
revision, task, and tool permissions constant. Record:

- whether profile, modifiers, language, framework, and inherited adapters were correct;
- whether the agent followed repository-native conventions;
- whether technology-specific constraints materially affected its reasoning or patch;
- target tests, lint, type analysis, static analysis, and build results;
- prohibited behavior observed in either run;
- unnecessary abstraction, unrelated cleanup, or invented constraints;
- reviewer disposition: accept, accept with changes, or reject.

Do not treat a plausible explanation as a pass. For implementation tasks, inspect the patch and execute the
target repository's existing checks. For review tasks, verify findings against code and framework behavior.

## Review record

Record the date, reviewer, ecosystem, target repository and revision, task, model, bundle output, verification
commands, result, and actionable feedback. External practitioner sign-off remains required before a stable release.

