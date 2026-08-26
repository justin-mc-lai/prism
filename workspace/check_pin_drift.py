#!/usr/bin/env python3
"""Pin 漂移检测：Prism 内 pin 产物与源仓 selfmedia-creator 对照。

规则：
- prism 侧不存在该 pin → SKIP（本仓未安装）
- 源仓侧缺失而 pin 存在 → FAIL（悬空 pin，失去回源参照）
- mode=identical 内容不一致 → FAIL（契约要求逐字节同步，如 ai_manga_drama CLI）
- mode=report 内容不一致 → WARN（历史快照允许演化，人工判断）
--strict 把 WARN 升级为 FAIL。exit 0 = 无 FAIL。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_CREATOR = Path(__file__).resolve().parents[2]  # prism 已并入 monorepo，上两级即 creator 根
PRISM_ROOT = Path(__file__).resolve().parents[1]

# (name, prism 相对路径, creator 相对路径, mode[, prism 跳过头行数, creator 跳过头行数])
# 带 ATTRIBUTION 头的文件型 pin 用跳行数排除头部后再比正文。
PINS: list[tuple] = [
    ("cli/ai_manga_drama", "scripts/ai_manga_drama.py", "scripts/ai_manga_drama.py",
     "identical", 4, 3),
    (
        "pipeline/ai-manga-drama",
        "content/pipelines/ai-manga-drama",
        "content/pipelines/ai-manga-drama",
        "identical",
    ),
]
# A1 MIT 渲染链（ATTRIBUTION-render-chain.md 登记，快照允许本地演化 → report）
for rel in [
    "scripts/render_wechat_html_cards.py",
    "scripts/render_wechat_image_cards.py",
    "scripts/render_wechat_article_pages.py",
    "scripts/render_spec_kit_wechat_cards.py",
    "scripts/render_superpowers_wechat_cards.py",
    "scripts/kushi_cover_text_overlay.py",
    "scripts/render_xhs_cover.py",
    "scripts/render-channel.sh",
    "scripts/lib/kit_render.py",
    "scripts/lib/rewrite-render-asset-refs.py",
]:
    PINS.append((f"render/{Path(rel).stem}", rel, rel, "report"))
for tpl in [
    "templates/kushi-wechat-image-post",
    "templates/kushi-wechat-article-post",
    "templates/wechat-card-kit",
    "templates/jieqi-yangsheng-classical",
]:
    PINS.append((f"template/{Path(tpl).name}", tpl, tpl, "report"))


def _vendor_skill_pins(prism_root: Path) -> list[tuple[str, str, str, str]]:
    """vendor/skills/* 全量按 report 模式对照源仓 skills/*。"""
    vendor = prism_root / "vendor" / "skills"
    if not vendor.is_dir():
        return []
    return [
        (f"skill/{d.name}", f"vendor/skills/{d.name}", f"skills/{d.name}", "report")
        for d in sorted(vendor.iterdir())
        if d.is_dir()
    ]


def tree_snapshot(root: Path, skip_head_lines: int = 0) -> dict[str, bytes] | None:
    """目录 → {相对路径: 内容}；文件 → {"": 内容}。不存在返回 None。

    skip_head_lines：文件型 pin 跳过头部 N 行（ATTRIBUTION 头）后再比对。
    """
    def _strip(data: bytes) -> bytes:
        lines = data.splitlines(keepends=True)
        # 行数不足以容纳声明头部时按原文比对，防止两侧都被剥空造成假 identical。
        if not skip_head_lines or len(lines) <= skip_head_lines:
            return data
        return b"".join(lines[skip_head_lines:])

    if root.is_file():
        return {"": _strip(root.read_bytes())}
    if not root.is_dir():
        return None
    snap: dict[str, bytes] = {}
    for p in sorted(root.rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts and ".DS_Store" != p.name:
            snap[str(p.relative_to(root))] = p.read_bytes()
    return snap


def diff_summary(a: dict[str, bytes], b: dict[str, bytes]) -> list[str]:
    diffs = []
    for key in sorted(set(a) | set(b)):
        if key not in a:
            diffs.append(f"+{key}（仅源仓有）")
        elif key not in b:
            diffs.append(f"-{key}（仅 pin 有）")
        elif a[key] != b[key]:
            diffs.append(f"~{key}")
    return diffs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prism-root", type=Path, default=PRISM_ROOT)
    parser.add_argument("--creator-root", type=Path, default=DEFAULT_CREATOR)
    parser.add_argument("--strict", action="store_true", help="report 级漂移也算失败")
    args = parser.parse_args()

    pins = PINS + _vendor_skill_pins(args.prism_root)
    failed = 0
    warned = 0
    for entry in pins:
        name, prism_rel, creator_rel, mode = entry[:4]
        p_skip = entry[4] if len(entry) > 4 else 0
        c_skip = entry[5] if len(entry) > 5 else 0
        pin_snap = tree_snapshot(args.prism_root / prism_rel, p_skip)
        if pin_snap is None:
            continue  # SKIP：本仓未安装该 pin
        src_snap = tree_snapshot(args.creator_root / creator_rel, c_skip)
        if src_snap is None:
            print(f"FAIL [{name}] 悬空 pin：源仓缺失 {creator_rel}")
            failed += 1
            continue
        if pin_snap == src_snap:
            print(f"ok   [{name}] identical")
            continue
        detail = "; ".join(diff_summary(pin_snap, src_snap)[:5])
        if mode == "identical":
            print(f"FAIL [{name}] identical 契约被破坏：{detail}")
            failed += 1
        elif args.strict:
            print(f"FAIL [{name}] (strict) 漂移：{detail}")
            failed += 1
        else:
            print(f"WARN [{name}] 快照漂移（{len(diff_summary(pin_snap, src_snap))} 个文件）：{detail}")
            warned += 1

    print(f"pins: {len(pins)} checked, {failed} fail, {warned} warn")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
