# Git 自动推送配置

## 配置状态

### ✅ 已完成
- **LaunchAgent**: `user.openclaw.git-push.plist` 已创建
- **调度间隔**: 每 900 秒（15 分钟）
- **状态**: 已加载并启动

### 📋 工作原理

LaunchAgent 每 15 分钟自动执行：
```bash
cd /Users/littlemy/.openclaw/workspace
git pull --rebase origin main
git push origin main
```

### 📁 日志位置

- **成功日志**: `/Users/littlemy/.openclaw/logs/git-push.log`
- **错误日志**: `/Users/littlemy/.openclaw/logs/git-push.err.log`

### ⚠️ 注意事项

**目前需要手动认证**：
由于 GitHub 需要认证，首次推送需要你手动输入用户名和 Personal Access Token。

运行一次手动推送来缓存凭证：
```bash
cd /Users/littlemy/.openclaw/workspace
git push origin main
```

输入：
- **Username**: `hyf715`
- **Password**: 你的 GitHub Personal Access Token

之后 LaunchAgent 就可以自动推送了。

### 🔧 管理命令

```bash
# 查看状态
launchctl list | grep git-push

# 停止
launchctl unload ~/Library/LaunchAgents/user.openclaw.git-push.plist

# 重新加载
launchctl load ~/Library/LaunchAgents/user.openclaw.git-push.plist

# 手动触发
launchctl start user.openclaw.git-push

# 查看日志
tail -f /Users/littlemy/.openclaw/logs/git-push.log
```

### 📝 推送内容

当前本地提交（共 6 个）：
```
14d2d91 Add GitHub remote setup guide
ead93fe Add OpenClaw recovery guide
e1a40a8 Configure delivery-loop: add CONFIG.md and update scripts
465b5e0 Add delivery-loop skill: goal-driven delivery loop for chat-based agents
590ac3a Remove nano-banana-pro skill
8f53230 Add HEARTBEAT.md with scheduled tasks
```
