# Prism × selfmedia-creator × selfmedia-sync-ai 逻辑单仓入口（方案甲）
# 用法：make -C workspace <target>   或   cd prism/workspace && make <target>

CREATOR_ROOT ?= ../../selfmedia-creator
MUTEX        := python3 check_content_mutex.py --creator-root $(CREATOR_ROOT)
PINS         := python3 check_pin_drift.py --creator-root $(CREATOR_ROOT)
GATES        := python3 ../scripts/check_human_voice.py
READABILITY  := python3 ../scripts/check_readability.py

.PHONY: help check check-mutex check-pins manga-validate gates sync-cli

help:
	@echo "逻辑单仓工作台（sot-layering-decision 方案甲）"
	@echo "  make check          - 互斥校验 + pin 漂移检测（CI 入口）"
	@echo "  make check-mutex    - L3 母稿双仓可写互斥校验"
	@echo "  make check-pins     - pin 产物 vs 源仓漂移检测（--strict 加在 PINS 后）"
	@echo "  make manga-validate - 漫剧分镜 schema 校验（源仓 ep-001 实例）"
	@echo "  make gates F=<稿>   - 对指定稿件跑 human-voice + readability 双门禁"

check: check-mutex check-pins

check-mutex:
	$(MUTEX)

check-pins:
	$(PINS)

manga-validate:
	python3 ../scripts/ai_manga_drama.py validate \
		--storyboard $(CREATOR_ROOT)/content/masters/ai-manga-drama/ep-001-escape/storyboard.json

gates:
	@test -n "$(F)" || { echo "用法: make gates F=content/masters/.../humanized.md"; exit 2; }
	$(GATES) $(F) && $(READABILITY) $(F)

sync-cli:
	{ printf '%s\n' \
	    '#!/usr/bin/env python3' \
	    '# ATTRIBUTION (A4 MIT): pinned from selfmedia-creator scripts/ai_manga_drama.py' \
	    '# Owner license decision A1/A4: MIT, see docs/owner-license-decision.md + docs/ATTRIBUTION-render-chain.md' \
	    '"""ai-manga-drama pipeline CLI (v0.0.5 R1)."""'; \
	  tail -n +4 $(CREATOR_ROOT)/scripts/ai_manga_drama.py; } > ../scripts/ai_manga_drama.py && \
	python3 -c "import ast; ast.parse(open('../scripts/ai_manga_drama.py').read()); print('pin synced: 源仓 CLI → prism（保留 ATTRIBUTION 头）')"
