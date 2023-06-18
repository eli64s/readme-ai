
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
readme-ai
</h1>
<h3 align="center">📍 Readme-ai: Empowering your coding journey with intelligent documentation.</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

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
- [💫 Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

README-AI is a Python tool that generates comprehensive README Markdown files using OpenAI's GPT language model APIs. The tool analyzes a local or remote git repository, tokenizes the content of files and maps file extensions to their programming languages, extracts dependencies through file parsers, and generates text for README.md files using prompts and GPT-3. The tool saves time and effort for developers by automating the tedious task of writing README files and helps to ensure that project documentation is informative, standardized, and easy to read.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a standard Python project structure with a clear separation of concerns between modules and directories. The Makefile provides convenient automation for common tasks. |
| **📝 Code Documentation** | The codebase contains thorough documentation for each module, class, and function. The documentation follows the Google docstring format and includes usage examples. |
| **🧩 Dependency Management** | The codebase uses Conda and pip to manage dependencies, with a clear separation of production and development dependencies. The setup script installs all required packages and specifies the API key for OpenAI's GPT-3. |
| **♻️ Modularity and Reusability** | The codebase is highly modular and follows the SOLID principles. Classes and functions are well-encapsulated, reusable, and have single responsibilities. |
| **✔️ Testing and Quality Assurance** | The codebase includes unit tests for each module and integration tests for the entire toolchain. The test suite uses pytest and coverage and is fully automated with the Makefile. |
| **⚡️ Performance and Optimization** | The codebase uses caching and parallel processing to improve performance in several areas, such as fetching repository information and generating Markdown files. Code profiling is available with the Makefile and SnakeViz. |
| **🔒 Security Measures** | The codebase does not deal with sensitive information, but proper error handling and exception handling are used to prevent potential security risks. The API key for OpenAI's GPT-3 is kept secret via configuration files. |
| **🔄 Version Control and Collaboration** | The codebase uses Git for version control and has a clear workflow for contributions and pull requests. The repository is well-organized with descriptive commit messages and branch naming conventions. |
| **🔌 External Integrations** | The codebase uses external integrations with OpenAI's GPT-3 language model and the conda package manager. The integrations are well-documented and follow best practices. |
| **📈 Scalability and Extensibility** | The codebase is designed to be scalable and extensible. It can handle multiple repositories at once and can be integrated with other tools and APIs. The code follows design patterns that allow for easy extension and customization. |

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
├── examples
│   ├── imgs
│   │   ├── closed_docs.png
│   │   ├── contribute.png
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

9 directories, 71 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                     | Module     |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | This code defines a Docker container that sets the working directory to /app, adds all the contents of the current directory to the container, and installs required Python packages using pip. Port 80 is made available outside the container, and the main.py file is launched when the container starts up.                                                                             | Dockerfile |
| Makefile   | This code provides a Makefile with several commands to automate common tasks in a Python project. These tasks include formatting the code style, cleaning unnecessary files, creating a Conda or Python virtual environment, running cProfile for profiling purposes, and visualizing profiling results with SnakeViz. The Makefile has a "help" command that lists all available commands. | Makefile   |
| setup.py   | The code is a setup script for the README-AI package. It installs required packages, defines extra packages for developers and tests, and includes project metadata such as the name, version, author, and license. It also specifies project keywords and URLs. The package generates comprehensive README Markdown files using OpenAI's GPT language model APIs.                          | setup.py   |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module           |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This Bash script sets options to exit on errors and pipe failures. It activates a Conda environment called "readme_ai" using the `conda activate` command and executes a Python script named "main.py" located in the "src" directory using the `python` command. Any environment variables that need to be exported can be added to the provided section.                                                                                                        | scripts/run.sh   |
| clean.sh | This code snippet is a Bash script that aims to clean up a project directory by removing various temporary or unnecessary files and directories. It deletes backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files such as raw data, log, out, and rdb files. The script uses the'find' command to identify the files and directories to remove and the'rm' command to delete them. | scripts/clean.sh |
| test.sh  | This code snippet is a Bash script used to generate a coverage report for a Python project using Conda and pytest. It specifies the directories to include and exclude from the report, generates the report, and sets a minimum coverage limit. Additionally, it removes unnecessary files and folders after the report is generated.                                                                                                                            | scripts/test.sh  |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Module         |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | This code snippet sets up a conda environment named'readme_ai' with Python 3.8, installs required dependencies from a requirements.txt file via pip, and adds the Python path from the conda environment to PATH. It also checks for the existence of necessary tools such as Git, conda, and a compatible version of Python. Lastly, it installs the tree command if it's not already installed. The script provides useful messages throughout the process to guide the user. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module            |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | The code snippet provides classes and methods to analyze a local or remote git repository by generating a Pandas DataFrame of file information and extracting dependencies. It also tokenizes the content of files and maps file extensions to their programming languages. Additionally, it includes file parsers for various dependency files such as Gradle, Maven, and Pipfile.                                                                                    | src/preprocess.py |
| conf.py       | The provided code snippet contains data classes for storing configuration constants used by README-AI. It includes configurations for the OpenAI API, repository, markdown, file paths, and LLM prompts. The `ConfigHelper` class provides helper functions for loading configuration files, while `load_config` and `load_config_helper` functions are used for loading TOML configuration files into the `AppConfig` and `ConfigHelper` classes, respectively.       | src/conf.py       |
| logger.py     | This code provides a custom logger class for a Python project, which allows developers to log messages at different levels (info, debug, warning, error, and critical). It also uses the colorlog library to add color to the output based on the level of the message. The class is designed as a singleton to ensure only one instance of the logger is created.                                                                                                     | src/logger.py     |
| factory.py    | This code snippet defines a Factory class for handling file I/O operations. It provides methods for reading and writing to different file formats including Markdown, TOML, JSON and YAML. The class includes a caching mechanism to improve performance and raises custom exceptions for file read and write errors.                                                                                                                                                  | src/factory.py    |
| model.py      | The provided code is an OpenAI API handler that generates text for README.md files. It includes methods for converting code to natural language text and for generating text using prompts and OpenAI's GPT-3. The handler includes exponential backoff logic for rate limiting and custom exception handling for HTTP and API errors.                                                                                                                                 | src/model.py      |
| builder.py    | This code snippet builds a README Markdown file for a codebase by creating various sections of the file and incorporating the necessary information. It uses functions to create Markdown tables, generate a directory tree, and format the badges for project dependencies, among other things. The final README file is saved to the specified path and logging is used to output information about the process.                                                     | src/builder.py    |
| utils.py      | The provided code snippet contains utility functions to be used with the README-AI tool. These functions include cloning a Git repository, converting an IPython Notebook file to a Python script, manipulating text by counting or truncating tokens, validating files and URLs, and flattening lists. There is also a function to clean and format generated text from a model by removing non-letter characters and extra white space.                              | src/utils.py      |
| parse.py      | The provided code snippet contains functions for parsing different types of dependency files for various programming languages. These include Docker Compose, Conda environment files, Pipfiles, Pyproject.toml files, requirements.txt files, Cargo.toml files, package.json files, yarn.lock files, Go mod files, Gradle files, Maven files, CMake files, configure.ac files, and Makefile.am files. The functions extract and return the names of the dependencies. | src/parse.py      |
| main.py       | The code snippet generates a README.md file for a repository using OpenAI's GPT APIs. It includes functions for validating the user's API key and repository URL/path, extracting dependencies and file text using a scanner, and generating code summary, slogan, overview, and features using GPT. The code also updates the configuration file and builds the actual README file.                                                                                   | src/main.py       |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

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

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] [📌  Task 4: Fix Bug A]


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

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
