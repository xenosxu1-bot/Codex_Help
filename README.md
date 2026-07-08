<h1 align="center">Codex Help</h1>

<p align="center">
  An unofficial OpenAI Codex guide for developers: quick start, core workflows, safety, configuration, and practical usage tips.
</p>

<p align="center">
  <a href="#english">English</a>
  &middot;
  <a href="#chinese">中文</a>
</p>

<p align="center">
  <img src="assets/images/codex-readme-banner.jpg" alt="Codex App interface preview" width="900">
</p>

<a id="english"></a>

## English

Codex Help is an unofficial learning guide for OpenAI Codex. It is designed to help developers quickly understand Codex surfaces, prompting patterns, safety boundaries, configuration, and practical workflows.

> This repository is based on the OpenAI Codex official manual refreshed on 2026-07-08. Codex changes over time, so pricing, model availability, feature maturity, enterprise controls, and limits should always be verified against the official documentation.

### Read Online

| Entry | Description |
| --- | --- |
| [English Guide - Web Version](https://xenosxu1-bot.github.io/Codex_Help/en-US.html) | Recommended entry. Includes a left-side outline for quick navigation. |
| [English Markdown Source](docs/en-US.md) | Markdown source for GitHub reading or editing. |
| [Chinese Guide - Web Version](https://xenosxu1-bot.github.io/Codex_Help/zh-CN.html) | Chinese web guide with a left-side outline. |
| [Chinese Markdown Source](docs/zh-CN.md) | Chinese Markdown source. |

### Highlights

- Understand what Codex is and which development tasks it is good at.
- Choose between Codex App, CLI, IDE Extension, Cloud, GitHub, Slack, and Linear.
- Write effective prompts with goal, context, constraints, and done criteria.
- Learn Plan mode, Goal mode, threads, worktrees, and review workflows.
- Configure `config.toml`, `AGENTS.md`, Skills, Plugins, MCP, Hooks, Rules, Automations, and Subagents.

### Repository Structure

| Path | Purpose |
| --- | --- |
| `README.md` | Project homepage and language entry point. |
| `docs/en-US.md` | English guide in Markdown. |
| `docs/zh-CN.md` | Chinese guide in Markdown. |
| `docs/en-US.html` | English web guide with a left-side outline. |
| `docs/zh-CN.html` | Chinese web guide with a left-side outline. |
| `assets/images/` | Screenshots used by the Markdown guides and README. |
| `docs/assets/images/` | Screenshot assets used by GitHub Pages. |
| `tools/generate_pages.py` | Generates the web pages with a left-side outline. |
| `docs/source-check.md` | Official documentation refresh and source-check notes. |

### Official Documentation

This repository is a learning companion, not a replacement for the official documentation.

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

Source check: [docs/source-check.md](docs/source-check.md)

### License

The original guide text in this repository is released under the MIT License. OpenAI product names, trademarks, documentation, and screenshots remain subject to their respective owners' terms.

<a id="chinese"></a>

## 中文

Codex Help 是一份 OpenAI Codex 非官方学习指南，面向希望快速熟悉 Codex 的开发者。它覆盖 Codex 的使用入口、提示词写法、安全边界、配置方式和常见工作流。

> 本项目根据 2026-07-08 刷新的 OpenAI Codex 官方手册整理。Codex 会持续更新，涉及价格、模型可用性、功能成熟度、企业策略和限制时，请以官方文档为准。

### 在线阅读

| 入口 | 说明 |
| --- | --- |
| [中文版教程 - 网页导航版](https://xenosxu1-bot.github.io/Codex_Help/zh-CN.html) | 推荐中文阅读入口，左侧带章节目录，方便快速跳转。 |
| [中文 Markdown 原文](docs/zh-CN.md) | 适合在 GitHub 中直接阅读、复制或二次编辑。 |
| [英文教程 - 网页导航版](https://xenosxu1-bot.github.io/Codex_Help/en-US.html) | 英文网页教程，左侧带章节目录。 |
| [英文 Markdown 原文](docs/en-US.md) | 英文 Markdown 源文档。 |

### 你可以学到什么

- Codex 是什么，适合处理哪些开发任务。
- 如何选择 Codex App、CLI、IDE Extension、Cloud、GitHub、Slack 和 Linear。
- 如何写包含目标、上下文、约束和完成标准的高质量提示词。
- 如何使用 Plan mode、Goal mode、threads、worktrees 和 review。
- 如何配置 `config.toml`、`AGENTS.md`、Skills、Plugins、MCP、Hooks、Rules、Automations 和 Subagents。

### 仓库结构

| 路径 | 作用 |
| --- | --- |
| `README.md` | 仓库首页和语言入口。 |
| `docs/zh-CN.md` | 中文完整教程 Markdown 原文。 |
| `docs/en-US.md` | 英文完整教程 Markdown 原文。 |
| `docs/zh-CN.html` | 中文网页导航版教程，左侧带章节目录。 |
| `docs/en-US.html` | 英文网页导航版教程，左侧带章节目录。 |
| `assets/images/` | Markdown 教程和 README 使用的截图资源。 |
| `docs/assets/images/` | GitHub Pages 网页版使用的截图资源。 |
| `tools/generate_pages.py` | 将 Markdown 教程生成带左侧目录的 HTML 页面。 |
| `docs/source-check.md` | 官方文档刷新和校验说明。 |

### 官方文档

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

### 许可

本仓库原创教程文本采用 MIT License。OpenAI 产品名称、商标、官方文档和截图仍受其各自权利方条款约束。
