#!/usr/bin/env python3
"""Template-based Xiaohongshu cover renderer (本地模板排版，非文生图).

与 render_wechat_image_cards.py 同思路：数据驱动 + PIL 确定性绘制。
第一个内置风格是「大字多层排版」（参考 xhscover.vivi.wiki 的多层排版/背景大字类模板）：
奶油白底、大标题、强调色块、标签 chips、来源行。
后续风格在 STYLES 注册表中追加即可。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

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
CREAM = (250, 247, 242)
SOFT_ORANGE = (255, 244, 230)
SOFT_BLUE = (239, 246, 255)
SOFT_GREEN = (236, 253, 245)
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
    align: str = "left",
) -> int:
    fnt = font(size, light=light, mono=mono)
    lines = wrap_text(draw, text, fnt, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    yy = y
    for line in lines:
        w = text_width(draw, line, fnt)
        xx = x if align == "left" else x + max(0, (max_width - w) // 2)
        draw.text((xx, yy), line, font=fnt, fill=fill)
        yy += line_height(draw, line, fnt) + line_gap
    return yy


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    *,
    radius: int = 28,
    fill: tuple[int, int, int] = (255, 255, 255),
    outline: tuple[int, int, int] | None = BORDER,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def chip(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, color_name: str = "blue", *, filled: bool = False) -> int:
    color = PALETTE.get(color_name, BLUE)
    fnt = font(28)
    w = text_width(draw, text, fnt) + 44
    h = 56
    if filled:
        rounded(draw, (x, y, x + w, y + h), radius=h // 2, fill=color, outline=None)
        draw.text((x + 22, y + 12), text, font=fnt, fill=(255, 255, 255))
    else:
        rounded(draw, (x, y, x + w, y + h), radius=h // 2, fill=(255, 255, 255), outline=color, width=3)
        draw.text((x + 22, y + 12), text, font=fnt, fill=color)
    return x + w


def style_multi_layer(draw: ImageDraw.ImageDraw, size: tuple[int, int], opts: dict[str, Any]) -> None:
    """大字多层排版：奶油白底 + 大标题 + 强调色块 + 标签 chips + 来源行。"""
    width, height = size
    if not opts.get("base_image"):
        draw.rectangle((0, 0, width, height), fill=CREAM)

    # 左上装饰块与右上序号
    draw.rounded_rectangle((72, 92, 432, 196), radius=28, fill=SOFT_ORANGE, outline=None)
    chip(draw, 108, 120, str(opts.get("kicker") or "库拾开源精选"), "orange", filled=True)
    draw.text((912, 108), str(opts.get("index") or "01"), font=font(64, mono=True), fill=(224, 217, 205))

    # 主标题（大字号，最多 3 行）
    title = str(opts.get("title") or "")
    fnt_title = font(92)
    title_lines = wrap_text(draw, title, fnt_title, width - 144)
    title_lines = title_lines[:3]
    y = 300
    for i, line in enumerate(title_lines):
        draw.text((72, y), line, font=fnt_title, fill=INK)
        y += line_height(draw, line, fnt_title) + 18

    # 强调色块：盖在标题最后一行的关键词下
    highlight = str(opts.get("highlight") or "")
    if highlight and title_lines:
        last_w = text_width(draw, title_lines[-1], fnt_title)
        kw = str(opts.get("highlight_text") or "")
        if kw and kw in title_lines[-1]:
            prefix_w = text_width(draw, title_lines[-1].split(kw)[0], fnt_title)
            kw_w = text_width(draw, kw, fnt_title)
            bar_y = y - line_height(draw, title_lines[-1], fnt_title) + 6
            draw.rectangle((72 + prefix_w, bar_y, 72 + prefix_w + kw_w, bar_y + 14), fill=SOFT_BLUE)
        else:
            draw.rectangle((72, y - 12, min(72 + last_w, width - 72), y), fill=SOFT_BLUE)
        y += 30

    # 副标题
    subtitle = str(opts.get("subtitle") or "")
    if subtitle:
        y = draw_wrapped(draw, 76, y + 14, subtitle, 40, width - 152, MUTED, light=True, line_gap=12, max_lines=2)

    # 标签 chips（最多 5 个，超宽自动换行）
    tags = [str(t) for t in (opts.get("tags") or [])[:5]]
    if tags:
        y += 56
        colors = ["blue", "green", "orange", "red", "ink"]
        x = 72
        for tag, color_name in zip(tags, colors):
            w = text_width(draw, tag, font(28)) + 44
            if x + w > width - 72:
                x = 72
                y += 78
            x = chip(draw, x, y, tag, color_name, filled=False) + 18
        y += 96

    # 底部来源行
    draw.line((72, height - 190, width - 72, height - 190), fill=(232, 226, 216), width=2)
    draw.text((72, height - 150), str(opts.get("source") or ""), font=font(30, mono=True), fill=MUTED)
    draw.text((72, height - 104), str(opts.get("footer") or "库拾 · 模板渲染封面"), font=font(26, light=True), fill=(168, 160, 148))


STYLES = {
    "multi-layer": style_multi_layer,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--style", default="multi-layer", choices=sorted(STYLES))
    parser.add_argument("--title", required=True)
    parser.add_argument("--highlight", default="")
    parser.add_argument("--highlight-text", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--kicker", default="库拾开源精选")
    parser.add_argument("--index", default="01")
    parser.add_argument("--tags", default="")
    parser.add_argument("--source", default="")
    parser.add_argument("--footer", default="")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1440)
    parser.add_argument("--base", default="", help="无文字底图路径；存在时不再填充奶油白底，直接在其上排版")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    size = (args.width, args.height)
    img = Image.new("RGB", size, (255, 255, 255))
    base_image = False
    if args.base:
        base_path = Path(args.base)
        if not base_path.is_absolute():
            base_path = ROOT / base_path
        with Image.open(base_path) as base:
            base = base.convert("RGB")
            base.thumbnail((args.width * 2, args.height * 2), Image.Resampling.LANCZOS)
            left = max(0, (base.width - args.width) // 2)
            top = max(0, (base.height - args.height) // 2)
            img.paste(base.crop((left, top, left + args.width, top + args.height)), (0, 0))
        base_image = True
    draw = ImageDraw.Draw(img)
    opts = {
        "title": args.title,
        "highlight": args.highlight,
        "highlight_text": args.highlight_text,
        "subtitle": args.subtitle,
        "kicker": args.kicker,
        "index": args.index,
        "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
        "source": args.source,
        "footer": args.footer,
        "base_image": base_image,
    }
    STYLES[args.style](draw, size, opts)

    out = Path(args.out)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print(out.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
