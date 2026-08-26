---
name: analyze-data
description: |
  多平台数据分析 Skill。支持阅读量、互动量、粉丝增长等数据聚合分析。
triggers:
  - pattern: "分析.*数据"
  - pattern: "/analytics"
  - pattern: "查看.*数据"
---

# Analyze Data Skill

## When to Use

Use this skill when:

- 用户需要查看内容数据表现
- 用户需要多平台数据对比
- 用户需要数据报告

## Workflow

### Step 1: 获取数据

调用各平台 API 获取数据：
- `getWechatGzhStats`
- `getXiaohongshuStats`
- `getDouyinStats`

### Step 2: 聚合分析

调用 `aggregateStats` 聚合多平台数据。

### Step 3: 生成报告

调用 `generateReport` 生成可视化报告。
