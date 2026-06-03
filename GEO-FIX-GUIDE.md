# GIBO官网GEO问题 — 开发修复指南

**日期**：2026-06-03
**CMS**：MetInfo V8.1
**模板**：mui192
**服务器**：openresty + PHP 7.2.34

---

## 使用方式

本文档提供给官网开发者，按优先级逐步修复。每项均标注了**影响范围**、**操作步骤**和**代码示例**。

---

## 🔴 P0：后台凭证验证（阻塞项）

当前董事会提供的凭证 (admin / gibo2837) 无法登录后台。

- 请IT部门验证该管理员账号是否存在或密码已被修改
- 后台地址：https://www.gibo.com.cn/webadmin/
- 如忘记密码，可通过登录页"忘记密码?"功能重置，或通过MySQL修改 `met_admin_table` 表的密码字段

---

## 🔴 P1：产品详情页添加 Product JSON-LD

**影响范围**：所有 showproduct.php 页面（300+产品）
**文件**：`/templates/mui192/product/showproduct.php`

在 `<head>` 中添加：

```php
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "<?php echo $product['name']; ?>",
  "description": "<?php echo strip_tags($product['description']); ?>",
  "sku": "<?php echo $product['model']; ?>",
  "brand": {
    "@type": "Brand",
    "name": "GIBO洁博利"
  },
  "image": "<?php echo $product['image']; ?>",
  "mpn": "<?php echo $product['model']; ?>",
  "category": "<?php echo $product['classname']; ?>",
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "priceSpecification": {
      "@type": "CompoundPriceSpecification",
      "priceType": "https://schema.org/ListPrice"
    }
  },
  "manufacturer": {
    "@type": "Organization",
    "name": "福建洁博利厨卫科技有限公司"
  }
}
</script>
```

---

## 🟡 P2：修复OG标签重复

### 问题分析

首页源码中存在**两套OG标签**：

| 属性 | 套A（静态PHP） | 套B（JS动态） |
|------|---------------|--------------|
| `og:type` | website | website |
| `og:site_name` | GIBO洁博利智能卫浴**官网** | GIBO洁博利智能卫浴 |
| `og:image` | /upload/201908/1566538990.png | /upload/202604/1775732015805499.png |
| `og:title` | 完整长标题+副标题 | 截取短标题（≤35字） |
| `og:description` | 完整长描述 | 截取短描述（≤65字） |

### 推荐修复：JS覆盖法（只需修改JS脚本）

**文件**：首页模板或 `/app/app/met_stat/web/templates/js/met_stat.js`

在JS动态脚本的开头，添加**先删除再创建**的逻辑：

```javascript
(function() {
    var currentUrl = window.location.href.split('#')[0];
    
    // ★ 删除所有已有OG标签，避免重复
    var ogProperties = ['og:title', 'og:description', 'og:image', 'og:url', 'og:type', 'og:site_name'];
    ogProperties.forEach(function(prop) {
        document.querySelectorAll('meta[property="' + prop + '"]').forEach(function(el) {
            el.remove();
        });
    });
    
    // 然后继续原有的创建逻辑...
```

### 备选修复：删除静态OG标签（需修改模板文件）

**文件**：`/templates/mui192/head.php` 或主要模板的 `<head>` 部分

删除以下6行：
```html
<meta property="og:site_name" content="GIBO洁博利智能卫浴官网" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://www.gibo.com.cn/index.php?lang=cn" />
<meta property="og:title" content="GIBO洁博利智能卫浴官网 - 感应水龙头,ODM专家,感应冲水器,感应洁具,智能卫浴" />
<meta property="og:description" content="洁博利创立于2005年..." />
<meta property="og:image" content="https://www.gibo.com.cn/upload/201908/1566538990.png" />
```

---

## 🟡 P3：修复H1标签数量

**影响范围**：全站所有页面
**文件**：`/templates/mui192/head.php` 或导航模板

### 当前问题

导航logo区域有两个 `<h1 hidden>`（PC端和移动端各一个），产品列表页还会多一个 `<h1>` 页面标题。

### 修复

将每个导航logo的：
```html
<h1 hidden>GIBO洁博利智能卫浴官网</h1>
```
改为：
```html
<span class="sr-only">GIBO洁博利智能卫浴官网</span>
```

或者使用 `aria-label`：
```html
<a href="" class="met-logo" title="GIBO洁博利智能卫浴官网" aria-label="GIBO洁博利智能卫浴官网">
    <div class="vertical-align-middle">
        <img src="upload/201908/1566543194.png" alt="GIBO洁博利智能卫浴官网"/>
    </div>
</a>
```

---

## 🟡 P4：统一百度统计ID

### 当前状态

首页存在两个不同ID的百度统计脚本：

**脚本1**（ID: `0bd5d0d4b41cc9d3aa928f5e0ed9e188`）：
```html
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?0bd5d0d4b41cc9d3aa928f5e0ed9e188";
  ...
})();
</script>
```

**脚本2**（ID: `b7c031fc8cc72263a621189a8721e1e5`）：
```html
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?b7c031fc8cc72263a621189a8721e1e5";
  ...
})();
</script>
```

### 修复步骤

1. 登录百度统计后台，确认哪个ID仍在正常收集数据
2. 保留该ID，删除另一个脚本块
3. 检查 `met_stat.js` 脚本（动态OG脚本所在的文件），确保其中也动态添加的百度统计脚本已被移除或统一ID

---

## 🟡 P5：met_stat.js 去重

**影响范围**：首页
**文件**：`/templates/mui192/foot.php` 或 `/templates/mui192/head.php`

首页底部加载了两次：
```html
<script src="https://www.gibo.com.cn/app/app/met_stat/web/templates/js/met_stat.js"></script>
```

找到两个引用位置，删除其中一个。

---

## 🟡 P6：规范 og:url

### 当前
```html
<meta property="og:url" content="https://www.gibo.com.cn/index.php?lang=cn" />
```

### 修复后
应该是在JS动态脚本中自动设置为 `window.location.href` 的规范版本。

在JS动态脚本中添加URL规范化逻辑：
```javascript
function getCanonicalUrl() {
    var url = window.location.href.split('#')[0];
    url = url.replace(/index\.php\?lang=\w+$/, '');
    url = url.replace(/\/index\.php$/, '/');
    url = url.replace(/\/+$/, '') || window.location.origin;
    return url;
}
```

---

## 🟡 P7：部署 LLMS.md 和 geo/ 目录

### 操作

从知识库仓库复制到官网服务器根目录：
```
cp <knowledge-base>/LLMS.md /var/www/gibo.com.cn/LLMS.md
cp -r <knowledge-base>/geo/ /var/www/gibo.com.cn/geo/
```

需确保目录权限为 755（www-data用户可读）。

---

## 🟢 P8：升级 PHP 版本

当前 PHP 7.2.34 已于2022年停止安全支持，建议升级至 PHP 8.0+。

由于 MetInfo V8.1 最高支持 PHP 7.4，需确认 MetInfo 官方是否提供 V8.1 的 PHP 8.0 补丁，或联系 MetInfo 技术支持。

---

## 附录A：验收检查清单

修复完成后，使用以下方式验证：

| 检查项 | 验证方式 |
|--------|----------|
| OG标签去重 | 浏览器打开首页，`document.querySelectorAll('meta[property^="og:"]')` 应无重复 |
| H1唯一 | `document.querySelectorAll('h1').length === 1` |
| 百度统计唯一 | `document.querySelectorAll('[src*="hm.baidu.com"]').length === 1` |
| met_stat.js唯一 | `document.querySelectorAll('[src*="met_stat.js"]').length === 1` |
| Product Schema | Google Rich Results Test 验证 showproduct.php 页面 |
| og:url规范 | 检查首页 OG 标签中的 URL 是否无 index.php |
| LLMS.md可访问 | curl https://www.gibo.com.cn/LLMS.md → 200 OK |

## 附录B：后台管理员密码重置

如遗忘MetInfo管理员密码，可以通过MySQL直接重置：

```sql
-- 登录MySQL
mysql -u root -p

-- 选择MetInfo数据库
USE metinfo;

-- 查看管理员表
SELECT * FROM met_admin_table;

-- 重置密码（MetInfo使用MD5(密码+随机码)加密，需要同步修改）
UPDATE met_admin_table SET admin_pass = MD5(CONCAT('新密码', admin_random)) WHERE admin_id = 'admin';
```

或使用MetInfo官方提供的密码找回功能：后台登录页 → 忘记密码。
