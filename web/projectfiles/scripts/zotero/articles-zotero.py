#!/usr/bin/env python3
#https://pyzotero.readthedocs.io/en/latest/index.html?highlight=style#search-request-parameters-for-read-api-calls

from pyzotero import zotero
zot = zotero.Zotero('24279', 'user', 'q4Wn37R6q4P2RZTIfYuxYsei')

collectionID = ('XSUIUJR3') #articles collectionID
zot.add_parameters(content='bib', linkwrap='1', style='turabian-fullnote-bibliography', itemType='-attachment')
items = zot.collection_items(collectionID)

bibliography = ''
for item in items:
    bibliography += item + '\n'

with open('web/projectfiles/templates/zotero/articles-bibliography.html', 'w') as f:
    f.write(str(bibliography))






