#!/bin/bash
# AI工具导航 - 更新前验证脚本
# 防止工具数据丢失

set -e

PROJECT_DIR="/root/.openclaw/workspace/projects/ai-tools-nav"
cd "$PROJECT_DIR"

echo "🔍 更新前验证..."

# 1. 检查当前工具数量
echo "   检查index.html工具数量..."
CURRENT_COUNT=$(grep -o 'data-name=' index.html 2>/dev/null | wc -l || echo "0")
echo "   当前工具数: $CURRENT_COUNT"

# 2. 检查分割文件总数量
echo "   检查分割文件工具数量..."
PART_COUNT=0
for f in index-part*.html; do
    if [ -f "$f" ]; then
        count=$(grep -o 'data-name=' "$f" 2>/dev/null | wc -l || echo "0")
        PART_COUNT=$((PART_COUNT + count))
        echo "   $f: $count 个工具"
    fi
done
echo "   分割文件总计: $PART_COUNT 个工具"

# 3. 验证数量匹配
if [ "$CURRENT_COUNT" -lt "$PART_COUNT" ]; then
    echo ""
    echo "❌ 警告: 工具数量不匹配!"
    echo "   index.html: $CURRENT_COUNT"
    echo "   应有不少于: $PART_COUNT"
    echo ""
    echo "⚠️  可能原因:"
    echo "   - 上次更新时数据丢失"
    echo "   - 需要重新合并工具数据"
    echo ""
    echo "🛠️  建议操作:"
    echo "   1. 从分割文件重新合并工具"
    echo "   2. 验证后再提交"
    echo ""
    exit 1
else
    echo "✅ 工具数量验证通过: $CURRENT_COUNT/$PART_COUNT"
fi

# 4. 检查关键元素
echo "   检查关键元素..."
MISSING=0

if ! grep -q 'google.com/s2/favicons' index.html; then
    echo "   ⚠️  缺少官方logo"
    MISSING=$((MISSING + 1))
fi

if ! grep -q 'tool-card' index.html; then
    echo "   ❌ 缺少工具卡片"
    MISSING=$((MISSING + 1))
fi

if [ "$MISSING" -gt 0 ]; then
    echo "❌ 关键元素检查失败"
    exit 1
fi

echo "✅ 所有验证通过，可以安全更新！"
