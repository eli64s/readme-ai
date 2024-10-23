---
title: Installation
---

Install `readmeai` using one of the following methods:

## <img width="3%" src="https://simpleicons.org/icons/python.svg">&emsp13;Pip

Pip is the default Python package manager and recommended for installing `readmeai`:

```sh
pip install readmeai
```

## <img width="3%" src="https://simpleicons.org/icons/pipx.svg">&emsp13;Pipx

Alternatively, use `pipx` to install `readmeai` in an isolated environment:

```sh
pipx install readmeai
```

??? tip "Why use pipx?"
	Using `pipx` allows you to install and run Python command-line applications in isolated environments, which helps prevent dependency conflicts with other Python projects.

## Optional Dependencies

To use additional LLM providers like **Anthropic** or **Google Gemini**, install the optional dependencies:

**Anthropic**:

```sh
pip install "readmeai[anthropic]"
```

**Google Gemini**:

```sh
pip install pip install "readmeai[google-generativeai]"
```

<!-- ## <img width="3%" src="https://simpleicons.org/icons/git.svg">&emsp13;From source

You can build `readmeai` from the source code by following these steps:

<details>
  <summary>Click to expand instructions</summary>

1. **Clone the repository:**

   ```sh
   ❯ git clone https://github.com/eli64s/readme-ai
   ```

2. **Navigate to the `readme-ai` directory:**

   ```sh
   ❯ cd readme-ai
   ```

3. **Install dependencies:**

   ```sh
   ❯ pip install -r setup/requirements.txt
   ```

Alternatively, the project can be setup using the bash script below:

## <img width="3%" src="/docs/assets/icons/gnubash.svg">&emsp13;Bash

1. **Run the setup script:**

	```sh
	❯ bash setup/setup.sh
	```

Or, use `poetry` to build the project:

## <img width="3%" src="/docs/assets/icons/poetry.svg">&emsp13;Poetry

1. **Install dependencies using Poetry:**

	```sh
	❯ poetry install
	```

</details>

After installation, verify that readme-ai is correctly installed by running:
```sh
readmeai --version
``` -->

For usage instructions, see the [Usage](../usage/cli.md) section.
