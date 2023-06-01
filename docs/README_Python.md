
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3 align="center">📍 README-AI: Your code's personal assistant!</h3>
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
- [📍Overview](#-overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

README-AI is a Python package that automates the creation of comprehensive README Markdown files for software projects using OpenAI's GPT language model APIs. Core functionalities include extracting dependencies and code summaries, generating badge icons, creating a directory tree structure, markdown tables for each sub-directory, and setup guides for projects. This package adds value by saving time and effort for developers who would otherwise have to manually create these README files, and by improving code documentation and project organization.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a consistent structure with separate directories for scripts, configuration files, source, and setup-related files. The Makefile provides a convenient command interface for various functionalities. |
| **📝 Code Documentation** | The codebase includes extensive documentation using comments, docstrings, and Markdown files. The README file provides detailed instructions on how to use the application, while the code includes function-level documentation for all non-trivial functions. |
| **🧩 Dependency Management** | The codebase utilizes various dependency management tools such as pip, conda, and Docker. The setup script and environment configuration files enable seamless environment setup and dependency installation. |
| **♻️ Modularity and Reusability** | The codebase follows modularity and encapsulation principles, with clearly defined interfaces between modules. Reusable components such as file handling, logging, and configuration utilities are implemented separately for easier reuse across different projects. |
| **✅ Testing and Quality Assurance** | The codebase follows good testing practices with comprehensive unit tests, coverage reports, and hooks to check code formatting, styling, and syntax. The pre-commit hook includes a variety of checks to ensure code quality and consistency. |
| **⚡️ Performance and Optimization** | The codebase includes several performance optimizations such as caching, lazy loading, and rate limiting to prevent API overuse. |
| **🔒 Security Measures** | The codebase does not feature any security-related components or concerns, except for rate limiting to prevent API overuse. |
| **🔄 Version Control and Collaboration** | The codebase follows Git's best practices with detailed commit messages, feature branches, pull requests, and code reviews. The repository also features Continuous Integration (CI) using GitHub Actions. |
| **🔌 External Integrations** | The codebase relies heavily on external integrations such as OpenAI's GPT-3 API, Docker, and GitHub Actions. |
| **📈 Scalability and Extensibility** | The codebase includes several abstractions and interfaces that can be extended or rewritten to support additional programming languages and dependencies. The code utilizes various design patterns and principles such as Factory pattern, dependency injection, and separation of concerns.

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

## 💻 Modules

<details closed><summary>Conf</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                     |
|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| ignore_files.toml     | The provided code snippet defines files and directories to be ignored when parsing repository contents. It includes a list of specific file extensions, directories, and file names that will be ignored. The purpose is to filter out irrelevant files and focus on the relevant ones.                                                                                                                                                                                                                                                                                                                                                                         | conf/ignore_files.toml     |
| language_names.toml   | The provided code snippet maps file extensions to their corresponding programming language names using a dictionary-like structure. It covers a wide range of programming languages and file types, from assembly to Python to Dockerfile. The mappings are stored in a variable called "language_names".                                                                                                                                                                                                                                                                                                                                                       | conf/language_names.toml   |
| conf.toml             | The provided code snippet consists of configuration parameters for the OpenAI API, local and remote repository details, file paths, and prompts for generating Markdown templates. The Markdown template includes a header, badges, table of contents, overview, features, project structure, modules, getting started guide, future development, contributing guidelines, license, and acknowledgments sections. The prompts are designed to elicit responses from users regarding project summaries, key characteristics, design patterns, architectural decisions, and other relevant elements. The Markdown template is generated based on these responses. | conf/conf.toml             |
| dependency_files.toml | The code snippet provides a list of all the common programming language dependency file names, including C/C++, Go, Java, Python, Rust, Ruby, Clojure, Elixir, JavaScript/Node.js, TypeScript, PHP, Swift, Kotlin, Dart/Flutter, R, Shell, Scala, Groovy, Lua, Julia, Haskell, C#, F#, Objective-C, Matlab, Perl, and Docker. These file names are used for package management, build automation, and dependency resolution in software development projects.                                                                                                                                                                                                   | conf/dependency_files.toml |
| language_setup.toml   | The provided code snippet offers a set of build and run instructions for various programming languages, allowing developers to quickly and easily compile and execute their code. Each language has its respective set of commands, including installation of dependencies and running the compiled app.                                                                                                                                                                                                                                                                                                                                                        | conf/language_setup.toml   |

</details>

<details closed><summary>Root</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                        | Module                  |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| .pre-commit-config.yaml | The code snippet provides a pre-commit configuration file that specifies a list of hooks to be executed before committing code changes. These hooks include checking for large files, syntax errors, trailing whitespaces, and more. The file also includes the use of the code formatter, Black, to format the code before committing.                                                                                        | .pre-commit-config.yaml |
| Dockerfile              | This code snippet sets up a Docker container with a Python 3.9 runtime environment. It sets the working directory to /app, adds the current directory contents to the container, copies the requirements file to the working directory, installs the required packages using pip, exposes port 80 to the host machine, and runs a main.py script with specified arguments when the container launches.                         | Dockerfile              |
| Makefile                | The provided code snippet is a Makefile that includes commands for various functionalities of README-AI. These functionalities include cleaning unnecessary files, executing style formatting, creating conda and virtual environments, running cProfile on the CLI script, and running SnakeViz on the profile.out file. The Makefile also includes a help command that lists all available commands with their descriptions. | Makefile                |
| pyproject.toml          | The provided code snippet contains configuration settings for various Python development tools. It includes settings for Black formatting, Flake8, iSort, Pytest, and Pytest coverage. These settings define things like line length, file inclusion/exclusion, testing paths, and more, to help maintain code quality and consistency.                                                                                        | pyproject.toml          |
| setup.py                | This code is a setup script for the README-AI package which generates comprehensive README Markdown files using OpenAI's GPT language model APIs. The script installs necessary dependencies, sets up project configurations, and provides project metadata and URLs. Additionally, the script allows for extra dependencies to be installed for development and testing purposes.                                             | setup.py                |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                             | Module           |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This Bash script sets some options for error handling and then activates a conda environment called "readme_ai" before running a Python script located in the "src" folder called "main.py". Any necessary environment variables can be exported beforehand.                                                                                                                                        | scripts/run.sh   |
| clean.sh | The code snippet is a Bash script that removes various files and directories related to programming projects. It deletes backup and cache files for Python, cache directories for various text editors, and build artifacts, pytest cache, and benchmarks. It also removes specific files such as logs and raw data.                                                                                | scripts/clean.sh |
| test.sh  | This code snippet activates a conda environment, sets directories to include/exclude in a coverage report, generates a coverage report using pytest, and removes certain files/folders. The coverage report includes missing lines and fails if coverage is below 90%. The files/folders removed include __pycache__,.pytest_cache,.coverage, and any local directories within the tests directory. | scripts/test.sh  |

</details>

<details closed><summary>Setup</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module                 |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| setup.sh         | The provided code snippet is a bash script used for setting up a conda environment named'readme_ai' with Python 3.8 and installing required packages using pip. It checks if git, conda, and the required Python version are installed and if the'readme_ai' environment already exists. If not, it creates a new environment and installs necessary dependencies. Finally, it activates the environment and provides instructions for future use. Additionally, it installs the'tree' command if it's not already installed. | setup/setup.sh         |
| environment.yaml | The code snippet provides a basic configuration file for a Conda environment called "base". The environment includes Python version 3.9 up to 3.12 and pip as a dependency manager. The channels utilized for package installation are the default and conda-forge channels.                                                                                                                                                                                                                                                  | setup/environment.yaml |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module            |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | This code snippet handles preprocessing of input codebases by cloning or copying a repository to a temporary directory, extracting its contents, and searching for dependency files to extract metadata. It also maps file extensions to programming language names, provides file parsers for various file types, and returns a list of additional dependencies including Docker and GitHub Actions.                                                                                                                                                                                                  | src/preprocess.py |
| conf.py       | The code provides configuration constants for the README-AI application. It includes data classes for API, Git, Markdown, Paths, and Prompts configuration. The ConfigHelper class provides helper configuration files and loads them during initialization. The load_config and load_config_helper functions load the TOML files and create instances of AppConfig and ConfigHelper classes respectively.                                                                                                                                                                                             | src/conf.py       |
| __init__.py   | The code snippet is a function that takes an array of numbers and returns an object containing the sum, average, minimum, and maximum values of the array. It uses the reduce method to calculate the sum, and the Math object to find the minimum and maximum values. The average is calculated by dividing the sum by the length of the array.                                                                                                                                                                                                                                                       | src/__init__.py   |
| logger.py     | The provided code snippet contains a custom logger module using loguru for README-AI. The Logger class is a singleton object with various logging methods such as info, debug, warning, error, critical, trace, success, exception, and log. The logger is configured to colorize output and display relevant information such as name, function, and line number.                                                                                                                                                                                                                                     | src/logger.py     |
| factory.py    | This code snippet is a file input/output (I/O) factory module that handles various file types such as Markdown, TOML, JSON, and YAML. It defines a FileHandler class that reads and writes files using appropriate methods based on their file extension. It also includes exception classes for handling errors during file read and write operations and a cache to store previously accessed files to improve performance.                                                                                                                                                                          | src/factory.py    |
| model.py      | The provided code snippet is an OpenAI API handler for generating text for the README.md file. It contains methods for converting code to natural language text, generating summaries for prompts using OpenAI's GPT-3, and handling errors that may occur during API calls. The handler also features a cache for storing generated text and a rate limiter to prevent exceeding API usage limits.                                                                                                                                                                                                    | src/model.py      |
| builder.py    | The provided code snippet builds a README Markdown file for a codebase by extracting project dependencies and code summaries from the repository, generating badge icons for each dependency, creating a directory tree structure, markdown tables for each sub-directory, and a setup guide for the project based on the top-used language. The code also includes helper functions to format badges, create tables, and parse the module field to create additional columns in the summary table. Finally, the code writes the generated Markdown file to the README file path and logs the process. | src/builder.py    |
| utils.py      | The code snippet provides utility methods for the README-AI project. It includes a function to convert an IPython Notebook file to a Python script, functions to clean up and truncate text, and a function to check if a given string is a valid URL. The code also imports necessary libraries and defines constants related to text encoding.                                                                                                                                                                                                                                                       | src/utils.py      |
| parse.py      | The code snippet provides functions to extract dependencies from various types of files for different programming languages, including Python, Rust, JavaScript/TypeScript, Go, Java, C/C++, and Docker. The functions parse specific file types such as conda environment files, Cargo.toml files, package.json files, etc. The extracted dependencies are returned as a list. The code also imports and utilizes other modules such as "re" for regular expressions, "typing" for type hints, "factory" for file handling, and "logger" for logging.                                                 | src/parse.py      |
| main.py       | The code generates a README.md file for a user's repository using OpenAI's GPT APIs. It validates and sets the OpenAI API key provided by the user, as well as validates the repository URL or path provided. It then generates summary text for code files and uses prompts and OpenAI's GPT-3 to generate additional text for the README file. The resulting README file is created according to user-specified output settings.                                                                                                                                                                     | src/main.py       |

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

`[📌  INSERT-REFERENCES-AND-RESOURCES]`


---

