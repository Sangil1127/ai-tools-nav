#!/bin/bash
# 空闲时间自动执行检查
# 添加到crontab或heartbeat中

PROJECT_DIR="/root/.openclaw/workspace/projects/ai-tools-nav"
BATCH_DIR="$PROJECT_DIR/batches"
LOCK_FILE="/tmp/ai-tools-batch.lock"

# 检查是否正在执行
if [ -f "$LOCK_FILE" ]; then
    PID=$(cat "$LOCK_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo "⏳ 已有批次在执行中 (PID: $PID)，跳过"
        exit 0
    else
        rm -f "$LOCK_FILE"
    fi
fi

# 获取当前时间
HOUR=$(date +%H)
# 只在工作时间自动执行 (9-22点)
if [ "$HOUR" -lt 9 ] || [ "$HOUR" -gt 22 ]; then
    echo "🌙 非工作时间，跳过自动执行"
    exit 0
fi

# 检查是否有待执行批次
cd "$PROJECT_DIR"
CURRENT_COUNT=$(grep -o 'data-name=' index.html 2>/dev/null | wc -l || echo "0")
NEXT_BATCH_START=$(( (CURRENT_COUNT / 25) * 25 + 1 ))
NEXT_BATCH_END=$((NEXT_BATCH_START + 24))
BATCH_FILE="$BATCH_DIR/batch-$(printf "%03d" $NEXT_BATCH_START)-$(printf "%03d" $NEXT_BATCH_END).json"

if [ ! -f "$BATCH_FILE" ]; then
    echo "📭 没有待执行批次 (下一批: $NEXT_BATCH_START-$NEXT_BATCH_END)"
    echo "   请先准备批次数据"
    exit 0
fi

# 创建锁文件
echo $$ > "$LOCK_FILE"

# 执行更新
echo "🤖 空闲时间自动执行批次更新..."
"$PROJECT_DIR/scripts/batch-update.sh"

# 清理锁文件
rm -f "$LOCK_FILE"
