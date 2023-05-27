
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3 align="center">📍 Make Your READMEs Smarter with README-AI!</h3>
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
- [🔮 Features](#-feautres)
  - [Distinctive Features](#distinctive-features)
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

The README-AI GitHub project is a powerful tool that helps developers create and maintain informative and accurate README files for their projects. By leveraging OpenAI's GPT-3 API, it automatically generates summaries of code files in a repository and builds a comprehensive README.md file for the user. This eliminates the tedious and time-consuming task of manually crafting a README file and streamlines repository maintenance. The README-AI project helps developers save time and ensure their repositories are up-to-date, giving users the valuable information they need to get started quickly.

---

## 🔮 Features

### Distinctive Features

1. **User-Centered Design Elements:** This project has been designed with the user in mind, providing clear and easy-to-follow documentation, a streamlined user experience, and a comprehensive code base with scripts in multiple languages. 
2. **Support for Multiple Programming Languages:** The preprocessing script is able to detect the programming language of each source code file, allowing users to read summaries of code written in any language. 
3. **Flexible Dependency Parsing:** The dependency parsing script supports a wide variety of dependency file formats, allowing developers to accurately generate READMEs for any type of project.
4. **OpenAI-Powered Summaries:** The project utilizes the OpenAI API to generate summaries for each file in a repository, resulting in comprehensive READMEs that accurately reflect the structure and contents of a codebase. 
5. **Logging and Error Handling:** This project provides comprehensive logging and error handling, allowing users to easily debug any issues they may encounter. 
6. **Custom FileHandler:** The FileHandler class helps to easily read and write different file types, such as Markdown, TOML, JSON, and YAML, adding to the project's flexibility. 
7. **Git Integration:** The project also integrates with Git, allowing developers to easily clone repositories and update README.md files.

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
│       ├── features.png
│       ├── header.png
│       ├── misc.png
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

8 directories, 63 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                             | Module           |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This code script activates a Conda environment and then runs a Python script, ensuring any environment variables are correctly set.                                                                                                                 | scripts/run.sh   |
| clean.sh | This script deletes unnecessary files, folders, and artifacts, including backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files.                                      | scripts/clean.sh |
| test.sh  | This script activates the Conda virtual environment and runs a coverage report, testing the source code in the specified directory while omitting specified files and folders. It then cleans up by deleting any generated cache files and folders. | scripts/test.sh  |

</details>

<details closed><summary>Src</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Module            |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| preprocess.py | This code script handles the preprocessing of input codebases, including cloning or copying a repository to a temporary directory, extracting its contents, extracting distinct file extensions and mapping them to programming language names, and searching for dependencies and extracting their metadata. It also provides functions for extracting repository names from paths or URLs, and for getting a list of additional dependencies.                     | src/preprocess.py |
| conf.py       | This script provides configuration constants for a README-AI application, defining OpenAI API, Git, Markdown, Paths, and Prompts configurations. Furthermore, it contains a helper method to load configuration constants from a TOML file and update the configuration helper.                                                                                                                                                                                     | src/conf.py       |
| logger.py     | This code script implements a custom Logger module using loguru for README-AI. It provides functions for logging messages at different levels(e.g. debug, warning, error, etc.) with customizable formatting.                                                                                                                                                                                                                                                       | src/logger.py     |
| factory.py    | This module provides a FileHandler class for handling different file types, such as Markdown, TOML, JSON, and YAML. It allows for reading and writing of these files, and contains methods to parse and write the content in the appropriate format. Additionally, it also provides two exceptions to raise when files cannot be read or written.                                                                                                                   | src/factory.py    |
| model.py      | This code script handles the OpenAI API to generate summary text for each file in a repository, using the GPT-3 large language model. It includes functions for fetching summaries from the API, setting up an HTTP client and TTLCache, and generating summaries with a given prompt. It handles errors, ignores certain files, and has a max token limit of 4096.                                                                                                 | src/model.py      |
| builder.py    | This code script builds the README Markdown file for a codebase, by collecting and formatting project information, such as dependencies, summaries, and code structure. It uses configuration and helper classes, as well as Git, Pandas and logging libraries, to create badges, tables, and a directory tree structure. Finally, it creates a setup guide based on the top used language in the project.                                                          | src/builder.py    |
| utils.py      | This script provides utility methods for a project, including functions to reformat sentences, process text with spaCy, and verify if a string is a valid URL.                                                                                                                                                                                                                                                                                                      | src/utils.py      |
| parse.py      | This script contains helper functions for dependency parsing used by the README-AI project. It provides functions for extracting dependencies from files such as conda environment files, Pipfiles, pyproject.toml files, requirements.txt files, Cargo.toml and Cargo.lock files, package.json files, yarn.lock files, package-lock.json files, Go module files, Go sum files, Gradle files, Maven files, Makefiles, CMakeLists.txt files, and configure.ac files. | src/parse.py      |
| main.py       | This code script is a program that generates a README.md file for a user's repository using OpenAI's GPT APIs. It includes functions to validate and set the OpenAI API key provided by the user, validate the repository URL or path provided by the user, generate summary text for code files using OpenAI's GPT-3, and build the README.md file.                                                                                                                | src/main.py       |

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

