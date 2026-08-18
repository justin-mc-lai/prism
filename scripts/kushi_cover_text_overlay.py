#!/usr/bin/env python3
"""库拾 article-paper 封面文字叠加：Gemini 无字底图 → 本地标题排版 1080×1440。

生成式模型只负责无文字底图；标题、副句、标签一律由本地排版叠加，
保证公众号封面标题清晰、无乱码。

Usage:
  python3 scripts/kushi_cover_text_overlay.py \
    --base .qi-dev/gemini-images/<slug>/cover-textless.jpg \
    --out content/renders/kushi-gzh/wechat-gzh/assets/<slug>-vN/01-cover.jpg \
    --title "给 Claude 装一套工程流水线" \
    --sub "先想清楚再写代码 · gstack" \
    --tag "开源仓库核对"
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1440
PAPER = (249, 248, 244)
INK = (26, 26, 26)
MUTED = (92, 92, 92)
ACCENT = (224, 138, 60)
LINE = (210, 210, 205)
FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="无文字底图（3:4，任意分辨率）")
    parser.add_argument("--out", required=True, help="输出 1080x1440 封面")
    parser.add_argument("--title", required=True, help="主标题（20 字内，不带账号前缀）")
    parser.add_argument("--sub", default="", help="副句")
    parser.add_argument("--tag", default="", help="右下小标签")
    args = parser.parse_args()

    im = Image.open(args.base).convert("RGB")
    if im.size != (W, H):
        im = im.resize((W, H), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(im)

    # 底部暖纸文字区 + 细分割线 + 橙色强调条
    band_top = 1016
    draw.rectangle((0, band_top, W, H), fill=PAPER)
    draw.line((0, band_top, W, band_top), fill=LINE, width=2)
    draw.rectangle((72, 1052, 168, 1062), fill=ACCENT)

    font_title = ImageFont.truetype(FONT_PATH, 70, index=2)
    draw.text((72, 1080), args.title, font=font_title, fill=INK)

    if args.sub:
        font_sub = ImageFont.truetype(FONT_PATH, 32, index=0)
        draw.text((72, 1190), args.sub, font=font_sub, fill=MUTED)

    if args.tag:
        font_tag = ImageFont.truetype(FONT_PATH, 26, index=0)
        box = draw.textbbox((0, 0), args.tag, font=font_tag)
        draw.text(
            (W - 72 - (box[2] - box[0]), 1352),
            args.tag,
            font=font_tag,
            fill=MUTED,
        )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=95, optimize=True)
    print(out)


if __name__ == "__main__":
    raise SystemExit(main())
