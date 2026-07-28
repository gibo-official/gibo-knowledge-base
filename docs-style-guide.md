---
title: "docs-style-guide"
lang: zh-CN
category: 仓库文档
product: ""
tags: ["GIBO", "洁博利", "风格指南", "写作规范", "AI知识库"]
summary: "GIBO 知识库文档写作规范：标题层级、问答格式、FrontMatter、术语统一、参数图双写与表格使用约定。"
updated: 2026-07-28
---

# 文档风格指南（docs-style-guide）

## 1. 标题层级
- 每篇文档仅一个 `#` 一级标题（文件主题）。
- 章节用 `##`，问答用 `### Q：`。
- 不要跳级（如 `#` 直接到 `###`）。

## 2. 问答格式（FAQ）
- 统一使用 `### Q：自然语言问句 [Tier标签] | tag1,tag2` 起头。
- 答案以 `A：` 开头，段间用 `---` 分隔，便于向量切片。
- 避免把多个问题挤在一个标题下。

## 3. FrontMatter
- 所有 FAQ 子文件必须含 `lang / category / product / tags / summary / updated`。
- `updated` 使用 `YYYY-MM-DD`，改动时同步更新。

## 4. 术语统一
- 以 [GLOSSARY](GLOSSARY.md) 的"规范中文名"为正文用词。
- 别名（如"感应水龙头"）仅在首次出现或 tags 中使用。
- 中英文对照见 [translation-glossary](translation-glossary.md)。

## 5. 关键参数：图 + 表双写（硬规则）
- **禁止仅用图片承载关键参数**（型号、尺寸、电压、流量、认证、压力、温度等）。
- 图片中的参数必须同步以 Markdown 表格呈现，确保文本可被检索/向量化，且图片 OCR/切片失败时参数不丢失。
- 适用对象：尺寸图、规格表截图、认证/证书图、接线/爆炸图、技术曲线图等。
- 示例：
  ```markdown
  ![产品尺寸图](assets/products/xxx.png)

  | 参数 | 数值 |
  |------|------|
  | 额定电压 | AC 100-240V |
  | 工作温度 | 0-55℃ |
  | 防护等级 | IPX4 |
  ```
- 扫描现状（2026-07-21）：全库参数图均已配套文字表，图+表双写达标；风险集中在空 alt（见第 8 节）。

## 8. 图片必须带描述性 alt 文本（硬规则）
- 所有图片引用 `![alt](path)` 的 `alt` **不得为空**，须用一句话说明图片内容/承载的参数。
- 反例：`![](assets/products/xxx.png)` ❌
- 正例：`![GBL-6161 安装尺寸图，单位 mm](assets/products/gbl-6161-dim.png)` ✅
- 例外（可不带 alt）：纯装饰 icon/logo/banner/背景图，应在文件名或注释中标注 `decor`。
- 现状（2026-07-21）：全库 3530 张图片中 **3482 张（98.6%）为空 alt**，是「图片内嵌文字风险」的主要来源。
  - 受管区（`faq/`、`products/`、`product-spec/`、`whitepapers/`、`solutions/`）新增图片**强制带 alt**，CI 将逐步开启 alt-WARN 检查以逐批收敛。
  - 历史文件允许存量空 alt，但鼓励回填。

## 6. 链接
- 内部链接使用相对路径；FAQ 子文件在 `product/`·`support/` 子目录下，指向仓库根级目录用 `../../`。
- 提交前确保无死链（CI 会校验）。

## 7. 语言与语气
- 中文文档用简体中文；英文文档用美式英文。
- 面向用户的内容用第二人称，技术文档用祈使句。
