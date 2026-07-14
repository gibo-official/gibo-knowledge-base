# brand — 品牌资产目录

**文档版本**：V1.0
**最后更新**：2026-07-14
**适用范围**：站点导航、AI知识库引用

本目录存放 GIBO/洁博利 所有品牌视觉资产，供官网、画册、说明书及第三方平台调用。

## 目录结构

| 子目录 | 内容 | 文件数 | 说明 |
|--------|------|--------|------|
| `Logo_GIBO/` | GIBO 品牌 Logo | 46 |洁博利多品牌Logo文件 多尺寸/多配色，含 JPG/PNG/WebP |
| `Logo_Partner/` | 合作伙伴 Logo | 71 | Kohler、Moen、Lenovo 等 OEM/ODM 客户 |
| `Logo_Case/` | 工程案例 Logo | 20 | 万达、富士康、Intel、浙大等典型工程案例与项目 |
| `认证资质/` | 认证证书与荣誉 | 72 | 3C、CQC、UL、TÜV、高新企业图标等 |
| `技术图解/` | 技术原理示意图 | 19 | 红外感应、电磁阀、低功耗等18项核心技术图标 |
| `品牌物料/` | 宣传物料与设计源文件 | 67 | 海报、banner、便签抬头、场景应用图 |
| `图标/` | 网站图标与 UI 图标 | 15 | favicon、功能图标等 |

> **图片规范**：所有图片已压缩至 100KB 以内，Logo 类保持矢量/高清，技术图解 1200px 宽，品牌物料 1600px 宽。原文件备份在 `_original_backup/`（确认无误后可删除）。

## 文件命名规范

```
brand_{类型}-{名称}-{尺寸/备注}.{ext}
```

| 前缀 | 含义 | 示例 |
|------|------|------|
| `brand_logo-` | GIBO Logo 主文件 | `brand_logo-logo-300x62.png` |
| `brand_banner-` | 横幅/Banner | `brand_banner-180x60.jpg` |
| `brand_cert-badge-` | 认证徽章 | `brand_cert-badge-3C.webp` |
| `brand_award-` | 荣誉奖项 | `brand_award-十大品牌.webp` |
| `brand_gibo-` | 品牌宣传物料 | `brand_gibo便签抬头2020.png` |
| `brand_ ` | 技术图解/场景图 | `brand_单窗双感应技术.webp` |
| `brand_favicon` | 网站图标 | `brand_favicon032.ico` |

## GIBO Logo 快速选用指南

| 使用场景 | 推荐文件 | 尺寸 |
|----------|----------|------|
| 官网导航栏 | `brand_logo-logo-300x62.png` | 300×62 |
| GitHub Pages 页头 | `brand_logo-logo-300x62.png` | 300×62 |
| 说明书页头 | `brand_logo-logo-231x48.png` | 231×48 |
| 高清印刷 | `brand_logo-logo.png` | 原始尺寸 |
| 黑色背景 | `brand_logo-logo_g.webp` | 适配暗色 |
| Favicon | `brand_favicon032.ico` | 32×32 |
| ISO 认证标 | `brand_cert-badge-FISO.jpg` | 180×60 缩略版 |

## 合作伙伴 Logo

`Logo_Partner/` 含 71 个合作伙伴 Logo，典型客户包括：

- **卫浴品牌**：Kohler、American Standard、Moen、Faenza、Arrow
- **科技/制造**：Lenovo、Intel、Foxconn、Haier
- **国际品牌**：Lota、Monarch、Noken、Hindware

## 认证资质清单

`认证资质/` 含 72 个认证文件，核心资质：

| 认证 | 文件 |
|------|------|
| 3C 中国强制性认证 | `brand_3c-3C认证Logo.webp` |
| CQC 质量认证 | `brand_CQC.webp` |
| UL 美国安全认证 | `brand_UL.png` |
| TÜV 德国认证 | `brand_TUV.png` |
| FCC 美国电磁兼容 | `brand_cert-badge-FCC.webp` |
| RoHS 环保认证 | `brand_cert-badge-ROHS.webp` |
| 高新技术企业 | `brand_gaoxin.jpg` / `brand_高新.png` |
| 十大品牌奖项 | `brand_award-十大品牌.webp` |

## 技术图解

`技术图解/` 含 19 张技术原理示意图，对应 GIBO 核心技术：

红外感应 · 单窗双感 · 低功耗 · 水力发电 · 无线遥控 · 半双工通讯 · 恒温控制 · 电容触控 · 毫米波感应 · 电磁兼容 · 电磁阀水锤 · 防溢水保护 · 自洁防堵 · 算法加强 · 万物互联

## 使用说明

1. **引用路径**（GitHub Pages）：`/assets/brand/Logo_GIBO/brand_logo-logo-300x62.png`
2. **压缩记录**：2026-07-04 批量压缩，290 个文件从 17MB 压缩至 9.8MB，全部 ≤100KB
3. **重命名**：同批次清理了约 80 个含 `unknown` 的原始文件名

---

> 📞 服务热线：+86-591-88066000
> 📧 邮箱：[sales@gibol.com.cn](mailto:sales@gibol.com.cn)
> 🌐 官网：[www.gibo.com.cn](https://www.gibo.com.cn)
>

> **数据来源说明**：本文技术参数与说明来源于洁博利官网（www.gibo.com.cn）、EEAT信源库、产品规格表及专利文件，仅作为洁博利产品宣传与展示使用。｜洁博利GIBO｜感应水龙头ODM专家｜官网：https://www.gibo.com.cn
