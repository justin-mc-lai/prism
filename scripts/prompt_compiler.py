#!/usr/bin/env python3
# ATTRIBUTION: Prism-native (prism-prompt-compiler-v1, 2026-09-21).
# Judgment frameworks distilled from vendor/skills/onlyshot (MIT) + alibaba/lumenx (MIT):
#   skills/prism-director/references/asset-prompt-templates.md  (7-段 identity block, 五类资产)
#   skills/prism-director/references/prompt-syntax-table.md     (§1 字段定式, §2 8 段定式)
# License/attribution: docs/ATTRIBUTION-drama-prompt-repos.md
"""Deterministic prompt compiler: storyboard.json + style preset -> text prompt artifacts.

Outputs (all inside the episode dir):
  资产提示词.md   asset ref prompts (T2I, one per identity)
  图片提示词.md   per-shot image prompts (I2I / T2I)
  视频提示词.md   per-shot video prompts (I2V / T2V)
  {episode}.srt   subtitle sidecar from dialogue + shot durations

Determinism contract: same storyboard + same style => byte-identical output.
No timestamps, no randomness, no environment reads enter the artifacts.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ai_manga_drama import load_json, validate_storyboard  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OVERLAY = ROOT / "registry" / "style-presets.yaml"
BASE = ROOT / "content" / "pipelines" / "ai-manga-drama" / "lumenx-style-presets.json"

# 戏剧光关键词：ref 阶段必须剔除（asset-prompt-templates.md §1 两层分离）
DRAMA_LIGHT_TOKENS = [
    "cinematic lighting", "lens flare", "chiaroscuro", "dramatic backlight",
    "dramatic rim lighting", "dramatic lighting", "volumetric fog", "neon",
    "glossy render", "harsh studio flash",
]

CLASS_LAYOUT = {
    "character": (
        "4-grid character reference sheet, "
        "quadrants: top-left front view, top-right 3/4 right, bottom-left 3/4 left, bottom-right back view, "
        "identical character in all 4 quadrants, "
        "NO text labels, NO annotations, NO watermarks, NO grid view labels"
    ),
    "creature": (
        "4-grid creature reference sheet, "
        "quadrants: front view, side view, back view, key-feature macro, "
        "human silhouette scale bar in each quadrant, NO text labels, NO watermarks"
    ),
    "crowd": (
        "single wide crowd composition, depth layers front/mid/back, "
        "NO text labels, NO watermarks, NO dominant hero character"
    ),
    "scene": (
        "4-grid location reference sheet, "
        "quadrants: top-left wide establishing, top-right entrance angle, "
        "bottom-left key furniture close-up, bottom-right opposite view, "
        "consistent lighting and palette in all 4, NO text labels, NO watermarks"
    ),
    "prop": (
        "4-grid product reference sheet on white background, "
        "quadrants: front view, 45-degree side, back view, macro detail, "
        "NO text labels, NO annotations, NO watermarks, NO hands"
    ),
}

CLASS_DESIGN_LABEL = {
    "character": "fixed character design",
    "creature": "fixed creature design",
    "crowd": "fixed crowd design",
    "scene": "fixed location design",
    "prop": "fixed prop design",
}


def ref_safe_style(positive: str) -> str:
    """Strip drama-light tokens from a style string (ref layer must stay neutral)."""
    out = positive
    for token in DRAMA_LIGHT_TOKENS:
        # case-insensitive removal of the token and any trailing comma/space
        lowered = out.lower()
        idx = lowered.find(token)
        while idx != -1:
            end = idx + len(token)
            while end < len(out) and out[end] in " ,":
                end += 1
            out = out[:idx] + out[end:]
            lowered = out.lower()
            idx = lowered.find(token)
    parts = [p.strip() for p in out.split(",")]
    return ", ".join(p for p in parts if p)


def load_presets() -> dict[str, dict]:
    """Merge overlay (registry/style-presets.yaml) over base (lumenx verbatim). Ids must not collide."""
    presets: dict[str, dict] = {}
    base = json.loads(BASE.read_text(encoding="utf-8"))
    for p in base["presets"]:
        presets[p["id"]] = p
    overlay = yaml.safe_load(OVERLAY.read_text(encoding="utf-8"))
    for p in overlay.get("presets", []):
        if p["id"] in presets:
            raise SystemExit(f"ERROR: style preset id collision base/overlay: {p['id']}")
        presets[p["id"]] = p
    return presets


def asset_class(item: dict, default: str) -> str:
    traits = str(item.get("traits") or "")
    if traits.startswith("[creature]"):
        return "creature"
    if traits.startswith("[crowd]"):
        return "crowd"
    return default


def asset_prompt(item: dict, kind: str, preset: dict) -> str:
    cls = asset_class(item, kind)
    layout = CLASS_LAYOUT[cls]
    design = CLASS_DESIGN_LABEL[cls]
    traits = str(item.get("traits") or "").replace("[creature]", "").replace("[crowd]", "").strip()
    style = ref_safe_style(str(preset.get("positive_prompt") or ""))
    negative = str(preset.get("negative_prompt") or "")
    aid = str(item.get("id"))
    lines = [
        f"[IDENTITY] {aid}, {design}, must remain consistent across all generations,",
        f"[BODY] {traits or '<traits 未提供>'},",
        f"[LAYOUT] {layout},",
        f"[STYLE] {style}, neutral studio lighting flat even,",
        f"[NEGATIVE] {negative}",
    ]
    return "\n".join(lines)


def _ref_tag(path: str | None, label: str) -> str:
    if not path:
        return f"({label}: <未提供参考图>)"
    return f"(@{path}) same identity, {label}"


def image_prompt(
    shot: dict,
    storyboard: dict,
    preset: dict,
    by_id: dict[str, dict],
    ref_to_name: dict[str, str],
) -> str:
    style = ref_safe_style(str(preset.get("positive_prompt") or ""))
    negative = str(preset.get("negative_prompt") or "")
    ref = shot.get("ref_image") or shot.get("asset_ref")
    # 只标本镜实际引用的实体，不列全角色（避免误导 provider 同框多主体）
    subject = ref_to_name.get(str(ref or ""), "<未解析到资产条目>")
    scene = by_id.get(str(shot.get("scene_ref") or ""), {})
    props = [by_id.get(str(p), {}) for p in (shot.get("prop_refs") or [])]
    scene_label = str(scene.get("name") or "未指定")
    scene_traits = str(scene.get("traits") or "未指定")
    scene_variant = str(scene.get("variant") or "未指定")
    prop_traits = "; ".join(str(p.get("traits") or "") for p in props if p) or "无"
    dialogue = str(shot.get("dialogue") or "").strip() or "无"
    lines = [
        f"[CHARACTER] {_ref_tag(ref, subject)}",
        f"[BACKGROUND] {scene_label}: {scene_traits}",
        f"[ACTION] {shot.get('description')}",
        f"[SCENE] props: {prop_traits}",
        f"[CAMERA] <storyboard description 内含镜头语言；未单列>",
        f"[LIGHT] scene variant: {scene_variant}",
        f"[TEXT] {dialogue}",
        f"[STYLE] {style}, neutral studio lighting flat even",
        f"[NEGATIVE] {negative}",
    ]
    return "\n".join(lines)


def video_prompt(shot: dict, preset: dict) -> str:
    style = str(preset.get("positive_prompt") or "")
    negative = str(preset.get("negative_prompt") or "")
    dialogue = str(shot.get("dialogue") or "").strip()
    lines = [
        f"[SHOT] {shot.get('shot_id')}, {shot.get('duration_seconds')}s",
        f"[ACTION] {shot.get('description')}",
        f"[DIALOGUE] {dialogue or '无'}",
        f"[AUDIO] <由下游 provider 依据 dialogue 合成；Prism 不本地生成音频>",
        f"[STYLE] {style}",
        f"[NEGATIVE] {negative}",
    ]
    return "\n".join(lines)


def _srt_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int(seconds % 3600 // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def build_srt(shots: list[dict]) -> str:
    blocks: list[str] = []
    cursor = 0.0
    for shot in shots:
        start = cursor
        cursor += float(shot.get("duration_seconds") or 0)
        text = str(shot.get("dialogue") or "").strip()
        if not text:
            continue
        blocks.append(f"{len(blocks) + 1}\n{_srt_ts(start)} --> {_srt_ts(max(start, cursor - 0.05))}\n{text}\n")
    return "\n".join(blocks)


def compile_episode(episode_dir: Path, style_id: str) -> dict[str, Path]:
    storyboard_path = episode_dir / "storyboard.json"
    result = validate_storyboard(storyboard_path)
    if not result["valid"]:
        raise SystemExit("ERROR: storyboard invalid: " + "; ".join(result["errors"]))
    storyboard = load_json(storyboard_path)
    presets = load_presets()
    if style_id not in presets:
        raise SystemExit(f"ERROR: unknown style preset: {style_id} (available: {len(presets)})")
    preset = presets[style_id]

    characters = storyboard.get("characters") or []
    scenes = storyboard.get("scenes") or []
    props = storyboard.get("props") or []
    by_id = {str(i.get("id")): i for i in [*characters, *scenes, *props]}
    # ref_image 路径 → 实体名（用于把每镜解析到具体主体）
    ref_to_name: dict[str, str] = {}
    for item in [*characters, *scenes, *props]:
        ref = item.get("ref_image")
        if ref:
            ref_to_name[str(ref)] = str(item.get("name") or item.get("id"))

    ep = storyboard.get("episode")
    style_name = f"{preset.get('name_zh') or preset.get('name')} ({style_id})"

    asset_lines = [
        f"# 资产提示词 — {ep}",
        "",
        f"风格预设：{style_name}",
        "",
        "> 中性平光、身份块逐字复用；本文件为 T2I 资产层输入，禁戏剧光与剧情情绪。",
        "> 生成后把图回填到对应条目的 `ref_image`，再进分镜编译。",
        "",
    ]
    for kind, items in (("character", characters), ("scene", scenes), ("prop", props)):
        for item in items:
            asset_lines += [
                f"## {item.get('id')} — {item.get('name')}",
                "",
                f"- ref_image: `{item.get('ref_image') or '<待生成并回填>'}`",
                "",
                "```text",
                asset_prompt(item, kind, preset),
                "```",
                "",
            ]

    image_lines = [f"# 图片提示词 — {ep}", "", f"风格预设：{style_name}", ""]
    for shot in storyboard.get("shots") or []:
        image_lines += [
            f"## {shot.get('shot_id')}（{shot.get('duration_seconds')}s）",
            "",
            "```text",
            image_prompt(shot, storyboard, preset, by_id, ref_to_name),
            "```",
            "",
        ]

    video_lines = [f"# 视频提示词 — {ep}", "", f"风格预设：{style_name}", ""]
    for shot in storyboard.get("shots") or []:
        video_lines += [
            f"## {shot.get('shot_id')}（{shot.get('duration_seconds')}s）",
            "",
            "```text",
            video_prompt(shot, preset),
            "```",
            "",
        ]

    outputs = {
        "assets": episode_dir / "资产提示词.md",
        "image": episode_dir / "图片提示词.md",
        "video": episode_dir / "视频提示词.md",
        "srt": episode_dir / f"{ep}.srt",
    }
    outputs["assets"].write_text("\n".join(asset_lines).rstrip() + "\n", encoding="utf-8")
    outputs["image"].write_text("\n".join(image_lines).rstrip() + "\n", encoding="utf-8")
    outputs["video"].write_text("\n".join(video_lines).rstrip() + "\n", encoding="utf-8")
    outputs["srt"].write_text(build_srt(storyboard.get("shots") or []), encoding="utf-8")
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="deterministic prompt compiler (storyboard + style -> text prompts)")
    parser.add_argument("--episode", required=True, help="episode directory containing storyboard.json")
    parser.add_argument("--style", required=True, help="style preset id (registry/style-presets.yaml + lumenx base)")
    parser.add_argument("--list-styles", action="store_true", help="list available preset ids and exit")
    args = parser.parse_args()

    if args.list_styles:
        for pid in sorted(load_presets()):
            print(pid)
        return

    outputs = compile_episode(Path(args.episode).expanduser().resolve(), args.style)
    print(json.dumps({k: str(v) for k, v in outputs.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
