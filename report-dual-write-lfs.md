# 关键参数「图+表双写」缺口扫描 + Git LFS 体积评估报告

> 生成时间：2026-07-21 · 范围：全库 `*.md` 776 个 + `assets/` 5612 个文件
> 关联需求：P2 增强项「关键参数图+表双写」「评估 assets/ 大图启用 Git LFS」

---

## 一、关键参数「图+表双写」缺口扫描

### 1.1 扫描方法
- 识别两类**参数图信号**：`alt` 文本或图片文件名含「尺寸图/规格/参数/认证/图纸/接线/爆炸图/曲线/spec/dimension/drawing/cert/table…」等关键词 → 视为承载结构化参数的图片。
- 对每张参数图，向前/后各 15 行扫描是否存在 Markdown 表格（`|…|…|`）；若无 → 标记「需补参数表」。
- 同时统计**空 alt 图片**（`![](path)`）规模，作为「图片内嵌文字风险」的代理指标（OCR/切片失败即丢失语义）。
- 跳过：`http(s)://` 外链、icon/logo/banner/背景/箭头等装饰图、代码块内引用。

### 1.2 扫描结果

| 指标 | 数值 |
|---|---|
| 扫描 `*.md` 文件 | 776 |
| 图片引用总数 | 3530 |
| 其中参数图（spec 信号） | 2（含表） |
| 参数图但附近无表格（需补表） | **0 处** |
| 空 alt 图片 | **3482 张（98.6%）** |

按目录的空 alt 分布：

| 目录 | 空 alt 张数 |
|---|---|
| zh | 1617 |
| en | 1099 |
| assets | 766 |
| 其他（solutions/whitepapers/…） | ~0 分散 |

### 1.3 结论

✅ **已知参数图（尺寸图/规格图/认证图）均已配套文字表，图+表双写达标。**
- 例：`zh/products/product-manual/66xx感应水箱CN_说明书.md` 的「产品尺寸图」后紧跟 `370 / 单位:mm` 文字与「技术参数」表格；`en/products/product-spec/BC-31519-spec.md` 含 5 张 `Parameter | Specification` 表。
- `product-spec/` 体系（GBL-6128 49 行表、G33608 47 行表等）已把核心参数文本化，降低对图片的依赖。

⚠️ **系统性风险：98.6% 的图片缺少 `alt` 文本。**
- 一旦图片内嵌文字（尺寸图/认证标识/参数截图）在 OCR 或向量切片时失败，参数与语义将整体丢失，且不利于可访问性与 SEO。
- 其中确含内嵌文字的高危对象：`assets/品牌物料/6195_尺寸图_*.png`（3.4MB 栅格尺寸图）、`assets/Cases/洁博利工程案例*.png`（4–5MB）、各 `catalogs/*.pdf`。

### 1.4 行动建议（已部分落地）
1. **`docs-style-guide.md` 已增补两条硬规则**（见下）：① 参数图必须「图+表双写」；② 图片必须带描述性 `alt`。
2. **回填 alt 文本**：优先处理 `product-spec/`、`product-manual/`、`faq/product/` 等受管区的参数图（当前仅 49 张非空 alt，含 4 张参数图）。
3. **将 alt 必填纳入 CI（WARN 级，待本批稳定后开启）**，逐批收敛空 alt 比例。

---

## 二、Git LFS 体积评估（assets/ 大图）

### 2.1 统计结果

| 指标 | 数值 |
|---|---|
| `assets/` 文件总数 | 5612 |
| `assets/` 总体积 | **363.1 MB**（380,691,191 B） |
| LFS 目录建议线（100 MB） | ⚠️ **已超线 → 建议评估启用** |
| 单文件 >50 MB | 0（最大 10.5 MB） |
| ≥1 MB 文件 | 43 个（累计 113.4 MB） |

按扩展名：

| 扩展名 | 数量 | 体积 |
|---|---|---|
| .jpg | 2068 | 180.4 MB |
| .png | 3135 | 130.2 MB |
| .pdf | 7 | 32.6 MB |
| .md | 216 | 6.8 MB |
| .webp | 53 | 2.9 MB |
| .xlsx/.xls | 8 | 3.2 MB |
| 其他(svg/gif/ico/json…) | <200 | <1 MB |

体积最大的文件（均为 🟡 1–10 MB，无 🔴）：

```
10.5 MB  assets/catalogs/catalog_2023-en.pdf
 5.7 MB  assets/catalogs/catalog_2022-cn-household-3qu.pdf
 5.6 MB  assets/Cases/洁博利工程案例大全 (19).png
 5.4 MB  assets/Cases/洁博利工程案例_辽宁舰.png
 3.4 MB  assets/品牌物料/6195_尺寸图_03.png
 3.4 MB  assets/品牌物料/6195_尺寸图_02.png
...
```

### 2.2 评估结论与建议

**结论：当前 `assets/` 363 MB 已超过 100 MB 的 Git LFS 建议启用线；虽然无单文件 >50 MB，但目录体量已具规模，克隆成本随协作者增多而显著上升。**

**建议（中长期，非本批立即执行）：**
1. 在仓库根新增 `.gitattributes`，对大二进制启用 LFS：
   ```
   assets/**/*.jpg    filter=lfs diff=lfs merge=lfs -text
   assets/**/*.jpeg   filter=lfs diff=lfs merge=lfs -text
   assets/**/*.png    filter=lfs diff=lfs merge=lfs -text
   assets/**/*.webp   filter=lfs diff=lfs merge=lfs -text
   assets/**/*.pdf    filter=lfs diff=lfs merge=lfs -text
   assets/**/*.gif    filter=lfs diff=lfs merge=lfs -text
   ```
2. 历史文件迁移（一次性、会改写对象，需团队知晓）：
   ```
   git lfs migrate import --include="assets/**/*.{jpg,jpeg,png,webp,pdf,gif}" --everything
   ```
3. **暂缓条件**：若短期仅单人维护、克隆频率低，可暂缓；一旦协作人数 ≥3 或新增视频/高清图册，立即启用。
4. 本批**不执行** LFS 迁移，保持 `git` 历史与云端一致，避免未协商的强制推送。

---

## 三、本批交付物

| 文件 | 说明 |
|---|---|
| `REPORT-dual-write-lfs.md` | 本报告 |
| `docs-style-guide.md`（更新） | 增补「图+表双写」+「图片必带 alt」两条硬规则 |
| `scripts/ci_check.py`（后续增强） | 计划增加 alt 必填 WARN 检查，逐批收敛空 alt |

> 状态：扫描与评估完成；LFS 启用待你确认后单独执行（不在本批提交内）。
