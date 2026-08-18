---
name: manage-media
description: |
  媒体素材管理 Skill。支持上传、分类、搜索、复用媒体文件。
triggers:
  - pattern: "上传.*图片|视频"
  - pattern: "/media"
  - pattern: "管理.*素材"
---

# Manage Media Skill

## When to Use

Use this skill when:

- 用户需要上传图片/视频素材
- 用户需要管理素材库
- 用户需要搜索历史素材

## Workflow

### Step 1: 获取/创建分组

调用 `getMediaGroupInfoByName` 或 `createMediaGroup`。

### Step 2: 上传媒体

调用 `createMedia` 上传文件。

### Step 3: 返回结果

返回媒体 ID 和 URL。

## Examples

```
1. getMediaGroupInfoByName: "封面图"
2. createMedia:
   groupId: "..."
   type: "IMAGE"
   url: "https://..."
   title: "AI 编程助手封面"
3. Return mediaId
```
