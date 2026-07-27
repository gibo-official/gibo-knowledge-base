---
lang: zh-CN
category: 仓库文档
title: "assets_体积优化方案"
summary: "最后更新：2026-07-14"
updated: 2026-07-14
product: ""
tags: ["GIBO", "洁博利", "仓库文档", "AI知识库"]
---

# assets 体积分析与 Gitee 同步优化方案
**文档版本**：V1.0 **最后更新**
：2026-07-14
**适用范围**
：品牌展示、产品展示、投标材料、行业研究、AI知识库引用



> 生成时间：2026-07

-09仓库：`D:\Github\gibo

- knowledge

- base`

> 目标：将 assets 从 2. 41GB 瘦身到适合 Gitee 免费单仓（≤1GB）的规模



---



#

## 一、当前体积全景



范围大小说明


---

| - |

---

| - |

---

| - |

整个仓库（含.git）
**27 GB**
*.git占23GB，是历史包袱

`.git`（历史对象）23GB多为已删除的`assets/standards/`巨型PDF（如269MB的std_GBT7001）

`.Temp`（备份）1.7GB

**已被 . gitignore 忽略，不会推送**

| * |


**assets（当前树）**

| * |
**2. 41 GB**
*真正要同步的对象



#

#

## assets 一级目录（按大小）



目录大小占比


---

| - |

---

| - |

---

| - |

products1.40GB58%

certificates638MB26%

Cases89MB4%

manuals76MB3%

videos55MB2%

company46MB2%

catalogs35MB1.5%

keyframes31MB1.3%

Icon14MB0.6%

品牌物料9MB0.4%

standard6.8MB0.3%

Exhibition5MB0.2%
### 按文件类型
类型数量大小备注


---

| - |

---

| - |

---

| - |

---

| - |

.jpg22901480MB已压缩，但大量超尺寸

.png3521707MB无损格式，多数可转JPG/WebP

.mp4254MBvideo2.mp4单文件52.6MB，超Gitee单文件限制

.pdf733MB多数为标准/目录文档

其他—<15MBmd/xls/svg等，可忽略



#

#

## 最关键的发现：超大文件
- *210 个文件
> 3MB，合计 1341. 5 MB，占 assets 的 56%
*。
- 典型案例：`6197_主图_01. jpg` 36MB、`6170_产品图_20. jpg` 21MB、`6196` 系列一堆 13MB jpg。

- 这些是产品图被存成了印刷级分辨率，对网页/知识库（AI 生成文案、详情图设计）完全没必要。



#

#

## PNG 分布（决定能转多少）



目录PNG大小数量


---

| - |

---

| - |

---

| - |

products434MB371

certificates133MB100

manuals62MB2838（平均仅22KB，无需动）

Cases35MB11

keyframes30MB33

Icon10MB136



> 真正可转的是

*

products(434)

+ certificates(133) = 567MB

*

的非透明 PNG。manuals 的 2838 个小 PNG 不用管。



---



#

## 二、Gitee 限制（免费版）
- **单仓库总容量**
：约 1GB（超出后禁止 push）。
- **单文件**：
> 100MB 无法推送；

> 50MB 会告警，建议走 LFS。
-
**LFS 免费额度**
：1GB 存储
+ 1GB/月下载（不够放全部 2. 4GB）。
- **结论**
：2. 41GB 当前树

**无法直接进单仓**
。必须先瘦身
+ 处理历史。



---



#

## 三、分阶优化方案（预计省 ~1. 45GB）



#

#

## Tier 1 — 压缩超大图片（最大、最安全收益，省 ~1. 1GB）

- 对
*210 个
> 3MB 文件

*

重采样到网页尺寸（长边 ~1920px，JPG 质量 82）。

- 保守估计：1341MB → ~210MB，

**省约 1. 13GB**
。
- 36MB 的 jpg 通常可压到 1–2MB。



#

#

## Tier 2 — 非透明 PNG → JPG/WebP（省 ~0. 3GB）

- 对 products

+ certificates 共 567MB PNG 做透明通道检测：



- 无透明 → 转 JPG（约 30–50% 体积）或 WebP（25–35%）。



- 有透明（logo/抠图）→ 保留 PNG。

- 预计

**省约 0. 25–0. 35GB**
。
## Tier 3 — 清理死亡重量（省 ~0. 06GB）

- 删除 `assets/certificates/. Temp/optimize_original/`（17. 5MB 历史备份，不该进仓库）。

- `video2. mp4` 52. 6MB 重新编码（h264 → ~10MB）或移入 LFS。



#

#

## Tier 4 — 历史与推送策略（避免 23GB 进 Gitee）
-
**以全新仓库方式推 Gitee**

：只推优化后的当前树，不 mirror 23GB 历史。`. git` 的 23GB 不会传输。

- 配置 `. gitattributes` 用
**Git LFS**兜底剩余
> 50MB 文件（video / 大 PDF）。
### 预计结果
阶段累计大小


---

| - |

---

| - |

现状2410MB

−Tier1图片压缩~1280MB

−Tier2PNG转换~950MB

−Tier3清理~880MB

若再压缩1–3MB图

+多转PNG

**可压到 ~700MB（稳进 1GB）**

| * |



---



#

## 四、两种落地架构（请二选一）



#

#

## 方案 A：瘦身后全量进 Gitee 单仓（推荐若坚持一个仓库）

- 执行 Tier1–4，压到 ~700MB–1GB。

- 推为全新仓库（无历史），大文件走 LFS。

- 优点：一个仓库管全部。缺点：仍逼近 1GB 上限，clone 偏重。



#

#

## 方案 B：知识库与素材分离（AI 知识库场景最推荐）
-
**Gitee 主仓**

：只放 markdown 知识（营销素材库、core

- products、证书清单等，几十 MB）

+ 优化后的
**缩略图**。 - **重型原图/视频**
：放 Gitee LFS 独立仓库，或对象存储/网盘；知识库中用链接引用。

- 优点：主仓轻量、clone 快、同步稳；AI 生成真正依赖的是结构化文案，高清原图仅辅助。

- 缺点：需要两处管理。



---



#

## 五、不可逆性提示

- Tier1/Tier2 的压缩/转格式是
**有损且不可逆**
的（原分辨率/质量丢失）。

- 执行前会先把
**全部原图备份**
到 `. Temp/assets_origin_backup_20260709/`，可随时还原。



>
**数据来源说明**
：本文技术参数与说明来源于洁博利官网（www. gibo. com. cn）、EEAT信源库、产品规格表及专利文件，仅作为洁博利产品宣传与展示使用。｜洁博利GIBO｜感应水龙头ODM专家｜官网：https://www. gibo. com. cn