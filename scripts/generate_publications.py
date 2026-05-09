#!/usr/bin/env python3
"""Generate the homepage publications section from data/publications.json."""

from __future__ import annotations

import json
import re
from datetime import date
from html import escape
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT_DIR / "data" / "publications.json"
INDEX_FILE = ROOT_DIR / "index.html"


def load_publications() -> dict:
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def format_author(author: str) -> str:
    author_html = escape(author)
    if "Xin Li" in author:
        return f"<u><strong>{author_html}</strong></u>"
    return author_html


def format_authors(authors: list[str]) -> str:
    return ", ".join(format_author(author) for author in authors)


def link_label(link: dict) -> str:
    text = link.get("text") or link.get("type") or "Link"
    labels = {
        "project": "Homepage",
        "Project Homepage": "Homepage",
        "homepage": "Homepage",
        "github": "Code",
        "pdf": "PDF",
        "arxiv": "arXiv",
    }
    return labels.get(text, text)


def generate_publication_item(pub: dict) -> str:
    links = []
    for link in pub.get("links", []):
        label = escape(link_label(link))
        url = escape(link["url"], quote=True)
        links.append(
            f'              <a href="{url}" target="_blank" rel="noopener noreferrer">{label}&nbsp;⤻</a>'
        )

    links_html = "\n".join(links)
    title = escape(pub["title"])
    authors = format_authors(pub.get("authors", []))
    venue = escape(pub.get("venue", ""))
    year = escape(str(pub.get("year", "")))

    return f"""          <article class="publication-item" role="listitem">
            <p class="pub-title">{title}</p>
            <p class="pub-authors">{authors}</p>
            <p class="pub-venue"><span class="venue-highlight">{venue}</span>, {year}</p>
            <div class="pub-links">
{links_html}
            </div>
          </article>"""


def generate_publications_section(data: dict) -> str:
    publications = [pub for pub in data.get("publications", []) if not pub.get("hidden")]
    items = "\n".join(generate_publication_item(pub) for pub in publications)
    return f"""      <section id="publications" aria-labelledby="publications-heading">
        <h2 id="publications-heading">Selected Publications</h2>
        <p class="section-note">
          (* indicates equal contribution. For a full list, please see my <a
            href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ" target="_blank"
            rel="noopener noreferrer">Google Scholar&nbsp;⤻</a>.)
        </p>
        <div class="publication-grid" role="list">

{items}
        </div>
      </section>"""


def display_date(today: date) -> str:
    return f"{today.strftime('%B')} {today.day}, {today.year}"


def update_index(publications_section: str) -> None:
    content = INDEX_FILE.read_text(encoding="utf-8")

    content, count = re.subn(
        r"\s*<section id=\"publications\" aria-labelledby=\"publications-heading\">.*?</section>",
        "\n" + publications_section,
        content,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise RuntimeError("Could not find the homepage publications section to replace.")

    today = date.today()
    content = re.sub(
        r'"dateModified": "[^"]+"',
        f'"dateModified": "{today.isoformat()}T10:00:00+08:00"',
        content,
        count=1,
    )
    content = re.sub(
        r"Last updated: [^.]+\.",
        f"Last updated: {display_date(today)}.",
        content,
        count=1,
    )

    INDEX_FILE.write_text(content, encoding="utf-8")


def main() -> None:
    data = load_publications()
    update_index(generate_publications_section(data))
    print(f"Updated {INDEX_FILE.relative_to(ROOT_DIR)} from {DATA_FILE.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    main()
