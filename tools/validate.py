#!/usr/bin/env python3
"""Validate schemas, metadata, canonical references, generated pages, and local Markdown links."""
from pathlib import Path
import hashlib, json, re, subprocess, sys, yaml
from jsonschema import Draft202012Validator
from distribution import distribution_files

ROOT=Path(__file__).resolve().parents[1]
errors=[]
version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
semantic_version_re=re.compile(r'^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$')
if not semantic_version_re.fullmatch(version): errors.append(f'VERSION is not valid semantic versioning: {version}')

def load_json(path): return json.loads(path.read_text(encoding='utf-8'))
def load_yaml(path): return yaml.safe_load(path.read_text(encoding='utf-8'))
def validate(path,schema_path):
    instance=load_yaml(path) if path.suffix in {'.yaml','.yml'} else load_json(path)
    schema=load_json(schema_path)
    for err in Draft202012Validator(schema).iter_errors(instance):
        errors.append(f'{path.relative_to(ROOT)}: {err.message}')

for path in sorted((ROOT/'schemas').glob('*.json')):
    try:
        schema=load_json(path)
        Draft202012Validator.check_schema(schema)
        if not schema.get('$id','').endswith(f':{version}'):
            errors.append(f'{path.relative_to(ROOT)}: $id version does not match VERSION')
        declared=schema.get('properties',{}).get('schema_version',{}).get('const')
        if declared is not None and declared != version:
            errors.append(f'{path.relative_to(ROOT)}: schema_version const does not match VERSION')
    except Exception as exc: errors.append(f'{path.relative_to(ROOT)}: invalid schema: {exc}')

entries={}
for path in sorted((ROOT/'principles/entries').glob('*.yaml')):
    validate(path,ROOT/'schemas/principle.schema.json')
    data=load_yaml(path)
    if data['id'] in entries: errors.append(f'duplicate principle id: {data["id"]}')
    entries[data['id']]=data
known=set(entries)
for pid,data in entries.items():
    for field in ('conflicts_with','reinforces'):
        for target in data.get(field,[]):
            if target not in known: errors.append(f'{pid}: {field} references unknown canonical principle {target}')
    if not (ROOT/'principles/compendium'/f'{pid}.md').exists(): errors.append(f'missing compendium page for {pid}')

validate(ROOT/'principles/registry.yaml',ROOT/'schemas/principle-registry.schema.json')
validate(ROOT/'principles/relationships.yaml',ROOT/'schemas/relationships.schema.json')
validate(ROOT/'orchestrator/skill.yaml',ROOT/'schemas/skill.schema.json')
validate(ROOT/'engineering-context.example.yaml',ROOT/'schemas/project-context.schema.json')
for path in sorted((ROOT/'orchestrator/examples').glob('*.yaml')): validate(path,ROOT/'schemas/resolved-policy.schema.json')
for path in sorted((ROOT/'evaluations/scenarios').glob('*.yaml')): validate(path,ROOT/'schemas/evaluation-scenario.schema.json')

registry=load_yaml(ROOT/'principles/registry.yaml')
if {x['id'] for x in registry['principles']} != known: errors.append('registry IDs do not match canonical entry IDs')

# Parse every YAML file.
for path in ROOT.rglob('*.yaml'):
    try:
        data=load_yaml(path)
        if isinstance(data,dict):
            for field in ('schema_version','specification_version','policy_version','version'):
                if field in data and data[field] != version:
                    errors.append(f'{path.relative_to(ROOT)}: {field} does not match VERSION')
    except Exception as exc: errors.append(f'{path.relative_to(ROOT)}: invalid YAML: {exc}')

# Keep user-facing version declarations aligned with the package version.
readme=(ROOT/'README.md').read_text(encoding='utf-8')
specification=(ROOT/'SPECIFICATION.md').read_text(encoding='utf-8')
changelog=(ROOT/'CHANGELOG.md').read_text(encoding='utf-8')
if f'Foundation version: `{version}`' not in readme: errors.append('README.md: foundation version does not match VERSION')
if f'Specification version: `{version}`' not in specification: errors.append('SPECIFICATION.md: specification version does not match VERSION')
if not re.search(rf'^## \[{re.escape(version)}\](?:\s|$)',changelog,re.MULTILINE): errors.append('CHANGELOG.md: missing release heading for VERSION')

# Generated pages must exactly match their canonical YAML sources.
generated=subprocess.run(
    [sys.executable,str(ROOT/'tools/generate_compendium.py'),'--check'],
    cwd=ROOT,
    text=True,
    capture_output=True,
)
if generated.returncode:
    detail=(generated.stdout or generated.stderr).strip()
    errors.append(f'generated outputs are not current{": " + detail if detail else ""}')

# The manifest must contain exactly the public distribution files and current hashes.
manifest_path=ROOT/'MANIFEST.sha256'
expected_manifest={path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in distribution_files(ROOT)}
actual_manifest={}
for line in manifest_path.read_text(encoding='utf-8').splitlines():
    digest,separator,relative=line.partition('  ')
    if not separator or not re.fullmatch(r'[0-9a-f]{64}',digest) or not relative:
        errors.append(f'MANIFEST.sha256: invalid line: {line}')
        continue
    if relative in actual_manifest: errors.append(f'MANIFEST.sha256: duplicate path: {relative}')
    actual_manifest[relative]=digest
if actual_manifest != expected_manifest:
    missing=sorted(set(expected_manifest)-set(actual_manifest))
    extra=sorted(set(actual_manifest)-set(expected_manifest))
    changed=sorted(path for path in set(actual_manifest)&set(expected_manifest) if actual_manifest[path] != expected_manifest[path])
    if missing: errors.append(f'MANIFEST.sha256: missing files: {", ".join(missing)}')
    if extra: errors.append(f'MANIFEST.sha256: unexpected files: {", ".join(extra)}')
    if changed: errors.append(f'MANIFEST.sha256: stale hashes: {", ".join(changed)}')

# Check relative Markdown links to local files, ignoring anchors and URLs.
link_re=re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for path in ROOT.rglob('*.md'):
    text=path.read_text(encoding='utf-8')
    for raw in link_re.findall(text):
        target=raw.split('#',1)[0].strip()
        if not target or '://' in target or target.startswith('mailto:'): continue
        resolved=(path.parent/target).resolve()
        try: resolved.relative_to(ROOT.resolve())
        except ValueError: errors.append(f'{path.relative_to(ROOT)}: link escapes repository: {raw}'); continue
        if not resolved.exists(): errors.append(f'{path.relative_to(ROOT)}: broken local link: {raw}')

if errors:
    print('Validation failed:')
    for err in errors: print(f'- {err}')
    sys.exit(1)
print(f'Validation passed: {len(entries)} canonical entries, schemas, examples, evaluations, YAML files, and local links.')
