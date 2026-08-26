---
name: schedule-post
description: |
  内容排期发布 Skill。支持日历视图、批量排期、自动发布。
triggers:
  - pattern: "排期.*发布"
  - pattern: "/schedule"
  - pattern: "定时.*发布"
---

# Schedule Post Skill

## When to Use

Use this skill when:

- 用户需要规划内容发布日历
- 用户需要批量设置定时发布
- 用户需要查看发布计划

## Workflow

### Step 1: 获取草稿列表

调用 `listDrafts` 获取待发布草稿。

### Step 2: 设置排期

调用 `schedulePublish` 设置发布时间。

### Step 3: 返回日历视图

返回排期结果和日历视图。
