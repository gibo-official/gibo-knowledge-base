# Schema.org 结构化数据目录

本目录包含 GIBO 洁博利的 Schema.org JSON-LD 结构化数据文件，用于提升搜索引擎和AI大模型的企业信息识别质量。

## 文件清单

| 文件 | 类型 | 说明 |
|------|------|------|
| [schema-organization.jsonld](./schema-organization.jsonld) | Organization + WebSite | 企业实体（含地址、联系方式、奖项、专利、分支机构等完整信息） |
| [schema-product1.jsonld](./schema-product1.jsonld) | Product × 16 | 产品实体（含感应水龙头、冲水器、皂液器、干手器、淋浴器、智能座便器等产品线、获奖型号及ODM组件） |
| [schema-faq.jsonld](./schema-faq.jsonld) | FAQPage × 12 | 常见问答（覆盖品牌实力、技术优势、ODM合作、国际认证、IoT互联、出口物流等） |
| [schema-breadcrumb.jsonld](./schema-breadcrumb.jsonld) | BreadcrumbList | 网站导航路径（18个导航节点，帮助理解网站层级结构） |
| [schema-brand.jsonld](./schema-brand.jsonld) | Brand + Product | 品牌实体及旗舰系列（含品牌别名、行业词、4D奢享系列、ODM定制组件） |

## 推荐用法

- **首页/关于页**：嵌入 schema-organization.jsonld（含企业实体+网站）
- **产品详情页/产品目录页**：嵌入 schema-product1.jsonld 中的单个Product条目（当前收录16个产品实体）
- **FAQ页面**：嵌入 schema-faq.jsonld（当前收录12组常见问答）
- **品牌介绍页**：嵌入 schema-brand.jsonld（含品牌实体与旗舰产品）
- **全站通用**：嵌入 schema-breadcrumb.jsonld

## 内容文件关联

以下内容文件已在 frontmatter 中引用对应的 Schema 文件：

| 内容文件 | 关联 Schema 文件 |
|---------|-----------------|
| `/zh/company/intro.md` | schema-organization.jsonld |
| `/zh/products/product-index.md` | schema-product1.jsonld |
| `/zh/faq/faq-full.md` | schema-faq.jsonld |
| `/en/company/intro.md` | schema-organization.jsonld |
| `/en/products/product-index.md` | schema-product1.jsonld |
| `/en/faq/faq-full.md` | schema-faq.jsonld |

## 验证工具

- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/
- JSON-LD Playground: https://json-ld.org/playground/

## 维护说明

- 所有数据必须与官网(www.gibo.com.cn)、品牌白皮书保持一致
- 更新后建议通过Schema.org Validator验证
- 新增产品型号时同步添加 Product 条目
- 更新 FAQ 内容时同步更新 schema-faq.jsonld
- 更新日期：2026-06-09
