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

> **Document Path**: `CHANGELOG.md`
> **Version**: V1.0 | **Last Updated**: 2026-06-04
