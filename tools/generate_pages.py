from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def inline_md(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1" loading="lazy">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def slugify(index: int, title: str) -> str:
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return ascii_slug or f"section-{index}"


def extract_title_and_toc(md: str):
    title = "Codex Help"
    toc = []
    section_index = 0
    for line in md.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            section_index += 1
            raw = line[3:].strip()
            toc.append((slugify(section_index, raw), raw))
    return title, toc


def remove_inline_toc(md: str) -> str:
    lines = md.splitlines()
    result: list[str] = []
    skipping = False
    for line in lines:
        if line.strip() in {"## 目录", "## Contents"}:
            skipping = True
            continue
        if skipping and line.startswith("## "):
            skipping = False
        if not skipping:
            result.append(line)
    return "\n".join(result)


def render_markdown(md: str) -> str:
    lines = md.splitlines()
    html_lines: list[str] = []
    in_code = False
    code_lang = ""
    list_open = False
    table_buffer: list[str] = []
    section_index = 0

    def close_list():
        nonlocal list_open
        if list_open:
            html_lines.append("</ul>")
            list_open = False

    def flush_table():
        nonlocal table_buffer
        if not table_buffer:
            return
        rows = table_buffer
        table_buffer = []
        if len(rows) < 2:
            for row in rows:
                html_lines.append(f"<p>{inline_md(row)}</p>")
            return
        html_lines.append("<table>")
        for idx, row in enumerate(rows):
            if idx == 1 and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", row):
                continue
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            tag = "th" if idx == 0 else "td"
            html_lines.append("<tr>" + "".join(f"<{tag}>{inline_md(c)}</{tag}>" for c in cells) + "</tr>")
        html_lines.append("</table>")

    for line in lines:
        if line.startswith("```") or line.startswith("````"):
            flush_table()
            close_list()
            if not in_code:
                in_code = True
                code_lang = line.strip("`").strip()
                html_lines.append(f'<pre><code class="language-{html.escape(code_lang)}">')
            else:
                in_code = False
                html_lines.append("</code></pre>")
            continue

        if in_code:
            html_lines.append(html.escape(line))
            continue

        if line.startswith("|") and line.rstrip().endswith("|"):
            close_list()
            table_buffer.append(line)
            continue
        flush_table()

        stripped = line.strip()
        if not stripped:
            close_list()
            html_lines.append("")
            continue

        if stripped.startswith("# "):
            close_list()
            html_lines.append(f"<h1>{inline_md(stripped[2:].strip())}</h1>")
        elif stripped.startswith("## "):
            close_list()
            section_index += 1
            raw = stripped[3:].strip()
            html_lines.append(f'<h2 id="{slugify(section_index, raw)}">{inline_md(raw)}</h2>')
        elif stripped.startswith("### "):
            close_list()
            raw = stripped[4:].strip()
            html_lines.append(f"<h3>{inline_md(raw)}</h3>")
        elif stripped.startswith("> "):
            close_list()
            html_lines.append(f"<blockquote>{inline_md(stripped[2:].strip())}</blockquote>")
        elif re.match(r"^- ", stripped):
            if not list_open:
                html_lines.append("<ul>")
                list_open = True
            html_lines.append(f"<li>{inline_md(stripped[2:].strip())}</li>")
        elif re.match(r"^\d+\. ", stripped):
            close_list()
            html_lines.append(f"<p>{inline_md(stripped)}</p>")
        else:
            close_list()
            html_lines.append(f"<p>{inline_md(stripped)}</p>")

    flush_table()
    close_list()
    if in_code:
        html_lines.append("</code></pre>")
    return "\n".join(html_lines)


def page_template(title: str, body: str, toc: list[tuple[str, str]], lang: str) -> str:
    switch = (
        '<a class="lang active" href="zh-CN.html">中文</a><a class="lang" href="en-US.html">English</a>'
        if lang == "zh"
        else '<a class="lang" href="zh-CN.html">中文</a><a class="lang active" href="en-US.html">English</a>'
    )
    toc_html = "\n".join(f'<a href="#{sid}">{html.escape(label)}</a>' for sid, label in toc)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      color-scheme: light;
      --text: #1f2937;
      --muted: #64748b;
      --line: #e2e8f0;
      --link: #0969da;
      --side: #f8fafc;
      --accent: #111827;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", "Microsoft YaHei", sans-serif;
      color: var(--text);
      background: #fff;
      line-height: 1.7;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 300px minmax(0, 1fr);
      min-height: 100vh;
    }}
    aside {{
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
      padding: 28px 20px;
      background: var(--side);
      border-right: 1px solid var(--line);
    }}
    aside h2 {{
      margin: 0 0 14px;
      font-size: 22px;
      color: var(--accent);
    }}
    .lang-switch {{
      display: flex;
      gap: 8px;
      margin: 0 0 22px;
    }}
    .lang {{
      display: inline-flex;
      padding: 7px 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      color: var(--link);
      text-decoration: none;
      background: #fff;
      font-size: 14px;
    }}
    .lang.active {{
      color: #fff;
      background: var(--accent);
      border-color: var(--accent);
    }}
    nav a {{
      display: block;
      padding: 7px 8px;
      border-radius: 8px;
      color: var(--link);
      text-decoration: none;
      font-size: 14px;
    }}
    nav a:hover {{
      background: #eef2ff;
      text-decoration: underline;
    }}
    main {{
      width: min(980px, 100%);
      padding: 38px 44px 80px;
    }}
    h1 {{
      margin-top: 0;
      font-size: 34px;
      line-height: 1.25;
      color: var(--accent);
    }}
    h2 {{
      margin-top: 42px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
      font-size: 26px;
      color: var(--accent);
      scroll-margin-top: 20px;
    }}
    h3 {{ margin-top: 28px; font-size: 20px; }}
    a {{ color: var(--link); }}
    img {{
      max-width: 100%;
      border: 1px solid var(--line);
      border-radius: 10px;
      margin: 12px 0 18px;
    }}
    code {{
      padding: 0.1em 0.35em;
      border-radius: 5px;
      background: #f1f5f9;
      font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace;
    }}
    pre {{
      overflow: auto;
      padding: 16px;
      border-radius: 10px;
      background: #0f172a;
      color: #e2e8f0;
    }}
    pre code {{ padding: 0; background: transparent; color: inherit; }}
    blockquote {{
      margin: 16px 0;
      padding: 10px 16px;
      border-left: 4px solid #94a3b8;
      color: var(--muted);
      background: #f8fafc;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 18px 0;
      font-size: 14px;
    }}
    th, td {{
      border: 1px solid var(--line);
      padding: 10px;
      vertical-align: top;
    }}
    th {{ background: #f8fafc; }}
    @media (max-width: 900px) {{
      .layout {{ display: block; }}
      aside {{
        position: static;
        height: auto;
        max-height: 45vh;
        border-right: none;
        border-bottom: 1px solid var(--line);
      }}
      main {{ padding: 28px 18px 64px; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <aside>
      <h2>目录 / Outline</h2>
      <div class="lang-switch">{switch}</div>
      <nav>{toc_html}</nav>
    </aside>
    <main>{body}</main>
  </div>
</body>
</html>
"""


def build(md_name: str, html_name: str, lang: str):
    md = (DOCS / md_name).read_text(encoding="utf-8-sig")
    md = remove_inline_toc(md)
    md = md.replace("../assets/images/", "assets/images/")
    title, toc = extract_title_and_toc(md)
    body = render_markdown(md)
    (DOCS / html_name).write_text(page_template(title, body, toc, lang), encoding="utf-8")


def main():
    build("zh-CN.md", "zh-CN.html", "zh")
    build("en-US.md", "en-US.html", "en")
    (DOCS / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=zh-CN.html"><a href="zh-CN.html">中文</a> / <a href="en-US.html">English</a>',
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
