# Codex Help

An unofficial, bilingual quick-start and practical guide for OpenAI Codex.

> This repository is based on the OpenAI Codex official manual refreshed on 2026-07-08. Codex changes over time, so pricing, model availability, feature maturity, and enterprise controls should always be verified against the official documentation.

## Read This Guide

- [中文教程](docs/zh-CN.md)
- [English guide](docs/en-US.md)

## What You Will Learn

- What Codex is and which tasks it is good at.
- How to choose between Codex App, CLI, IDE Extension, Cloud, GitHub, Slack, and Linear.
- How to write prompts that include goal, context, constraints, and done criteria.
- How to use Plan mode, Goal mode, threads, worktrees, and reviews.
- How sandboxing, approvals, web search, and network access work.
- How to configure `config.toml`, `AGENTS.md`, Skills, Plugins, MCP, Hooks, Rules, Automations, and Subagents.
- How to get started quickly without losing safety or reviewability.

## Fast Start

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

## Interface Screenshots

The guide includes official Codex interface screenshots under [assets/images](assets/images). They are referenced from both language versions so the repository can be read offline after cloning.

## Official Documentation

Use this repository as a learning companion, not as a replacement for official docs:

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

See also: [source check](docs/source-check.md).

## Repository Structure

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
```

## License

The original guide text in this repository is released under the MIT License. OpenAI product names, trademarks, documentation, and screenshots remain subject to their respective owners' terms.
