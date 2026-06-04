---
title: 官网后台访问与问题诊断报告
version: V1.0
last_updated: 2026-06-04
scope: 官网故障诊断、GEO技术问题清单、IT修复指引
related:
  - ../../geo-patches/README.md
  - ../../schema/README.md
---

# 官网后台访问与问题诊断报告

> **访问时间**: 2026-06-04
> **访问方式**: Cookie会话注入 (`met_auth` + `admin_lang=cn` + `PHPSESSID`)
> **CMS**: MetInfo V8.1
> **服务器**: openresty + PHP 7.2.34
> **模板**: mui192

---

## 一、✅ 后台访问确认

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 后台地址 | ✅ 可访问 | https://www.gibo.com.cn/webadmin/ |
| 登录状态 | ✅ 已登录 | Cookie认证通过，显示"GIBO官网管理系统" |
| 可视化编辑模块 | ✅ 可用 | `n=ui_set` 模块可正常加载（15KB） |
| 页面配置API | ✅ 可用 | `doset_page_config` API返回"操作成功" |

## 二、🔴 中文首页0字节问题确认

| 页面 | HTTP状态 | 大小 | 说明 |
|------|----------|------|------|
| `index.php?lang=cn`（中文首页） | 200 | **0字节** ❌ | 页面空白，配置损坏 |
| `index.php?lang=en`（英文首页） | 200 | 108KB ✅ | 正常显示 |
| `product/list.php?lang=cn` | 404 | 277字节 | 页面不存在 |
| `about/` | 200 | 0字节 ❌ | 同样配置损坏 |
| `news/` | 200 | 0字节 ❌ | 同样配置损坏 |
| `search/` | 200 | 0字节 ❌ | 同样配置损坏 |

**根因判断**: `met_config` 表中 `lang=cn` 的首页配置数据损坏，导致PHP解析时发生致命错误（因 `display_errors=Off` 返回白页）。

## 三、可用后台模块

| 模块 | 路径 | 状态 |
|------|------|------|
| 可视化编辑 | `n=ui_set` | ✅ 可用 |
| 后台首页 | `n=admin&c=index&a=doInfo` | ❌ 返回0字节 |
| SEO设置 | `n=seo` | ❌ 模块不存在 |
| 栏目管理 | `n=column` | ❌ 模块不存在 |
| 标签管理 | `n=label` | ❌ 模块不存在 |
| 数据库工具 | `n=databack` | ❌ 模块不存在 |

## 四、🔧 修复方案（需要IT部门执行）

### 4.1 方案A：通过phpMyAdmin修复（推荐）

1. 登录服务器 phpMyAdmin 或 MySQL 客户端
2. 选择 MetInfo 数据库（通常为 `metinfo`）
3. 检查 `met_config` 表中 `lang=cn` 的记录：
   ```sql
   SELECT * FROM met_config WHERE lang='cn' AND name='met_skin_user' AND columnid=0;
   ```
4. 如果该记录损坏或缺失，从 `lang=en` 的记录复制：
   ```sql
   -- 先备份
   CREATE TABLE met_config_bak AS SELECT * FROM met_config;
   
   -- 检查英文版的配置是否完整
   SELECT COUNT(*) FROM met_config WHERE lang='en' AND columnid=0;
   ```
5. 或将管理员密码重置为已知密码：
   ```sql
   UPDATE met_admin_table SET admin_pass = MD5(CONCAT('gibo2026', admin_random)) WHERE admin_id = 'admin';
   ```
   重置后密码为：`gibo2026`

### 4.2 方案B：通过服务器文件修复

1. SSH登录服务器
2. 检查PHP错误日志：
   ```bash
   tail -100 /var/log/php_errors.log
   ```
3. 在PHP入口文件 `index.php` 中临时开启错误显示调试：
   ```php
   error_reporting(E_ALL);
   ini_set('display_errors', 1);
   ```
   访问中文首页查看具体错误信息

### 4.3 方案C：使用后台忘记密码功能

1. 访问 https://www.gibo.com.cn/webadmin/
2. 点击"忘记密码"
3. 通过管理员邮箱重置密码

---

## 五、已确认的GEO技术问题清单

| 优先级 | 问题 | 状态 |
|--------|------|------|
| 🔴 P0 | 中文首页0字节（严重阻塞） | 需IT修复 |
| 🔴 P1 | 产品详情页缺失Product JSON-LD | 需在模板中添加 |
| 🟡 P2 | OG标签重复（静态+JS两套） | 需修改模板 |
| 🟡 P3 | H1标签超标（首页2个，产品页3个） | 需修改模板 |
| 🟡 P4 | 百度统计双ID | 需统一 |
| 🟡 P5 | met_stat.js重复加载 | 需去重 |
| 🟡 P6 | og:url指向index.php非规范URL | 需修复 |
| 🟡 P7 | LLMS.md和geo/目录未部署 | 需FTP复制 |

---

**文档路径**: `/zh/company/website-fix-report.md`
**版本**: V1.0 | **日期**: 2026-06-04
