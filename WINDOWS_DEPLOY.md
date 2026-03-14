# Windows 云 PC 部署方案

## 方案A：安装 Git（推荐）

### 步骤1：下载并安装 Git
访问：https://git-scm.com/download/win

或者使用 PowerShell 安装：
```powershell
# 使用 winget 安装（Windows 10/11）
winget install --id Git.Git -e --source winget
```

安装时全部选默认选项即可。

### 步骤2：安装后重启 PowerShell
关闭当前窗口，重新打开 PowerShell

### 步骤3：验证安装
```powershell
git --version
```

### 步骤4：配置并推送
```powershell
# 配置Git
git config --global user.name "Sangil1127"
git config --global user.email "your-email@example.com"

# 创建本地仓库文件夹
mkdir ai-tools-nav
cd ai-tools-nav

# 初始化git
git init
git branch -m master main

# 复制所有项目文件到 ai-tools-nav 文件夹

# 添加并提交
git add .
git commit -m "Initial commit"

# 连接GitHub并推送
git remote add origin https://github.com/Sangil1127/ai-tools-nav.git
git push -u origin main
```

---

## 方案B：不用Git，直接上传（更简单）

### 步骤1：在GitHub创建仓库
访问：https://github.com/new
- Repository name: `ai-tools-nav`
- 选择 Public
- 勾选 "Add a README file"
- 点击 Create repository

### 步骤2：直接上传文件
1. 打开仓库页面：https://github.com/Sangil1127/ai-tools-nav
2. 点击 "Add file" → "Upload files"
3. 拖拽或选择以下文件上传：
   - index.html
   - sitemap.xml
   - robots.txt
4. 点击 "Commit changes"

### 步骤3：启用GitHub Pages
1. 进入 Settings → Pages
2. Source 选择 "Deploy from a branch"
3. Branch 选择 "main" / "(root)"
4. 点击 Save

5分钟后访问：https://Sangil1127.github.io/ai-tools-nav/

---

## 方案C：我帮你打包文件

我把所有文件打包成 ZIP，你下载后解压上传到 GitHub。

需要这个方案吗？回复 "要ZIP"
