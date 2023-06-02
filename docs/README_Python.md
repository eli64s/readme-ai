
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3 align="center">📍 Empower Your Readme with README-AI-Your Virtual Writing Assistant</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />

<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [🖥 Installation](#-installation)
  - [🤖 Using README-AI](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

README-AI is a Python-based CLI tool that generates comprehensive README Markdown files for Git repositories using OpenAI's GPT language model APIs. The core functionalities of the project include preprocessing the input codebase, extracting dependencies, generating natural language text summaries, and building a complete README file. The project automates the time-consuming task of creating comprehensive documentation for code projects, enabling developers to focus on building and improving their software.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | README-AI follows a clear and organized structure with separate directories for scripts, configuration files, source code, and tests. The Makefile provides various commands for managing the project and automating repetitive tasks. |
| **📝 Code Documentation** | The codebase has extensive and helpful documentation and comments. The README file provides an overview of the project and detailed instructions on how to set up and run the program. |
| **🧩 Dependency Management** | The codebase uses Conda and pip to manage dependencies, with the option to create a Conda or virtual environment using the provided Makefile and setup scripts. |
| **♻️ Modularity and Reusability** | The codebase uses various design patterns such as the factory pattern to handle different file types and the logger pattern to provide customized logging. The code is modular and reusable, allowing for easy expansion and maintenance. |
| **✔️ Testing and Quality Assurance** | The codebase includes a dedicated directory for tests and a Makefile command for generating a coverage report using pytest and coverage. The scripts/test.sh file runs the tests and ensures that the test coverage stays above 90%. |
| **⚡️ Performance and Optimization** | The codebase uses the asyncio library for asynchronous tasks and includes caching mechanisms to reduce the number of API requests made. The codebase also uses profiling tools like SnakeViz to optimize performance. |
| **🔒 Security Measures** | The codebase uses secure HTTP requests and API keys to access the OpenAI GPT APIs. Security vulnerabilities in dependencies are minimized through the use of Conda and virtual environments. |
| **🔄 Version Control and Collaboration** | The codebase uses Git for version control and includes a setup script that checks for the presence of Git and sets up a repository. The codebase includes a CONTRIBUTING.md file, indicating that it welcomes contributions from other developers. |
| **🔌 External Integrations** | The codebase integrates with OpenAI's GPT language model APIs to generate natural language text. It also integrates with Docker for containerization. |
| **📈 Scalability and Extensibility** | The codebase is flexible and modular, allowing for easy expansion and modification. The use of design patterns and libraries like asyncio and loguru make the codebase scalable and extensible. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

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
├── docs
│   ├── README_C.md
│   ├── README_FastAPI.md
│   ├── README_FastAPI_Redis.md
│   ├── README_GITLAB.md
│   ├── README_Go.md
│   ├── README_Go_Bash.md
│   ├── README_Java.md
│   ├── README_JavaScript.md
│   ├── README_JavaScript_GPT.md
│   ├── README_Kotlin.md
│   ├── README_LangChain.md
│   ├── README_MLOps.md
│   ├── README_PyFlink.md
│   ├── README_Python.md
│   ├── README_Python_ML.md
│   ├── README_RUST_C.md
│   ├── README_React.md
│   ├── README_Rust.md
│   ├── README_TypeScript.md
│   └── imgs
│       ├── closed_docs.png
│       ├── features.png
│       ├── header.png
│       ├── misc.png
│       ├── open_docs.png
│       ├── overview.png
│       ├── setup.png
│       └── tree.png
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

9 directories, 69 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Module     |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | This code snippet sets up a Docker image for running a Python application. It installs the required packages using pip, exposes port 80 for external access, and sets the command to run the main.py file when the container launches with the host specified as 0.0.0.0.                                                                                                                                                                                                                           | Dockerfile |
| Makefile   | This Makefile provides various commands for managing a Python project called README-AI. The `clean` command removes unnecessary files, the `style` command formats the code according to various style conventions, and the `conda` and `venv` commands create either a Conda environment or Python virtual environment, each with the required dependencies. The `profile` command runs cProfile on the `main.py` script and the `snakeviz` command runs SnakeViz on the resulting profiling data. | Makefile   |
| setup.py   | This code is a setup script for the README-AI package, which is a CLI tool that generates comprehensive README Markdown files using OpenAI's GPT language model APIs. The script installs required packages and sets up dependencies for development and testing, providing additional functionality for documentation, style, and testing. Finally, it defines project details such as author, version, keywords, and project URLs for documentation and source code.                              | setup.py   |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                | Module           |
|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This bash script activates a conda environment called "readme_ai" and runs a Python script called "main.py" located in the "src" directory. It also sets the "pipefail" option and exports environment variables, if needed.                                                                                                                                                                           | scripts/run.sh   |
| clean.sh | The code snippet is a Bash script that removes various types of files and directories. It removes backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, and benchmarks. It also removes specific files such as raw data files, logs, and output files.                                                                                                 | scripts/clean.sh |
| test.sh  | The provided code snippet is a bash script that activates a Conda environment and generates a coverage report for Python code using pytest and coverage. It excludes certain directories and files from the coverage report, removes generated files, caches, and local directories to clean up the workspace. The coverage report is shown in the terminal and fails if the coverage falls below 90%. | scripts/test.sh  |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module         |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | This code snippet is a Bash script that sets up a Python environment named'readme_ai' with necessary packages and dependencies for a project. It checks for the existence of the environment and installs it if it doesn't exist. The script also checks for necessary installations such as Git, Conda, Python version, and required packages. Additionally, it installs a tree command if it's not already installed. A welcome message is displayed at the beginning of the script, and the script concludes by providing instructions for activating the environment. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module            |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | The provided code snippet handles preprocessing of an input codebase by cloning or copying a repository to a temporary directory, extracting its contents, and searching for software and packages used by the codebase. It includes functions for cloning a remote repository, extracting file extensions, mapping extensions to programming language names, and parsing various types of dependency files. There is also a function for returning additional dependencies and a function for getting the contents of a repository from a URL or local path. | src/preprocess.py |
| conf.py       | The provided code snippet defines configuration constants for the README-AI application using data classes and helper functions. It contains data classes for API, Git, Markdown, Paths and Prompts configuration, and a ConfigHelper class to manage the application's helper configuration files. It also includes functions to load configuration constants from TOML files.                                                                                                                                                                               | src/conf.py       |
| logger.py     | The provided code defines a custom logger module using the loguru library. It offers various logging functionalities such as info, debug, error, warning, and critical log levels. The logger can also handle exceptions and tracebacks and provides a success log level. It also has the ability to log at a custom log level.                                                                                                                                                                                                                               | src/logger.py     |
| factory.py    | The code provides a factory module for reading and writing different file types, including markdown, TOML, JSON, and YAML files. It includes methods for reading and writing files, as well as methods for getting the appropriate action for a given file extension and action type. The code also includes error-handling classes for exceptions raised when a file cannot be read or written.                                                                                                                                                              | src/factory.py    |
| model.py      | The provided code snippet is an OpenAI API handler for generating natural language text for a README.md file, which can convert code to text and generate text using prompts. It includes functions for creating a summary, handling HTTP errors, and caching previous API requests. Additionally, it has an option to close the HTTP client once it is no longer needed.                                                                                                                                                                                     | src/model.py      |
| builder.py    | The provided code snippet builds a README Markdown file for a codebase, using metadata from a configuration file and information from the user's repository. It generates badge icons for dependencies, creates a directory tree structure, and creates markdown tables for each sub-directory in the project. It also includes a setup guide based on the top used language in the project and code summaries generated for each file in the repository.                                                                                                     | src/builder.py    |
| utils.py      | This code snippet provides utility functions for the README-AI project. It includes functions to convert an IPython Notebook file to a Python script, clean up a sentence generated by OpenAI's GPT API, count the number of tokens in a text string, truncate a string based on the number of tokens, and check if a string is a valid URL.                                                                                                                                                                                                                  | src/utils.py      |
| parse.py      | The provided code snippet contains various parsing functions that extract dependencies from different types of files used in various programming languages. These functions utilize regular expressions and file handling to extract package names from files such as Conda environment files, Pipfiles, Cargo.toml, package.json, Go module files, Gradle/Maven files, and Docker Compose files. The parsed dependencies are returned as a list of strings.                                                                                                  | src/parse.py      |
| main.py       | The code snippet is a Python program that generates a README.md file for a repository using OpenAI's GPT APIs. It uses typer for the command-line interface, asyncio for asynchronous tasks, and several other modules for preprocessing, model handling, and building the final README file. It extracts dependencies and generates summary text for code files and chat text for repository overview, features, and slogan.                                                                                                                                 | src/main.py       |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

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

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] ...


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
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
