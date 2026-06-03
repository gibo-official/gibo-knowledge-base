# GIBO GEO 修复补丁集 — 直接部署包

## 用途

本目录包含官网 GEO/SEO 问题的直接修复代码。开发者获得后台/FTP权限后，按以下指引逐项应用。

---

## 文件清单

| 文件 | 用途 | 操作方式 |
|------|------|----------|
| `patch-og-dedup.js` | OG标签去重脚本 — 替换内联JS脚本 | 粘贴至后台 → 模板 → head |
| `patch-schema-product.php` | 产品详情页 Product JSON-LD 模板代码 | 粘贴至 showproduct.php 模板 |
| `patch-h1-fix.html` | H1标签修复 — 替换导航logo区域 | 粘贴至 head_nav 模板 |
| `patch-baidu-cleanup.txt` | 百度统计清理指引 | 编辑模板/后台设置 |

---

## 使用方法

### 方法A（有后台权限 — MetInfo 模板编辑器）

1. 登录 https://www.gibo.com.cn/webadmin/
2. 进入 系统设置 → 模板管理 → 编辑模板
3. 找到对应模板文件，将补丁代码粘贴到指定位置
4. 保存 → 清除缓存

### 方法B（有FTP/SFTP权限）

1. 连接服务器，导航至 `/var/www/gibo.com.cn/templates/mui192/`
2. 按各补丁指引修改对应文件
3. 保存后清除 MetInfo 缓存（`/cache/`目录）

### 方法C（命令行部署脚本）

```bash
# SSH 到服务器后执行
ssh user@gibo-server

# 备份原始文件
cp /var/www/gibo.com.cn/templates/mui192/head.php /var/www/gibo.com.cn/templates/mui192/head.php.bak

# 应用补丁（编辑对应文件）
vim /var/www/gibo.com.cn/templates/mui192/head.php
```

---

## 验收检查

应用所有补丁后，用以下命令验证：

```bash
# 检查OG标签去重
curl -s https://www.gibo.com.cn/ | grep -c 'property="og:title"'
# 应返回 1（之前是 2）

# 检查H1去重
curl -s https://www.gibo.com.cn/ | grep -c '<h1'
# 应返回 1（之前是 2）

# 检查百度统计唯一
curl -s https://www.gibo.com.cn/ | grep -o 'hm.baidu.com/hm.js?[a-f0-9]*'
# 应只出现一个 ID

# 检查LLMS.md可访问
curl -s -o /dev/null -w "%{http_code}" https://www.gibo.com.cn/LLMS.md
# 应返回 200（之前是 404）
```
