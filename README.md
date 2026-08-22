# lixin.ai

Personal academic homepage of [Xin Li](https://lixin.ai) — PhD student at Nanyang
Technological University, Singapore.

## How it works

Everything is `index.html`. It is a single self-contained file: the CSS lives in an
inline `<style>` block and the JavaScript in an inline `<script>` block, with no
build step, no dependencies, and no local stylesheet or script to link.

Edit `index.html` directly and push to `html_simple`; GitHub Pages deploys from that
branch and serves it at the `CNAME` domain.

```
index.html          the entire site
CNAME               lixin.ai
robots.txt
sitemap.xml         update lastmod, and add an entry, when pages change
_headers            inert on GitHub Pages; kept only for a possible Netlify move
data/               CV, portrait, share card, talk slides
images/             favicons
```

## Assets in use

| File | Used by |
| --- | --- |
| `data/Xin_Li_CV_2026.pdf` | the CV link in the identity rail |
| `data/XinLI_profile.webp` | the JSON-LD `Person.image` (full resolution source) |
| `data/avatar-280.webp` | the 140px portrait, preloaded |
| `data/share-card.jpg` | `og:image` / `twitter:image`, 1200x630 |
| `images/icon-32.png`, `images/icon-180.png` | favicon and apple-touch-icon |
| `data/talk_slides/*.pdf` | the Talks section |

Two superseded CVs (`data/XinLi_CV.pdf`, `data/Xin_Li_s_CV.pdf`) are kept
deliberately: their URLs were public for months and may still be linked from
application portals and email.

## When updating

Publications, news and the rest are hand-written HTML — there is no generator. A
Python one used to live in `scripts/`, driven by `data/publications.json`; it stopped
matching the markup, would have silently rebuilt the section from stale data, and was
removed. It is in the git history if it is ever wanted.

Three things are easy to forget when editing:

- `sitemap.xml` — bump `lastmod`, and add a `<url>` entry for any new page.
- the JSON-LD `dateModified` near the top of `index.html`.
- the "Last updated" line in the footer.
