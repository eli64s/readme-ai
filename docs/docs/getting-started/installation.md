---
title: "Installation"
description: "Step-by-step guide for installing readme-ai using pip, pipx, Docker and other methods"
---

Install `readmeai` using any of the following package managers:

=== "<img width="12px" height="12px" src="https://simpleicons.org/icons/python.svg">&nbsp;pip"

    Install with [pip] (recommended for most users):

    ```sh
    pip install -U readmeai
    ```

    !!! note "Installation Notes"
        1. The `-U` flag ensures that `pip` upgrades the package to the latest version.
        2. The core `readmeai` package includes support for [OpenAI][openai] and [Ollama][ollama] language models. See the next section for optional dependencies.

=== "<img width="12px" height="12px" src="https://simpleicons.org/icons/pipx.svg">&nbsp;pipx"

    Install in an isolated environment with [pipx]:

    ```sh
    pipx install readmeai
    ```

    ??? tip "Why use pipx?"
        Using `pipx` allows you to install and run Python command-line applications in isolated environments, which helps prevent dependency conflicts with other Python projects.

=== "<img width="12px" height="12px" src="https://simpleicons.org/icons/uv.svg">&nbsp;uv"

    For the fastest installation use [uv]:

    ```sh
    uv tool install readmeai
    ```

    ??? tip "Why use uv?"
        `uv` is a new-generation Python package installer, built with Rust, that offers significant speed improvements over most Python package managers such as `pip`. It's particularly useful for larger projects with many dependencies.

---

### Installing Optional Dependencies

The `readmeai` package integrates with multiple LLM services through optional dependencies. To use language models offered by **Anthropic** or **Google Gemini**, install ReadmeAI's extra dependencies:

=== "<img width="12px" height="12px" src="https://simpleicons.org/icons/anthropic.svg">&nbsp;Anthropic"

    ```sh
    pip install "readmeai[anthropic]"
    ```

=== "<img width="12px" height="12px" src="https://simpleicons.org/icons/googlegemini.svg">&nbsp;Google Gemini"

    ```sh
    pip install "readmeai[google-generativeai]"
    ```

=== "Multiple Services"

    ```sh
    pip install "readmeai[anthropic,google-generativeai]"
    ```

---

## Verify Installation

After installing `readmeai`, verify the installation with the following command:

```sh
readmeai --version
```

Or use the `-V` flag:

```sh
readmeai -V
```

You should see the installed version of `readmeai` displayed in the output:

```sh
readmeai version 0.6.0
```

---

<!-- REFERENCE LINKS -->
--8<-- "references.md:links-install"
--8<-- "references.md:links-main"

<!-- LLM SERVICES -->
<!-- [anthropic]: https://docs.anthropic.com/en/home
[gemini]: https://ai.google.dev/tutorials/python_quickstart
[ollama]: https://github.com/ollama/ollama
[openai]: https://platform.openai.com/docs/quickstart/account-setup: -->

<!-- QUICK START -->
<!-- [pypi]: https://pypi.org/project/splitme-ai/
[pip]: https://pip.pypa.io/en/stable/
[pipx]: https://pipx.pypa.io/stable/
[python]: https://www.python.org/
[uv]: https://docs.astral.sh/uv/ -->
