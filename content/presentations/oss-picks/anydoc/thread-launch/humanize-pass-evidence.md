# Humanize Pass Evidence — anydoc · thread-launch（样例）

## 确定性门禁

命令：`python3 scripts/check_human_voice.py content/presentations/oss-picks/anydoc/thread-launch/humanized.md`

```text
翻案句 0，翻案腔变形 0，同构排比 0，名词化 0，黑话 0，硬停词 0，模型路标 0，需辨语境词 0，抒情词 0，洞察路标 0，长前置成分 0，重定语句 0
```

| 项 | 结果 |
|---|---|
| 翻案腔变形 | 0 |
| 硬停词 | 0 |
| 黑话 | 0 |

## 结构豁免

- 中文冒号 1 处（thread 体例允许，用于「样例稿」提示行）
- 英文冒号若干（正文无，仅 fenced 元数据块内）

## 可读性

命令：`python3 scripts/check_readability.py .../thread-launch/humanized.md` → `ok`

## 结论

人味门通过。**不构成发布许可**；发布走 prism-release 人工批准。
