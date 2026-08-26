# Project adapter · character-illustrations (selfmedia-creator)

Forked from [moxordo/character-illustrations](https://github.com/moxordo/character-illustrations) (MIT; portions Ian Xiaohei / peanut).

## When to use

- 16:9 **单图解释/正文配图**（白底手绘、一图一义）
- registry `visual_skill: character-illustrations` + `character_profile: <slug>`

## Character routing (this repo)

| profile | account / vertical | 用途 |
|---------|-------------------|------|
| `xiaohei` | 可选 / 技术隐喻默认 | 通用怪诞解释 |
| `hangban-ticket` | `hangban-gzh` · airline-info | 票务须知 |
| `qinggan-star` | `qinggan-gzh` · **仅单图概念** | 情感结构单图 |
| `qi-spark` | `qi-share` · qi-notes | X/短内容 |

Load: `skills/character-illustrations/characters/<profile>.md`

## Do NOT use for

- **情感号多格/条漫/分镜连载** → `skills/comic-storyboard` 或本机 `baoyu-comic`
- 真实截图 enrich → `kushi-visual-enrich`

## Output path (project)

```text
content/masters/{vertical}/{slug}/assets/{slug}-illustrations/
  01-topic.png
```

## Image backend

1. Agnes (`qi_dev.sh agnes-image-gen`) — current default  
2. SVG backend in skill — optional if Chrome/Pillow available  
3. Grok 4.5 — **not** an image model (see ian-xiaohei PROJECT.md)

## Registry fields

```yaml
visual_skill: character-illustrations
character_profile: hangban-ticket
```
