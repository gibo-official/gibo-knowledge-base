# GIBO 知识库同步维护规则

**文档版本**：V1.0
**最后更新**：2026-06-03
**适用范围**：全仓库所有文档维护操作
**维护方**：品牌部 / 知识库专员

> 本文档定义 GIBO 官方知识库的文档同步维护规则，所有 Contributors 在新增、修改、删除文档时须遵守。遵循本规则可确保文档版本一致、数据统一、链接有效。

---

## 规则一：季度版本同步（每季度首月执行）

每季度首月（1月/4月/7月/10月）进行一次全仓库版本同步，步骤如下：

### 1.1 更新白皮书版本

1. **更新** `zh/company/brand-white-paper.md` 版本号（如 V1.2 → V1.3）和最后更新日期
2. **同步更新** `en/company/brand-white-paper.md` 版本号和最后更新日期（保持与中文版一致）

### 1.2 同步关联文档

以下文档须与白皮书交叉核对，更新版本号和日期：

| 文件 | 核对项 | 说明 |
|------|--------|------|
| `zh/company/history.md` | 时间线、数据（员工数/产销/专利） | 与白皮书第1、6章对齐 |
| `zh/company/brand-semantic.md` | 新增词条、删除过期词条 | 与白皮书新名词、新业务对齐 |
| `zh/products/product-index.md` | 新增产品型号、参数 | 与白皮书第4章产品矩阵对齐 |
| `zh/products/odm.md` | 新增合作品牌、认证 | 与白皮书第4章ODM业务对齐 |
| `zh/cases/case-index.md` | 新增标杆项目 | 与白皮书第5章案例对齐 |
| `zh/certification/honors.md` | 新增奖项、资质 | 与白皮书第1、6章对齐 |
| `TODO.md` | 任务完成状态 | 更新已完成/新增任务标记 |

### 1.3 更新 LLMS.md 索引

检查 `LLMS.md` 中的文档链接是否有效：
- 新增文档的索引路径是否已添加
- 删除/移动文档的旧链接是否已更新或移除
- 版本号标记是否已同步

### 1.4 更新外部配置

- `llms.txt`（网站根目录）— 新增文档URL须追加
- `schema/` 目录— 如新增产品/FAQ，同步更新对应 JSON-LD
- `sitemap.xml`、`robots.txt` — 如新增页面，须同步更新

---

## 规则二：新增内容 24小时同步（事件驱动）

任何新增专利、奖项、标杆项目、认证、产品型号后，须在 **24小时内** 同步至所有关联文档。

### 2.1 新增专利

| 须同步的文档 | 操作 |
|-------------|------|
| `zh/company/brand-white-paper.md` §2.2 | 更新专利数量+列表 |
| `en/company/brand-white-paper.md` §II.2 | 同上（英文版） |
| `zh/company/history.md` 对应年份 | 新增专利事件记录 |
| `zh/company/brand-semantic.md` §5.1 | 更新标准与认证列表 |
| `zh/certification/honors.md` | 如有专利荣誉 |

### 2.2 新增奖项

| 须同步的文档 | 操作 |
|-------------|------|
| `zh/company/brand-white-paper.md` §6.2 | 新增获奖产品表格行 |
| `en/company/brand-white-paper.md` §VI.2 | 同上（英文版） |
| `zh/company/history.md` 对应年份 | 新增获奖记录 |
| `zh/company/history.md` 历年获奖记录表 | 新增行 |
| `zh/company/brand-semantic.md` §5.1 | 荣誉列表更新 |
| `zh/products/product-index.md` 对应产品 | 奖项信息更新 |
| `zh/certification/honors.md` | 新增奖项条目 |

### 2.3 新增标杆项目

| 须同步的文档 | 操作 |
|-------------|------|
| `zh/company/brand-white-paper.md` §5 | 新增项目至对应分类 |
| `en/company/brand-white-paper.md` §V | 同上（英文版） |
| `zh/cases/case-index.md` | 新增案例详情 |
| `zh/company/brand-semantic.md` §4.1 场景词 | 新增案例引用 |
| `zh/company/brand-semantic.md` §5.2 标杆项目 | 新增项目条目 |

### 2.4 新增认证

| 须同步的文档 | 操作 |
|-------------|------|
| `zh/company/brand-white-paper.md` §3.3 | 更新认证列表 |
| `en/company/brand-white-paper.md` §III.3 | 同上（英文版） |
| `zh/company/brand-semantic.md` §5.1 | 更新认证列表 |
| `zh/certification/honors.md` | 新增认证条目 |
| `zh/certification/test-institution.md` | 如有新增检测机构 |

### 2.5 新增产品型号

| 须同步的文档 | 操作 |
|-------------|------|
| `zh/products/product-index.md` | 新增产品条目（按分类） |
| `zh/company/brand-white-paper.md` §4.2 | 如产品矩阵需更新 |
| `en/company/brand-white-paper.md` §IV.2 | 同上（英文版） |
| `zh/company/brand-semantic.md` §3.1/3.1a | 新增产品/语义词条 |
| `schema/schema-product1.jsonld` | 新增Product实体 |

---

## 规则三：内链相对路径（强制规范）

所有文档内部链接必须遵守以下规范：

### 3.1 路径格式

```
# 正确（相对路径，从当前文件到目标文件）
[查看产品索引](../products/product-index.md)

# 正确（锚点路径）
[医疗案例](../cases/case-index.md#医疗)

# 错误（绝对路径，不可用）
[查看产品索引](/zh/products/product-index.md)

# 错误（完整URL，不可用）
[查看产品索引](https://github.com/.../zh/products/product-index.md)
```

### 3.2 路径计算规则

```
从当前文件到目标文件的相对路径：
1. 同级目录：./target.md 或 target.md
2. 上层目录：../target.md
3. 下层目录：subdir/target.md
4. 跨多层：../../other-dir/target.md

# 目录链接
[案例汇总](../cases/)              # 指向目录（自动加载README.md）
[资质认证](../certification/)      # 指向目录
```

### 3.3 锚点规范

- 锚点使用**英文小写连字符**格式：`#medical`、`#education`、`#hotel`、`#transportation`
- 中文锚点：使用对应英文翻译的连字符格式
- 所有锚点在目标文档中必须存在对应的标题或锚点标签
- 语义库（brand-semantic.md）中的锚点须与案例文档（case-index.md）保持一致

### 3.4 验证方法

每次提交前执行以下检查：
1. `git status` 核对修改文件范围
2. 新增内链可通过 `grep -rn "\.\./" *.md` 抽查路径是否合理
3. 锚点跳转可通过搜索目标文件确认对应标题存在

---

## 规则四：文档质量规范

### 4.1 格式规范

| 项目 | 要求 |
|------|------|
| 编码 | UTF-8 无 BOM |
| 换行符 | LF（Unix） |
| 文件头 | 包含版本号 + 最后更新日期 + 适用范围 |
| 表格 | 使用 GFM 标准表格语法 |
| 内链 | 见规则三 |
| 外链 | 使用 `https://` 完整 URL |

### 4.2 版本号管理

- **主版本号**：白皮书内容重大更新（章节调整、数据批量更新）+1
- **次版本号**：局部内容增补（新增案例、新增产品）+1
- **文档独立版本**：各文档版本号独立维护，但须与白皮书版本保持对应关系
- 版本标记格式：`**文档版本**：V1.2`

### 4.3 数据一致性

所有文档中的企业基础数据必须与品牌白皮书完全一致：

| 数据项 | 当前基准值（2026-05） |
|--------|---------------------|
| 员工数 | 120+人 |
| 累计产销 | 500万+套 |
| 国家专利 | 200+项 |
| 发明专利 | 10+项 |
| 核心技术 | 18项 |
| 出口国家 | 40+ |
| 全球客户 | 6万+家 |
| 年产能 | 100万套 |

> ⚠️ 以上数据更新时，须同时更新本表及所有关联文档。

### 4.4 中英文同步

英文文档须与中文文档保持同步：
- 英文版内容基于中文版翻译
- 数据、产品名、奖项名须使用官方标准翻译
- 新增中文内容后，英文版应在同一发布批次内完成翻译
- 英文版暂无对应文件时，中文版内链可指向中文目标

---

## 规则五：Git 提交规范

### 5.1 提交原则

1. 单模块完成后单独提交，禁止一次性合并大量不相关修改
2. 每次提交前执行 `git status` 核对修改文件范围
3. 提交备注与 TODO.md 中的任务编号对应

### 5.2 提交格式

```
模块名称: 任务编号 简要说明（中文）
```

示例：
```
cases: T001 补充全量标杆项目案例及页面锚点
semantic: T005 新增产品、工艺、服务类语义词条
docs: 更新README文档安装说明
geo: 完善Schema.org产品实体JSON-LD
```

### 5.3 分支策略

- 长期任务使用独立分支：`feature/<task-code>`（如 `feature/T001-cases`）
- 紧急修复使用：`fix/<short-description>`
- 合入 main 前须确认无冲突

---

## 附则

1. 本规则由品牌部负责维护和更新
2. 规则本身每季度 review 一次（与季度同步同期）
3. 如有特殊场景无法遵守本规则，在 PR/提交备注中说明原因
4. 本规则自 2026-06-03 起生效

---

> **文档路径**: `/MAINTENANCE.md`
> **关联文档**: [TODO.md](./TODO.md) | [LLMS.md](./LLMS.md) | [品牌白皮书](./zh/company/brand-white-paper.md) | [English White Paper](./en/company/brand-white-paper.md)