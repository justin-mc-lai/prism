#!/usr/bin/env python3
# ATTRIBUTION: Prism-native (prism-drama-storyboard-spec-v1, 2026-09-29).
# Judgment framework distilled from a community 神魔修仙漫剧分镜填写规范 (unvendored; see
# docs/ATTRIBUTION-drama-prompt-repos.md §补充来源). Rules are referenced by MJ-* ids in
# skills/prism-director/references/drama-storyboard-spec.md; gate in
# contracts/drama-storyboard-spec.contract.md.
"""Deterministic drama-storyboard-spec gate (MJ-* rules).

Usage:
  python3 scripts/drama_spec.py --storyboard <episode>/storyboard.json [--json] [--out <path>]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SHOT_SIZES = ("极远景", "远景", "全景", "中景", "近景", "特写", "大特写")
CLOSEUP_SIZES = ("特写", "大特写")
CAMERA_MOVES = (
    "推", "急推", "拉", "急拉", "摇", "移", "跟", "升降", "甩", "震颤", "旋转",
    "推/急推", "拉/急拉",
)
EMOTIONS = ("愤怒", "冷漠", "平静", "蔑视", "威严", "恐惧", "内心独白", "坚定")
# speech_rate → (字/秒 下界, 上界)，MJ-LINE-02；容差 ±1
SPEECH_RATE_RANGE = {
    "正常": (5, 6),
    "激动": (7, 8),
    "快": (7, 8),
    "低沉": (4, 5),
    "慢": (4, 5),
    "内心独白": (2, 6),
}
# MJ-BAN：具体禁项（注意「血光」是允许的光效，故用具体词组）
BANNED_TERMS = (
    "红色血液", "内脏", "断肢", "喷溅", "扭曲人脸", "鬼脸", "哭脸",
    "血滴", "哀嚎", "残影", "色情", "裸露",
)
AUDIO_REQUIRED_LINE = "音频要求：不要背景音乐，不要字幕，不要解说声音。"
BEAT_MIN, BEAT_MAX = 2.0, 5.0
BEAT_COUNT_MIN, BEAT_COUNT_MAX = 5, 8
CLOSEUP_RATIO_MAX = 0.40
SFX_MAX_CHARS = 10
DIALOGUE_MAX_CHARS = 30


def _chars(text: str) -> int:
    return len("".join(str(text).split()))


def _looks_like_drama(shots: list) -> bool:
    """Heuristic: storyboard carries drama content (dialogue or cast) but no spec."""
    for s in shots:
        if not isinstance(s, dict):
            continue
        if str(s.get("dialogue") or "").strip():
            return True
        if s.get("cast"):
            return True
    return False


def validate_drama_spec(storyboard: dict) -> dict:
    """Return {"valid": bool, "errors": [reason_codes], "warnings": [reason_codes], "stats": {...}}.

    2026-10-01: 未声明 spec 不再静默跳过。分镜呈漫剧形态（含台词/cast）却未声明
    `spec: manju-drama` 时，产出 warning `drama_spec_undeclared_spec`（须人工确认；
    `prompt_compiler.py --strict` 会拒绝编译）。warning 不阻断 validate（向后兼容）。
    """
    errors: list[str] = []
    warnings: list[str] = []
    spec = storyboard.get("spec")
    shots = storyboard.get("shots") or []
    has_beats = any(isinstance(s, dict) and s.get("beats") for s in shots)

    if has_beats and spec != "manju-drama":
        errors.append("drama_spec_spec_flag_missing")
    if spec != "manju-drama":
        if _looks_like_drama(shots):
            warnings.append("drama_spec_undeclared_spec")
        return {"valid": not errors, "errors": errors, "warnings": warnings,
                "stats": {"applied": False}}

    stats: dict = {"applied": True, "shots": []}
    for i, shot in enumerate(shots, 1):
        if not isinstance(shot, dict):
            continue
        sid = str(shot.get("shot_id") or f"shot-{i}")
        beats = shot.get("beats")
        if not isinstance(beats, list) or not beats:
            errors.append(f"drama_spec_beats_missing:{sid}")
            continue
        if not (BEAT_COUNT_MIN <= len(beats) <= BEAT_COUNT_MAX):
            errors.append(f"drama_spec_beat_count:{sid}={len(beats)}")

        closeups = 0
        beat_seconds = 0.0
        for j, beat in enumerate(beats, 1):
            if not isinstance(beat, dict):
                errors.append(f"drama_spec_beat_fields_missing:{sid}.{j}")
                continue
            for field in ("shot_size", "camera_move", "vfx", "dialogue", "sfx", "description",
                          "emotion", "speech_rate", "on_screen", "blocking"):
                if field not in beat:
                    errors.append(f"drama_spec_beat_fields_missing:{sid}.{j}:{field}")

            dur = beat.get("duration_seconds")
            if not isinstance(dur, (int, float)) or not (BEAT_MIN <= float(dur) <= BEAT_MAX):
                errors.append(f"drama_spec_beat_duration:{sid}.{j}={dur!r}")
            beat_seconds += float(dur or 0)

            size = beat.get("shot_size")
            if size not in SHOT_SIZES:
                errors.append(f"drama_spec_camera_unknown:size:{sid}.{j}={size!r}")
            if size in CLOSEUP_SIZES:
                closeups += 1
            move = beat.get("camera_move")
            if move not in CAMERA_MOVES:
                errors.append(f"drama_spec_camera_unknown:move:{sid}.{j}={move!r}")

            sfx = str(beat.get("sfx") or "").strip()
            if not sfx or sfx == "无":
                errors.append(f"drama_spec_sfx_missing:{sid}.{j}")
            elif _chars(sfx) > SFX_MAX_CHARS:
                errors.append(f"drama_spec_sfx_too_long:{sid}.{j}={_chars(sfx)}")

            dlg = str(beat.get("dialogue") or "").strip()
            if _chars(dlg) > DIALOGUE_MAX_CHARS:
                errors.append(f"drama_spec_line_too_long:{sid}.{j}={_chars(dlg)}")
            rate = beat.get("speech_rate")
            if dlg and rate in SPEECH_RATE_RANGE and float(dur or 0) > 0:
                lo, hi = SPEECH_RATE_RANGE[rate]
                cps = _chars(dlg) / float(dur)
                if not (lo - 1 <= cps <= hi + 1):
                    errors.append(f"drama_spec_line_rate:{sid}.{j}={cps:.1f}")

            if not str(beat.get("vfx") or "").strip():
                errors.append(f"drama_spec_vfx_missing:{sid}.{j}")
            on_screen = beat.get("on_screen")
            if not isinstance(on_screen, int) or on_screen < 1:
                errors.append(f"drama_spec_blocking_missing:{sid}.{j}:on_screen={on_screen!r}")
            if not str(beat.get("blocking") or "").strip():
                errors.append(f"drama_spec_blocking_missing:{sid}.{j}")
            if beat.get("emotion") not in EMOTIONS:
                errors.append(f"drama_spec_beat_fields_missing:{sid}.{j}:emotion={beat.get('emotion')!r}")

            blob = " ".join(str(beat.get(k) or "") for k in ("description", "dialogue", "vfx"))
            for term in BANNED_TERMS:
                if term in blob:
                    errors.append(f"drama_spec_banned_content:{sid}.{j}:{term}")

        ratio = closeups / len(beats) if beats else 0.0
        if closeups < 1:
            errors.append(f"drama_spec_closeup_ratio:{sid}=0")
        elif ratio > CLOSEUP_RATIO_MAX:
            errors.append(f"drama_spec_closeup_ratio:{sid}={ratio:.2f}")

        shot_dur = float(shot.get("duration_seconds") or 0)
        if abs(beat_seconds - shot_dur) > 0.01:
            errors.append(f"drama_spec_beat_duration:{sid}:sum={beat_seconds:.1f}!=shot={shot_dur:.1f}")

        stats["shots"].append(
            {"shot_id": sid, "beats": len(beats), "seconds": round(beat_seconds, 1),
             "closeups": closeups, "closeup_ratio": round(ratio, 2)}
        )
    return {"valid": not errors, "errors": errors, "warnings": warnings, "stats": stats}


def main() -> None:
    parser = argparse.ArgumentParser(description="drama-storyboard-spec gate (MJ-* rules)")
    parser.add_argument("--storyboard", required=True)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    path = Path(args.storyboard).expanduser().resolve()
    storyboard = json.loads(path.read_text(encoding="utf-8"))
    result = validate_drama_spec(storyboard)
    if args.out:
        Path(args.out).expanduser().resolve().write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    for w in result.get("warnings") or []:
        print(f"WARNING: drama-storyboard-spec: {w} (needs human confirmation)", file=sys.stderr)
    if not result["valid"]:
        print("FAIL: drama-storyboard-spec: " + "; ".join(result["errors"]), file=sys.stderr)
        sys.exit(2)
    print("PASS: drama-storyboard-spec" + ("" if result["stats"].get("applied") else " (not applied)"))


if __name__ == "__main__":
    main()
