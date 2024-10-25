---
title: CLI Reference
---

README-AI offers a wide range of configuration options to customize your README generation. This page provides a comprehensive list of all available options with detailed explanations.

## Options

| Option | Description | Default | Impact |
|--------|-------------|---------|--------|
| `--align` | Text alignment in header | `center` | Affects the visual layout of the README header |
| `--api` | LLM API service | `offline` | Determines which AI service is used for content generation |
| `--badge-color` | Badge color (name or hex) | `0080ff` | Customizes the color of status badges in the README |
| `--badge-style` | Badge icon style type | `flat` | Changes the visual style of status badges |
| `--base-url` | Base URL for the repository | `v1/chat/completions` | Used for API requests to the chosen LLM service |
| `--context-window` | Max context window of LLM API | `3999` | Limits the amount of context provided to the LLM |
| `--emojis` | Add emojis to README sections | `False` | Adds visual flair to section headers |
| `--header-style` | Header template style | `classic` | Changes the overall look of the README header |
| `--image` | Project logo image | `blue` | Sets the main image displayed in the README |
| `--model` | Specific LLM model to use | `gpt-3.5-turbo` | Chooses the AI model for content generation |
| `--output` | Output filename | `readme-ai.md` | Specifies the name of the generated README file |
| `--rate-limit` | Max API requests per minute | `5` | Prevents exceeding API rate limits |
| `--repository` | Repository URL or local path | `None` | Specifies the project to analyze |
| `--temperature` | Creativity level for generation | `0.9` | Controls the randomness of the AI's output |
| `--toc-style` | Table of contents style | `bullet` | Changes the format of the table of contents |
| `--top-p` | Top-p sampling probability | `0.9` | Fine-tunes the AI's output diversity |
| `--tree-depth` | Max depth of directory tree | `2` | Controls the detail level of the project structure |

Some options have a significant impact on the generated README's appearance and content. Experiment with different settings to find the best configuration for your project!

---
