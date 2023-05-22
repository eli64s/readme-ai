
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3 align="center">📍 Unlock the Power of AI: Read Anywhere with README-AI!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="Pytest" />

<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/spaCy-09A3D5.svg?style=for-the-badge&logo=spaCy&logoColor=white" alt="spaCy" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
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

The README-AI GitHub project provides a powerful and intuitive tool for developers to automatically generate a comprehensive README.md file for their codebase. This helps to significantly reduce the time and effort needed to create a comprehensive README file for the project. By understanding the codebase structure and automatically generating summaries of code files, README-AI provides users with a simple, efficient, and concise way to share their codebase with others. Additionally, the project also helps users to keep track of their project's dependencies and codebase changes, resulting in a more organized and up-to-date codebase.

---

## 🔮 Feautres

User-Centered Design Elements:

- Intuitive user interface for easy interaction, allowing users to select their repository and configuration options quickly and without confusion.
- Automated summary generation, which greatly simplifies the process of creating a README for a repository.
- In-built error checking and validation, ensuring a robust experience.

Architecture Design & Robust Technologies:

- The project is built on top of the OpenAI GPT-3 API, enabling it to generate summaries of code files.
- A modular structure is employed, with individual code scripts for preprocessing, configuring, logging, parsing, testing, building, and main functions.
- Caching is used to store API responses, configuration data, and file content, to improve performance.
- Logging is implemented for debugging and tracking purposes, using the loguru library.

Unique Features:

- Automated dependency extraction, which enables the project to detect and extract metadata from dependency files.
- Automated README building, which allows the project to quickly and easily generate a README for a repository.
- Automated code summary generation, which enables the project to generate summaries of code files with OpenAI’s GPT-3 API.
- Automated testing, which enables the project to run various tests and generate coverage reports.

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
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
│       ├── docs.png
│       ├── header.png
│       ├── misc.png
│       ├── setup.png
│       ├── toc.png
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

8 directories, 63 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                         | Module           |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This code script activates a conda environment and executes a Python script. It also sets environment variables, if needed, and uses the pipefail option to ensure that errors are caught correctly.            | scripts/run.sh   |
| clean.sh | This script removes backup files, Python cache files, cache directories, Visual Studio Code settings, build artifacts, pytest cache, benchmarks, and specific files such as raw_data.csv, logs, outs, and rdbs. | scripts/clean.sh |
| test.sh  | This code script activates a virtual environment, sets the directories to include and exclude from the coverage report, generates the coverage report, and removes files and folders.                           | scripts/test.sh  |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                       | Module            |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | This code script handles preprocessing of an input codebase, by cloning or copying a repository to a temporary directory, extracting its contents, mapping distinct file extensions to programming language names, and searching for and extracting metadata from dependency files. It also checks if a Dockerfile is present in the repository.                                                              | src/preprocess.py |
| conf.py       | This code script provides configuration constants for an application, including OpenAI API, Git, Markdown, and Paths configurations. It also includes a ConfigHelper class which reads in files from the conf/ directory, and updates helper configurations such as dependency_files, ignore_files, language_names, and language_setup.                                                                       | src/conf.py       |
| logger.py     | This code script provides a custom logger module using loguru for README-AI that configures a logger with handlers and allows for logging of messages of varying levels.                                                                                                                                                                                                                                      | src/logger.py     |
| factory.py    | This FileHandler class provides a factory module for reading and writing different file types, such as markdown, TOML, JSON, and YAML, with appropriate methods for handling each file type. It also provides exception classes for when a file cannot be read or written.                                                                                                                                    | src/factory.py    |
| model.py      | This code script provides a handler for OpenAI API to generate text for the README.md file. It includes functions to get a TTLCache and HTTP client, convert code to text by using OpenAI's GPT-3 API, and generate summary text from a prompt. It also includes a placeholder summary for files that exceed the max token limit.                                                                             | src/model.py      |
| builder.py    | This code script creates a README Markdown file for a codebase, which includes a table of contents, installation and run instructions, a directory tree, a list of project dependencies, and summaries of code files. It parses the project files to create additional columns in a DataFrame, generates badge icons for dependencies, and includes information from configuration data and helper classes.   | src/builder.py    |
| utils.py      | This code script provides utility methods for the project. It includes functions to reformat a sentence generated by OpenAI's GPT API, process text using spaCy, and check if a given string is a valid URL.                                                                                                                                                                                                  | src/utils.py      |
| parse.py      | This code script provides a set of functions for extracting dependencies from files in various languages(Python, Rust, JavaScript/TypeScript, Go, Java, C/C++). The files include Conda environment, Pipfile, pyproject.toml, requirements.txt, Cargo.toml, Cargo.lock, package.json, yarn.lock, package-lock.json, Go module, Go sum, Gradle, Maven, Makefile, CMakeLists.txt, configure.ac and Makefile.am. | src/parse.py      |
| main.py       | This script uses OpenAI's GPT APIs to generate README.md files for repositories. It validates and sets the OpenAI API key, validates the repository URL or path, reads configuration from a TOML file, extracts dependencies, generates summary text for code files, and builds the README.md file.                                                                                                           | src/main.py       |

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
#run tests
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

