#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from distribution import distribution_files

ROOT = Path(__file__).resolve().parents[1]
version = (ROOT/'VERSION').read_text().strip()
archive = ROOT.parent / f'{ROOT.name}-v{version}.zip'
files = distribution_files(ROOT) + [ROOT / 'MANIFEST.sha256']

with ZipFile(archive, 'w', compression=ZIP_DEFLATED) as output:
    for path in sorted(files, key=lambda item: item.relative_to(ROOT).as_posix()):
        output.write(path, Path(ROOT.name) / path.relative_to(ROOT))

print(archive)
