#!/usr/bin/env python3
"""Render 库拾 WeChat image-post cards from HTML templates via Playwright.

Design contract: templates/kushi-wechat-image-post/css/card.css
Data contract: cards.yaml (same shape as render_wechat_image_cards.py)

Text is HTML/CSS local layout — never AI text-in-image.
Optional HyperFrames project can wrap the same HTML later for motion.
"""

from __future__ import annotations

import argparse
import html
import io
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from lib.kit_render import kit_theme_class, render_kit_body  # noqa: E402

TEMPLATE_CSS = ROOT / "templates/kushi-wechat-image-post/css/card.css"
KIT_CSS = "css/kit.css"
KIT_JS = "js/kit.js"
KIT_VENDOR = ("vendor/anime.min.js", "vendor/rough-notation.iife.js")


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def rel_to_root(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def soft_class(color: str) -> str:
    return {
        "blue": "soft-blue",
        "green": "soft-green",
        "orange": "soft-orange",
        "red": "soft-red",
    }.get(color, "soft-blue")


def render_sections(sections: list[dict[str, Any]]) -> str:
    parts: list[str] = []
    for section in sections or []:
        color = str(section.get("color") or "blue")
        bullets = "".join(
            f"<li>{esc(item)}</li>" for item in (section.get("bullets") or [])[:4]
        )
        parts.append(
            f"""
            <section class="panel {soft_class(color)}">
              <div class="panel-head">
                <span class="dot {esc(color)}"></span>
                <h3 class="panel-title">{esc(section.get("title"))}</h3>
              </div>
              <ul class="bullets {esc(color)}">{bullets}</ul>
            </section>
            """
        )
    return "\n".join(parts)


def render_hero(card: dict[str, Any]) -> str:
    hero = card.get("hero") or {}
    if str(hero.get("kind") or "") != "counts":
        return ""
    label = str(hero.get("label") or "")
    stats_html = []
    for stat in (hero.get("stats") or [])[:3]:
        color = str(stat.get("color") or "blue")
        stats_html.append(
            f"""
            <div class="stat {esc(color)}">
              <div class="num">{esc(stat.get("number"))}</div>
              <div class="label">{esc(stat.get("label"))}</div>
            </div>
            """
        )
    return f"""
      <div>
        {"<div class='hero-label'>" + esc(label) + "</div>" if label else ""}
        <div class="stats">{"".join(stats_html)}</div>
      </div>
    """


def render_compare(card: dict[str, Any]) -> str:
    compare = card.get("compare") or {}
    cols = []
    for key, default in (("left", "blue"), ("right", "green")):
        panel = compare.get(key) or {}
        color = str(panel.get("color") or default)
        bullets = "".join(
            f"<li>{esc(item)}</li>" for item in (panel.get("bullets") or [])[:4]
        )
        cols.append(
            f"""
            <div class="col {esc(color)}">
              <div class="col-title">{esc(panel.get("title"))}</div>
              <ul class="bullets {esc(color)} ink">{bullets}</ul>
            </div>
            """
        )
    return f'<div class="compare">{"".join(cols)}</div>'


def render_flow(items: list[Any], color: str = "green") -> str:
    color = color or "green"
    chunks: list[str] = []
    for i, item in enumerate(items or []):
        if i:
            chunks.append(f'<div class="flow-arrow" style="background:{_css_color(color)}"></div>')
        chunks.append(
            f'<div class="flow-step" style="border-color:{_css_color(color)}">{esc(item)}</div>'
        )
    return f'<div class="flow">{"".join(chunks)}</div>'


def _css_color(name: str) -> str:
    return {
        "blue": "#2563eb",
        "green": "#059669",
        "orange": "#ea7a00",
        "red": "#dc2626",
    }.get(name, "#2563eb")


def render_commands(card: dict[str, Any]) -> str:
    commands = card.get("commands") or []
    if isinstance(commands, str):
        commands = [commands]
    parts = [f'<div class="cmd">{esc(cmd)}</div>' for cmd in commands[:3]]
    for note in (card.get("notes") or [])[:3]:
        parts.append(
            f"""
            <div class="note">
              <span class="bang">!</span>
              <p>{esc(note)}</p>
            </div>
            """
        )
    return "\n".join(parts)


def render_quote(card: dict[str, Any]) -> str:
    quote = card.get("quote") or {}
    text = str(quote.get("text") or "")
    source = str(quote.get("source") or "")
    translation = str(quote.get("translation") or "")
    if not text:
        return ""
    parts = [
        '<div class="quote">'
        f'<div class="quote-text">{esc(text)}</div>',
    ]
    if translation:
        parts.append(f'<div class="quote-trans">{esc(translation)}</div>')
    parts.append(f'<div class="quote-src">{esc(source)}</div></div>')
    return "".join(parts)


def render_body(card: dict[str, Any]) -> str:
    layout = str(card.get("layout") or "")
    color = str(card.get("color") or "blue")
    chunks: list[str] = []

    if layout == "cover":
        chunks.append(render_hero(card))
    elif layout == "compare":
        chunks.append(render_compare(card))
    elif layout == "command":
        chunks.append(render_commands(card))

    if card.get("callout") and layout not in ("compare", "command"):
        callout_color = color if color in ("blue", "orange") else "blue"
        chunks.append(
            f'<div class="callout {esc(callout_color)}">{esc(card.get("callout"))}</div>'
        )

    if card.get("flow") and layout not in ("compare", "command"):
        chunks.append(render_flow(card.get("flow") or [], color))

    if card.get("sections"):
        chunks.append(render_sections(card.get("sections") or []))

    chunks.append(render_quote(card))

    takeaway = str(card.get("takeaway") or "")
    if takeaway:
        chunks.append(f'<div class="takeaway">{esc(takeaway)}</div>')

    return "\n".join(chunks)


def render_card_html(
    card: dict[str, Any],
    *,
    source: str,
    total: int,
    css_text: str,
    channel: str = "微信贴图",
    kit_scripts: str = "",
) -> str:
    color = str(card.get("color") or "blue")
    seq = int(card.get("seq") or 1)
    background = str(card.get("background") or "").strip()
    card_style = ""
    if background:
        card_style = (
            ' style="background-image:url(&quot;%s&quot;);'
            'background-size:cover;background-position:center;"' % html.escape(background, quote=True)
        )
    if card.get("kit"):
        kit = card["kit"]
        body = render_kit_body(kit)
        theme = kit_theme_class(kit)
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=1080, height=1440" />
<title>{esc(card.get("title"))}</title>
<style>{css_text}</style>
</head>
<body>
  <article class="kit-card {theme}"{card_style}>
    {body}
    <footer class="kit-footer">
      <span>{esc(source)}</span>
      <span>{seq:02d}/{total}</span>
    </footer>
  </article>
{kit_scripts}
</body>
</html>
"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=1080, height=1440" />
<title>{esc(card.get("title"))}</title>
<style>{css_text}</style>
</head>
<body>
  <article class="card"{card_style}>
    <header class="header">
      <span class="chip {esc(color)}">{esc(card.get("kicker") or "开源项目")}</span>
      <span class="channel">{esc(channel)}</span>
    </header>
    <h1 class="title">{esc(card.get("title"))}</h1>
    {"<p class='subtitle'>" + esc(card.get("subtitle")) + "</p>" if card.get("subtitle") else ""}
    <div class="body">
      {render_body(card)}
    </div>
    <footer class="footer">
      <span class="source">{esc(source)}</span>
      <span class="pager">{seq}/{total}</span>
    </footer>
  </article>
{kit_scripts}
</body>
</html>
"""


def screenshot_htmls(
    html_paths: list[Path],
    out_paths: list[Path],
    size: tuple[int, int],
    *,
    wait_motion: bool = False,
) -> None:
    from playwright.sync_api import sync_playwright

    width, height = size
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
        )
        for html_path, out_path in zip(html_paths, out_paths):
            page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            if wait_motion:
                has_flag = page.evaluate(
                    "typeof window.__kitMotionDone !== 'undefined'"
                )
                if has_flag:
                    page.wait_for_function(
                        "window.__kitMotionDone === true", timeout=6000
                    )
                else:
                    page.wait_for_timeout(80)
            else:
                page.wait_for_timeout(80)
            page.screenshot(path=str(out_path), type="png", full_page=False)
        browser.close()


def export_animation(
    html_path: Path,
    out_path: Path,
    *,
    export: str,
    fps: int,
    gif_scale: float,
    size: tuple[int, int],
    wait_motion: bool,
) -> Path:
    """Capture frames during kit animations and encode GIF (PIL) or MP4 (ffmpeg)."""
    from playwright.sync_api import sync_playwright
    from PIL import Image

    width, height = size
    interval = 1.0 / max(1, fps)
    max_seconds = 4.0 if wait_motion else 1.0
    raw_frames: list[bytes] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
        )
        page.goto(html_path.resolve().as_uri(), wait_until="domcontentloaded")
        # kit.js 在 DOMContentLoaded 前已执行；直接开录，避免错过开场帧
        page.wait_for_timeout(30)
        start = time.monotonic()
        last_shot = -1.0
        done_at: float | None = None
        while True:
            elapsed = time.monotonic() - start
            if elapsed > max_seconds + 0.6:
                break
            if elapsed - last_shot >= interval - 1e-6:
                raw_frames.append(page.screenshot(type="png"))
                last_shot = elapsed
                if wait_motion and done_at is None:
                    flag = page.evaluate(
                        "typeof window.__kitMotionDone !== 'undefined' && window.__kitMotionDone === true"
                    )
                    if flag:
                        done_at = elapsed
                if done_at is not None and elapsed - done_at >= 0.35 and len(raw_frames) >= 6:
                    break
            time.sleep(0.03)
        browser.close()

    if not raw_frames:
        raise RuntimeError(f"no frames captured for {html_path.name}")
    images = [Image.open(io.BytesIO(b)).convert("RGB") for b in raw_frames]

    if export == "gif":
        if gif_scale != 1.0:
            w = max(1, int(images[0].width * gif_scale))
            h = max(1, int(images[0].height * gif_scale))
            images = [im.resize((w, h), Image.Resampling.LANCZOS) for im in images]
        images[0].save(
            out_path,
            save_all=True,
            append_images=images[1:],
            duration=max(40, int(1000 / fps)),
            loop=0,
            optimize=True,
        )
        return out_path

    if export == "mp4":
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            raise RuntimeError("mp4 export requires ffmpeg on PATH")
        tmp = Path(tempfile.mkdtemp(prefix="kit-frames-"))
        try:
            for i, im in enumerate(images):
                im.save(tmp / f"f{i:04d}.png")
            subprocess.run(
                [
                    ffmpeg,
                    "-y",
                    "-framerate",
                    str(fps),
                    "-i",
                    str(tmp / "f%04d.png"),
                    "-c:v",
                    "libx264",
                    "-pix_fmt",
                    "yuv420p",
                    "-movflags",
                    "+faststart",
                    str(out_path),
                ],
                check=True,
                capture_output=True,
            )
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        return out_path

    raise ValueError(f"unknown export: {export}")


def make_contact_sheet(paths: list[Path], out: Path) -> None:
    from PIL import Image

    thumbs: list[Any] = []
    for path in paths:
        with Image.open(path) as im:
            thumbs.append(im.convert("RGB").resize((216, 288), Image.Resampling.LANCZOS))
    sheet = Image.new("RGB", (216 * 3 + 32 * 4, 288 * 2 + 32 * 3), (255, 255, 255))
    for i, thumb in enumerate(thumbs):
        x = 32 + (i % 3) * (216 + 32)
        y = 32 + (i // 3) * (288 + 32)
        sheet.paste(thumb, (x, y))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, "PNG", optimize=True)


def build_kit_assets(kit_dir: Path, html_dir: Path) -> tuple[str, str]:
    """Return (extra_css, script_tags) for wechat-card-kit.

    CSS is inlined (single-file HTML); vendor/kit JS are copied into
    <html_dir>/_kit/ and referenced by relative path so file:// rendering
    keeps working offline regardless of symlinked output dirs.
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
    parser.add_argument("--cards", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--html-dir", default="")
    parser.add_argument("--manifest", default="")
    parser.add_argument("--contact-sheet", default="")
    parser.add_argument("--template-css", default="",
                        help="Path to card.css (default: templates/kushi-wechat-image-post/css/card.css)")
    parser.add_argument("--kit", default="",
                        help="Path to templates/wechat-card-kit: inject kit css/js and wait for motion end state")
    parser.add_argument("--export", choices=("none", "gif", "mp4"), default="none",
                        help="Export animated output per card (gif via PIL / mp4 via ffmpeg)")
    parser.add_argument("--fps", type=int, default=10, help="Animation capture fps (default 10)")
    parser.add_argument("--gif-scale", type=float, default=0.5,
                        help="GIF downscale factor (default 0.5 -> 540x720; WeChat size friendly)")
    parser.add_argument("--skip-cover-roles", default="cover_card",
                        help="Comma-separated roles to skip (e.g. cover when using punk cover)")
    args = parser.parse_args()

    cards_path = Path(args.cards)
    if not cards_path.is_absolute():
        cards_path = ROOT / cards_path
    data = yaml.safe_load(cards_path.read_text(encoding="utf-8")) or {}
    meta = data.get("metadata") or {}
    dimensions = meta.get("dimensions") or {"width": 1080, "height": 1440}
    size = (int(dimensions["width"]), int(dimensions["height"]))
    source = str(meta.get("source_label") or meta.get("source_url") or "")
    profile = str(meta.get("visual_profile") or "kushi-oss-portrait-white-infographic")
    channel = str(meta.get("channel") or "微信贴图")
    cards = list(data.get("cards") or [])
    uses_kit = any(isinstance(c, dict) and c.get("kit") for c in cards)
    skip_roles = {r.strip() for r in str(args.skip_cover_roles or "").split(",") if r.strip()}

    out_dir = Path(args.output_dir)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    html_dir = Path(args.html_dir) if args.html_dir else out_dir / "html"
    if not html_dir.is_absolute():
        html_dir = ROOT / html_dir
    html_dir.mkdir(parents=True, exist_ok=True)

    css_path = Path(args.template_css) if args.template_css else TEMPLATE_CSS
    if not css_path.is_absolute():
        css_path = ROOT / css_path
    css_text = css_path.read_text(encoding="utf-8")
    kit_scripts = ""
    wait_motion = False
    kit_dir: Path | None = None
    if args.kit:
        kit_dir = Path(args.kit)
    elif uses_kit:
        kit_dir = ROOT / "templates/wechat-card-kit"
    if kit_dir is not None:
        if not kit_dir.is_absolute():
            kit_dir = ROOT / kit_dir
        kit_css, kit_scripts = build_kit_assets(kit_dir, html_dir)
        css_text = css_text + "\n" + kit_css
        wait_motion = True
    html_paths: list[Path] = []
    out_paths: list[Path] = []
    manifest_cards: list[dict[str, Any]] = []
    animated_exports: list[dict[str, Any]] = []

    for index, card in enumerate(cards, start=1):
        card = dict(card)
        card.setdefault("seq", index)
        role = str(card.get("role") or "")
        file_name = str(card.get("file") or f"{index:02d}.png")
        stem = Path(file_name).stem
        html_path = html_dir / f"{stem}.html"

        if role in skip_roles:
            manifest_cards.append(
                {
                    "seq": index,
                    "role": role,
                    "title": card.get("title"),
                    "path": None,
                    "skipped": True,
                    "reason": f"role {role} skipped (external cover)",
                }
            )
            continue

        html_path.write_text(
            render_card_html(
                card,
                source=source,
                total=len(cards),
                css_text=css_text,
                channel=channel,
                kit_scripts=kit_scripts,
            ),
            encoding="utf-8",
        )
        out_path = out_dir / file_name
        html_paths.append(html_path)
        out_paths.append(out_path)
        manifest_cards.append(
            {
                "seq": index,
                "role": role,
                "title": card.get("title"),
                "path": rel_to_root(out_path),
                "html": rel_to_root(html_path),
                "width": size[0],
                "height": size[1],
                "renderer": "html+playwright",
                "qa_status": "pass_local_html_render",
            }
        )

    if html_paths:
        screenshot_htmls(html_paths, out_paths, size, wait_motion=wait_motion)
    if args.export != "none":
        for html_path, out_path in zip(html_paths, out_paths):
            ext = args.export
            anim_out = out_path.with_suffix(f".{ext}")
            export_animation(
                html_path,
                anim_out,
                export=args.export,
                fps=args.fps,
                gif_scale=args.gif_scale,
                size=size,
                wait_motion=wait_motion,
            )
            animated_exports.append(
                {
                    "card": out_path.name,
                    "file": rel_to_root(anim_out),
                    "format": ext,
                    "fps": args.fps,
                    "scale": args.gif_scale if ext == "gif" else 1.0,
                }
            )

    if args.manifest:
        manifest_path = Path(args.manifest)
        if not manifest_path.is_absolute():
            manifest_path = ROOT / manifest_path
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest = {
            "schema_version": "1",
            "visual_profile": profile,
            "media_type": meta.get("media_type", "image"),
            "kind": meta.get("kind", "image_post"),
            "dimensions": {"width": size[0], "height": size[1]},
            "image_count": len(out_paths),
            "source_url": meta.get("source_url"),
            "renderer": "scripts/render_wechat_html_cards.py",
            "template": "templates/kushi-wechat-image-post",
            "cards": manifest_cards,
        }
        if animated_exports:
            manifest["animated_exports"] = animated_exports
        manifest_path.write_text(
            yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    if args.contact_sheet and out_paths:
        contact_path = Path(args.contact_sheet)
        if not contact_path.is_absolute():
            contact_path = ROOT / contact_path
        make_contact_sheet(out_paths, contact_path)

    for path in out_paths:
        print(rel_to_root(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
