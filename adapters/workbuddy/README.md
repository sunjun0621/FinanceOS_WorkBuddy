# WorkBuddy Adapter

## 安装

### 方式一：SkillHub 安装
```bash
skillhub install financeos
```

### 方式二：手动安装
将 `SKILL.md` 复制到 `~/.workbuddy/skills/financeos/SKILL.md`

### 方式三：作为项目 Skill
将 `SKILL.md` 复制到 `{workspace}/.workbuddy/skills/financeos/SKILL.md`

## 使用

在 WorkBuddy 对话中：
```
/financeos 帮我做月度经营分析
```

或直接引用数据文件：
```
/financeos 分析这份报表 @"/path/to/report.xlsx"
```

## KB 路径

WorkBuddy 适配器默认 KB 路径为 `~/.workbuddy/financeos-kb/`。

安装后需将本仓库的 `kb/` 目录内容复制到该路径。
