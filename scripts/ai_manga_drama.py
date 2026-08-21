#!/usr/bin/env python3
# ATTRIBUTION (A4 MIT): pinned from selfmedia-creator@07aed5f scripts/ai_manga_drama.py
# Owner license decision A1/A4: MIT, see docs/owner-license-decision.md + docs/ATTRIBUTION-render-chain.md
"""ai-manga-drama pipeline CLI (v0.0.5 R1)."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PIPELINE_DIR = ROOT / "content" / "pipelines" / "ai-manga-drama"
SCHEMA_PATH = PIPELINE_DIR / "storyboard-schema.json"
MASTERS_DIR = ROOT / "content" / "masters" / "ai-manga-drama"
RENDERS_DIR = ROOT / "content" / "renders" / "ai-manga-drama" / "draft"
QA_EVIDENCE_DIR = ROOT / ".beacon" / "evidence" / "qa" / "ai-manga-drama"
VIDEO_PROVIDER_ENVS = ["FAL_KEY", "REPLICATE_API_TOKEN", "SILICONFLOW_API_KEY"]


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


def validate_storyboard(storyboard: Path, *, verbose: bool = False) -> dict:
    data = load_json(storyboard)
    schema = load_json(SCHEMA_PATH)
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
    shots = data.get("shots")
    if not isinstance(shots, list) or not shots:
        errors.append("shots must be a non-empty list")
    else:
        if mode == "production" and not (8 <= len(shots) <= 12):
            errors.append(f"production storyboard requires 8-12 shots, got {len(shots)}")
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
            shot_ids.append(str(shot.get("shot_id") or ""))
        if len(set(shot_ids)) != len(shot_ids):
            errors.append("shot_id must be unique")
    if errors:
        return {"valid": False, "errors": errors}
    if verbose:
        print(f"schema_ok shot_count={len(shots)} duration={duration} ratio={data.get('ratio')}")
    return {"valid": True, "errors": [], "shot_count": len(shots), "duration_seconds": duration}


def cmd_init(args: argparse.Namespace) -> None:
    parent = Path(args.dir).expanduser().resolve()
    episode = parent / args.episode
    episode.mkdir(parents=True, exist_ok=True)
    assets = episode / "assets"
    assets.mkdir(exist_ok=True)
    readme = episode / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# {args.episode}\n\nEpisode skeleton created by `ai_manga_drama.py init`.\n\n"
            "Populate `storyboard.json`, `assets/`, `cost-ledger.json`, then run request/assemble/qa.\n",
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
            "characters": [{"id": "hero", "name": "Hero", "traits": "placeholder character traits"}],
            "shots": [
                {
                    "shot_id": "shot-01",
                    "description": "A single establishing shot placeholder; replace before production.",
                    "dialogue": "",
                    "asset_ref": "assets/panel-01.png",
                    "duration_seconds": 60,
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


def find_video_provider() -> str | None:
    for name in VIDEO_PROVIDER_ENVS:
        if os.environ.get(name):
            return name
    return None


def cmd_request(args: argparse.Namespace) -> None:
    episode_dir = Path(args.episode).expanduser().resolve()
    storyboard_path = episode_dir / "storyboard.json"
    validate_storyboard(storyboard_path)
    storyboard = load_json(storyboard_path)
    shots = storyboard.get("shots") or []
    provider = find_video_provider()
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
        "provider": "seedance-2.5" if provider else "seedance-2.5",
        "mode": "reference-to-video" if provider else "unavailable",
        "episode": storyboard.get("episode"),
        "ratio": "9:16",
        "resolution": "480p",
        "segments": [
            {
                "segment_order": i + 1,
                "shot_ids": seg["shots"],
                "approximate_seconds": round(seg["seconds"], 1),
            }
            for i, seg in enumerate(segments)
        ],
        "references": {
            "images": [shot["asset_ref"] for shot in shots],
            "audio": [],
            "video": [],
        },
    }
    out = Path(args.out).expanduser().resolve() if args.out else episode_dir / "video-request.json"
    out.write_text(json.dumps(request_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "provider": "seedance-2.5",
        "status": "READY" if provider else "BLOCKED:missing_credential",
        "provider_env": provider or "",
        "fallback": "kenburns" if not provider else "",
        "release_gate": "pending_human",
        "request_ref": str(out),
    }
    (episode_dir / "video-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False))
    if not provider:
        fail("missing video provider credential; no fake video generated", code=2)


def cmd_assemble(args: argparse.Namespace) -> None:
    if args.mode != "kenburns":
        fail(f"unsupported assemble mode: {args.mode}")
    episode_dir = Path(args.episode).expanduser().resolve()
    storyboard_path = episode_dir / "storyboard.json"
    validate_storyboard(storyboard_path)
    storyboard = load_json(storyboard_path)
    shots = storyboard.get("shots") or []
    out = (
        Path(args.out).expanduser().resolve()
        if args.out
        else RENDERS_DIR / f"{storyboard.get('episode')}-480p.mp4"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    tmpdir = Path(tempfile.mkdtemp(prefix="amd-assemble-"))
    segments: list[Path] = []
    try:
        for i, shot in enumerate(shots, 1):
            asset = episode_dir / str(shot["asset_ref"])
            if not asset.is_file():
                fail(f"asset missing: {asset}")
            seg = tmpdir / f"seg-{i:02d}.mp4"
            duration = float(shot.get("duration_seconds") or 0)
            vf = (
                "scale=480:854:force_original_aspect_ratio=increase,crop=480:854,"
                "zoompan=z='min(zoom+0.0012,1.15)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=480x854:fps=24"
            )
            cmd = [
                "ffmpeg", "-y", "-loop", "1", "-t", f"{duration:.2f}", "-i", str(asset),
                "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "28",
                "-pix_fmt", "yuv420p", "-r", "24", str(seg),
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            segments.append(seg)
        concat_list = tmpdir / "concat.txt"
        concat_list.write_text(
            "\n".join(f"file '{seg.resolve()}'" for seg in segments) + "\n", encoding="utf-8"
        )
        subprocess.run(
            [
                "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
                "-c", "copy", "-movflags", "+faststart", str(out),
            ],
            check=True,
            capture_output=True,
        )
    finally:
        import shutil

        shutil.rmtree(tmpdir, ignore_errors=True)
    manifest_path = episode_dir / "video-manifest.json"
    if manifest_path.exists():
        manifest = load_json(manifest_path)
    else:
        manifest = {}
    manifest.update(
        {
            "provider": "ffmpeg-kenburns",
            "status": "DRAFT_KENBURNS",
            "output": str(out),
            "release_gate": "pending_human",
        }
    )
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "DRAFT_KENBURNS", "output": str(out)}, ensure_ascii=False))


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
    if manifest_path.is_file():
        manifest = load_json(manifest_path)
        gate_ok = str(manifest.get("release_gate")) == "pending_human"
        status_ok = str(manifest.get("status")).startswith(("DRAFT_", "READY", "BLOCKED:"))
        results["video_manifest"] = {"pass": gate_ok and status_ok, "manifest": manifest}
        ok = ok and gate_ok and status_ok
    else:
        results["video_manifest"] = {"pass": False, "error": "video-manifest.json missing"}
        ok = False

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
    parser = argparse.ArgumentParser(description="ai-manga-drama pipeline CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="create episode skeleton")
    p_init.add_argument("--episode", required=True)
    p_init.add_argument("--dir", required=True)
    p_init.set_defaults(func=cmd_init)

    p_val = sub.add_parser("validate", help="validate storyboard against schema")
    p_val.add_argument("--storyboard", required=True)
    p_val.add_argument("--json", action="store_true")
    p_val.set_defaults(func=cmd_validate)

    p_req = sub.add_parser("request", help="build Seedance 2.5 request or fail closed")
    p_req.add_argument("--episode", required=True)
    p_req.add_argument("--out", default="")
    p_req.set_defaults(func=cmd_request)

    p_asm = sub.add_parser("assemble", help="assemble draft video")
    p_asm.add_argument("--episode", required=True)
    p_asm.add_argument("--mode", default="kenburns")
    p_asm.add_argument("--out", default="")
    p_asm.set_defaults(func=cmd_assemble)

    p_qa = sub.add_parser("qa", help="run five-category QA")
    p_qa.add_argument("--episode", required=True)
    p_qa.set_defaults(func=cmd_qa)

    p_man = sub.add_parser("manifest", help="print episode manifest")
    p_man.add_argument("--episode", required=True)
    p_man.set_defaults(func=cmd_manifest)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
