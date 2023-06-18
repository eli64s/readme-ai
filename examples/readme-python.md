
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
readme-ai
</h1>
<h3 align="center">📍 Transforming your README into a work of AI art!</h3>
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
  - [🤖 Using readme-ai](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

README-AI is a tool that generates high-quality README files for software projects using OpenAI's GPT language model APIs. It includes functionalities for analyzing local or remote Git repositories, extracting file and dependency information, and creating a README file in Markdown format. It also provides various configuration options and a customizable file input/output factory for different file types. The tool saves developers time and effort by automating the creation of project documentation and providing language model-generated summaries and prompts.

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
│       ├── contribute.png
│       ├── features.png
│       ├── header.png
│       ├── license.png
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

9 directories, 70 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module     |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | This code snippet creates a Docker container with Python 3.9 and sets the working directory to /app. It copies the current directory contents into /app, installs required packages using pip, exposes port 80 to the outside world, and runs the main.py file located in the /app/src directory.                                                                                                                                                                                                                                         | Dockerfile |
| Makefile   | This Makefile provides several commands to clean unnecessary files, execute style formatting, create a Conda or Python virtual environment, run cProfile on a CLI script, and run SnakeViz. The style command uses several Python formatting tools, while the clean command executes a separate shell script. The Conda and Python virtual environment commands both install requirements from a requirements.txt file. The profile command generates a profile output file and the snakeviz command visualizes this file using SnakeViz. | Makefile   |
| setup.py   | This code sets up the configuration and dependencies for the README-AI package. It includes packages for documentation, styling, testing and a CLI tool that generates comprehensive README files powered by OpenAI's GPT language model APIs. It also includes project descriptions, URLs, and keywords.                                                                                                                                                                                                                                 | setup.py   |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                | Module           |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This bash script sets some options for error handling, exports environment variables, activates a conda environment, and runs a Python script located in the specified source directory. It is a useful automation tool for running Python scripts with specified requirements in a streamlined manner.                                                                                | scripts/run.sh   |
| clean.sh | The provided code snippet is a Bash script that removes various types of files and directories commonly associated with Python development and other build artifacts. It first finds and deletes backup files and Python cache files, then removes cache directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files such as logs and raw data files. | scripts/clean.sh |
| test.sh  | This Bash script sets up and activates the "readme_ai" Conda environment. It then generates a coverage report for the files in the "src" directory while excluding the "tests" directory and "__init__.py" file. The script also removes some files and folders, such as "__pycache__" and ".coverage".                                                                                | scripts/test.sh  |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module         |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | The provided code snippet is a bash script that sets up a conda environment for running a Python program. It checks if the required software (Git, Conda, Python, and the necessary packages) is installed and installs them if needed. It also creates a new conda environment, activates it, and installs the required packages using pip. Finally, it deactivates the environment and provides a message about the setup being complete. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module            |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | The provided code snippet handles preprocessing of a codebase and includes a class for creating a temporary directory, a class for analyzing a local or remote git repository, and a dictionary of callable file parser methods for extracting dependency file contents from the analyzed repository. The `RepositoryParserWrapper` class utilizes the `RepositoryParser` class to get unique contents, file contents, and dependencies. The `conf` module is used for configuration, and other modules are imported for various functionalities. | src/preprocess.py |
| conf.py       | The provided code snippet defines several data classes to store configuration constants for README-AI, an application that generates README files for software projects. The classes are used to store configurations for the OpenAI API, Git repositories, Markdown formatting, file paths, and LLM prompts. The ConfigHelper class is used to load configuration files and dependencies based on the AppConfig dataclass. The load_config function loads a TOML file with configuration constants and returns a dictionary.                     | src/conf.py       |
| logger.py     | The provided code snippet is a custom logger module that uses the loguru library. It has a class called "Logger" that supports various log levels such as info, debug, warning, error, critical, trace, success, and exception. It also has a method for logging messages at a specific level. The logger can be configured with different handlers, such as for displaying log messages on the console or writing them to a file.                                                                                                                | src/logger.py     |
| factory.py    | This code snippet is a file input/output (I/O) factory module that handles different file types such as Markdown, TOML, JSON, and YAML. It contains methods that read and write to different file types, and the appropriate method is selected based on the file type extension. It also includes error handling for issues such as failing to read or write to a file. Additionally, it utilizes a cache to store recently read files for future use.                                                                                           | src/factory.py    |
| model.py      | The provided code snippet defines a Python class for handling OpenAI API calls to generate natural language text. It includes methods for converting code to text and generating text from prompts, as well as an exception handler and a cache for storing previously generated text. The class uses asynchronous programming and implements retrying and rate limiting functionality.                                                                                                                                                           | src/model.py      |
| builder.py    | The provided code snippet is a Python script that generates a README Markdown file for a codebase. It uses various functions to create different sections of the README, including badges, project summary tables, language-specific setup guides, and a directory tree. The resulting README file is saved to the working directory and its path is logged using a custom logger.                                                                                                                                                                | src/builder.py    |
| utils.py      | The provided code snippet contains utility methods for the README-AI tool. It includes functions for cloning a repository, converting an IPython Notebook file to a Python script, counting the number of tokens in a text string, truncating a text string to a maximum number of tokens, adjusting the maximum number of tokens based on the specific prompt, checking if a given string is a valid URL, flattening a nested list, and cleaning and formatting the generated text from the model.                                               | src/utils.py      |
| parse.py      | The provided code snippet contains functions for parsing dependencies from various files, including Docker-compose, Python, Rust, JavaScript, Go, Java, and C/C++. The functions use different parsing techniques, such as regular expressions and parsing libraries like YAML and TOML. The parsed dependencies are returned as a list of strings.                                                                                                                                                                                               | src/parse.py      |
| main.py       | This code snippet generates a README.md file for a repository using OpenAI's GPT APIs. It validates the user's OpenAI API key and repository URL or path. It generates code summaries and natural language text using large language models. It then builds the README file using the generated text and dependencies obtained from the repository.                                                                                                                                                                                               | src/main.py       |

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
