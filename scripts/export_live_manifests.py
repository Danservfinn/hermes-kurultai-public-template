#!/usr/bin/env python3
"""Export sanitized structural manifests from a live Hermes/Brain host.
This script is intentionally conservative: it redacts likely secrets, personal identifiers,
delivery targets, and absolute home paths. Review output before committing.
"""
from __future__ import annotations
import json, re, os, datetime
from pathlib import Path
try:
    import yaml
except ImportError:
    raise SystemExit("Install PyYAML first: python3 -m pip install pyyaml")
HOME=Path.home()
OUT=Path(__file__).resolve().parents[1]/'manifests'
OUT.mkdir(exist_ok=True)
SENSITIVE_FIELD=re.compile(r'(token|secret|key|password|credential|cookie|auth|chat|phone|email|api)', re.I)
def clean(k,v):
    if SENSITIVE_FIELD.search(str(k)): return '[REDACTED]'
    if isinstance(v,dict): return {kk:clean(kk,vv) for kk,vv in v.items()}
    if isinstance(v,list): return [clean(k,x) for x in v]
    if isinstance(v,str):
        s=v.replace(str(HOME),'${HOME}')
        if '@' in s or re.search(r'\d{6,}',s): return '[REDACTED]'
        return s
    return v
cfgp=HOME/'.hermes/config.yaml'
if cfgp.exists():
    cfg=yaml.safe_load(cfgp.read_text()) or {}
    (OUT/'hermes-config.manifest.yaml').write_text(yaml.safe_dump(clean('config',cfg), sort_keys=True))
print('Wrote sanitized manifests to', OUT)
