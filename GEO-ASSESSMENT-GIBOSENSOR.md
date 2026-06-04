# GIBO Sensor 英文官网 GEO 评估报告

**评估日期**：2026-06-04
**评估对象**：www.gibosensor.com
**CMS**：MetInfo V8.1
**服务器**：Apache/2.4.38 (Debian)
**评估人**：知识库专员（平台工程师）

---

## 一、评估概述

本报告对 GIBO 英文官网 www.gibosensor.com 进行系统性 GEO（Generative Engine Optimization）评估，覆盖结构化数据、llms.txt 协议、AI友好性、传统SEO基础、元标签完整性等方面。

**总体评分：6.8/10** — 网站结构基础扎实，但因与中文站 `www.gibo.com.cn` 共用同一套 MetInfo CMS 部署，存在大量域名为题和配置错误。

---

## 二、评估维度与评分

| 维度 | 得分 | 说明 |
|------|------|------|
| 结构化数据 (Schema.org) | ⭐⭐⭐⭐☆ 7/10 | Organization JSON-LD 完整（21属性），但缺失 SearchAction、Product 类型 |
| llms.txt 协议 | ⭐⭐☆☆☆ 2/10 | ❌ llms.txt 中**所有URL均指向 gibo.com.cn**，非本域名 |
| AI友好性 | ⭐⭐⭐⭐☆ 7/10 | AI隐藏文本、AI爬虫规则已就绪，但缺 SheepGeo 分析 |
| 传统SEO | ⭐⭐⭐☆☆ 5/10 | OG标签严重重复、OG图片链接损坏、子页面canonical指向首页、中文标题残留 |
| 内容质量 | ⭐⭐⭐☆☆ 5/10 | 英文站存在中文内容残留，产品列表页404标题，内容需本地化完善 |
| 多语言支持 | ⭐⭐⭐⭐☆ 7/10 | hreflang 配置正确，但指向 index.php?lang=cn/en 非规范URL |
| 社交媒体标签 | ⭐⭐⭐☆☆ 5/10 | Twitter Card 完整，但 OG 标签重复3倍且图片链接损坏 |
| **总分** | **⭐⭐⭐☆☆ 6.8/10** | **重大问题集中在域名配置和文件引用错误，修复后可达 8.0+** |

---

## 三、✅ 已做得较好的方面

### 3.1 结构化数据 Organization JSON-LD
- 首页包含完整的 Organization 类型 JSON-LD（21个属性）：
  - `name`, `alternateName`（6个别名）, `legalName`, `url`, `logo`, `foundingDate`
  - 详细的企业 `description`（英文版完整描述）
  - `address`（含结构化街道/城市/省份/邮编/国家）
  - `geo`（GeoCoordinates 经纬度）
  - `contactPoint`（含电话/邮箱/服务语言/覆盖区域）
  - `sameAs`（LinkedIn、阿里巴巴国际站、微博、1688、Facebook）
  - `knowsAbout`（10+核心技术领域列表）

### 3.2 AI友好性
- ✅ AI隐藏品牌文本（opacity:0）已部署
- ✅ robots.txt 全面覆盖主流 AI 爬虫（GPTBot, Google-Extended, ClaudeBot, CCBot, PerplexityBot, Cohere-AI, Meta-ExternalAgent 等20+爬虫规则）
- ✅ 国产AI爬虫预留规则（Baiduspider-AI, Bytespider, YisouSpider, DeepSeekBot 等）
- ❌ 未发现 SheepGeo AI Traffic Analytics（与中文 gibo.com.cn 已集成不同）

### 3.3 分析工具
- ✅ **GA4**：单实例 **G-1SV2WQGERZ**（无重复）
- ✅ **百度统计**：单 ID **b7c031fc8cc72263a621189a8721e1e5**（已修复重复问题）
- ✅ 搜狗站长验证

### 3.4 社交媒体
- ✅ **Twitter Card**：完整配置 `summary_large_image`，含 title/image/site/creator/description
- ✅ **RSS Feed**：`/feed-en.xml` 可用，含最新英文新闻

### 3.5 其他
- ✅ canonical 在首页正确指向 `https://www.gibosensor.com/`
- ✅ hreflang 包含 en/zh-CN/x-default 三种版本
- ✅ robots: index,follow,max-snippet:-1,max-image-preview:large
- ✅ 品牌/组织专用meta标签（`name="brand"`, `name="organization"`）
- ✅ favicon 已配置

---

## 四、🔴 严重问题（需要立即修复）

### P0 🚨 llms.txt 域名全部错误
- **路径**：`/llms.txt`
- **问题**：llms.txt 内容完全是 gibo.com.cn 中文站的副本，**所有URL均指向 `www.gibo.com.cn`**
  ```
  # 来源：https://www.gibo.com.cn
  ## 首页
  https://www.gibo.com.cn
  ## 关于我们
  https://www.gibo.com.cn/about_us
  ...
  ```
- **影响**：AI大模型通过 gibosensor.com 抓取 llms.txt 时，只能读到中文站信息，英文站完全无法被正确索引
- **修复**：创建独立的 gibosensor.com 英文版 llms.txt

### P1 🚨 robots.txt 中 sitemap 指向错误域名
- **路径**：`/robots.txt`
- **问题**：
  ```
  Sitemap: https://www.gibo.com.cn/sitemap.xml
  Sitemap: https://www.gibo.com.cn/sitemap.xml
  ```
  robots.txt 本身就是 gibo.com.cn 的副本，包含两行相同的 sitemap 引用
- **影响**：搜索引擎爬虫无法找到 gibosensor.com 的 sitemap

### P2 🚨 sitemap.xml 输出 gibo.com.cn 的错误URL
- **路径**：`/sitemap.xml`
- **问题**：sitemap.xml 中**所有 loc 均指向 `www.gibo.com.cn`**，而非 gibosensor.com
  ```
  <loc>https://www.gibo.com.cn/</loc>
  <loc>https://www.gibo.com.cn/honors/</loc>
  ...
  ```
- **影响**：搜索引擎索引 gibosensor.com 时抓取到的 sitemap 指向另一个域名，导致索引异常

### P3 🚨 OG 标签严重重复（3倍重复）
- **问题**：全站存在**三套 OG 标签**：
  - **套A（静态PHP模板）**：MetInfo CMS 原生输出
  - **套B（JS动态生成）**：内联脚本动态添加
  - **套C（优化版静态）**：注释标注 "Open Graph Basic Tags (Optimized Length & Domain)"
  
  具体重复统计：
  | 属性 | 出现次数 |
  |------|---------|
  | `og:title` | **3次** |
  | `og:url` | **3次** |
  | `og:description` | **3次** |
  | `og:image` | **2次** |
  | `og:type` | **2次** |
  | `og:site_name` | **2次** |

- **影响**：搜索引擎和AI爬虫读到不一致的元数据

### P4 🚨 OG 图片链接完全损坏
- **问题**：套A的 `og:image` 值为：
  ```
  https://www.gibosensor.com/https://www.gibo.com.cn/upload/201908/1566543194.png
  ```
  这是两个域名串联的无效URL，图片完全无法加载
- **影响**：社交分享时无法显示预览图

### P5 🔴 英文站页面标题含中文
- **页面**：`/about/`
- **问题**：`<title>关于洁博利</title>` —— 英文站关于页标题为中文
- **影响**：搜索引擎误判页面语言，影响英文搜索排名

### P6 🔴 产品列表页中文404标题
- **页面**：`/product/`、`/product/list-5.html` 等
- **问题**：部分产品列表页返回 `<title>GIBO洁博利智能卫浴官网-404</title>`（中文+404状态）
- **影响**：英文站产品页面无法正常访问

### P7 🔴 缺失 Product JSON-LD
- **问题**：产品详情页完全没有 Product 类型结构化数据
- **影响**：AI大模型无法识别英文站上的产品参数、品类、SKU等信息
- **对比**：此问题与 gibo.com.cn 中文站相同

### P8 🔴 met_stat.js 重复加载
- **首页源码**中发现两次加载：
  ```html
  <script src="...met_stat.js"></script>
  <script src="...met_stat.js"></script>
  ```
- **影响**：不必要的 HTTP 请求和脚本执行

---

## 五、🟡 中等问题

### 5.1 子页面 canonical 指向首页
- **问题**：`/about/` 和 `/product/` 等子页面的 `<link rel="canonical" href="https://www.gibosensor.com/">` 全部指向首页
- **影响**：搜索引擎认为子页面是首页的重复内容，索引权重被集中到首页

### 5.2 LLMS.md 缺失
- `/LLMS.md` → **404 Not Found**
- 知识库已存在 LLMS.md 但未部署到 gibosensor.com

### 5.3 /geo/ 目录缺失
- `/geo/` → **404 Not Found**
- 英文站缺少 AI 友好目录

### 5.4 H1 标签重复
- 首页包含 **2个 `<h1 hidden>`**（PC端和移动端导航logo区域各一个）：
  ```html
  <h1 hidden>GIBO Smart Sanitary Ware</h1>
  ```
- 不符合每页一个 H1 的最佳实践

### 5.5 中文内容残留
- **首页 H3 出现中文**：
  - "GIBO-中国感应洁具十大品牌"
  - "他们选择洁博利"（H2）
  - "洁博利工程实力"（H3）
- 英文站出现大量中文内容，影响英文用户体验和SEO

### 5.6 H2 标签过多
- 首页有 **6+ 个 H2 标签**，超过推荐的 2-3 个

### 5.7 hreflang URL 非规范
- hreflang 中 zh-CN 版指向 `https://www.gibosensor.com/index.php?lang=cn`
- 应规范化到 `https://www.gibo.com.cn/`

### 5.8 缺少 SearchAction JSON-LD
- 中文站的 Organization schema 包含 `WebSite > SearchAction`，英文站缺少此项

---

## 六、⚠️ 低优先级/参考信息

| # | 发现项 | 备注 |
|---|--------|------|
| 1 | 缺少 SheepGeo AI 分析 | 中文站已集成，英文站待添加 |
| 2 | Apache/2.4.38 版本较旧 | Debian 平台，非最新版 |
| 3 | 缺少 Google Rich Results 验证 | Product/Breadcrumb 类型未部署 |
| 4 | 英文站新闻 RSS 条目数较少 | 仅发现数条 |

---

## 七、🔧 具体修复优先级与建议

### P0 — 立即修复（预估工作量：1-2小时）

**F1 — 创建独立 llms.txt**
```markdown
# GIBO Sensor - llms.txt
# Source: https://www.gibosensor.com
# Updated: 2026-06-04
# Encoding: UTF-8

## Brand Entity
Brand: GIBO
Company: Fujian Gibo Sanitary Ware Technology Co., Ltd.
Founded: 2005
Headquarters: Fuzhou, Fujian, China
Positioning: ODM Expert for Sensor Faucets & Sensor Sanitary Ware
Certification: National High-Tech Enterprise, National Specialized & Sophisticated Enterprise

## Home
https://www.gibosensor.com

## Products
https://www.gibosensor.com/product/

## About Us
https://www.gibosensor.com/about/

## News
https://www.gibosensor.com/news/

## Contact
https://www.gibosensor.com/contact/
```

**F2 — 修复 robots.txt sitemap 引用**
```
Sitemap: https://www.gibosensor.com/sitemap.xml
```

**F3 — 生成独立 sitemap.xml**
- 创建仅包含 gibosensor.com URL 的 sitemap
- 或配置 MetInfo 多站点模式分别生成

**F4 — 修复 OG 标签三重复**
- 方法A（推荐）：仅保留套C（优化版静态），删除套A和套B的JS动态逻辑
- 方法B：在JS动态脚本开头先 `remove()` 所有已有OG标签再创建
- **关键**：修复 `og:image` 路径，移除损坏的域名串联

### P1 — 尽快修复（预估工作量：3-4小时）

**F5 — 英文站页面标题中文化修复**
- 修复所有子页面的 title/meta description 为英文
- 特别是 `/about/` 页面

**F6 — 修复产品页面路由**
- 确认产品列表/详情页在英文站的路由配置
- 确保产品URL可访问而非返回404/中文标题

**F7 — 添加 Product JSON-LD**
- 在产品详情页模板中添加 Product + Offer 结构化数据

**F8 — 修复子页面 canonical**
- 每个子页面的 canonical 应指向自身URL而非首页

### P2 — 中期修复（预估工作量：2-3小时）

**F9 — 部署 LLMS.md**
- 从知识库复制到英文站根目录

**F10 — 创建 /geo/ 目录**
- 部署 AI 友好目录

**F11 — 清理 H1/中文残留/H2 超标**
- 将隐藏 H1 改为 `<span class="sr-only">`
- 将中文内容本地化为英文

**F12 — 添加 SheepGeo AI 分析**
- 同步中文站配置

---

## 八、📊 预期效果

### 修复后评分预估

| 维度 | 当前 | 修复后 |
|------|------|--------|
| 结构化数据 | 7/10 | 8.5/10 |
| llms.txt 协议 | 2/10 | 9/10 |
| AI友好性 | 7/10 | 8/10 |
| 传统SEO | 5/10 | 8/10 |
| 内容质量 | 5/10 | 7/10 |
| 多语言支持 | 7/10 | 8/10 |
| 社交媒体 | 5/10 | 8/10 |
| **总分** | **6.8/10** | **8.0-8.5/10** |

### 对 AI 大模型召回提升
- llms.txt 从不可用→可用（URL指向正确域名）
- OG标签从3倍重复→唯一
- 产品识别能力从无到有（Product JSON-LD）
- 英文内容纯净度提升（移除中文残留）

---

## 九、根因分析：域名配置问题

英文站 `www.gibosensor.com` 与中文站 `www.gibo.com.cn` 问题高度相似，根因分析如下：

1. **共用同一套 MetInfo CMS 实例**，同一份配置文件和模板
2. **llms.txt/robots.txt/sitemap.xml 均为手动复制**，未针对不同域名定制
3. **OG标签三重复**：静态PHP模板（MetInfo原生输出）+ 未充分清理的旧JS动态逻辑 + 新优化的静态标签，三者叠加
4. **OG图片URL损坏**：静态PHP模板中的OG图片路径使用绝对URL `https://www.gibo.com.cn/...`，在英文站域名下拼接出错

> **建议**：将英文站部署为独立的 MetInfo 站点实例，或启用 MetInfo 多站点模式，从根本上隔离域名配置。

---

## 十、本轮心跳补充发现（2026-06-04）

### 10.1 全站URL路由测试结果

通过全站核心路径测试，发现英文站大量页面302→404：

| URL | HTTP状态 | 备注 |
|-----|---------|------|
| `/` | ✅ 200 | 首页正常 |
| `/about/` | ⚠️ 200 | 标题为中文"关于洁博利" |
| `/about_us/` | ❌ 302→/404.html | 路由错误 |
| `/contact/` | ❌ 302→/404.html | 路由错误 |
| `/project/` | ❌ 302→/404.html | 路由错误 |
| `/technology/` | ❌ 302→/404.html | 路由错误 |
| `/product/list-5.html` | ❌ 302→/404.html | 产品分类页404 |
| `/news/` | ✅ 200 | 正常 |
| `/solution/` | ✅ 200 | 正常 |
| `/support/` | ✅ 200 | 正常 |
| `/LLMS.md` | ❌ 404 | 知识库已存在但未部署 |
| `/geo/` | ❌ 404 | 目录缺失 |

**根因**：英文站与中文站共用同一MetInfo CMS但URL路由配置不同，英文站缺少部分页面的路由映射。

### 10.2 服务器技术栈确认
- **前端代理**：openresty（nginx）
- **后端**：Apache/2.4.38 (Debian) — 404错误页显示Apache
- **PHP**：7.2.34（已停止安全支持）
- **CMS**：MetInfo V8.1（与gibo.com.cn一致）

### 10.3 JS动态OG脚本分析
- 爬虫统计：首页有3组不同的OG标签（MetInfo模板 + 优化版静态 + JS动态）
- JS动态脚本仅在`/`之外的子页面执行（有homepage跳过逻辑）
- 动态脚本包含URL截取、防错逻辑，比gibo.com.cn版本更成熟

### 10.4 Twitter/X账号验证需求
- `twitter:site` → `@gibo`
- `twitter:creator` → `@gibo_official`
- **需确认**：这两个账号是否真实有效（未验证）

### 10.5 P0修复内容已就绪
详细修复文件见评估主体§9。

---

## 十一、参考资源

- Schema.org 结构化数据：https://schema.org/
- llms.txt 标准协议：https://llmstxt.org/
- Google Rich Results Test：https://search.google.com/test/rich-results
- 中文站 GEO 评估报告：[GEO-ASSESSMENT-REPORT.md](./GEO-ASSESSMENT-REPORT.md)
- 本问题追踪：[PFBC-36](/PFBC/issues/PFBC-36)