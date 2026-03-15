#!/bin/bash
# AI工具导航 - 批次更新脚本
# 每次执行添加25个工具，自动保存版本

set -e

PROJECT_DIR="/root/.openclaw/workspace/projects/ai-tools-nav"
BATCH_DIR="$PROJECT_DIR/batches"
SCRIPT_DIR="$PROJECT_DIR/scripts"

cd "$PROJECT_DIR"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🚀 AI工具导航 - 批次更新脚本"
echo "=============================="

# 1. 检查当前进度
echo ""
echo "📊 检查当前进度..."

CURRENT_COUNT=$(grep -o 'data-name=' index.html 2>/dev/null | wc -l || echo "0")
echo "   当前工具数量: $CURRENT_COUNT"

# 计算下一批次
BATCH_NUM=$(( (CURRENT_COUNT / 25) + 1 ))
START_NUM=$((CURRENT_COUNT + 1))
END_NUM=$((START_NUM + 24))

echo "   下一批次: 第$BATCH_NUM批"
echo "   目标范围: $START_NUM - $END_NUM"

# 2. 检查是否有预定义批次文件
BATCH_FILE="$BATCH_DIR/batch-$(printf "%03d" $START_NUM)-$(printf "%03d" $END_NUM).json"

if [ -f "$BATCH_FILE" ]; then
    echo ""
    echo "✅ 发现预定义批次文件: $(basename $BATCH_FILE)"
    echo "   准备合并到主文件..."
    
    # 这里调用Python脚本合并工具
    python3 "$SCRIPT_DIR/merge-batch.py" "$BATCH_FILE"
    
    echo "   ✅ 批次合并完成"
else
    echo ""
    echo "⚠️  未找到批次文件: $(basename $BATCH_FILE)"
    echo "   请先准备批次数据或使用交互模式"
    exit 1
fi

# 3. 验证更新
echo ""
echo "🔍 验证更新..."

NEW_COUNT=$(grep -o 'data-name=' index.html 2>/dev/null | wc -l || echo "0")
echo "   更新后工具数量: $NEW_COUNT"

if [ "$NEW_COUNT" -lt "$END_NUM" ]; then
    echo "   ❌ 警告: 工具数量未达到预期 ($NEW_COUNT < $END_NUM)"
    echo "   请检查批次文件内容"
    exit 1
fi

echo "   ✅ 验证通过"

# 4. 版本存档
echo ""
echo "💾 执行版本存档..."
"$SCRIPT_DIR/version-archive.sh"

# 5. 生成批次报告
echo ""
echo "📝 生成批次报告..."

cat > "$BATCH_DIR/batch-$(printf "%03d" $START_NUM)-$(printf "%03d" $END_NUM)-report.md" << EOF
# 批次更新报告

## 基本信息
- **批次编号**: 第$BATCH_NUM批
- **工具范围**: $START_NUM - $END_NUM
- **执行时间**: $(date '+%Y-%m-%d %H:%M:%S')
- **执行状态**: ✅ 成功

## 更新内容
- 新增工具数: $((NEW_COUNT - CURRENT_COUNT))
- 更新后总数: $NEW_COUNT
- 目标进度: $((NEW_COUNT * 100 / 1000))%

## 分类统计
$(grep -o 'data-category="[^"]*"' index.html | sed 's/data-category=//' | sort | uniq -c | sort -rn | head -15)

## 下一批次
- 批次编号: 第$((BATCH_NUM + 1))批
- 目标范围: $((END_NUM + 1)) - $((END_NUM + 25))
EOF

echo "   ✅ 报告已保存"

# 6. 完成汇总
echo ""
echo "=============================="
echo -e "${GREEN}🎉 第$BATCH_NUM批更新完成！${NC}"
echo "   新增工具: $((NEW_COUNT - CURRENT_COUNT))个"
echo "   当前总数: $NEW_COUNT个"
echo "   总进度: $((NEW_COUNT * 100 / 1000))%"
echo "   剩余: $((1000 - NEW_COUNT))个"
echo ""
echo "   下一批: 第$((BATCH_NUM + 1))批 ($((END_NUM + 1))-$((END_NUM + 25)))"
echo "=============================="

# 7. 提示下一批
echo ""
echo "💡 提示:"
echo "   - 批次报告: $BATCH_DIR/batch-$(printf "%03d" $START_NUM)-$(printf "%03d" $END_NUM)-report.md"
echo "   - 继续执行: ./scripts/batch-update.sh"
echo ""
