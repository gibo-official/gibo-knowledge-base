---
title: "FAQ 归档目录说明"
lang: zh-CN
category: Archive
product: ""
tags: ["GIBO", "FAQ", "归档", "备份"]
summary: "GIBO FAQ 旧版聚合文件的归档目录，已移出主树，不参与 AI 向量切片与 CI 正文校验。"
updated: 2026-07-28
---

# FAQ 归档目录说明

本目录存放从 `zh/faq/` 与 `en/faq/` 移出的**旧版聚合文件**，已于 2026-07-28 Phase 3 备份治理中移出主树。

## 文件清单
- `zh-faq-backup.md`：中文旧版全量 FAQ 聚合备份
- `zh-faq-geo-backup.md`：中文旧版 GEO FAQ 聚合备份（910 问原始池，Top100 已精选入 `zh/faq/faq-geo-top10.md`）
- `en-faq-backup.md`：英文旧版全量 FAQ 聚合备份
- `en-faq-geo-backup.md`：英文旧版 GEO FAQ 聚合备份

## 治理原则
- 归档文件**不参与** AI 向量切片（Milvus）、不参与 CI 正文校验。
- 如需恢复历史内容，请从本目录取用，勿在活动 FAQ 正文内引用（见仓库根 `filename-rule.md` 归档文件约定）。
- Git 历史完整保留，可随时 `git log` / `git show` 追溯。
