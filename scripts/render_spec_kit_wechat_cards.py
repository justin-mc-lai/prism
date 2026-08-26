#!/usr/bin/env python3
"""Render Spec Kit WeChat image-post cards.

This script intentionally uses Gemini-generated no-text visual bases and then
composites exact local typography on top. That keeps the creative visual layer
generative while making Chinese/command text deterministic and QA-able.
"""

from __future__ import annotations

import math
import shutil
from pathlib import Path
from typing import Iterable, Sequence

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE_DIR = ROOT / ".qi-dev/gemini-images/spec-kit-wechat-v2/base"
RENDER_DIR = ROOT / "content/renders/kushi-gzh/wechat-gzh/assets/spec-kit"
MASTER_DIR = ROOT / "content/masters/oss-picks/spec-kit/assets"
PUNK_DIR = ROOT / "punk-assets/punk-cover/spec-kit-wechat-gzh-depth-v1"
QA_DIR = ROOT / "content/presentations/oss-picks/spec-kit/wechat-gzh-depth-v1/qa"

CARD_SIZE = (1376, 768)
PUNK_COVER_SIZE = (1645, 700)  # 2.35:1

FONT_CN = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_CN_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"
FONT_FALLBACK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

NAVY = (22, 37, 64)
BLUE = (42, 103, 212)
CYAN = (42, 152, 211)
RED = (214, 64, 72)
ORANGE = (219, 132, 37)
GREEN = (31, 142, 100)
GRAY = (103, 113, 128)
LIGHT = (245, 248, 252)
BORDER = (208, 216, 226)
PAPER = (251, 252, 254)


def font(size: int, *, light: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
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


def fit_cover(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    img = img.convert("RGB")
    w, h = img.size
    tw, th = size
    scale = max(tw / w, th / h)
    nw, nh = int(w * scale), int(h * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    return img.crop((left, top, left + tw, top + th))


def base_canvas(base_name: str, size: tuple[int, int] = CARD_SIZE, opacity: int = 214) -> Image.Image:
    path = BASE_DIR / f"{base_name}.jpg"
    if path.exists():
        img = fit_cover(Image.open(path), size)
        img = ImageEnhance.Color(img).enhance(0.55)
        img = ImageEnhance.Contrast(img).enhance(0.82)
        img = ImageEnhance.Brightness(img).enhance(1.16)
        img = img.filter(ImageFilter.GaussianBlur(radius=0.35))
        wash = Image.new("RGBA", size, (255, 255, 255, opacity))
        img = Image.alpha_composite(img.convert("RGBA"), wash)
    else:
        img = Image.new("RGBA", size, PAPER + (255,))
    draw_grid(img)
    return img.convert("RGBA")


def draw_grid(img: Image.Image, step: int = 56) -> None:
    d = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    for x in range(24, w, step):
        d.line((x, 24, x, h - 24), fill=(90, 111, 138, 18), width=1)
    for y in range(24, h, step):
        d.line((24, y, w - 24, y), fill=(90, 111, 138, 13), width=1)
    d.rectangle((34, 34, w - 34, h - 34), outline=(96, 116, 140, 38), width=1)


def text_bbox(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.ImageFont) -> tuple[int, int, int, int]:
    return draw.textbbox(xy, text, font=fnt)


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    box = text_bbox(draw, (0, 0), text, fnt)
    return box[2] - box[0]


def draw_text(
    d: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    size: int,
    fill: tuple[int, int, int] = NAVY,
    *,
    light: bool = False,
    mono: bool = False,
    anchor: str | None = None,
    spacing: int = 8,
) -> None:
    d.text(xy, text, font=font(size, light=light, mono=mono), fill=fill, anchor=anchor, spacing=spacing)


def rounded(
    d: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    *,
    radius: int = 28,
    fill: tuple[int, int, int, int] = (255, 255, 255, 230),
    outline: tuple[int, int, int, int] = BORDER + (210,),
    width: int = 2,
) -> None:
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap_chars(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        trial = current + ch
        if current and text_width(draw, trial, fnt) > max_width:
            lines.append(current)
            current = ch
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    d: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text: str,
    size: int,
    max_width: int,
    fill: tuple[int, int, int] = NAVY,
    *,
    line_gap: int = 8,
    light: bool = False,
) -> int:
    fnt = font(size, light=light)
    yy = y
    for line in wrap_chars(d, text, fnt, max_width):
        d.text((x, yy), line, font=fnt, fill=fill)
        box = text_bbox(d, (x, yy), line, fnt)
        yy += (box[3] - box[1]) + line_gap
    return yy


def draw_chip(d: ImageDraw.ImageDraw, x: int, y: int, text: str, color: tuple[int, int, int] = BLUE) -> None:
    fnt = font(26)
    w = text_width(d, text, fnt) + 36
    # Keep the label deterministic and readable. Some PIL backends render very
    # low-alpha rounded fills as visually saturated on composited RGBA canvases;
    # using a solid chip with white text prevents “blank pill” failures.
    rounded(d, (x, y, x + w, y + 48), radius=24, fill=color + (235,), outline=color + (255,), width=1)
    d.text((x + 18, y + 10), text, font=fnt, fill=(255, 255, 255))


def arrow(d: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color=BLUE, width: int = 4) -> None:
    d.line((*start, *end), fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 18
    spread = 0.45
    p1 = (end[0] - length * math.cos(angle - spread), end[1] - length * math.sin(angle - spread))
    p2 = (end[0] - length * math.cos(angle + spread), end[1] - length * math.sin(angle + spread))
    d.polygon([end, p1, p2], fill=color)


def draw_mini_doc(d: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, color=BLUE, alpha: int = 210) -> None:
    rounded(d, (x, y, x + w, y + h), radius=14, fill=(255, 255, 255, alpha), outline=color + (140,), width=2)
    d.line((x + 24, y + 46, x + w - 24, y + 46), fill=color + (90,), width=3)
    for i in range(4):
        yy = y + 78 + i * 28
        d.line((x + 24, yy, x + w - 30 - i * 12, yy), fill=(86, 101, 125, 90), width=2)


def save(img: Image.Image, name: str) -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    MASTER_DIR.mkdir(parents=True, exist_ok=True)
    out = RENDER_DIR / name
    img.convert("RGB").save(out, "PNG", optimize=True)
    shutil.copy2(out, MASTER_DIR / name)


def render_cover_card() -> Image.Image:
    img = base_canvas("01-cover-base", opacity=202)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 82, "GitHub 官方开源", BLUE)
    draw_text(d, (84, 154), "Spec Kit", 52, NAVY)
    draw_text(d, (84, 244), "先写规格", 118, NAVY)
    draw_text(d, (94, 382), "再让 AI 写代码", 64, BLUE)
    draw_wrapped(d, 92, 485, "碰代码之前，先把“要做什么”落成可执行规格。", 34, 560, GRAY, line_gap=10)

    # Main metaphor: requirement fragments pass through a spec gate.
    gate = (790, 180, 1148, 562)
    rounded(d, gate, radius=34, fill=(255, 255, 255, 232), outline=(42, 103, 212, 190), width=3)
    draw_text(d, (830, 224), "SPEC", 50, BLUE, mono=True)
    draw_text(d, (830, 292), "规格门", 42, NAVY)
    d.line((828, 366, 1110, 366), fill=BLUE + (150,), width=4)
    draw_mini_doc(d, 860, 395, 116, 126, BLUE, 210)
    draw_mini_doc(d, 995, 395, 90, 104, NAVY, 205)
    for y in [250, 325, 410, 490]:
        arrow(d, (610, y + 22), (790, y), (98, 112, 132), 3)
    arrow(d, (1148, 374), (1288, 374), BLUE, 6)
    draw_text(d, (1190, 324), "CODE", 34, BLUE, mono=True)

    draw_text(d, (86, 688), "需求 → 规格 → 计划 → 任务 → 实现", 32, NAVY)
    draw_text(d, (1040, 688), "wechat image card · v2", 22, GRAY, mono=True)
    return img


def render_pain_card() -> Image.Image:
    img = base_canvas("02-pain-base", opacity=222)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 72, "痛点", RED)
    draw_text(d, (84, 146), "AI 先动手，需求后消失", 66, NAVY)
    draw_wrapped(d, 88, 232, "真正缺的不是“更会写代码”，而是一份稳定、可追溯的“要做什么”。", 34, 890, GRAY)

    cards = [
        (92, 355, "需求只在聊天里", "换会话就丢", RED),
        (508, 355, "diff 不敢合", "改了六个文件，不知为何", ORANGE),
        (924, 355, "两周后说不清", "没有决策依据", BLUE),
    ]
    for x, y, title, sub, color in cards:
        rounded(d, (x, y, x + 338, y + 214), radius=26, fill=(255, 255, 255, 238), outline=color + (150,), width=3)
        d.ellipse((x + 28, y + 30, x + 80, y + 82), fill=color + (22,), outline=color + (160,), width=2)
        if color == RED:
            d.line((x + 40, y + 56, x + 68, y + 56), fill=color, width=5)
        elif color == ORANGE:
            d.line((x + 40, y + 48, x + 68, y + 68), fill=color, width=5)
            d.line((x + 68, y + 48, x + 40, y + 68), fill=color, width=5)
        else:
            draw_text(d, (x + 49, y + 36), "?", 38, color)
        draw_text(d, (x + 32, y + 104), title, 38, NAVY)
        draw_wrapped(d, x + 34, y + 158, sub, 25, 270, GRAY, line_gap=4)

    arrow(d, (430, 464), (500, 464), GRAY, 3)
    arrow(d, (846, 464), (916, 464), GRAY, 3)
    draw_text(d, (92, 680), "Spec Kit 的第一步：把需求从聊天窗口搬进仓库。", 34, BLUE)
    return img


def render_repo_card() -> Image.Image:
    img = base_canvas("03-repo-base", opacity=220)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 72, "它是什么", BLUE)
    draw_text(d, (84, 148), "Spec Kit", 86, NAVY)
    draw_text(d, (92, 252), "规格驱动开发工具包", 50, BLUE)

    rounded(d, (690, 120, 1248, 608), radius=34, fill=(255, 255, 255, 238), outline=BLUE + (150,), width=3)
    draw_text(d, (736, 176), "github.com/github/spec-kit", 32, NAVY, mono=True)
    d.line((736, 232, 1204, 232), fill=BORDER + (220,), width=2)
    bullets = [
        ("官方开源", "把需求变成结构化规格"),
        ("不是补全", "是开发前置流水线"),
        ("可接入多种 Agent", "围绕 spec / plan / tasks 落地"),
    ]
    y = 278
    for i, (title, sub) in enumerate(bullets):
        color = [BLUE, GREEN, ORANGE][i]
        d.ellipse((736, y + 4, 760, y + 28), fill=color)
        draw_text(d, (778, y - 2), title, 32, NAVY)
        draw_text(d, (778, y + 42), sub, 25, GRAY)
        y += 104

    draw_mini_doc(d, 120, 368, 170, 198, BLUE)
    draw_mini_doc(d, 255, 408, 150, 174, NAVY)
    draw_mini_doc(d, 390, 448, 126, 146, GREEN)
    draw_text(d, (92, 640), "先问“做什么”，再讨论“怎么做”。", 36, NAVY)
    return img


def render_pipeline_card() -> Image.Image:
    img = base_canvas("04-pipeline-base", opacity=226)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 72, "核心流程", BLUE)
    draw_text(d, (84, 146), "五步把 AI 改仓库管起来", 62, NAVY)

    steps = [
        ("1", "constitution", "定原则"),
        ("2", "specify", "写需求"),
        ("3", "plan", "补方案"),
        ("4", "tasks", "拆任务"),
        ("5", "implement", "落代码"),
    ]
    x0, y0, gap = 92, 332, 248
    centers: list[tuple[int, int]] = []
    for i, (num, cmd, zh) in enumerate(steps):
        x = x0 + i * gap
        centers.append((x + 92, y0 + 92))
        rounded(d, (x, y0, x + 184, y0 + 184), radius=30, fill=(255, 255, 255, 238), outline=BLUE + (130,), width=2)
        d.ellipse((x + 18, y0 + 18, x + 62, y0 + 62), fill=BLUE + (24,), outline=BLUE + (160,), width=2)
        draw_text(d, (x + 34, y0 + 20), num, 30, BLUE, mono=True)
        draw_text(d, (x + 22, y0 + 82), cmd, 26, NAVY, mono=True)
        draw_text(d, (x + 52, y0 + 126), zh, 32, BLUE)
    for a, b in zip(centers, centers[1:]):
        arrow(d, (a[0] + 92, a[1]), (b[0] - 92, b[1]), BLUE, 4)
    draw_text(d, (96, 610), "推荐顺序：clarify 在 plan 前；analyze 在 implement 前。", 34, GRAY)
    draw_text(d, (96, 666), "重点不是步骤多，而是每一步都有可检查的产物。", 34, NAVY)
    return img


def render_commands_card() -> Image.Image:
    img = base_canvas("05-commands-base", opacity=224)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 72, "上手", GREEN)
    draw_text(d, (84, 146), "三步先跑通", 78, NAVY)
    draw_wrapped(d, 88, 244, "先拿一个真实但不危险的小需求试，不要第一把就上正式业务系统。", 30, 512, GRAY)

    rounded(d, (640, 116, 1248, 564), radius=30, fill=(21, 32, 54, 238), outline=(76, 104, 148, 210), width=2)
    d.ellipse((674, 150, 690, 166), fill=RED)
    d.ellipse((702, 150, 718, 166), fill=ORANGE)
    d.ellipse((730, 150, 746, 166), fill=GREEN)
    commands = [
        "$ uv tool install specify-cli",
        "$ specify init my-project",
        "$ /speckit.specify …",
    ]
    y = 214
    for line in commands:
        draw_text(d, (684, y), line, 29, (236, 244, 255), mono=True)
        y += 78

    actions = [
        ("1", "安装 CLI", "把工具装进本地环境"),
        ("2", "初始化项目", "生成项目内规格目录"),
        ("3", "写第一份规格", "从一个小需求开始"),
    ]
    y = 358
    for num, title, sub in actions:
        rounded(d, (92, y, 552, y + 86), radius=22, fill=(255, 255, 255, 240), outline=BORDER + (220,), width=2)
        d.ellipse((120, y + 24, 160, y + 64), fill=GREEN + (24,), outline=GREEN + (150,), width=2)
        draw_text(d, (132, y + 24), num, 26, GREEN, mono=True)
        draw_text(d, (184, y + 16), title, 31, NAVY)
        draw_text(d, (184, y + 54), sub, 23, GRAY)
        y += 98
    draw_wrapped(d, 648, 618, "命令入口按 integration 查看，初始化后以项目内生成文件为准。", 28, 560, GRAY, line_gap=6)
    return img


def render_extensions_card() -> Image.Image:
    img = base_canvas("06-extensions-base", opacity=224)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 72, "扩展机制", BLUE)
    draw_text(d, (84, 146), "Extension / Preset / Bundle", 58, NAVY)
    draw_text(d, (88, 226), "不是铁板流程，而是一套可以叠加的角色配置。", 32, GRAY)

    layers = [
        (304, "Extension", "加新能力", BLUE),
        (424, "Preset", "改模板和术语", GREEN),
        (544, "Bundle", "打包成角色配置", ORANGE),
    ]
    for y, en, zh, color in layers:
        rounded(d, (130, y, 720, y + 82), radius=24, fill=(255, 255, 255, 238), outline=color + (150,), width=3)
        draw_text(d, (168, y + 18), en, 34, color, mono=True)
        draw_text(d, (454, y + 20), zh, 32, NAVY)
        d.line((168, y + 64, 676, y + 64), fill=color + (72,), width=2)

    rounded(d, (820, 232, 1234, 560), radius=28, fill=(255, 255, 255, 238), outline=BLUE + (120,), width=2)
    draw_text(d, (860, 278), "优先级", 46, NAVY)
    priority = ["项目本地覆盖", "Preset", "Extension", "Core"]
    y = 356
    for i, item in enumerate(priority):
        color = [BLUE, GREEN, ORANGE, GRAY][i]
        d.rounded_rectangle((866, y, 1192, y + 44), radius=14, fill=color + (20,), outline=color + (110,), width=1)
        draw_text(d, (888, y + 8), item, 26, color)
        if i < len(priority) - 1:
            draw_text(d, (1008, y + 48), "↓", 30, GRAY)
        y += 70
    draw_text(d, (94, 676), "从官方流程起步，再慢慢替换成团队自己的流程。", 34, NAVY)
    return img


def render_punk_cover() -> Image.Image:
    img = base_canvas("01-cover-base", size=PUNK_COVER_SIZE, opacity=206)
    d = ImageDraw.Draw(img, "RGBA")
    w, h = PUNK_COVER_SIZE
    d.rectangle((0, 0, w, h), fill=(255, 255, 255, 18))
    draw_chip(d, 86, 72, "OSS PICKS · WECHAT COVER", BLUE)
    draw_text(d, (86, 158), "先写规格", 126, NAVY)
    draw_text(d, (92, 306), "Spec Kit：碰代码之前先写规格", 48, BLUE)
    draw_text(d, (94, 392), "需求先落成可执行规格，AI 再按计划、任务动代码。", 34, GRAY)
    gate = (1080, 144, 1490, 522)
    rounded(d, gate, radius=34, fill=(255, 255, 255, 235), outline=BLUE + (170,), width=3)
    draw_text(d, (1126, 198), "SPEC", 52, BLUE, mono=True)
    draw_text(d, (1126, 280), "Gate", 44, NAVY, mono=True)
    for y in (228, 314, 398, 476):
        arrow(d, (820, y + 16), (1080, y), (100, 116, 138), 3)
    arrow(d, (1490, 338), (1584, 338), BLUE, 6)
    draw_text(d, (92, 606), "需求 → 规格 → 计划 → 任务 → 实现", 32, NAVY)
    return img


def make_contact_sheet(images: Sequence[tuple[str, Image.Image]]) -> None:
    thumb_w, thumb_h = 430, 240
    gap = 20
    sheet = Image.new("RGB", (thumb_w * 2 + gap * 3, thumb_h * 3 + gap * 4), (246, 248, 252))
    d = ImageDraw.Draw(sheet)
    for idx, (name, img) in enumerate(images):
        x = gap + (idx % 2) * (thumb_w + gap)
        y = gap + (idx // 2) * (thumb_h + gap)
        thumb = fit_cover(img.convert("RGB"), (thumb_w, thumb_h))
        sheet.paste(thumb, (x, y))
        d.rectangle((x, y, x + thumb_w, y + thumb_h), outline=(196, 205, 218), width=2)
        d.text((x + 12, y + 12), name, font=font(18, mono=True), fill=(22, 37, 64))
    QA_DIR.mkdir(parents=True, exist_ok=True)
    sheet.save(QA_DIR / "contact-sheet-v2.png", "PNG", optimize=True)


def main() -> None:
    cards = [
        ("cover-spec-driven.png", render_cover_card()),
        ("01-distraction-before-spec.png", render_pain_card()),
        ("github-repo-header.png", render_repo_card()),
        ("02-five-step-pipeline.png", render_pipeline_card()),
        ("04-slash-commands.png", render_commands_card()),
        ("03-extensions-layers.png", render_extensions_card()),
    ]
    for name, image in cards:
        save(image, name)

    PUNK_DIR.mkdir(parents=True, exist_ok=True)
    render_punk_cover().convert("RGB").save(PUNK_DIR / "cover.png", "PNG", optimize=True)
    make_contact_sheet(cards)

    print("rendered:")
    for name, _ in cards:
        print(f"- {RENDER_DIR / name}")
    print(f"- {PUNK_DIR / 'cover.png'}")
    print(f"- {QA_DIR / 'contact-sheet-v2.png'}")


if __name__ == "__main__":
    main()
