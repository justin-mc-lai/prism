# Intel Briefing — watermarks-remover（2026-08-15）

- mode_id: brief-intel
- public_id: intel
- lane: standard
- recommended_next_harness: master
- map_ids_considered: ['MAP-003', 'MAP-010']
- 来源: GitHub Search API（created > 2026-08-01 · sort=stars · 检索时间 2026-08-15）

## 热点结论

`guillaumemeyer/watermarks-remover` 为近两周新建仓库中 star 增速第一梯队：**8,509 stars /
876 forks / 13 open issues**（检索时刻 2026-08-15），MIT 协议，Python 实现。
定位：去除多厂商 AI 溯源水印（Unicode 隐藏字符 / 统计采样水印 / C2PA 元数据），
官方口径为「对你自己拥有的内容做隐私与卫生处理」。

## 选题角度

面向内容创作者与 AI 重度用户的科普角度：**“AI 会在你的文件里藏什么水印，怎么查出来、怎么按需清掉”**。
信息差点：

1. 大多数人不知道 AI 文本/图片会带多层溯源痕迹（不可见 Unicode、统计水印、C2PA 元数据）。
2. 不知道清理工具要分三层处理（文本卫生 / 统计改写 / 文件元数据），不是一键魔法。
3. 不知道仓库自己保留了哪些边界（两个 harness 镜像因 license 从不发布；官方强调「content you own」）。

## 证据

- `https://api.github.com/repos/guillaumemeyer/watermarks-remover`（元数据，检索时刻 2026-08-15）
- `README.md`（功能/分层/安装/边界，检索时刻 2026-08-15）
- 风险提示：star 数会随时间变化；本话题涉及「去除 AI 溯源标记」，成稿必须保留
  「content you own」边界，不得写成教人伪装/规避检测的工具。
