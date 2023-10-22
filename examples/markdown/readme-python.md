
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
readme-ai
</h1>
<h3>◦ Smarter docs, powered by AI!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />

<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
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

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [📂 Project Structure](#-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Prerequisites](#️-prerequisites)
  - [💻 Installation](#-installation)
  - [🎮 Using readme-ai](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project README-AI is a tool that automatically generates high-level summaries for codebases using OpenAI's text generation model. It analyzes code repositories, extracts information about dependencies and file structure, and generates a Markdown file with a comprehensive summary of the codebase. The tool saves developers time by providing them with a ready-to-use README file that includes key information about the project. Its value proposition lies in its ability to quickly produce informative and standardized project documentation, making it easier for developers to understand, use, and collaborate on codebases.

---

## ⚙️ Features

| Feature                | Description                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **⚙️ Architecture**    | The codebase follows a modular architecture, with different files and modules responsible for specific tasks. The use of factories, wrappers, and handlers promotes code organization and separation of concerns. |
| **📖 Documentation**   | The codebase is well-documented, with detailed explanations of each file's purpose and functionality. The provided summaries are informative and help understand the codebase.                                        |
| **🔗 Dependencies**    | The code relies on external libraries such as pandas and requests for data manipulation and HTTP requests. It uses Git, Python, conda, and additional tools like Tree and SnakeViz for development processes.                                                               |
| **🧩 Modularity**      | The codebase demonstrates modularity by separating functionalities into different modules and classes. Each module focuses on one aspect of the project, which makes the codebase more maintainable and reusable.                     |
| **✔️ Testing**         | The codebase has a testing strategy, as evidenced by the presence of a test script. It uses the pytest framework for generating a test coverage report and the SnakeViz tool for analyzing the profiled output.                             |
| **⚡️ Performance**     | The overall performance of the codebase appears to be efficient. The code utilizes Pandas for data manipulation, performance profiling, and optimization techniques to ensure good performance.                          |
| **🔐 Security**        | The codebase does not directly handle security-related functionality. However, it generates an OpenAI API key, and handling it securely is important to protect access to the AI model.                                    |
| **🔀 Version Control** | The code repository uses Git for version control. It provides a version history, facilitates collaboration, and allows for easy branching and merging of code changes.                                                        |
| **🔌 Integrations**    | The codebase integrates with external services and tools such as the OpenAI API, Git repositories, and Docker containers. These integrations enhance the functionality and flexibility of the application.                       |
| **📶 Scalability**     | The codebase does not explicitly address scalability. However, by using modular design and external services, the application can potentially handle growth and can be extended to support additional features in the future.   |

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
├── poetry.lock
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

9 directories, 72 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                   | Summary                                                                                                                                                                                                            |
| ---                                                                    | ---                                                                                                                                                                                                                |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/main/Dockerfile) | This Dockerfile sets up a Python environment in a container by installing Git and Python dependencies, copying project files, and running a main.py file as the entry point command.                               |
| [Makefile](https://github.com/eli64s/readme-ai/blob/main/Makefile)     | This makefile provides commands to facilitate code formatting, cleaning, creating conda and virtual environments, profiling code using cProfile, and analyzing the profiled output using SnakeViz.                 |
| [setup.py](https://github.com/eli64s/readme-ai/blob/main/setup.py)     | The provided code is a setup script for the README-AI package. It defines the required packages, author information, project details, and dependencies. It also specifies keywords, classifiers, and project URLs. |

</details>

<details closed><summary>Setup</summary>

| File                                                                     | Summary                                                                                                                                                                                                                                               |
| ---                                                                      | ---                                                                                                                                                                                                                                                   |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/main/setup/setup.sh) | This code snippet checks if a conda environment exists, installs the "tree" command if it's not installed, ensures the presence of Git and Python 3.7+, creates a conda environment named "readme_ai" with Python 3.8 and installs required packages. |

</details>

<details closed><summary>Scripts</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                     |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run_batch.sh) | The code snippet is a Bash script that loops through a list of GitHub repository URLs and runs a Python script called "main.py" for each repository. The Python script takes the repository URL as input and generates a markdown file named "readme-[repository_name].md" as output.                                   |
| [run.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run.sh)             | This code snippet is a Bash script that activates a conda environment named "readme_ai" and runs a Python script called "main.py". The script sets the options to exit on error and fail on pipe failures at the beginning. It also exports environment variables, if needed, and requires an OpenAI API key to be set. |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/clean.sh)         | This code snippet is a Bash script that removes unwanted files and directories commonly found in a Python project. It deletes backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, benchmark files, and specific files like logs and raw data.                         |
| [test.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/test.sh)           | The provided code snippet activates a Conda environment named readme_ai. It generates a coverage report using pytest, excluding specified directories and files. It sets a minimum coverage threshold of 90%. After generating the report, it removes unnecessary files and folders.                                    |

</details>

<details closed><summary>Src</summary>

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/src/preprocess.py) | The provided code snippet is a module for preprocessing a codebase. It includes classes for wrapping the repository parser, analyzing local or remote git repositories, generating file information, tokenizing content, mapping file extensions to programming languages, and extracting dependency file contents. The code handles various file formats and uses pandas for data manipulation.                                                                                                                                                                                               |
| [conf.py](https://github.com/eli64s/readme-ai/blob/main/src/conf.py)             | The code snippet defines multiple data classes that store configuration constants for README-AI. It includes classes for API configuration, Git repository configuration, Markdown configuration, paths to configuration files, prompts configuration, and the main application configuration. Additionally, there is a helper class that loads and stores additional configuration settings from TOML files. Overall, the code organizes and manages configuration constants necessary for README-AI.                                                                                         |
| [logger.py](https://github.com/eli64s/readme-ai/blob/main/src/logger.py)         | The provided code snippet defines a custom logger class that wraps the functionality of the logging module. It supports multiple log levels, such as info, debug, warning, error, and critical, and uses a colored formatter for log messages. The class ensures that only one instance of the logger is created and allows logging to be configured with different log levels.                                                                                                                                                                                                                |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/src/factory.py)       | This code snippet provides a factory class that handles file input/output operations. It supports reading and writing different file types such as Markdown, TOML, JSON, and YAML. It offers methods to read and write files, and it also handles caching to improve performance. It raises specific exceptions when there are errors in file operations.                                                                                                                                                                                                                                      |
| [model.py](https://github.com/eli64s/readme-ai/blob/main/src/model.py)           | The provided code snippet is a handler for making requests to the OpenAI API to generate text for the README.md file. It includes functionality for converting code to natural language text and generating text using prompts. The code also handles rate limiting, caching, and error handling.                                                                                                                                                                                                                                                                                              |
| [builder.py](https://github.com/eli64s/readme-ai/blob/main/src/builder.py)       | The code snippet builds a README Markdown file for a codebase. It creates different sections including badges, directory tree, modules, setup guide, and more. It uses information from the configuration file and generates Markdown tables from code summaries. It also retrieves and formats badges for project dependencies.                                                                                                                                                                                                                                                               |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/src/utils.py)           | This code snippet provides utility methods for the README-AI tool. It includes functions for cloning and validating Git repositories, extracting username and repository name from GitHub URLs, adjusting maximum tokens for prompts, token counting, text truncation, file/url validation, list flattening, and text formatting.                                                                                                                                                                                                                                                              |
| [parse.py](https://github.com/eli64s/readme-ai/blob/main/src/parse.py)           | The provided code snippet consists of a collection of methods that parse different file formats to extract dependencies. This includes files such as docker-compose.yaml, conda environment files, Pipfile, Pipfile.lock, pyproject.toml, requirements.txt, Cargo.toml, Cargo.lock, package.json, yarn.lock, package-lock.json, go.mod, build.gradle, pom.xml, CMakeLists.txt, configure.ac, and Makefile.am. The methods take the content of the files as input and return a list of dependencies extracted from the files. Each method handles the parsing logic for a specific file format. |
| [main.py](https://github.com/eli64s/readme-ai/blob/main/src/main.py)             | This code snippet is the main entrypoint for the README-AI application. It takes command line arguments for the OpenAI API key, output file path, and repository URL or path. It validates the API key and repository, then it generates a README.md file by orchestrating the generation process using an OpenAI model. The generated README contains a code summary, slogan, overview, and features. Finally, it formats the text and builds the markdown file.                                                                                                                              |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 💻 Installation

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

### 🎮 Using readme-ai

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
