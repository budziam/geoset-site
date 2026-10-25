#!/usr/bin/env python3
"""Refresh the ?v= cache-busting hashes in the HTML files.

GitHub Pages serves assets with `cache-control: max-age=600`, so a browser can
keep showing a previous stylesheet or logo for ten minutes after a deploy. The
query string is derived from the file contents; run this script after editing
styles.css, logo.png or icon.png and commit the result.
"""
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = {
    "styles.css": "css",
    "logo.png": "logo",
    "icon.png": "icon",
}
PAGES = ["index.html", "404.html"]


def digest(name: str) -> str:
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()[:8]


def main() -> int:
    tags = {name: digest(name) for name in ASSETS}
    changed = []
    for page in PAGES:
        path = ROOT / page
        text = path.read_text()
        original = text
        for name, tag in tags.items():
            pattern = re.compile(re.escape(name) + r"\?v=[0-9a-f]*")
            text = pattern.sub(f"{name}?v={tag}", text)
        if text != original:
            path.write_text(text)
            changed.append(page)
    for name, tag in tags.items():
        print(f"{name:12} {tag}")
    print("updated:", ", ".join(changed) if changed else "nothing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
