---
slug: prism-form-product-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-product-v1/truth.md
---

# User Stories — prism-form-product-v1（Lake D2 扩展）

## US-PRD-001 商品内容一条龙

prism-goal 接「帮我做这个商品的好物图文/带货视频脚本」→ classify_form 命中 product →
master 冻结商品事实快照（规格/价格有源）→ director 卖点排序 + shot list → produce 按
`form-product.contract` 产出 → qa 过事实门 + 极限词门 + anti-slop-gate → release 草稿停人工。

## US-PRD-002 商品事实无源

用户未提供商品资料且无抓取留档 → intake blocked `reason_code=product_fact_missing`，
human card 列缺失项，不产出成稿。

## US-PRD-003 形态自动识别歧义

输入同时命中多个形态关键词（如「把这本书做成漫剧和短视频」）→ human card 列候选交人，
禁止静默猜测；显式指定时跳过映射表。

## US-PRD-004 短剧参考蒸馏

制作漫剧/短剧时，produce/director 可按名引用 `vendor/skills/drama-skills` 的对应 skill
资产（MIT 已 pin）作对照参考；dramaclaw 判断框架只作 distill 参考，不整包复制。
