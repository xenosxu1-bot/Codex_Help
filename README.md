# Codex Help

一份面向开发者的 OpenAI Codex 非官方双语使用指南，帮助你快速理解 Codex 的核心功能、操作入口、安全边界和高效工作流。

An unofficial bilingual guide for OpenAI Codex, designed to help developers quickly understand Codex features, surfaces, safety boundaries, and practical workflows.

> 本项目根据 2026-07-08 刷新的 OpenAI Codex 官方手册整理。Codex 会持续更新，涉及价格、模型可用性、功能成熟度、企业策略和限制时，请以官方文档为准。

## 在线阅读

| 入口 | 说明 |
| --- | --- |
| [中文版教程 - 网页导航版](https://xenosxu1-bot.github.io/Codex_Help/zh-CN.html) | 推荐阅读入口，左侧带章节目录，适合快速跳转学习。 |
| [English Guide - Web Version](https://xenosxu1-bot.github.io/Codex_Help/en-US.html) | English version with a left-side outline for quick navigation. |
| [中文 Markdown 原文](docs/zh-CN.md) | 适合在 GitHub 中直接阅读、复制或二次编辑。 |
| [English Markdown Source](docs/en-US.md) | Markdown source for GitHub reading, copying, or editing. |

## 项目适合谁

- 第一次接触 Codex，希望快速上手的开发者。
- 想区分 Codex App、CLI、IDE Extension、Cloud 等入口的用户。
- 希望把 Codex 引入团队研发流程的工程团队。
- 想系统了解 `AGENTS.md`、`config.toml`、Skills、Plugins、MCP、Hooks、Rules、Automations 和 Subagents 的进阶用户。

## 你可以学到什么

- Codex 是什么，适合处理哪些开发任务。
- 如何选择 Codex App、CLI、IDE Extension、Cloud、GitHub、Slack 和 Linear。
- 如何写包含目标、上下文、约束和完成标准的高质量提示词。
- 如何使用 Plan mode、Goal mode、threads、worktrees 和 review。
- 沙箱、审批、网络访问和 web search 的基本安全模型。
- 如何用 `AGENTS.md` 和 `config.toml` 固化项目规则与默认行为。
- 如何通过 Skills、Plugins、MCP 和 Automations 把重复流程变成可复用能力。

## 快速开始

1. 在 Codex App、CLI 或 IDE 中打开仓库根目录。
2. 先让 Codex 理解项目，不要急着改代码：

   ```text
   请阅读这个项目的结构，找出构建、测试、lint 命令，以及主要源码目录和项目约定。
   先不要修改文件。
   ```

3. 添加可复用的项目规则：

   ```text
   请为这个仓库生成 AGENTS.md。
   包括安装命令、测试命令、lint、代码风格、review 要求和完成标准。
   ```

4. 从小而可验证的任务开始：

   ```text
   修复这个失败测试，不要改变公开 API。
   修复后运行最小相关测试，并报告命令和结果。
   ```

5. 接受改动前先审查：

   ```text
   /review
   ```

## 仓库结构

```text
Codex_Help/
  README.md
  docs/
    zh-CN.md
    en-US.md
    zh-CN.html
    en-US.html
    source-check.md
  assets/
    images/
  tools/
    generate_pages.py
  LICENSE
  NOTICE.md
  CONTRIBUTING.md
```

## 结构说明

| 路径 | 作用 |
| --- | --- |
| `README.md` | 仓库首页，提供项目介绍、在线阅读入口、快速开始和仓库结构。 |
| `docs/zh-CN.md` | 中文完整教程 Markdown 原文。 |
| `docs/en-US.md` | English full guide in Markdown. |
| `docs/zh-CN.html` | 中文网页导航版，左侧带章节目录，用于 GitHub Pages。 |
| `docs/en-US.html` | English web version with a left-side outline for GitHub Pages. |
| `docs/source-check.md` | 记录本教程对照官方 Codex 手册校验的范围和刷新时间。 |
| `assets/images/` | Markdown 教程引用的 Codex 界面截图。 |
| `docs/assets/images/` | GitHub Pages 网页版使用的截图资源。 |
| `tools/generate_pages.py` | 将 Markdown 教程生成带左侧目录的 HTML 页面。 |
| `LICENSE` | MIT License，说明本仓库原创教程文本的许可。 |
| `NOTICE.md` | 非官方说明，以及 OpenAI 名称、商标、官方文档和截图权利归属说明。 |
| `CONTRIBUTING.md` | 贡献指南，说明如何基于官方文档更新内容并保持中英文一致。 |

## 官方文档

本仓库是学习辅助材料，不替代官方文档。建议结合以下官方页面阅读：

- [Codex overview](https://developers.openai.com/codex/overview)
- [Codex prompting](https://developers.openai.com/codex/prompting)
- [Codex workflows](https://developers.openai.com/codex/workflows)
- [Codex App](https://developers.openai.com/codex/app)
- [Codex CLI](https://developers.openai.com/codex/cli)
- [Codex IDE Extension](https://developers.openai.com/codex/ide)
- [Configuration](https://developers.openai.com/codex/config-basic)
- [Agent approvals and security](https://developers.openai.com/codex/agent-approvals-security)
- [AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [Skills](https://developers.openai.com/codex/skills)
- [Plugins](https://developers.openai.com/codex/plugins)
- [MCP](https://developers.openai.com/codex/mcp)

来源校验：[docs/source-check.md](docs/source-check.md)

## English

Codex Help is an unofficial bilingual guide for OpenAI Codex.

### Read Online

| Entry | Description |
| --- | --- |
| [Chinese Guide - Web Version](https://xenosxu1-bot.github.io/Codex_Help/zh-CN.html) | Chinese guide with a left-side outline. |
| [English Guide - Web Version](https://xenosxu1-bot.github.io/Codex_Help/en-US.html) | Recommended English reading experience with quick navigation. |
| [Chinese Markdown Source](docs/zh-CN.md) | Markdown source for GitHub reading or editing. |
| [English Markdown Source](docs/en-US.md) | Markdown source for GitHub reading or editing. |

### What You Will Learn

- What Codex is and which development tasks it is good at.
- How to choose between Codex App, CLI, IDE Extension, Cloud, GitHub, Slack, and Linear.
- How to write prompts with goal, context, constraints, and done criteria.
- How Plan mode, Goal mode, threads, worktrees, and review workflows work.
- How sandboxing, approvals, network access, and web search work.
- How to configure `config.toml`, `AGENTS.md`, Skills, Plugins, MCP, Hooks, Rules, Automations, and Subagents.

## License

本仓库原创教程文本采用 MIT License。OpenAI 产品名称、商标、官方文档和截图仍受其各自权利方条款约束。

The original guide text in this repository is released under the MIT License. OpenAI product names, trademarks, documentation, and screenshots remain subject to their respective owners' terms.
