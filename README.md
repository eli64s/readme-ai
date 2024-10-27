<p align="center">
  <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/svg/readme-ai-cosmic.svg" alt="readme-ai-banner-logo" width="100%">
</p>

<p align="center">
  <em>Designed for simplicity, customization, and developer productivity.</em>
</p>

<p align="center">
  <a href="https://github.com/eli64s/readme-ai/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/eli64s/readme-ai/release-pipeline.yml?logo=githubactions&label=CICD&logoColor=white&color=4169E1" alt="github-actions">
  </a>
  <a href="https://app.codecov.io/gh/eli64s/readme-ai">
    <img src="https://img.shields.io/codecov/c/github/eli64s/readme-ai?logo=codecov&logoColor=white&label=Coverage&color=5D4ED3" alt="codecov">
  </a>
  <a href="https://pypi.python.org/pypi/readmeai/">
    <img src="https://img.shields.io/pypi/v/readmeai?logo=Python&logoColor=white&label=PyPI&color=7934C5" alt="pypi-version">
  </a>
  <a href="https://www.pepy.tech/projects/readmeai">
    <img src="https://img.shields.io/pepy/dt/readmeai?logo=PyPI&logoColor=white&label=Downloads&color=9400D3" alt="pepy-total-downloads">
  </a>
  <a href="https://opensource.org/license/mit/">
    <img src="https://img.shields.io/github/license/eli64s/readme-ai?logo=opensourceinitiative&logoColor=white&label=License&color=8A2BE2" alt="license">
  </a>
</p>

---

## 🔗 Quick Links

1. [Overview](#-overview)
2. [Demo](#-demo)
3. [Features](#️-features)
4. [Getting Started](#-getting-started)
5. [Configuration](#-configuration)
6. [Examples](#-examples)
7. [Contributing](#-contributing)

> [!IMPORTANT]
> ✨ Visit the [Official Documentation][mkdocs] for detailed guides and tutorials.

---

## 🔮 Overview

README-AI is a developer tool that automatically generates README markdown files using a robust repository processing engine and advanced language models. Simply provide a URL or path to your codebase, and a well-structured and detailed README will be generated.

**Why README-AI?**

This tool is designed to streamline the documentation process for developers, saving time and effort while ensuring high-quality README files. Key benefits include:

- **AI-Powered:** Leverage language models for intelligent content generation.
- **Consistency:** Ensure clean, standardized documentation across projects.
- **Customization:** Tailor the output to fit your project's requirements.
- **Language Agnostic:** Works with most programming languages/frameworks.
- **Save Time:** Generate comprehensive READMEs in less than a minute.

---

## 👾 Demo

**Running from the command line:**

[readmeai-cli-demo](https://github.com/eli64s/artifacts/assets/43382407/55b8d1b9-06a7-4b1f-b6a7-aaeccdb27679)

**Running directly in your browser:**

[readmeai-streamlit-demo](https://github.com/eli64s/artifacts/assets/43382407/3eb39fcf-c1df-49c6-bb5c-63e141857ae3)

---

## ☄️ Features

- **🚀 Automated Documentation:** Generate comprehensive README files automatically from your codebase.
- **🎨 Customizable Output:** Tailor the styling, formatting, badges, header designs, and more preferences.
- **🌐 Language Agnostic:** Compatible with a wide range of programming languages and project types.
- **🤖 Multi-LLM Support:** Current support for `OpenAI`, `Ollama`, `Anthropic`, `Google Gemini`.
- **📑 Offline Mode:** Create boilerplate README files offline, without any external API calls.
- **📝 Best Practices:** Ensures clean, professional documentation, adhering to markdown best practices.

Let's take a look at some possible customizations created by readme-ai:

<table>
  <!-- ROW -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/custom-dragon.png" alt="custom-dragon-project-logo" width="700">
      <br>
      <code>--image custom --badge-color FF4B4B --badge-style flat-square --header-style classic</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/toc/roman-numeral.png" alt="docker-go-readme-example" width="700">
      <br>
      <code>--badge-color 00ADD8 --badge-style for-the-badge --header-style modern --toc-style roman</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td colspan="2" align="center"><br>
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/ascii-art.png" alt="ascii-readme-header-style" width="700">
      <br>
      <code>--header-style ascii</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td colspan="2" align="center"><br>
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/svg-banner.png" alt="svg-" width="700">
      <br>
      <code>--badge-style for-the-badge --header-style svg</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/docs/assets/img/headers/cloud.png" alt="readme-header-with-cloud-logo" width="350">
      <br>
      <code>--align left --badge-style flat-square --image cloud</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/docs/assets/img/headers/gradient.png" alt="readme-header-with-gradient-markdown-logo" width="350">
      <br>
      <code>--align left --badge-style flat --image gradient</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/custom-balloon.png" alt="custom-balloon-project-logo" width="350">
      <br>
      <code>--badge-style flat --image custom</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/skill-icons-light.png" alt="readme-header-with-skill-icons-light" width="350">
      <br>
      <code>--badge-style skills-light --image grey</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/blue.png" alt="readme-header-with-blue-markdown-logo" width="350">
      <br>
      <code>--badge-style flat-square</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/black.png" alt="readme-header-with-black-readme-logo" width="350">
      <br>
      <code>--badge-style flat --image black</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td colspan="2" align="center"><br>
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/compact.png" alt="compact-readme-header" width="700">
      <br>
      <code>--image cloud --header-style compact --toc-style fold</code>
    </td>
  </tr>
  <!-- ROW -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/docs/assets/img/headers/modern-flat-square.png" alt="readme-header-style-modern" width="700">
      <br>
      <code>-i custom -bc BA0098 -bs flat-square -hs modern -ts fold</code>
    </td>
  </tr>
</table>

> [!IMPORTANT]
> See the [Official Documentation][mkdocs] for more information on customization options and best practices.

Next, let's explore the key sections of a typical README generated by readme-ai.

<details closed>
  <summary><strong>📍 Overview</strong></summary><br>
  <table>
    <tr>
      <td>
      <b>Overview</b><br>
        <p>◎ High-level introduction of the project, focused on the value proposition and use-cases, rather than technical aspects.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/llm-content/overview.png" alt="readme-overview-section" width="700">
      </td>
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>✨ Features</strong></summary><br>
  <table>
    <tr>
      <td><b>Features Table</b><br>
        <p>◎ Generated markdown table that highlights the key technical features and components of the codebase. This table is generated using a structured <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/prompts.toml">prompt template.</a>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/llm-content/features-table.png" alt="readme-features-section" width="700">
      </td>
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>📃 Codebase Documentation</strong></summary><br>
  <table>
    <tr>
      <td><b>Directory Tree</b><br>
        <p>◎ The project's directory structure is generated using pure Python and embedded in the README. See <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/tree.py">readmeai.generators.tree.</a> for more details.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/project-structure/tree.png" alt="directory-tree" width="700">
      </td>
    </tr>
    <tr>
      <td style="padding-top:20px;">
        <b>File Summaries</b><br>
        <p>◎ Summarizes key modules of the project, which are also used as context for downstream <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/prompts.toml">prompts.</a>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/project-structure/file-summaries.png" alt="file-summaries" width="700">
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>🚀 Quickstart Instructions</strong></summary>
  <br>
  <table>
    <tr>
      <td><b>Getting Started Guides</b><br>
        <p>◎ Prerequisites and system requirements are extracted from the codebase during preprocessing. The <a href="https://github.com/eli64s/readme-ai/tree/main/readmeai/parsers">parsers</a> handles the majority of this logic currently.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/getting-started/prerequisites-and-installation.png" alt="getting-started-section-prerequisites" width="700">
      </td>
    </tr>
    <tr>
      <td><b>Installation Guide</b><br>
        <p>◎ <code>Installation</code>, <code>Usage</code>, and <code>Testing</code> guides are generated based on the project's dependency files and codebase configuration.
        </p>
        <tr>
        <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/getting-started/usage-and-testing.png" alt="getting-started-section-usage-and-testing" width="700">
      </td>
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>🔰 Contributing Guidelines</strong></summary>
  <br>
  <table>
    <tr>
      <td><b>Contributing Guide</b><br>
        <p>◎ Dropdown section that outlines general process for contributing to your project.</p>
        <p>◎ Provides links to your contributing guidelines, issues page, and more resources.</p>
        <p>◎ Graph of contributors is also included.</p>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/contributing/contributing-guidelines.png" alt="contributing-guidelines-section" width="700">
      </td>
    </tr>
    <tr>
      <td><b>Additional Sections</b><br>
        <p>◎ <code>Project Roadmap</code>, <code>Contributing Guidelines</code>, <code>License</code>, and <code>Acknowledgements</code> are included by default.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/contributing/footer.png" alt="footer-readme-section" width="700"></td>
    </tr>
  </table>
</details>

---

## 🛸 Getting Started

### System Requirements

- **Python**: `3.9+`
- **Package Manager/Container**: `pip`, `pipx`, `uv`, or `docker`.

### Supported Sources

The following git hosting services are supported for source code retrieval, along with your local file system:

- [**GitHub**](https://github.com/)
- [**GitLab**](https://gitlab.com/)
- [**Bitbucket**](https://bitbucket.org/)
- [**File System**](https://en.wikipedia.org/wiki/File_system)

### Supported LLM APIs

To enable the full functionality of `readmeai`, an account and API key are required for one of the following providers:

- [**OpenAI**](https://platform.openai.com/docs/quickstart/account-setup): Recommended for general use. Requires an OpenAI account and API key.
- [**Ollama**](https://github.com/ollama/ollama): Free and open-source. No API key required.
- [**Anthropic**](https://www.anthropic.com/): Requires an Anthropic account and API key.
- [**Google Gemini**](https://ai.google.dev/tutorials/python_quickstart): Requires a Google Cloud account and API key.
- [**Offline Mode**](https://github.com/eli64s/readme-ai/blob/main/examples/offline-mode/readme-litellm.md): Generates a README without making API calls.

<sub>For more information on setting up an API key, refer to the provider's documentation.</sub>

## ⚙️ Installation

Choose your preferred installation method:

<!--
#### Using `pip`
[![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/readmeai/)
-->

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/python.svg">&emsp13;Pip

```sh
❯ pip install readmeai
```

<!--
#### Using `pipx`
[![pipx](https://img.shields.io/badge/pipx-2CFFAA.svg?style=flat&logo=pipx&logoColor=black)](https://pipxproject.github.io/pipx/installation/)
-->

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/pipx.svg">&emsp13;Pipx

```sh
❯ pipx install readmeai
```

> [!TIP]
> <sub>Using [pipx](https://pipx.pypa.io/stable/installation/) allows you to install and run Python command-line applications in isolated environments, which helps prevent dependency conflicts with other Python projects.</sub>

<!--
#### Using `docker`
[![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://hub.docker.com/r/zeroxeli/readme-ai)
 -->

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/3052baaca03db99d00808acfec43a44e81ecbf7f/docs/docs/assets/svg/docker.svg">&emsp13;Docker

Pull the latest Docker image from the Docker Hub repository.

```sh
❯ docker pull zeroxeli/readme-ai:latest
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/git.svg">&emsp13;From source

<details><summary>Click to expand instructions</summary>

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

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/gnubash.svg">&emsp13;Bash

1. **Run the setup script:**

	```sh
	❯ bash setup/setup.sh
	```

Or, use `poetry` to build the project:

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/poetry.svg">&emsp13;Poetry

1. **Install dependencies using Poetry:**

	```sh
	❯ poetry install
	```

</details><br>

> [!IMPORTANT]
> To use the **Anthropic** and **Google Gemini** clients, additional dependencies are required. See the following installation commands:
> - **Anthropic:**
>   ```sh
>   ❯ pip install "readmeai[anthropic]"
>   ```
> - **Google Gemini:**
>   ```sh
>   ❯ pip install "readmeai[google-generativeai]"
>   ```

## 🤖 Running the CLI

**1. Set Up Environment Variables**

With OpenAI:

```sh
❯ export OPENAI_API_KEY=<your_api_key>

# Or for Windows users:

❯ set OPENAI_API_KEY=<your_api_key>
```

<details closed><summary>Additional Providers (Ollama, Anthropic, Google Gemini)</summary><br>

<details closed><summary>Ollama</summary><br>

Refer to the [Ollama documentation](https://github.com/ollama/ollama) for more information on setting up the Ollama API. Here is a basic example:

1. Pull your model of choice from the Ollama repository:

	```sh
	❯ ollama pull mistral:latest
	```

2. Start the Ollama server and set the `OLLAMA_HOST` environment variable:

	```sh
	❯ export OLLAMA_HOST=127.0.0.1 && ollama serve
	```

</details>

<details closed><summary>Anthropic</summary>

1. Export your Anthropic API key:

	```sh
	❯ export ANTHROPIC_API_KEY=<your_api_key>
	```

</details>

<details closed><summary>Google Gemini</summary>

1. Export your Google Gemini API key:

	```sh
	❯ export GOOGLE_API_KEY=<your_api_key
	```

</details>

</details>

**2. Generate a README**

Run the following command, replacing the repository URL with your own:

```sh
❯ readmeai --repository https://github.com/eli64s/readme-ai --api openai
```

> [!IMPORTANT]
> By default, the `gpt-3.5-turbo` model is used. Higher costs may be incurred when more advanced models.
>

Run with `Ollama` and set `llama3` as the model:

```sh
❯ readmeai --api ollama --model llama3 --repository https://github.com/eli64s/readme-ai
```

Run with `Anthropic`:

```sh
❯ readmeai --api anthropic -m claude-3-5-sonnet-20240620 -r https://github.com/eli64s/readme-ai
```
Run with `Google Gemini`:

```sh
❯ readmeai --api gemini -m gemini-1.5-flash -r https://github.com/eli64s/readme-ai
```

Use a `local` directory path:

```sh
readmeai --repository /path/to/your/project
```

Add more customization options:

```sh
❯ readmeai --repository https://github.com/eli64s/readme-ai \
           --output readmeai.md \
           --api openai \
           --model gpt-4 \
           --badge-color A931EC \
           --badge-style flat-square \
           --header-style compact \
           --toc-style fold \
           --temperature 0.9 \
           --tree-depth 2
           --image LLM \
           --emojis
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/3052baaca03db99d00808acfec43a44e81ecbf7f/docs/docs/assets/svg/docker.svg">&emsp13;Docker

Run the Docker container with the OpenAI client:

```sh
❯ docker run -it --rm \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    -v "$(pwd)":/app zeroxeli/readme-ai:latest \
    --repository https://github.com/eli64s/readme-ai \
    --api openai
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/git.svg">&emsp13;From source

<details closed><summary><i>Click to expand instructions</i></summary>

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/gnubash.svg">&emsp13;Bash

If you installed the project from source with the bash script, run the following command:

1. **Activate the virtual environment:**

   ```sh
   ❯ conda activate readmeai
   ```

2. **Run the CLI:**

   ```sh
   ❯ python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
	```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/poetry.svg">&emsp13;Poetry

1. **Activate the virtual environment:**

   ```sh
   ❯ poetry shell
   ```

2. **Run the CLI:**

   ```sh
   ❯ poetry run python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
   ```

</details>

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/streamlit.svg">&emsp13;Streamlit

Try readme-ai directly in your browser, no installation required. See the <a href="https://github.com/eli64s/readme-ai-streamlit">readme-ai-streamlit</a> repository for more details.

[<img align="center" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" width="20%">](https://readme-ai.streamlit.app/)

---

## 🧪 Testing

<!--
#### Using `pytest`
[![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white)](https://docs.pytest.org/en/7.1.x/contents.html)
-->

The [pytest](https://docs.pytest.org/en/7.2.x/contents.html) and [nox](https://nox.thea.codes/en/stable/) frameworks are used for development and testing.

Install the dependencies using Poetry:

```sh
❯ poetry install --with dev,test
```

Run the unit test suite using Pytest:

```sh
❯ make test
```

Run the test suite against Python 3.9, 3.10, 3.11, and 3.12 using Nox:

```sh
❯ make test-nox
```

> [!TIP]
> <sub>Nox is an automation tool that automates testing in multiple Python environments. It is used to ensure compatibility across different Python versions.</sub>

---

## 🔡 Configuration

Customize your README generation using these CLI options:

| Option            | Description                                   | Default           |
|-------------------|-----------------------------------------------|-------------------|
| `--align`         | Text alignment in header                      | `center`          |
| `--api`           | LLM API service provider                      | `offline`         |
| `--badge-color`   | Badge color name or hex code                  | `0080ff`          |
| `--badge-style`   | Badge icon style type                         | `flat`            |
| `--header-style`  | Header template style                         | `classic`         |
| `--toc-style` 	| Table of contents style 				        | `bullet` 			|
| `--emojis`        | Adds emojis to the README header sections     | `False`           |
| `--image`         | Project logo image                            | `blue`            |
| `--model`         | Specific LLM model to use                     | `gpt-3.5-turbo`   |
| `--output`        | Output filename                               | `readme-ai.md`    |
| `--repository`    | Repository URL or local directory path        | `None`            |
| `--temperature`   | Creativity level for content generation       | `0.1`             |
| `--tree-depth`    | Maximum depth of the directory tree structure | `2`               |

Run the following command to view all available options:

```sh
❯ readmeai --help
```

<sub>Visit the [Official Documentation][mkdocs] for more detailed information on configuration options, examples, and best practices.</sub>

---

## 🎨 Examples

View example README files generated by readme-ai across various tech stacks:

| Technology | Example Output | Repository | Description |
|------------|---------------|------------|-------------|
| Readme-ai | [readme-ai.md][default] | [readme-ai][readme-ai] | Readme-ai project |
| Apache Flink | [readme-pyflink.md][modern-header] | [pyflink-poc][pyflink] | Pyflink project |
| Streamlit | [readme-streamlit.md][svg-banner] | [readme-ai-streamlit][streamlit] | Streamlit web app |
| Vercel & NPM | [readme-vercel.md][dalle-logo] | [github-readme-quotes][vercel] | Vercel deployment |
| Go & Docker | [readme-docker-go.md][for-the-badge] | [docker-gs-ping][docker-golang] | Dockerized Go app |
| FastAPI & Redis | [readme-fastapi-redis.md][fastapi-redis] | [async-ml-inference][fastapi] | Async ML inference service |
| Java | [readme-java.md][compact-header] | [Minimal-Todo][java] | Minimalist todo Java app |
| PostgreSQL & DuckDB | [readme-postgres.md][classic-header] | [Buenavista][postgres] | Postgres proxy server |
| Kotlin | [readme-kotlin.md][readme-kotlin] | [android-client][kotlin] | Android client app |
| Offline Mode | [offline-mode.md][offline-mode] | [litellm][litellm] | LLM API service |

<sub>Find additional README examples in the [examples directory](https://github.com/eli64s/readme-ai/tree/main/examples).</sub>

---

## 🏎💨 Roadmap

* [ ] Release `readmeai 1.0.0` with enhanced documentation management features.
* [ ] Develop `Vscode Extension` to generate README files directly in the editor.
* [ ] Develop `GitHub Actions` to automate documentation updates.
* [ ] Add `badge packs` to provide additional badge styles and options.
  + [ ] Code coverage, CI/CD status, project version, and more.

---

## 🔰 Contributing

Contributions are welcome! Please read the [Contributing Guide][contributing] to get started.

- **💡 [Contributing Guide][contributing]**: Learn about our contribution process and coding standards.
- **🐛 [Report an Issue][issues]**: Found a bug? Let us know!
- **💬 [Start a Discussion][discussions]**: Have ideas or suggestions? We'd love to hear from you.

<br>
<p align="left">
  <a href="https://github.com{/eli64s/readme-ai/}graphs/contributors">
    <img src="https://contrib.rocks/image?repo=eli64s/readme-ai">
  </a>
</p>

---

## 🎗 License

README-AI is released under the terms of the [MIT License][license].

---

## 🙌 Acknowledgments

* [Shields.io](https://shields.io/)
* [Simple Icons](https://simpleicons.org/)
* [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
* [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
* [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)

<p align="right"><a href="#-overview">⬆️ Top</a></p>

---

<!-- Documentation -->
[mkdocs]: https://eli64s.github.io/readme-ai "Official Documentation"

<!-- GitHub Links -->
[contributing]: https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md
[issues]: https://github.com/eli64s/readme-ai/issues
[discussions]: https://github.com/eli64s/readme-ai/discussions
[license]: https://github.com/eli64s/readme-ai/blob/main/LICENSE

<!-- Example READMEs -->
[default]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-ai.md "readme-python.md"
[ascii-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/ascii.md "ascii.md"
[classic-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/classic.md "readme-postgres.md"
[compact-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/compact.md "readme-java.md"
[modern-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/modern.md "readme-pyflink.md"
[svg-banner]: https://github.com/eli64s/readme-ai/blob/main/examples/banners/svg-banner.md "readme-streamlit.md"
[dalle-logo]: https://github.com/eli64s/readme-ai/blob/main/examples/logos/dalle.md "readme-vercel.md"
[readme-kotlin]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md "readme-kotlin.md"
[for-the-badge]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-docker-go.md "readme-docker-go.md"
[fastapi-redis]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md "readme-fastapi-redis.md"
[offline-mode]: https://github.com/eli64s/readme-ai/blob/main/examples/offline-mode/readme-litellm.md "readme-litellm.md"

<!-- Example Repositories -->
[readme-ai]: https://github.com/eli64s/readme-ai "readme-ai"
[pyflink]: https://github.com/eli64s/pyflink-poc "pyflink-poc"
[postgres]: https://github.com/jwills/buenavista "Buenavista"
[java]: https://github.com/avjinder/Minimal-Todo "minimal-todo"
[kotlin]: https://github.com/rumaan/file.io-Android-Client "android-client"
[docker-golang]: https://github.com/olliefr/docker-gs-ping "docker-gs-ping"
[vercel]: https://github.com/PiyushSuthar/github-readme-quotes "github-readme-quotes"
[streamlit]: https://github.com/eli64s/readme-ai-streamlit  "readme-ai-streamlit"
[fastapi]: https://github.com/FerrariDG/async-ml-inference "async-ml-inference"
[litellm]: https://github.com/BerriAI/litellm "offline-mode"
