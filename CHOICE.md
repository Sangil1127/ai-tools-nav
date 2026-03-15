# 给我GitHub权限，或一键复制方案

## 方案A：给我GitHub Token（我帮你推送）

### 步骤1：创建Personal Access Token

1. 访问：https://github.com/settings/tokens
2. 点击 **"Generate new token"** → **"Classic"**
3. 填写Note：`AI工具导航部署`
4. 勾选权限：**repo**（完整仓库权限）
5. 点击 **"Generate token"**
6. **复制生成的token**（只显示一次！）

Token看起来像这样：
```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 步骤2：发给我

把token发给我，我立即推送所有文件！

---

## 方案B：一键复制粘贴（最安全，推荐）

### 创建sitemap.xml

1. 访问：https://github.com/Sangil1127/ai-tools-nav/new/main/sitemap.xml
2. 粘贴以下内容：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://Sangil1127.github.io/ai-tools-nav/</loc>
    <lastmod>2026-03-14</lastmod>
    <priority>1.0</priority>
    <changefreq>daily</changefreq>
  </url>
</urlset>
```

3. 点击 **"Commit new file"**

### 创建robots.txt（顺便一起做了）

1. 访问：https://github.com/Sangil1127/ai-tools-nav/new/main/robots.txt
2. 粘贴以下内容：

```
User-agent: *
Allow: /

Sitemap: https://Sangil1127.github.io/ai-tools-nav/sitemap.xml
```

3. 点击 **"Commit new file"**

### 等待2-3分钟

然后在Google Search Console重新提交sitemap！

---

## 🎯 推荐方案B

**理由：**
- ✅ 不需要给我token（更安全）
- ✅ 1分钟完成
- ✅ 你可以控制所有文件

**操作时间：** 1分钟

---

## ❓ 你选哪个？

**回复：**
- **"给token"** → 我教你创建token发给我
- **"自己做"** → 按方案B操作
