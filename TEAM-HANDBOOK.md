# 洁博利 GIBO 知识库 · 团队资产总册（Memory + Skills + 工具 + API）

> 目的：汇总自项目启动（2026-06-16）至 2026-07-31 的全部**工作记忆、所用技能、PDF 工具、相关 API / 连接器**，供团队成员接手与共享使用。
> 仓库：`gibo-official/gibo-knowledge-base` ｜ 活副本：`D:/Github/gibo-knowledge-base` ｜ 站点：`https://gibo-official.github.io/gibo-knowledge-base/`
> 本册为内部运维手册（中文），独立放置，不接入 README / MAINTENANCE 索引。

---

## 一、完整记忆清单（每日日志索引，2026-06-16 → 2026-07-31）

| 日期 | 当日主要工作（取自日志 `## ` 章节） | 关键产出 / 提交 |
|---|---|---|
| 06-16 | 初始失效链接修复 | 失效 `.md` 链接 342→135（安全层级修正 207 处）；1116 个图片/PDF 资产链接失效（资产缺位非逻辑错误） |
| 07-07 | GitHub 云端同步到本地 | 拉取远端至本地工作区 |
| 07-14 | 失效链接修复；两份科技项目 PDF→MD（pdftotext）；英译本；同步 GitHub；仓库体积诊断（GitHub API 2.69GB）；本地清理 | `1193f26`；发现超大 blob（269MB 灯具 PDF 等） |
| 07-15 | 云端整库重置执行 | force push 清理历史大 blob，仓库降至 ~379MB |
| 07-17 | 图片 / 资产整理（白底图、透明图提取与去重） | 按 SHA256 内容去重 |
| 07-18 | 白底图/透明图提取（`D:\Product`）；尺寸图方向修正；横版 PDF 未应用 Rotate 诊断 | 13 张左置竖排标题栏图需横转 |
| 07-20 | 尺寸图方向修正；批量旋转 11 张尺寸图+BOM 图；6172 文字替换「唯有家卫浴」→「福建洁博利…」；电商主图 `IMT-` 前缀删除；GEO 优化第 4-5 步 + 本地推云端 | 推云端 |
| 07-21 | 两目录图片批量压缩 ≤150KB；详情图按型号整合；方案图按内容命名；OCR 诊断；**企业微信文档读取能力核实**（wecom-cli 无 get_doc_content）；高品质感应洁具判断标准 GEO 优化；FAQ 主题拆分 + GLOSSARY/CI/规范文档 + 图/表双写与 LFS 评估 | 提交推送 |
| 07-23 | 同步核查（云端 vs 本地差异 + 容量）；历史大文件清理 + 强制推送；GEO 知识库完整评估 | 授权删 `.git` 残留 blob 并强推 |
| 07-24 | 执行 P0-GEO 三项；faq.md vs faq-geo-optimized.md 对比；FAQ 按主题拆分执行；**Markdown 逐字符换行损坏诊断与修复**（催生 `md-charwrap-repair` 技能） | 修复换行损坏 |
| 07-25 | FAQ 结构回退为 3 文件；README 全量核查 + assets 损坏修复；参数图双写；**图片 alt 补全（`md-img-alt-add` 新建）**；assets 24 个 README 重写；**FrontMatter 合并（`md-fm-dedup` 新建/增强）**；keywords 改分类名；tags 去型号；`geo-diag-report` 适配为知识库 GEO 审计；技能固化 | 多技能固化 |
| 07-27 | LLMS.md 过度合并修复；全量诊断 + 分步计划；Phase 0-4 执行（过度合并清零 / 结构规范 / 元数据双语 / 内容完整 / GEO 增强死链治理） | `d0ee953`→`2ffdac0` 多提交 |
| 07-28 | 第三轮体检；完整目录索引生成；第四~八轮（清理 / 死链清除 / 画册案例入库 / GEO 业务单元拆分 / 认证收敛组件去重）；仓库 390MB 无 LFS 诊断；新增 `.gitattributes`（LFS 对未来生效） | `fde3ee7`…`d99fd8f` |
| 07-29 | case-index V2.1；英文 case-index 同步；展会 README V2.0；GEO 业务单元拆分启动；样板 V1.1 修正；学校场景融合 + 新建学校节水改造白皮书；内链回链索引补完（消孤岛）；两份方案书口径统一；手动改名链接同步 + 文件 B 迁移至 technology；**波总立常驻规则：文件事件三提示**；应用三提示新增 6710/6712 强制英文说明书 | 多提交至 `eb1b21b` 等 |
| 07-30 | 红外感应线路板技术原理解析英文翻译；**GitHub Pages 规划与启用**；GEO 因子库重命名完善 + §2.8 认证因子落地 | `fc48340`→`c424eaa` |
| 07-31 | 营业执照注册信息补全（V1.1）；EEAT/ESG 文件新建（V1.0→V1.4 多轮强化：可核验查询页 / 资质 / 院校合作 / 专利商标查询 / 行业协会 / 社媒 / 规上链接 / 4 款获奖）；intro.md V1.2 七维度扩写；intro.md 移除本地路径与百度百科信源 | `ff2db37`…`26ec890` |

> 长期记忆（精炼决策）见第二章；完整原文在 `.workbuddy/memory/MEMORY.md` 与各 `YYYY-MM-DD.md`。

---

## 二、常驻规则与拍板决策（来自 MEMORY.md）

### 2.1 文件事件三提示（波总 2026-07-29 立，常驻）
每次**新增 / 删除 / 移动改名**文件，必须暂停并问：
1. **更新内链**：是否扫描并更新所有仍指向旧路径/旧文件名的内链（README 索引、兄弟文档关联、product-index / tags-index / bilingual-pairing-report 等）？
2. **解决孤岛**：是否同步更新索引/导航/回链，消除孤岛（新文件被引用、旧文件删除后无悬空链接）？
3. **新增英文版**：该中文明细文件是否需同步翻译英文版到 `en/` 对应目录？
> 不可只做一部分（如只改链接不补英文、只移动不修路径）。

### 2.2 口径统一（波总拍板 2026-07-29）
- **产销规模官方口径**：年产能 **100 万台套**、累计产销 **500 万+ 套**、出口 **40+ 国家地区**、**2000+ 标杆工程**、国内 **60000+ 用户**。（年产能 ≠ 累计产销）
- **沟槽式规格口径**：适用温度 0~55℃、供电 AC220V（保留 DC24V 备选）、价格 1000 元/套。学校节水白皮书「参数口径说明」框已写"2026 统一口径"。

### 2.3 GEO 优先策略（波总 2026-07-30 拍板）
- 站点只服务 **AI / 大模型 / 搜索引擎爬取**（`sitemap.xml` + `llms.txt` + 每页结构化数据）；人类浏览不是目标。
- 内部 `.md` 链接线上 404（Jekyll 把 `foo.md`→`foo.html`，源 `.md` 不发布），**不影响 AI 索引** → **不改 `.md`→`.html`**。
- **不启用 Gitee Pages**（Gitee 仅作代码镜像/备份；且曾因仓库 >500MB 同步失败）。

### 2.4 推送与环境怪象
- 远程仅 `origin`（GitHub: `gibo-official/gibo-knowledge-base`），无 Gitee 远程（Gitee 仅镜像）。
- ⚠️ 沙箱不持久化 `refs/remotes/origin/main` 远程跟踪引用 → `git status` 显示"领先 origin N"是**假象**。核实真值用：`git ls-remote origin main`。
- 提交规范：优先新建 commit，不 amend；提交前走 `git-safe-sync` 校验。

### 2.5 已知遗留（待拍板，未提交）
- `6712淋浴器CN_说明书.md`、`67xx沟槽式…CN_说明书.md` 旧名删除未提交；`series-sensor-components.md` 预存改动未提交。
- `6710沟槽式节水控制器CN_说明书.md` 正文旧噪音：H1 带 `ZZZ_` 前缀、文档版本 V1.0/2026-07-10 与 frontmatter V1.1 矛盾、产品信息表误用 DC12V/节水率60%。
- 回收站有 **6-16 旧仓库副本**（`E:/$RECYCLE.BIN/.../$R4RLR6L`，含 .git + 173 md，比线上 V1.3 旧）→ **勿恢复覆盖**；线上站点不受影响。

---

## 三、Skills 清单（全部 20 项 + 本项目新建/增强标注）

> 当前全部位于**用户级** `~/.workbuddy/skills/`，项目级 `.workbuddy/skills/` 为空。团队共享建议：把"核心·本项目资产"复制到 `gibo-knowledge-base/.workbuddy/skills/` 随仓库分发。

### 3.1 核心 · 本项目新建 / 深度增强（强建议进项目级）
| 技能 | 状态 | 用途 |
|---|---|---|
| `md-charwrap-repair` | **本项目增强至 v4** | 修复逐字符换行 / 字间空格 / 坏表 / 折叠表四类损坏；保留 FM+代码块；幂等（再跑无差异） |
| `md-img-alt-add` | **本项目新建** | 图片补全 alt（产品名+上级标题）；含 `add_img_alt_standard.py` 标准/证书/目录类变体 |
| `md-fm-dedup` | **本项目新建/增强** | FrontMatter 字段去重合并；含 `extract_catalog_map.py`（实时解析 product-catalog 型号→分类映射）、`normalize_keywords`/`normalize_tags`/`is_model_token`（去型号、填分类词） |
| `git-safe-sync` | 复用 | 大批量改名/迁移/改链后提交推送前安全校验（远程分叉、MM 漏改、游离文件、grep 退出码误判） |
| `markdown-broken-link-fixer` | 复用 | 扫描修复 Markdown 失效链接（本地 .md / 图片 / PDF / 相对层级 / PDF→MD 迁移对齐） |
| `image-optimizer` | 复用 | 批量压缩图片（单文件 ≤100KB；备份原图、PNG→JPG、保留中文命名） |
| `markdown-header-footer-standardizer` | 复用 | 页眉（文档版本/最后更新/适用范围）页脚（数据来源+公司信息）标准化 |
| `geo-diag-report` | **本项目适配** | 品牌 GEO 诊断，已适配为"知识库 GEO 审计"（检索增强 + 虚拟仿真） |
| `gibo-vidu-product-video` | **GIBO 专属** | 洁博利产品视频生成（Vidu 图生/参考生视频，固化参数与 dry-run） |

### 3.2 内容分发（按需，依赖各平台 API）
`wechat-publish`（微信服务号）· `xhs-publish`（小红书）· `zhihu-publish`（知乎）· `wechat-article-pro`（公众号文章）· `buffer-graphql-publish`（Buffer LinkedIn/Facebook）· `qq-email`（QQ 邮箱 SMTP）

### 3.3 辅助
`doc-text-extract`（Word .doc/.docx 文本提取）· `image-orientation-ocr-fallback`（图片方向纠正）· `prompt-engineering-expert`（提示词工程）· `vidu-video-generate-2`（通用 Vidu 视频）

---

## 四、PDF 工具

| 工具 | 用途 | 项目中的实际使用 |
|---|---|---|
| `pdftotext`（poppler-utils） | `pdftotext -enc UTF-8` 抽取 PDF 正文为文本 | 两份科技项目研究 PDF（2020 新型智能感应水龙头 / 2022 双模智能控制水龙头）→ 结构化 MD |
| `PyMuPDF`（`fitz`，Python） | 渲染 PDF 页面为图片后人工识别 | 画册第 42 页工程案例名录入库（图片型 PDF） |
| `markdown-broken-link-fixer` | PDF→MD 迁移后的链接对齐 | 白皮书/说明书 PDF 转 MD 后修复指向旧 PDF 的链接 |
| 图册 PDF（资产） | `assets/catalogs/` 下 7 份图册 PDF | 仅作目录链接引用，非断链；不在自动清理范围 |

> 注：未安装独立 `pdf` Skill。若团队需要"PDF 生成/编辑/合并"能力，可后续按需 `find-skills` 安装并固化进项目级 skills。

---

## 五、相关 API / 连接器 / 外部依赖

| 类别 | 名称 | 说明 / 项目中的使用 |
|---|---|---|
| **代码托管** | GitHub API | 仓库 size 查询（`gh api` 或 REST）；`gh` CLI 当前沙箱不可用，启用开关需手动授权 |
| **协作连接器（已连）** | 企业微信 `wecom` | wecom-cli 仅 create_doc / edit_doc_content / 表格查询（smartsheet_*/sheet_*）；**无 get_doc_content** → 读普通 doc 正文只能粘贴文本 / 导出 Word·PDF / 升级 CLI |
| | 腾讯文档 `tencent-docs` | 连接器已连；企微文档登录墙限制读取 |
| | 智能体邮箱 `agent-mail` | 已连 |
| **内容分发 API** | 微信服务号 API | AppID / AppSecret（IP 白名单机 119.13.89.143 经 draft/add + freepublish） |
| | 小红书 / 知乎 / 公众号 | 浏览器自动化或官方 API（各发布技能封装） |
| | Buffer GraphQL API | Personal Key（LinkedIn / Facebook 图文） |
| | QQ 邮箱 SMTP | 环境变量 `QQ_EMAIL_ACCOUNT` / `QQ_EMAIL_AUTH_CODE` |
| **视频生成** | Vidu API | 产品视频（Token 鉴权，图生/参考生视频） |
| **GEO 检索** | WebFetch / WebSearch | geo-diag-report 与日常检索增强 |
| **结构化数据** | schema.org JSON-LD | org / brand / product / faq / breadcrumb（每页注入，强化 AI 实体识别） |

---

## 六、软件 / 运行时 / 工具链

| 层 | 工具 |
|---|---|
| **AI 协作** | WorkBuddy 主会话（⚠️ 禁用「安拓-分发策略师」「海外 B2B 营销自动化架构师」两专家；不带入小维/Wiki 人设）；结构化输出、确认后直接执行 |
| **版本与站点** | Git + GitHub（`gibo-official/gibo-knowledge-base`）；GitHub Pages + Jekyll（`_config.yml` / `_layouts/default.html` / `jekyll-seo-tag` / `jekyll-sitemap`） |
| **运行时（managed，隔离）** | Python 3.14 / 3.13（venv：`~/.workbuddy/binaries/python/envs/default`）；Node 22（workspace：`~/.workbuddy/binaries/node/workspace`） |
| **图片处理** | ImageMagick / PIL（image-optimizer 底层） |
| **文件同步** | 企业微信微盘 WeDrive（`E:/WXWork/.../洁博利智能厨卫/`）；多机经 GitHub 同步 |
| **外部依赖** | Vidu（视频）、Buffer（社媒）、各平台 API；WebFetch（检索/抓取） |

---

## 七、关键文件导航

- `MEMORY.md` —— 本册来源的精炼长期记忆
- `MAINTENANCE.md` —— 运维规则
- `llms.txt` / `LLMS.md` —— AI 索引（中英文双语，列全部内容入口）
- `sitemap.xml` —— Jekyll 自动生成
- `schema/*.jsonld` —— 结构化数据
- `NAV.md` —— 业务单元文档导航（场景 / 产品系列 GEO 拆分）
- `geo-factor-library.md` —— GEO 因子库（认证/技术/EEAT 等因子与映射）
- `.workbuddy/memory/YYYY-MM-DD.md` —— 每日工作日志（本册第一章来源）

---

## 八、新人接手 Checklist

1. `git clone` 仓库到本地（活副本参考 `D:/Github/gibo-knowledge-base`）。
2. 安装"核心·本项目资产"九项 skills 到**项目级** `.workbuddy/skills/`（或用户级），确保团队一致。
3. 设 `origin` = GitHub（`gibo-official/gibo-knowledge-base`）；遇 `git status` "领先数"用 `git ls-remote origin main` 核实真值。
4. 通读 `MEMORY.md` + `MAINTENANCE.md` + 本册第二章（常驻规则）。
5. 改完内容 → 走 `git-safe-sync` 校验 → 新建 commit（不 amend）→ `git push origin main`。
6. 涉及**新增/删除/改名文件** → 触发"文件事件三提示"，先与团队确认内链/孤岛/英文版再提交。
7. PDF 类需求用 `pdftotext` / `PyMuPDF`；读企微/腾讯文档正文靠用户粘贴或导出 PDF/Word。

---

*本册由主会话整理归档（2026-07-31），覆盖项目全周期资产，供团队共享。*
