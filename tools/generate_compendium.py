#!/usr/bin/env python3
"""Generate registry, relationships, indexes, categories, and compendium Markdown."""
import argparse
from pathlib import Path
import yaml

parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true', help='Verify generated files without changing them.')
args = parser.parse_args()

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = ROOT / 'principles' / 'entries'
PRINCIPLES = ROOT / 'principles'
OUT = PRINCIPLES / 'compendium'
CAT_OUT = PRINCIPLES / 'categories'
errors = []

def load(path): return yaml.safe_load(path.read_text(encoding='utf-8'))
def emit(path, content):
    if args.check:
        if not path.is_file() or path.read_text(encoding='utf-8') != content:
            errors.append(f'{path.relative_to(ROOT)} is missing or stale')
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

def save(path, data): emit(path, yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100))
def bullets(values): return '\n'.join(f'- {value}' for value in values) if values else '- None recorded.'

categories = {x['id']: x['name'] for x in load(PRINCIPLES/'categories.yaml')['categories']}
entries = [load(path) for path in sorted(ENTRIES.glob('*.yaml'))]
by_id = {entry['id']: entry for entry in entries}
if len(by_id) != len(entries): raise SystemExit('Duplicate principle IDs detected.')

registry = {
    'schema_version': entries[0]['schema_version'] if entries else '0.8.0',
    'status': 'candidate',
    'canonical_source': 'principles/entries',
    'generated_outputs': ['principles/registry.yaml','principles/relationships.yaml','principles/INDEX.md','principles/categories','principles/compendium'],
    'principles': []
}
relationships = {'schema_version': registry['schema_version'], 'relationships': []}
expected_compendium = set()
for data in sorted(entries, key=lambda x: x['id']):
    pid=data['id']
    registry['principles'].append({
        'id':pid,'name':data['name'],'classification':data['classification'],'category':data['category'],
        'status':data['status'],'source':f'principles/entries/{pid}.yaml',
        'compendium':f'principles/compendium/{pid}.md','primary_core_skill':data['primary_core_skill']})
    for target in data.get('conflicts_with',[]):
        relationships['relationships'].append({'from':pid,'type':'may-conflict-with','to':target,'context_required':True})
    for target in data.get('reinforces',[]):
        relationships['relationships'].append({'from':pid,'type':'reinforces','to':target,'context_required':False})

    content=f"""---
id: {pid}
name: {data['name']}
classification: {data['classification']}
category: {data['category']}
status: {data['status']}
source: principles/entries/{pid}.yaml
generated: true
---

# {data['name']}

> {data['summary']}

## Canonical interpretation

{data['canonical_statement']}

## Purpose

{data['intent']}

## Apply when

{bullets(data['applies_when'])}

## This does not mean

{bullets(data['does_not_mean'])}

## Trade-offs

{bullets(data['trade_offs'])}

## Conflicts with canonical entries

{bullets([f'`{x}`' for x in data.get('conflicts_with',[])])}

## Broader policy tensions

{bullets([f'`{x}`' for x in data.get('tensions_with',[])])}

## Reinforces canonical entries

{bullets([f'`{x}`' for x in data.get('reinforces',[])])}

## Supports broader concerns

{bullets([f'`{x}`' for x in data.get('supports_concerns',[])])}

## Core Skill ownership

Primary owner: `{data['primary_core_skill']}`

## Positive example

{data['example']}

## Counterexample

{data['counterexample']}

## Guidance for AI models

{bullets(data['ai_guidance'])}

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/{pid}.yaml` and regenerate the compendium instead of editing this file directly.
"""
    output_path = OUT/f'{pid}.md'
    expected_compendium.add(output_path)
    emit(output_path, content)

save(PRINCIPLES/'registry.yaml', registry)
save(PRINCIPLES/'relationships.yaml', relationships)

expected_categories = set()
for cid, title in categories.items():
    items=sorted((x for x in entries if x['category']==cid), key=lambda x:x['name'])
    rows='\n'.join(f"| [{x['name']}](../compendium/{x['id']}.md) | `{x['classification']}` | {x['summary']} |" for x in items)
    output_path = CAT_OUT/f'{cid}.md'
    expected_categories.add(output_path)
    emit(output_path, f"""# {title}

This category groups related concepts for navigation. Category membership does not make every item equally normative.

| Entry | Classification | Summary |
|---|---|---|
{rows}
""")

rows='\n'.join(f"| [{x['name']}](compendium/{x['id']}.md) | `{x['classification']}` | [{categories[x['category']]}](categories/{x['category']}.md) | `{x['primary_core_skill']}` |" for x in sorted(entries,key=lambda x:x['name']))
emit(PRINCIPLES/'INDEX.md', f"""# Canonical Principles Index

The canonical machine-readable sources are stored in `principles/entries/`. This generated index provides human navigation for **{len(entries)}** catalogue entries.

| Entry | Classification | Category | Primary Core Skill |
|---|---|---|---|
{rows}
""")

if args.check:
    for path in set(OUT.glob('*.md')) - expected_compendium:
        errors.append(f'{path.relative_to(ROOT)} is an obsolete generated file')
    for path in set(CAT_OUT.glob('*.md')) - expected_categories:
        errors.append(f'{path.relative_to(ROOT)} is an obsolete generated file')
    if errors:
        print('Generated output check failed:')
        for error in sorted(errors):
            print(f'- {error}')
        raise SystemExit(1)
    print(f'Generated outputs are current: {len(categories)} category pages and {len(entries)} compendium pages.')
else:
    print(f'Generated registry, relationships, index, {len(categories)} category pages, and {len(entries)} compendium pages.')
