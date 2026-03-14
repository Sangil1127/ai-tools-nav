#!/bin/bash
# GitHub Pages 故障排查脚本

echo "🔧 GitHub Pages 故障排查"
echo "=========================="
echo ""

cd /root/.openclaw/workspace/projects/ai-tools-nav

# 检查当前配置
echo "📊 当前配置:"
echo "  远程仓库:"
git remote -v
echo ""
echo "  本地分支:"
git branch
echo ""
echo "  文件列表:"
ls -la *.html 2>/dev/null | grep -E "index\.html|simple\.html"
echo ""

# 修复步骤
echo "🔧 修复步骤:"
echo ""

# 1. 检查是否有远程仓库
if ! git remote | grep -q origin; then
    echo "❌ 错误: 没有配置远程仓库"
    echo "   请运行: git remote add origin https://github.com/你的用户名/ai-tools-nav.git"
    exit 1
fi

# 2. 重命名分支为main（GitHub Pages默认）
echo "步骤 1: 重命名分支为 main..."
git branch -m master main 2>/dev/null || echo "  分支可能已经是 main"

# 3. 重新推送
echo "步骤 2: 推送代码到 GitHub..."
git push -u origin main --force

echo ""
echo "✅ 修复完成！"
echo ""
echo "⏳ 请等待 5-10 分钟后刷新页面"
echo ""
echo "📋 检查清单:"
echo "   □ 仓库是 Public（公开）吗？"
echo "   □ Settings → Pages 中 Source 选择了 main / root 吗？"
echo "   □ 等待了至少 5 分钟吗？"
echo ""
echo "🌐 访问地址: https://$(git remote get-url origin | sed 's/.*github.com\///; s/\.git$//').github.io/ai-tools-nav/"
