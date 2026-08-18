"""wechat-card-kit 组件渲染（cards.yaml kit 字段 / markdown :::kit 共用）。

字段说明见 skills/selfmedia-director/references/wechat-image-post-components.md。
所有文本都转义，动画只加 data-motion 属性，由 kit.js 驱动；截图必须等
window.__kitMotionDone === true。
"""

from __future__ import annotations

import html as _html
from typing import Any


def esc(value: Any) -> str:
    return _html.escape(str(value or ""), quote=True)


def _mark(text: str, mark: str | None, cls: str = "kit-mark kit-mark--orange") -> str:
    if not mark or mark not in text:
        return esc(text)
    idx = text.find(mark)
    return (
        esc(text[:idx])
        + f'<mark class="{cls}" data-rough="highlight" data-rough-color="#f3c27a">{esc(mark)}</mark>'
        + esc(text[idx + len(mark) :])
    )


def _title_html(kit: dict[str, Any]) -> str:
    title = str(kit.get("title") or "")
    if not title:
        return ""
    gradient = str(kit.get("title_gradient") or "")
    if gradient and gradient in title:
        idx = title.find(gradient)
        inner = (
            esc(title[:idx])
            + f'<span class="kit-gradient" data-motion="sweep">{esc(gradient)}</span>'
            + esc(title[idx + len(gradient) :])
        )
    else:
        inner = _mark(title, str(kit.get("title_mark") or ""))
    cls = "kit-title kit-title--lg" if kit.get("title_lg") else "kit-title"
    return f'<h1 class="{cls}" data-motion="reveal">{inner}</h1>'


def _subtitle_html(kit: dict[str, Any]) -> str:
    subtitle = str(kit.get("subtitle") or "")
    if not subtitle:
        return ""
    inner = _mark(subtitle, str(kit.get("subtitle_mark") or ""), "kit-mark kit-mark--green")
    return f'<p class="kit-subtitle" data-motion="reveal">{inner}</p>'


def _chips_html(kit: dict[str, Any]) -> str:
    chips = [str(c) for c in (kit.get("chips") or []) if str(c)]
    if not chips:
        return ""
    style = str(kit.get("chip_style") or "outline")
    inner = "".join(
        f'<span class="kit-chip kit-chip--{style}">{esc(c)}</span>' for c in chips[:3]
    )
    return f'<div class="kit-chips" data-motion="stagger">{inner}</div>'


def _stats_html(kit: dict[str, Any]) -> str:
    stats = kit.get("stats") or []
    if not stats:
        return ""
    parts = []
    for stat in stats[:3]:
        number = str(stat.get("number") or "0")
        color = str(stat.get("color") or "blue")
        label = str(stat.get("label") or "")
        parts.append(
            "<div>"
            f'<b class="kit-num kit-num--{color}" data-motion="countup" data-count="{esc(number)}">0</b>'
            f'<span class="kit-num-label">{esc(label)}</span>'
            "</div>"
        )
    return f'<div class="kit-stats" data-motion="stagger" style="display:flex;gap:64px;margin-top:8px;">{"".join(parts)}</div>'


def _timeline_html(kit: dict[str, Any]) -> str:
    items = kit.get("timeline") or []
    if not items:
        return ""
    parts = []
    for item in items[:5]:
        if isinstance(item, dict):
            time = str(item.get("time") or "")
            text = str(item.get("text") or "")
        else:
            raw = str(item)
            time, _, text = raw.partition("|")
        time_html = f'<span class="kit-tl-time">{esc(time)}</span>' if time else ""
        parts.append(f"<li>{time_html}{esc(text)}</li>")
    return f'<ol class="kit-timeline" data-motion="stagger">{"".join(parts)}</ol>'


def _steps_html(kit: dict[str, Any]) -> str:
    steps = [str(s) for s in (kit.get("steps") or []) if str(s)]
    if not steps:
        return ""
    color = str(kit.get("steps_color") or "green")
    inner = "".join(f"<li>{esc(s)}</li>" for s in steps[:5])
    return f'<ol class="kit-steps kit-steps--{color}" data-motion="stagger">{inner}</ol>'


def _checklist_html(kit: dict[str, Any]) -> str:
    items = [str(i) for i in (kit.get("checklist") or []) if str(i)]
    if not items:
        return ""
    cls = "kit-check kit-check--warn" if kit.get("check_warn") else "kit-check"
    inner = "".join(f"<li>{esc(i)}</li>" for i in items[:6])
    return f'<ul class="{cls}" data-motion="stagger">{inner}</ul>'


def _callout_html(kit: dict[str, Any]) -> str:
    callout = kit.get("callout") or {}
    title = str(callout.get("title") or "") if isinstance(callout, dict) else ""
    body = str(callout.get("body") or callout.get("text") or "") if isinstance(callout, dict) else str(callout)
    if not body:
        return ""
    color = str(callout.get("color") or "orange") if isinstance(callout, dict) else "orange"
    title_html = f'<div class="kit-callout-title">{esc(title)}</div>' if title else ""
    return (
        f'<aside class="kit-callout kit-callout--{color}" data-motion="reveal">'
        f"{title_html}<p class=\"kit-callout-body\">{esc(body)}</p></aside>"
    )


def _quote_html(kit: dict[str, Any]) -> str:
    quote = kit.get("quote") or {}
    text = str(quote.get("text") or "") if isinstance(quote, dict) else str(quote)
    if not text:
        return ""
    source = str(quote.get("source") or "") if isinstance(quote, dict) else ""
    src_html = f'<span class="kit-quote-src">{esc(source)}</span>' if source else ""
    return f'<blockquote class="kit-quote" data-motion="reveal">{esc(text)}{src_html}</blockquote>'


def _endcard_html(kit: dict[str, Any]) -> str:
    endcard = kit.get("endcard") or {}
    if not isinstance(endcard, dict):
        return ""
    title = str(endcard.get("title") or "")
    cta = str(endcard.get("cta") or "")
    if not title:
        return ""
    style = "kit-endcard--soft" if endcard.get("soft", True) else "kit-endcard--blue"
    cta_html = f'<span class="kit-endcard-cta">{esc(cta)} <span data-motion="pulse">→</span></span>' if cta else ""
    return (
        f'<div class="kit-endcard {style}" data-motion="reveal">'
        f'<div class="kit-endcard-title">{esc(title)}</div>{cta_html}</div>'
    )


def render_kit_body(kit: dict[str, Any]) -> str:
    """Render T1-T4 components from a kit field dict (no footer)."""
    parts = []
    eyebrow = str(kit.get("eyebrow") or "")
    if eyebrow:
        parts.append(f'<span class="kit-eyebrow" data-motion="reveal">{esc(eyebrow)}</span>')
    parts.append(_title_html(kit))
    parts.append(_subtitle_html(kit))
    parts.append(_chips_html(kit))
    parts.append(_stats_html(kit))
    parts.append(_timeline_html(kit))
    parts.append(_steps_html(kit))
    parts.append(_checklist_html(kit))
    parts.append(_callout_html(kit))
    parts.append(_quote_html(kit))
    parts.append(_endcard_html(kit))
    next_text = str(kit.get("next") or "")
    if next_text:
        parts.append(f'<p class="kit-next" data-motion="reveal">{esc(next_text)}</p>')
    disclaimer = str(kit.get("disclaimer") or "")
    if disclaimer:
        parts.append(f'<p class="kit-disclaimer">{esc(disclaimer)}</p>')
    return "\n".join(p for p in parts if p)


def kit_theme_class(kit: dict[str, Any]) -> str:
    theme = str(kit.get("theme") or "white")
    return f"kit-card--{theme}" if theme in ("white", "paper", "ink") else "kit-card--white"
