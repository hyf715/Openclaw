# OpenClaw 复活指南

## 当前状态
OpenClaw 目前运行正常：
- **Gateway**: 127.0.0.1:18789 (loopback-only)
- **服务**: LaunchAgent (loaded, running)
- **进程**: pid 13084
- **状态**: RPC probe: ok

---

## OpenClaw 挂掉后的复活方法

### 方法 1: 使用 openclaw 命令重启（推荐）

```bash
# 检查状态
openclaw status

# 重启 Gateway
openclaw gateway restart

# 或者
openclaw gateway stop
openclaw gateway start
```

### 方法 2: 手动重启 LaunchAgent

```bash
# 停止服务
launchctl stop ai.openclaw.gateway

# 启动服务
launchctl start ai.openclaw.gateway

# 或者重新加载
launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist
launchctl load ~/Library/LaunchAgents/ai.openclaw.gateway.plist
```

### 方法 3: 手动启动 Gateway 进程

```bash
# 直接运行 Gateway
node /opt/homebrew/lib/node_modules/openclaw/dist/index.js gateway --port 18789

# 后台运行
nohup node /opt/homebrew/lib/node_modules/openclaw/dist/index.js gateway --port 18789 > ~/.openclaw/logs/gateway.log 2>&1 &
```

### 方法 4: 检查并修复配置

```bash
# 检查配置文件
cat ~/.openclaw/openclaw.json

# 如果配置有问题，重新配置
openclaw configure
```

---

## 故障排查

### 检查日志
```bash
# Gateway 日志
tail -f ~/.openclaw/logs/gateway.log

# 错误日志
tail -f ~/.openclaw/logs/gateway.err.log

# 系统日志
tail -f /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log
```

### 检查端口占用
```bash
# 检查 18789 端口
lsof -i :18789

# 如果端口被占用，杀死进程
lsof -ti :18789 | xargs kill -9
```

### 检查 Node.js 环境
```bash
# 检查 Node.js 版本
node --version

# 检查 OpenClaw 版本
npm list -g openclaw
```

---

## 预防措施

### 1. 启用 KeepAlive
LaunchAgent 已配置 `KeepAlive: true`，OpenClaw 挂掉后会自动重启。

### 2. 监控状态
定期运行 `openclaw status` 检查服务状态。

### 3. 备份配置
```bash
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup
```

### 4. 检查依赖
确保 Node.js 和 OpenClaw 正常安装：
```bash
node --version
npm list -g openclaw
```

---

## 快速命令参考

```bash
# 重启 OpenClaw
openclaw gateway restart

# 检查状态
openclaw status

# 查看日志
tail -f ~/.openclaw/logs/gateway.log

# 手动启动
node /opt/homebrew/lib/node_modules/openclaw/dist/index.js gateway --port 18789
```

---

## 联系支持

如果以上方法都无法复活 OpenClaw：
- 文档: https://docs.openclaw.ai/troubleshooting
- 社区: https://discord.com/invite/clawd