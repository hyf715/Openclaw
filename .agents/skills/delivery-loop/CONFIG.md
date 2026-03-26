# delivery-loop - 真实交付框架配置

## 配置状态

### ✅ 已完成配置

| 文件 | 状态 | 说明 |
|------|------|------|
| `SKILL.md` | ✅ | Skill 核心文档 |
| `README.md` | ✅ | 使用说明 |
| `scripts/work-loop.sh` | ✅ | 工作循环脚本（15 分钟） |
| `scripts/report-loop.sh` | ✅ | 报告循环脚本（1 小时） |

### 📋 使用方式

#### 1. 手动触发工作循环
```bash
bash ~/.openclaw/workspace/.agents/skills/delivery-loop/scripts/work-loop.sh
```

#### 2. 手动触发报告循环
```bash
bash ~/.openclaw/workspace/.agents/skills/delivery-loop/scripts/report-loop.sh
```

#### 3. 配置 cron 定时执行

添加到 crontab（`crontab -e`）：

```cron
# 每 15 分钟执行一次工作循环
*/15 * * * * /bin/bash ~/.openclaw/workspace/.agents/skills/delivery-loop/scripts/work-loop.sh >> ~/.openclaw/workspace/.agents/skills/delivery-loop/work-loop.log 2>&1

# 每小时执行一次报告循环（例如：08:00, 09:00, 10:00...）
0 * * * * /bin/bash ~/.openclaw/workspace/.agents/skills/delivery-loop/scripts/report-loop.sh >> ~/.openclaw/workspace/.agents/skills/delivery-loop/report-loop.log 2>&1
```

### 🎯 核心规则

1. **Work Loop (15 分钟)**
   - 必须产生可验证的产出
   - 例如：git commit、文件更新、文档导出

2. **Report Loop (1 小时)**
   - 只总结实际交付的内容
   - 必须引用证据（commit ID、路径、URL）
   - 如果无产出，说明原因和下一步计划

3. **反作弊规则**
   - 报告必须基于证据
   - 永远不允许用"盘点/计划"代替实际交付

### 📊 验证清单

在生成报告前，必须检查：
- [ ] 有实际的产出物吗？（commit、文件更新、导出文档）
- [ ] 报告中包含证据吗？（commit ID、路径、URL）
- [ ] 没有把计划当作实际交付吗？
- [ ] 如果无产出，说明了原因和下一步吗？

### 🔧 自定义配置

你可以根据需要修改以下内容：

1. **循环间隔**：修改 cron 配置中的时间
2. **交付物类型**：根据你的项目调整产出标准
3. **报告格式**：修改 report-loop.sh 中的输出格式

### 📝 示例

**工作循环输出**：
```
🚀 Delivery Loop 工作循环启动
⏱️  循环间隔: 15 分钟
🎯 目标: 实际交付，不是计划
📋 Git 状态:
 M AGENTS.md
?? HEARTBEAT.md
⚠️  检测到未提交的变更
💡 建议: 提交这些变更以产生可验证的产出
📊 最近提交:
a1b2c3d Update AGENTS.md
```

**报告循环输出**：
```
📊 Delivery Loop 报告循环启动
⏱️  循环间隔: 1 小时
📝 报告类型: 仅总结实际交付
Git 最近提交 (最近 1 小时):
a1b2c3d Update AGENTS.md
b2c3d4e 添加 HEARTBEAT.md
变更的文件:
AGENTS.md
HEARTBEAT.md
✅ 报告生成完成
```
