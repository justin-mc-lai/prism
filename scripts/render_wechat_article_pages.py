#!/usr/bin/env python3
"""Render a long-form WeChat image-post from Markdown via HTML pagination.

Pipeline:
  markdown → warm-paper HTML (+ SVG diagrams) → 1080×1440 Playwright screenshots

Block-aware snap avoids cutting paragraphs / diagrams mid-block.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from lib.kit_render import render_kit_body  # noqa: E402

TEMPLATE_DIR = ROOT / "templates/kushi-wechat-article-post"
CSS_PATH = TEMPLATE_DIR / "css/article.css"
DIAGRAM_DIR = TEMPLATE_DIR / "diagrams"
KIT_CSS = "css/kit.css"
KIT_JS = "js/kit.js"
KIT_VENDOR = ("vendor/anime.min.js", "vendor/rough-notation.iife.js")

PAGE_W = 1080
PAGE_H = 1440
FOOTER_H = 56


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def inline_format(text: str) -> str:
    """Escape then lightly mark slash-commands and bare URLs."""
    escaped = html.escape(text)
    # Only treat slash-commands after whitespace / CJK punctuation, never mid-path.
    escaped = re.sub(
        r"(?<=[\s，。；：、（）【】“”\"'（])/(?!/)([a-z][a-z0-9-]*)",
        r"<code>/\1</code>",
        escaped,
    )
    escaped = re.sub(
        r"(^)/(?!/)([a-z][a-z0-9-]*)",
        r"<code>/\2</code>",
        escaped,
    )
    escaped = re.sub(
        r"(https?://[^\s<]+)",
        r'<a href="\1">\1</a>',
        escaped,
    )
    escaped = re.sub(
        r"(?<![<>/])\b(codex plugin (?:marketplace add|add) [a-zA-Z0-9_@./-]+)",
        r"<code>\1</code>",
        escaped,
    )
    escaped = re.sub(
        r"(?<=[\s，。；：、（])(\./[a-z0-9._-]+)",
        r"<code>\1</code>",
        escaped,
    )
    escaped = re.sub(
        r"(?<=[\s，。；：、（])(mkdir)\b",
        r"<code>\1</code>",
        escaped,
    )
    return escaped


def parse_blocks(md_body: str) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    lines = md_body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        fence = re.match(r"^(`{3,}|~{3,})(.*)$", line)
        if fence:
            marker = fence.group(1)
            lang = fence.group(2).strip()
            code_lines: list[str] = []
            i += 1
            while i < len(lines):
                closing = lines[i].strip()
                if closing.startswith(marker):
                    i += 1
                    break
                code_lines.append(lines[i].rstrip("\n"))
                i += 1
            blocks.append({"type": "code", "lang": lang, "text": "\n".join(code_lines)})
            continue
        if line.startswith(":::"):
            directive = line[3:].strip()
            comp_type = directive.split(maxsplit=1)[0] if directive else ""
            comp_rest = directive[len(comp_type) :].strip() if comp_type else ""
            if comp_type in ("callout", "stat", "compare"):
                body_lines: list[str] = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith(":::"):
                    body_lines.append(lines[i].rstrip("\n"))
                    i += 1
                if i < len(lines):
                    i += 1  # skip closing :::
                blocks.append(parse_component_block(comp_type, comp_rest, body_lines))
                continue
        if line.startswith("# "):
            blocks.append({"type": "h1", "text": line[2:].strip()})
            i += 1
            continue
        if line.startswith("## "):
            blocks.append({"type": "h2", "text": line[3:].strip()})
            i += 1
            continue
        para_lines = [line]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and not lines[i].startswith("#")
            and not lines[i].lstrip().startswith(("```", "~~~"))
            and not lines[i].lstrip().startswith(":::")
        ):
            para_lines.append(lines[i].rstrip())
            i += 1
        joined = ""
        for idx, part in enumerate(para_lines):
            if idx == 0:
                joined = part
            elif part[:1].isascii() and joined[-1:].isascii():
                joined += " " + part
            else:
                joined += part
        blocks.append({"type": "p", "text": joined})
    return blocks


def _split_table_row(line: str) -> list[str]:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return [c for c in cells if c != ""] or [""]


def _is_separator_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{2,}:?", c) for c in cells)


def parse_component_block(
    comp_type: str,
    rest: str,
    lines: list[str],
) -> dict[str, Any]:
    """Parse :::callout / :::stat / :::compare / :::kit component blocks."""
    if comp_type == "callout":
        kinds = {"note", "warning", "danger", "ok", "tip"}
        first = rest.split(maxsplit=1)[0] if rest else "note"
        kind = first if first in kinds else "note"
        title = rest[len(first) :].strip() if first in kinds else rest.strip()
        if not title:
            title = {"note": "注意", "warning": "留意", "danger": "别踩坑", "ok": "核对结果", "tip": "建议"}.get(kind, "注意")
        body = "".join(ln for ln in lines if ln.strip()) or ""
        return {"type": "callout", "kind": kind, "title": title, "text": body}
    if comp_type == "stat":
        nonempty = [ln.strip() for ln in lines if ln.strip()]
        if rest.strip():
            number = rest.strip()
            body = nonempty
        else:
            number = nonempty[0] if nonempty else ""
            body = nonempty[1:] if nonempty else []
        label = body[0] if body else ""
        note = "".join(body[1:]) if len(body) > 1 else ""
        return {"type": "stat", "number": number, "label": label, "note": note}
    if comp_type == "compare":
        header: list[str] = []
        rows: list[list[str]] = []
        for ln in lines:
            if not ln.strip() or not ln.strip().startswith("|"):
                continue
            cells = _split_table_row(ln)
            if _is_separator_row(cells):
                continue
            if not header:
                header = cells
            else:
                rows.append(cells)
        if not header:
            header = ["项目", "说明"]
        return {"type": "compare", "header": header, "rows": rows}
    if comp_type == "kit":
        fields: dict[str, Any] = {"theme": rest.strip() or "white"}
        list_keys = {"chips", "steps", "checklist"}
        pair_keys = {"timeline", "quote", "callout", "endcard"}
        for ln in lines:
            line = ln.strip()
            if not line or ":" not in line:
                continue
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if not key:
                continue
            if key in list_keys:
                fields[key] = [v.strip() for v in value.split("|") if v.strip()]
            elif key == "timeline":
                items = []
                for chunk in value.split("|"):
                    chunk = chunk.strip()
                    if not chunk:
                        continue
                    t, _, text = chunk.partition(" ")
                    items.append({"time": t.strip(), "text": text.strip()})
                fields[key] = items
            elif key == "quote":
                text, _, source = value.partition("|")
                fields[key] = {"text": text.strip(), "source": source.strip()}
            elif key == "callout":
                title, _, body = value.partition("|")
                fields[key] = {"title": title.strip(), "text": body.strip()}
            elif key == "endcard":
                title, _, cta = value.partition("|")
                fields[key] = {"title": title.strip(), "cta": cta.strip()}
            else:
                fields[key] = value
        return {"type": "kit", "kit": fields}
    return {"type": "p", "text": rest}


def load_diagram_injections(config_path: Path | None) -> list[dict[str, Any]]:
    """Load optional diagram injection rules. Empty = no diagrams (generic articles)."""
    if not config_path:
        return []
    if not config_path.exists():
        raise FileNotFoundError(f"diagrams config missing: {config_path}")
    data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    rules = data.get("injections") or []
    if not isinstance(rules, list):
        raise ValueError(f"diagrams.yaml injections must be a list: {config_path}")
    return rules


def inject_diagrams(
    blocks: list[dict[str, Any]],
    rules: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Insert diagram markers from explicit rules. No rules ⇒ passthrough (no hardcoded topic diagrams)."""
    if not rules:
        return blocks
    out: list[dict[str, Any]] = []
    used: set[int] = set()
    for block in blocks:
        out.append(block)
        if block["type"] != "p":
            continue
        text = block["text"]
        for idx, rule in enumerate(rules):
            if idx in used:
                continue
            match_all = rule.get("match_all") or []
            match_any = rule.get("match_any") or []
            ok_all = all(token in text for token in match_all) if match_all else True
            ok_any = any(token in text for token in match_any) if match_any else True
            if match_all or match_any:
                if not (ok_all and ok_any):
                    continue
            else:
                continue
            diagram_file = str(rule.get("file") or "").strip()
            if not diagram_file:
                continue
            out.append(
                {
                    "type": "diagram",
                    "id": str(rule.get("id") or Path(diagram_file).stem),
                    "title": str(rule.get("title") or Path(diagram_file).stem),
                    "file": diagram_file,
                }
            )
            used.add(idx)
    # Optional append_unmatched: put unused diagrams at end (before source line if present)
    append_unused = any(bool(r.get("append_if_unmatched")) for r in rules)
    if append_unused:
        insert_at = len(out)
        for i in range(len(out) - 1, -1, -1):
            if out[i]["type"] == "p" and (
                out[i]["text"].startswith("仓库 http") or out[i]["text"].startswith("https://")
            ):
                insert_at = i
                break
        for idx, rule in enumerate(rules):
            if idx in used or not rule.get("append_if_unmatched"):
                continue
            diagram_file = str(rule.get("file") or "").strip()
            if not diagram_file:
                continue
            out.insert(
                insert_at,
                {
                    "type": "diagram",
                    "id": str(rule.get("id") or Path(diagram_file).stem),
                    "title": str(rule.get("title") or Path(diagram_file).stem),
                    "file": diagram_file,
                },
            )
            insert_at += 1
            used.add(idx)
    return out


def resolve_diagram_file(filename: str, diagrams_dirs: list[Path]) -> Path:
    name = Path(filename).name
    for base in diagrams_dirs:
        candidate = base / name
        if candidate.exists():
            return candidate
        # allow nested relative paths under a diagrams dir
        nested = base / filename
        if nested.exists():
            return nested
    raise FileNotFoundError(f"diagram not found: {filename} (searched {[str(d) for d in diagrams_dirs]})")


def render_article_html(
    blocks: list[dict[str, Any]],
    *,
    title: str,
    source_label: str,
    css_text: str,
    diagrams_dirs: list[Path] | None = None,
) -> str:
    dirs = diagrams_dirs or [DIAGRAM_DIR]
    parts: list[str] = []
    first_p = True
    for block in blocks:
        kind = block["type"]
        if kind == "h1":
            parts.append(f"<h1>{html.escape(block['text'])}</h1>")
            first_p = True
        elif kind == "h2":
            parts.append(
                f'<h2 style="font-size:34px;margin:28px 0 16px;font-family:PingFang SC,sans-serif">'
                f"{html.escape(block['text'])}</h2>"
            )
        elif kind == "callout":
            parts.append(
                f'<figure class="callout callout-{html.escape(block["kind"])}" data-block="1">'
                f'<div class="callout-title">{html.escape(block["title"])}</div>'
                f"<p>{inline_format(block['text'])}</p></figure>"
            )
        elif kind == "stat":
            parts.append(
                f'<figure class="stat-block" data-block="1">'
                f'<div class="stat-number">{html.escape(block["number"])}</div>'
                f'<div class="stat-label">{html.escape(block["label"])}</div>'
                f"<p class=\"stat-note\">{inline_format(block['note'])}</p></figure>"
            )
        elif kind == "compare":
            header_html = "".join(
                f"<th>{inline_format(c)}</th>" for c in block["header"]
            )
            rows_html = "".join(
                "<tr>" + "".join(f"<td>{inline_format(c)}</td>" for c in row) + "</tr>"
                for row in block["rows"]
            )
            parts.append(
                f'<figure class="compare-block" data-block="1"><table>'
                f"<thead><tr>{header_html}</tr></thead>"
                f"<tbody>{rows_html}</tbody></table></figure>"
            )
        elif kind == "code":
            code = html.escape(block["text"])
            lang = html.escape(block.get("lang", ""))
            if lang:
                parts.append(
                    f'<figure class="code-block" data-block="1">'
                    f'<div class="code-label">{lang}</div>'
                    f"<pre><code>{code}</code></pre></figure>"
                )
            else:
                parts.append(
                    f'<figure class="code-block" data-block="1">'
                    f"<pre><code>{code}</code></pre></figure>"
                )
        elif kind == "kit":
            kit_body = render_kit_body(block.get("kit") or {})
            if kit_body:
                parts.append(f'<div class="kit-article-block" data-block="1">{kit_body}</div>')
        elif kind == "diagram":
            svg_path = resolve_diagram_file(block["file"], dirs)
            svg = svg_path.read_text(encoding="utf-8")
            # strip xml declaration if any
            svg = re.sub(r"<\?xml[^>]*\?>", "", svg).strip()
            parts.append(
                f'<figure class="diagram" data-block="1">'
                f'<div class="diagram-title">{html.escape(block["title"])}</div>'
                f"{svg}</figure>"
            )
        elif kind == "p":
            cls = "lead" if first_p else ""
            if block["text"].startswith("仓库 http") or block["text"].startswith("https://"):
                parts.append(f'<p class="source-line" data-block="1">{inline_format(block["text"])}</p>')
            else:
                parts.append(f'<p class="{cls}" data-block="1">{inline_format(block["text"])}</p>')
            first_p = False

    body = "\n".join(parts)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width={PAGE_W}"/>
<title>{html.escape(title)}</title>
<style>{css_text}</style>
</head>
<body>
<article class="article" id="article">
  <div class="article-meta">
    <span>库拾 · 开源核对</span>
    <span>{html.escape(source_label)}</span>
  </div>
  {body}
</article>
</body>
</html>
"""


SNAP_JS = """
() => {
  const pageH = %d;
  const footerH = %d;
  const usable = pageH - footerH;
  const article = document.getElementById('article');
  const blocks = Array.from(document.querySelectorAll('[data-block], h1, .article-meta'));
  const docBottom = Math.max(
    document.documentElement.scrollHeight,
    document.body.scrollHeight,
    article.offsetTop + article.offsetHeight
  );
  // 只按真实内容块计算分页边界，避免 article 底部 padding 产生空尾页。
  const blockBottoms = blocks.map((el) =>
    el.getBoundingClientRect().top + window.scrollY + el.getBoundingClientRect().height
  );
  const contentEnd = Math.max(docBottom - 120, ...blockBottoms);

  // Block-aware page starts. Slices are cropped from a full-page screenshot
  // (scrollY viewport shots clamp near the bottom and overlap).
  const starts = [0];
  let cursor = 0;
  while (cursor + usable < contentEnd - 2) {
    const idealEnd = cursor + usable;
    let next = idealEnd;
    for (const el of blocks) {
      const top = el.getBoundingClientRect().top + window.scrollY;
      const bottom = top + el.getBoundingClientRect().height;
      if (top < idealEnd && bottom > idealEnd + 8) {
        next = Math.max(cursor + 80, top - 8);
        break;
      }
      if (top >= idealEnd - 4 && top < idealEnd + usable * 0.35) {
        next = top - 8;
        break;
      }
    }
    if (next <= cursor) next = cursor + usable;
    // Stop if remaining content fits on this page
    if (next >= contentEnd - 24) break;
    starts.push(Math.floor(next));
    cursor = Math.floor(next);
    if (starts.length > 40) break;
  }
  return { starts, docBottom, usable, pageH };
}
""" % (PAGE_H, FOOTER_H)


def screenshot_pages(
    html_path: Path,
    out_dir: Path,
    *,
    source_label: str,
    start_index: int = 1,
    wait_motion: bool = False,
) -> list[Path]:
    from playwright.sync_api import sync_playwright
    from PIL import Image, ImageDraw, ImageFont

    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []

    font_path = "/System/Library/Fonts/Menlo.ttc"
    try:
        font = ImageFont.truetype(font_path, 22)
        font_sm = ImageFont.truetype(font_path, 20)
    except OSError:
        font = ImageFont.load_default()
        font_sm = font

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": PAGE_W, "height": PAGE_H},
            device_scale_factor=1,
        )
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        if wait_motion:
            has_flag = page.evaluate("typeof window.__kitMotionDone !== 'undefined'")
            if has_flag:
                page.wait_for_function("window.__kitMotionDone === true", timeout=6000)
            else:
                page.wait_for_timeout(120)
        else:
            page.wait_for_timeout(120)
        meta = page.evaluate(SNAP_JS)
        starts: list[int] = [int(y) for y in meta["starts"]]
        doc_bottom = int(meta["docBottom"])
        usable = int(meta["usable"])

        # One full-document shot, then crop non-overlapping slices.
        # Avoids scrollY clamp near the end (which duplicated the last paragraphs).
        tmp_full = out_dir / "_tmp_full.png"
        page.screenshot(path=str(tmp_full), type="png", full_page=True)
        full = Image.open(tmp_full).convert("RGB")
        # Guard: Playwright full_page width should match viewport
        if full.size[0] != PAGE_W:
            full = full.resize(
                (PAGE_W, int(full.size[1] * PAGE_W / full.size[0])),
                Image.Resampling.LANCZOS,
            )
        full_h = full.size[1]
        content_bottom = min(doc_bottom, full_h)

        # Drop trailing starts that leave almost no unique content
        while len(starts) > 1 and starts[-1] >= content_bottom - 48:
            starts.pop()

        total_pages = len(starts)
        paper = (249, 248, 244)
        for i, y in enumerate(starts):
            end = starts[i + 1] if i + 1 < len(starts) else content_bottom
            slice_h = max(1, min(end, content_bottom) - y)
            # Never take more than usable into the content area
            slice_h = min(slice_h, usable)
            crop = full.crop((0, y, PAGE_W, y + slice_h))
            canvas = Image.new("RGB", (PAGE_W, PAGE_H), paper)
            canvas.paste(crop, (0, 0))
            draw = ImageDraw.Draw(canvas)
            draw.rectangle((0, PAGE_H - FOOTER_H, PAGE_W, PAGE_H), fill=paper)
            draw.line(
                (72, PAGE_H - FOOTER_H, PAGE_W - 72, PAGE_H - FOOTER_H),
                fill=(210, 210, 205),
                width=1,
            )
            seq = start_index + i
            draw.text((72, PAGE_H - 40), source_label, font=font_sm, fill=(92, 92, 92))
            draw.text(
                (PAGE_W - 120, PAGE_H - 42),
                f"{i + 1}/{total_pages}",
                font=font,
                fill=(92, 92, 92),
            )
            out = out_dir / f"{seq:02d}-article.png"
            canvas.save(out, "PNG", optimize=True)
            paths.append(out)
        tmp_full.unlink(missing_ok=True)
        browser.close()
    return paths


def make_contact_sheet(paths: list[Path], out: Path) -> None:
    from PIL import Image

    thumbs = []
    for path in paths:
        with Image.open(path) as im:
            thumbs.append(im.convert("RGB").resize((180, 240), Image.Resampling.LANCZOS))
    cols = min(3, max(1, len(thumbs)))
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (180 * cols + 24 * (cols + 1), 240 * rows + 24 * (rows + 1)), (255, 255, 255))
    for i, thumb in enumerate(thumbs):
        x = 24 + (i % cols) * (180 + 24)
        y = 24 + (i // cols) * (240 + 24)
        sheet.paste(thumb, (x, y))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, "PNG", optimize=True)


def build_kit_assets(kit_dir: Path, html_dir: Path) -> tuple[str, str]:
    """Return (extra_css, script_tags) for wechat-card-kit.

    Vendor/kit JS are copied into <html_dir>/_kit/ so file:// rendering works
    offline regardless of symlinked output dirs.
    """
    css_path = kit_dir / KIT_CSS
    if not css_path.exists():
        raise FileNotFoundError(f"kit css missing: {css_path}")
    extra_css = css_path.read_text(encoding="utf-8")

    target = html_dir / "_kit"
    target.mkdir(parents=True, exist_ok=True)
    files = [kit_dir / KIT_JS] + [kit_dir / v for v in KIT_VENDOR]
    tags = []
    for f in files:
        if not f.exists():
            raise FileNotFoundError(f"kit asset missing: {f}")
        dst = target / f.name
        shutil.copy2(f, dst)
        tags.append(f'<script src="_kit/{html.escape(f.name, quote=True)}"></script>')
    return extra_css, "\n".join(tags)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--html-out", default="")
    parser.add_argument("--title", default="")
    parser.add_argument("--source-label", default="")
    parser.add_argument("--start-index", type=int, default=2, help="First article page number (1=cover reserved)")
    parser.add_argument("--manifest", default="")
    parser.add_argument("--contact-sheet", default="")
    parser.add_argument(
        "--diagrams",
        default="",
        help="Optional diagrams.yaml (match rules). Omit for text-only pagination.",
    )
    parser.add_argument(
        "--diagrams-dir",
        action="append",
        default=[],
        help="Extra SVG search dirs (repeatable). Template diagrams/ always searched last.",
    )
    parser.add_argument("--total-with-cover", action="store_true",
                        help="Rewrite footers as n/N including cover after render")
    parser.add_argument("--kit", default="",
                        help="Path to templates/wechat-card-kit: inject kit css/js and wait for motion end state")
    args = parser.parse_args()

    md_path = Path(args.markdown)
    if not md_path.is_absolute():
        md_path = ROOT / md_path
    raw = md_path.read_text(encoding="utf-8")
    body = strip_frontmatter(raw)

    diagrams_cfg = Path(args.diagrams) if args.diagrams else None
    if diagrams_cfg and not diagrams_cfg.is_absolute():
        diagrams_cfg = ROOT / diagrams_cfg
    rules = load_diagram_injections(diagrams_cfg)
    blocks = inject_diagrams(parse_blocks(body), rules)

    title = args.title
    if not title:
        for b in blocks:
            if b["type"] == "h1":
                title = b["text"]
                break
        title = title or md_path.stem

    source_label = args.source_label.strip()
    if not source_label:
        # Derive from first repo URL line when present
        for b in blocks:
            if b["type"] == "p" and "github.com/" in b["text"]:
                m = re.search(r"github\.com/[^\s]+", b["text"])
                if m:
                    source_label = m.group(0).rstrip("/")
                    break
        source_label = source_label or "github.com"

    diagrams_dirs: list[Path] = []
    for d in args.diagrams_dir:
        p = Path(d)
        if not p.is_absolute():
            p = ROOT / p
        diagrams_dirs.append(p)
    if diagrams_cfg:
        diagrams_dirs.append(diagrams_cfg.parent / "diagrams")
        diagrams_dirs.append(diagrams_cfg.parent)
    diagrams_dirs.append(DIAGRAM_DIR)

    css = CSS_PATH.read_text(encoding="utf-8")

    out_dir = Path(args.output_dir)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    html_out = Path(args.html_out) if args.html_out else out_dir / "article.html"
    if not html_out.is_absolute():
        html_out = ROOT / html_out
    html_out.parent.mkdir(parents=True, exist_ok=True)

    kit_scripts = ""
    wait_motion = False
    uses_kit = ":::kit" in body
    kit_dir: Path | None = None
    if args.kit:
        kit_dir = Path(args.kit)
    elif uses_kit:
        kit_dir = ROOT / "templates/wechat-card-kit"
    if kit_dir is not None:
        if not kit_dir.is_absolute():
            kit_dir = ROOT / kit_dir
        kit_css, kit_scripts = build_kit_assets(kit_dir, html_out.parent)
        css = css + "\n" + kit_css
        wait_motion = True
    html_doc = render_article_html(
        blocks,
        title=title,
        source_label=source_label,
        css_text=css,
        diagrams_dirs=diagrams_dirs,
    )
    if kit_scripts:
        html_doc = html_doc.replace("</body>", kit_scripts + "\n</body>")
    html_out.write_text(html_doc, encoding="utf-8")

    paths = screenshot_pages(
        html_out,
        out_dir,
        source_label=source_label,
        start_index=args.start_index,
        wait_motion=wait_motion,
    )

    if args.total_with_cover:
        from PIL import Image, ImageDraw, ImageFont

        total = len(paths) + 1  # cover
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 22)
            font_sm = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 20)
        except OSError:
            font = ImageFont.load_default()
            font_sm = font
        for idx, path in enumerate(paths):
            im = Image.open(path).convert("RGB")
            draw = ImageDraw.Draw(im)
            draw.rectangle((0, PAGE_H - FOOTER_H, PAGE_W, PAGE_H), fill=(249, 248, 244))
            draw.line((72, PAGE_H - FOOTER_H, PAGE_W - 72, PAGE_H - FOOTER_H), fill=(210, 210, 205), width=1)
            page_no = args.start_index + idx
            draw.text((72, PAGE_H - 40), source_label, font=font_sm, fill=(92, 92, 92))
            draw.text((PAGE_W - 140, PAGE_H - 42), f"{page_no}/{total}", font=font, fill=(92, 92, 92))
            im.save(path, "PNG", optimize=True)

    if args.manifest:
        manifest_path = Path(args.manifest)
        if not manifest_path.is_absolute():
            manifest_path = ROOT / manifest_path
        manifest = {
            "schema_version": "1",
            "visual_profile": "kushi-article-paper-portrait",
            "renderer": "scripts/render_wechat_article_pages.py",
            "template": "templates/kushi-wechat-article-post",
            "source_markdown": str(md_path.relative_to(ROOT)),
            "html": str(html_out.relative_to(ROOT)),
            "dimensions": {"width": PAGE_W, "height": PAGE_H},
            "article_pages": [
                {"seq": args.start_index + i, "path": str(p.relative_to(ROOT))}
                for i, p in enumerate(paths)
            ],
        }
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(
            yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    if args.contact_sheet:
        contact = Path(args.contact_sheet)
        if not contact.is_absolute():
            contact = ROOT / contact
        make_contact_sheet(paths, contact)

    for p in paths:
        print(p.relative_to(ROOT) if p.is_relative_to(ROOT) else p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
