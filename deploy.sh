#!/bin/bash
# GitHub Pages 一键部署脚本
# 用户: Sangil1127
# 项目: ai-tools-nav

echo "🚀 AI工具导航 - GitHub部署脚本"
echo "================================"
echo ""

# 检查git是否安装
if ! command -v git &> /dev/null; then
    echo "❌ 错误: 未安装git"
    exit 1
fi

# 进入项目目录
cd /root/.openclaw/workspace/projects/ai-tools-nav

echo "📁 当前目录: $(pwd)"
echo ""

# 检查远程仓库
echo "🔍 检查远程仓库..."
if git remote | grep -q "origin"; then
    echo "✅ 远程仓库已配置"
    git remote -v
else
    echo "📝 添加远程仓库..."
    git remote add origin https://github.com/Sangil1127/ai-tools-nav.git
    echo "✅ 远程仓库添加成功"
fi

echo ""
echo "📤 准备推送代码..."
echo ""

# 确保分支名为main
git branch -m master main 2>/dev/null || true

# 添加所有文件
echo "📝 添加文件到暂存区..."
git add -A

# 提交
echo "💾 提交更改..."
git commit -m "部署: AI工具导航 v1.0 - SEO优化版" || echo "⚠️ 没有新的更改需要提交"

# 推送到GitHub
echo ""
echo "🚀 推送到GitHub..."
echo "如果提示登录，请按指示操作"
echo ""
git push -u origin main

echo ""
echo "================================"
echo "✅ 推送完成！"
echo ""
echo "下一步:"
echo "1. 访问 https://github.com/Sangil1127/ai-tools-nav/settings/pages"
echo "2. 启用 GitHub Pages"
echo "3. 等待2-5分钟后访问: https://Sangil1127.github.io/ai-tools-nav/"
echo ""
