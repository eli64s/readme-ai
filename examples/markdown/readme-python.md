<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>README-AI</h1>
<h3>◦ Revolutionize documentation with readme-ai!</h3>
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
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running readme-ai](#-running-readme-ai)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository "readme-ai" is a tool that automates the generation of README files for software projects. It utilizes machine learning models and natural language processing techniques to analyze the codebase and generate a comprehensive and informative README. The tool helps developers save time and effort by automatically documenting their projects, improving visibility and collaboration. The project provides an easy-to-use command-line interface and is designed to be customizable and extensible for different project requirements.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architecture, with separate directories for different components such as cli, config, core, markdown, and services. The main.py serves as the entry point for the application.|
| 📄 | **Documentation**  | There is no explicit documentation available in the repository. It would be beneficial to have comprehensive documentation to understand the codebase and its usage. |
| 🔗 | **Dependencies**   | The repository relies on Poetry for managing dependencies. The dependencies are listed in the poetry.lock and pyproject.toml files.|
| 🧩 | **Modularity**     | The system is organized into smaller, interchangeable components within separate directories. This promotes code reusability and maintainability. Most components have clear responsibilities and are decoupled from each other.|
| 🧪 | **Testing**        | There are no specific testing strategies or tools mentioned in the repository. It would be beneficial to have unit tests, integration tests, or a test framework to ensure the reliability of the system.|
| ⚡️  | **Performance**    | The performance characteristics of the system are not explicitly mentioned. It would be necessary to analyze the code and its usage to determine its performance in terms of speed, efficiency, and resource usage.|
| 🔐 | **Security**       | There are no specific security measures mentioned in the repository. It would be necessary to analyze the code to determine the security practices implemented, such as input validation, proper handling of sensitive data, and prevention of common vulnerabilities.|
| 🔀 | **Version Control**| The repository uses version control with Git. There are GitHub Actions workflows present in the .github/workflows directory for automated builds, package publishing, and release management.|
| 🔌 | **Integrations**   | There are no explicit integration details mentioned in the repository. It would be necessary to analyze the code to determine how the system interacts with other systems and services.|
| 📶 | **Scalability**    | The scalability aspects of the system are not explicitly mentioned. It would require a deeper analysis of the codebase and its design to determine its ability to handle growth.|

---


## 📂 Repository Structure

```sh
└── ./
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

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/main/requirements.txt) | The code in the "requirements.txt" file lists the necessary packages and libraries required for running the code successfully, including "black", "click", "colorlog", "cachetools", "flake8", "gitpython", and others.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/main/Dockerfile)             | The code defines a Dockerfile for creating a Docker image. The image is based on a Python 3.9 installation. It installs necessary dependencies, creates a non-root user, sets permissions, installs the "readmeai" package from PyPI with a specified version, and sets the command to run the "readmeai" CLI when the container starts.                                                                                                                                                                                                                                                                                                                      |
| [Makefile](https://github.com/eli64s/readme-ai/blob/main/Makefile)                 | This Makefile provides a set of commands for various tasks related to repository file management, code formatting, linting, and package installations. The available commands include cleaning up repository files, executing code formatting, linting the code, installing requirements, creating a conda environment, and creating a virtual environment. Additionally, there is a command to fix git untracked files.                                                                                                                                                                                                                                      |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/main/pyproject.toml)     | The code is a configuration file written in TOML format that defines the dependencies, scripts, and metadata for a Python project called "readmeai." It specifies the required packages and their versions, as well as additional development dependencies. The code also defines scripts for various tasks, such as building images, running tests, and cleaning. The configuration includes metadata such as project name, version, description, authors, license, and keywords. The code enables the project to be built and managed using the Poetry tool and provides options for generating README files from the terminal using AI-powered automation. |
| [poetry.lock](https://github.com/eli64s/readme-ai/blob/main/poetry.lock)           | The code represents a directory tree structure, containing various files and directories. It includes a Dockerfile, a Makefile, and various Python modules and packages. The directory structure includes components for command line interface (CLI), configuration settings, core functionalities such as logging and parsing, markdown generation, services related to version control, and utility functions. Additionally, it contains script files for building images and publishing packages.                                                                                                                                                         |

</details>

<details closed><summary>Setup</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/main/setup/setup.sh)                 | This code is a setup script for the README-AI environment. It first checks if the'tree' command is installed and installs it if needed. Then, it verifies the presence of Git and Anaconda/Miniconda. Next, it checks for Python 3.8+ and creates a new conda environment named'readmeai' if it doesn't already exist. It activates the environment, adds the Python path to the PATH variable, and installs required packages from the'requirements.txt' file. Finally, it deactivates the environment and provides a completion message. |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/main/setup/environment.yaml) | The code above defines the environment configuration for the "readmeai" project. It specifies the name of the project, the channels to fetch packages from (conda-forge and defaults), and the dependencies required for the project, which include Python version 3.9 and pip.                                                                                                                                                                                                                                                            |

</details>

<details closed><summary>Scripts</summary>

| File                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run_batch.sh)     | The code in the "run_batch.sh" script is a bash script that runs a batch process to generate README files for multiple GitHub repositories using the "readmeai" Python package. It loops through a list of repository URLs and for each repository, it extracts the repository name, then calls the "readmeai" Python package's command-line interface (CLI) to generate a README file for the repository. The generated README file is saved with the name "readme-[repository name].md". |
| [build_image.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_image.sh) | The code in `scripts/build_image.sh` builds a Docker image named "readme-ai" with the tag "latest". It uses Docker Buildx to create and use a builder instance, pulls the necessary buildkit image, and then builds and pushes the Docker image with support for both linux/amd64 and linux/arm64 platforms. The script outputs messages indicating the progress and success of the build and push operations.                                                                             |
| [build_pypi.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_pypi.sh)   | The code `build_pypi.sh` is a Bash script that builds a Python package called "readmeai" and pushes it to the Python Package Index (PyPI). It first runs a script `clean.sh` to clean the previous build artifacts. Then, it uses the `python-m build` command to build the package. Finally, it uses `twine upload` to upload the built package to PyPI, using provided authentication information. After successful upload, it displays a success message.                               |
| [run.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run.sh)                 | The code in `scripts/run.sh` activates the conda environment `readmeai` and then runs a Python script `readmeai.cli.commands`, passing it the arguments `-o readme-ai.md-r https://github.com/eli64s/readme-ai`. It also includes a commented section to export environment variables if needed.                                                                                                                                                                                           |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/clean.sh)             | The code in `scripts/clean.sh` is a Bash script that provides a way to clean various artifacts and files in a project. It defines several clean functions for different types of artifacts, such as build artifacts, Python file artifacts, test and coverage artifacts, backup files, and Python cache files. The script takes command line arguments to execute specific clean functions or displays available commands and their usage if no arguments are provided.                    |
| [test.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/test.sh)               | The code in `scripts/test.sh` is a bash script that runs tests and generates a coverage report for the `readmeai` directory. It activates the `readmeai` conda environment and sets the directories to be included and excluded from the coverage report. It then runs pytest with coverage, generates the coverage report, and sets a minimum coverage threshold of 90%. Finally, it removes temporary files and folders related to the tests.                                            |

</details>

<details closed><summary>.github</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/release-drafter.yml) | The code is a configuration file for a release drafter. It follows the conventions specified in the keepachangelog.com website. It defines templates for the name and tag of each release, as well as categories for different types of changes such as features, bug fixes, and documentation. It also specifies how to format each change entry and how to resolve the version based on labels. Finally, it provides a template for the release notes, including a section for listing the changes. |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-drafter.yml) | The code is a GitHub Actions workflow file (.github/workflows/release-drafter.yml) that automates the creation of release notes for a project. It listens for events such as pushes to the main branch and pull requests, and it runs a job called "update_release_draft" on the latest Ubuntu environment. This job has permissions to read contents and write pull requests. The steps in the job use the release-drafter action to draft release notes based on merged pull requests, using the GitHub token stored as a secret in the repository. |
| [publish_package.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/publish_package.yml) | This code sets up a GitHub workflow that is triggered when there is a push to the main branch or when a new release is created. It runs on an Ubuntu environment and performs several steps. It checks out the code, sets up Python 3.x, installs dependencies including build and twine, builds the package, and publishes it to PyPI using twine. The PyPI API token is stored as a secret in GitHub.                                                                                                                                               |
| [build_image.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/build_image.yml)         | The code is a GitHub Actions workflow named "Build Docker Image" triggered by pushes to the main branch and new releases. It sets up QEMU, Docker Buildx, and logs into Docker Hub using provided secrets. Then it builds and pushes a Docker image to Docker Hub with the tag "zeroxeli/readme-ai:latest" for platforms linux/amd64, linux/arm/v7, and linux/arm64/v8.                                                                                                                                                                               |

</details>

<details closed><summary>Readmeai</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [main.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/main.py) | The code is part of the readme-ai application and serves as the main entry point. It imports various modules and functions related to configuration settings, logging, preprocessing, and markdown generation. The `main` function takes in several parameters to configure the application and calls the `readme_agent` function to orchestrate the README file generation process. Within `readme_agent`, the code generates a tree structure of the repository, parses dependencies, generates codebase file summaries, and generates a README.md file based on the provided prompts and configurations. |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/ignore_files.toml)         | The code above defines a configuration file, ignore_files.toml, that specifies files and directories to be ignored. It includes a list of directories and file extensions that should be excluded from consideration in a project, such as version control data, test files, and temporary files. This configuration allows developers to filter out specific files and directories when working with the project.                                                                                                                                                                                                                                     |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_names.toml)     | The code is a configuration file that maps programming language file extensions to their corresponding names. It provides a comprehensive list of file extensions and their corresponding language names, allowing for easy identification and categorization of code files. This information can be used in various software development tools and processes where language-specific operations or analysis is required.                                                                                                                                                                                                                              |
| [identifiers.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/identifiers.toml)           | The code represents a directory tree for a project called "readmeai". The tree includes various directories and files related to the project, such as Dockerfile, Makefile, examples, poetry.lock, pyproject.toml, and scripts. Additionally, there is a path in the "readmeai/settings/identifiers.toml" file that contains categories and a list of keywords associated with each category. These categories include project types like web, mobile, desktop, backend, frontend, game, data, ml, library, cli, api, plugin, and embedded. Each category has a list of keywords representing commonly used technologies or features in that category. |
| [config.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml)                     | The code is a configuration file written in TOML format that holds various settings and templates for a project called "readme-ai." It includes settings for the model API, version control systems, CLI options, git options, paths, prompts, and markdown templates. The file also contains pre-defined prompts and templates for generating documentation and summaries, including features, overview, slogan, and code summaries. The settings can be customized to generate different outputs and formats for the project documentation.                                                                                                          |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/dependency_files.toml) | The code above defines a list of commonly used dependency file names for various programming languages. These file names are used to identify dependencies in software projects. The list includes file names for languages such as C/C++, Go, Java, Python, Rust, Ruby, Clojure, Elixir, JavaScript/Node.js, TypeScript, PHP, Swift, Kotlin, Dart/Flutter, R, Shell, Scala, Groovy, Lua, Julia, Haskell, C#, F#, Objective-C, Matlab, and Perl. It also includes common Docker-related files.                                                                                                                                                         |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_setup.toml)     | The code represents a directory tree structure with various files and folders. It includes configuration files, code files, examples, scripts, and setup files. In particular, the code snippet highlights a "language_setup.toml" file inside the "readmeai/settings" directory. This file contains instructions for setting up and running different programming languages, including commands for building, running, and testing code in each language.                                                                                                                                                                                             |

</details>

<details closed><summary>Core</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/preprocess.py) | The code provides functionalities for preprocessing the input codebase. It includes classes and functions for analyzing a local or remote git repository, generating file information, extracting dependency file contents, mapping file extensions to programming languages, tokenizing the content of each file, and extracting file contents and unique contents. These functionalities are implemented in the `RepositoryParser` class, which takes a configuration and a configuration helper as input. |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/tokens.py)         | The code in the "tokens.py" file provides utilities for handling language tokens. It includes functions to adjust the maximum number of tokens based on a specific prompt, count the number of tokens in a text string, determine the token encoder to use for a model, and truncate a text string to a maximum number of tokens.                                                                                                                                                                            |
| [logger.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/logger.py)         | The code represents a custom logger class for a project. It uses the logging module to log messages at different levels (debug, info, warning, error, critical). The logger is configured with a colored formatter that prints log messages with color-coded levels. The class implements methods for each log level and a generic log method to log messages at a specific level. The logger is a singleton, ensuring only one instance of the class exists.                                                |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/factory.py)       | The code implements a Factory class called FileHandler that handles file I/O operations. It provides methods to read and write different file types, such as JSON, Markdown, TOML, TXT, and YAML. The class dynamically selects the appropriate reading and writing methods based on the file extension. It also includes exception handling for any errors that may occur during file operations.                                                                                                           |
| [model.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/model.py)           | The code represents an OpenAI API handler used to generate natural language text based on code snippets. It includes functionalities such as converting code to text, generating text using prompts, and handling API requests and exceptions. The handler uses asyncio to handle concurrent tasks efficiently and implements a caching mechanism for improved performance.                                                                                                                                  |
| [parser.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/parser.py)         | The code provides a set of methods to parse and extract dependency file metadata. It supports various file formats such as JSON, TOML, YAML, and specific formats like Docker Compose, Conda environment files, Pipfile, Pipfile.lock, poetry.lock, pyproject.toml, requirements.txt, Cargo.toml, Cargo.lock, package.json, yarn.lock, package-lock.json, go.mod, build.gradle, pom.xml, CMakeLists.txt, configure.ac, and Makefile.am. The methods extract dependencies and return a list of package names. |

</details>

<details closed><summary>Config</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [__Init__.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/__Init__.py) | The code in the `readmeai/config/__Init__.py` file likely serves as an initialization module for the configuration management of the `readmeai` project. It may contain code to set up and define the configuration settings, allowing the project to access and utilize these settings throughout its components and modules.                                                                                                                |
| [settings.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings.py) | The code provides Pydantic models for the configuration settings of the readme-ai application. It includes models for API configuration, CLI options, Git repository configuration, Markdown code block templates, file paths, OpenAI prompts, and the entire application configuration. Additionally, there is a helper class that loads additional configuration files and a function to load and parse the configuration from a TOML file. |

</details>

<details closed><summary>Markdown</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [tree.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tree.py)             | The code is a Python class `TreeGenerator` that generates a tree structure for a given directory. It takes in a root directory, repository URL, project name, and optional maximum depth. The `generate_and_format_tree` method generates and formats the tree structure. The `_generate_tree` method recursively generates the tree structure, ignoring certain directories based on configuration settings. The `_format_tree` method formats the generated tree structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [badges.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/badges.py)         | The code is a part of a larger project for generating badges for a README file. This specific file generates badges in various styles using icons from shields.io and app iOS style badges. It reads configuration settings, dependencies, and icons from files, filters and formats the icons, and returns the badges as Markdown image tags. The code also sorts the badges based on their color and arranges them in lines to display in the README file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [template.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/template.py)     | The provided code defines a set of classes for generating readme files based on different project types. The `ReadmeTemplate` class is an abstract base class that defines the core structure and methods for rendering readme files. It has methods for rendering the project description, installation instructions, and other common sections.There are two concrete implementations of the `ReadmeTemplate` class: `LibraryTemplate` and `WebTemplate`. These classes override the `render_install` method to provide project-specific installation instructions and can also override other sections if needed.The `gen_readme` function takes a `Project` object as input. The `Project` class contains information about the project type, name, and description. The function uses the project type to select the appropriate template class from the `template_registry` dictionary. It then creates an instance of the selected template class, passes the project object to it, and calls its `render` method to generate the readme content.The provided example demonstrates the usage of the code by creating a `Project` object with type "library", name "My Library", and description "Awesome reusable code". It then calls the `gen_readme` function with the project object and prints the generated readme content. |
| [tables.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tables.py)         | The code defines functions to create Markdown tables used to format code summaries generated by LLM. The `create_markdown_tables` function formats the code summaries into a list. The `create_tables` function creates Markdown tables for each sub-directory in the project. The `create_table` function formats the data into a Markdown table. The `build_recursive_tables` function creates a Markdown table structure for a given directory, including collapsible sections for sub-directories.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [headers.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/headers.py)       | The code is part of a project that generates a README Markdown file for a codebase. It contains functions to construct different sections of the README file, format the contents of the file, and remove emojis from headers and the Table of Contents. The code also imports modules from other files within the project to perform various tasks, such as creating badges, tables, and setup instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/quickstart.py) | The code in "readmeai/markdown/quickstart.py" creates the "Getting Started" section of the README file. It takes in a configuration object, a helper object, and a list of summaries as inputs. It counts the number of occurrences of different programming languages in the summaries and determines the most commonly used language. It then retrieves the setup guide for that language from the helper object and updates the default installation, run, and test commands accordingly. If any errors occur, it falls back to using the default run command. The function returns the updated installation, run, and test commands.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

</details>

<details closed><summary>Utils</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                           |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/utils/utils.py) | The code in utils.py contains utility methods for the readme-ai application. The methods include checking if a string is a valid URL, filtering out files that should be ignored, flattening a nested list, formatting generated text, and removing text between HTML tags. These methods are used to perform various tasks and enhance the functionality of the application. |

</details>

<details closed><summary>Cli</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [options.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/options.py)   | The code in `readmeai/cli/options.py` defines options for a command line interface (CLI) related to generating README files using a large language model. These options include specifying the API key for the language model, the type of badge icons to use in the README header, whether to include emojis in the README headings, the language model engine to use, whether to generate the README offline (without the language model API), the output file path for the generated README, the repository URL or directory path, the sampling temperature for the language model, the language in which to write the README file, and the template style to use. |
| [commands.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/commands.py) | The code defines CLI commands for the readme-ai tool. It uses the click library for creating command-line interfaces. The commands function is the entrypoint for the CLI and accepts various options and arguments. It then calls the main function from `readmeai.main` module, passing the provided options and arguments. The main function is responsible for executing the desired functionality of the tool, which is generating a readme file based on the given parameters.                                                                                                                                                                                  |

</details>

<details closed><summary>Services</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [version_control.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/version_control.py) | The code provides Git-related utilities for the readme-ai project. It includes functions to make HTTP requests to retrieve metadata about repositories from GitHub, GitLab, and Bitbucket. It also includes functions to clone a repository to a temporary directory, find the path to the git executable, validate the git executable path, validate file permissions of the cloned repository, and get the file URL for a given file based on the platform. Additionally, it includes functions to extract user and repository names from a URL or path and parse the repository URL to construct the API URL. |

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
