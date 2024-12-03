---
title: "System Requirements"
description: "Detailed guide on system requirements, supported repository sources, and LLM API providers for README-AI"
---

This guide outlines the necessary system requirements and compatibility information for using `readmeai` effectively.

## Core Requirements

- **Python Version**: `3.9` or higher
- **Package Management/Conainter Runtime**: Choose one of the following:
    - [`pip`][pip]: Python's default package installer, recommended for most users.
    - [`pipx`][pipx]: Install and run `readmeai` in an isolated environment.
    - [`uv`][uv]: Fastest way to install `readmeai` with a single command.
    - [`docker`][docker]: Run `readmeai` in a containerized environment.

## Supported Repository Sources

The `readmeai` CLI can retrieve source code from the following Git hosting services or your local file system:

| Platform | Description | Resource |
| :------- | :---------- | :--- |
| File System | Access repositories on your machine | [Learn more][file-system] |
| GitHub | World's largest code hosting platform | [GitHub.com][github] |
| GitLab | Complete DevOps platform | [GitLab.com][gitlab] |
| Bitbucket | Atlassian's Git solution | [Bitbucket.org][bitbucket] |

!!! note
    Missing a Git provider? [open an issue][issues] or [submit a pull request][pulls] to help us expand our platform support.

## Supported LLM API Providers

To unlock the full potential of `readmeai`, you'll need an account and API key from one of the providers below:

| Provider | Description | Resource |
|----------|-------------|-------|
| OpenAI | Recommended for general use | [OpenAI Developer quickstart][openai] |
| Anthropic | Advanced language models | [Anthropic Developer docs][anthropic] |
| Google Gemini | Google's multimodal AI model | [Gemini API quickstart][gemini] |
| Ollama | Free and open-source (No API key required) | [Ollama GitHub repository][ollama] |
| Offline Mode | Run `readmeai` without a LLM API | [Example offline mode README][offline-mode] |

## Next Steps

- [Installation](installation.md): Learn how to install `readmeai`
- [CLI Reference](cli.md): Discover how to use `readmeai` effectively
- [Troubleshooting](../troubleshooting.md): Find solutions to common issues

---

<!-- LLM API developer docs -->
[openai]: https://platform.openai.com/docs/quickstart/account-setup: "OpenAI Developer quickstart"
[anthropic]: https://docs.anthropic.com/en/home "Anthropic Developer docs"
[gemini]: https://ai.google.dev/tutorials/python_quickstart "Gemini API quickstart"
[ollama]: https://github.com/ollama/ollama "Ollama GitHub repository"
[offline-mode]: https://github.com/eli64s/readme-ai/blob/main/examples/offline-mode/readme-litellm.md "Example offline mode README"

<!-- package managemers/container runtimes -->
[pip]: https://pip.pypa.io/en/stable/ "pip"
[pipx]: https://pipx.pypa.io/stable/ "pipx"
[uv]: https://docs.astral.sh/uv/ "uv"
[docker]: https://docs.docker.com/ "docker"

<!-- git hosting services -->
[file-system]: https://en.wikipedia.org/wiki/File_system "Learn more"
[github]: https://github.com/ "GitHub.com"
[gitlab]: https://gitlab.com/ "GitLab.com"
[bitbucket]: https://bitbucket.org/ "Bitbucket.org"

<!-- readme-ai links -->
[issues]: https://github.com/eli64s/readme-ai/issues "open an issue"
[pulls]: https://github.com/eli64s/readme-ai/pulls) "submit a pull request"
