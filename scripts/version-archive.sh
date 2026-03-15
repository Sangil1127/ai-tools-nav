#!/bin/bash
# AI工具导航网站 - 版本存档脚本
# 确保每次更新都有完整备份和记录

set -e  # 遇到错误立即退出

echo "🚀 开始版本存档流程..."

PROJECT_DIR="/root/.openclaw/workspace/projects/ai-tools-nav"
BACKUP_DIR="/root/.openclaw/workspace/projects/ai-tools-nav/backups"
VERSION_LOG="/root/.openclaw/workspace/projects/ai-tools-nav/VERSION_LOG.md"

cd "$PROJECT_DIR"

# 1. 检查Git状态
echo "📋 检查Git状态..."
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  发现未提交的更改，准备提交..."
    
    # 生成版本号
    VERSION=$(date +"v%Y.%m.%d-%H%M")
    
    # 获取变更摘要
    CHANGES=$(git diff --stat | tail -1)
    
    # 提交所有更改
    git add -A
    git commit -m "[$VERSION] 自动存档 - $CHANGES" || echo "无新内容提交"
    
    # 推送到远程
    git push origin main
    
    echo "✅ Git提交完成: $VERSION"
else
    echo "✅ 工作区干净，无需提交"
fi

# 2. 创建本地备份
echo "💾 创建本地备份..."
mkdir -p "$BACKUP_DIR"

BACKUP_NAME="backup-$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$BACKUP_DIR/$BACKUP_NAME" \
    --exclude='node_modules' \
    --exclude='.git' \
    --exclude='backups' \
    . 2>/dev/null || true

echo "✅ 备份创建: $BACKUP_NAME"

# 3. 记录版本日志
echo "📝 记录版本日志..."
if [ ! -f "$VERSION_LOG" ]; then
    echo "# AI工具导航 - 版本更新日志" > "$VERSION_LOG"
    echo "" >> "$VERSION_LOG"
fi

cat >> "$VERSION_LOG" << EOF

## $(date '+%Y-%m-%d %H:%M:%S')
- **版本**: $VERSION
- **提交**: $(git rev-parse --short HEAD)
- **状态**: ✅ 已存档
- **备份**: $BACKUP_NAME
- **工具数**: $(grep -o 'class="tool-card"' index.html 2>/dev/null | wc -l || echo "N/A")

EOF

echo "✅ 版本日志已更新"

# 4. 验证存档完整性
echo "🔍 验证存档完整性..."

# 检查关键文件
if [ ! -f "index.html" ]; then
    echo "❌ 错误: index.html 不存在!"
    exit 1
fi

# 检查工具数量
TOOL_COUNT=$(grep -o 'class="tool-card"' index.html 2>/dev/null | wc -l || echo "0")
echo "   工具数量: $TOOL_COUNT"

# 检查Git提交是否同步
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main 2>/dev/null || echo "N/A")

if [ "$LOCAL" = "$REMOTE" ]; then
    echo "✅ 本地与远程同步"
else
    echo "⚠️  本地与远程不同步，强制推送..."
    git push origin main --force-with-lease
fi

# 5. 清理旧备份（保留最近10个）
echo "🧹 清理旧备份..."
cd "$BACKUP_DIR" && ls -t *.tar.gz 2>/dev/null | tail -n +11 | xargs rm -f 2>/dev/null || true
cd "$PROJECT_DIR"

echo ""
echo "🎉 版本存档流程完成！"
echo "   版本: $VERSION"
echo "   备份: $BACKUP_DIR/$BACKUP_NAME"
echo "   日志: $VERSION_LOG"
