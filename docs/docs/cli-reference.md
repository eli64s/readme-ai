---
title: "CLI Options"
description: "Complete reference for readme-ai's command line interface options and configurations"
search:
    boost: 2
---

# Command Line Reference

This guide provides a comprehensive reference for the readme-ai CLI, including all available options and their descriptions.

## Core Options

| Option | Short | Values | Default | Description |
|--------|-------|---------|---------|-------------|
| `--version` | `-V` | - | - | Show the version and exit |
| `--help` | - | - | - | Show help message and exit |
| `--repository` | `-r` | `TEXT` | - | Repository URL (GitHub, GitLab, BitBucket) or local path *(required)* |
| `--output` | `-o` | `TEXT` | `README.md` | Output file path for the generated README |

## LLM Configuration

| Option | Short | Values | Default | Description |
|--------|-------|---------|---------|-------------|
| `--api` | - | `anthropic`<br>`gemini`<br>`ollama`<br>`openai`<br>`offline` | `openai` | LLM API service provider |
| `--base-url` | - | `TEXT` | - | Base URL for the LLM API service |
| `--model` | `-m` | `TEXT` | *varies by provider* | LLM model to use |
| `--context-window` | `-cw` | `INTEGER` | - | Maximum tokens for model's context window |
| `--rate-limit` | `-rl` | `1-25` | - | Requests per minute for the LLM API |
| `--temperature` | `-t` | `0.0-2.0` | `0.7` | Temperature for text generation |
| `--top-p` | - | `0.0-1.0` | `1.0` | Top-p sampling probability |
| `--system-message` | `-sm` | `TEXT` | - | Custom system message for the LLM |

## Styling Options

### Layout and Alignment

| Option | Short | Values | Default | Description |
|--------|-------|---------|---------|-------------|
| `--align` | `-a` | `center`<br>`left`<br>`right` | `left` | Alignment for README header sections |
| `--header-style` | `-hs` | `ASCII`<br>`ASCII_BOX`<br>`BANNER`<br>`CLASSIC`<br>`CLEAN`<br>`COMPACT`<br>`CONSOLE`<br>`MODERN` | `CLEAN` | README header style template |
| `--navigation-style` | `-ns` | `ACCORDION`<br>`BULLET`<br>`NUMBER`<br>`ROMAN` | `BULLET` | Navigation menu style for table of contents |

### Visual Elements

| Option | Short | Values | Default | Description |
|--------|-------|---------|---------|-------------|
| `--badge-color` | `-bc` | `TEXT` | - | Primary color for badge icons (hex code or name) |
| `--badge-style` | `-bs` | `default`<br>`flat`<br>`flat-square`<br>`for-the-badge`<br>`plastic`<br>`skills`<br>`skills-light`<br>`social` | `flat` | Visual style of badge icons |
| `--logo` | `-l` | `ANIMATED`<br>`BLACK`<br>`BLUE`<br>`GRADIENT`<br>`ORANGE`<br>`METALLIC`<br>`PURPLE`<br>`RAINBOW`<br>`TERMINAL`<br>`CUSTOM`<br>`LLM` | `GRADIENT` | Project logo style |
| `--logo-size` | `-ls` | `TEXT` | - | Project logo size |

### Content Enhancement

| Option | Short | Values | Default | Description |
|--------|-------|---------|---------|-------------|
| `--emojis` | `-e` | `default`<br>`minimal`<br>`ascension`<br>`fibonacci`<br>`harmony`<br>`prism`<br>`quantum`<br>`monochrome`<br>`unicode`<br>`atomic`<br>`cosmic`<br>`crystal`<br>`earth`<br>`fire`<br>`forest`<br>`nature`<br>`water`<br>`gradient`<br>`rainbow`<br>`solar`<br>`fun`<br>`vintage`<br>`zen`<br>`random` | `default` | Emoji theme for header sections |
| `--tree-max-depth` | `-td` | `INTEGER` | `3` | Maximum depth of directory tree |

!!! tip "Using Short Options"
    Many commands have short versions (e.g., `-r` instead of `--repository`). Use these for quicker typing in the terminal.

!!! note "Default Values"
    When an option is not specified, readme-ai will use sensible defaults optimized for most use cases.

---
