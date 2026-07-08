# OpenAI Codex: Features and Practical Usage Guide

> Status: This is an unofficial guide based on the OpenAI Codex official manual refreshed on 2026-07-08. Codex evolves quickly. For pricing, model availability, feature maturity, enterprise policy, and current limits, verify the official documentation.

## Contents

- [1. What Codex Is](#1-what-codex-is)
- [2. What Codex Can Help With](#2-what-codex-can-help-with)
- [3. Choose the Right Surface](#3-choose-the-right-surface)
- [4. Interface Tour](#4-interface-tour)
- [5. First-Run Workflow](#5-first-run-workflow)
- [6. Prompting That Works](#6-prompting-that-works)
- [7. Threads, Context, Plan Mode, and Goal Mode](#7-threads-context-plan-mode-and-goal-mode)
- [8. Approvals, Sandboxing, and Security](#8-approvals-sandboxing-and-security)
- [9. Configuration](#9-configuration)
- [10. Models and Reasoning](#10-models-and-reasoning)
- [11. Codex App Tips](#11-codex-app-tips)
- [12. Codex CLI Tips](#12-codex-cli-tips)
- [13. IDE Extension Tips](#13-ide-extension-tips)
- [14. Cloud, GitHub, Slack, and Linear](#14-cloud-github-slack-and-linear)
- [15. AGENTS.md](#15-agentsmd)
- [16. Skills, Plugins, MCP, Hooks, and Rules](#16-skills-plugins-mcp-hooks-and-rules)
- [17. Automations and Subagents](#17-automations-and-subagents)
- [18. Windows Notes](#18-windows-notes)
- [19. Prompt Templates](#19-prompt-templates)
- [20. Troubleshooting](#20-troubleshooting)
- [21. Official Sources](#21-official-sources)

## 1. What Codex Is

Codex is OpenAI's coding agent for software development. It can read a codebase, edit files, run commands, inspect tool output, review diffs, debug failures, and call configured tools when needed.

Think of Codex as a development teammate that works best when the task is scoped and verifiable. Give it the goal, context, constraints, and done criteria; then ask it to implement, test, and summarize what changed.

## 2. What Codex Can Help With

Codex is useful for:

- Writing features that follow existing project patterns.
- Explaining unfamiliar or legacy codebases.
- Debugging failures from logs, stack traces, tests, or reproducible steps.
- Adding unit, integration, and regression tests.
- Reviewing local diffs or pull requests.
- Running repetitive workflows such as migrations, refactors, changelog updates, and project setup.
- Generating or reviewing non-code artifacts such as PDFs, spreadsheets, documents, and presentations in the Codex App.

Best results usually come from tasks that can be checked with a command, test, screenshot, or review step.

## 3. Choose the Right Surface

| Surface | Best for | Strengths | Notes |
| --- | --- | --- | --- |
| Codex App | Desktop work, multiple threads, visual review, worktrees, automations | Rich UI, Git tools, terminal, browser preview, artifact viewer | Also supports projectless chats |
| CLI | Terminal-first work, remote machines, scripts, CI-like workflows | Fast, composable, supports `codex exec` | Mention paths explicitly |
| IDE Extension | Editor-attached work | Open files and selected code become context | Great for short feedback loops |
| Cloud | Parallel or async hosted tasks | Offloads long work | Requires GitHub and a cloud environment |
| GitHub | Pull request review and fixes | `@codex review`, `@codex fix...` | Requires Codex cloud and review setup |
| Slack / Linear | Delegating from collaboration tools | Starts cloud tasks from existing context | Requires connectors and environments |

Quick rule:

- Coding in an editor: use the IDE Extension or Codex App.
- Working from a terminal: use CLI.
- Running long or parallel work: use Cloud or App worktrees.
- Reviewing a PR: use GitHub integration or local `/review`.
- Repeating a workflow: turn it into a Skill or Plugin.

## 4. Interface Tour

### Codex App

![Codex App review pane](../assets/images/codex-app-review-pane.webp)

Codex App is the desktop workspace for threads, diffs, reviews, Git actions, local terminals, worktrees, automations, browser preview, and artifacts.

### Codex CLI

![Codex CLI splash](../assets/images/codex-cli-splash.png)

The CLI runs Codex in the terminal. Use it interactively with `codex` or non-interactively with `codex exec`.

### IDE Extension

![Codex IDE extension](../assets/images/codex-ide-extension.webp)

The IDE Extension brings Codex into VS Code-compatible editors. It can use open files, selected code, and editor context.

### In-app Browser

![Codex in-app browser](../assets/images/codex-in-app-browser.webp)

The in-app browser previews local development servers, file-backed previews, and public pages that do not require sign-in.

### Browser Comments

![Codex browser annotations](../assets/images/codex-browser-annotations.webp)

Browser comments let you mark a page region and ask Codex to address that exact visual feedback.

### Artifact Viewer

![Codex artifact viewer](../assets/images/codex-artifact-viewer.webp)

The Codex App can preview non-code artifacts such as documents, spreadsheets, presentations, and PDFs.

### Automations

![Codex automations](../assets/images/codex-automations.webp)

Automations can run scheduled checks, reminders, monitors, or recurring follow-up tasks.

### Floating Pop-out

![Codex floating pop-out](../assets/images/codex-popout-window.webp)

The floating pop-out keeps an active thread visible next to your browser, editor, or preview window.

### Browser Developer Mode

![Codex browser developer mode](../assets/images/codex-browser-developer-mode.webp)

Browser Developer Mode can enable deeper Chrome DevTools Protocol access for profiling and debugging, subject to workspace policy.

## 5. First-Run Workflow

1. Start at the repository root:

   ```bash
   codex
   ```

2. Ask Codex to inspect the project before editing:

   ```text
   Read this repository structure. Identify the build, test, lint commands, main source folders, and project conventions. Do not edit files yet.
   ```

3. Create or improve `AGENTS.md`:

   ```text
   Generate an AGENTS.md for this repository. Include setup commands, tests, linting, coding conventions, review expectations, and done criteria.
   ```

4. Start with a small, verifiable task:

   ```text
   Fix this failing test without changing the public API. After the fix, run the smallest relevant test and report the command and result.
   ```

5. Review the diff:

   ```text
   /review
   ```

## 6. Prompting That Works

A strong Codex prompt usually includes four things:

- Goal: what should change or be built.
- Context: files, folders, logs, screenshots, examples, or errors.
- Constraints: APIs, architecture, security rules, compatibility, dependency limits, or style.
- Done criteria: tests pass, bug no longer reproduces, screenshot matches, or behavior is verified.

Template:

```text
Goal:
<What you want changed>

Context:
- Files: @src/foo.ts @src/foo.test.ts
- Current behavior: ...
- Related example: ...

Constraints:
- Do not change the public API
- Reuse existing helpers
- Do not add dependencies unless you explain why first

Done when:
- Add or update tests
- Run <specific command>
- Summarize changes and verification
```

For complex work, start with Plan mode:

```text
/plan Investigate the authentication flow and propose a migration plan. Do not edit files yet.
```

When the requirement is fuzzy, ask Codex to interview you first:

```text
I have a vague idea for improving dashboard performance. Ask me the key questions needed to define scope, metrics, and acceptance criteria before writing code.
```

## 7. Threads, Context, Plan Mode, and Goal Mode

A thread is one continuous Codex session: prompts, model output, file reads, edits, commands, approvals, and follow-ups. Keep related work in one thread, but avoid running two threads that edit the same files at the same time.

Local threads run on your machine. Cloud threads run in isolated cloud environments and are useful for async or parallel work.

Codex manages a model context window. Long tasks may be compacted automatically, and you can use `/compact` to summarize old context.

Use Plan mode when the task is ambiguous or high risk:

```text
/plan Propose the implementation steps and verification strategy. Do not modify files yet.
```

Use Goal mode for longer work:

```text
/goal Migrate this project to TypeScript. The app should compile in strict mode without explicit any types.
```

Good goals are specific and measurable.

## 8. Approvals, Sandboxing, and Security

Codex safety is controlled by two layers:

- Sandbox mode: what Codex can technically access or modify.
- Approval policy: when Codex must pause and ask.

Common sandbox modes:

| Mode | Behavior | Use case |
| --- | --- | --- |
| `read-only` | Inspect files without automatic edits | Research and review |
| `workspace-write` | Read and edit inside the workspace | Default local development |
| `danger-full-access` | No sandbox boundary | Only in externally isolated trusted environments |

Common approval policies:

| Policy | Behavior | Use case |
| --- | --- | --- |
| `untrusted` | Ask before commands outside the trusted set | More cautious runs |
| `on-request` | Work inside sandbox, ask when crossing boundaries | Interactive development |
| `never` | Do not ask for approvals | Non-interactive automation with safe constraints |

Recommended local default:

```bash
codex --sandbox workspace-write --ask-for-approval on-request
```

Read-only investigation:

```bash
codex --sandbox read-only --ask-for-approval on-request
```

Network access for commands is normally separate from web search. Enable command network access only when needed:

```toml
[sandbox_workspace_write]
network_access = true
```

## 9. Configuration

User configuration lives at:

```text
~/.codex/config.toml
```

Project configuration can live at:

```text
.codex/config.toml
```

Project config loads only for trusted projects. Precedence is:

1. CLI flags and `--config`.
2. Project `.codex/config.toml`, closest wins.
3. Selected profile file.
4. User `~/.codex/config.toml`.
5. System config.
6. Built-in defaults.

Common settings:

```toml
model = "gpt-5.5"
model_reasoning_effort = "high"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "cached"

[sandbox_workspace_write]
network_access = false

[features]
multi_agent = true
hooks = true
fast_mode = true
```

One-off overrides:

```bash
codex --model gpt-5.5
codex -c model='"gpt-5.5"'
codex -c sandbox_workspace_write.network_access=true
```

## 10. Models and Reasoning

According to the refreshed official manual, start with `gpt-5.5` for most Codex tasks. Use `gpt-5.4-mini` for faster, lighter tasks or subagents. `gpt-5.3-codex-spark` is a research preview model for ChatGPT Pro subscribers optimized for near-instant coding iteration.

General guidance:

| Task | Suggested setup |
| --- | --- |
| Complex debugging or migration | `gpt-5.5` with high or xhigh reasoning |
| Normal implementation and tests | `gpt-5.5` with medium or high reasoning |
| Fast exploration or supporting subagents | `gpt-5.4-mini` |
| Near-real-time text iteration | `gpt-5.3-codex-spark`, if available |

Fast mode can increase speed at higher credit consumption:

```text
/fast on
/fast off
/fast status
```

## 11. Codex App Tips

Use Codex App when you want visual workflows:

- Local threads edit the current project.
- Worktree threads isolate changes in a Git worktree.
- Cloud threads run remotely.
- The diff pane supports review, comments, staging, reverting, committing, pushing, and pull request creation.
- The integrated terminal lets you run tests and development servers.
- The in-app browser previews local pages and supports browser comments.
- Computer Use can operate desktop apps with approval boundaries.

For front-end work, keep a floating Codex thread next to the browser or preview window and iterate with visual feedback.

## 12. Codex CLI Tips

Start interactive mode:

```bash
codex
codex "Explain this codebase to me"
```

Resume work:

```bash
codex resume
codex resume --last
codex resume --all
codex resume <SESSION_ID>
```

Run a one-shot task:

```bash
codex exec "fix the CI failure"
```

Attach images:

```bash
codex -i screenshot.png "Explain this error"
codex --image img1.png,img2.jpg "Summarize these diagrams"
```

Useful slash commands:

| Command | Purpose |
| --- | --- |
| `/permissions` | Change permission mode |
| `/model` | Change model and reasoning |
| `/plan` | Plan before editing |
| `/goal` | Set or manage a long-running goal |
| `/review` | Review the current diff |
| `/diff` | Show Git diff |
| `/mention` | Attach files or folders |
| `/mcp` | List MCP tools |
| `/skills` | Use a skill |
| `/compact` | Summarize context |
| `/status` | Inspect session state |

## 13. IDE Extension Tips

The IDE Extension works well when your editor context matters. It can use open files, selected ranges, and `@file` references.

Example:

```text
Use @example.tsx as a reference to add a new page named Resources.
```

If Codex seems to miss the current file, check IDE context or explicitly mention the file.

## 14. Cloud, GitHub, Slack, and Linear

Codex Cloud is useful for long-running or parallel tasks. It requires a configured cloud environment and a GitHub repository.

CLI:

```bash
codex cloud
codex cloud exec --env ENV_ID "Summarize open bugs"
```

GitHub PR review:

```md
@codex review
```

Ask Codex to fix a finding:

```md
@codex fix the P1 issue
```

Slack and Linear can start cloud tasks from comments or threads when their connectors are configured.

## 15. AGENTS.md

`AGENTS.md` is durable guidance for Codex. Use it for repository-specific commands, conventions, review expectations, and verification steps.

Good contents:

- Repository layout.
- Install, build, test, lint commands.
- Coding style.
- Pull request expectations.
- Security constraints.
- Done criteria.

Example:

```md
# AGENTS.md

## Repository expectations

- Use pnpm, not npm.
- Run `pnpm typecheck` after TypeScript changes.
- Do not change public APIs unless explicitly requested.
- Explain before adding production dependencies.

## Review guidelines

- Prioritize correctness, security, regressions, and missing tests.
- Do not raise style-only comments as high-priority findings.
```

When Codex repeats the same mistake, ask for a retrospective and update `AGENTS.md`.

## 16. Skills, Plugins, MCP, Hooks, and Rules

Skills package reusable task workflows:

```text
$skill-creator
```

Use Skills for repeated workflows such as document generation, security scanning, framework migrations, or release checks.

Plugins are installable bundles that can include skills, MCP configuration, hooks, app mappings, and assets:

```text
$plugin-creator
```

MCP connects Codex to external tools and private context:

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
```

HTTP MCP server:

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
```

Hooks run lifecycle checks around tool use. Rules can allow, prompt, or forbid command prefixes outside the sandbox. Use them for repeatable safety and team policy.

## 17. Automations and Subagents

Automations are scheduled checks, reminders, monitors, or recurring follow-ups. Use thread automations when future runs depend on the same conversation context.

Subagents help parallelize read-heavy work:

```text
Review this branch with parallel subagents. Spawn one agent for security risks, one for correctness regressions, and one for test gaps. Wait for all three, then summarize findings with file references.
```

Subagents use more tokens. They are best for exploration, triage, review, and summarization. Be careful with parallel write-heavy workflows.

## 18. Windows Notes

Codex supports Windows through the native Codex App, CLI, IDE Extension, and WSL2.

Recommended native Windows sandbox:

```toml
[windows]
sandbox = "elevated"
```

Fallback:

```toml
[windows]
sandbox = "unelevated"
```

Use WSL2 when your toolchain is Linux-native. Keep repositories under the WSL home directory for better performance:

```bash
mkdir -p ~/code
cd ~/code
```

If the Windows sandbox cannot read a directory:

```text
/sandbox-add-read-dir C:\absolute\directory\path
```

## 19. Prompt Templates

Feature work:

```text
Goal:
Implement <feature>.

Context:
- Entry files: @...
- Similar implementation: @...
- Requirements: ...

Constraints:
- Reuse existing components and helpers
- Do not change public APIs
- Do not add dependencies unless you explain why first

Done when:
- Add or update tests
- Run <command>
- Summarize changes and verification
```

Debugging:

````text
Problem:
<behavior>

Reproduction:
1. ...
2. ...

Error/log:
```text
<paste error>
```

Constraints:
- ...

Find the root cause first, then make the smallest safe fix and rerun the relevant check.
````

Review:

```text
Review the current diff. Prioritize correctness, security, regressions, and missing tests. Report findings by severity with file and line references. If there are no issues, say that clearly and list any remaining test gaps.
```

## 20. Troubleshooting

Codex missed the right files:

- Start from the repository root.
- Mention files with `@` or `/mention`.
- Check IDE context.
- Confirm the App project points at the right folder.

Codex is going in the wrong direction:

- Ask it to restate the goal and constraints.
- Switch to `/plan`.
- Give examples of what to follow.
- Narrow the task.

Commands fail:

- Check sandbox mode.
- Check network access.
- Check working directory.
- Check missing dependencies.
- Check approval policy.

MCP tools are unavailable:

- Verify `config.toml`.
- Confirm OAuth login.
- Check environment variables and shell environment policy.
- Confirm `enabled_tools` / `disabled_tools`.
- Restart Codex after config changes.

## 21. Official Sources

- [Codex overview](https://developers.openai.com/codex/overview)
- [Codex prompting](https://developers.openai.com/codex/prompting)
- [Codex workflows](https://developers.openai.com/codex/workflows)
- [Best practices](https://developers.openai.com/codex/learn/best-practices)
- [Agent approvals and security](https://developers.openai.com/codex/agent-approvals-security)
- [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing)
- [Config basics](https://developers.openai.com/codex/config-basic)
- [Advanced configuration](https://developers.openai.com/codex/config-advanced)
- [Codex models](https://developers.openai.com/codex/models)
- [Codex CLI](https://developers.openai.com/codex/cli)
- [CLI slash commands](https://developers.openai.com/codex/cli/slash-commands)
- [Codex App](https://developers.openai.com/codex/app)
- [Codex app features](https://developers.openai.com/codex/app/features)
- [Codex IDE extension](https://developers.openai.com/codex/ide)
- [AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md)
- [Agent Skills](https://developers.openai.com/codex/skills)
- [Plugins](https://developers.openai.com/codex/plugins)
- [Build plugins](https://developers.openai.com/codex/plugins/build)
- [Model Context Protocol](https://developers.openai.com/codex/mcp)
- [Rules](https://developers.openai.com/codex/rules)
- [Hooks](https://developers.openai.com/codex/hooks)
- [Subagents](https://developers.openai.com/codex/subagents)
- [Windows](https://developers.openai.com/codex/windows)
