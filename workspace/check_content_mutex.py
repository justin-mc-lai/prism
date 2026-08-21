#!/usr/bin/env python3
"""L3 母稿互斥校验（sot-layering-decision.md D2）。

同名 {vertical}/{slug} 母稿禁止在 Prism 与 selfmedia-creator 两侧同时可写；
例外必须在 EXCEPTIONS 里写明理由。exit 0 = 通过，exit 1 = 存在违规。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_CREATOR = Path(__file__).resolve().parents[2] / "selfmedia-creator"

# key = "{group}/{slug}"；reason 必须可审计，禁止空理由豁免。
EXCEPTIONS: dict[str, str] = {
    "oss-picks/anydoc": "pre-split 历史副本：Prism 为唯一写入口（D2），源仓副本只读待清理",
}


def collect_slugs(masters_dir: Path) -> set[str]:
    """收集 {masters}/{group}/{slug} 两层结构的 slug（跳过 _ 开头与隐藏目录）。"""
    slugs: set[str] = set()
    if not masters_dir.is_dir():
        return slugs
    for group in sorted(masters_dir.iterdir()):
        if not group.is_dir() or group.name.startswith(("_", ".")):
            continue
        for slug_dir in sorted(group.iterdir()):
            if slug_dir.is_dir() and not slug_dir.name.startswith((".", "_")):
                slugs.add(f"{group.name}/{slug_dir.name}")
    return slugs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prism-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--creator-root", type=Path, default=DEFAULT_CREATOR)
    args = parser.parse_args()

    prism_slugs = collect_slugs(args.prism_root / "content" / "masters")
    creator_slugs = collect_slugs(args.creator_root / "content" / "masters")
    collisions = sorted(prism_slugs & creator_slugs)

    unexcepted = [c for c in collisions if c not in EXCEPTIONS]
    stale_exceptions = [k for k in EXCEPTIONS if k not in collisions]

    print(f"prism masters:   {len(prism_slugs)} slugs ({args.prism_root})")
    print(f"creator masters: {len(creator_slugs)} slugs ({args.creator_root})")
    for c in collisions:
        mark = "EXEMPT" if c in EXCEPTIONS else "VIOLATION"
        print(f"  [{mark}] {c}" + (f" — {EXCEPTIONS[c]}" if c in EXCEPTIONS else ""))

    failed = False
    if unexcepted:
        print(f"FAIL: {len(unexcepted)} 处双仓可写冲突，按 D2 指定唯一写入口或删除一侧")
        failed = True
    for k in stale_exceptions:
        print(f"WARN: 例外 {k} 已无对应冲突，请从 EXCEPTIONS 移除")
    if not failed:
        print("mutex: ok")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
