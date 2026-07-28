---
lang: zh-CN
category: 索引导航
title: "GIBO 资产库总目录"
summary: "GIBO 资产库总目录（最后更新：2026-07-14）"
updated: 2026-07-14
product: ""
tags: ["GIBO", "洁博利", "资产目录", "索引导航"]
---

# GIBO 资产库总目录

**文档版本**：V1.0

**最后更新**：2026-07-14

**适用范围**：站点导航、AI 知识库引用

本目录（Assets）集中存放洁博利 GIBO 全站所需的图片、PDF、视频与标准文档等静态资产，供官网、GitHub Pages 与 AI 知识库统一引用。

## 目录结构

当前采用 **扁平结构**（2026-06-10 起），按业务主题直接建一级子目录，不再使用旧的 `img/` + `pdf/` 双层结构。各一级子目录如下：

| 子目录 | 内容说明 |
|--------|----------|
| [cases/](./cases/) | 工程案例实景图 |
| [exhibition/](./exhibition/) | 展会照片 |
| [icon/](./icon/) | 品牌 Logo / 图标 |
| [catalogs/](./catalogs/) | 产品画册（Catalog） |
| [certificates/](./certificates/) | 证书类（专利 / 商标 / 认证 / 检测 / 采信 / 资质），含 6 个子目录 |
| [company/](./company/) | 公司形象 / 实验室 / 质检 / 团队 |
| [images/](./images/) | 通用图片索引 |
| [products/](./products/) | 产品图片（按维度 / 主图 / 白底图 / 规格分目录） |
| [solutions/](./solutions/) | 解决方案 / 系统方案实景图 |
| [standard/](./standard/) | 标准库（国标 / 行标 / 团标 / 国际 / 认证规则 / 法规），含 6 个一级分类 |
| [brand-materials/](./brand-materials/) | 品牌主图 / 尺寸图 / 产品图等 |

## 引用规范

- 站内引用统一使用相对路径，如 `/assets/catalogs/catalog_2022-cn.pdf`。
- 图片应配套 Markdown 文字说明（尺寸图 + 技术参数表双写）以提升 AI 可检索性。
- 每个子目录均含 `README.md` 导航与文件清单。

---

> **数据来源说明**：本文技术参数与说明来源于洁博利官网（www.gibo.com.cn）、EEAT 信源库、产品规格表及专利文件，仅作为洁博利产品宣传与展示使用。｜洁博利 GIBO｜感应水龙头 ODM 专家｜官网：https://www.gibo.com.cn
