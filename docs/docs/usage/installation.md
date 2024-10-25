---
title: Installation
---

Install `readmeai` using one of the following methods based on your preference.

## <img width="3%" src="https://simpleicons.org/icons/python.svg">&emsp13;Pip

Pip is the default Python package manager and the simplest way to install `readmeai`:

```sh
pip install readmeai
```

## <img width="3%" src="https://simpleicons.org/icons/pipx.svg">&emsp13;Pipx

To install `readmeai` in an isolated environment, use [pipx](https://pipx.pypa.io/):

```sh
pipx install readmeai
```

??? tip "Why pipx?"
	Using `pipx` allows you to install and run Python command-line applications in isolated environments, which helps prevent dependency conflicts with other Python projects.

## <img width="3%" src="https://simpleicons.org/icons/astral.svg">&emsp13;uv

For faster installations, use [uv](https://github.com/astral-sh/uv) to install `readmeai`:

```sh
uv tool install readmeai
```

??? tip "Why uv?"
    `uv` is a new-generation Python package installer, built with Rust, that offers significant speed improvements over most Python package managers such as `pip`. It's particularly useful for larger projects with many dependencies.

### Installing Optional Dependencies

The `readmeai` package integrates with multiple LLM services through optional dependencies. To use language models from **Anthropic** or **Google Gemini**, you'll need to install extra dependencies.

!!! note
    Ensure to use **quotes** around the package name when installing optional dependencies to avoid shell interpretation issues.

#### Using Anthropic

```sh
pip install "readmeai[anthropic]"
```

#### Using Google Gemini

```sh
pip install "readmeai[google-generativeai]"
```

???+ info "Install Multiple Dependencies"
    You can install multiple extra dependencies at once by combining them with commas:
    ```sh
    pip install "readmeai[anthropic,google-generativeai]"
    ```

## Verify Installation

After installing `readmeai`, verify the installation with the following command:

```sh
readmeai --version

# or

readmeai -V
```

You should see the installed version of `readmeai` displayed in the output:

```sh
readmeai version 0.5.99
```
