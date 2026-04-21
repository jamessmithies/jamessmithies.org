https://jamessmithies.org

A personal website and blog, established 2010. Originally built with WordPress, then manually migrated to Django and hosted on various hardware (Raspberry Pi, EC2, VPS) before being converted to an offline Django -> static GitHub Pages solution. In 2026 the site was migrated from Django to Hugo, removing the need for Docker, PostgreSQL, Nginx, and the offline build process.

## Setup

1. Install Hugo (v0.145+):

```
curl -sL https://github.com/gohugoio/hugo/releases/download/v0.145.0/hugo_extended_0.145.0_linux-amd64.tar.gz | tar xz -C ~/.local/bin hugo
```

2. Create the Python virtual environment (required for `make mastodon`, `make zotero`, and `make publish`, which use Python scripts to fetch data from external APIs):

```
make venv
```

If the venv doesn't install correctly (e.g. `make zotero` fails with `ModuleNotFoundError`), recreate it manually:

```
rm -rf .venv
python3 -m venv .venv
.venv/bin/pip install pyzotero beautifulsoup4 requests
```

## Usage

```
make serve       # Local dev server at localhost:1313
make build       # Build static site to docs/
make mastodon    # Update Mastodon sidebar
make zotero      # Update Zotero bibliographies
```

## Publishing workflow

1. Edit content in `content/` (blog posts, static pages)
2. Preview locally with `make serve`
3. Optionally run `make zotero` if bibliography has changed
4. Optionally run `make mastodon` to update the Mastodon sidebar
5. Run `make build`
5. Commit and push to GitHub

## Project structure

```
hugo.toml        # Hugo configuration
content/         # Blog posts and pages (Markdown/HTML)
layouts/         # Hugo templates
static/          # CSS, favicon, media, CNAME
scripts/         # Mastodon and Zotero update scripts
docs/            # Built output (served by GitHub Pages)
makefile         # Build commands
```
