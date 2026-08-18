#!/usr/bin/env python3
"""Rewrite humanized asset refs to per-slug render paths: assets/foo -> assets/{slug}/foo."""
from __future__ import annotations

import re
import sys


def rewrite(text: str, slug: str) -> str:
    def repl(m: re.Match[str]) -> str:
        path = m.group(1)
        if path.startswith(f"assets/{slug}/"):
            return m.group(0)
        if not path.startswith("assets/"):
            return m.group(0)
        rest = path[len("assets/") :]
        if rest == "github-trending.png" and slug.startswith("daily-"):
            rest = f"github-trending-{slug.removeprefix('daily-')}.png"
        return f"](assets/{slug}/{rest})"

    return re.sub(r"\]\((assets/[^)]+)\)", repl, text)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: rewrite-render-asset-refs.py SLUG < text", file=sys.stderr)
        return 1
    slug = sys.argv[1]
    text = sys.stdin.read()
    sys.stdout.write(rewrite(text, slug))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
