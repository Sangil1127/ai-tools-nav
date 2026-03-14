#!/bin/bash
# GitHub Pages 部署脚本

echo "🚀 AI工具导航 - GitHub Pages 部署脚本"
echo "=========================================="
echo ""

# 配置
PROJECT_DIR="/root/.openclaw/workspace/projects/ai-tools-nav"
REPO_NAME="ai-tools-nav"

cd "$PROJECT_DIR"

# 1. 检查git
echo "📦 步骤 1/5: 检查Git..."
if ! command -v git &> /dev/null; then
    apt-get update > /dev/null 2>&1
    apt-get install -y git
fi

# 2. 初始化git仓库
echo "📦 步骤 2/5: 初始化Git仓库..."
git init
git config user.email "deploy@ai-tools-nav.com"
git config user.name "AI Tools Nav"

# 3. 准备文件
echo "📦 步骤 3/5: 准备文件..."

# 确保 index.html 在根目录
if [ ! -f "index.html" ]; then
    echo "❌ 错误: index.html 不存在"
    exit 1
fi

# 创建 README
cat > README.md << 'EOF'
# AI工具导航

精选全球优质AI工具，助你提升10倍工作效率。

## 在线访问
https://你的用户名.github.io/ai-tools-nav/

## 收录工具
- AI写作工具 (ChatGPT, Claude, Kimi, 文心一言等)
- AI绘画工具 (Midjourney, Stable Diffusion, DALL-E 3等)
- AI编程工具 (GitHub Copilot, Cursor, Codeium等)
- AI视频工具 (Runway, HeyGen, Descript等)
- AI办公效率工具

## 特点
- 每日更新，持续收录最新AI工具
- 免费/付费分类
- 国产AI专题
- 完全免费访问

## 技术栈
- HTML5 + CSS3
- 响应式设计
- 深色科技主题
EOF

# 4. 提交代码
echo "📦 步骤 4/5: 提交代码..."
git add .
git commit -m "Initial commit: AI Tools Navigation website"

echo ""
echo "=========================================="
echo "✅ 本地Git仓库准备完成！"
echo ""
echo "📝 接下来请手动完成以下步骤："
echo ""
echo "步骤 1: 在GitHub创建仓库"
echo "   1. 访问 https://github.com/new"
echo "   2. 仓库名: ai-tools-nav"
echo "   3. 选择 Public (公开)"
echo "   4. 不要勾选 README (我们已创建)"
echo "   5. 点击 Create repository"
echo ""
echo "步骤 2: 配置远程仓库并推送"
echo "   执行以下命令（替换YOUR_USERNAME）："
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/ai-tools-nav.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "步骤 3: 启用GitHub Pages"
echo "   1. 进入仓库 Settings → Pages"
echo "   2. Source 选择 Deploy from a branch"
echo "   3. Branch 选择 main / root"
echo "   4. 点击 Save"
echo "   5. 等待几分钟，访问: https://YOUR_USERNAME.github.io/ai-tools-nav/"
echo ""
echo "=========================================="
echo ""

# 显示当前状态
echo "📊 当前仓库状态:"
git status --short
echo ""
echo "📁 文件列表:"
ls -la *.html *.md 2>/dev/null || ls -la
