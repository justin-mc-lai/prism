#!/usr/bin/env python3
"""Render account-contracted WeChat image-post cards from a YAML shot package."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]

FONT_CN = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_CN_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"
FONT_FALLBACK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

INK = (17, 24, 39)
MUTED = (102, 112, 133)
BLUE = (37, 99, 235)
GREEN = (5, 150, 105)
ORANGE = (234, 122, 0)
RED = (220, 38, 38)
SOFT_BLUE = (239, 246, 255)
SOFT_GREEN = (236, 253, 245)
SOFT_ORANGE = (255, 247, 237)
SOFT_RED = (254, 242, 242)
BORDER = (210, 219, 231)
PANEL = (249, 250, 252)

PALETTE = {
    "blue": BLUE,
    "green": GREEN,
    "orange": ORANGE,
    "red": RED,
    "ink": INK,
}

SOFT = {
    "blue": SOFT_BLUE,
    "green": SOFT_GREEN,
    "orange": SOFT_ORANGE,
    "red": SOFT_RED,
    "ink": PANEL,
}


def font(size: int, *, light: bool = False, mono: bool = False) -> ImageFont.ImageFont:
    if mono:
        candidates = [FONT_MONO, FONT_FALLBACK]
    elif light:
        candidates = [FONT_CN_LIGHT, FONT_CN, FONT_FALLBACK]
    else:
        candidates = [FONT_CN, FONT_CN_LIGHT, FONT_FALLBACK]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def line_height(draw: ImageDraw.ImageDraw, sample: str, fnt: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), sample or "字", font=fnt)
    return box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    if not text:
        return []
    lines: list[str] = []
    current = ""
    for token in text:
        trial = current + token
        if current and text_width(draw, trial, fnt) > max_width:
            lines.append(current)
            current = token
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text: str,
    size: int,
    max_width: int,
    fill: tuple[int, int, int] = INK,
    *,
    light: bool = False,
    mono: bool = False,
    line_gap: int = 12,
    max_lines: int | None = None,
) -> int:
    fnt = font(size, light=light, mono=mono)
    lines = wrap_text(draw, text, fnt, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    yy = y
    for line in lines:
        draw.text((x, yy), line, font=fnt, fill=fill)
        yy += line_height(draw, line, fnt) + line_gap
    return yy


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    *,
    radius: int = 28,
    fill: tuple[int, int, int] = (255, 255, 255),
    outline: tuple[int, int, int] = BORDER,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def chip(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, color_name: str = "blue") -> None:
    color = PALETTE.get(color_name, BLUE)
    fnt = font(28)
    w = text_width(draw, text, fnt) + 42
    draw.rounded_rectangle((x, y, x + w, y + 52), radius=26, fill=color)
    draw.text((x + 21, y + 10), text, font=fnt, fill=(255, 255, 255))


def footer(draw: ImageDraw.ImageDraw, source: str, seq: int, total: int) -> None:
    draw.text((72, 1350), source, font=font(24, mono=True), fill=MUTED)
    draw.text((930, 1346), f"{seq}/{total}", font=font(34, mono=True), fill=MUTED)


def title_block(draw: ImageDraw.ImageDraw, card: dict[str, Any], width: int) -> int:
    color_name = card.get("color", "blue")
    chip(draw, 72, 72, str(card.get("kicker", "库拾开源")), color_name)
    draw.text((910, 82), "微信贴图", font=font(24), fill=MUTED)
    y = 158
    y = draw_wrapped(draw, 72, y, str(card["title"]), 58, width - 144, INK, line_gap=16, max_lines=2)
    subtitle = str(card.get("subtitle") or "")
    if subtitle:
        y = draw_wrapped(draw, 74, y + 8, subtitle, 30, width - 148, MUTED, light=True, line_gap=10, max_lines=3)
    return y + 20


def draw_callout(draw: ImageDraw.ImageDraw, y: int, text: str, color_name: str = "blue") -> int:
    color = PALETTE.get(color_name, BLUE)
    soft = SOFT.get(color_name, SOFT_BLUE)
    rounded(draw, (72, y, 1008, y + 136), radius=30, fill=soft, outline=color, width=3)
    draw_wrapped(draw, 112, y + 36, text, 38, 856, color, line_gap=12, max_lines=2)
    return y + 166


def draw_sections(draw: ImageDraw.ImageDraw, y: int, sections: list[dict[str, Any]]) -> int:
    for section in sections:
        color_name = section.get("color", "blue")
        color = PALETTE.get(color_name, BLUE)
        soft = SOFT.get(color_name, PANEL)
        bullets = [str(item) for item in section.get("bullets") or []]
        title = str(section.get("title") or "")

        body_lines = 0
        body_font = font(29, light=True)
        for bullet in bullets:
            body_lines += len(wrap_text(draw, bullet, body_font, 740))
        panel_h = max(148, 88 + body_lines * 44 + max(0, len(bullets) - 1) * 8)
        panel_h = min(panel_h, 270)

        rounded(draw, (72, y, 1008, y + panel_h), radius=26, fill=soft, outline=BORDER, width=2)
        draw.ellipse((104, y + 30, 146, y + 72), fill=color)
        draw.ellipse((121, y + 47, 129, y + 55), fill=(255, 255, 255))
        draw.text((168, y + 28), title, font=font(35), fill=INK)
        yy = y + 84
        for bullet in bullets[:4]:
            draw.text((166, yy), "•", font=font(31), fill=color)
            yy = draw_wrapped(draw, 196, yy, bullet, 29, 740, MUTED, light=True, line_gap=8, max_lines=2)
            yy += 2
        y += panel_h + 26
    return y


def draw_flow(draw: ImageDraw.ImageDraw, y: int, items: list[str], color_name: str = "blue") -> int:
    """Draw a safe-area aware horizontal flow.

    Older renders used a fixed box width and step, so four flow nodes could
    overflow the 1080px canvas and get clipped in the WeChat editor. This
    layout computes each row from the available safe width and wraps longer
    flows while keeping arrows inside the same safe area.
    """
    color = PALETTE.get(color_name, BLUE)
    safe_left = 72
    safe_right = 1008
    max_per_row = 4
    box_h = 112
    row_gap = 34
    arrow_gap = 28
    cursor_y = y

    for row_start in range(0, len(items), max_per_row):
        row = items[row_start : row_start + max_per_row]
        count = max(1, len(row))
        available = safe_right - safe_left
        gap = 48 if count > 1 else 0
        box_w = int((available - gap * (count - 1)) / count)
        box_w = max(156, min(218, box_w))
        total_w = box_w * count + gap * (count - 1)
        x = safe_left + max(0, (available - total_w) // 2)

        for index, item in enumerate(row):
            rounded(
                draw,
                (x, cursor_y, x + box_w, cursor_y + box_h),
                radius=24,
                fill=(255, 255, 255),
                outline=color,
                width=3,
            )
            text_size = 29 if box_w >= 190 else 27
            draw_wrapped(draw, x + 22, cursor_y + 30, item, text_size, box_w - 44, INK, line_gap=8, max_lines=2)
            if index < count - 1:
                arrow_start = x + box_w + arrow_gap // 2
                arrow_end = x + box_w + gap - arrow_gap // 2
                arrow_y = cursor_y + box_h // 2
                draw.line((arrow_start, arrow_y, arrow_end, arrow_y), fill=color, width=5)
                draw.polygon(
                    [(arrow_end, arrow_y), (arrow_end - 18, arrow_y - 11), (arrow_end - 18, arrow_y + 11)],
                    fill=color,
                )
            x += box_w + gap

        cursor_y += box_h + row_gap

    return cursor_y + 10


def draw_cover_hero(draw: ImageDraw.ImageDraw, y: int, card: dict[str, Any]) -> int:
    """Cover hero. Supports content-driven `hero` field; falls back to the
    original Agent formula hero for legacy cards."""
    hero = card.get("hero") or {}
    kind = str(hero.get("kind") or "formula")

    if kind == "counts":
        label = str(hero.get("label") or "")
        stats = hero.get("stats") or []
        if label:
            draw_wrapped(draw, 72, y + 8, label, 46, 936, INK, line_gap=12, max_lines=1)
            y += 92
        if stats:
            box_w = 250
            box_h = 158
            gap = 44
            n = min(3, len(stats))
            total = box_w * n + gap * (n - 1)
            x0 = 72 + (936 - total) // 2
            yy = y + 14
            for stat in stats[:3]:
                color_name = str(stat.get("color") or "blue")
                color = PALETTE.get(color_name, BLUE)
                rounded(
                    draw,
                    (x0, yy, x0 + box_w, yy + box_h),
                    radius=30,
                    fill=(255, 255, 255),
                    outline=color,
                    width=4,
                )
                number = str(stat.get("number") or "")
                fnt_num = font(54, mono=True)
                nw = text_width(draw, number, fnt_num)
                draw.text((x0 + (box_w - nw) // 2, yy + 22), number, font=fnt_num, fill=color)
                draw_wrapped(
                    draw,
                    x0 + 22,
                    yy + 98,
                    str(stat.get("label") or ""),
                    27,
                    box_w - 44,
                    INK,
                    line_gap=8,
                    max_lines=2,
                )
                x0 += box_w + gap
            y = yy + box_h + 18
        return y

    pieces = hero.get("parts") or [
        {"text": "LLM", "color": "blue"},
        {"text": "Context", "color": "orange"},
        {"text": "Tools", "color": "green"},
    ]
    label = str(hero.get("label") or "Agent =")
    rounded(draw, (72, y, 1008, y + 300), radius=38, fill=(255, 255, 255), outline=BLUE, width=4)
    draw.text((132, y + 54), label, font=font(56, mono=True), fill=BLUE)
    x = 132
    yy = y + 154
    for i, piece in enumerate(pieces[:3]):
        name = str(piece.get("text") or "")
        color = PALETTE.get(str(piece.get("color") or "blue"), BLUE)
        rounded(draw, (x, yy, x + 230, yy + 96), radius=28, fill=(255, 255, 255), outline=color, width=3)
        draw.text((x + 42, yy + 25), name, font=font(34, mono=True), fill=color)
        if i < len(pieces) - 1:
            draw.text((x + 250, yy + 21), "+", font=font(48, mono=True), fill=MUTED)
        x += 302
    return y + 334


def draw_compare(draw: ImageDraw.ImageDraw, y: int, card: dict[str, Any]) -> int:
    """Two-column comparison card. Each column has a title and up to 4 bullets."""
    compare = card.get("compare") or {}
    col_w = 440
    gap = 32
    panels: list[tuple[str, str, list[str], str]] = []
    max_h = 0
    body_font = font(27, light=True)
    for key, default_color in (("left", "blue"), ("right", "green")):
        panel = compare.get(key) or {}
        color_name = str(panel.get("color") or default_color)
        title = str(panel.get("title") or "")
        bullets = [str(item) for item in (panel.get("bullets") or [])[:4]]
        body_lines = sum(len(wrap_text(draw, bullet, body_font, col_w - 84)) for bullet in bullets)
        panel_h = max(132, 110 + (30 if title else 0) + len(bullets) * 8 + body_lines * 36)
        panel_h = min(panel_h, 560)
        panels.append((key, color_name, bullets, title))
        max_h = max(max_h, panel_h)

    xs = {"left": 72, "right": 72 + col_w + gap}
    for key, color_name, bullets, title in panels:
        x = xs[key]
        color = PALETTE.get(color_name, BLUE)
        soft = SOFT.get(color_name, SOFT_BLUE)
        rounded(draw, (x, y, x + col_w, y + max_h), radius=26, fill=soft, outline=color, width=3)
        yy = y + 28
        if title:
            yy = draw_wrapped(draw, x + 28, yy, title, 32, col_w - 56, color, line_gap=10, max_lines=2)
            yy += 6
        for bullet in bullets:
            draw.text((x + 28, yy), "•", font=font(29), fill=color)
            yy = draw_wrapped(draw, x + 56, yy, bullet, 27, col_w - 84, INK, light=True, line_gap=8, max_lines=3)
            yy += 6
    return y + max_h + 18


def draw_command_block(draw: ImageDraw.ImageDraw, y: int, card: dict[str, Any]) -> int:
    """Command card: monospace commands plus short caveat notes."""
    commands = card.get("commands") or []
    if isinstance(commands, str):
        commands = [commands]
    for cmd in commands[:3]:
        rounded(draw, (72, y, 1008, y + 108), radius=20, fill=PANEL, outline=BORDER, width=2)
        draw_wrapped(draw, 104, y + 22, str(cmd), 30, 848, INK, mono=True, line_gap=8, max_lines=2)
        y += 122
    for note in (card.get("notes") or [])[:3]:
        draw.text((104, y + 4), "!", font=font(34), fill=RED)
        y = draw_wrapped(draw, 150, y + 4, str(note), 28, 812, MUTED, light=True, line_gap=8, max_lines=3)
        y += 18
    return y + 12


def render_card(card: dict[str, Any], size: tuple[int, int], source: str, total: int) -> Image.Image:
    width, height = size
    img = Image.new("RGB", size, (255, 255, 255))
    draw = ImageDraw.Draw(img)

    color_name = card.get("color", "blue")
    seq = int(card.get("seq") or 1)
    y = title_block(draw, card, width)

    layout = str(card.get("layout") or "")
    if layout == "cover":
        y = draw_cover_hero(draw, y + 8, card)
    elif layout == "compare":
        y = draw_compare(draw, y + 10, card)
    elif layout == "command":
        y = draw_command_block(draw, y + 10, card)

    if card.get("callout") and layout not in ("compare", "command"):
        y = draw_callout(draw, y, str(card["callout"]), color_name)
    if card.get("flow") and layout not in ("compare", "command"):
        y = draw_flow(draw, y + 8, [str(item) for item in card["flow"]], color_name)
    y = draw_sections(draw, y + 4, card.get("sections") or [])

    takeaway = str(card.get("takeaway") or "")
    if takeaway:
        if y > height - 340:
            print(f"warning: card {seq} content may overflow safe area (cursor={y})", file=sys.stderr)
        takeaway_y = min(y + 8, height - 320)
        rounded(draw, (72, takeaway_y, 1008, min(takeaway_y + 148, height - 88)), radius=26, fill=PANEL, outline=BORDER, width=2)
        draw_wrapped(draw, 108, takeaway_y + 34, takeaway, 30, 850, INK, line_gap=10, max_lines=3)

    footer(draw, source, seq, total)
    return img


def make_contact_sheet(paths: list[Path], out: Path) -> None:
    thumbs: list[Image.Image] = []
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cards", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--master-copy-dir", default="")
    parser.add_argument("--manifest", default="")
    parser.add_argument("--contact-sheet", default="")
    args = parser.parse_args()

    cards_path = ROOT / args.cards if not Path(args.cards).is_absolute() else Path(args.cards)
    data = yaml.safe_load(cards_path.read_text(encoding="utf-8")) or {}
    meta = data.get("metadata") or {}
    dimensions = meta.get("dimensions") or {"width": 1080, "height": 1440}
    size = (int(dimensions["width"]), int(dimensions["height"]))
    source = str(meta.get("source_label") or meta.get("source_url") or "")
    profile = str(meta.get("visual_profile") or "kushi-oss-portrait-white-infographic")
    cards = data.get("cards") or []

    out_dir = ROOT / args.output_dir if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    master_dir = None
    if args.master_copy_dir:
        master_dir = ROOT / args.master_copy_dir if not Path(args.master_copy_dir).is_absolute() else Path(args.master_copy_dir)
        master_dir.mkdir(parents=True, exist_ok=True)

    rendered: list[Path] = []
    manifest_cards: list[dict[str, Any]] = []
    for index, card in enumerate(cards, start=1):
        card = dict(card)
        card.setdefault("seq", index)
        file_name = str(card.get("file") or f"{index:02d}.png")
        img = render_card(card, size, source, len(cards))
        out = out_dir / file_name
        img.save(out, "PNG", optimize=True)
        if master_dir:
            shutil.copy2(out, master_dir / file_name)
        rendered.append(out)
        manifest_cards.append(
            {
                "seq": index,
                "role": card.get("role"),
                "title": card.get("title"),
                "path": str(out.relative_to(ROOT)),
                "master_asset": str((master_dir / file_name).relative_to(ROOT)) if master_dir else None,
                "width": size[0],
                "height": size[1],
                "qa_status": "pass_local_render",
            }
        )

    if args.manifest:
        manifest_path = ROOT / args.manifest if not Path(args.manifest).is_absolute() else Path(args.manifest)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest = {
            "schema_version": "1",
            "visual_profile": profile,
            "media_type": meta.get("media_type", "image"),
            "kind": meta.get("kind", "image_post"),
            "dimensions": {"width": size[0], "height": size[1]},
            "image_count": len(rendered),
            "source_url": meta.get("source_url"),
            "renderer": "scripts/render_wechat_image_cards.py",
            "cards": manifest_cards,
        }
        manifest_path.write_text(yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False), encoding="utf-8")

    if args.contact_sheet:
        contact_path = ROOT / args.contact_sheet if not Path(args.contact_sheet).is_absolute() else Path(args.contact_sheet)
        make_contact_sheet(rendered, contact_path)

    print("\n".join(str(path.relative_to(ROOT)) for path in rendered))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
