HUGO = $(HOME)/.local/bin/hugo
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python3

# Set up virtual environment
venv:
	python3 -m venv $(VENV) && $(PIP) install pyzotero beautifulsoup4 requests

# Hugo site
serve:
	$(HUGO) server

build:
	$(HUGO) && mkdir -p docs/blog/feed && cp docs/blog/index.xml docs/blog/feed/index.html

# Update external data
mastodon:
	$(PYTHON) scripts/mastodon.py

zotero:
	$(PYTHON) scripts/zotero/update_zotero.py
