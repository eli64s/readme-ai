<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>README-AI</h1>
<h3>◦ Revolutionize your READMEs with AI.</h3>
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

The repository readme-ai is an automated tool that generates high-quality README files for software projects. It uses AI algorithms to analyze the project code and metadata, and then generates a comprehensive README file with sections such as project description, installation instructions, usage examples, and contribution guidelines. This tool saves developers time and effort by automating the process of creating informative and professional README files, thereby improving the overall documentation quality of software projects.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architecture with clear separation of concerns. It is organized into different packages: `cli`, `config`, `core`, `markdown`, `services`, and `settings`. The `main.py` file serves as the entry point. It uses a factory design pattern to create instances of different classes. The codebase utilizes a Command Line Interface (CLI) for interaction. Overall, it follows a clean and maintainable architectural design.|
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation. There are some explanatory comments and docstrings, but a more detailed explanation of classes, functions, and usage is missing. Additional documentation, including a user guide and API documentation, would greatly improve the codebase's comprehensiveness and ease of use. |
| 🔗 | **Dependencies**   | The codebase relies on a few external libraries such as `Click`, `Pygments`, `Poetry`, and `Toml`. These libraries are well-known and widely used. The `pyproject.toml` and `poetry.lock` files define the project's dependencies and their specific versions, ensuring compatibility and reproducible builds. The codebase also depends on Docker to build and run the project. |
| 🧩 | **Modularity**     | The codebase is well-organized into modular components. Each package within the `readmeai` directory focuses on a specific functionality. The codebase follows the Single Responsibility Principle, making it easier to maintain and extend. The presence of separate packages for `cli`, `config`, `core`, `markdown`, `services`, and `settings` promotes code reusability and modularity. Adding or modifying functionality can be done by working on the relevant package, without impacting other parts of the codebase. |
| 🧪 | **Testing**        | The codebase lacks a comprehensive testing strategy. Some test cases are present in the `tests` directory, but they are limited in scope. Integration testing, unit testing, and test coverage seem to be missing. Implementing automated tests using frameworks like `pytest` would enhance code quality and help catch regressions. Continuous integration (CI) workflows defined in the `.github` directory indicate the intent for automated testing, but they are not fully utilized. |
| ⚡️  | **Performance**    | The codebase does not have any specific performance optimizations mentioned. However, it follows best practices by utilizing appropriate data structures and processing techniques. Since the code primarily operates on plain-text files, the performance is expected to be efficient. There is potential for further optimization, by leveraging caching or parallel processing for computationally intensive tasks. Profiling and benchmarking would help identify any bottlenecks and optimize accordingly. |
| 🔐 | **Security**       | The codebase does not explicitly address security concerns. It lacks input validation, authentication, and authorization mechanisms, which can pose security risks. To enhance security, proper input validation, secure file handling, and user authentication/authorization should be implemented. Additionally, using security analysis tools like static code analysis and vulnerability scanning would help identify potential security flaws. |
| 🔀 | **Version Control**| The codebase effectively uses Git for version control. The presence of multiple workflow files in the `.github/workflows` directory indicates the use

---


## 📂 Repository Structure

```sh
└── readme-ai/
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

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/main/requirements.txt) | The code provided represents a directory structure and a requirements.txt file. The structure includes various directories for code organization, such as.github, examples, readmeai, scripts, and setup. The requirements.txt file lists the dependencies required for the code, including libraries like black, click, gitpython, and pytest. The code structure and dependencies suggest that this code may involve a project related to AI-enabled README generation and documentation management.        |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/main/Dockerfile)             | This code is a Dockerfile that builds a Docker image for the "readmeai" package. It starts with a base image of Python 3.9, installs Git, creates a non-root user, and sets up the working directory. It then installs the "readmeai" package from PyPI with a pinned version and sets the command to run the CLI.                                                                                                                                                                                            |
| [Makefile](https://github.com/eli64s/readme-ai/blob/main/Makefile)                 | This Makefile provides a set of commands to facilitate repository file cleanup, code formatting, linting, and installing requirements. It also includes commands to create a conda environment (`conda`) or a virtual environment (`venv`) and install the necessary requirements. Finally, there is a command (`git-rm-cache`) to fix git untracked files.                                                                                                                                                   |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/main/pyproject.toml)     | The code represents the configuration settings and dependencies for the "readmeai" project. It includes build system requirements, project metadata (name, version, description, authors, etc.), documentation and homepage URLs, keywords, scripts, dependencies, and development dependencies. The configuration also specifies settings for code formatting (black), import sorting (isort), and testing (pytest).                                                                                         |
| [poetry.lock](https://github.com/eli64s/readme-ai/blob/main/poetry.lock)           | This is a directory tree layout of a codebase for a project called "readme-ai". It includes a variety of files and directories that organize the codebase and its functionalities. It consists of configuration files, Dockerfile, Makefile, examples, markdown templates, services, settings, and utility modules. These modules provide functionality for command-line interface (CLI), configuration settings, logging, data preprocessing, parsing, tokenization, version control, and utility functions. |

</details>

<details closed><summary>Setup</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/main/setup/setup.sh)                 | The code is a script for setting up the README-AI environment. It checks if the'tree' command is installed and installs it if necessary. It also checks if Git and Conda are installed, then checks the Python version and creates a Conda environment named'readmeai' if it doesn't already exist. Finally, it activates the environment, adds the Python path to the PATH environment variable, installs required packages from'requirements.txt', and completes the setup process. |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/main/setup/environment.yaml) | The code represents the directory tree structure of a project. It includes various files and folders that are essential for the project's functionalities. The "setup/environment.yaml" file contains the project's environment configuration, specifying the name, channels, and dependencies required to run the project.                                                                                                                                                           |

</details>

<details closed><summary>Scripts</summary>

| File                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run_batch.sh)     | The code in the "run_batch.sh" script is used to automate the process of generating readme files for multiple GitHub repositories. It defines an array of repository URLs and iterates through each one. For each repository, it extracts the repository name from the URL and passes it as an argument to the "readmeai" command line interface (CLI) tool. The CLI tool then generates a readme file for that repository by making use of the "readmeai" Python package.                                                                        |
| [build_image.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_image.sh) | The code in the `build_image.sh` script builds a Docker image called `readme-ai` with the version `latest`. It creates a buildx builder, pulls the necessary buildkit, and uses buildx to build and push the Docker image with the specified platform (linux/amd64, linux/arm64). Finally, it displays a success message with the image name and version.                                                                                                                                                                                         |
| [build_pypi.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_pypi.sh)   | The `build_pypi.sh` script is used to automate the process of building and publishing the `readmeai` package to PyPI. This script performs the following steps:1. Runs the `clean.sh` script to clean any previous build artifacts.2. Builds the package using the `python-m build` command.3. Uses `twine` to upload the package to PyPI, using the `--repository-url` flag to specify the PyPI repository and the `-u` and `-p` flags to authenticate using a PyPI API key.4. Displays a success message once the package is published to PyPI. |
| [run.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run.sh)                 | The `run.sh` script is responsible for running the `readmeai` Python package. It first exports any necessary environment variables and activates the `readmeai` conda environment. Then, it executes the `readmeai` package by running the `python3-m readmeai.cli.commands` command, specifying the output file name (`-o readme-ai.md`) and the GitHub repository URL (`-r https://github.com/eli64s/readme-ai`).                                                                                                                               |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/clean.sh)             | The code in "scripts/clean.sh" is a bash script that provides a set of commands for cleaning up build artifacts, Python file artifacts, test and coverage artifacts, backup files, and Python cache files. It offers various subcommands such as clean, clean-build, clean-pyc, clean-test, and clean-backup-and-cache, which can be executed from the command line to perform different types of cleaning operations.                                                                                                                            |
| [test.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/test.sh)               | The code in `test.sh` is a script that sets up the environment for running tests, generates a coverage report, and cleans up afterward. It activates the `readmeai` Conda environment, defines directories to include and exclude from the coverage report, runs the tests using `pytest` with coverage, and displays the coverage report. It then removes unnecessary files and folders, such as `__pycache__`, `.pytest_cache`, `.coverage`, and any files matching `*local_dir*` in the `tests` directory.                                     |

</details>

<details closed><summary>.github</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/release-drafter.yml) | The code above is a configuration file for the release drafter feature in GitHub. It specifies the templates and categories to be used for generating release notes based on git commit messages. The templates include the name and tag format for releases, as well as the categories for different types of changes like features, bug fixes, and documentation updates. The configuration also defines how the changes are formatted in the release notes. |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-drafter.yml) | This code is a GitHub Actions workflow file called "release-drafter.yml". The workflow is triggered by pushes to the main branch and specific events related to pull requests. The workflow has permission to read the contents of the repository and write contents and pull requests. It runs on an Ubuntu environment. The steps include setting the GHE_HOST variable (optional) and using the "release-drafter/release-drafter@v5" action, which drafts the next release notes based on the merged pull requests. The action is configured with the GITHUB_TOKEN secret for authentication. |
| [publish_package.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/publish_package.yml) | This code sets up a workflow to automatically publish a Python package to PyPI (Python Package Index). It is triggered on a push to the `main` branch or when a new release is created. The workflow checks out the code, sets up Python, installs the necessary dependencies, builds the package, and finally publishes it using Twine. The PyPI API token is retrieved from GitHub secrets to securely authenticate the upload.                                                                                                                                                                |
| [build_image.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/build_image.yml)         | The code is a GitHub Actions workflow script that builds and pushes a Docker image to Docker Hub. It is triggered on the push to the main branch and the creation of a new release. The script checks out the code, sets up QEMU and Docker Buildx, logs in to Docker Hub using credentials stored as secrets, and then builds and pushes the Docker image using the docker/build-push-action@v4 action. The image is built for three platforms: linux/amd64, linux/arm/v7, and linux/arm64/v8, and is tagged as zeroxeli/readme-ai:latest.                                                      |

</details>

<details closed><summary>Readmeai</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [main.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/main.py) | The code represents the main entrypoint for a Python application called readme-ai. It imports various modules and functions for the application's core functionalities, including logging, model handling, preprocessing, and README file generation. The main function takes in several parameters related to the configuration of the application and executes the readme_agent function asynchronously. The readme_agent function orchestrates the README file generation process, including cloning the repository, generating a repository tree, parsing dependencies, generating code summaries, and finally generating the README.md file. |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/ignore_files.toml)         | The code represents a configuration file, "ignore_files.toml", which contains a list of files, directories, and file extensions to be ignored. These ignored files/directories are typically excluded from version control or other processes. The file contains three sections: "ignore_files" with a list of directories to be ignored, "extensions" with a list of file extensions to be ignored, and "files" with a list of specific files to be ignored.                                                                                                               |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_names.toml)     | The code above represents a directory tree structure that contains various files and directories. The specific code snippet shown is from the file "language_names.toml" located in the "readmeai/settings" directory. This file maps programming language file extensions to their corresponding names. Each language extension is associated with a specific name, such as "asm" corresponding to "Assembly" or "c" corresponding to "C". This mapping can be used to identify and label programming languages based on file extensions.                                  |
| [identifiers.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/identifiers.toml)           | The code is a configuration file that defines identifiers for different project types. Each project type is associated with a list of keywords that are commonly found in that type of project. These project types include web, mobile, desktop, backend, frontend, game, data, machine learning (ml), library, CLI, API, plugin, and embedded. This configuration file is used to identify project types based on the presence of these keywords in code repositories during analysis or processing.                                                                      |
| [config.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml)                     | The code provided is a configuration file written in TOML format. It contains various settings and templates used by a program called `readmeai`. The settings include API and CLI options, paths to dependency files, repository details, markdown templates, and prompts for generating documentation. The templates define the structure of the generated markdown documents, including tables, headers, badges, dropdowns, and an overview. The prompts provide instructions for the user to provide a technical analysis of the codebase and its components.           |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/dependency_files.toml) | The code above represents a configuration file for the dependency file names in various programming languages. It lists the common names of files that contain dependencies for each language. This configuration file is used by a tool or system to identify and manage dependencies in different projects written in various programming languages.                                                                                                                                                                                                                      |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_setup.toml)     | The code represents the directory tree structure of a project called "readme-ai" and its various files and folders. It includes a Dockerfile, Makefile, examples, poetry.lock, pyproject.toml, readmeai folder with subfolders for different functionalities, settings folder, utils folder, scripts folder, and setup folder. The specific file "language_setup.toml" within the "readmeai/settings" folder contains instructions for setting up and running different programming languages, including commands for building, running, and testing code in each language. |

</details>

<details closed><summary>Core</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/preprocess.py) | The code in `readmeai/core/preprocess.py` provides functionalities for preprocessing a codebase. It includes a `RepositoryParser` class that handles preprocessing tasks such as generating file information, extracting dependency file contents, mapping file extensions to programming languages, and tokenizing file content. It also provides methods for analyzing a local or remote git repository, extracting dependencies, and retrieving file contents. Overall, this code performs various preprocessing operations on a codebase to enable further analysis and processing.                                             |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/tokens.py)         | The code in `readmeai/core/tokens.py` provides utility functions for handling language tokens. It includes functions for adjusting the maximum number of tokens based on a specific prompt, counting the number of tokens in a text string, getting the token encoder to use for the model, and truncating a text string to a maximum number of tokens.                                                                                                                                                                                                                                                                             |
| [logger.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/logger.py)         | This code defines a custom logger class for the project. It allows for logging messages at different levels (info, debug, warning, error, critical), and configures the logger to format and colorize the log messages. The logger is implemented as a singleton, meaning there is a single instance of the logger class that can be accessed from anywhere in the project.                                                                                                                                                                                                                                                         |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/factory.py)       | The `FileHandler` class in `factory.py` is a factory class that handles file I/O operations. It provides methods to read and write various file formats such as JSON, Markdown, TOML, TXT, and YAML. The class uses a cache to store the contents of files that have already been read, improving performance. It also supports exception handling for file read and write operations.                                                                                                                                                                                                                                              |
| [model.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/model.py)           | The code represents a Tech Lead who handles API requests to OpenAI to generate text for a README.md file. It uses large language models to convert code files to natural language text by making API calls with custom prompts. The code can handle rate limiting, caching, and exceptions.                                                                                                                                                                                                                                                                                                                                         |
| [parser.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/parser.py)         | The code includes a set of methods to parse and extract dependency file metadata. It provides functions to parse various file formats like JSON, TOML, YAML, Docker Compose, Conda environment, Pipfile, poetry.lock, pyproject.toml, requirements.txt, Cargo.toml, Cargo.lock, package.json, yarn.lock, package-lock.json, go.mod, build.gradle, pom.xml, CMakeLists.txt, configure.ac, and Makefile.am. Each parsing function takes the content of the file as input and returns a list of dependencies or keys extracted from the file. The code also provides a function to get a dictionary of all the supported file parsers. |

</details>

<details closed><summary>Config</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [__Init__.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/__Init__.py) | The code is an empty `__Init__.py` file located in the `config` directory of the `readme-ai` project. It serves as an initializer for the `config` module. Its purpose is to mark the `config` directory as a Python package and allow it to be imported and used by other modules in the project.                                                                                                                                                        |
| [settings.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings.py) | The code above defines Pydantic models for the readme-ai application's configuration settings. It includes models for API configuration, CLI options, Git repository configuration, Markdown templates, file paths, prompts, and the overall application configuration. The code also provides a helper class to load additional configuration files. There are functions to load the configuration constants and to load the configuration helper files. |

</details>

<details closed><summary>Markdown</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [tree.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tree.py)             | The code provided is a TreeGenerator class that generates and formats a tree structure for a given directory. It takes a root directory, repository URL, project name, and maximum depth as inputs. The generate_and_format_tree() method generates and formats the tree structure using the _generate_tree() and _format_tree() methods. The _generate_tree() method recursively generates the tree structure by iterating over the directories and files in the directory. The _format_tree() method formats the generated tree structure.                                                                                           |
| [badges.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/badges.py)         | The code in `readmeai/markdown/badges.py` generates badges for a README file. It defines functions to format SVG icons into Markdown image tags, retrieve badges for project dependencies, generate markdown templates for badges, and get README badges using shields.io badges or app iOS style badges.                                                                                                                                                                                                                                                                                                                              |
| [template.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/template.py)     | The code defines a hierarchy of directory structure and a Python class model for generating README templates. The `ReadmeTemplate` class is an abstract base class with common methods for rendering sections of a README template. The `LibraryTemplate` and `WebTemplate` classes are concrete implementations of `ReadmeTemplate` that override certain methods. The `gen_readme()` function takes a `Project` object and generates a README template based on its type, using the appropriate template implementation. The example at the bottom demonstrates the usage of the code.                                               |
| [tables.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tables.py)         | The code in the `tables.py` file creates Markdown tables used to format the code summaries generated by the LLM (Language Model) tool. The `create_markdown_tables` function formats the code summaries into a list. The `create_tables` function creates Markdown tables for each sub-directory in the project, grouping the summaries by sub-folder. The `create_table` function generates a Markdown table from the given data, including file names and summaries. The `build_recursive_tables` function recursively creates a Markdown table structure for a given directory, including collapsible sections for sub-directories. |
| [headers.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/headers.py)       | The code in `headers.py` is part of a larger codebase (in the `readmeai` package) that builds the README Markdown file for a code repository. The code includes functions to construct the various sections of the README file, format the contents for each section, and remove emojis from headers and the Table of Contents. It also handles creating badges, tables, and setup instructions for the README.                                                                                                                                                                                                                        |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/quickstart.py) | The code in `quickstart.py` generates the'Quick Start' section of a README file. It takes in configurations (`conf` and `helper`) and a list of summaries. Inside the function, it calculates language counts based on file suffixes, filters out ignored files, and determines the most common language and its setup guide. If the setup guide has at least 3 steps, it updates the default installation, run, and test commands. If any exception occurs during the process, it falls back to the default setup guide. The function returns the default installation, run, and test commands.                                       |

</details>

<details closed><summary>Utils</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                   |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                       |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/utils/utils.py) | The code in the `utils.py` file provides utility methods for the `readme-ai` application. It includes functions to check if a string is a valid URL, flatten a nested list, format generated text from a model, remove text between HTML tags, and filter out files that should be ignored based on a configuration file. |

</details>

<details closed><summary>Cli</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [options.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/options.py)   | The code in `readmeai/cli/options.py` provides options for the command line interface of the `readme-ai` tool. These options include:-`api_key`: Secret key for the Large language model API.-`badges`: Specifies the type of badge icon to use in the README.md header.-`emojis`: Enables or disables the use of emojis in README heading sections.-`model`: Specifies the large language model engine to use.-`offline`: Generates a README.md without using the Large language model API when set to `True`.-`output`: Specifies the output file path for the generated README.md.-`repository`: Specifies the URL or directory path of the repository.-`temperature`: Specifies the temperature for language model sampling.-`language`: Specifies the language to write the README.md file in.-`style`: Specifies the template to use for the README.md file. |
| [commands.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/commands.py) | The code is a command-line interface (CLI) for the "readme-ai" project. It uses the Click library to define CLI commands and options. The main function is called when the CLI is executed and it passes the provided options as arguments. The CLI allows the user to generate a readme file for a repository using various options such as API key, badges, emojis, offline mode, model, output file path, repository URL, temperature, language, and style.                                                                                                                                                                                                                                                                                                                                                                                                     |

</details>

<details closed><summary>Services</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [version_control.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/version_control.py) | The code provides a set of utility functions for version control services. It includes functions to make HTTP requests to retrieve repository metadata, clone a repository to a temporary directory, extract user and repository names from a URL or path, generate the URL for a file based on the platform, parse a repository URL and construct an API URL, find the path to the git executable, and validate file permissions and the git executable path. |

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

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/readme-ai/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/eli64s/readme-ai/issues)**: Submit bugs found or log feature requests for ELI64S.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
