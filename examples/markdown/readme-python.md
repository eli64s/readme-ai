<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>README-AI</h1>
<h3>◦ AI-powered READMEs made simple!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest" />
</p>
<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/eli64s/readme-ai?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running readme-ai](#-running-readme-ai)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The readme-ai repository is a powerful tool that automates the generation of high-quality README files for projects. It uses advanced natural language processing techniques to analyze the codebase and extract relevant information. With its intuitive command-line interface, users can quickly create comprehensive README files that accurately describe their project's purpose, features, and installation instructions. By saving time and ensuring consistency, readme-ai enhances the documentation process and improves project visibility.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architecture, with components organized into separate directories based on their functionality. The core functionality is implemented in the `core` directory, while the CLI commands are implemented in the `cli` directory. |
| 📄 | **Documentation**  | The documentation appears to be lacking or incomplete. There is no dedicated documentation directory, and it is not clear if there are any external documentation resources available. |
| 🔗 | **Dependencies**   | The codebase relies on external dependencies managed through Poetry. The specific dependencies are listed in the `poetry.lock` file.  |
| 🧩 | **Modularity**     | The codebase is organized into smaller components, allowing for easier development and maintenance. Each component is responsible for a specific functionality, such as parsing, preprocessing, and generating Markdown. |
| 🧪 | **Testing**        | The codebase does not include any testing strategies or tools. There are no test directories or test scripts available. Implementing testing would improve code reliability and maintainability. |
| ⚡️  | **Performance**    | The codebase does not have any specific performance optimizations. However, the usage of Python and its libraries can generally offer good performance for a command-line tool like this. |
| 🔐 | **Security**       | There is no evidence of specific security measures implemented in the codebase. However, since this tool primarily operates on local files, the security risks should be low. |
| 🔀 | **Version Control**| The codebase includes version control strategies through its use of Git. The .github directory contains workflows related to build, publish, and release processes.  |
| 🔌 | **Integrations**   | The codebase does not have any explicit integrations with external systems or services. It primarily operates on local file systems. |
| 📶 | **Scalability**    | The codebase does not explicitly address scalability considerations. However, since it is a command-line tool, scalability might not be a significant concern.

---


## 📂 Repository Structure

```sh
└── readmeai/
    ├── .github/
    │   ├── release-drafter.yml
    │   └── workflows/
    │       ├── build_image.yml
    │       ├── publish_package.yml
    │       └── release-drafter.yml
    ├── Dockerfile
    ├── Makefile
    ├── examples/
    │   ├── images/
    │   └── markdown/
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai/
    │   ├── cli/
    │   │   ├── commands.py
    │   │   └── options.py
    │   ├── config/
    │   │   ├── __Init__.py
    │   │   └── settings.py
    │   ├── core/
    │   │   ├── factory.py
    │   │   ├── logger.py
    │   │   ├── model.py
    │   │   ├── parser.py
    │   │   ├── preprocess.py
    │   │   └── tokens.py
    │   ├── main.py
    │   ├── markdown/
    │   │   ├── badges.py
    │   │   ├── headers.py
    │   │   ├── quickstart.py
    │   │   ├── tables.py
    │   │   ├── template.py
    │   │   └── tree.py
    │   ├── services/
    │   │   └── version_control.py
    │   ├── settings/
    │   │   ├── config.toml
    │   │   ├── dependency_files.toml
    │   │   ├── identifiers.toml
    │   │   ├── ignore_files.toml
    │   │   ├── language_names.toml
    │   │   └── language_setup.toml
    │   └── utils/
    │       └── utils.py
    ├── requirements.txt
    ├── scripts/
    │   ├── build_image.sh
    │   ├── build_pypi.sh
    │   ├── clean.sh
    │   ├── run.sh
    │   ├── run_batch.sh
    │   └── test.sh
    ├── setup/
    │   ├── environment.yaml
    │   └── setup.sh

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/main/requirements.txt) | The code in "requirements.txt" contains a list of Python packages and libraries needed for the project. These packages include black, click, colorlog, cachetools, flake8, gitpython, httpx, h2, isort, openai, pre-commit, pydantic, pyyaml, pytest, pytest-cov, responses, ruff, tabulate, tenacity, tiktoken, and toml. These packages provide various functionalities such as formatting, logging, version control, HTTP requests, testing, and more.                                                                                                                                                                                                        |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/main/Dockerfile)             | The provided Dockerfile sets up a Docker container environment with Python 3.9 installed. It installs system dependencies, creates a non-root user, sets permissions, and adds the directory for user scripts to the PATH. It then installs the "readmeai" package from PyPI with a pinned version and sets the command to run the "readmeai" CLI.                                                                                                                                                                                                                                                                                                               |
| [Makefile](https://github.com/eli64s/readme-ai/blob/main/Makefile)                 | The Makefile provides a set of commands for repository file management and development tasks. It includes commands for cleaning up the repository files, executing code formatting and linting, installing requirements, creating a conda or virtual environment, and fixing git untracked files. These commands are executed by running the corresponding targets in the Makefile using the make command.                                                                                                                                                                                                                                                       |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/main/pyproject.toml)     | The code is a configuration file written in TOML format for the "readmeai" Python project. It specifies the project's metadata, dependencies, scripts, and development tools. It also defines the project's dev dependencies, test configurations, and code formatting rules.                                                                                                                                                                                                                                                                                                                                                                                    |
| [poetry.lock](https://github.com/eli64s/readme-ai/blob/main/poetry.lock)           | The code consists of a directory tree containing several files and folders. It includes a Dockerfile and a Makefile for building and running the code, as well as example files in the "examples" folder. The "readmeai" folder contains various modules for different functionalities, such as CLI commands, configuration settings, core functionalities like logging and parsing, and markdown-related operations. It also includes services for version control and utility functions. The "settings" folder contains configuration files in TOML format. Additionally, there are shell scripts for various tasks like building images and running the code. |

</details>

<details closed><summary>Setup</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/main/setup/setup.sh)                 | The code is a setup script for the README-AI project. It checks if the'tree' command is installed and installs it if necessary. Then, it checks if Git and Conda are installed and exits if they're not.Next, it checks if Python 3.8 or higher is installed and exits if it's not.If the conda environment'readmeai' does not exist, it creates it using the'environment.yaml' file.The'readmeai' environment is then activated, and the Python path is added to the PATH environment variable.The required packages from the'requirements.txt' file are installed using pip.Finally, the conda environment is deactivated, and the setup is completed. |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/main/setup/environment.yaml) | The code represents the environment setup for a project called "readmeai". It specifies the name of the project, channels to use (conda-forge and defaults), and dependencies required for the project. This includes Python version 3.9 or higher, installation of pip, and an empty pip section.                                                                                                                                                                                                                                                                                                                                                       |

</details>

<details closed><summary>Scripts</summary>

| File                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run_batch.sh)     | The code provided is a bash script that automates the generation of README files for a list of GitHub repositories. It uses the `readmeai` Python package to create Markdown files based on the repository's URL. The script iterates over a predefined list of repository URLs, extracts the repository name, and passes the URL to the `readmeai.cli.commands` module along with output file options to create a Markdown file for each repository.                                                                                                                                                                                                                                                                                             |
| [build_image.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_image.sh) | The code in the `build_image.sh` script is used to build and push a Docker image. It sets the image name and version, creates a new build context using Docker BuildKit, pulls the necessary dependencies, and builds the image for multiple platforms. Finally, it pushes the built image to a Docker registry.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [build_pypi.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_pypi.sh)   | The code in the `build_pypi.sh` script performs the following core functionalities:1. Cleans the project by running the `clean.sh` script.2. Builds the project using the `python-m build` command.3. Uploads the built files to the PyPI repository using `twine upload`.4. Prints a success message indicating that the `readmeai` package has been successfully pushed to PyPI.                                                                                                                                                                                                                                                                                                                                                                |
| [run.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run.sh)                 | The code in `scripts/run.sh` activates the `readmeai` conda environment and then runs the `readmeai` Python script using the `python3` command. The script takes arguments `-o readme-ai.md` and `-r https://github.com/eli64s/readme-ai`. It also includes commented out lines to export environment variables if needed.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/clean.sh)             | The `clean.sh` script is a bash script that provides several functions for cleaning different artifacts and files in a Python project. The `clean()` function removes build, test, coverage, and Python artifacts. The `clean_build()` function removes build artifacts. The `clean_pyc()` function removes Python file artifacts. The `clean_test()` function removes test and coverage artifacts. The `clean_backup_and_cache()` function removes backup files and Python cache files. The script provides a command line interface to invoke these functions based on the provided command.                                                                                                                                                    |
| [test.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/test.sh)               | The code in `scripts/test.sh` is a bash script that performs the following tasks:1. Activates the conda environment named "readmeai".2. Sets the directories to include in the coverage report (`source_dir` variable).3. Sets the directories to exclude from the coverage report (`omit_dir` variable).4. Sets the specific file to omit from the coverage report (`omit_file` variable).5. Runs pytest with coverage enabled, specifying the source and omit directories.6. Generates a coverage report that shows missing lines and fails if the coverage is below 90%.7. Removes unnecessary files and folders, such as `__pycache__`, `.pytest_cache`, `.coverage`, and any file or folder named "*local_dir*" under the `tests` directory. |

</details>

<details closed><summary>.github</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/release-drafter.yml) | The code is a configuration file for the release drafter tool. It defines the template for generating release notes based on the conventions of Keep a Changelog. It sets up categories for different types of changes (features, bug fixes, etc.) and assigns corresponding labels. It provides a customizable template for the release notes, including placeholders for the version number and the changes made. It also configures a version resolver to determine the appropriate version based on the labels applied to issues or pull requests. |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-drafter.yml) | This code is a GitHub Actions workflow file that automates the process of creating release drafts for a repository. It listens for push and pull request events on the "main" branch and runs the release-drafter action. The action is responsible for drafting release notes based on merged pull requests. It requires write permissions to create releases and pull requests. The workflow runs on an Ubuntu environment and uses the release-drafter@v5 action with the provided configuration name and GitHub token secret.                                                                                                                                                                 |
| [publish_package.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/publish_package.yml) | The code is a GitHub workflow that automates the process of publishing a Python package to PyPI (Python Package Index). It runs on the "main" branch and also when a new release is created. The workflow consists of several steps:1. Checking out the code from the repository.2. Setting up Python 3.x.3. Installing necessary dependencies (pip, build, twine).4. Building the package using the "python-m build" command.5. Publishing the package to PyPI using the "python-m twine upload" command. The access credentials are provided through environment variables (TWINE_USERNAME and TWINE_PASSWORD), where the password is sourced from the PyPI API token stored in GitHub secrets. |
| [build_image.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/build_image.yml)         | The code in.github/workflows/build_image.yml sets up a Docker image building workflow. It triggers on pushes to the main branch and on new releases. It uses various GitHub Actions to accomplish the following steps: performing a checkout of the repository, setting up QEMU and Docker Buildx, logging in to Docker Hub, building the Docker image, and pushing it to the Docker registry with specified tags.                                                                                                                                                                                                                                                                                |

</details>

<details closed><summary>Readmeai</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [main.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/main.py) | The code is the main entrypoint for an application called readme-ai. It orchestrates the generation process of a README file. It loads configuration settings, retrieves the repository tree structure, parses the codebase to get dependencies and file information, generates code summaries using OpenAI Language Models (LLMs), and builds the README.md file with headers and content based on the retrieved information. The code supports offline mode and outputs logs during the execution process. |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/ignore_files.toml)         | The code above represents the content of the `ignore_files.toml` file in the `readmeai/settings/` directory. This file is used to specify files, directories, and file extensions that should be ignored or excluded. It provides a comprehensive list of these items, including common files and directories that are often excluded in software projects. The code includes lists of ignored directories, extensions, and files, enabling users to easily customize their project's ignore list.                                     |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_names.toml)     | The code is a configuration file that maps programming language file extensions to their corresponding names. It provides a list of file extensions and their associated programming languages, allowing for easy identification and categorization of files based on their extensions.                                                                                                                                                                                                                                                |
| [identifiers.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/identifiers.toml)           | The code provided contains a configuration file called "identifiers.toml" that defines different identifiers for various project types. The identifiers are organized into different categories such as web, mobile, desktop, backend, frontend, game, data, machine learning, library, CLI, API, plugin, and embedded. Each category contains a list of keywords that are commonly associated with projects of that type. These identifiers can be used to analyze and classify projects based on their file and directory structure. |
| [config.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml)                     | The code defines various settings and prompts for the readmeai project. It includes API settings, version control system URLs, CLI options, Git options, file paths, and Markdown template code. The settings determine the behavior of the readmeai project, while the prompts are structured templates for generating content. The codebase overview prompt requests a technical analysis of the project, file summaries, and core functionalities summarized in a Markdown table.                                                   |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/dependency_files.toml) | The code provides a configuration file (`dependency_files.toml`) that specifies the dependency file names for various programming languages. These file names are used by the `readmeai` application to identify and track the dependencies of a project. The file lists a wide range of known dependency file names for different languages, such as `requirements.txt` for Python, `package.json` for JavaScript, and `build.gradle` for Java.                                                                                       |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_setup.toml)     | The code represents a language setup and run instructions configuration file. It contains a mapping of programming languages to the commands needed to compile, run, and test code in each language.                                                                                                                                                                                                                                                                                                                                   |

</details>

<details closed><summary>Core</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/preprocess.py) | The code is a part of the "readmeai" project and specifically focuses on the preprocessing of an input codebase. It provides functionalities to analyze a local or remote git repository, generate a list of file information, extract dependency file contents, retrieve the file contents from a list of dictionaries, extract unique contents from the list, extract the dependencies of a user's repository, map file extensions to programming languages, and tokenize the content of each file. The code is organized into classes and functions that handle these different tasks. |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/tokens.py)         | The code in the `tokens.py` file provides utilities for handling tokenization. It includes functions to adjust the maximum number of tokens based on a specific prompt, get the number of tokens in a text string, determine the token encoder to use for the model, and truncate a text string to a maximum number of tokens. These utilities are used for preprocessing and manipulating text data in the `readmeai` project.                                                                                                                                                           |
| [logger.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/logger.py)         | The `Logger` class is a custom logger implementation that allows for logging messages at different levels (info, debug, warning, error, critical). It configures the logger with a colored formatter and log colors for each level. The logger can be instantiated with a name and a logging level, and provides methods for logging messages at different levels.                                                                                                                                                                                                                        |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/factory.py)       | The `FileHandler` class in the `factory.py` file is a factory class that handles file input and output operations. It provides methods to read and write content from/to different file types such as JSON, Markdown, TOML, TXT, and YAML. The class dynamically determines the appropriate read/write methods based on the file extension. It also includes exception handling to raise custom exceptions when file operations fail. Additionally, the class maintains a cache of file contents to improve performance when reading the same file multiple times.                        |
| [model.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/model.py)           | The code represents an OpenAI API handler that generates text for the README.md file. It has functionalities to convert code to natural language text, generate text using prompts, and handle API requests to generate text. It includes methods for initializing the handler, converting code to text, generating text from prompts, handling API requests, and closing the HTTP client.                                                                                                                                                                                                |
| [parser.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/parser.py)         | The code in `readmeai/core/parser.py` provides methods for parsing and extracting dependency file metadata. It includes functions for parsing various file types such as JSON, TOML, YAML, Docker Compose, Pipfile, Pyproject.toml, requirements.txt, Cargo.toml, etc. Each parse function takes in the content of the file and returns a list of dependencies extracted from the file. The code also includes utility functions for parsing specific fields from JSON and TOML files.                                                                                                    |

</details>

<details closed><summary>Config</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [__Init__.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/__Init__.py) | The code in `readmeai/config/__Init__.py` serves as the initialization file for the `config` module in the `readmeai` directory. It includes the necessary code to initialize and configure settings related to the project, such as importing the `settings.py` module.                                                                                                                                                                    |
| [settings.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings.py) | The code defines Pydantic models for the README AI application's configuration settings. It includes models for API configuration, CLI options, Git repository configuration, Markdown code block templates, file paths, prompts, and the overall application configuration. The code also includes a helper class to load additional configuration files. There are functions to load the main configuration and the configuration helper. |

</details>

<details closed><summary>Markdown</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [tree.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tree.py)             | The code generates a tree structure for a given directory. It includes a class called `TreeGenerator`, which takes in a root directory, repository URL, project name, and optional maximum depth to generate the tree. The `generate_and_format_tree` method generates and formats the tree structure using the `_generate_tree` and `_format_tree` methods. The `_generate_tree` method recursively traverses the directory, adding directory and file names to the tree structure, while the `_format_tree` method formats the final tree structure with the project name.                                                                                |
| [badges.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/badges.py)         | The code in the `badges.py` file generates badges for the README file. It uses icons from the Shields.io and app iOS styles to create the badges. The code reads the icons from resource files, filters them based on the project's dependencies, and formats them into Markdown image tags. The badges are sorted by color and displayed in multiple lines if there are more than 8 badges. The generated badges are returned as a string.                                                                                                                                                                                                                 |
| [template.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/template.py)     | The code defines a directory tree structure for a project called "readmeai". It includes various files and directories related to the project. The `template.py` file defines classes for generating a readme file based on different project types. The `ReadmeTemplate` abstract class provides a blueprint for subclasses to implement. The `LibraryTemplate` and `WebTemplate` subclasses override certain sections of the readme template. The `Project` class holds information about the project. The `gen_readme` function generates a readme file based on the project type. Finally, an example is provided to demonstrate the usage of the code. |
| [tables.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tables.py)         | The code contains functions that create Markdown tables used to format the code summaries generated by the LLM (Language Model) tool. The `create_markdown_tables` function formats the code summaries into a list, while the `create_tables` function creates Markdown tables for each sub-directory in the project. The code also includes utility functions to create and format the Markdown tables. Finally, the `build_recursive_tables` function recursively builds a Markdown table structure for a given directory.                                                                                                                                |
| [headers.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/headers.py)       | This code builds the README Markdown file for a codebase. It constructs various sections of the README by formatting the contents for each section. It creates badges, tables, and a setup guide, and removes emojis from headers and the Table of Contents if specified. The generated README file is written to the output path specified in the configuration.                                                                                                                                                                                                                                                                                           |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/quickstart.py) | The code in the `quickstart.py` file is responsible for creating the'Getting Started' section of a README file. It uses the provided configuration and helper objects to determine the default installation, run, and test commands. It also analyzes the summaries list to determine the most frequently used programming language and retrieve the corresponding setup guide. If an error occurs, it falls back to using the default run command. The function then returns the default installation, run, and test commands as a tuple.                                                                                                                  |

</details>

<details closed><summary>Utils</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                         |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/utils/utils.py) | The code in utils.py provides utility methods for the readme-ai application. It includes functions such as filtering out files to ignore, checking if a string is a valid URL, flattening a nested list, formatting text, and removing text between HTML tags. The code uses regular expressions and the pathlib library for file handling. |

</details>

<details closed><summary>Cli</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [options.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/options.py)   | The code defines various options for the command line interface of a program called "readmeai". These options include API key, badges, emojis, model, offline mode, output file path, repository, temperature, language, and style. These options can be used to customize the generation of a README.md file using the "readmeai" program.                                                                                       |
| [commands.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/commands.py) | The code in the file `commands.py` defines the CLI commands for a tool called `readme-ai`. It uses the `click` library to create command-line options for the tool. The main function `commands` accepts several optional arguments and invokes the `main` function from another module. The purpose of the `readme-ai` tool is to generate a README file for a GitHub repository based on various options specified by the user. |

</details>

<details closed><summary>Services</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [version_control.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/version_control.py) | The code in `version_control.py` provides Git-related utilities for the `readme-ai` project. It includes functions for making HTTP requests to retrieve metadata about a GitHub, GitLab, or Bitbucket repository, cloning a repository to a temporary directory, finding the path to the git executable, validating the file permissions of a cloned repository, getting the file URL for a given file based on the platform, extracting the user and repository name from a URL or path, and parsing the repository URL to construct the API URL. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

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

### 🤖 Running readme-ai

```sh
python main.py
```

### 🧪 Tests
```sh
pytest
```

---


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

[**Discussions**](https://github.com/eli64s/readme-ai/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/eli64s/readme-ai/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

- Contributions are welcome! Please follow these steps:

1. Fork the project repository to your GitHub account.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive such as `new-feature-x` or `bugfix-issue-x`.
```sh
git checkout -b new-feature-x
```
4. Develop your changes locally.
5. Commit your updates with a clear explanation of the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub.
```sh
git push origin new-feature-x
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
8. Once your pull request is reviewed, it will be merged into the main branch of the project repository.

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
