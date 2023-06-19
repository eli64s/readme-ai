
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3>◦ README-AI: Elevate your README game with AI!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />

<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
</p>
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

The README-AI project is a command-line tool that uses OpenAI's GPT language model APIs to generate comprehensive README Markdown files for software repositories. Its core functionalities include preprocessing a codebase to extract file information and dependencies, generating natural language text using GPT, and building a formatted README file. Its value proposition is to save developers time and effort by automating the creation of high-quality documentation for their projects.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a modular architecture with clear separation of concerns. It utilizes different components for various tasks such as preprocessing, parsing, model handling, and Markdown generation. The application is designed to be scalable and extendable, with well-defined interfaces between the components. |
| **📑 Documentation** | The codebase has comprehensive documentation in the form of docstrings, README files, and inline comments. The documentation provides details on the purpose and functionality of each module, class, and method. It also includes instructions on how to install and use the application. |
| **🧩 Dependencies** | The codebase has a minimal set of dependencies, with most required packages included in the Python standard library. The only external dependencies are OpenAI's API and various packages for Docker and virtual environment management, testing, and profiling. |
| **♻️ Modularity** | The codebase follows a modular design pattern, with each module having a clear responsibility and function. The different modules interact through well-defined interfaces, allowing for easy changes and replacements of components. |
| **✔️ Testing** | The codebase includes a test suite with unit tests for each module and integration tests for the entire application. The tests use the pytest framework and are run automatically with every commit and pull request using a GitHub Actions workflow. |
| **⚡️ Performance** | The codebase has several performance optimizations, including caching of frequently used data, asynchronous processing, and profiling tools to identify performance bottlenecks. The Dockerfile also uses a lightweight base image to reduce the container's size and optimize startup time. |
| **🔒 Security** | The codebase has several security measures in place, including the use of secure coding practices, input validation, and exception handling to prevent code injection and other attacks. The application also uses secure communication channels to access the OpenAI API and other external resources. |
| **🔀 Version Control** | The codebase is hosted on GitHub and uses Git for version control. The development workflow includes feature branches, pull requests, code reviews, and automated testing and deployment. The codebase also has a well-defined branching strategy with clearly defined naming conventions for different types of branches. |
| **🔌 Integrations** | The codebase has integrations with various tools such as GitHub, Docker, and Conda. The Makefile includes several automation commands for building Docker images, creating virtual environments, and running tests and profiling. The application also includes support for various programming languages and file formats, providing flexibility for integration with different projects. |
| **📈 Scalability** | The codebase is designed to be scalable, with modularity and performance optimizations enabling support for large codebases. The application also includes configuration files that can be used to adjust various parameters to optimize performance for different environments. Additionally, the application architecture is designed to be extensible,

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
│   │   ├── closed_docs.png
│   │   ├── contribute.png
│   │   ├── demo.png
│   │   ├── features.png
│   │   ├── header.png
│   │   ├── license.png
│   │   ├── open_docs.png
│   │   ├── overview.png
│   │   ├── setup.png
│   │   └── tree.png
│   ├── readme-c.md
│   ├── readme-fastapi-redis.md
│   ├── readme-fastapi.md
│   ├── readme-gitlab.md
│   ├── readme-go-bash.md
│   ├── readme-go.md
│   ├── readme-java.md
│   ├── readme-javascript-gpt.md
│   ├── readme-javascript.md
│   ├── readme-kotlin.md
│   ├── readme-langchain.md
│   ├── readme-mlops.md
│   ├── readme-pyflink.md
│   ├── readme-python-ml.md
│   ├── readme-python.md
│   ├── readme-react.md
│   ├── readme-rust-c.md
│   ├── readme-rust.md
│   ├── readme-streamlit.md
│   └── readme-typescript.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── clean.sh
│   ├── run.sh
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

9 directories, 72 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                        | Module     |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | This code snippet creates a Docker image for a Python application. It sets the working directory, installs required packages from a requirements file, exposes port 80 to the outside world, and runs the main.py file when the container launches, specifying the host as 0.0.0.0.                                                                                                            | Dockerfile |
| Makefile   | This is a Makefile with several commands for automating tasks related to the project development workflow. The commands include cleaning unnecessary files, executing style formatting, creating a conda or virtual environment, running cProfile on a CLI script, and running SnakeViz on a profiling output file. These commands automate repetitive tasks and save time for the developers. | Makefile   |
| setup.py   | The provided code snippet is a setup script for the README-AI package, which is a command-line tool that uses OpenAI's GPT language model APIs to generate comprehensive README Markdown files. It includes installation requirements, optional dev and test dependencies, project information such as author and URL, and relevant keywords and classifiers.                                  | setup.py   |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                            | Module           |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | The provided code snippet is a Bash script that activates a Conda environment named'readme_ai' and runs a Python script'main.py'. It also includes error handling with'set-eo pipefail' and the option to export environment variables if needed.                                                                                                                                  | scripts/run.sh   |
| clean.sh | The provided code snippet is a bash script that aims to remove unnecessary files and directories from a project directory. It removes backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files. The script utilizes the'find' command to locate and'rm' to remove the specified files and directories. | scripts/clean.sh |
| test.sh  | This code snippet is a bash script that uses Conda to activate a virtual environment called "readme_ai". It then generates a code coverage report for the "src" directory, excluding files in the "tests" directory and a specific file called "__init__.py". The script also removes certain files and folders such as "__pycache__" and ".pytest_cache".                         | scripts/test.sh  |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                           | Module         |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | This Bash script checks for the installation of Git, Conda, and a specific version of Python. If not installed, the script prompts the user to install these dependencies. The script creates a new Conda environment named'readme_ai' with Python 3.8 and installs requirements from'requirements.txt'. Finally, it adds the Python path to the PATH environment variable and deactivates the Conda environment. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module            |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | The code provides preprocessing functionalities for a given input codebase. It analyzes a local or remote git repository, generates a DataFrame of file information, maps file extensions to their programming languages, tokenizes the content of each file, and extracts the dependency file contents. It also provides a wrapper class for the RepositoryParser.                                                                                                                                       | src/preprocess.py |
| conf.py       | The provided code snippet contains data classes to store various configuration constants used in the README-AI application. These data classes include ApiConfig, GitConfig, MarkdownConfig, PathsConfig, PromptsConfig, AppConfig, and ConfigHelper. The load_config() function loads configuration constants from a TOML file, and load_config_helper() function loads multiple configuration helper TOML files. The ConfigHelper class provides helper methods to read and update configuration files. | src/conf.py       |
| logger.py     | The provided code snippet is a custom logger class for the project. It uses the Python logging module along with the colorlog module to configure and format log messages with colored output. The class defines methods to log at different levels, such as info, debug, warning, error, and critical.                                                                                                                                                                                                   | src/logger.py     |
| factory.py    | The code snippet provides a Factory class that handles file I/O operations. It supports reading and writing files with different extensions and formats such as Markdown, TOML, JSON, and YAML. The class also includes exception handling for when files cannot be read or written, and it uses a cache to store previously read file content to improve performance.                                                                                                                                    | src/factory.py    |
| model.py      | The provided code snippet is an OpenAI API handler that can generate text for README.md files by converting code to natural language text and using prompts with OpenAI's GPT-3. It includes methods for handling exceptions and uses caching to improve performance. The code is written in Python and uses asyncio for asynchronous processing.                                                                                                                                                         | src/model.py      |
| builder.py    | This code builds a README Markdown file for a codebase. It creates various sections in the file using functions such as creating tables for sub-directories, getting badges for project dependencies, creating a directory tree, and generating a'Getting Started' guide based on the programming language. Finally, it writes the generated markdown to a README file.                                                                                                                                   | src/builder.py    |
| utils.py      | The provided code snippet offers utility functions for the README-AI tool. It includes functions to clone a repository, adjust the maximum number of tokens based on a prompt, count and truncate text to a maximum number of tokens, check if a file or URL is valid, flatten a nested list, and format generated text by removing non-letter characters and extra white space. The code is written in Python and implements commonly used modules such as git, pathlib, and re.                         | src/utils.py      |
| parse.py      | The provided code snippet contains functions for parsing dependency files in various languages such as Python, Go, Rust, and JavaScript. These functions extract the names of packages and libraries from different file formats such as YAML, TOML, and JSON. The parsed dependencies are returned as a list of strings. The code uses regular expressions and external libraries such as `toml` and `yaml` for parsing the files.                                                                       | src/parse.py      |
| main.py       | This code generates a README.md file for a given code repository using OpenAI's GPT APIs. It extracts dependencies and file text from the repository using a scanner, generates code-to-text and additional markdown text using GPT, and formats the texts to markdown. The final markdown output is then built using a builder and written to the specified output path.                                                                                                                                 | src/main.py       |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

1. Clone the README-AI repository:
```sh
git clone https://github.com/eli64s/README-AI
```

2. Change to the project directory:
```sh
cd README-AI
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using README-AI

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
