#!/usr/bin/env bash
# delivery-loop: 检查 git 状态并准备下一个交付物
# 每 15 分钟执行一次

echo "🚀 Delivery Loop 工作循环启动"
echo "⏱️  循环间隔: 15 分钟"
echo "🎯 目标: 实际交付，不是计划"

# 检查 git 状态
echo "📋 Git 状态:"
git status --short

# 检查是否有未提交的变更
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  检测到未提交的变更"
    echo "💡 建议: 提交这些变更以产生可验证的产出"
else
    echo "✅ Git 状态干净"
    echo "💡 建议: 开始下一个任务，产生新的交付物"
fi

echo "📊 最近提交:"
git log --oneline -5
