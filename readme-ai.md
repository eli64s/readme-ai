<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>readme-ai</h1>
<h3>◦ Here is an 80-character slogan for the readme-ai project on GitHub:"Automatically generate readable READMEs so you can focus on code!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/SVG-FFB13B.svg?style&logo=SVG&logoColor=black" alt="SVG" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />

<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/license/eli64s/readme-ai?style&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/eli64s/readme-ai?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
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

Here is a 3 sentence overview of the readme-ai project:The readme-ai project is an open-source tool that automates the generation of README files for GitHub repositories through natural language interactions. By analyzing a codebase and using AI assistants, it is able to summarize projects, dependencies, usage instructions and more to produce comprehensive yet succinct README documentation. This helps developers quickly onboard to new projects and understand how to get started with compiling, testing and using the code with little manual effort.

---

## 📦 Features

 Here is a Markdown table analyzing the key features of the Readme AI codebase:

|    | Feature            | Description |
|-|-|-|
| ⚙️ | **Architecture**   | The system is designed with a modular architecture, separating code into logical components (md_builder, cli) to generate Markdown files programmatically. |
| 📄 | **Documentation**  | Docstrings and comments describe classes, functions and arguments clearly. Usage and development guides help new users and contributors get started quickly. |
| 🔗 | **Dependencies**   | External dependencies include Python libraries for Markdown parsing (mdformat), argument parsing (click) and testing (pytest). This allows the system to focus on its core functionality. |  
| 🧩 | **Modularity**     | Code is organized into distinct modules for the Markdown builder, CLI interface and tests. Individual components can be developed and tested independently. |
| 🧪 | **Testing**        | Automated unit tests use Pytest and cover key functions to prevent regressions and ensure the system works as intended. Testing strategies facilitate continuous integration. |
| ⚡️ | **Performance**    | As a CLI tool to generate Markdown files from templates, the system has good performance for its use cases without unnecessary complexity. Resource usage is optimized through its modular design. |
| 🔐 | **Security**       | As an open source tool without authentication or sensitive data, the focus is on secure development practices like keeping dependencies up-to-date and following best practices. |
| 🔀 | **Version Control**| Git is used for version control, including a clear commit history and README providing guidance for contributing to the project. |
| 🔌 | **Integrations**   | The CLI interface allows customizing Markdown generation through configuration files or programmatic calls, enabling diverse integrations based on user needs. |
| 📶 | **Scalability**    | The modular design allows the system to easily accommodate additional features and growth over time without compromising organization or performance.

---


## 📂 Repository Structure

```sh
└── readme-ai/
    ├── .dockerignore
    ├── .github/
    │   ├── release-drafter.yml
    │   └── workflows/
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── docs/
    │   ├── README-fr.md
    │   └── README-zh-CN.md
    ├── examples/
    │   ├── imgs/
    │   ├── readme-energy-forecasting.md
    │   ├── readme-fastapi-redis.md
    │   ├── readme-go.md
    │   ├── readme-java.md
    │   ├── readme-javascript.md
    │   ├── readme-kotlin.md
    │   ├── readme-lanarky.md
    │   ├── readme-mlops.md
    │   ├── readme-pyflink.md
    │   ├── readme-python.md
    │   ├── readme-rust-c.md
    │   └── readme-typescript.md
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai/
    │   ├── __init__.py
    │   ├── cli/
    │   ├── core/
    │   ├── data/
    │   ├── main.py
    │   ├── md_builder/
    │   ├── settings/
    │   └── utils/
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
    └── tests/
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
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/main/requirements.txt) | Package dependencies for:-Code testing (pytest, responses, pytest-cov)-Linting (black, isort, flake8)-Formatting (black)-CLI building (click)-API client (httpx, openai)-Caching (cachetools)-YAML and TOML (pyyaml, toml)-Data validation (pydantic)-Git integration (gitpython)-Table printing (tabulate)-Retrying functions (tenacity)-HTTP/2 (h2)-Pre-commit hooks (pre-commit)-REST API mocking (ruff)-TikTok API (tiktoken) |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/main/Dockerfile)             | This Dockerfile sets up a Python development environment with Readme AI CLI pre-installed. It defines a non-root user, sets that user as the default, installs dependencies, and configures the image to run the Readme AI CLI command on container start.                                                                                                                                                                        |
| [Makefile](https://github.com/eli64s/readme-ai/blob/main/Makefile)                 | This Makefile contains commands to automate development tasks, including setting up a virtual environment for the codebase using either Conda or venv, formatting code style with tools like pylint and black, cleaning temporary files, and fixing untracked git changes.                                                                                                                                                        |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/main/pyproject.toml)     | This file defines configuration for the README.ai CLI tool: it specifies dependencies, build requirements/scripts, testing/linting, and coverage specifications. Poetry manages the package, dependencies are listed, build uses Masonry, scripts define the CLI, tests/linting on save via pre-commit, and coverage excludes certain files/folders.                                                                              |

</details>

<details closed><summary>Setup</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                  |
| ---                                                                                      | ---                                                                                                                                                                                                                      |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/main/setup/setup.sh)                 | This script sets up a Python conda environment for a project, checking and installing dependencies, then creating and activating the'readmeai' environment to configure the PATH and install additional Python packages. |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/main/setup/environment.yaml) | Defines core packages for a Python environment-Python 3.9, pip, and installation via pip. Allows reproducibility and shareability of the environment.                                                                    |

</details>

<details closed><summary>Scripts</summary>

| File                                                                                   | Summary                                                                                                                                                                                                                                                                                  |
| ---                                                                                    | ---                                                                                                                                                                                                                                                                                      |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run_batch.sh)     | This bash script iterates through an array of GitHub repository URLs, extracts the repository name from each URL, and uses the ReadmeAI Python module to generate areadme file for that repo, naming it based on the extracted name.                                                     |
| [build_image.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_image.sh) | This shell script automates building and pushing a Docker image. It sets variables for image name and tag, builds the image using BuildKit, and pushes it to a repository, tagging with the provided name and version.                                                                   |
| [build_pypi.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/build_pypi.sh)   | This script builds a Python package, cleans previous builds, creates a new build, and uploads it to PyPI using Twine with the necessary credentials.                                                                                                                                     |
| [run.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run.sh)                 | This shell script activates a Conda env, then uses the ReadmeAI Python library to generate documentation from a GitHub repo. It retrieves the repo at the given URL, and writes an output README file.                                                                                   |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/clean.sh)             | This script removes temporary, cached and backup files to clean a Python project directory. It finds and deletes artifacts like.py[co] files, empty directories like __pycache__ as well as build artifacts, logs and other miscellaneous files.                                         |
| [test.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/test.sh)               | This Bash script runs Python tests with coverage reporting, then cleans up redundant files. It activates a Conda environment, sets source/omit dirs for coverage, runs Pytest with coverage, produces a coverage report, then removes __pycache__, cache, coverage and local test files. |

</details>

<details closed><summary>.github</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/release-drafter.yml) | This release drafter file automates the creation of GitHub release notes. It defines templates for the release name, tag, categories of changes, individual changes, resolving the semantic version number, and the overall release notes template. This provides a structured, repeatable process for documenting new features, bug fixes, and other changes between releases in a format aligned with semantic versioning and the Keep a Changelog standard. |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                            |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-drafter.yml) | This YAML workflow file automates the release process by drafting release notes as pull requests are merged. It watches default and custom branches for pushes/PR events, reads release template files, and publishes release notes/tags using the GitHub API token on PR integration.             |
| [publish_package.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/publish_package.yml) | This GitHub Action publishes a Python package to PyPI on main branch pushes or releases. It installs dependencies, builds the package, and uploads the built artifacts to PyPI using twine with the secret API token env vars.                                                                     |
| [build_image.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/build_image.yml)         | This workflow configures GitHub actions to build and push a Docker image upon code commits to main branch or release creation. It sets up QEMU and Docker Buildx for multi-architecture builds, logs into Docker Hub, then builds and pushes the image with specified tags across Linux platforms. |

</details>

<details closed><summary>Readmeai</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                              |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                  |
| [main.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/main.py) | This Python application generates README files through natural language interactions. It clones a Git repository, analyzes file structure and dependencies, then uses a large language model to write descriptive text for the README based on developer-provided prompts. The formatted Markdown is assembled and output to a file. |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/ignore_files.toml)         | This file defines a set of file paths and extensions to ignore when parsing a repository's contents, to exclude automatically generated, temporary, and test/cache files like.git,.tox, and __pycache__. It improves parsing performance and relevance.                                                                                                                                                                                                                                              |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_names.toml)     | This file provides a mapping of common file extensions to their associated programming language names. This allows identification of a file's language based on its extension for proper syntax highlighting and other automated functions.                                                                                                                                                                                                                                                          |
| [config.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml)                     | This configuration file contains the settings for readmeai, an AI assistant for creating README files on GitHub. It defines the OpenAI API credentials for query completion, as well as paths for file I/O. Prompt templates are provided to generate Markdown content summarizing code, projects features, getting started instructions, and more. The structured prompts andMarkdown template code enable the assistant to automatically generate comprehensive yet succinct README documentation. |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/dependency_files.toml) | This configuration file defines a list of common dependency file names mapped to different programming languages. It provides a list of standard filenames that may indicate dependencies managed or built for a project, to help identify the libraries and tools required to compile, test and run the code.                                                                                                                                                                                       |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_setup.toml)     | This file outlines build and run instructions for various programming languages, including commands to compile/interpret code, execute the main program, and run unit tests where applicable. It provides a standardized starting point for local development and testing across different languages.                                                                                                                                                                                                |

</details>

<details closed><summary>Core</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [config.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/config.py)         | This Python code defines Pydantic models and helpers for loading configuration from TOM files in the readme-ai project. Key-value files specify various app settings like API keys, output paths, documentation templates. Models validate values and allow accessing configs as objects. Loading and merging of multiple config files handled to provide flexible configuration.                                                                              |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/preprocess.py) | This code handles preprocessing functions for README generation. It analyzes code repositories, identifies files and languages, extracts dependencies, and tokenizes file contents. Key steps include generating file information, mapping extensions to languages, retrieving dependency contents, and processing the data into a standardized format with tokens and language details to serve as structured input for postprocessing and report generation. |
| [logger.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/logger.py)         | This Python file defines a custom Logger class that provides color logging functionality. It uses the singleton pattern to ensure only one logger instance exists per name. Logger methods configure color formatting and call the corresponding logging methods while passing messages to the underlying logging module.                                                                                                                                      |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/factory.py)       | This factory class provides a unified API for reading from and writing to different file formats. It supports JSON, Markdown, TOML, TXT and YAML files, handling the appropriate parser/formatter for each. Files are cached for efficient reading. Formatted content is written via selected methods based on file extension. Errors are raised for unsupported formats or I/O failures.                                                                      |
| [model.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/model.py)           | This code handles interactions with OpenAI's API to generate natural language summaries of source code files. It initializes an HTTP client, retries requests on failure, validates responses and manages rate limiting. Given code snippets, it parallelizes API requests to summarize each one, handles errors, caches responses and returns results while abstracting away complexities of the API.                                                         |
| [parser.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/parser.py)         | This module contains functions to parse various dependency and package files to extract core metadata like dependencies, projects/libraries, and services. Each file type has a dedicated parsing method handling the different file formats including JSON, YAML, TOML and plain text. The parsed data is returned as lists for further processing.                                                                                                           |

</details>

<details closed><summary>Utils</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/utils/tokens.py) | This module provides token-related utility functions for text generation. It can adjust the max tokens based on prompt validity, count tokens in text, and truncate text to a set number of tokens. This allows the system to carefully analyze input text and apply token limits for improved precision during natural language generation.                                                                                                                                                      |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/utils/utils.py)   | This file contains several utility functions used throughout the application:-is_valid_url checks if a string is a valid URL-flatten_list flattens a nested list into a single level list-format_sentence cleans text by removing whitespace and formatting sentences-remove_substring removes text between HTML tagsThese functions provide common reusable operations like input validation, data formatting and cleaning to produce consistent output.                                         |
| [github.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/utils/github.py) | This module provides utility functions for cloning GitHub repositories to temporary directories and retrieving data from GitHub repositories, including:-clone_repo_to_temp_dir() clones a repo to a temp dir, removes.git, and validates the clone-find_git_executable() finds the Git executable path-validate_git_executable() validates the Git executable-get_github_file_link() generates a URL for a file-get_user_repository_name() parses the username and repo from a URL or local path |

</details>

<details closed><summary>Cli</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                  |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                      |
| [options.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/options.py)   | This file defines option parameters for the CLI interface. It specifies click Options for API key, badge style, text encoding, API endpoint, language model, offline mode, output path, repository, temperature, language, and style to customize the README generation. |
| [commands.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/commands.py) | This file defines the CLI commands for readme-ai using Click. It sets up command line options for API key, badges, encoding etc and maps them to the main() function from readmeai.main to execute the core NLP generation tasks based on the provided parameters.       |

</details>

<details closed><summary>Md_builder</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                  |
| [tree.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/md_builder/tree.py)       | This Python module generates a Markdown-formatted directory tree recursively by taking a root path and generating indented branches. It returns a string representing the tree structure with a maximum depth of 2 levels, where subdirectories and files are displayed with unicode box characters to visualize the hierarchy.                                                      |
| [badges.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/md_builder/badges.py)   | This Python module generates badges from dependency data to display in a project README. It retrieves logo icons, maps dependencies to badge SVGs, sorts by color, and formats them as Markdown images with configurable formatting of badge groupings.                                                                                                                              |
| [tables.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/md_builder/tables.py)   | This Python module generates Markdown tables that summarize directories and files within a codebase. It recursively maps the directory structure, extracts file paths and summaries, then organizes these into collapsible tables within Markdown. Tables are created for the root and each sub-directory, with file names and summaries formatted and linked to their GitHub paths. |
| [headers.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/md_builder/headers.py) | This Python module builds the README.md file for a codebase. It inserts various sections like headers, badges, tables of contents generated from code metadata. Config settings specify formatting and content. External APIs are used to fetch additional info. Sections are constructed and joined to create the final Markdown file, which is written to disk.                    |
| [usage.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/md_builder/usage.py)     | This code analyzes a project's codebase to generate a customized "Getting Started" guide for the README. It counts languages used, identifies the most common, maps it to commands for install/run/test. Default commands are returned if errors occur, providing project-specific onboarding instructions.                                                                          |

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


## 🛣 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
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

This project is licensed under the `ℹ️  LICENSE-TYPE` License. See the [LICENSE-Type](LICENSE) file for additional info.

---

## 👏 Acknowledgments

`- ℹ️ List any resources, contributors, inspiration, etc.`

[↑ Return](#Top)

---
