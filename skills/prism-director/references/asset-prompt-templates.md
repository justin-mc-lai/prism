# 资产提示词模板（distill · onlyshot ref 工艺 + 三圣经）

> 蒸馏源：`vendor/skills/onlyshot/references/ref-prompt-industrial.md`（v0.5.0）、
> `vendor/skills/onlyshot/assets/templates/{05_角色圣经,06_场景圣经,07_道具圣经}.md`
> （MIT，A-cat-with-carrots/OnlyShot；授权登记见 `docs/ATTRIBUTION-drama-prompt-repos.md`）。
> 只取模板结构与阈值，不复制上游运行时/样例数据。
>
> **与既有门的分工（三者叠加，互不替代）**
> | 文件 | 管什么 |
> |---|---|
> | `storyworld-extraction.md` | 从剧本**抽出哪些**资产（四层判定 + 五类字段） |
> | `asset-consistency-gate.md` | 抽出来之后**跨镜是否一致**（三分法/CON-01/AST-05） |
> | **本表** | 抽出之后**资产提示词怎么写**（T2I ref 卡） |
> | `prompt-syntax-table.md` | **镜头提示词**怎么写（I2I 分镜） |
>
> **阈值可信度**：NOT 词 ≤5、戏剧光 ref 前后不像同一人 40%、前 200 token 权重最高，
> 均为上游单项目实战观测（即梦/Seedream 5.0 类），**不是模型物理常数**；
> 换模型/形态须重测（同 `contracts/prompt-syntax.contract.md` §5 精神）。

---

## 0. 三条铁律（决定一致性上限）

```
1. ref 图 ≠ 成片：ref 必须 neutral flat lighting（中性平光），不要戏剧化光
2. prompt ≠ 一致性：一致性靠 visual reference anchoring（ref 图本身），prompt 只控质量
3. identity block 逐字复用 = 常量；风格串 = 可换后缀；构图 = 每镜变量
```

**铁律 3 是一致性上限的唯一来源**：三者的分离度决定跨镜是否崩，与模型强弱无关。
把风格写进身份块 = 换风格就得重画身份；把身份写进分镜 = 与 ref 打架（同 `prompt-syntax-table.md` §0）。

上游实测旁证：戏剧光 ref 在 image2video 里**前后两镜角色不像同一人**的概率达 40%，
中性光 < 5%（`ref-prompt-industrial.md §10`）。所以 ref 一律平光。

---

## 1. 风格正交（资产 × 风格 = 笛卡尔积，禁止写死）

资产串是**常量**，风格串是**可换后缀**。同一角色换 4 种导演视角 = 4 次套同一身份块 + 换风格串，
不需要重写身份。这是「3 模式 × 4 视角」不爆炸的前提。

**组装顺序（顺序即权重）**

```text
[风格指纹]  →  身份块  →  造型/材质  →  布局  →  [NEGATIVE]
   头部最高权重          中段            尾部结构化
```

- 风格指纹放 **prompt 开头**（前 200 token 权重最高，不是末尾）。
- 风格串取**风格预设 SoT**：`registry/style-presets.yaml`（Prism overlay，29 预设）
  ⊕ `content/pipelines/ai-manga-drama/lumenx-style-presets.json`（lumenx base 15，原样拷贝）。
  合并按 `id` 去重，重复即 fail-closed；overlay 的 `merge.required_views` 定义四种必备视角
  （真人/动画/水墨/国风）。
- 负面词取同预设 `negative_prompt`，再与 `[NEGATIVE]` 段合并去重。
- **ref 阶段只用预设 `positive_prompt` 里与"画风/材质"有关的部分，剔除戏剧光关键词**
  （`cinematic lighting` / `lens flare` / `chiaroscuro` / `dramatic backlight` 等留给分镜/视频段）。
- 风格预设缺目标视角时**新建 overlay 条目**，不改身份块、不改 base。

---

## 2. 通用 7 段 identity block 骨架（所有资产类共用）

> 上游称「6 段」，实际列出 7 个显式标签（IDENTITY/BODY/FACE/ATTIRE/LAYOUT/STYLE/NEGATIVE）。
> 本表按**实际标签数**称 7 段。每段独立行 + 显式标签 → 模型按段处理 → 信息不混。

```text
[IDENTITY]  <asset_id>, fixed <character|location|prop> design,
            must remain consistent across all generations,

[BODY]      <主体构成：体型/结构/轮廓/尺度，>4 head units 或等价尺度参照>,
            <标志性结构特征>,
            single cohesive object, NO separation between parts,

[FACE]      <特征落点：五官画在哪个具体部位>,
            <眼/表情/纹理细节>,
            expression: <中性气质关键词，禁戏剧化情绪>,

[ATTIRE]    <服饰/配饰/材质，明确写在哪一部位>,
            NO <禁止出现的结构>,
            <四肢/附属物从哪长出，数量>,

[LAYOUT]    <视图布局：4-grid / 3-view / 单图>,
            quadrants: <左上><右上><左下><右下>,
            identical <asset> in all quadrants,
            NO text labels, NO annotations, NO watermarks, NO grid view labels,

[STYLE]     <风格串（来自预设 positive_prompt 的稳定部分）>,
            neutral studio lighting flat even, solid <color> background,
            <材质/笔触>,

[NEGATIVE]  <≤5 个 NOT 词，去重>
```

**各段反模式**

| 段 | 禁止 |
|---|---|
| IDENTITY | 省略 id；id 每次换拼写 |
| BODY | 写抽象质量词（「精致」「高级」）；不写尺度参照 |
| FACE | 写戏剧化情绪（「悲愤」「泪流满面」）→ 污染 ref |
| ATTIRE | 服饰位置含糊（写「穿着X」不写在哪一部位） |
| LAYOUT | 只写「4 views」不写每格内容 → 模型自动加英文水印 |
| STYLE | 写 `cinematic` / `lens flare` / `dramatic lighting` → 一致性崩 |
| NEGATIVE | 堆 ≥6 个 NOT（上游实测生效率降到 30%） |

---

## 3. 五类资产模板

五类共用 §2 骨架，差异只在槽位语义与视图布局。落盘映射见 §7。

### 3.1 人物卡（character sheet）→ `characters[]`

- 视图：**4 宫格**（正面 / 3/4 右 / 3/4 左 / 背面），4 格同一人。
- 必填槽：年龄、性别、体型、发型、五官锚点、服装（按阶段列服装表）、视觉母题 ≥2、标志动作 ≥2。
- 服装表按阶段（第 1-9 集 / 10-30 / …）；**换装 = 变体，不新建身份**（`asset-consistency-gate.md §1`）。
- 中性气质词只写"长相气质"（e.g. `elegant aloof`），不写剧情情绪。

```text
[IDENTITY] char_01_lin, fixed character design, must remain consistent across all generations,
[BODY] 26yo female, slim build, 4.5 head units, straight posture, waist-length black hair,
[BODY] (cont.) signature red ribbon at neck,
[FACE] oval face, almond eyes with single highlight, mole under left eye, calm neutral expression,
[ATTIRE] olive-green stand-collar service dress, brass buttons on chest, NO armor,
[BODY] two arms, leather satchel strap crossing right shoulder,
[LAYOUT] 4-grid character reference sheet,
[LAYOUT] quadrants: top-left front view, top-right 3/4 right, bottom-left 3/4 left, bottom-right back view,
[LAYOUT] identical character in all 4 quadrants, NO text labels, NO annotations, NO watermarks,
[STYLE] <style preset positive (no cinematic lighting)>, neutral studio lighting flat even,
[STYLE] solid pale grey background, clean cel shading, bold outlines,
[NEGATIVE] not realistic, not 3D photoreal, not multiple characters, no text, no watermark
```

### 3.2 场景卡（establishing / 四宫格）→ `scenes[]`

- 视图：**4 宫格**（全景 / 入口 / 关键陈设特写 / 窗外或对位视角），整体灯光色调装修一致。
- 必填槽：物理空间、装饰、氛围、**中性灯光**、面积尺度、重复母题、内/外景（`kind`）。
- **时段/天气是变体**（夜景版/雨天版/火光版），写在 `variant`，不新建场景身份。
- 场景 ref 承载"光"：分镜层不重写光影（见 `continuity-seven-laws.md §6` 旁证）。

```text
[IDENTITY] scene_01_office, fixed location design, must remain consistent across all generations,
[BODY] 40㎡ corner office, north-facing floor-to-ceiling window, grey concrete walls,
[BODY] one wooden desk, two visitor chairs, wall-mounted family photo, scale: 1 door = 2.1m,
[FACE] (细节层) worn desk edge, chipped paint at window frame, single potted plant,
[ATTIRE] (陈设层) navy blinds half-drawn, brass desk lamp off, NO people, NO clutter,
[LAYOUT] 4-grid location reference sheet,
[LAYOUT] quadrants: top-left wide establishing, top-right entrance angle,
[LAYOUT] bottom-left key furniture close-up, bottom-right view through window,
[LAYOUT] consistent lighting and palette in all 4, NO text labels, NO watermarks,
[STYLE] <style preset positive, interior-appropriate>, neutral daylight flat even,
[STYLE] solid ambient palette, realistic material texture,
[NEGATIVE] no people, no text, no watermark, not multiple rooms
```

### 3.3 道具卡（prop sheet）→ `props[]`

- 视图：**4 宫格白底产品图**（正面平视 / 侧面 45° / 背面 / 关键细节特写）。
- 必填槽：外观、材质、尺寸、颜色、剧情功能、象征、携带规则（`holder` 指向 `characters[].id`）。
- 只收录有剧情推动/象征意义的道具；日常物件不建资产。
- **换手即换 `holder`，不新建道具**。

```text
[IDENTITY] prop_01_compass, fixed prop design, must remain consistent across all generations,
[BODY] antique brass pocket compass, 5cm diameter, 1.2cm thick, hinged lid, worn patina,
[FACE] (细节层) engraved rose dial, faint blue glow along the needle, tiny chip at 3 o'clock rim,
[ATTIRE] (配件层) leather lanyard 30cm, single brass ring, NO chain, NO gemstones,
[LAYOUT] 4-grid product reference sheet on white background,
[LAYOUT] quadrants: top-left front view, top-right 45-degree side,
[LAYOUT] bottom-left back view, bottom-right macro detail of dial engraving,
[LAYOUT] NO text labels, NO annotations, NO watermarks, NO hands,
[STYLE] <style preset positive, product-appropriate>, neutral studio lighting flat even,
[STYLE] solid white background, clear visible material texture,
[NEGATIVE] no hands, no text, no watermark, not multiple objects
```

### 3.4 神兽卡（creature sheet）→ `characters[]`（暂）

> 剧情级神兽/异兽。含**进化态**：`base` 不可覆盖，进化 = 新版本（同 agent-mangaka-forge 的
> `evolution` 语义，见 §6）。

- 视图：4 宫格（正面 / 侧面 / 背面 / 关键特征特写），加**尺度参照物**（人/门/树）。
- 必填槽：物种、体型、尺度参照、标志结构、威胁度、栖息场景、进化链（`base → form_2 → form_3`）。
- 进化态必须保留 `base` 的**谱系标记**（读者仍能认出是同一只）。

```text
[IDENTITY] creature_01_xuanwu, fixed creature design, base form, lineage: xuanwu,
[BODY] turtle-serpent chimera, 6m shell span, scale: 3x human height,
[BODY] obsidian shell with molten-gold seam lines, serpent tail coiled once,
[FACE] two amber slit eyes, jaw with three fangs, expression: ancient indifferent,
[ATTIRE] (附属层) gold filigree along shell rim, NO saddle, NO harness,
[LAYOUT] 4-grid creature reference sheet,
[LAYOUT] quadrants: front view, side view, back view, shell-pattern macro,
[LAYOUT] human silhouette scale bar in each quadrant, NO text labels, NO watermarks,
[STYLE] <style preset positive>, neutral studio lighting flat even, solid dark slate background,
[NEGATIVE] not cute, not cartoon chibi, no text, no watermark, not multiple creatures
```

### 3.5 群像卡（crowd sheet）→ `characters[]`（暂）

> 同种群像 / 异种群像。核心是**数量与密度约束**，不是个体身份。

- 视图：单图群像 + 可选分排示意（前/中/后景密度）。
- 必填槽：群体类型、人数范围、统一特征、个体差异度、密度、是否可辨识个体。
- **可辨识个体必须升级为人物卡**；群像卡只承载"模糊群体"（避免"多 ref 同框 = 一致性必崩"，
  见 `prompt-syntax-table.md §8`）。

```text
[IDENTITY] crowd_01_villagers, fixed crowd design, generic group,
[BODY] 12-20 adult villagers, mixed ages, unified palette of earth tones,
[BODY] density: dense foreground, sparse background,
[FACE] faces suggested not detailed, no recognizable individual,
[ATTIRE] common straw hats and hemp tunics, variation in shade only,
[LAYOUT] single wide crowd composition, depth layers front/mid/back,
[LAYOUT] NO text labels, NO watermarks, NO dominant hero character,
[STYLE] <style preset positive>, neutral overcast lighting flat even,
[NEGATIVE] no detailed faces, no text, no watermark, not one hero pose
```

---

## 4. 防坑：四视图水印陷阱

只写「4-grid character sheet, 4 different angles」→ 模型理解成教学图，
**自动渲染 FRONT / SIDE / BACK 英文水印**。

**Fix**：`[LAYOUT]` 段必须逐字拒绝：

```text
NO text labels, NO annotations, NO watermarks, NO grid view labels,
NO ENG text overlay, single composition per quadrant
```

---

## 5. 防坑：拟物化的真假陷阱

模型默认按「人 + 装饰」理解，**假拟物化**（90% 项目踩坑）：

```text
❌ "young woman wearing pagoda headpiece"  → 少女 + 塔头饰（≠ 拟物化）
```

**真拟物化**必须显式约束：

```text
✅ the character IS <object> itself        （不是 wearing it）
✅ NO human face, NO human torso underneath
✅ eyes painted directly on <object> surface
✅ chibi arms emerging from sides only
✅ NOT humanoid character                   （在 NEGATIVE 段）
```

---

## 6. 变体与进化的命名规则

| 类型 | 语义 | 目录/ID 规则 |
|---|---|---|
| `base` | 原始正典设计 | `<asset_id>`；**永不覆盖** |
| `variant` | 身份不变，服装/伤势/时段/天气/持物变 | `<asset_id>__<variant>`；记基底+变化+原因+范围 |
| `evolution` | 神兽/角色觉醒态、变身态 | `<asset_id>__<form>`；**必须保留 base 谱系标记** |

- 换风格 ≠ 变体：风格在 §1 的**风格串**里换，身份块不动。
- 变体只在"观众看得出不一致"的可见事实变化时创建（防每章重画烧钱，同 story-claw 的 stage 策略）。
- 所有变化按 `asset-consistency.contract.md` CON-04 记五要素。

---

## 7. 落盘映射（→ storyboard schema）

| 本表资产类 | storyboard-schema 字段 | 备注 |
|---|---|---|
| 人物卡 | `characters[]` | `id`/`name`/`traits` + `voice_id` |
| 场景卡 | `scenes[]` | `kind` ∈ `interior`/`exterior`；时段天气写 `variant` |
| 道具卡 | `props[]` | `holder` → `characters[].id` |
| 神兽卡 | `characters[]` | 暂落 `characters[]`，`traits` 前缀标 `[creature]` |
| 群像卡 | `characters[]` | 暂落 `characters[]`，`traits` 前缀标 `[crowd]` |

> `ponytail:` creature/crowd 暂借 `characters[]` 槽位（schema 只有三类）。
> 升级路径：`content/pipelines/ai-manga-drama/storyboard-schema.json` 加 `creatures[]` / `crowds[]`
> 顶层数组 + `scripts/ai_manga_drama.py` 的 `_validate_entities` 加解析，届时本表 §3.4/§3.5 换槽位。

---

## 8. 候选数与成本（上游实测，量级参考）

| 候选数 | 适用 | 相对成本 | 用途 |
|---|---|---|---|
| 1 | 过渡镜 | 最低 | 占位 |
| 2 | 标准对话段 | 低 | **默认** |
| 3 | 反转/爽点 | 中 | 选最佳 |
| 4 | 关键爆点 | 高 | 选最佳 + 留备选 |

- 分镜图成本约占视频成本 **10%**，可省视频试错 **50%+**（上游 N=1 项目估算，非普适常数）。
- 视频生成时 ref **5-8 张最优**（image ≤9，塞满 9 张注意力分散）。

---

## 9. 自查清单（每张 ref 跑前必查）

```text
□ identity block 在 prompt 顶部（asset_id + fixed design）
□ 风格指纹放 prompt 开头（前 200 token），不在末尾
□ ref 用 neutral flat lighting（不 cinematic / dramatic / lens flare）
□ NOT 词 ≤5 个
□ [LAYOUT] 含 NO text labels / NO annotations / NO watermarks
□ 拟物化用 IS the object（不是 wearing）
□ 服饰/附属物位置明确（on <具体部位> only）
□ 身份块逐字复用（换风格只换风格串，不动身份块）
□ 变体/进化按 §6 命名，base 未被覆盖
□ 尺度参照在场（人物 head units / 场景门高 / 神兽人形剪影）
```

通过后才提交 T2I。未过清单的 ref 不进资产库，更不进分镜（fail-closed，同 AST-05）。

---

## 10. 授权与边界

- 上游 MIT / Apache-2.0 内容商用须保留 `docs/ATTRIBUTION-drama-prompt-repos.md` 声明与随附 LICENSE。
- 上游阈值（NOT ≤5、40%/5%、前 200 token、成本占比）来自其单项目实测，**非模型物理常数**；
  引用须带来源与测试条件，未重测即引用视为无证据。
- 角色名/形状/配色防侵权：不借用现有 IP，商标词全替换，公众人物台词改写式致敬；
  审核「真实公众人物影射」为一票否决项（上游清单，本表只作提醒，不据此声称平台过审）。
- 本表**不**做授权判断（属 `contracts/adaptation.contract.md`）、**不**冻结正典（属 `prism-master`）、
  **不**出分镜（属 `prompt-syntax-table.md`）。
