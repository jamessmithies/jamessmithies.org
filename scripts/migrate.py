#!/usr/bin/env python3
"""
Migrate Django fixtures to Hugo content files.
Run from the repo root: python3 hugo-site/scripts/migrate.py
"""

import json
import os
import re
from datetime import datetime

FIXTURE_PATH = "web/projectfiles/fixtures/jsorg_backup.json"
CONTENT_DIR = "hugo-site/content"


def load_fixtures():
    with open(FIXTURE_PATH) as f:
        return json.load(f)


def build_lookups(data):
    categories = {}
    tags = {}
    for item in data:
        if item["model"] == "blog.category":
            categories[item["pk"]] = {
                "title": item["fields"]["title"],
                "slug": item["fields"]["slug"],
            }
        elif item["model"] == "blog.tag":
            tags[item["pk"]] = {
                "title": item["fields"]["title"],
                "slug": item["fields"]["slug"],
            }
    return categories, tags


def escape_yaml(s):
    """Escape a string for YAML double-quoted scalar."""
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    return s


def migrate_blog_entries(data, categories_lookup, tags_lookup):
    # Build M2M relationships from through tables or inline fields
    entries = [item for item in data if item["model"] == "blog.entry"]

    for entry in entries:
        fields = entry["fields"]
        pk = entry["pk"]

        # Parse date
        pub_date_str = fields["pub_date"]
        dt = datetime.fromisoformat(pub_date_str.replace("Z", "+00:00"))

        year = dt.strftime("%Y")
        month = dt.strftime("%m")
        day = dt.strftime("%d")
        slug = fields["slug"]

        # Determine draft status
        status = fields["status"]
        draft = status != 1  # 1=Live, 2=Draft, 3=Hidden

        # Get categories and tags
        cat_ids = fields.get("categories", [])
        tag_ids = fields.get("tags", [])
        cat_titles = [categories_lookup[c]["title"] for c in cat_ids if c in categories_lookup]
        tag_titles = [tags_lookup[t]["title"] for t in tag_ids if t in tags_lookup]

        # Build frontmatter
        lines = ["---"]
        lines.append(f'title: "{escape_yaml(fields["title"])}"')
        lines.append(f"date: {pub_date_str}")
        lines.append(f'slug: "{slug}"')
        if draft:
            lines.append("draft: true")

        if cat_titles:
            lines.append("categories:")
            for c in cat_titles:
                lines.append(f'  - "{escape_yaml(c)}"')

        if tag_titles:
            lines.append("tags:")
            for t in tag_titles:
                lines.append(f'  - "{escape_yaml(t)}"')

        if fields.get("excerpt"):
            lines.append(f'excerpt: "{escape_yaml(fields["excerpt"])}"')

        if fields.get("featured"):
            lines.append("featured: true")

        if fields.get("hero_image"):
            lines.append(f'hero_image: "/media/{fields["hero_image"]}"')

        lines.append("---")
        lines.append("")
        lines.append(fields.get("body", ""))

        content = "\n".join(lines)

        # Create directory and write file
        dir_path = os.path.join(CONTENT_DIR, "blog", year, month, day, slug)
        os.makedirs(dir_path, exist_ok=True)
        filepath = os.path.join(dir_path, "index.md")
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  Blog: {year}/{month}/{day}/{slug}")


def migrate_static_pages(data):
    """Migrate Bio, Design, Credits, Research single-record pages."""
    page_models = {
        "index.bio": ("bio", "Bio"),
        "index.design": ("design", "Site Design"),
        "index.credits": ("credits", "Site Credits"),
        "index.research": ("research", "Research"),
    }

    for model_name, (section, default_title) in page_models.items():
        items = [item for item in data if item["model"] == model_name]
        if not items:
            continue
        item = items[0]
        fields = item["fields"]
        title = fields.get("title", default_title)
        about = fields.get("about", "")

        lines = ["---"]
        lines.append(f'title: "{escape_yaml(title)}"')
        lines.append(f'layout: "list"')
        lines.append("---")
        lines.append("")
        lines.append(about)

        dir_path = os.path.join(CONTENT_DIR, section)
        os.makedirs(dir_path, exist_ok=True)
        filepath = os.path.join(dir_path, "_index.md")
        with open(filepath, "w") as f:
            f.write("\n".join(lines))
        print(f"  Page: {section}")


def migrate_projects(data):
    """Migrate projects - combine overview + individual projects into one page."""
    projects = [item for item in data if item["model"] == "index.projects"]
    projects.sort(key=lambda x: x["fields"].get("position", 0))

    lines = ["---"]
    lines.append('title: "Projects"')
    lines.append('layout: "list"')
    lines.append("---")
    lines.append("")

    for proj in projects:
        fields = proj["fields"]
        title = fields.get("title", "")
        about = fields.get("about", "")
        position = fields.get("position", 0)

        if position == 0 or title.lower() == "overview":
            # Overview goes as intro content
            lines.append(about)
            lines.append("")
        else:
            lines.append(f"<h5>{title}</h5>")
            lines.append(about)
            lines.append("")

    dir_path = os.path.join(CONTENT_DIR, "projects")
    os.makedirs(dir_path, exist_ok=True)
    filepath = os.path.join(dir_path, "_index.md")
    with open(filepath, "w") as f:
        f.write("\n".join(lines))
    print("  Page: projects")


def create_homepage():
    """Create minimal homepage content file."""
    lines = ["---"]
    lines.append('title: "jamessmithies.org"')
    lines.append("---")

    filepath = os.path.join(CONTENT_DIR, "_index.md")
    with open(filepath, "w") as f:
        f.write("\n".join(lines))
    print("  Page: homepage")


def create_blog_index():
    """Create blog section index."""
    lines = ["---"]
    lines.append('title: "Blog"')
    lines.append("aliases:")
    lines.append("  - /blog/1/")
    lines.append("---")

    dir_path = os.path.join(CONTENT_DIR, "blog")
    os.makedirs(dir_path, exist_ok=True)
    filepath = os.path.join(dir_path, "_index.md")
    with open(filepath, "w") as f:
        f.write("\n".join(lines))
    print("  Page: blog index")


def create_taxonomy_terms(data):
    """Create _index.md for each category and tag with explicit slugs."""
    for item in data:
        if item["model"] == "blog.category":
            slug = item["fields"]["slug"]
            title = item["fields"]["title"]
            dir_path = os.path.join(CONTENT_DIR, "categories", slug)
            os.makedirs(dir_path, exist_ok=True)
            with open(os.path.join(dir_path, "_index.md"), "w") as f:
                f.write(f'---\ntitle: "{escape_yaml(title)}"\nslug: "{slug}"\n---\n')
            print(f"  Category: {slug}")

        elif item["model"] == "blog.tag":
            slug = item["fields"]["slug"]
            title = item["fields"]["title"]
            dir_path = os.path.join(CONTENT_DIR, "tags", slug)
            os.makedirs(dir_path, exist_ok=True)
            with open(os.path.join(dir_path, "_index.md"), "w") as f:
                f.write(f'---\ntitle: "{escape_yaml(title)}"\nslug: "{slug}"\n---\n')
            print(f"  Tag: {slug}")


def main():
    print("Loading fixtures...")
    data = load_fixtures()
    categories, tags = build_lookups(data)

    print(f"\nFound: {len(categories)} categories, {len(tags)} tags")
    print(f"Found: {sum(1 for d in data if d['model'] == 'blog.entry')} blog entries")

    print("\nMigrating blog entries...")
    migrate_blog_entries(data, categories, tags)

    print("\nMigrating static pages...")
    migrate_static_pages(data)
    migrate_projects(data)

    print("\nCreating homepage...")
    create_homepage()

    print("\nCreating blog index...")
    create_blog_index()

    print("\nCreating taxonomy term pages...")
    create_taxonomy_terms(data)

    print("\nDone! Content files written to hugo-site/content/")


if __name__ == "__main__":
    main()
