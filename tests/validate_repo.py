#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys, xml.etree.ElementTree as ET
from pathlib import Path
try:
    import yaml
except Exception:
    yaml=None
ROOT=Path(__file__).resolve().parents[1]
errors=[]
required=['README.md','LICENSE','CONTRIBUTING.md','config/config.template.yaml','brain/AGENTS.md','scripts/bootstrap.sh','manifests/hermes-config.manifest.yaml']
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'missing {rel}')
for p in (ROOT/'docs/assets').glob('*.svg'):
    try: ET.parse(p)
    except Exception as e: errors.append(f'invalid svg {p}: {e}')
for p in (ROOT/'manifests').glob('*.json'):
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f'invalid json {p}: {e}')
if yaml:
    for p in list((ROOT/'manifests').glob('*.yaml'))+list((ROOT/'config').glob('*.yaml')):
        try: yaml.safe_load(p.read_text())
        except Exception as e: errors.append(f'invalid yaml {p}: {e}')
private_key_marker = ''.join(['-----', 'BEGIN ']) + r'(?:RSA |OPENSSH |EC |DSA )?' + ''.join(['PRIVATE ', 'KEY', '-----'])
secret_patterns=[
    r'sk-[A-Za-z0-9]{20,}',
    r'gh[pousr]_[A-Za-z0-9_]{20,}',
    r'\b\d{7,12}:[A-Za-z0-9_-]{30,}\b',
    private_key_marker,
    r'(?i)(api[_-]?key|token|secret|password)[ \t]*[:=][ \t]*[^\s#]{16,}',
]
privacy_patterns=[
    '/' + 'Users' + '/' + 'kublai',
    r'(?i)hard-private',
    r'(?i)TELEGRAM_CHAT_ID\s*[:=]\s*[-0-9]{6,}',
]
skip_dirs={'.git','__pycache__'}
for p in ROOT.rglob('*'):
    if not p.is_file() or any(part in skip_dirs for part in p.parts): continue
    if p.suffix.lower() in {'.png','.jpg','.jpeg','.gif','.pdf'}: continue
    txt=p.read_text(errors='ignore')
    for pat in secret_patterns:
        if re.search(pat, txt): errors.append(f'secret-like pattern in {p.relative_to(ROOT)}: {pat}')
    # allow hard-private mention only in boundary docs/readme/gitignore as excluded path
    for pat in privacy_patterns:
        if re.search(pat, txt) and p.name not in {'README.md','.gitignore','security-boundary.md','validate_repo.py'}:
            errors.append(f'privacy pattern in {p.relative_to(ROOT)}: {pat}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('OK: public template validation passed')
