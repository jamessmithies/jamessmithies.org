#!/usr/bin/env python3
"""
Fetch all Zotero bibliographies and write to Hugo partials.
Run from repo root: python3 scripts/zotero/update_zotero.py

Requires: pip install pyzotero
Set ZOTERO_API_KEY environment variable, or it falls back to the default key.
"""

import os
from pyzotero import zotero

ZOTERO_USER_ID = '24279'
ZOTERO_API_KEY = os.environ.get('ZOTERO_API_KEY', 'q4Wn37R6q4P2RZTIfYuxYsei')
OUTPUT_DIR = 'layouts/partials/zotero'

COLLECTIONS = {
    'books': 'PN9N565D',
    'articles': 'XSUIUJR3',
    'chapters': 'XI3XZQ9G',
    'conferences': 'ZIZIUZK7',
    'interviews': 'RUV7WJN6',
    'reports': 'B3CQRI3W',
    'reviews': 'VTXACJJ7',
    'software': 'UGLUWKRW',
    'talks': '23WVAUI9',
}

zot = zotero.Zotero(ZOTERO_USER_ID, 'user', ZOTERO_API_KEY)

for name, collection_id in COLLECTIONS.items():
    print(f'Fetching {name}...')
    zot.add_parameters(
        content='bib',
        linkwrap='1',
        style='turabian-fullnote-bibliography',
        itemType='-attachment',
        sort='date',
        direction='desc',
    )
    items = zot.collection_items(collection_id)

    bibliography = ''
    for item in items:
        bibliography += item + '\n'

    output_path = os.path.join(OUTPUT_DIR, f'{name}-bibliography.html')
    with open(output_path, 'w') as f:
        f.write(bibliography)
    print(f'  Written to {output_path}')

print('\nDone!')
