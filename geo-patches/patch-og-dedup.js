/**
 * patch-og-dedup.js — OG标签去重补丁
 *
 * 替换官网head中的动态OG标签内联脚本。
 * 核心改进：在创建新OG标签前，先移除所有已存在的同名标签，彻底杜绝重复。
 *
 * 用法：在MetInfo后台 → 模板管理 → 编辑 head 模板，
 * 找到内联的OG标签脚本，替换为以下代码。
 */

(function() {
    var currentUrl = window.location.href.split('#')[0];

    // ===== 第一步：删除所有已有OG标签（核心修复）=====
    var ogProperties = [
        'og:title', 'og:description', 'og:image', 'og:url',
        'og:type', 'og:site_name', 'og:locale'
    ];
    ogProperties.forEach(function(prop) {
        document.querySelectorAll('meta[property="' + prop + '"]').forEach(function(el) {
            el.remove();
        });
    });

    // 同时删除所有 Twitter Card 标签（避免重复）
    var twitterNames = [
        'twitter:card', 'twitter:title', 'twitter:description',
        'twitter:image', 'twitter:site', 'twitter:creator'
    ];
    twitterNames.forEach(function(name) {
        document.querySelectorAll('meta[name="' + name + '"]').forEach(function(el) {
            el.remove();
        });
    });

    // ===== 第二步：获取页面原始标题和描述 =====
    var pageTitle = document.querySelector('title') ? document.querySelector('title').innerText : 'GIBO洁博利智能卫浴';

    // 智能截取 og:title（限制 25-35 字符）
    function getShortTitle(fullTitle) {
        var shortTitle = fullTitle.replace(/ - .*$/, '').replace(/ [|｜].*$/, '');
        if (shortTitle.length > 35) {
            shortTitle = shortTitle.substring(0, 32) + '...';
        }
        return shortTitle;
    }

    // 获取页面描述
    var pageDesc = '';
    var customDesc = document.querySelector('meta[name="description"]');

    if (customDesc && customDesc.getAttribute('content')) {
        var fullDesc = customDesc.getAttribute('content');
        if (fullDesc.length > 65) {
            pageDesc = fullDesc.substring(0, 62) + '...';
        } else if (fullDesc.length >= 30 && fullDesc.length <= 65) {
            pageDesc = fullDesc;
        } else {
            pageDesc = '洁博利20年专注感应水龙头、冲水器，产销300万+套，服务全球40+国。ODM/OEM定制。';
        }
    } else {
        pageDesc = '洁博利20年专注感应水龙头、冲水器，产销300万+套，服务全球40+国。ODM/OEM定制。';
    }

    // 获取页面主图
    var pageImage = '';
    var ogImage = document.querySelector('meta[property="og:image"]');
    if (ogImage) {
        pageImage = ogImage.getAttribute('content');
    }
    if (!pageImage) {
        pageImage = 'https://www.gibo.com.cn/upload/202604/1775732015805499.png';
    }

    // ===== 第三步：统一创建 OG 标签 =====
    var head = document.head || document.getElementsByTagName('head')[0];

    function createMeta(property, content) {
        var meta = document.createElement('meta');
        if (property.startsWith('og:')) {
            meta.setAttribute('property', property);
        } else {
            meta.setAttribute('name', property);
        }
        meta.setAttribute('content', content);
        head.appendChild(meta);
    }

    // OGP 基础标签
    createMeta('og:site_name', 'GIBO洁博利智能卫浴');

    createMeta('og:type', 'website');

    createMeta('og:locale', 'zh_CN');

    createMeta('og:url', currentUrl.replace(/index\.php\?lang=\w+$/, '').replace(/\/index\.php$/, '/').replace(/\/+$/, '') || window.location.origin);

    createMeta('og:title', getShortTitle(pageTitle));

    createMeta('og:description', pageDesc);

    createMeta('og:image', pageImage);

    // Twitter Card
    createMeta('twitter:card', 'summary_large_image');
    createMeta('twitter:image', pageImage);
    createMeta('twitter:site', '@gibo');
    createMeta('twitter:creator', '@gibo_official');
    createMeta('twitter:title', getShortTitle(pageTitle));
    createMeta('twitter:description', pageDesc);
})();
