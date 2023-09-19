<div align="center">
    <h1 align="center">
        <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80" />
        <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80" />
        <br>README-AI
    </h1>
    <h3>◦ Generate beautiful and informative README.md files.</h3>
    <h3>◦ Developed with OpenAI's GPT language model APIs.</h3>
    <br>
    <p align="center">
        <img src="https://img.shields.io/badge/Markdown-000000.svg?stylee&logo=Markdown&logoColor=white" alt="Markdown" />
        <img src="https://img.shields.io/badge/OpenAI-412991.svg?stylee&logo=OpenAI&logoColor=white" alt="OpenAI" />
        <img src="https://img.shields.io/badge/Python-3776AB.svg?stylee&logo=Python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?stylee&logo=Pytest&logoColor=white" alt="pytest" />
        <img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
        <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="actions" />
    </p>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/v/readmeai?color=5D6D7E&logo=pypi" alt="pypi-version" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/pyversions/readmeai?color=5D6D7E&logo=python" alt="pypi-python-version" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/dm/readmeai?color=5D6D7E" alt="pypi-downloads" />
    </a>
    <img src="https://img.shields.io/github/license/eli64s/readme-ai?color=5D6D7E" alt="github-license" />
</div>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
    - [🎯 *Motivation*](#-motivation)
    - [⚠️ *Disclaimer*](#️-disclaimer)
- [👾 Demo](#-demo)
- [⚙️ Features](#️-features)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Dependencies](#️-dependencies)
    - [📂 Repository](#-repository)
    - [🔐 OpenAI API](#-openai-api)
  - [📦 Installation](#-installation)
  - [🎮 Using *README-AI*](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🔢 Configuration](#-configuration)
- [🛠 Future Development](#-future-development)
- [📒 Changelog](#-changelog)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

*README-AI* is a powerful, user-friendly command-line tool that generates extensive README markdown documents for your software and data projects. By providing a remote repository URL or path to your codebase, this tool generates documentation for your entire project, leveraging the capabilities of large language models and OpenAI's GPT APIs.

#### 🎯 *Motivation*

Simplifies the process of writing and maintaining high-quality project documentation. My aim for this project is to provide all skill levels a tool that improves their technical workflow, in an efficient and user-friendly manner. Ultimately, the goal of *README-AI* is to improve the adoption and usability of open-source projects, enabling everyone to better understand and use open-source tools.
#### ⚠️ *Disclaimer*

*README-AI* is currently under development and has an opinionated configuration and setup. While this tool provides an excellent starting point for documentation, its important to review all text generated by the OpenAI API to ensure it accurately represents your codebase. Ensure all content in your repository is free of sensitive information before executing.

Additionally, frequently monitor your API usage and costs by visiting the [OpenAI API Usage Dashboard](https://platform.openai.com/account/usage).

---

## 👾 Demo

<a href="https://youtu.be/pl-VcVfGbbk">
    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/f0c5a038f63ae04b2d4452974676a92db42be8ce/examples/imgs/demo.png" alt="demo-video">
</a>

<!-- #### *🤖 Streamlit UI (experimental)*

> Try out the *readme-ai* app in your browser using this [link!](https://readme-ai.streamlit.app/)
-->

---

## ⚙️ Features

<h1 align="center">1.<br>👇<br><br>📑 Codebase Documentation</h1>
<table align="center">
    <tr>
        <td>
            <h3>◦ Repository File Summaries</h3>
            <ul>
                <li>Code summaries are generated for each file via OpenAI's <i>gpt-3.5-turbo</i> engine.</li>
                <li>The File column in the markdown table contains a link to the file on GitHub.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/modules.png" alt="docs">
        </td>
    </tr>
</table>

<h1 align="center">⒉<br>👇<br><br>🎖 Badges</h1>
<table align="center">
    <tr>
        <td>
            <h3>◦ Introduction, Badges, & Table of Contents</h3>
            <ul>
                <li>The OpenAI API is prompted to create a 1-sentence phrase describing your project.</li>
                <li>Project dependencies and metadata are visualized using <a href="https://shields.io/">Shields.io</a> badges.</li>
                <li>Badges are sorted by hex code, displayed from light to dark hues.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/header.png" alt="docs">
        </td>
    </tr>
</table>

<h1 align="center">⒊<br>👇<br><br>🧚 Prompted Text Generation</h1>
<table align="center">
    <tr>
        <td>
            <h3>◦ Features Table & Overview</h3>
            <ul>
                <li>Detailed prompts are embedded with repository metadata and passed to the OpenAI API.</li>
                <ul>
                    <li><em>Features</em> table highlights various technical attributes of your codebase.
                    </li>
                    <li><em>Overview</em> section describes your project's use case and applications.
                    </li>
                </ul>
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/features.png" alt="features">
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/overview.png" alt="overview">
        </td>
    </tr>
</table>

<h1 align="center">⒋<br>👇<br><br>🌲 Repository Tree</h1>
<table align="center">
    <tr>
        <td>
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/tree.png" alt="tree">
        </td>
    </tr>
</table>

<h1 align="center">⒌<br>👇<br><br>📦 Dynamic User Setup Guides</h1>
<table align="center">
    <tr>
        <td>
            <h3><b>◦ Installation, Usage, & Testing</b></h3>
            <ul>
                <li>Generates instructions for installing, using, and testing your codebase.</li>
                <li>README-AI currently supports this feature for code written with:</li>
                <ul>
                    <li>
                        <i>Python, Rust, Go, C, Kotlin, Java, JavaScript, TypeScript.</i>
                    </li>
                </ul>
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/getting_started.png" alt="getting_started">
        </td>
    </tr>
</table>

<h1 align="center">⒍<br>👇<br><br>👩‍💻 Contributing Guidelines & more!</h1>
<table align="center">
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/closing.png" alt="contribute">
        </td>
    </tr>
</table>

<h1 align="center">⒎<br>👇<br><br>💥 Example <i>README</i> Files</h1>
<p align="center">Example markdown files generated by <i>readme-ai!</i></p>

<div align="center">

|     | Example File                                                                                              | Repository                                                                                      | Language               | Bytes   |
|-----|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|------------------------|---------|
| 1️⃣ | [readme-python.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-python.md)               | [readme-ai](https://github.com/eli64s/readme-ai)                                                | Python                 | 19,839  |
| 2️⃣ | [readme-typescript.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-typescript.md)       | [chatgpt-app-react-typescript](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript) | TypeScript, React      | 988     |
| 3️⃣ | [readme-javascript.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-javascript.md)       | [assistant-chat-gpt-javascript](https://github.com/idosal/assistant-chat-gpt)                   | JavaScript, React      | 212     |
| 4️⃣ | [readme-kotlin.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md)               | [file.io-android-client](https://github.com/rumaan/file.io-Android-Client)                      | Kotlin, Java, Android  | 113,649 |
| 5️⃣ | [readme-rust-c.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-rust-c.md)               | [rust-c-app](https://github.com/DownWithUp/CallMon)                                             | C, Rust                | 72      |
| 6️⃣ | [readme-go.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-go.md)                       | [go-docker-app](https://github.com/olliefr/docker-gs-ping)                                      | Go                     | 41      |
| 7️⃣ | [readme-java.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-java.md)                   | [java-minimal-todo](https://github.com/avjinder/Minimal-Todo)                                   | Java                   | 17,725  |
| 8️⃣ | [readme-fastapi-redis.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md) | [async-ml-inference](https://github.com/FerrariDG/async-ml-inference)                           | Python, FastAPI, Redis | 355     |
| 9️⃣ | [readme-mlops.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-mlops.md)                 | [mlops-course](https://github.com/GokuMohandas/mlops-course)                                    | Python, Jupyter        | 8,524   |
| 🔟  | [readme-pyflink.md](https://github.com/eli64s/readme-ai/blob/main/examples/readme-pyflink.md)             | [flink-flow](https://github.com/eli64s/flink-flow)                                              | PyFlink                | 32      |

</div>

<h1 align="center">⒏<br>👇<br><br>📜 Custom README templates coming soon!</h1>
<p align="center">Developing a feature that allows users to select from a variety of README formats and styles.</p>
<p align="center">Custom templates will be tailored for use-cases such as data, ai & ml, research, minimal, and more!</p>

<p align="right">
    <a href="#top"><b>🔝 Return </b></a>
</p>

---

## 🚀 Getting Started

### ✔️ Dependencies

Before you begin, ensure that you have the following prerequisites installed:
- *Python > 3.8*
- *Pip or Docker (recommended)*
- *OpenAI API paid account and api key (see setup instructions below)*

#### 📂 Repository

You'll need a URL link to your remote repository or the directory path to your local code repository. The following repository types are supported:
- *GitHub*
- *GitLab*
- *File System*

#### 🔐 OpenAI API

To use the *README-AI* app, you must create an OpenAI API account and generate an API key. The steps below outline this process:

<details closed><summary>OpenAI API User Guide</summary>

1. Go to the [OpenAI website](https://platform.openai.com/).
2. Click the "Sign up for free" button.
3. Fill out the registration form with your information and agree to the terms of service.
4. Once logged in, click on the "API" tab.
5. Follow the instructions to create a new API key.
6. Copy the API key and keep it in a secure place.

</details>
<br>

> **⚠️ Note**
>
> - To maximize your experience with README-AI, it is recommended to set up a payment method on OpenAI's website. By doing so, you gain access to more powerful language models like gpt-3.5-turbo. Without a payment method, your usage will be restricted to the base gpt-3 models. This limitation might lead to less precise README files or potential errors during the generation process.
>
> - When using a payment method, make sure you have sufficient credits to run the README-AI application. Additionally, remember to regularly monitor your API usage and costs by visiting the [OpenAI API Usage Dashboard](https://platform.openai.com/account/usage). Please note that this API is not free and you will be charged for each request made, which can accumulate rapidly.
>
> - The generation of the README.md file should take under 1 minute. If the program runs for more than a few minutes, terminate the process immediately.

---

### 📦 Installation

Use any of the following methods to install project dependencies.

> *Pip ([PyPI Package](https://pypi.org/project/readmeai/))* - recommended
```sh
pip install --upgrade readmeai
```

> *Docker ([Docker Hub](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general))*
```sh
docker pull zeroxeli/readme-ai:latest
```

If you prefer to install the project dependencies locally, follow the steps below.

1. Clone the *readme-ai* repository to your machine.

```sh
git clone https://github.com/eli64s/readme-ai
```

2. Navigate to the *readme-ai* directory.

```sh
cd readme-ai
```

3. Install the project dependencies using one of the following methods.

> *Bash*

```sh
bash setup/setup.sh
```

> *Conda*

```sh
conda create -n readmeai python=3.9 -y && \
conda activate readmeai && \
pip install -r requirements.txt
```

> *Poetry*

```sh
poetry install
```

### 🎮 Using *README-AI*

Use the command-line to provide the OpenAI API key (if not already set) and specify an output path for your README file, along with the path to your local repository or remote code repository. You can also provide the output path in the [configuration file](./readmeai/conf/conf.toml)

Command-Line Arguments:

- `-k` or `--api-key`: Your OpenAI API key.
- `-o` or `--output`: The output path for your README.md file.
- `-r` or `--repository`: The URL or path to your code repository.
- `-t` or `--template`: The README template format to use. (coming soon!)
- `l` or `--language`: The language of text written in the README file (coming soon!)

Use any of the following methods to run the *readme-ai* CLI application.

> *Pip ([PyPI Package](https://pypi.org/project/readmeai/))* - recommended

```sh
readmeai --api-key "YOUR_API_KEY" --output readme-ai.md --repository https://github.com/eli64s/readme-ai

# Or export your OpenAI API key as an environment variable
export OPENAI_API_KEY="YOUR_API_KEY"
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

> *Docker ([Docker Hub](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general))*

```sh
docker run -it \
-e OPENAI_API_KEY="YOUR_API_KEY" \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

> *Conda*

```sh
conda activate readmeai
export OPENAI_API_KEY="YOUR_API_KEY"
python readmeai/main.py -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

> *Poetry*

```sh
poetry shell
export OPENAI_API_KEY="YOUR_API_KEY"
poetry run python readmeai/main.py -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

### 🧪 Running Tests

Execute the following command to run the test suite.

```sh
bash scripts/test.sh
```

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---

## 🔢 Configuration

To customize the README file generation process, you can modify the [configuration file](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml). The file contains the following sections:

- [*api*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L2) - OpenAI language model API configuration settings.
- [*git*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L12) - Default git repository settings used if no repository is provided.
- [*paths*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L17) - Directory paths and files used by the *readme-ai* application.
- [*prompts*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L26) - Large language model prompts used to generate the README file.
- [*md*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L59) - Dynamic Markdown section code templates used to build the README file.

---

## 🛠 Future Development

- [X] Distribute the *readme-ai* app as a Python library via [*PyPI*](https://pypi.org/project/readmeai/) and on [*Docker Hub*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general).
- [ ] Integrate *readme-ai* with Streamlit to provide a user-friendly UI to generate README files.
- [ ] Design README output templates for a variety of use-cases (i.e. data, web-dev, minimal, etc.)
- [ ] Add support for generating README files in any language (i.e. CN, ES, FR, JA, KO, RU).
- [ ] Create GitHub Actions script to automatically update your README file when new code is pushed.

---

## 📒 Changelog

[Changelog](./CHANGELOG.md)

---

## 🤝 Contributing

[Contributing Guidelines](./CONTRIBUTING.md)

---

## 📄 License

[MIT](./LICENSE)

---

## 👏 Acknowledgments

*Badges*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---
