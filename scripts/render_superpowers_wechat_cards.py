#!/usr/bin/env python3
"""Render Superpowers WeChat image-post cards.

The public WeChat cards are deterministic local typography on a clean white
canvas. Generated/Gemini assets, when they exist, are treated only as upstream
research or cover inspiration; they are not composited into the body cards so
visual QA can guarantee no grid noise, random text, or internal production
notes leak into the draft.
"""

from __future__ import annotations

import math
import shutil
from pathlib import Path
from typing import Sequence

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE_DIR = ROOT / ".qi-dev/gemini-images/superpowers-wechat-v1/base"
RENDER_DIR = ROOT / "content/renders/kushi-gzh/wechat-gzh/assets/superpowers"
MASTER_DIR = ROOT / "content/masters/oss-picks/superpowers/assets"
PRESENTATION_DIR = ROOT / "content/presentations/oss-picks/superpowers/wechat-gzh-depth-v1"
QA_DIR = PRESENTATION_DIR / "qa"
PUNK_DIR = ROOT / "punk-assets/punk-cover/superpowers-wechat-gzh-depth-v1"

CARD_SIZE = (1376, 768)
PUNK_COVER_SIZE = (1645, 700)

FONT_CN = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_CN_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"
FONT_FALLBACK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

NAVY = (21, 34, 58)
BLUE = (39, 101, 205)
CYAN = (38, 143, 190)
RED = (210, 67, 74)
ORANGE = (221, 134, 37)
GREEN = (28, 141, 97)
GRAY = (97, 108, 124)
LIGHT = (246, 248, 252)
BORDER = (207, 216, 226)
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


def base_canvas(base_name: str, size: tuple[int, int] = CARD_SIZE, opacity: int = 218) -> Image.Image:
    _ = (base_name, opacity)
    return Image.new("RGBA", size, (255, 255, 255, 255))


def text_bbox(d: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.ImageFont) -> tuple[int, int, int, int]:
    return d.textbbox(xy, text, font=fnt)


def text_width(d: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    box = text_bbox(d, (0, 0), text, fnt)
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
    fill: tuple[int, int, int, int] = (255, 255, 255, 235),
    outline: tuple[int, int, int, int] = BORDER + (220,),
    width: int = 2,
) -> None:
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap_chars(d: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        trial = current + ch
        if current and text_width(d, trial, fnt) > max_width:
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
    fnt = font(25)
    w = text_width(d, text, fnt) + 34
    rounded(d, (x, y, x + w, y + 46), radius=23, fill=color + (235,), outline=color + (255,), width=1)
    d.text((x + 17, y + 9), text, font=fnt, fill=(255, 255, 255))


def arrow(d: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color=BLUE, width: int = 4) -> None:
    d.line((*start, *end), fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 18
    spread = 0.45
    p1 = (end[0] - length * math.cos(angle - spread), end[1] - length * math.sin(angle - spread))
    p2 = (end[0] - length * math.cos(angle + spread), end[1] - length * math.sin(angle + spread))
    d.polygon([end, p1, p2], fill=color)


def draw_doc(d: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, color=BLUE) -> None:
    rounded(d, (x, y, x + w, y + h), radius=14, fill=(255, 255, 255, 230), outline=color + (130,), width=2)
    d.line((x + 22, y + 42, x + w - 22, y + 42), fill=color + (90,), width=3)
    for i in range(4):
        yy = y + 72 + i * 28
        d.line((x + 22, yy, x + w - 28 - i * 10, yy), fill=(84, 99, 122, 90), width=2)


def footer(d: ImageDraw.ImageDraw, text: str = "github.com/obra/superpowers") -> None:
    draw_text(d, (84, 690), text, 25, GRAY, mono=True)
    draw_text(d, (1126, 690), "OSS Picks", 23, GRAY, mono=True)


def save(img: Image.Image, name: str) -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    MASTER_DIR.mkdir(parents=True, exist_ok=True)
    out = RENDER_DIR / name
    img.convert("RGB").save(out, "PNG", optimize=True)
    shutil.copy2(out, MASTER_DIR / name)


def render_cover_card() -> Image.Image:
    img = base_canvas("01-cover-base", opacity=204)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 74, "AI Coding Skills", BLUE)
    draw_text(d, (84, 148), "Superpowers", 58, NAVY, mono=True)
    draw_text(d, (84, 242), "让 Agent", 98, NAVY)
    draw_text(d, (90, 362), "先守规矩", 116, BLUE)
    draw_wrapped(d, 92, 505, "不是让 AI 写更多代码，而是把澄清、计划、测试、评审变成强制流程。", 32, 610, GRAY, line_gap=9)

    gate = (790, 160, 1168, 555)
    rounded(d, gate, radius=36, fill=(255, 255, 255, 236), outline=BLUE + (190,), width=3)
    draw_text(d, (830, 214), "SKILL", 48, BLUE, mono=True)
    draw_text(d, (830, 286), "纪律门", 44, NAVY)
    d.line((830, 352, 1128, 352), fill=BLUE + (150,), width=4)
    labels = [("澄清", 846, 392), ("计划", 996, 392), ("测试", 846, 468), ("评审", 996, 468)]
    for label, x, y in labels:
        rounded(d, (x, y, x + 110, y + 50), radius=16, fill=LIGHT + (240,), outline=BORDER + (220,), width=1)
        draw_text(d, (x + 55, y + 9), label, 28, NAVY, anchor=None)
    for y in [234, 330, 426]:
        arrow(d, (645, y), (790, y), GRAY, 3)
    arrow(d, (1168, 356), (1296, 356), BLUE, 6)
    draw_text(d, (1210, 302), "CODE", 35, BLUE, mono=True)
    footer(d)
    return img


def render_pain_card() -> Image.Image:
    img = base_canvas("02-pain-base", opacity=222)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 72, "痛点", RED)
    draw_text(d, (84, 146), "AI 一上来就乱改？", 67, NAVY)
    draw_wrapped(d, 88, 230, "真正吓人的不是改得慢，而是它为什么这样改，你两周后也说不清。", 34, 850, GRAY, line_gap=9)

    cards = [
        (92, 356, "需求没对齐", "还没问清，就新建文件", RED),
        (508, 356, "diff 不敢合", "路由、配置、测试一起动", ORANGE),
        (924, 356, "会话一换就丢", "决策依据只在聊天里", BLUE),
    ]
    for x, y, title, sub, color in cards:
        rounded(d, (x, y, x + 338, y + 214), radius=26, fill=(255, 255, 255, 240), outline=color + (150,), width=3)
        d.ellipse((x + 30, y + 30, x + 82, y + 82), fill=color + (22,), outline=color + (160,), width=2)
        if color == RED:
            d.line((x + 43, y + 56, x + 69, y + 56), fill=color, width=5)
        elif color == ORANGE:
            d.line((x + 43, y + 47, x + 69, y + 69), fill=color, width=5)
            d.line((x + 69, y + 47, x + 43, y + 69), fill=color, width=5)
        else:
            draw_text(d, (x + 47, y + 36), "?", 37, color)
        draw_text(d, (x + 32, y + 104), title, 38, NAVY)
        draw_wrapped(d, x + 34, y + 158, sub, 25, 270, GRAY, line_gap=4)
    arrow(d, (432, 464), (498, 464), GRAY, 3)
    arrow(d, (848, 464), (914, 464), GRAY, 3)
    draw_wrapped(d, 104, 610, "Superpowers 的切口：先把工作顺序变成必须执行的 skill。", 31, 1010, NAVY)
    footer(d)
    return img


def render_repo_card() -> Image.Image:
    img = base_canvas("03-repo-base", opacity=224)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 72, "仓库定位", BLUE)
    draw_text(d, (84, 145), "不是 IDE 插件，是流程层", 64, NAVY)
    draw_text(d, (88, 228), "它把资深工程师的工作习惯拆成 Skills，按场景触发。", 31, GRAY)
    draw_text(d, (88, 272), "可在 Claude Code、Codex、Cursor 等工具中使用。", 31, GRAY)

    rounded(d, (86, 332, 636, 604), radius=30, fill=(255, 255, 255, 242), outline=BLUE + (160,), width=3)
    repo_lines = [
        ("仓库", "obra/superpowers", BLUE),
        ("定位", "Agentic skills framework", BLUE),
        ("许可证", "MIT", NAVY),
        ("组成", "skills/ · 多端插件 · 文档", NAVY),
        ("适配", "Claude Code / Codex / Cursor", NAVY),
    ]
    yy = 366
    for label, value, color in repo_lines:
        draw_text(d, (124, yy), f"{label}：", 29, GRAY)
        mono_value = value in {"obra/superpowers", "Agentic skills framework", "Claude Code / Codex / Cursor"}
        value_size = 24 if label == "适配" else 29
        draw_text(d, (220, yy - 1), value, value_size, color, mono=mono_value)
        yy += 45

    modules = [
        (744, 350, "方法论", "先设计，再动手", BLUE),
        (1012, 350, "Skills", "触发条件 + 禁止项", GREEN),
        (744, 502, "多端", "Codex / Cursor 等", ORANGE),
        (1012, 502, "纪律层", "把流程焊进会话", RED),
    ]
    arrow(d, (636, 468), (738, 402), BLUE, 3)
    arrow(d, (636, 468), (1006, 402), BLUE, 3)
    arrow(d, (636, 468), (738, 554), BLUE, 3)
    arrow(d, (636, 468), (1006, 554), BLUE, 3)
    for x, y, title, sub, color in modules:
        rounded(d, (x, y, x + 232, y + 104), radius=22, fill=(255, 255, 255, 238), outline=color + (140,), width=2)
        draw_text(d, (x + 24, y + 20), title, 33, color)
        draw_text(d, (x + 24, y + 62), sub, 22, GRAY)
    footer(d)
    return img


def render_workflow_card() -> Image.Image:
    img = base_canvas("04-workflow-base", opacity=222)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 70, "核心机制", GREEN)
    draw_text(d, (84, 142), "把老工程师动作焊进会话", 62, NAVY)
    draw_wrapped(d, 88, 224, "不是 README 里的温馨提示，而是每次任务中必须触发的工作流。", 32, 850, GRAY)

    steps = [
        ("澄清", "brainstorming", BLUE),
        ("开分支", "worktrees", CYAN),
        ("写计划", "plans", ORANGE),
        ("TDD", "red-green", RED),
        ("Review", "code review", GREEN),
        ("收尾", "finish branch", NAVY),
    ]
    x0, y0 = 82, 380
    gap = 200
    for i, (title, sub, color) in enumerate(steps):
        x = x0 + i * gap
        rounded(d, (x, y0, x + 150, y0 + 150), radius=26, fill=(255, 255, 255, 241), outline=color + (160,), width=3)
        draw_text(d, (x + 75, y0 + 30), title, 35, color, anchor="ma")
        draw_text(d, (x + 75, y0 + 86), sub, 18, GRAY, mono=True, anchor="ma")
        if i < len(steps) - 1:
            arrow(d, (x + 156, y0 + 75), (x0 + (i + 1) * gap - 10, y0 + 75), GRAY, 3)
    rounded(d, (232, 590, 1146, 650), radius=24, fill=(245, 248, 252, 240), outline=BORDER + (200,), width=1)
    draw_text(d, (258, 606), "判断标准：如果某个 skill 有 1% 可能适用，先加载再回复。", 31, NAVY)
    footer(d)
    return img


def render_quickstart_card() -> Image.Image:
    img = base_canvas("05-quickstart-base", opacity=220)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 70, "上手验证", ORANGE)
    draw_text(d, (84, 142), "装好后，先做冒烟测试", 63, NAVY)
    draw_wrapped(d, 88, 224, "别看它会不会立刻写代码，先看它会不会停下来问清楚。", 32, 760, GRAY)

    rounded(d, (92, 344, 642, 594), radius=28, fill=(23, 35, 58, 236), outline=(23, 35, 58, 255), width=2)
    draw_text(d, (126, 378), "/add-plugin superpowers", 29, (235, 244, 255), mono=True)
    draw_text(d, (126, 440), "帮我加邮箱登录，先别写代码。", 31, (255, 255, 255))
    d.line((126, 502, 590, 502), fill=(121, 150, 184, 160), width=2)
    draw_text(d, (126, 526), "期望：先追问方案，不直接新建文件", 26, (204, 218, 236))

    rounded(d, (730, 344, 1248, 594), radius=28, fill=(255, 255, 255, 242), outline=GREEN + (150,), width=3)
    draw_text(d, (768, 384), "重点读三份 skill", 40, NAVY)
    code_lines = [
        "skills/brainstorming/SKILL.md",
        "skills/writing-plans/SKILL.md",
        "skills/subagent-driven-development/SKILL.md",
    ]
    yy = 452
    for line in code_lines:
        draw_text(d, (770, yy), line, 21, BLUE, mono=True)
        yy += 42
    arrow(d, (650, 470), (724, 470), GREEN, 5)
    footer(d)
    return img


def render_guardrails_card() -> Image.Image:
    img = base_canvas("06-guardrails-base", opacity=222)
    d = ImageDraw.Draw(img, "RGBA")
    draw_chip(d, 82, 70, "冷静提醒", RED)
    draw_text(d, (84, 142), "不是魔法，是护栏", 70, NAVY)
    draw_wrapped(d, 88, 232, "流程不会消灭模型幻觉，但能让风险更早暴露、让人更容易审。", 33, 840, GRAY)

    cards = [
        (92, 370, "测试兜底", "胡编 API 仍会发生", RED),
        (508, 370, "Review 卡口", "严重问题先停下", ORANGE),
        (924, 370, "人工确认", "公开前必须人审", GREEN),
    ]
    for x, y, title, sub, color in cards:
        rounded(d, (x, y, x + 338, y + 176), radius=28, fill=(255, 255, 255, 242), outline=color + (150,), width=3)
        draw_text(d, (x + 34, y + 34), title, 40, color)
        draw_wrapped(d, x + 36, y + 96, sub, 27, 260, GRAY)
    draw_wrapped(d, 126, 600, "适合：被 Agent 即兴发挥折磨过、又希望把规范写成可复用 Skill 的团队。", 31, 1060, NAVY)
    footer(d)
    return img


def render_punk_cover() -> Image.Image:
    img = base_canvas("01-cover-base", size=PUNK_COVER_SIZE, opacity=207)
    d = ImageDraw.Draw(img, "RGBA")
    w, h = PUNK_COVER_SIZE
    d.rectangle((48, 46, w - 48, h - 46), outline=(96, 116, 140, 70), width=1)
    d.line((76, 136, w - 76, 136), fill=(96, 116, 140, 70), width=1)
    d.line((76, h - 108, w - 76, h - 108), fill=(96, 116, 140, 70), width=1)

    draw_text(d, (82, 78), "OSS PICKS / WECHAT COVER", 24, GRAY, mono=True)
    draw_text(d, (1198, 78), "SUPERVISED WORKFLOW", 23, GRAY, mono=True)
    draw_text(d, (112, 184), "先守规矩", 116, NAVY)
    draw_text(d, (118, 330), "Superpowers：让 AI 动代码前先学流程", 48, BLUE)
    draw_wrapped(d, 122, 420, "把澄清、计划、TDD、子代理、Review、分支收尾做成必须触发的 Skills。", 34, 760, GRAY, line_gap=10)

    gate = (1040, 204, 1446, 476)
    rounded(d, gate, radius=30, fill=(255, 255, 255, 238), outline=BLUE + (170,), width=3)
    draw_text(d, (1080, 250), "RULE GATE", 34, BLUE, mono=True)
    for i, label in enumerate(["澄清", "计划", "测试", "评审"]):
        x = 1082 + (i % 2) * 160
        y = 316 + (i // 2) * 72
        rounded(d, (x, y, x + 118, y + 48), radius=16, fill=LIGHT + (240,), outline=BORDER + (220,), width=1)
        draw_text(d, (x + 59, y + 9), label, 27, NAVY, anchor=None)
    arrow(d, (922, 340), (1036, 340), ORANGE, 5)
    arrow(d, (1448, 340), (1548, 340), BLUE, 5)
    draw_text(d, (118, 610), "github.com/obra/superpowers", 28, GRAY, mono=True)
    return img


def make_contact_sheet(items: Sequence[tuple[str, Image.Image]]) -> None:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    thumb_w, thumb_h = 344, 192
    gap = 22
    label_h = 38
    cols = 3
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * thumb_w + (cols + 1) * gap, rows * (thumb_h + label_h) + (rows + 1) * gap), "white")
    d = ImageDraw.Draw(sheet)
    for idx, (name, img) in enumerate(items):
        col = idx % cols
        row = idx // cols
        x = gap + col * (thumb_w + gap)
        y = gap + row * (thumb_h + label_h)
        thumb = fit_cover(img.convert("RGB"), (thumb_w, thumb_h))
        sheet.paste(thumb, (x, y))
        d.text((x, y + thumb_h + 8), name, font=font(18, mono=True), fill=NAVY)
    sheet.save(QA_DIR / "contact-sheet-v2.png", "PNG", optimize=True)


def main() -> None:
    cards = [
        ("cover-superpowers.png", render_cover_card()),
        ("01-agent-runs-ahead.png", render_pain_card()),
        ("02-repo-evidence.png", render_repo_card()),
        ("03-mandatory-workflow.png", render_workflow_card()),
        ("04-install-smoke-test.png", render_quickstart_card()),
        ("05-guardrails.png", render_guardrails_card()),
    ]
    for name, img in cards:
        save(img, name)
    make_contact_sheet(cards)

    PUNK_DIR.mkdir(parents=True, exist_ok=True)
    render_punk_cover().convert("RGB").save(PUNK_DIR / "cover.png", "PNG", optimize=True)
    print("rendered Superpowers WeChat cards:")
    for name, _ in cards:
        print(f"- {RENDER_DIR / name}")
    print(f"- {QA_DIR / 'contact-sheet-v2.png'}")
    print(f"- {PUNK_DIR / 'cover.png'}")


if __name__ == "__main__":
    main()
