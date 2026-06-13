# GIBO 知识库资产文件命名规范

**文档版本**：V1.0
**最后更新**：2026-06-13
**适用范围**：全仓库 assets/ 目录下的所有静态资源文件

---

## 一、通用规则

1. **字符集**：仅允许小写字母、数字、连字符（-）、下划线（_）、点号（.）
2. **中文文件名**：全部转为拼音或英文，禁止中文文件名
3. **空格处理**：空格替换为连字符
4. **序号规则**：同类型仅1张时不加序号；2张及以上从01开始
5. **扩展名**：统一小写（.jpg / .png / .pdf / .mp4）

---

## 二、产品相关资产（核心规范）

**格式**：`{型号}_{名称cn}_{类型}_{序号}.{ext}`

**型号**：产品官方型号，如 6110、6170d、9165d、g61901
**名称cn**：产品中文名拼音连字符格式，如 gan-ying-shui-long-tou（感应水龙头）
**类型词表**：

| 类型词 | 含义 | 示例 |
|--------|------|------|
| main | 主图/正面图 | 6110_gan-ying-shui-long-tou_main.jpg |
| side | 侧面图 | 6110_gan-ying-shui-long-tou_side_01.jpg |
| detail | 细节图 | 6110_gan-ying-shui-long-tou_detail_01.jpg |
| scene | 场景图/安装效果图 | 6110_gan-ying-shui-long-tou_scene.jpg |
| install | 安装示意图 | 6110_gan-ying-shui-long-tou_install.jpg |
| spec | 规格参数图 | 6110_gan-ying-shui-long-tou_spec.jpg |
| manual | 说明书 | 6110_gan-ying-shui-long-tou_manual.pdf |
| datasheet | 规格书 | 6110_gan-ying-shui-long-tou_datasheet.pdf |
| award | 获奖证书 | 6170d_gan-ying-shui-long-tou_award.jpg |
| cert | 认证证书 | 6110_gan-ying-shui-long-tou_cert_ce.jpg |
| video-cn | 中文视频 | 6110_gan-ying-shui-long-tou_video-cn.mp4 |
| video-en | 英文视频 | 6110_gan-ying-shui-long-tou_video-en.mp4 |
| video-install-cn | 中文安装教程 | 6110_gan-ying-shui-long-tou_video-install-cn.mp4 |
| video-install-en | 英文安装教程 | 6110_gan-ying-shui-long-tou_video-install-en.mp4 |

---

## 三、非产品资产（扩展规范）

### 3.1 品牌资产 brand/

**格式**：`brand_{类型}_{描述}_{序号}.{ext}`

| 类型词 | 含义 | 示例 |
|--------|------|------|
| logo | 公司Logo | brand_logo-color-horizontal.png |
| logo-bw | 黑白Logo | brand_logo-bw-horizontal.png |
| logo-icon | Logo图标（方形） | brand_logo-icon.png |
| mark | 品牌印记 | brand_mark.png |
| badge | 认证标识 | brand_badge-ce.png |
| banner | 横幅图片 | brand_banner-official_01.jpg |
| poster | 海报 | brand_poster-4d-launch.jpg |
| trademark | 注册商标 | brand_trademark-2016.png |

### 3.2 公司资产 company/

**格式**：`company_{区域}_{描述}_{序号}.{ext}`

| 区域词 | 含义 | 示例 |
|--------|------|------|
| hq | 总部外观 | company_hq-exterior.jpg |
| office | 办公区 | company_office-open_01.jpg |
| workshop | 生产车间 | company_workshop-smt_01.jpg |
| lab | 实验室 | company_lab-test_01.jpg |
| showroom | 展厅 | company_showroom_01.jpg |
| team | 团队照片 | company_team-2023.jpg |
| history | 历史照片 | company_history-2013-shop-opening.jpg |

### 3.3 证书资产 certificates/

**格式**：`cert_{认证类型}_{型号或年份}_{序号}.{ext}`

| 认证类型词 | 含义 | 示例 |
|------------|------|------|
| iso | ISO认证 | cert_iso-9001-2024.pdf |
| water-save | 节水认证 | cert_water-save-6195-2026.pdf |
| ce | CE认证 | cert_ce-6102ad.pdf |
| cupc | cUPC认证 | cert_cupc-2015.pdf |
| nsf | NSF认证 | cert_nsf-2015.pdf |
| invention | 发明专利 | cert_invention_01.png |
| utility | 实用新型专利 | cert_utility_01.jpg |
| design-patent | 外观设计专利 | cert_design-patent_01.png |
| software | 软件著作权 | cert_software_01.png |
| award | 行业奖项 | cert_award-feiteng-6170d-2020.jpeg |
| high-tech | 高新技术企业 | cert_high-tech-2023.jpg |
| standard | 标准参编 | cert_standard-t-xmbk002-2024.png |

### 3.4 展会资产 exhibitions/

**格式**：`exh_{年份}_{展会描述}_{序号}.{ext}`

示例：`exh_2013-shanghai-expo_01.jpg`

### 3.5 设备资产 equipment/

**格式**：`equip_{车间/区域}_{设备描述}_{序号}.{ext}`

示例：`equip_smt-mounting-machine_01.jpg`

### 3.6 画册资产 catalogs/

**格式**：`catalog_{年份}_{语言}_{类型}.{ext}`

示例：`catalog_2025-cn-full.pdf`、`catalog_2023-en-product.pdf`

### 3.7 白皮书资产 whitepapers/

**格式**：`whitepaper_{主题}_{版本}.{ext}`

示例：`whitepaper-dtof-v1.pdf`、`whitepaper-odm-outline.md`

---

## 四、双语文件命名

中文文件使用中文名称拼音（或英文释义），英文文件加 `-en` 后缀：

- 中文说明书：`6110_gan-ying-shui-long-tou_manual.pdf`
- 英文说明书：`6110_gan-ying-shui-long-tou_manual-en.pdf`
- 中文安装视频：`6110_gan-ying-shui-long-tou_video-install-cn.mp4`
- 英文安装视频：`6110_gan-ying-shui-long-tou_video-install-en.mp4`

---

> **文档路径**：`/NAMING-CONVENTION.md`
> **关联文档**：[MAINTENANCE.md](./MAINTENANCE.md) | [CONTENT_STATUS.md](./CONTENT_STATUS.md)
