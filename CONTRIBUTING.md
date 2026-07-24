---
title: "CONTRIBUTING"
lang: zh-CN
category: 仓库文档
product: ""
tags: ["GIBO", "洁博利", "贡献", "协作", "AI知识库"]
summary: "GIBO 知识库贡献流程：分支模型、FAQ 新增规范、命名与风格要求，以及本地 CI 自检方法。"
updated: 2026-07-24
---

# 贡献指南（CONTRIBUTING）

## 1. 分支模型
- 主分支：`main`（受保护，CI 自动校验）。
- 日常改动：从 `main` 切出 `feature/xxx` 分支， PR 合入 `main`。
- 提交信息：中文简述 + 必要时补充说明。

## 2. 新增 / 修改 FAQ
- FAQ 已按主题拆分为独立子文件，位于 `zh/faq/product/`、`zh/faq/support/`、`en/faq/product/`、`en/faq/support/`。
- **新增问答**：放到对应主题的 `faq-<key>.md` 子文件末尾，使用标准格式：
  ```markdown
  ### Q：用户自然语言问句 [Tier标签] | tag1,tag2

  A：答案正文。

  ---
  ```
- **新增产品线/主题**：在 `product/` 或 `support/` 新建 `faq-<key>.md`，并在对应 `faq-product.md` / `faq-support.md` 总览页与 `faq-index.md` 补充链接。
- 单文件问答建议 ≤ 120 条，超出请拆分，以提升向量切片精度。

## 3. 命名与风格
- 文件命名：见 [文件命名规则](filename-rule.md)。
- 写作风格：见 [文档风格指南](docs-style-guide.md)。
- 术语统一：所有术语以 [GLOSSARY](GLOSSARY.md) 规范名为准，别名仅用于检索标签。

## 4. FrontMatter 必填
FAQ 子文件头部必须包含：
```yaml
---
title: "..."
lang: zh-CN | en-US
category: FAQ
product: "<key>"
tags: ["GIBO", "洁博利", "...", "FAQ", "AI知识库"]
summary: "..."
updated: YYYY-MM-DD
---
```

## 5. 本地自检（CI 前必跑）
```bash
python3 scripts/ci_check.py            # 全仓（历史资产仅警告）
# 或仅校验本次改动
python3 scripts/ci_check.py $(git diff --name-only origin/main...HEAD -- '*.md')
```
CI 会在每次 push / PR 自动运行，校验：死链、命名合规、FrontMatter、Markdown lint。
受管文档（faq/、根级文档、scripts/）强校验；历史资产目录仅警告。
