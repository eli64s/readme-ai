
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
readme-ai
</h1>
<h3>◦ Let README-AI write your docs, while you code.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />

<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/eli64s/readme-ai?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/eli64s/readme-ai?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/eli64s/readme-ai?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/eli64s/readme-ai?style&color=5D6D7E)
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The README-AI project is a tool that generates comprehensive README Markdown files for GitHub repositories using OpenAI's GPT language model APIs. It analyzes the codebase, extracts dependencies and file text, generates natural language summaries and markdown, and builds a README file. The tool automates the process of generating effective documentation for a codebase, saving valuable time for developers and improving code readability for users. The project is highly configurable with several options for API and Git configurations, making it adaptable to a wide range of use cases.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a modular architecture with separate files for handling different concerns such as preprocessing, building, logging, and file I/O, among others. The application also uses the Factory design pattern for handling file I/O operations. It uses Python 3.9 and standard libraries for most functionality and utilizes the OpenAI GPT API to generate text from code. |
| **📑 Documentation** | The repository includes a well-written README file that provides an overview of the project and its features, as well as instructions for setting up and running the application. The repository also includes comments in the code for clarity and maintainability. |
| **🧩 Dependencies** | The codebase uses several third-party libraries such as pandas, colorlog, and httpx for data manipulation, logging, and HTTP requests, respectively. It also uses the OpenAI GPT API for generating text from code. |
| **♻️ Modularity** | The repository follows a modular design, separating concerns into different files for readability, maintainability, and reusability of code. The codebase adheres to the Single Responsibility Principle, with each module handling one specific responsibility. |
| **✔️ Testing** | The repository includes test scripts for unit and integration testing using the pytest framework, with coverage reports generated using conda and pytest-cov. The repository also includes scripts to automate testing and coverage reporting. |
| **⚡️ Performance** | The application uses asynchronous HTTP requests with the httpx library to interface with the OpenAI GPT API, improving performance by allowing for parallel requests. The code also includes caching of generated summaries to avoid repeating requests to the API. |
| **🔒 Security** | The repository includes a script to ensure that the environment used for the application is secure, with the necessary packages and dependencies installed. The repository also includes instructions for setting up virtual environments using conda or Python virtualenv. |
| **🔀 Version Control** | The repository is hosted on GitHub and includes a detailed commit history with informative commit messages. The repository also includes a Makefile for automating various tasks and scripts for automating testing and generating coverage reports. |
| **🔌 Integrations** | The repository does not include integrations with other services or systems. |
| **📈 Scalability** | The codebase uses asynchronous HTTP requests, which can be scaled to handle a larger number of requests concurrently. The code also includes caching of generated summaries, which helps to improve scalability by reducing the need for repeated requests to the OpenAI GPT API. |

---


## 📂 Project Structure


```bash
repo
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── conf.toml
│   ├── dependency_files.toml
│   ├── ignore_files.toml
│   ├── language_names.toml
│   ├── language_setup.toml
│   └── svg
│       ├── badges.json
│       └── badges_compressed.json
├── examples
│   ├── imgs
│   │   ├── closing.png
│   │   ├── demo.png
│   │   ├── features.png
│   │   ├── getting_started.png
│   │   ├── header.png
│   │   ├── modules.png
│   │   ├── overview.png
│   │   └── tree.png
│   ├── readme-c.md
│   ├── readme-energy-forecasting.md
│   ├── readme-fastapi-redis.md
│   ├── readme-fastapi.md
│   ├── readme-gitlab.md
│   ├── readme-go-bash.md
│   ├── readme-go.md
│   ├── readme-java.md
│   ├── readme-javascript-gpt.md
│   ├── readme-javascript.md
│   ├── readme-kotlin.md
│   ├── readme-lanarky.md
│   ├── readme-mlops.md
│   ├── readme-pyflink.md
│   ├── readme-python-ml.md
│   ├── readme-python.md
│   ├── readme-react.md
│   ├── readme-rust-c.md
│   ├── readme-rust.md
│   └── readme-typescript.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── clean.sh
│   ├── run.sh
│   ├── run_batch.sh
│   └── test.sh
├── setup
│   ├── environment.yaml
│   └── setup.sh
├── setup.py
├── src
│   ├── __init__.py
│   ├── builder.py
│   ├── conf.py
│   ├── factory.py
│   ├── logger.py
│   ├── main.py
│   ├── model.py
│   ├── parse.py
│   ├── preprocess.py
│   └── utils.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_builder.py
    ├── test_conf.py
    ├── test_factory.py
    ├── test_logger.py
    ├── test_main.py
    ├── test_model.py
    ├── test_parse.py
    ├── test_preprocess.py
    └── test_utils.py

9 directories, 71 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                         | Module     |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | The code creates a Docker container using Python 3.9, sets the working directory to /app, and adds the contents of the current directory to it. The requirements.txt file is copied and the required packages are installed using pip. Port 80 is exposed to the outside world, and the main.py file is run using the specified command when the container is launched.         | Dockerfile |
| Makefile   | This Makefile provides a set of commands to automate various tasks such as formatting code style, creating virtual environments (conda and python), running cProfile on a CLI script, and running SnakeViz on the generated profile. The'help' command provides an overview of available commands, and each command is executed by specifying its name after the'make' command. | Makefile   |
| setup.py   | This code is a setup script for the README-AI package, which generates comprehensive README Markdown files using OpenAI's GPT language model APIs. The script includes package dependencies, author information, project URLs, and keywords. The script also specifies the Python version required and provides options for dev and test environments.                          | setup.py   |

</details>

<details closed><summary>Scripts</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                           | Module               |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| run_batch.sh | The provided code snippet is a Bash script that stores a list of GitHub repository URLs in an array variable and iterates through the array to execute a Python script that generates a README file in Markdown format for each repository. It uses the basename of each repository URL as part of the filename for each README file.                             | scripts/run_batch.sh |
| run.sh       | This bash script activates a conda environment called "readme_ai" and runs a Python script located at "src/main.py". It also sets the "pipefail" option to ensure that any non-zero exit codes from commands within the script will cause the script to exit immediately. Additionally, an environment variable for the OpenAI API key can be exported if needed. | scripts/run.sh       |
| clean.sh     | This code snippet removes various files and directories that are not needed in a project. It deletes backup files, Python cache files, cache directories, and VS Code settings. It also removes build artifacts, pytest cache, benchmarks, and specific files such as raw data and log files.                                                                     | scripts/clean.sh     |
| test.sh      | This code snippet is a Bash script for generating test code coverage reports using Conda and pytest. It sets directories to include and exclude from the coverage report, generates the report, and sets a coverage failure threshold. It also removes certain files and folders after running the tests.                                                         | scripts/test.sh      |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                    | Module         |
|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | The provided Bash script checks if the'tree' command is installed and installs it if not. It then checks for the presence of Git, Python 3.7 or higher, and the'readme_ai' environment. If the environment exists, it skips its creation, otherwise creates it and installs required packages from'requirements.txt'. Finally, it exports the Python path and deactivates the environment. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module            |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | The provided code snippet handles preprocessing of a codebase. It includes classes for analyzing a git repository, mapping file extensions to programming languages, and extracting dependency file contents. The code utilizes pandas for data manipulation and includes several file parser methods for different file types.                                                                                                                                                                                                               | src/preprocess.py |
| conf.py       | The provided code snippet defines several data classes to store configuration constants for the README-AI application, including API, Git, Markdown, Paths, and Prompts configurations. It also includes a ConfigHelper to assist in loading and handling these configurations. The load_config and load_config_helper functions are used to load the configuration constants from TOML files.                                                                                                                                                | src/conf.py       |
| logger.py     | The code provides a Logger class with methods for logging messages at different levels (info, debug, warning, error, and critical) and a custom log format using the colorlog library. The class is designed to be a singleton, ensuring that only one instance of the logger is used throughout the project, and can be configured with a specific logging level.                                                                                                                                                                            | src/logger.py     |
| factory.py    | The code snippet provides a Factory class for handling file input/output operations. It supports reading and writing to Markdown, TOML, JSON, and YAML file formats. The code also includes error handling for cases where files cannot be read or written, and includes a caching mechanism for read operations.                                                                                                                                                                                                                             | src/factory.py    |
| model.py      | The provided code snippet is an OpenAI API handler that generates natural language text from code and prompts. The `code_to_text` function converts code to text for a given prompt, while the `chat_to_text` function generates text from a list of prompts. The `generate_text` function handles the request to the OpenAI API to generate text and uses the `httpx` library for asynchronous HTTP requests. The handler also includes a cache to store the generated summaries and a rate limiter to avoid exceeding the API's rate limit. | src/model.py      |
| builder.py    | This code snippet builds a README Markdown file for a codebase. It creates various sections of the README file, such as badges, a directory tree, a list of packages and dependencies, and markdown tables for each sub-directory in the project. Additionally, the snippet uses Pandas to format generated code summaries into a DataFrame. The resulting README file is written to the local file system.                                                                                                                                   | src/builder.py    |
| utils.py      | The provided code snippet contains various utility functions for use with the README-AI tool. It includes functionality for cloning repositories, extracting username and repository name from GitHub URLs, adjusting the max number of tokens for a prompt, counting and truncating text by the number of tokens, checking if a file is valid for processing, checking if a URL is valid, flattening nested lists, and formatting generated text.                                                                                            | src/utils.py      |
| parse.py      | This code snippet includes various functions to parse dependency files for different languages. These languages include Python, JavaScript, Rust, Java, C++, and C. Each function extracts and returns a list of dependencies from their respective file type. The parsing is done using various libraries such as `yaml`, `toml`, and `json`. Any errors during parsing are logged using the `Logger` class.                                                                                                                                 | src/parse.py      |
| main.py       | This code generates a README file for a given repository using OpenAI's GPT APIs. It extracts dependencies and file text using a scanner, generates code-to-text and markdown text using GPT, and formats the resulting text into markdown. The resulting markdown is built into a README file.                                                                                                                                                                                                                                               | src/main.py       |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

1. Clone the readme-ai repository:
```sh
git clone https://github.com/eli64s/readme-ai
```

2. Change to the project directory:
```sh
cd readme-ai
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using readme-ai

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] [ℹ️  Task 1: Implement X]
> - [ ] [ℹ️  Task 2: Refactor Y]
> - [ ] [...]


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `[ℹ️  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [ℹ️  List any resources, contributors, inspiration, etc.]

---
