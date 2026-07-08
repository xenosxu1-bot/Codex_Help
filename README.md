# Codex Help / Codex 使用指南

非官方 OpenAI Codex 双语快速入门与实用教程。  
An unofficial bilingual quick-start and practical guide for OpenAI Codex.

> 中文：本仓库根据 2026-07-08 刷新的 OpenAI Codex 官方手册整理。Codex 会持续更新，涉及价格、模型可用性、功能成熟度、企业策略和限制时，请以官方文档为准。  
> English: This repository is based on the OpenAI Codex official manual refreshed on 2026-07-08. Codex changes over time, so pricing, model availability, feature maturity, enterprise controls, and limits should always be verified against the official documentation.

## 语言 / Languages

- [中文教程](docs/zh-CN.md)
- [English Guide](docs/en-US.md)

## 项目目标 / Project Goal

中文：这个项目帮助读者快速熟悉 Codex 的主要功能、使用入口、安全边界和高效工作流，适合刚开始使用 Codex 的开发者，也适合作为团队内部推广和培训材料。

English: This project helps readers quickly understand Codex's core features, available surfaces, safety boundaries, and practical workflows. It is useful for developers new to Codex and for teams introducing Codex into their development process.

## 你将学到什么 / What You Will Learn

中文：

- Codex 是什么，适合处理哪些开发任务。
- 如何在 Codex App、CLI、IDE Extension、Cloud、GitHub、Slack 和 Linear 之间选择。
- 如何写包含目标、上下文、约束和完成标准的高质量提示词。
- 如何使用 Plan mode、Goal mode、threads、worktrees 和 review。
- 沙箱、审批、网络访问和 web search 的基本安全模型。
- 如何配置 `config.toml`、`AGENTS.md`、Skills、Plugins、MCP、Hooks、Rules、Automations 和 Subagents。
- 如何让 Codex 快速上手项目，同时保持可验证、可审查、可回滚。

English:

- What Codex is and which development tasks it is good at.
- How to choose between Codex App, CLI, IDE Extension, Cloud, GitHub, Slack, and Linear.
- How to write prompts with goal, context, constraints, and done criteria.
- How to use Plan mode, Goal mode, threads, worktrees, and reviews.
- How sandboxing, approvals, network access, and web search work.
- How to configure `config.toml`, `AGENTS.md`, Skills, Plugins, MCP, Hooks, Rules, Automations, and Subagents.
- How to onboard Codex into a project while keeping work verifiable, reviewable, and reversible.

## 快速开始 / Fast Start

中文：

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

English:

1. Open your repository root in Codex App, CLI, or your IDE.
2. Ask Codex to inspect the project before editing:

   ```text
   Read this repository structure. Identify build, test, lint commands, main source folders, and project conventions. Do not edit files yet.
   ```

3. Add durable project guidance:

   ```text
   Generate an AGENTS.md for this repository. Include setup commands, tests, linting, coding conventions, review expectations, and done criteria.
   ```

4. Start with a small, verifiable task:

   ```text
   Fix this failing test without changing the public API. After the fix, run the smallest relevant test and report the command and result.
   ```

5. Review the diff before accepting changes:

   ```text
   /review
   ```

## 界面截图 / Interface Screenshots

中文：教程包含 Codex 官方界面截图，存放在 [assets/images](assets/images)。中英文文档都引用这些本地图片，因此 clone 仓库后也可以离线阅读。

English: The guide includes official Codex interface screenshots under [assets/images](assets/images). Both language versions reference these local images, so the guide can be read offline after cloning.

## 官方文档 / Official Documentation

中文：本仓库是学习辅助材料，不替代官方文档。  
English: Use this repository as a learning companion, not as a replacement for official docs.

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

来源校验 / Source check: [docs/source-check.md](docs/source-check.md)

## 仓库结构 / Repository Structure

```text
Codex_Help/
  README.md
  docs/
    zh-CN.md
    en-US.md
    source-check.md
  assets/
    images/
  LICENSE
  NOTICE.md
  CONTRIBUTING.md
```

## 结构说明 / Structure Guide

| 路径 / Path | 作用 / Purpose |
| --- | --- |
| `README.md` | 仓库首页，提供中英文项目介绍、快速开始、阅读入口和官方文档链接。 / Repository homepage with bilingual overview, fast start, reading links, and official documentation links. |
| `docs/zh-CN.md` | 中文完整教程，适合中文读者系统学习 Codex 功能、配置、安全和工作流。 / Full Chinese guide for learning Codex features, configuration, safety, and workflows. |
| `docs/en-US.md` | English full guide, aligned with the Chinese guide for English readers. / 英文完整教程，与中文教程保持同一事实口径。 |
| `docs/source-check.md` | 记录本教程对照官方 Codex 手册校验的范围和刷新时间。 / Records the official Codex manual refresh and source-check scope. |
| `assets/images/` | 存放教程引用的 Codex 界面截图，支持离线阅读。 / Stores Codex interface screenshots used by the guides for offline reading. |
| `LICENSE` | MIT License，说明本仓库原创教程文本的许可。 / MIT License for the original guide text. |
| `NOTICE.md` | 声明本仓库为非官方学习材料，并说明 OpenAI 名称、商标、官方文档和截图权利归属。 / Notes that this is an unofficial learning guide and clarifies ownership of OpenAI names, trademarks, official docs, and screenshots. |
| `CONTRIBUTING.md` | 贡献指南，说明如何基于官方文档更新内容并保持中英文一致。 / Contribution guide for official-doc-aligned updates and bilingual consistency. |
| `.gitignore` | 忽略系统文件、日志、本地环境变量和依赖目录。 / Ignores system files, logs, local environment files, and dependency folders. |

## 许可 / License

中文：本仓库原创教程文本采用 MIT License。OpenAI 产品名称、商标、官方文档和截图仍受其各自权利方条款约束。

English: The original guide text in this repository is released under the MIT License. OpenAI product names, trademarks, documentation, and screenshots remain subject to their respective owners' terms.
