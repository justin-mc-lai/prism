#!/usr/bin/env python3
"""可读性检查（Prism 原生实现，规则蒸馏自 selfmedia-creator readability-lint.py R9/R10）。

上游脚本为源仓自研、无 LICENSE，不 pin；本文件按蒸馏出的规则全新实现，
作为 Prism 在仓的可读性门禁。只报警，不自动改文。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEPTH_SECTIONS = (
    "一句话看透本质",
    "核心架构与主流程",
    "绝妙的设计亮点",
    "潜在坑点与局限性",
)
DEPTH_ENTRY_SECTIONS = ("小白 MVP", "由简入深")

TRANSLATION_CREASE = (
    "正如我们所见",
    "被广泛使用",
    "基于以下原因",
    "基于……的原因",
)

FORBIDDEN_PHRASES = (
    "总（30 秒",
    "分（读者",
    "总（收尾）",
)

FILLERS = ("值得注意的是", "此外，", "至关重要", "深入探讨", "不仅", "而且")
WEAK_MODIFIERS = re.compile(r"(非常|极其|显然)(?=[\u4e00-\u9fff])")
PASSIVE_HINT = re.compile(r"被.{1,12}(发布|完成|实现|采用)")
FORBIDDEN_HEADING = re.compile(r"^##\s*总（|^##\s*分（", re.MULTILINE)

ENGLISH_ALLOW = re.compile(
    r"https?://|github\.com|@[\w-]+|`\S+`|⭐|CLI|API|Markdown|HTML|PNG|JPG|IP|README|OSS|MIT"
)
ENGLISH_LINE = re.compile(r"[A-Za-z]{4,}.*[A-Za-z]{4,}")


def lint_text(text: str, *, strict: bool = True, depth: bool = False) -> list[str]:
    errors: list[str] = []
    if FORBIDDEN_HEADING.search(text):
        errors.append("forbidden heading: 总（ / 分（ literal titles（内部公式标签泄漏）")
    for pat in FORBIDDEN_PHRASES:
        if pat in text:
            errors.append(f"forbidden phrase: {pat}（内部公式标签泄漏）")
    if depth:
        for sec in DEPTH_SECTIONS:
            if sec not in text:
                errors.append(f"depth: missing section heading containing {sec}")
        for sec in DEPTH_ENTRY_SECTIONS:
            if sec not in text:
                errors.append(f"depth: missing entry section containing {sec}")
    for pat in TRANSLATION_CREASE:
        if pat in text:
            errors.append(f"translation crease: {pat}")
    filler_hits = sum(text.count(p) for p in FILLERS)
    if filler_hits >= 3:
        errors.append(f"prose: AI filler phrases count={filler_hits} (此外/值得注意的是/至关重要…)")
    mod_hits = len(WEAK_MODIFIERS.findall(text))
    if mod_hits >= 4:
        errors.append(f"prose: weak modifiers count={mod_hits} (非常/极其/显然)")
    passive_hits = len(PASSIVE_HINT.findall(text))
    if passive_hits >= 1:
        errors.append(f"prose: passive hint count={passive_hits} (被…发布/完成/实现/采用)")
    if strict:
        in_code = False
        for i, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if not stripped or stripped.startswith(("#", "!", "|", ">")):
                continue
            if in_code:
                continue
            # 泄漏判定：整行无中文、含 ≥4 个英文词、且无技术白名单令牌
            if (
                not re.search(r"[\u4e00-\u9fff]", stripped)
                and len(re.findall(r"[A-Za-z]{4,}", stripped)) >= 4
                and not ENGLISH_ALLOW.search(stripped)
            ):
                errors.append(f"line {i}: untranslated English sentence leak")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="可读性检查（Prism 原生）")
    parser.add_argument("path", help="Markdown 或文本文件路径")
    parser.add_argument("--lenient", action="store_true", help="宽松模式（仍报错，仅降低严格度）")
    parser.add_argument("--depth", action="store_true", help="四段式体裁必填段检查")
    args = parser.parse_args()

    try:
        text = Path(args.path).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as e:
        print(f"无法读取稿件。{e}", file=sys.stderr)
        return 2

    errors = lint_text(text, strict=not args.lenient, depth=args.depth)
    if errors:
        for e in errors:
            print(f"readability: {e}", file=sys.stderr)
        return 1
    print(f"readability: ok {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
