---
title: "filename-rule"
lang: zh-CN
category: 仓库文档
product: ""
tags: ["GIBO", "洁博利", "文件命名", "规范", "AI知识库"]
summary: "GIBO 知识库文件命名规则：小写、连字符、无空格，语言目录与 FAQ 子文件命名约定，以及允许的例外。"
updated: 2026-07-24
---

# 文件命名规则（filename-rule）

> 本规则与 [文档风格指南](docs-style-guide.md)、[贡献指南](CONTRIBUTING.md) 配套。CI 会对受管文档做命名合规校验。

## 通用规则
1. **小写字母 + 数字 + 连字符**：`sensor-faucet-spec.md`。
2. **禁止空格**：用连字符 `-` 代替。
3. **禁止大写字母**（以下例外除外）。
4. **禁止特殊字符**：`\ / : * ? " < > | @ # % & ( )` 等不出现在文件名。
5. 使用有意义的英文/拼音短词，避免无含义的随机串。

## 允许的例外（全大写缩写，CI 白名单）
- `README.md`、`LLMS.md`、`GLOSSARY.md`、`NAMING-CONVENTION.md`、`MAINTENANCE.md`、`ROLE-DESCRIPTIONS.md`、`LICENSE` / `LICENSE.txt`

## 目录约定
- 语言目录：`zh/`（中文）、`en/`（英文）。
- FAQ 子文件位于 `zh/faq/product/`、`zh/faq/support/` 等，文件名 `faq-<key>.md`：
  - `faq-tap.md`（感应龙头）、`faq-flusher.md`（冲水器）、`faq-sensor.md`（模块）、
    `faq-soap.md`（皂液器）、`faq-hand-dryer.md`（干手器）、`faq-shower.md`（淋浴）、
    `faq-toilet.md`（马桶）、`faq-odm.md`（ODM）、`faq-trouble.md`（故障）、`faq-installation.md`（安装）、
    `faq-company.md`（公司）、`faq-comparison.md`（对比）、`faq-user.md`（体验）、
    `faq-scenario.md`（场景）、`faq-buying.md`（购买决策）。
- 总览页：`faq-product.md`、`faq-support.md`、`faq-geo-top10.md`。
- 图片资源：`assets/products/...`、`assets/standard/...`，建议小写连字符。

## 归档文件
- 旧版/历史文件以 `-backup.md` 结尾（如 `faq-backup.md`），不强制命名校验，但请勿在正文中引用。
