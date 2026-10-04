#!/usr/bin/env python3
"""Render GUIDE.md to GUIDE.pdf using the same browser engine the site targets."""
import os, markdown, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "site" / "GUIDE.md"
OUT = ROOT / "site" / "GUIDE.pdf"
TMP = ROOT / "_guide.html"

body = markdown.markdown(SRC.read_text(encoding="utf-8"),
                         extensions=["tables", "fenced_code", "sane_lists"])

CSS = """
@page { size: A4; margin: 18mm 16mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.55 "DejaVu Sans", Arial, sans-serif; color: #15181c; margin: 0; }
h1 { font-size: 22pt; margin: 0 0 .2em; color: #15181c; }
h2 { font-size: 14pt; margin: 1.6em 0 .5em; padding-top: .5em;
     border-top: 2px solid #1f6f5c; color: #164f42; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 1.2em 0 .3em; color: #164f42; break-after: avoid; }
p, li { orphans: 2; widows: 2; }
ul, ol { padding-left: 1.3em; }
li { margin: .2em 0; }
hr { display: none; }
a { color: #1a5a4a; text-decoration: none; border-bottom: 1px solid #bcd6cd; }
code { font-family: "DejaVu Sans Mono", Consolas, monospace; font-size: 9pt;
       background: #f1efe9; padding: .1em .3em; border-radius: 3px; }
pre { background: #f6f4ee; border: 1px solid #e4e0d8; border-left: 3px solid #1f6f5c;
      border-radius: 5px; padding: .7em .9em; overflow-wrap: break-word;
      white-space: pre-wrap; break-inside: avoid; }
pre code { background: none; padding: 0; font-size: 8.6pt; line-height: 1.45; }
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; break-inside: avoid; }
th, td { border: 1px solid #e4e0d8; padding: .4em .6em; text-align: left; vertical-align: top; }
th { background: #eef3f1; }
strong { color: #0f1316; }
"""

TMP.write_text(
    f"<!doctype html><html lang='en'><head><meta charset='utf-8'>"
    f"<title>How to edit and publish this site</title><style>{CSS}</style></head>"
    f"<body>{body}</body></html>", encoding="utf-8")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(TMP.as_uri(), wait_until="load")
    pg.pdf(path=str(OUT), format="A4", print_background=True,
           display_header_footer=True,
           header_template="<div></div>",
           footer_template="<div style='font:8pt \"DejaVu Sans\",sans-serif;color:#8a8f98;"
                           "width:100%;padding:0 16mm;text-align:right'>"
                           "Editing &amp; publishing guide — page "
                           "<span class='pageNumber'></span> of <span class='totalPages'></span></div>",
           margin={"top": "16mm", "bottom": "16mm", "left": "0", "right": "0"})
    b.close()

TMP.unlink()
print("wrote", OUT, os.path.getsize(OUT), "bytes")
