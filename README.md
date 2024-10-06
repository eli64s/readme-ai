<p align="center">
  <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/icons/readme-ai-logo.svg" width="60%">
</p>
<h5 align="center">README-AI, Your AI-Powered Documentation Assistant</h5>
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

1. [⚡️ Introduction](#️-introduction)
2. [👾 Demo](#-demo)
3. [☄️ Features](#-features)
4. [🛸 Quickstart](#-getting-started)
5. [🔡 Configuration](#-configuration)
6. [🤖 Examples](#-examples)
7. [🔰 Contributing](#-contributing)

<br>

> [!IMPORTANT]
> ✨ See the [Official Documentation](https://eli64s.github.io/readme-ai) for more details.

<!--
<p align="center">
  <a href="https://eli64s.github.io/readme-ai">
    <img src="https://img.shields.io/badge/Official%20Documentation-526CFE?logo=MaterialForMkDocs&logoColor=white&labelColor=526CFE">
  </a>
  <a href="https://readme-ai.streamlit.app/">
    <img src="https://img.shields.io/badge/Streamlit%20Web%20Application-FF4B4B?logo=Streamlit&logoColor=white&labelColor=FF4B4B">
  </a>
  <a href="https://www.youtube.com/watch?v=NiUrm1ni7bE">
    <img src="https://img.shields.io/badge/YouTube%20Tutorial-FFFFFF?logo=YouTube&logoColor=FF7878">
  </a>
</p>
-->

---

## ⚡️ Introduction

***Objective***

README-AI is a developer tool for automatically generating README markdown files using a robust repository processor engine and generative AI. Simply provide a repository URL or local path to your codebase, and a well-structured and detailed README file will be generated for you.


***Motivation***

This project aims to streamline the documentation process for developers, ensuring projects are properly documented and easy to understand. Whether you're working on an open-source project, enterprise software, or a personal project, README-AI is here to help you create high-quality documentation quickly and efficiently.

---

## 👾 Demo

**Running from the command line:**

[readmeai-cli-demo](https://github.com/eli64s/artifacts/assets/43382407/55b8d1b9-06a7-4b1f-b6a7-aaeccdb27679)

**Running directly in your browser:**

[readmeai-streamlit-demo](https://github.com/eli64s/artifacts/assets/43382407/3eb39fcf-c1df-49c6-bb5c-63e141857ae3)

---

## ☄️ Features

* **Automated Documentation**: Synchronize data from third-party sources and generates documentation automatically.
* **Customizable Output**: Dozens of options for styling/formatting, badges, header designs, and more.
* **Language Agnostic**: Works across a wide range of programming languages and project types.
* **Multi-LLM Support**: Compatible with `OpenAI`,  `Ollama`,  `Anthropic`,  `Google Gemini` and `Offline Mode`.
* **Offline Mode**: Generate a boilerplate README without calling an external API.
* **Markdown Best Practices**: Leverage best practices in Markdown formatting for clean, professional-looking docs.

A few combinations of README styles and configurations:

<table>
  <!-- row 0 -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/headers/custom-image.png" alt="custom-project-logo" width="700" /><br>
      <code>--image custom --badge-color FF4B4B --badge-style flat-square --header-style classic</code>
    </td>
  </tr>
  <!-- row 1 -->
  <tr>
    <td colspan="2" align="center"><br>
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/headers/header-minimal.png" width="700" /><br>
      <code>--image cloud --header-style compact --toc-style fold</code>
    </td>
  </tr>
  <!-- row 2 -->
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/assets/images/headers/header-cloud.png" alt="cloud-db-logo" width="450" /><br>
      <code>--align left --badge-style flat-square --image cloud</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/assets/images/headers/header-gradient.png" alt="gradient-markdown-logo" width="450" /><br>
      <code>--align left --badge-style flat --image gradient</code>
    </td>
  </tr>
  <!-- row 3 -->
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/headers/header-custom.png" alt="custom-logo" width="450" /><br>
      <code>--badge-style flat --image custom</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/headers/header-skills.png" alt="skills-light" width="450" /><br>
      <code>--badge-style skills-light --image grey</code>
    </td>
  </tr>
  <tr>
    <!-- row 4 -->
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/headers/header-flat-square.png" alt="readme-ai-header" width="450" /><br>
      <code>--badge-style flat-square</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/headers/header-black.png" alt="black-logo" width="450" /><br>
      <code>--badge-style flat --image black</code>
    </td>
  </tr>
  <!-- row 5 -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/headers/header-default-v2.png" alt="default-header" width="900" /><br>
      <code>--image custom --badge-color 00ffe9 --badge-style flat-square --header-style classic</code>
    </td>
  </tr>
  <!-- row 6 -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://github.com/eli64s/readme-ai/blob/main/docs/assets/images/project-logo-dalle.png" alt="default-header" width="900" /><br>
      <code>--image llm --badge-style plastic --header-style classic</code>
    </td>
  </tr>
  <!-- row 7 -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/assets/images/headers/modern-pyflink.png" alt="default-header" width="900" /><br>
      <code>--image custom --badge-color BA0098 --badge-style flat-square --header-style modern --toc-style fold</code>
    </td>
  </tr>
</table>

See the <a href="https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#-configuration">Configuration</a> section for a complete list of CLI options.

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
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/overview.png" alt="llm-overview" width="700" /></td>
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>✨ Features</strong></summary><br>
  <table>
    <tr>
      <td><b>Features Table</b><br>
        <p>◎ Generated markdown table that highlights the key technical features and components of the codebase. This table is generated using a structured <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/prompts.toml#L18">prompt template.</a>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/llm-features.png" alt="llm-features" width="700" /></td>
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
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/project-structure.png" alt="directory-tree" width="700" />
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
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/file-summaries.png" alt="file-summaries" width="700" />
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
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/prerequisites.png" alt="prerequisites" width="700"  />
      </td>
    </tr>
    <tr>
      <td><b>Installation Guide</b><br>
        <p>◎ <code>Installation</code>, <code>Usage</code>, and <code>Testing</code> guides are generated based on the project's dependency files and codebase configuration.
        </p>
        <tr>
        <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/usage_guide.png" alt="installation" width="700" />
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
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/contributing_guidelines.png" alt="contributing-guidelines" width="700" /></td>
    </tr>
    <tr>
      <td><b>Additional Sections</b><br>
        <p>◎ <code>Project Roadmap</code>, <code>Contributing Guidelines</code>, <code>License</code>, and <code>Acknowledgements</code> are included by default.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/assets/images/footer.png" alt="footer" width="700" /></td>
    </tr>
  </table>
</details>

---

## 🛸 Getting Started

**System Requirements:**

* Python `3.9+`
* Package Manager/Container: `pip`,  `pipx`,  `docker`
* LLM API Service: `OpenAI`,  `Ollama`,  `Anthropic`,  `Google Gemini`,  `Offline Mode`

**Repository URL or Path:**

Make sure to have a repository URL or local directory path ready for the CLI.

* [**GitHub**](https://github.com/)
* [**GitLab**](https://gitlab.com/)
* [**Bitbucket**](https://bitbucket.org/)
* [**File System**](https://en.wikipedia.org/wiki/File_system)

**LLM API Service:**
* [**OpenAI**](https://platform.openai.com/docs/quickstart/account-setup): Recommended, requires an account setup and API key.
* [**Ollama**](https://github.com/ollama/ollama): Free and open-source, potentially slower and more resource-intensive.
* [**Anthropic**](https://www.anthropic.com/): Requires an Anthropic account and API key.
* [**Google Gemini**](https://ai.google.dev/tutorials/python_quickstart): Requires a Google Cloud account and API key.
* [**Offline Mode**](https://github.com/eli64s/readme-ai/blob/main/examples/readme-offline.md): Generates a boilerplate README without making API calls.

---

### 🔩 Installation

Install readme-ai using your preferred package manager, container, or directly from the source.

#### Using `pip`

[![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/readmeai/)

```sh
❯ pip install readmeai
```

#### Using `pipx`

[![pipx](https://img.shields.io/badge/pipx-2CFFAA.svg?style=flat&logo=pipx&logoColor=black)](https://pipxproject.github.io/pipx/installation/)

```sh
❯ pipx install readmeai
```

> [! TIP]
>
> <sub>Use [pipx](https://pipx.pypa.io/stable/installation/) to install and run Python command-line applications without causing dependency conflicts with other packages!</sub>

#### Using `docker`

Pull the latest Docker image from the Docker Hub repository.

[![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://hub.docker.com/r/zeroxeli/readme-ai)

```sh
❯ docker pull zeroxeli/readme-ai:latest
```

#### From `source`

<details closed><summary><i>Build readme-ai</i></summary><br>

#### Using `bash`

[![bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white)](https://www.gnu.org/software/bash/)

```sh
❯ bash setup/setup.sh
```

#### Using `poetry`

  [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

1. Clone the repository:

```sh
❯ git clone https://github.com/eli64s/readme-ai
```

2. Navigate to the `readme-ai` directory:

```sh
❯ cd readme-ai
```

3. Install dependencies using `poetry`:

```sh
❯ poetry install
```

4. Enter the `poetry` shell environment:

```sh
❯ poetry shell
```

</details>

#### Installing Optional Dependencies

To use the **Anthropic** and **Google Gemini** clients, install the optional dependencies.

Anthropic:

```sh
❯ pip install readmeai[anthropic]
```

Google Gemini:

```sh
❯ pip install readmeai[gemini]
```

---

### ⚙️ Usage

#### Environment Variables

**OpenAI**

Generate a OpenAI API key and set it as the environment variable `OPENAI_API_KEY` .

```sh
# Using Linux or macOS
❯ export OPENAI_API_KEY=<your_api_key>

# Using Windows
❯ set OPENAI_API_KEY=<your_api_key>
```

**Ollama**

Pull your model of choice from the Ollama repository:

```sh
❯ ollama pull mistral:latest
```

Start the Ollama server:

```sh
❯ export OLLAMA_HOST=127.0.0.1 && ollama serve
```

<sub>See all available models from Ollama [here.](https://github.com/ollama/ollama-python?tab=readme-ov-file)</sub>

**Anthropic**

Generate an Anthropic API key and set the following environment variables:

```sh
❯ export ANTHROPIC_API_KEY=<your_api_key>
```

**Google Gemini**

Generate a Google API key and set the following environment variables:

```sh
❯ export GOOGLE_API_KEY=<your_api_key>
```

#### Running the CLI

#### Using `pip`

[![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/readmeai/)

With OpenAI:

```sh
❯ readmeai --api openai --repository https://github.com/eli64s/readme-ai
```

> [! IMPORTANT]
> By default, the `gpt-3.5-turbo` model is used. Higher costs may be incurred when more advanced models.
>

With Ollama:

```sh
❯ readmeai --api ollama --model llama3 --repository https://github.com/eli64s/readme-ai
```

With Anthropic:

```sh
❯ readmeai --api anthropic -m claude-3-5-sonnet-20240620 -r https://github.com/eli64s/readme-ai
```

With Gemini:

```sh
❯ readmeai --api gemini -m gemini-1.5-flash -r https://github.com/eli64s/readme-ai
```

Adding more customization options:

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

#### Using `docker`

Running the Docker container with the OpenAI API:

[![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://hub.docker.com/r/zeroxeli/readme-ai)

```sh
❯ docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
-r https://github.com/eli64s/readme-ai
```

#### Using `streamlit`

Try readme-ai directly in your browser, no installation required. See the <a href="https://github.com/eli64s/readme-ai-streamlit">readme-ai-streamlit</a> repository for more details.

[<img align="center" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" width="20%">](https://readme-ai.streamlit.app/)

#### From `source`

<details closed>
  <summary><i>Using readme-ai</i></summary><br>

  #### Using `bash`

  [![bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white)](https://www.gnu.org/software/bash/)



```sh
  ❯ conda activate readmeai
  ❯ python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
  ```

  #### Using `poetry`

  [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)



```sh
  ❯ poetry shell
  ❯ poetry run python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
  ```

</details>

---

### 🧪 Testing

The pytest framework and nox automation tool are used for testing the application.

#### Using `pytest`

[![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white)](https://docs.pytest.org/en/7.1.x/contents.html)

```sh
❯ make test
```

#### Using `nox`

```sh
❯ make test-nox
```

> [!TIP]
> <sub>Use [nox](https://nox.thea.codes/en/stable/) to test application against multiple Python environments and dependencies!</sub>

---

## 🔡 Configuration

Customize your README generation using these CLI options:

| Option | Description | Default |
| :-- | :--: | :--: |
| `--align` | Text align in header | `center` |
| `--api` | LLM API service provider | `offline` |
| `--badge-color` | Badge color name or hex code | `0080ff` |
| `--badge-style` | Badge icon style type | `flat` |
| `--base-url` | Base URL for the repository | `v1/chat/completions` |
| `--context-window` | Maximum context window of the LLM API | `3900` |
| `--emojis` | Adds emojis to the README header sections | `False` |
| `--header-style` | Header template style | `classic` |
| `--image` | Project logo image | `blue` |
| `--model` | Specific LLM model to use | `gpt-3.5-turbo` |
| `--output` | Output filename | `readme-ai.md` |
| `--rate-limit` | Maximum API requests per minute | `10` |
| `--repository` | Repository URL or local directory path | `None` |
| `--temperature` | Creativity level for content generation | `0.1` |
| `--toc-style` | Table of contents template style | `bullet` |
| `--top-p` | Probability of the top-p sampling method | `0.9` |
| `--tree-depth` | Maximum depth of the directory tree structure | `2` |

> [!TIP]
> For a full list of options, run `readmeai --help` in your terminal.
>

### 🎨 Customization

To see the full list of customization options, check out the [Configuration](https://eli64s.github.io/readme-ai/configuration/) section in the official documentation. This section provides a detailed overview of all available CLI options and how to use them, including badge styles, header templates, and more.

---

## 🤖 Examples

| Language/Framework | Output File | Input Repository | Description |
| :--: | :--: | :--: | :--: |
| Python | [readme-python.md][0a] | [readme-ai][0b] | Core readme-ai project |
| TypeScript & React | [readme-typescript.md][1a] | [ChatGPT App][1b] | React Native ChatGPT app |
| PostgreSQL & DuckDB | [readme-postgres.md][2a] | [Buenavista][2b] | Postgres proxy server |
| Kotlin & Android | [readme-kotlin.md][3a] | [file.io Client][3b] | Android file sharing app |
| Streamlit | [readme-streamlit.md][4a] | [readme-ai-streamlit][4b] | Streamlit UI for readme-ai app |
| Rust & C | [readme-rust-c.md][5a] | [CallMon][5b] | System call monitoring tool |
| Docker & Go | [readme-go.md][6a] | [docker-gs-ping][6b] | Dockerized Go app |
| Java | [readme-java.md][7a] | [Minimal-Todo][7b] | Minimalist todo Java app |
| FastAPI & Redis | [readme-fastapi-redis.md][8a] | [async-ml-inference][8b] | Async ML inference service |
| Jupyter Notebook | [readme-mlops.md][9a] | [mlops-course][9b] | MLOps course repository |
| Apache Flink | [readme-local.md][10a] | Local Directory | Example using a local directory |

<sub>See additional README files generated by readme-ai [here](https://github.com/eli64s/readme-ai/tree/main/examples/markdown)</sub>

---

## 🏎💨 Project Roadmap

* [ ] Release `readmeai 1.0.0` with enhanced documentation management features.
* [ ] Develop `Vscode Extension` to generate README files directly in the editor.
* [ ] Develop `GitHub Actions` to automate documentation updates.
* [ ] Add `badge packs` to provide additional badge styles and options.
  + [ ] Code coverage, CI/CD status, project version, and more.

---

## 🔰 Contributing

Contributions are welcome and encouraged! If interested, please begin by reviewing the resources below:

* **💡 [Contributing Guide][1]**: Learn about our contribution process, coding standards, and how to submit your ideas.
* **💬 [Start a Discussion][2]**: Have questions or suggestions? Join our community discussions to share your thoughts and engage with others.
* **🐛 [Report an Issue][3]**: Found a bug or have a feature request? Let us know by opening an issue so we can address it promptly.

<br>
<p align="left">
  <a href="https://github.com{/eli64s/readme-ai/}graphs/contributors">
    <img src="https://contrib.rocks/image?repo=eli64s/readme-ai">
  </a>
</p>

---

## 📒 Changelog

[Changelog][0]

---

## 🎗 License

[MIT License][4]

---

## 🙌 Acknowledgments

* [Shields.io](https://shields.io/)
* [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
* [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
* [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)

<p align="right">
  <a href=#️-introduction>⬆️ Top</a>
</p>

---

<!-- README Example Links -->
[0a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-ai.md "readme-python.md"
[0b]: https://github.com/eli64s/readme-ai "readme-ai"
[1a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-typescript.md "readme-typescript.md"
[1b]: https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript "ChatGPT App"
[2a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-postgres.md "readme-postgres.md"
[2b]: https://github.com/jwills/buenavista "Buenavista"
[3a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md "readme-kotlin.md"
[3b]: https://github.com/rumaan/file.io-Android-Client "file.io Client"
[4a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-streamlit-v0.5.88.md "readme-streamlit.md"
[4b]: https://github.com/eli64s/readme-ai-streamlit "readme-ai-streamlit"
[5a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-rust-c.md "readme-rust-c.md"
[5b]: https://github.com/DownWithUp/CallMon "CallMon"
[6a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-docker-go.md "readme-docker-go.md"
[6b]: https://github.com/olliefr/docker-gs-ping "docker-gs-ping"
[7a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-java.md "readme-java.md"
[7b]: https://github.com/avjinder/Minimal-Todo "Minimal-Todo"
[8a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md "readme-fastapi-redis.md"
[8b]: https://github.com/FerrariDG/async-ml-inference "async-ml-inference"
[9a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-mlops.md "readme-mlops.md"
[9b]: https://github.com/GokuMohandas/mlops-course "mlops-course"
[10a]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-local.md "readme-local.md"

<!-- GitHub Repository Links -->
[0]: https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md "Changelog"
[1]: https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md "Contributing Guide"
[2]: https://github.com/eli64s/readme-ai/discussions "Start a Discussion"
[3]: https://github.com/eli64s/readme-ai/issues "Open an Issue"
[4]: https://github.com/eli64s/readme-ai/blob/main/LICENSE "License"
