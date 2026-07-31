#!/usr/bin/env python3
from pathlib import Path
import hashlib
from distribution import distribution_files

ROOT=Path(__file__).resolve().parents[1]
lines=[]
for path in distribution_files(ROOT):
    lines.append(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}')
(ROOT/'MANIFEST.sha256').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Updated manifest for {len(lines)} files.')
