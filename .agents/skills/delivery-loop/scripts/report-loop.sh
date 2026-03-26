#!/usr/bin/env bash
# delivery-loop: 生成报告循环
# 每小时执行一次

echo "📊 Delivery Loop 报告循环启动"
echo "⏱️  循环间隔: 1 小时"
echo "📝 报告类型: 仅总结实际交付"

# 获取最近的 git commits（最近 1 小时）
echo "Git 最近提交 (最近 1 小时):"
git log --oneline --since="1 hour ago" --all

# 如果没有最近的提交，检查全天的提交
if [ -z "$(git log --oneline --since="1 hour ago" --all)" ]; then
    echo "⚠️  最近 1 小时无提交"
    echo "📋 今日提交:"
    git log --oneline --since="00:00" --all
fi

# 列出变更的文件
echo "变更的文件:"
git diff HEAD~5 --name-only

# 检查是否有未提交的变更
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  检测到未提交的变更，可能需要提交"
fi

echo "✅ 报告生成完成"
