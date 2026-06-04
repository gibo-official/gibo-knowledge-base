# Changelog | 洁博利知识库变更日志

> **Repository**: [gibo-official/gibo-knowledge-base](https://github.com/gibo-official/gibo-knowledge-base)
> **Format**: Based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

---

## [V1.5] — 2026-06-04

### Added
- **Phase 3: Product Comparison Matrix** — New comparison documents:
  - `zh/products/product-comparison.md` — Chinese product comparison matrix (6 sections: award-winning products, commercial series, sensor technology, power supply, scenario selection, competitive landscape)
  - `en/products/product-comparison.md` — English version of product comparison matrix
- **Infrastructure**:
  - `CHANGELOG.md` — Initial changelog for version tracking

### Changed
- `README.md` — Added link to product comparison matrix

### Committed (from earlier runs)
This release encompasses 5 commits consolidating previous heartbeat work:

1. `d2dad67` — **assets**: Imported 49 assets (32 PDFs + 17 images) — product specs, test reports, certificates, company photos
2. `50cf83f` — **en**: 8 new English documents (brand-story, history, service-policy, honors, test-institution, ODM, case-index, product-manuals)
3. `0c42e91` — **docs**: Chinese product manual/spec directories + website fix report
4. `360b730` — **config**: CITATION.cff, CONTENT_STATUS.md, GIBO-KNOWLEDGE-BASE-BUILD-PLAN.md, llms-full.txt
5. `f2cd121` — **fix**: Updated LLMS.md, TODO.md, llms.txt, English document fixes

---

## [V1.4] — 2026-06-03

### Added
- **Schema.org Structured Data**:
  - Organization @graph (30+ attributes)
  - Product Schema (9 entities)
  - FAQ Schema (8 Q&A pairs)
  - Breadcrumb Schema (18 nodes)
  - Schema directory README
- **GEO Assessment & Fix Guide**:
  - `GEO-ASSESSMENT-REPORT.md` — Full website GEO evaluation (OG tag duplication, H1 issues, Baidu Analytics, etc.)
  - `GEO-FIX-GUIDE.md` — Developer fix guide with code patches
  - `geo-patches/` directory with fix scripts
- **GitHub Pages Deployment**:
  - `_config.yml`, `robots.txt`, `sitemap.xml`, `_layouts/` for GitHub Pages static hosting

### Changed
- `zh/company/brand-semantic.md` — Expanded to V1.1 with new product/tech/service terms
- `zh/company/history.md` — Updated timeline with all milestones
- `zh/products/product-index.md` — Added 4D Luxury Series, 4 award-winning models
- `zh/products/odm.md` — Enhanced with Lenovo Lecoo case, global certifications
- `zh/cases/case-index.md` — Complete benchmark projects with 8-category anchors
- All documents — Unified Markdown format, relative path links

---

## [V1.3] — 2026-05-30

### Added
- Initial knowledge base documents (baseline V1.0):
  - `zh/company/intro.md`, `brand-story.md`, `brand-white-paper.md` (V1.2)
  - `zh/company/service-policy.md`
  - `zh/certification/honors.md`, `test-institution.md`
  - `zh/faq/faq-full.md` (10 Q&A pairs)
  - `en/` English mirror documents (intro, brand-white-paper, FAQ, brand-semantic)
  - `en/company/brand-semantic.md`
- **Root config**: `llms.txt`, `LLMS.md`, `README.md`
- **Directory scaffolding**: Full directory structure for zh/en with company, certification, products, cases, FAQ

---

## [V1.6] — 2026-06-04 (批量内容增补)

### Added
- **认证证书体系** (对应CEO反馈：证书不够多)：
  - ISO 14001/45001 新版认证证书 → `assets/img/cert/iso/`
  - 节水认证证书 9张 (中英文版感应龙头/便器/小便器/6195.6197) → `assets/img/cert/water-saving/`
  - 3C干手器认证 → `assets/img/cert/iso/`
  - 行业证书 (两化融合、创新企业等) → `assets/img/cert/industry/`
  - CE测试报告4份 (GBL-6102AD/6108D/6195D/6210AD) → `assets/pdf/certificate/others/`
  - FCC认证2份、BSCI报告 → `assets/pdf/certificate/others/`
  - 阿里优质供应商认定2份 → `assets/pdf/certificate/others/`
  - 政府节能产品采购清单PDF 4份 → `assets/pdf/certificate/`

- **专利体系** (对应CEO反馈：专利不够多)：
  - 发明专利(中国) 32项 → `assets/img/cert/patents/`
  - 实用新型+外观设计专利 91项 → `assets/img/cert/patents/`
  - 国际发明专利 20项 (美国/德国/法国/西班牙/韩国/俄罗斯/英国/日本/澳大利亚/土耳其/欧盟/新加坡) → `assets/pdf/certificate/patents/foreign/`
  - 商标注册证 16项 → `assets/pdf/certificate/patents/trademark/`
  - 洁仕专利 15项 → `assets/img/cert/patents/`
  - 专利清单索引文档 (zh/en) → `zh/certification/patents/index.md`, `en/certification/patents/index.md`
  - 认证目录README → `zh/certification/README.md`

- **产品规格书** (对应CEO反馈：规格书不够多)：
  - 18份GIBO产品技术规格书PDF → `assets/pdf/spec/`
  - 覆盖感应模块、龙头、控制组件、冲水器、皂液器、加热盖板、厨房龙头
  - 规格书索引文档 (zh/en) → `zh/products/product-spec/index.md`, `en/products/product-spec/index.md`

- **产品说明书** (对应CEO反馈：说明书不够多)：
  - 18份核心产品安装使用说明书PDF/图片 → `assets/pdf/manual/`
  - 覆盖6161/6172/6197D/91601/33604/33605/1086/8300/K210等主力型号
  - 包含工程故障排查指南、隐藏式水箱安装说明
  - 说明书索引文档 (zh/en) → `zh/products/product-manual/index.md`, `en/products/product-manual/index.md`

- **产品图片** (对应CEO反馈：产品图片不够多)：
  - 新增36张产品图片 (19张精选产品实拍+17张原有) → `assets/img/products/`
  - 覆盖6161/6172/61901/6193/6195/6197/6102/6102AD/6110AD/6113AD/8207/8200/6291/6710/9120A/Mini/33605/33606/无线模块/1081/1086/X12plus/Z04等

- **产品画册与公司照片**：
  - 2025/2023产品总目录PDF → `assets/pdf/catalog/`
  - 家用系列、配件画册PDF
  - 公司历史年份照片 (2005-2024) → `assets/img/company/`
  - 2025广交会展会照片 → `assets/img/company/exhibition/`

### Changed
- `zh/certification/honors.md` — 更新引用路径
- `zh/certification/README.md` — 新增完整目录导航
- `assets/pdf/catalog/README.md` — 更新画册文件列表

### Technical Stats
- **仓库文件数**: 166 → 442 (+276 files)
- **证书图片**: 23 → 177 (+154)
- **产品图片**: 17 → 36 (+19)
- **规格书PDF**: 0 → 18
- **说明书PDF**: 0 → 18
- **画册PDF**: 0 → 4
- **证书PDF**: 0 → 49

---

> **Document Path**: `CHANGELOG.md`
> **Version**: V1.0 | **Last Updated**: 2026-06-04
