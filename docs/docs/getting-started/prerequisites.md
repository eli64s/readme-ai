---
title: System Requirements
description: "Guide to system requirements, supported platforms, and LLM providers for readme-ai"
search:
    boost: 2
---

This guide covers everything you need to know about setting up and using readme-ai, including system requirements, supported platforms, and LLM providers.

## Prerequisites

ReadmeAI requires Python 3.9 or higher, and one of the following installation methods:

| Requirement                          | Details                          |
|--------------------------------------|----------------------------------|
| • [Python][python-link] ≥3.9         | Core runtime                     |
| **Installation Method** (choose one) |                                  |
| • [pip][pip-link]                    | Default Python package manager   |
| • [pipx][pipx-link]                  | Isolated environment installer   |
| • [uv][uv-link]                      | High-performance package manager |
| • [docker][docker-link]              | Containerized environment        |

## Supported Repository Platforms

To generate a README file, provide the source repository. ReadmeAI supports these platforms:

| Platform                   | Details                   |
|----------------------------|---------------------------|
| [File System][file-system] | Local repository access   |
| [GitHub][github]           | Industry-standard hosting |
| [GitLab][gitlab]           | Full DevOps integration   |
| [Bitbucket][bitbucket]     | Atlassian ecosystem       |

## Supported LLM Providers

ReadmeAI is model agnostic, with support for the following LLM API services:

| Provider                     | Best For        | Details                  |
|------------------------------|-----------------|--------------------------|
| [OpenAI][openai]             | General use     | Industry-leading models  |
| [Anthropic][anthropic]       | Advanced tasks  | Claude language models   |
| [Google Gemini][gemini]      | Multimodal AI   | Latest Google technology |
| [Ollama][ollama]             | Open source     | No API key needed        |
| [Offline Mode][offline-mode] | Local operation | No internet required     |

## Next Steps

1. Follow our [Installation Guide](installation.md) to set up readme-ai
2. Learn the basics in our [CLI Reference](./usage/cli.md) guide
3. Get help with common issues in our [Troubleshooting](../community/troubleshooting.mdhooting.md) guide

---

<!-- REFERENCE LINKS -->
[docker-link]: https://hub.docker.com/r/zeroxeli/readme-ai
[python-link]: https://www.python.org/
[pip-link]: https://pip.pypa.io/en/stable/
[pypi-link]: https://pypi.org/project/readmeai/
[pipx-link]: https://pipx.pypa.io/stable/
[uv-link]: https://docs.astral.sh/uv/

<!-- GIT HOST PROVIDERS -->
[file-system]: https://en.wikipedia.org/wiki/File_system
[github]: https://github.com/
[gitlab]: https://gitlab.com/
[bitbucket]: https://bitbucket.org/

<!-- LLM API PROVIDERS -->
[anthropic]: https://docs.anthropic.com/en/home
[gemini]: https://ai.google.dev/tutorials/python_quickstart
[ollama]: https://github.com/ollama/ollama
[openai]: https://platform.openai.com/docs/quickstart/account-setup:
[offline-mode]: https://github.com/eli64s/readme-ai/blob/main/examples/offline-mode/readme-litellm.md

<!-- README-AI LINKS -->
[issues]: https://github.com/eli64s/readme-ai/issues "open an issue"
[pulls]: https://github.com/eli64s/readme-ai/pulls) "submit a pull request"

---

<!-- HOW TO USE SNIPPETS -->

<!-- # System Requirements

This guide covers everything you need to know about setting up and using readme-ai, including system requirements, supported platforms, and LLM providers.

## Prerequisites

ReadmeAI requires Python 3.9 or higher, plus one installation method of your choice:

--8<-- "requirements.md:core"

## Supported Repository Platforms

ReadmeAI needs access to your repository to generate a README file. Current supported platforms include:

--8<-- "requirements.md:platforms"

## Supported LLM Providers

Choose from several Language Model providers to power the readme-ai backend:

--8<-- "requirements.md:providers"

<!-- Reference Links -->

<!-- --8<-- "references.md:links-main" -->
