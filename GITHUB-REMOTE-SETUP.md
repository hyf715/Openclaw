# GitHub 远程仓库配置

## 已配置的远程仓库

- **远程名称**: `origin`
- **URL**: `https://github.com/hyf715/Openclaw.git`
- **分支**: `main`

## 推送认证方式

### 方法 1: 使用 GitHub Personal Access Token（推荐）

1. 访问 https://github.com/settings/tokens
2. 创建新的 Personal Access Token
3. 选择范围：`repo`（读写代码仓库）
4. 复制生成的 token

然后运行：
```bash
cd /Users/littlemy/.openclaw/workspace
git push origin main
# 输入用户名: your-github-username
# 输入密码: paste-your-token-here
```

### 方法 2: 使用 SSH（更安全）

1. 生成 SSH 密钥（如果还没有）：
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

2. 复制公钥到剪贴板：
```bash
cat ~/.ssh/id_ed25519.pub
```

3. 将公钥添加到 GitHub：https://github.com/settings/keys

4. 修改远程 URL：
```bash
git remote set-url origin git@github.com:hyf715/Openclaw.git
```

5. 推送：
```bash
git push -u origin main
```

## 当前配置状态

```bash
cd /Users/littlemy/.openclaw/workspace
git remote -v
# origin  https://github.com/hyf715/Openclaw.git (fetch)
# origin  https://github.com/hyf715/Openclaw.git (push)
```

## 下一步

选择上述任一方法完成认证后，运行：
```bash
git push -u origin main
```
