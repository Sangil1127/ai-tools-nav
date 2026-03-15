# Google验证代码部署方案

## 🔍 问题确认

本地代码已包含Google验证代码，但GitHub上的是旧版本。

**需要在GitHub上更新 index.html 文件。**

---

## 方案A：直接在GitHub编辑（最简单）

### 步骤1：打开文件编辑

1. 访问：
   ```
   https://github.com/Sangil1127/ai-tools-nav/blob/main/index.html
   ```

2. 点击右上角的 **编辑按钮**（铅笔图标 ✏️）

### 步骤2：添加验证代码

找到 `<head>` 部分，在现有meta标签后面添加：

```html
<meta name="google-site-verification" content="KCqH9ZOpREsN1j23WZ47SZA5VHarPskyyvKVoNk9tIo" />
```

**完整位置：**
```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- 在这里添加 ↓ -->
  <meta name="google-site-verification" content="KCqH9ZOpREsN1j23WZ47SZA5VHarPskyyvKVoNk9tIo" />
  
  <title>AI工具导航大全...</title>
  ...
</head>
```

### 步骤3：保存

1. 滚动到页面底部
2. 填写提交信息：`添加Google验证代码`
3. 点击 **"Commit changes"**

### 步骤4：等待部署

等待2-3分钟，然后：
1. 刷新网站：`https://Sangil1127.github.io/ai-tools-nav/`
2. 回到Google Search Console点击验证

---

## 方案B：重新上传文件

如果你找不到编辑按钮，直接重新上传：

### 步骤1：删除旧文件

1. 访问：https://github.com/Sangil1127/ai-tools-nav
2. 点击 `index.html`
3. 点击右上角的 **...** 菜单
4. 选择 **"Delete file"**
5. 确认删除

### 步骤2：上传新文件

1. 点击 **"Add file"** → **"Upload files"**
2. 把下面的完整代码复制保存为 `index.html`，然后上传

（或者我发给你完整的index.html文件内容，你复制上传）

---

## 🎯 推荐方案A

直接在GitHub上编辑，1分钟完成！

**请访问：**
```
https://github.com/Sangil1127/ai-tools-nav/edit/main/index.html
```

然后在 `<head>` 里添加：
```html
<meta name="google-site-verification" content="KCqH9ZOpREsN1j23WZ47SZA5VHarPskyyvKVoNk9tIo" />
```

**完成后告诉我，我帮你验证是否部署成功！**
