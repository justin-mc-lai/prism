#!/usr/bin/env python3
# ATTRIBUTION (A4 MIT): originally pinned from selfmedia-creator scripts/ai_manga_drama.py
# Owner license decision A1/A4: MIT, see docs/owner-license-decision.md + docs/ATTRIBUTION-render-chain.md
# prism-prompt-compiler-v1 (2026-09-21) diverged from the pin: removed all local fallback
# (FFmpeg kenburns synthesis, edge-tts voice, audio mux). assemble now stitches provider clips only.
# See docs/beacon/v0.0.1/change/prism-prompt-compiler-v1.md
"""ai-manga-drama pipeline CLI (v0.0.1 · provider-only, no fallback)."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from drama_spec import validate_drama_spec  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
PIPELINE_DIR = ROOT / "content" / "pipelines" / "ai-manga-drama"
SCHEMA_PATH = PIPELINE_DIR / "storyboard-schema.json"
MASTERS_DIR = ROOT / "content" / "masters" / "ai-manga-drama"
RENDERS_DIR = ROOT / "content" / "renders" / "ai-manga-drama" / "draft"
QA_EVIDENCE_DIR = ROOT / ".beacon" / "evidence" / "qa" / "ai-manga-drama"
AI_LABEL_TEXT = "本内容由人工智能生成"
TARGET_RESOLUTION = (480, 854)

# 渲染阶段 → 凭证环境变量。凭证永不入库（credentials_never_in_repo）。
RENDER_STAGE_ENVS = {
    "t2i": "PRISM_T2I_KEY",
    "i2v": "PRISM_I2V_KEY",
    "t2v": "PRISM_T2V_KEY",
    "tts": "PRISM_TTS_KEY",
}
# 图生/文生视频的既有 provider 凭证别名（兼容旧调用，语义等价）
LEGACY_VIDEO_ENVS = ["FAL_KEY", "REPLICATE_API_TOKEN", "SILICONFLOW_API_KEY"]
# manga_drama 默认链路必需阶段（t2v 为 i2v 的替代，二者满足其一）
REQUIRED_STAGES = ("t2i",)
REQUIRED_VIDEO_STAGES = ("i2v", "t2v")


def ai_label_font() -> str:
    """Resolve a CJK font for the mandatory AI-content label (总局令第16号)."""
    candidates = [os.environ.get("AI_LABEL_FONT")]
    candidates += [
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    ]
    for p in candidates:
        if p and Path(p).is_file():
            return p
    fail("no CJK font found for AI label; set AI_LABEL_FONT")


def make_ai_label_png(path: Path) -> None:
    """Render the mandatory AI-content label as a transparent PNG (drawtext-free)."""
    from PIL import Image, ImageDraw, ImageFont

    font = ImageFont.truetype(ai_label_font(), 26)
    probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    box = probe.textbbox((0, 0), AI_LABEL_TEXT, font=font)
    pad = 12
    img = Image.new("RGBA", (box[2] - box[0] + pad * 2, box[3] - box[1] + pad * 2), (0, 0, 0, 130))
    ImageDraw.Draw(img).text(
        (pad - box[0], pad - box[1]), AI_LABEL_TEXT, font=font, fill=(255, 255, 255, 255)
    )
    img.save(path)


def fail(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"file not found: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid json {path}: {exc}")
    if not isinstance(data, dict):
        fail(f"expected json object: {path}")
    return data


def _check_ref_image(item: dict, label: str, base_dir: Path, errors: list[str]) -> None:
    """ref_image 声明即须解析到真实文件（fail-closed，AC-PPC-003）。"""
    ref = item.get("ref_image")
    if ref in (None, ""):
        return
    if not isinstance(ref, str):
        errors.append(f"{label} ref_image must be a string")
        return
    if not (base_dir / ref).is_file():
        errors.append(f"{label} ref_image not found: {ref}")


def _validate_entities(
    data: dict,
    key: str,
    errors: list[str],
    *,
    kind_enum: tuple[str, ...] = (),
    base_dir: Path | None = None,
) -> set[str]:
    """Validate an optional asset array (characters/scenes/props); return declared ids."""
    items = data.get(key)
    if items is None:
        return set()
    if not isinstance(items, list):
        errors.append(f"{key} must be a list")
        return set()
    ids: list[str] = []
    for i, item in enumerate(items, 1):
        if not isinstance(item, dict):
            errors.append(f"{key}[{i}] must be object")
            continue
        for field in ("id", "name", "traits") + (("kind",) if kind_enum else ()):
            if field not in item:
                errors.append(f"{key}[{i}] missing {field}")
        if kind_enum:
            kind = item.get("kind")
            if kind not in kind_enum:
                errors.append(f"{key}[{i}] kind must be {'|'.join(kind_enum)}, got {kind!r}")
        if base_dir is not None:
            _check_ref_image(item, f"{key}[{i}]", base_dir, errors)
        ids.append(str(item.get("id") or ""))
    if any(not i for i in ids):
        errors.append(f"{key}[].id must be non-empty")
    if len(set(ids)) != len(ids):
        errors.append(f"{key}[].id must be unique")
    return {i for i in ids if i}


def validate_storyboard(storyboard: Path, *, verbose: bool = False) -> dict:
    data = load_json(storyboard)
    schema = load_json(SCHEMA_PATH)
    base_dir = storyboard.parent
    errors: list[str] = []
    required = schema.get("required", [])
    for key in required:
        if key not in data:
            errors.append(f"missing required field: {key}")
    if data.get("ratio") != "9:16":
        errors.append(f"ratio must be 9:16, got {data.get('ratio')}")
    duration = data.get("duration_seconds")
    if not isinstance(duration, int) or not (60 <= duration <= 90):
        errors.append(f"duration_seconds must be int 60-90, got {duration!r}")
    mode = data.get("mode")
    if mode not in ("production", "template"):
        errors.append(f"mode must be production|template, got {mode!r}")
    spec = data.get("spec")
    if spec is not None and spec != "manju-drama":
        errors.append(f"spec must be manju-drama, got {spec!r}")
    character_ids = _validate_entities(data, "characters", errors, base_dir=base_dir)
    scene_ids = _validate_entities(data, "scenes", errors, kind_enum=("interior", "exterior"), base_dir=base_dir)
    prop_ids = _validate_entities(data, "props", errors, base_dir=base_dir)
    for i, prop in enumerate(data.get("props") or [], 1):
        if not isinstance(prop, dict):
            continue
        holder = prop.get("holder")
        if holder and holder not in character_ids:
            errors.append(f"props[{i}] holder {holder!r} not in characters")
    shots = data.get("shots")
    if not isinstance(shots, list) or not shots:
        errors.append("shots must be a non-empty list")
    else:
        if mode == "production":
            lo, hi = (4, 12) if spec == "manju-drama" else (8, 12)
            if not (lo <= len(shots) <= hi):
                errors.append(f"production storyboard requires {lo}-{hi} shots, got {len(shots)}")
        shot_ids = []
        for i, shot in enumerate(shots, 1):
            if not isinstance(shot, dict):
                errors.append(f"shot {i} must be object")
                continue
            for field in ("shot_id", "description", "dialogue", "asset_ref", "duration_seconds"):
                if field not in shot:
                    errors.append(f"shot {i} missing {field}")
            desc = str(shot.get("description") or "")
            if len(desc) < 10:
                errors.append(f"shot {i} description too short (<10 chars)")
            _check_ref_image(shot, f"shot {i}", base_dir, errors)
            scene_ref = shot.get("scene_ref")
            if scene_ref and scene_ref not in scene_ids:
                errors.append(f"shot {i} scene_ref {scene_ref!r} not in scenes")
            prop_refs = shot.get("prop_refs") or []
            if not isinstance(prop_refs, list):
                errors.append(f"shot {i} prop_refs must be a list")
            else:
                for ref in prop_refs:
                    if ref not in prop_ids:
                        errors.append(f"shot {i} prop_ref {ref!r} not in props")
            cast = shot.get("cast") or []
            if not isinstance(cast, list):
                errors.append(f"shot {i} cast must be a list")
            else:
                for ref in cast:
                    if ref not in character_ids:
                        errors.append(f"shot {i} cast {ref!r} not in characters")
            shot_ids.append(str(shot.get("shot_id") or ""))
        if len(set(shot_ids)) != len(shot_ids):
            errors.append("shot_id must be unique")
    # drama-storyboard-spec gate（MJ-*）：spec=manju-drama 时强制，含 beats 结构/音效/站位/特写配比
    drama = validate_drama_spec(data)
    errors.extend(drama["errors"])
    if errors:
        return {"valid": False, "errors": errors}
    if verbose:
        print(
            f"schema_ok shot_count={len(shots)} duration={duration} ratio={data.get('ratio')} "
            f"spec={spec or '-'} characters={len(character_ids)} scenes={len(scene_ids)} props={len(prop_ids)}"
        )
    return {
        "valid": True,
        "errors": [],
        "shot_count": len(shots),
        "duration_seconds": duration,
        "spec": spec,
        "drama_spec": drama["stats"],
        "character_count": len(character_ids),
        "scene_count": len(scene_ids),
        "prop_count": len(prop_ids),
    }


def cmd_init(args: argparse.Namespace) -> None:
    parent = Path(args.dir).expanduser().resolve()
    # Project-root semantics (prism-project-docs-v1 AC-PDO-001): a `docs/prism`
    # target gets the content-isomorphic tree + facade README; the episode then
    # nests at masters/ai-manga-drama/<ep>/ per the directory contract. Any
    # other --dir keeps legacy behavior: episode directly under parent.
    is_project_root = parent.name == "prism" and parent.parent.name == "docs"
    if is_project_root:
        content_root = Path(__file__).resolve().parent.parent / "content"
        if content_root.is_dir():
            # ponytail: single source of truth — mirror content/'s top level
            names = sorted(p.name for p in content_root.iterdir())
        else:
            names = ["briefings", "distribution", "masters", "pipelines", "presentations", "storyworlds"]
        parent.mkdir(parents=True, exist_ok=True)
        for name in names:
            (parent / name).mkdir(exist_ok=True)
        facade = parent / "README.md"
        if not facade.exists():
            facade.write_text(
                "# docs/prism — Prism 作品目录（门面索引）\n\n"
                "本目录由 `ai_manga_drama.py init` 建立，结构与 Prism 仓 `content/` 同构。\n"
                "这里只放作品产物；需求真相在 `docs/beacon/`，两者互不越界。\n\n"
                "| 索引 | 位置 |\n|------|------|\n"
                "| 大纲 / 剧本 | `storyworlds/<world>/episodes/` |\n"
                "| 母稿 | `masters/`（漫剧 episode：`masters/ai-manga-drama/<episode>/`） |\n"
                "| 分镜剧本 | `pipelines/<form>/<slug>/`（`storyboard.json`、`分镜脚本.md`、提示词、srt） |\n"
                "| 简报 | `briefings/` |\n"
                "| 成片 / 发布 | `presentations/`、`distribution/` |\n\n"
                "- 能力面在 Prism 仓：所有命令经 `$PRISM_HOME/scripts/...` 调用，项目内零脚本副本。\n",
                encoding="utf-8",
            )
        episode = parent / "masters" / "ai-manga-drama" / args.episode
    else:
        episode = Path(args.dir).expanduser().resolve() / args.episode
    episode.mkdir(parents=True, exist_ok=True)
    (episode / "assets").mkdir(exist_ok=True)
    (episode / "clips").mkdir(exist_ok=True)
    readme = episode / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# {args.episode}\n\nEpisode skeleton created by `ai_manga_drama.py init`.\n\n"
            "Flow: populate `storyboard.json` (+ `assets/` ref images) → "
            "`prompt_compiler.py` → `request` → provider renders `clips/` → `assemble` → `qa`.\n\n"
            "No local fallback: `assemble` stitches provider clips only; missing clip or credential fails closed.\n",
            encoding="utf-8",
        )
    storyboard = episode / "storyboard.json"
    if not storyboard.exists():
        template = {
            "episode": args.episode,
            "title": "Untitled",
            "ratio": "9:16",
            "duration_seconds": 60,
            "mode": "template",
            "characters": [
                {"id": "hero", "name": "Hero", "traits": "placeholder character traits"}
            ],
            "scenes": [
                {"id": "scene-01", "name": "Scene 1", "kind": "interior", "traits": "placeholder scene traits"}
            ],
            "props": [
                {"id": "prop-01", "name": "Prop 1", "traits": "placeholder prop traits", "holder": "hero"}
            ],
            "shots": [
                {
                    "shot_id": "shot-01",
                    "description": "A single establishing shot placeholder; replace before production.",
                    "dialogue": "",
                    "asset_ref": "assets/panel-01.png",
                    "duration_seconds": 60,
                    "scene_ref": "scene-01",
                    "prop_refs": ["prop-01"],
                }
            ],
        }
        storyboard.write_text(json.dumps(template, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"init": str(episode), "storyboard": str(storyboard), "status": "ok"}, ensure_ascii=False))


def cmd_validate(args: argparse.Namespace) -> None:
    result = validate_storyboard(Path(args.storyboard).expanduser().resolve(), verbose=True)
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    if not result["valid"]:
        fail("; ".join(result["errors"]))


def resolve_stage_credential(stage: str) -> str | None:
    """Return the env var name that carries this stage's credential, else None."""
    primary = RENDER_STAGE_ENVS[stage]
    if os.environ.get(primary):
        return primary
    if stage in ("i2v", "t2v"):
        for legacy in LEGACY_VIDEO_ENVS:
            if os.environ.get(legacy):
                return legacy
    return None


def cmd_request(args: argparse.Namespace) -> None:
    episode_dir = Path(args.episode).expanduser().resolve()
    storyboard_path = episode_dir / "storyboard.json"
    validate_storyboard(storyboard_path)
    storyboard = load_json(storyboard_path)
    shots = storyboard.get("shots") or []

    stages = []
    for stage in ("t2i", "i2v", "t2v", "tts"):
        env = resolve_stage_credential(stage)
        stages.append(
            {
                "stage": stage,
                "credential_env": env or RENDER_STAGE_ENVS[stage],
                "status": "READY" if env else "BLOCKED:missing_credential",
            }
        )
    stage_status = {s["stage"]: s["status"] for s in stages}
    missing = [s for s in REQUIRED_STAGES if stage_status[s] != "READY"]
    if not any(stage_status[s] == "READY" for s in REQUIRED_VIDEO_STAGES):
        missing.append("i2v|t2v")

    segment_cap = 30.0
    segments = []
    current = {"shots": [], "seconds": 0.0}
    for shot in shots:
        seconds = float(shot.get("duration_seconds") or 0)
        if current["seconds"] + seconds > segment_cap and current["shots"]:
            segments.append(current)
            current = {"shots": [], "seconds": 0.0}
        current["shots"].append(shot["shot_id"])
        current["seconds"] += seconds
    if current["shots"]:
        segments.append(current)

    request_payload = {
        "episode": storyboard.get("episode"),
        "ratio": "9:16",
        "resolution": "480p",
        "mode": "provider-only",
        "stages": stages,
        "segments": [
            {
                "segment_order": i + 1,
                "shot_ids": seg["shots"],
                "approximate_seconds": round(seg["seconds"], 1),
            }
            for i, seg in enumerate(segments)
        ],
        "references": {
            "images": [shot.get("ref_image") or shot["asset_ref"] for shot in shots],
            "audio": [],
            "video": [],
        },
        "prompt_artifacts": {
            "assets": "资产提示词.md",
            "image": "图片提示词.md",
            "video": "视频提示词.md",
        },
    }
    out = Path(args.out).expanduser().resolve() if args.out else episode_dir / "render-request.json"
    out.write_text(json.dumps(request_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest = {
        "mode": "provider-only",
        "status": "READY" if not missing else "BLOCKED:missing_credential",
        "missing_stages": missing,
        "stages": stages,
        "release_gate": "pending_human",
        "request_ref": str(out),
    }
    (episode_dir / "video-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False))
    if missing:
        fail(
            "missing render provider credential(s): "
            + ", ".join(missing)
            + "; no fallback, no fake video generated",
            code=2,
        )


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return float(out)


def _probe_resolution(path: Path) -> tuple[int, int]:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
         "-of", "csv=p=0", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    parts = out.split(",")
    return int(parts[0]), int(parts[1])


def required_clip_paths(episode_dir: Path, shots: list[dict]) -> list[Path]:
    return [episode_dir / "clips" / f"{shot.get('shot_id')}.mp4" for shot in shots]


def cmd_assemble(args: argparse.Namespace) -> None:
    """Stitch provider-rendered clips only. No synthesis, no fallback (AC-PPC-005)."""
    episode_dir = Path(args.episode).expanduser().resolve()
    storyboard_path = episode_dir / "storyboard.json"
    validate_storyboard(storyboard_path)
    storyboard = load_json(storyboard_path)
    shots = storyboard.get("shots") or []

    # 1. 未过编译器不得进 assemble（illegal transition）
    for artifact in ("资产提示词.md", "图片提示词.md", "视频提示词.md"):
        if not (episode_dir / artifact).is_file():
            fail(f"prompt compiler artifact missing: {artifact}; run prompt_compiler.py first", code=2)

    # 2. provider 片段必须齐全（缺任一即 fail-closed，不合成替代品）
    clips = required_clip_paths(episode_dir, shots)
    missing_clips = [str(p) for p in clips if not p.is_file()]
    if missing_clips:
        fail(
            "provider clips missing; no fallback synthesis: " + json.dumps(missing_clips, ensure_ascii=False),
            code=2,
        )

    # 3. 片段规格必须达标（分辨率），否则拒绝拼接而不是偷偷缩放
    bad_specs = []
    for clip, shot in zip(clips, shots):
        try:
            w, h = _probe_resolution(clip)
        except (subprocess.CalledProcessError, ValueError) as exc:
            bad_specs.append({"clip": str(clip), "error": str(exc)})
            continue
        if (w, h) != TARGET_RESOLUTION:
            bad_specs.append({"clip": str(clip), "resolution": f"{w}x{h}", "expected": "480x854"})
    if bad_specs:
        fail("provider clips do not match 480x854; re-render instead of rescaling: "
             + json.dumps(bad_specs, ensure_ascii=False), code=2)

    out = (
        Path(args.out).expanduser().resolve()
        if args.out
        else RENDERS_DIR / f"{storyboard.get('episode')}-480p.mp4"
    )
    out.parent.mkdir(parents=True, exist_ok=True)

    tmpdir = Path(tempfile.mkdtemp(prefix="amd-assemble-"))
    try:
        concat_list = tmpdir / "concat.txt"
        concat_list.write_text("\n".join(f"file '{c.resolve()}'" for c in clips) + "\n", encoding="utf-8")
        concatenated = tmpdir / "concat.mp4"
        subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(concatenated)],
            check=True,
            capture_output=True,
        )

        # Mandatory AI-content label (总局令第16号): burn once over the full cut.
        label_png = tmpdir / "ai-label.png"
        make_ai_label_png(label_png)
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(concatenated), "-i", str(label_png),
                "-filter_complex", "overlay=(W-w)/2:24",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "28",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out),
            ],
            check=True,
            capture_output=True,
        )
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    manifest_path = episode_dir / "video-manifest.json"
    manifest = load_json(manifest_path) if manifest_path.exists() else {}
    manifest.update(
        {
            "mode": "provider-only",
            "status": "STITCHED_PROVIDER_CLIPS",
            "output": str(out),
            "release_gate": "pending_human",
            "clips": [str(c) for c in clips],
        }
    )
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "STITCHED_PROVIDER_CLIPS", "output": str(out), "clips": len(clips)}, ensure_ascii=False))


def _ffprobe(path: Path) -> dict:
    width = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    duration = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    parts = width.split(",")
    return {"width": int(parts[0]), "height": int(parts[1]), "duration_seconds": float(duration)}


def cmd_qa(args: argparse.Namespace) -> None:
    episode_dir = Path(args.episode).expanduser().resolve()
    results: dict[str, dict] = {}
    ok = True

    storyboard_path = episode_dir / "storyboard.json"
    storyboard = load_json(storyboard_path)
    storyboard_check = validate_storyboard(storyboard_path)
    results["storyboard_schema"] = {"pass": storyboard_check["valid"], "errors": storyboard_check["errors"]}
    ok = ok and storyboard_check["valid"]

    missing_assets = [
        str(shot.get("asset_ref"))
        for shot in (storyboard.get("shots") or [])
        if not (episode_dir / str(shot.get("asset_ref") or "")).is_file()
    ]
    results["asset_refs"] = {"pass": not missing_assets, "missing": missing_assets}
    ok = ok and not missing_assets

    # 编译器产物必须在场（provider-only 链路的前置文本）
    artifacts = ("资产提示词.md", "图片提示词.md", "视频提示词.md")
    missing_artifacts = [a for a in artifacts if not (episode_dir / a).is_file()]
    results["prompt_artifacts"] = {"pass": not missing_artifacts, "missing": missing_artifacts}
    ok = ok and not missing_artifacts

    render = RENDERS_DIR / f"{storyboard.get('episode')}-480p.mp4"
    results["output_exists"] = {"pass": render.is_file() and render.stat().st_size > 0, "path": str(render)}
    ok = ok and render.is_file() and render.stat().st_size > 0

    if render.is_file() and render.stat().st_size > 0:
        try:
            probe = _ffprobe(render)
            duration_ok = 60 <= probe["duration_seconds"] <= 90
            resolution_ok = probe["width"] == 480 and probe["height"] == 854
            results["timing"] = {"pass": duration_ok, "duration_seconds": probe["duration_seconds"]}
            results["resolution"] = {"pass": resolution_ok, "width": probe["width"], "height": probe["height"]}
            ok = ok and duration_ok and resolution_ok
        except (subprocess.CalledProcessError, ValueError) as exc:
            results["probe"] = {"pass": False, "error": str(exc)}
            ok = False

    ledger_path = episode_dir / "cost-ledger.json"
    if ledger_path.is_file():
        try:
            ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
            ledger_ok = isinstance(ledger, list) and len(ledger) > 0 and all(
                e.get("provider") and e.get("status") for e in ledger
            )
            results["cost_ledger"] = {"pass": ledger_ok, "entries": len(ledger) if isinstance(ledger, list) else 0}
            ok = ok and ledger_ok
        except json.JSONDecodeError as exc:
            results["cost_ledger"] = {"pass": False, "error": str(exc)}
            ok = False
    else:
        results["cost_ledger"] = {"pass": False, "error": "cost-ledger.json missing"}
        ok = False

    manifest_path = episode_dir / "video-manifest.json"
    manifest: dict = {}
    if manifest_path.is_file():
        manifest = load_json(manifest_path)
        gate_ok = str(manifest.get("release_gate")) == "pending_human"
        status_ok = str(manifest.get("status")).startswith(("STITCHED_", "READY", "BLOCKED:"))
        mode_ok = str(manifest.get("mode")) == "provider-only"
        results["video_manifest"] = {"pass": gate_ok and status_ok and mode_ok, "manifest": manifest}
        ok = ok and gate_ok and status_ok and mode_ok
    else:
        results["video_manifest"] = {"pass": False, "error": "video-manifest.json missing"}
        ok = False

    # provider-only 反断言：manifest 不得声称任何本地兜底 provider
    banned = ("ffmpeg-kenburns", "edge-tts", "kenburns")
    declared_provider = str(manifest.get("provider") or "")
    fallback_free = not any(b in declared_provider.lower() for b in banned)
    results["no_local_fallback"] = {"pass": fallback_free, "provider": declared_provider}
    ok = ok and fallback_free

    QA_EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    scorecard = {
        "schema_version": "1.0",
        "feature": "ai-manga-drama",
        "episode": storyboard.get("episode"),
        "status": "pass" if ok else "fail",
        "checks": results,
        "at": __import__("datetime").datetime.now().isoformat(),
    }
    score_path = QA_EVIDENCE_DIR / "SCORECARD.json"
    score_path.write_text(json.dumps(scorecard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(scorecard, ensure_ascii=False))
    if not ok:
        fail("qa checks failed")


def cmd_manifest(args: argparse.Namespace) -> None:
    episode_dir = Path(args.episode).expanduser().resolve()
    manifest_path = episode_dir / "video-manifest.json"
    if not manifest_path.is_file():
        fail(f"manifest missing: {manifest_path}")
    print(json.dumps(load_json(manifest_path), ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="ai-manga-drama pipeline CLI (provider-only, no fallback)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="create episode skeleton")
    p_init.add_argument("--episode", required=True)
    p_init.add_argument("--dir", required=True)
    p_init.set_defaults(func=cmd_init)

    p_val = sub.add_parser("validate", help="validate storyboard against schema (+ ref_image existence)")
    p_val.add_argument("--storyboard", required=True)
    p_val.add_argument("--json", action="store_true")
    p_val.set_defaults(func=cmd_validate)

    p_req = sub.add_parser("request", help="build provider render request or fail closed")
    p_req.add_argument("--episode", required=True)
    p_req.add_argument("--out", default="")
    p_req.set_defaults(func=cmd_request)

    p_asm = sub.add_parser("assemble", help="stitch provider clips (no synthesis, no fallback)")
    p_asm.add_argument("--episode", required=True)
    p_asm.add_argument("--out", default="")
    p_asm.set_defaults(func=cmd_assemble)

    p_qa = sub.add_parser("qa", help="run provider-only QA checks")
    p_qa.add_argument("--episode", required=True)
    p_qa.set_defaults(func=cmd_qa)

    p_man = sub.add_parser("manifest", help="print episode manifest")
    p_man.add_argument("--episode", required=True)
    p_man.set_defaults(func=cmd_manifest)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
