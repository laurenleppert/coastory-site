#!/usr/bin/env python3
"""Render coastory.app from the Coastory repo's legal markdown.

    python3 build.py [--source ../Coastory/docs/legal]

Reads privacy-policy.md and terms-of-service.md, converts the markdown subset
those files use (ATX headings, paragraphs, `-` lists, `>` blockquotes, tables,
**bold**, *italics*, `code`, [links](url)) into HTML, wraps each in the page
shell, and writes:

    privacy/index.html   ->  https://coastory.app/privacy
    terms/index.html     ->  https://coastory.app/terms

The markdown in the app repo is the source of truth. This script never edits
it, never strips its banners or bracketed markers, and has no dependencies
beyond the standard library, so the render is the same on any machine.

`index.html` (the landing page) is hand-written and NOT touched by this script.
"""
from __future__ import annotations

import argparse
import html
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_SOURCE = HERE.parent / "Coastory" / "docs" / "legal"

PAGES = {
    "privacy-policy.md": ("privacy", "Privacy Policy"),
    "terms-of-service.md": ("terms", "Terms of Service"),
}

# Links between the two legal docs are relative .md links in the repo; on the
# site they are sibling directories.
LINK_REWRITES = {
    "./privacy-policy.md": "/privacy/",
    "privacy-policy.md": "/privacy/",
    "./terms-of-service.md": "/terms/",
    "terms-of-service.md": "/terms/",
    "[PRIVACY URL]": "/privacy/",
    "[ACCOUNT DELETION URL]": "/delete-account/",
}


def inline(text: str) -> str:
    """Escape, then apply inline markdown (code, bold, italics, links)."""
    out = []
    # Code spans first so nothing inside them is touched.
    parts = re.split(r"(`[^`]*`)", text)
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            out.append(f"<code>{html.escape(part[1:-1])}</code>")
            continue
        seg = html.escape(part, quote=False)
        seg = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", seg)
        seg = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", seg)
        seg = re.sub(
            r"\[([^\]]+)\]\(([^)\s]+)\)",
            lambda m: f'<a href="{html.escape(LINK_REWRITES.get(m.group(2), m.group(2)), quote=True)}">{m.group(1)}</a>',
            seg,
        )
        out.append(seg)
    return "".join(out)


def slug(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)


def render_markdown(md: str) -> tuple[str, str]:
    """Return (title, body_html). Title is the first H1."""
    # Reference-style link definitions ([Privacy Policy]: ./privacy-policy.md).
    refs: dict[str, str] = {}
    lines_kept = []
    for line in md.splitlines():
        m = re.match(r"^\[([^\]]+)\]:\s*(\S+)\s*$", line)
        if m:
            refs[m.group(1)] = LINK_REWRITES.get(m.group(2), m.group(2))
        else:
            lines_kept.append(line)
    text = "\n".join(lines_kept)
    for name, url in refs.items():
        text = text.replace(f"[{name}]", f"[{name}]({url})")

    lines = text.splitlines()
    title = ""
    out: list[str] = []
    i = 0
    para: list[str] = []

    def flush_para():
        nonlocal para
        if para:
            out.append(f"<p>{inline(' '.join(s.strip() for s in para))}</p>")
            para = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush_para()
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush_para()
            level = len(m.group(1))
            heading = m.group(2).strip()
            if level == 1 and not title:
                title = heading
                out.append(f"<h1>{inline(heading)}</h1>")
            else:
                out.append(f'<h{level} id="{slug(heading)}">{inline(heading)}</h{level}>')
            i += 1
            continue

        if stripped.startswith(">"):
            flush_para()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(f'<blockquote><p>{inline(" ".join(quote))}</p></blockquote>')
            continue

        if stripped.startswith("- "):
            flush_para()
            out.append("<ul>")
            while i < len(lines) and lines[i].strip().startswith("- "):
                item = lines[i].strip()[2:]
                i += 1
                # Continuation lines (indented, non-blank, not a new bullet).
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() and not lines[i].strip().startswith("- "):
                    item += " " + lines[i].strip()
                    i += 1
                out.append(f"<li>{inline(item)}</li>")
            out.append("</ul>")
            continue

        if stripped.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            # Drop the separator row (|---|---|).
            body = [r for r in cells[1:] if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
            out.append('<div class="table-wrap"><table>')
            out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr></thead>")
            out.append("<tbody>")
            for r in body:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table></div>")
            continue

        if stripped in ("---", "***"):
            flush_para()
            out.append("<hr>")
            i += 1
            continue

        para.append(line)
        i += 1

    flush_para()
    return title, "\n".join(out)


SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Coastory</title>
<meta name="description" content="{description}">
<link rel="icon" href="/icon.png">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="/"><img src="/icon.png" alt="" width="36" height="36"><span>Coastory</span></a>
  <nav>
    <a href="/privacy/">Privacy</a>
    <a href="/terms/">Terms</a>
    <a href="/delete-account/">Delete account</a>
    <a href="/support/">Support</a>
  </nav>
</header>
<main class="doc">
{body}
</main>
<footer class="site-footer">
  <p>Coastory is made by Velocicoder. <a href="mailto:support@coastory.app">support@coastory.app</a></p>
</footer>
</body>
</html>
"""


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", type=pathlib.Path, default=DEFAULT_SOURCE, help="directory holding the legal .md files")
    args = ap.parse_args(argv)
    src: pathlib.Path = args.source
    if not src.is_dir():
        print(f"error: source directory not found: {src}", file=sys.stderr)
        return 2
    for name, (folder, page_title) in PAGES.items():
        md_path = src / name
        if not md_path.exists():
            print(f"error: missing {md_path}", file=sys.stderr)
            return 2
        title, body = render_markdown(md_path.read_text(encoding="utf-8"))
        out_dir = HERE / folder
        out_dir.mkdir(exist_ok=True)
        (out_dir / "index.html").write_text(
            SHELL.format(
                title=html.escape(title or page_title, quote=True),
                description=html.escape(f"Coastory {page_title}.", quote=True),
                body=body,
            ),
            encoding="utf-8",
        )
        print(f"wrote {folder}/index.html from {md_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
