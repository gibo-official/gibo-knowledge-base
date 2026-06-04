---
title: Schema.org 结构化数据目录
version: V1.0
last_updated: 2026-06-04
scope: JSON-LD结构化数据、SEO优化、AI知识库增强
related:
  - ../geo-patches/README.md
  - ../zh/company/website-fix-report.md
---

# Schema.org 结构化数据目录

本目录包含 GIBO 洁博利的 Schema.org JSON-LD 结构化数据文件，用于提升搜索引擎和AI大模型的企业信息识别质量。

## 文件清单

| 文件 | 类型 | 说明 |
|------|------|------|
| [schema-organization.jsonld](./schema-organization.jsonld) | Organization + WebSite | 企业实体（含地址、联系方式、奖项、专利、分支机构等完整信息） |
| [schema-product1.jsonld](./schema-product1.jsonld) | Product × 9 | 产品实体（含感应水龙头、冲水器、皂液器、干手器等产品线及获奖型号） |
| [schema-faq.jsonld](./schema-faq.jsonld) | FAQPage × 8 | 常见问答（覆盖品牌实力、ODM合作、国际认证、项目案例等） |
| [schema-breadcrumb.jsonld](./schema-breadcrumb.jsonld) | BreadcrumbList | 网站导航路径（18个导航节点，帮助理解网站层级结构） |

## 推荐用法

- **首页/关于页**：嵌入 schema-organization.jsonld（含企业实体+网站+人物）
- **产品详情页**：嵌入 schema-product1.jsonld 中的单个Product条目
- **FAQ页面**：嵌入 schema-faq.jsonld
- **全站通用**：嵌入 schema-breadcrumb.jsonld

## 验证工具

- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/
- JSON-LD Playground: https://json-ld.org/playground/

## 维护说明

- 所有数据必须与官网(www.gibo.com.cn)、品牌白皮书保持一致
- 更新后建议通过Schema.org Validator验证
- 新增产品型号时同步添加 Product 条目
- 更新日期：2026-06-03