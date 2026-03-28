# MEMORY.md - Long-Term Memory

## 2026-03-27 - Skillhub Installation & Amazon Product Search

### Key Events
- Installed Skillhub CLI only mode initially, then full Skillhub store
- Skills installed via Skillhub: `find-skills`, `skillhub-preference`
- Reviewed existing skills vs Skillhub versions
- Attempted to find Amazon Industrial & Scientific rising products

### Decisions
- Installed Skillhub full version for better skill discovery and updates
- Used web_fetch/web_search before browser automation for efficiency
- Subagent fallback needed due to Amazon's dynamic content loading

### Security Lessons
- Always check security risk assessments before installing skills
- Be cautious of skills using `shell: true` with user input
- Verify skill sources (official > community)
- Review SKILL.md for suspicious patterns

### Amazon Product Search Results
- Swiffer WetJet Multi-Surface Floor Cleaner Solution Refill (3,456+销量)
- Dawn Ultra Dish Suction Dispenser (销量显著上升)
- Mrs. Meyer's Clean Day Multi-Surface Cleaner (留香型，销量上升)
- Simple Green All-Purpose Cleaner (128oz 大容量装)
- Lysol Disinfectant Spray (消毒喷雾，销量上升)

### Open Questions
- How to properly audit skills with shell access?
- Should cron tasks run in isolated or current session?
- How to configure npm cache permissions for subagents?
- Should we create a dedicated Amazon scraper skill?

### 2026-03-27 更新
- Skillhub 已安装完成，包括 CLI 和 skills（find-skills, skillhub-preference）
- Amazon Industrial & Scientific 类别销量上升产品已部分识别（Swiffer, Dawn, Mrs. Meyer's, Simple Green, Lysol）
- 子代理遇到 npm 缓存权限问题，需后续解决
- 每日回顾任务自动执行，检查内存和待办事项

## 2026-03-28 - 本周总结
### Key Events
- 本周主要工作围绕 Skillhub 安装和 Amazon 产品搜索展开
- 成功识别了 5 个 Amazon Industrial & Scientific 类别的热销产品
- 尝试使用子代理执行任务，遇到 npm 缓存权限问题

### Decisions
- 优先使用 web_fetch/web_search 而非浏览器自动化以提高效率
- 记录每周总结，便于追踪进度和经验教训

### Open Questions
- 如何为子代理正确配置 npm 缓存权限？
- 是否应该创建专用的 Amazon scraper 技能？

### 2026-03-28 更新
- 本周总结已完成，记录在 memory/2026-03-28.md
- 主要成就：Skillhub 安装完成，自动化每日回顾任务已启动
- 待解决：npm 缓存权限问题，Amazon 产品监控技能创建

## 2026-03-27 - npm 缓存权限问题解决尝试
### Key Events
- Subagent 尝试使用 agent-browser 技能访问 Amazon 网站
- 遇到 npm 缓存权限问题，无法完全执行任务
- 最终通过 web_fetch/web_search 获取了部分 Amazon 产品信息
