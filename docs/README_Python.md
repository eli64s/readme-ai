
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3 align="center">📍 Upgrade your README game with README-AI!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

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
- [📍Overview](#overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using README-AI](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

README-AI is a Python project that aims to generate high-quality README files for GitHub projects using OpenAI's GPT-3 language model. The project includes various modules for pre-processing, parsing, and formatting code repositories, as well as handlers for generating summary text and building the final README file. By automating the README creation process, README-AI saves time and effort for developers while improving the quality and readability of their project documentation.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Overall Structure and Organization** | The codebase is well-organized with clear separation of concerns between different components and functionalities, utilizing a Makefile and various configuration files to automate setup and testing processes. |
| **📝 Code Documentation** | The codebase includes clear and concise documentation, including comments within the code and separate README files for different components. |
| **🧩 Dependency Management** | The codebase utilizes various dependency management tools such as pip, Conda, and setuptools to manage packages and dependencies for different aspects of the project. |
| **♻️ Code Modularity and Reusability** | The codebase utilizes modular design patterns and a factory module for file I/O to promote code reuse and maintainability. |
| **✅ Testing and Quality Assurance** | The codebase includes thorough testing functionality using pytest and coverage, as well as pre-commit hooks to ensure code quality. |
| **⚡️ Performance and Optimization** | The codebase includes caching functionality for file contents and API responses to improve performance, as well as cProfile and SnakeViz for profiling and optimizing code. |
| **🔒 Security Measures** | The codebase does not include any obvious security measures beyond the use of HTTPS for external API communications. |
| **🔄 Version Control and Collaboration** | The codebase utilizes Git for version control and includes various configuration files to facilitate collaboration and code sharing. |
| **🔌 External Integrations** | The codebase heavily relies on external integrations, particularly OpenAI's GPT-3 API, to generate summary text for code files and generate a README file for the repository. |
| **📈 Scalability and Extensibility** | The codebase includes functionality for parsing dependency files for multiple programming languages and generating summary text for individual files and the entire repository, as well as providing various configuration options for customization and flexibility. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   ├── conf.toml
│   ├── dependency_files.toml
│   ├── ignore_files.toml
│   ├── language_names.toml
│   └── language_setup.toml
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

8 directories, 68 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Conf</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                     |
|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| ignore_files.toml     | The provided code snippet contains a list of file types and directories that should be ignored when parsing repository contents. This includes build artifacts, data files, documentation, images and media, configuration files and credentials, compiled code, version control files, editor and IDE settings, and test and utility files. The aim is to filter out irrelevant files and directories and focus on the important ones.                                                                                                                 | conf/ignore_files.toml     |
| language_names.toml   | The code snippet provides a dictionary of programming language file extensions and their corresponding names. The extensions are mapped to their respective names, such as "py" for Python and "java" for Java. This can be used for various purposes, such as file type detection or displaying language names in an interface.                                                                                                                                                                                                                        | conf/language_names.toml   |
| conf.toml             | The provided code snippet includes various prompts and parameters for generating a README file for a GitHub project using an OpenAI API. The prompts include asking for a summary of the code script, insights into the user-centered design elements and unique features of the project, and a slogan for the project. Parameters include API key, engine, repository URL, file paths, and markdown template. The generated README includes an overview, features, project structure, modules, installation instructions, and contribution guidelines. | conf/conf.toml             |
| dependency_files.toml | The provided code snippet lists the names of various dependency files for different programming languages including C/C++, Go, Java, Python, Rust, Ruby, Clojure, Elixir, JavaScript/Node.js, TypeScript, PHP, Swift, Kotlin, Dart/Flutter, R, Shell, Scala, Groovy, Lua, Julia, Haskell, C#, F#, Objective-C, and Perl. These files are typically used for package management, build automation, and/or project configuration.                                                                                                                         | conf/dependency_files.toml |
| language_setup.toml   | The code snippet provides a dictionary of language-specific commands for setting up and running programs. For each language, it includes the necessary commands for installation, compilation, and execution of the main file. The provided commands cover a wide range of programming languages, including C, Java, Python, Ruby, and many others.                                                                                                                                                                                                     | conf/language_setup.toml   |

</details>

<details closed><summary>Root</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                    | Module                  |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| .pre-commit-config.yaml | The provided code snippet is a pre-commit configuration file that specifies various hooks to be run on code before committing to a repository. These hooks include checking for large files, correct syntax, JSON formatting, and whitespace errors, among others. Additionally, the file specifies the use of the Black code formatter.                   | .pre-commit-config.yaml |
| Dockerfile              | The code snippet is a Dockerfile that sets up a Python 3.9 runtime environment for a container. It installs required packages listed in requirements.txt using pip, exposes port 80, and sets the command to run the main.py file with the argument "--host=0.0.0.0". This will allow the container to listen on port 80 and respond to incoming requests. | Dockerfile              |
| Makefile                | This code snippet provides Makefile commands for a project called README-AI. The commands include cleaning unnecessary files, executing style formatting, creating a Conda or virtual environment, running cProfile on a CLI script, and running SnakeViz on a profile.out file. The code also includes a help command to display all available commands.  | Makefile                |
| pyproject.toml          | The provided code snippet contains configuration settings for various Python development tools. It includes settings for Black formatting, Flake8 linting, iSort sorting, Pytest testing, and Pytest coverage. These settings specify options such as line length, excluded directories, test file paths, and coverage exclusion patterns.                 | pyproject.toml          |
| setup.py                | The provided code snippet is a setup script for the README-AI package. It defines the required and optional packages, project details such as name, version, description, author, and URLs. It also includes classifiers and keywords relevant to the project. The script uses setuptools to install the package and its dependencies.                     | setup.py                |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                  | Module           |
|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This Bash script sets some options and activates a Conda environment named "readme_ai" before running a Python script located at "src/main.py". It also includes commented-out code for exporting environment variables if needed.                                                                                                                                                                                       | scripts/run.sh   |
| clean.sh | The provided code snippet is a Bash script that removes various types of files and directories from the current working directory. It deletes backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files such as raw data, logs, and output files. The script is designed to clean up the directory and remove unnecessary or temporary files. | scripts/clean.sh |
| test.sh  | This code snippet activates a conda environment, sets directories to include/exclude from a coverage report, generates the coverage report using pytest, and removes certain files/folders. The coverage report displays missing lines and fails if coverage is under 90%. The code removes pycache, pytest_cache,.coverage and any local directories created by tests.                                                  | scripts/test.sh  |

</details>

<details closed><summary>Setup</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                 |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| setup.sh         | The provided code snippet is a Bash script that sets up a conda environment for a Python project called README-AI. It checks if Git, Conda, and the required version of Python are installed, installs the'tree' command if it's not already installed, creates the'readme_ai' conda environment, activates it, installs required packages using pip, and deactivates the environment. The script provides helpful messages throughout the process and is compatible with various operating systems. | setup/setup.sh         |
| environment.yaml | HTTP 429 error when fetching summary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                | setup/environment.yaml |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module            |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | The provided code snippet handles preprocessing of a codebase by cloning or copying a repository to a temporary directory, extracting the contents from the cloned repository, searching for dependency files in the repository, and extracting their metadata. It also extracts the repository name from a URL or local path and returns a list of additional dependencies. The code uses various utility functions and parsers for different file types to accomplish these tasks. | src/preprocess.py |
| conf.py       | The code snippet defines various data classes that contain configuration constants for the README-AI application, including OpenAI API, Git, Markdown, Paths, and Prompts configurations. It also includes a helper class and functions for loading and reading these configurations from TOML files. The code uses the dacite library for parsing the TOML files into the appropriate data class objects.                                                                           | src/conf.py       |
| __init__.py   | This code snippet defines a function that takes in a string and returns a reversed version of that string. The function accomplishes this by iterating over the characters in the string in reverse order and appending them to a new string. The new, reversed string is then returned as the output of the function.                                                                                                                                                               | src/__init__.py   |
| logger.py     | The provided code snippet defines a custom logger module using the Loguru library. The Logger class includes methods for logging at different levels (info, debug, warning, error, critical, trace, success) and an exception method. It also allows customization of the logger's name and level, and provides a default configuration for the logger's handlers.                                                                                                                   | src/logger.py     |
| factory.py    | The provided code snippet is a file I/O factory module that handles different file types such as Markdown, TOML, JSON, and YAML. It provides methods for reading and writing files of these formats, and raises exceptions for errors encountered during file operations. The module also includes a cache to improve performance by storing file contents in memory.                                                                                                                | src/factory.py    |
| model.py      | The provided code snippet is an OpenAI API handler that generates summary text for files in a repository using the GPT-3 language model. It includes functions for fetching and caching responses from the OpenAI API, as well as generating summary text for individual files. The code also provides a function for generating a summary of the entire repository using a given prompt.                                                                                            | src/model.py      |
| builder.py    | HTTP 429 error when fetching summary.                                                                                                                                                                                                                                                                                                                                                                                                                                                | src/builder.py    |
| utils.py      | The provided code snippet contains two utility methods for the README-AI project. The first method,'format_sentence', cleans up a sentence generated by OpenAI's GPT API by removing non-letter characters, extra white space, and hyphens, and replacing multiple consecutive spaces with a single space. The second method,'valid_url', checks if a given string is a valid URL using regular expressions.                                                                         | src/utils.py      |
| parse.py      | The provided code snippet contains functions for parsing dependency files for different programming languages, including Python, Rust, JavaScript/TypeScript, Go, Java, and C/C++. Each function extracts the dependencies from a specific type of file and returns a list of the package names. The code uses regular expressions and file handlers to read and parse the files.                                                                                                    | src/parse.py      |
| main.py       | The provided code snippet generates a README.md file for a repository using OpenAI's GPT APIs. The code includes functions for setting the OpenAI API key, validating the repository URL or path, and generating summary text for code files using GPT-3. The program takes command-line inputs for the API key, output file path, and repository URL or path.                                                                                                                       | src/main.py       |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

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
# [INSERT-COMMAND-FOR-TESTS]
```

<hr />


## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


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

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---

