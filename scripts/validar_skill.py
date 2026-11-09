#!/usr/bin/env python3
"""Confere a estrutura estática do pacote Low Ticket Autopilot (sem rede)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'SKILL.md'
errors = []
if not SKILL.is_file():
    errors.append('SKILL.md ausente')
else:
    data = SKILL.read_text(encoding='utf-8')
    if not data.startswith('---\n'):
        errors.append('YAML frontmatter ausente')
    if not re.search(r'^name: low-ticket-autopilot$', data, re.M):
        errors.append('name incorreto')
    if not re.search(r'^description: .+', data, re.M):
        errors.append('description ausente')
    paths = re.findall(r'`((?:references|assets)/[\w.-]+\.(?:md|csv|json))`', data)
    for rel in sorted(set(paths)):
        if not (ROOT / rel).is_file():
            errors.append(f'Referência ausente: {rel}')
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix in ('.md', '.json', '.csv', '.py'):
        try:
            p.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            errors.append(f'Arquivo não UTF-8: {p.relative_to(ROOT)}')
if errors:
    print('FALHA:\n- ' + '\n- '.join(errors))
    sys.exit(1)
print(f'OK: skill validada; {len([p for p in ROOT.rglob("*") if p.is_file()])} arquivos.')
