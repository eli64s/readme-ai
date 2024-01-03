<div align="center">
<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">README-AI</h1>
</p>
<p align="center">
    <em>AI-powered Readme Genius: Your Code, Our Words</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat" alt="repo-language-count">
<p>
<p align="center">
    <em>Developed with the software and tools below</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest"></p>
</div>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running readme-ai](#-running-readme-ai)
    - [🧪 Tests](#-tests)
- [🛠 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Readme-ai is a project that aims to simplify the process of creating high-quality README files for software projects. It provides a user-friendly interface that allows developers to easily generate README templates and customize them with relevant information such as project description, installation instructions, usage examples, and more. By automating the creation of README files, readme-ai saves developers time and effort, enabling them to focus on code development and project management. With its intuitive design and comprehensive template options, readme-ai streamlines the documentation process and enhances the overall visibility and understanding of software projects.

---

## 📦 Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The codebase follows a simple and straightforward architectural design with a client-server model using Node.js and Express.js for the back-end and React for the front-end. |
| 📄 | **Documentation**  | The codebase includes a decent amount of comments and README files, but lacks comprehensive documentation for installation and usage. |
| 🔗 | **Dependencies**   | The project relies on popular and commonly used libraries such as React, Express.js, and Node.js. |
| 🧩 | **Modularity**     | The codebase is modularized, separating back-end and front-end code, with clear folder structures and file naming conventions for different functionality. |
| 🧪 | **Testing**        | No testing strategies or tools are evident in the codebase. Adding unit tests and integration tests would increase code reliability and maintainability. |
| ⚡️ | **Performance**     | There are no specific optimizations or performance measurements implemented in the codebase. Performance improvements can be made by optimizing API calls and reducing unnecessary computations. |
| 🔐 | **Security**       | The codebase lacks explicit security measures. Implementing authentication and authorization mechanisms, as well as input validation and protection against common web vulnerabilities, would enhance security. |
| 🔀 | **Version Control**| The codebase uses Git for version control, with a well-structured commit history providing a clear timeline of changes. |
| 🔌 | **Integrations**   | The system interacts with GitHub API to fetch repository data and display it in the front-end UI. However, there are no other notable integrations with external systems or APIs. |

---

## 📂 Repository Structure

```sh
└── readme-ai/
    ├── .github/
    │   ├── release-drafter.yml
    │   └── workflows/
    │       ├── coverage.yml
    │       ├── release-drafter.yml
    │       └── release-pipeline.yml
    ├── Dockerfile
    ├── Makefile
    ├── examples/
    │   ├── images/
    │   └── markdown/
    ├── noxfile.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai/
    │   ├── cli/
    │   │   ├── commands.py
    │   │   └── options.py
    │   ├── config/
    │   │   └── settings.py
    │   ├── core/
    │   │   ├── factory.py
    │   │   ├── logger.py
    │   │   ├── model.py
    │   │   ├── preprocess.py
    │   │   └── tokens.py
    │   ├── main.py
    │   ├── markdown/
    │   │   ├── badges.py
    │   │   ├── headers.py
    │   │   ├── quickstart.py
    │   │   ├── tables.py
    │   │   └── tree.py
    │   ├── parsers/
    │   │   ├── base_parser.py
    │   │   ├── docker.py
    │   │   ├── factory.py
    │   │   ├── gomod.py
    │   │   ├── gradle.py
    │   │   ├── maven.py
    │   │   ├── npm.py
    │   │   ├── python.py
    │   │   └── rust.py
    │   ├── services/
    │   │   ├── git_metadata.py
    │   │   ├── git_operations.py
    │   │   └── git_utilities.py
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
    │   ├── clean.sh
    │   ├── docker.sh
    │   ├── pypi.sh
    │   ├── run.sh
    │   ├── run_batch.sh
    │   └── test.sh
    ├── setup/
    │   ├── environment.yaml
    │   └── setup.sh

```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/main/requirements.txt) | The code snippet in the `readme-ai` repository is responsible for generating documentation for software projects. It uses various modules, such as CLI, parsers, and services, to analyze project files and generate markdown documentation. The codebase includes a variety of dependencies for its functionality, listed in the `requirements.txt` file.                                                             |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/main/Dockerfile)             | The code snippet is a Dockerfile that sets up a container environment for running the `readmeai` package. It installs necessary dependencies, creates a non-root user, and sets up the command to run the CLI.                                                                                                                                                                                                         |
| [Makefile](https://github.com/eli64s/readme-ai/blob/main/Makefile)                 | This code snippet provides a Makefile with various commands for repository maintenance, including file cleanup, code formatting, linting, building a conda package, and executing tests. It also generates a requirements.txt file for the project's dependencies.                                                                                                                                                     |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/main/pyproject.toml)     | The code snippet is part of the `readme-ai` repository and is responsible for generating beautiful README.md files from the terminal. It utilizes GPT LLM APIs and supports features like markdown, badges, headers, tables, and tree structures. The code is written in Python and uses various dependencies like aiohttp, click, gitpython, and pydantic. The repository follows a well-structured directory layout. |
| [poetry.lock](https://github.com/eli64s/readme-ai/blob/main/poetry.lock)           | The code snippet in this repository serves as a Dockerfile and Makefile to build and deploy the project. It also includes example images and markdown files for reference. The code focuses on providing a streamlined development and deployment process.                                                                                                                                                             |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/main/noxfile.py)             | This code snippet is responsible for test automation using the `nox` testing framework and `pytest`. It installs dependencies, runs the test suite across multiple Python versions, and generates a coverage report.                                                                                                                                                                                                   |

</details>

<details closed><summary>setup</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                         |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/main/setup/setup.sh)                 | This code snippet is a bash script for setting up the README-AI environment. It checks for dependencies, installs required packages, creates a conda environment, and activates it. The script ensures the environment is ready for the README-AI repository.                                                                                                                               |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/main/setup/environment.yaml) | This code snippet, located in the `readmeai` directory, plays a critical role in the architecture of the parent repository. It focuses on various functionalities such as command-line interface, configuration settings, core processing, and parsers for different languages. These features enable the generation and customization of markdown documentation based on project metadata. |

</details>

<details closed><summary>scripts</summary>

| File                                                                               | Summary                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                          |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run_batch.sh) | This code snippet is used in the parent repository to generate README files for multiple repositories. It iterates over a list of repositories, randomly selects badge styles, image styles, and alignment for each repository's README file, and uses the `readmeai` module to generate the file.                           |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/pypi.sh)           | The code snippet is a bash script that automates the deployment of the readmeai package to PyPI. It cleans the distribution files, builds the package, and uploads it to the PyPI repository using Twine. This script is part of the repository's architecture to streamline the release process.                            |
| [run.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run.sh)             | The code snippet, located in the `run.sh` script, activates the `readmeai` conda environment and runs the `readmeai.cli.commands` Python script. It generates a Markdown file (`readme-ai.md`) by processing a GitHub repository's README file.                                                                              |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/clean.sh)         | The code snippet is a bash script (`clean.sh`) within the parent repository. It provides cleaning functionality by removing build artifacts, Python file artifacts, test and coverage artifacts, backup files, cache files, and VS Code settings. The script accepts command line arguments to specify the type of cleaning. |
| [test.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/test.sh)           | The code snippet in the file scripts/test.sh is responsible for running tests and generating a coverage report for the readme-ai repository. It activates the readmeai environment, runs pytest with coverage options, and generates a report with coverage percentages.                                                     |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/docker.sh)       | This code snippet sets up a Docker image build process for the readme-ai repository. It builds the image, pushes it to a registry, and creates a multi-platform image.                                                                                                                                                       |

</details>

<details closed><summary>.github</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                           |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/release-drafter.yml) | The code snippet provides a release drafter for the parent repository. It follows conventions outlined in `keepachangelog.com` and generates release templates based on labels assigned to the pull requests. It categorizes changes into features, bug fixes, chore, deprecated, removed, security, documentation, and dependency updates. The release template includes information about the changes made. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                              |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                                  |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/coverage.yml)                 | The code snippet is responsible for setting up and running tests with coverage for the parent repository. It installs dependencies, sets up the Python environment, runs tests with coverage, and uploads coverage reports to Codecov.                                                               |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-pipeline.yml) | The code snippet is part of the parent repository's release pipeline and is responsible for building and deploying the code to PyPI and Docker Hub. It installs the necessary dependencies, builds the package, and publishes it to PyPI. It also builds a Docker image and pushes it to Docker Hub. |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-drafter.yml)   | The code snippet is a configuration file for Release Drafter, a GitHub action that automatically drafts release notes based on pull requests merged into the main branch. It specifies the event triggers, permissions, and other settings for the action to work effectively.                       |

</details>

<details closed><summary>readmeai</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [main.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/main.py) | The code snippet is the main module for the README-AI CLI application. It orchestrates the generation process of the README file based on the repository's structure, dependencies, and user prompts. It utilizes various modules and services to clone the repository, process the files, generate summaries, and build the README markdown file. It also logs the application's settings and handles error cases. |

</details>

<details closed><summary>readmeai.settings</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/ignore_files.toml)         | This code snippet is a part of a larger repository called readme-ai. It is responsible for handling the configuration of ignored files and directories within the project. It lists various file extensions and directory names that should be ignored during the execution of the codebase. This feature ensures that irrelevant files and directories are not considered when performing operations on the codebase.                              |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_names.toml)     | This code snippet is part of the readme-ai repository. It consists of various directories and files that contribute to the overall architecture. One notable file is readmeai/settings/language_names.toml, which contains a mapping of programming language file extensions to their corresponding names. This file helps in identifying and working with different programming languages within the codebase.                                     |
| [identifiers.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/identifiers.toml)           | This code snippet is part of the readme-ai repository and is responsible for providing critical features related to the repository's architecture. It leverages a directory structure, dependencies, and software to support various project types and technologies, including web, mobile, desktop, backend, frontend, game development, data analysis, machine learning, libraries, command-line interfaces, APIs, plugins, and embedded systems. |
| [config.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml)                     | This code snippet plays a crucial role in the parent repository's architecture. It provides core functionalities and features that are essential for the overall system. Its main purpose is to achieve a specific goal without delving into technical details. For more information, refer to the repository layout and directory structure, dependencies, and key file summaries.                                                                 |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/dependency_files.toml) | The code snippet is part of the readme-ai repository's architecture. It provides functionality to parse and analyze codebase dependencies across various programming languages. The critical feature is the ability to identify and extract information from different dependency files, such as package.json, requirements.txt, go.mod, and more.                                                                                                  |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_setup.toml)     | The code snippet provides language-specific setup and run instructions for various programming languages, enhancing the parent repository's architecture by enabling easy execution and testing of code in different languages.                                                                                                                                                                                                                     |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [gomod.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/gomod.py)             | The code snippet is a GoModParser class that parses package dependencies from go.mod files. It extracts package names using regex patterns and returns a list of names.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/factory.py)         | This code snippet provides an abstract factory for parsers used to extract information from different types of dependency files. It returns a dictionary of file types and their corresponding parser objects. These parsers are crucial for extracting relevant data from various dependency files in the codebase.                                                                                                                                                                                                                                                                                              |
| [docker.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/docker.py)           | The code snippet is a Docker file parser that extracts a list of services from a docker-compose.yaml file. It handles YAML decoding errors and returns an empty list if no services are found.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [npm.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/npm.py)                 | This code snippet is part of the readme-ai repository and focuses on parsing JSON dependency files. It uses the `json` module to extract package names from specific sections in the file. It returns a list of dependencies.                                                                                                                                                                                                                                                                                                                                                                                     |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/gradle.py)           | The code snippet provides parsers for extracting package names from Gradle dependency files. It includes parsers for both `build.gradle` and `build.gradle.kts` files. The parsers use regular expressions to extract package names from the files. The extracted package names are then returned as a list.                                                                                                                                                                                                                                                                                                      |
| [base_parser.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/base_parser.py) | This code snippet is a base class for dependency file parsers in the `readme-ai` repository. It defines an abstract method `parse` that extracts package names from dependency files. It also provides a method `log_error` to log error messages when parsing fails.                                                                                                                                                                                                                                                                                                                                             |
| [python.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/python.py)           | This code snippet is part of the `readmeai` codebase and is responsible for parsing different types of dependency files in Python projects. It includes parsers for requirements.txt, TOML, and YAML files, extracting package names from each file type. These parsers handle different build systems and extract the necessary dependencies for the project.                                                                                                                                                                                                                                                    |
| [maven.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/maven.py)             | This code snippet is part of the readme-ai repository and is located in the `readmeai/parsers/maven.py` file. It contains the MavenParser class, which is responsible for parsing Maven dependency files in the pom.xml format. The `parse` method extracts package names from the content of the pom.xml file using regular expressions. If the extracted dependencies include any with spring in their name, the spring dependency is added to the list. The method returns a set of unique dependencies. If any exception occurs during the parsing process, an error is logged and an empty list is returned. |
| [rust.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/rust.py)               | This code snippet is a parser for Rust dependency files in the readmeai repository. It extracts package names from Rust TOML files. It utilizes the `toml` library for parsing TOML content.                                                                                                                                                                                                                                                                                                                                                                                                                      |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/preprocess.py) | This code snippet is part of the `readme-ai` repository and handles the preprocessing of the input codebase. It analyzes a local or remote git repository, generates file information, extracts dependency file contents, and tokenizes the content of each file. It also maps file extensions to programming languages and extracts the dependencies of the repository. The code achieves these tasks through the `RepoProcessor` class and various helper functions.                                                                                                                                                                                                                                                                                                                       |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/tokens.py)         | This code snippet provides tokenization utilities for the `readme-ai` CLI application. It includes functions for adjusting the maximum number of tokens based on a prompt, counting the number of tokens in a text string, selecting the token encoder to use for the model, and truncating a text string to a maximum number of tokens. These utilities are essential for processing text inputs and ensuring compatibility with the model.                                                                                                                                                                                                                                                                                                                                                 |
| [logger.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/logger.py)         | The code snippet provides a custom implementation of a logger using the colorlog library. It configures the logger and provides methods to log messages at different levels such as info, debug, warning, error, and critical. This logger is used in the readmeai/core/logger.py file within the parent repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/factory.py)       | The code snippet provides a FileHandler class in the readmeai/core/factory.py file. It serves as a file input/output (I/O) factory, allowing reading and writing of various file formats such as JSON, Markdown, TOML, TXT, and YAML. The class encapsulates methods for reading and writing files in these formats, providing a convenient and unified interface for handling file I/O operations within the codebase.The code supports reading and writing files of different formats, abstracting away the details of the specific file format being used. This promotes code modularity and reusability, as other components in the codebase can rely on the FileHandler class to handle their file I/O needs without needing to directly deal with the intricacies of each file format. |
| [model.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/model.py)           | The code snippet is part of the readme-ai repository and is responsible for generating text for the README.md file using GPT language models. It includes functions for handling prompts, batching, and generating summaries for code files. The code also implements rate limiting and caching for optimal performance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                           |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                               |
| [settings.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings.py) | This code snippet defines various Pydantic models and enums used for configuring the readme-ai CLI tool. It handles settings related to Git service, badges, images, CLI options, markdown templates, and more. The code also includes a helper class for loading additional configuration files. |

</details>

<details closed><summary>readmeai.markdown</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [tree.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tree.py)             | The code snippet is a TreeGenerator class that generates a formatted directory tree structure for a code repository. It takes the root directory, repository URL, repository name, and maximum depth as inputs, and returns the formatted tree structure as a string. It uses the ConfigHelper class, Logger class, and utils module for configuration and utility functions.                                                                                                                                                   |
| [badges.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/badges.py)         | The code snippet in the `readmeai/markdown/badges.py` file generates badges for a README file using various icons from repositories. It formats the badges into HTML `<img>` tags and retrieves the icons from an external source. The badges can be customized based on the project's dependencies and other metadata.                                                                                                                                                                                                         |
| [tables.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tables.py)         | This code snippet is responsible for generating Markdown tables to store text responses in the README file of the parent repository. It takes a list of data and constructs a table with headers and rows. Each row contains a hyperlink to a file, if available. The tables are organized by project sub-directory.                                                                                                                                                                                                            |
| [headers.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/headers.py)       | The code snippet is responsible for constructing each section of the README Markdown file in a repository. It formats the contents, including headers, badges, tables, project setup, and more. The code also removes emojis from headers and the Table of Contents if required.                                                                                                                                                                                                                                                |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/quickstart.py) | The code snippet is part of the readme-ai repository and is located in the `readmeai/markdown/quickstart.py` file. It dynamically generates the Quick Start section of the README file, counting the occurrences of each programming language and retrieving setup commands for the top language. The main function, `getting_started`, takes in an `AppConfig` object, a `ConfigHelper` object, and a list of summaries and returns a `ProjectSetup` object with information about using, running, and testing the repository. |

</details>

<details closed><summary>readmeai.utils</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                 |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/utils/utils.py) | This code snippet contains utility functions for the README-AI package. It includes functions for validating URLs, flattening nested lists, formatting text, getting relative file paths, accessing package resources, removing substrings from strings, and checking if files should be ignored. These functions are critical for various tasks related to generating and processing README files. |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                           |
| [options.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/options.py)   | This code snippet provides command-line interface options for the readme-ai application. It allows users to customize the generation of a README.md file by specifying various parameters such as alignment, badges, emojis, image, model, offline generation, output file name, repository, temperature, max tokens, template, and language. |
| [commands.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/commands.py) | The code snippet is the CLI entry point for the readme-ai repository. It provides command-line options to configure the readme-ai application and calls the main function to execute it. The CLI allows users to generate readme files using the specified options.                                                                           |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                   |
| [git_utilities.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/git_utilities.py)   | This code snippet provides Git service utilities to retrieve repository metadata. It includes functions to get the URL of a file in the remote repository, get the full name of the repository, and parse the repository URL to return the API URL.                                                                                                   |
| [git_operations.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/git_operations.py) | This code snippet is responsible for cloning and validating git repositories in a temporary directory. It uses the `git` library to clone the repository and performs error handling to ensure successful cloning. Additionally, it includes functions to find the path to the git executable and validate file permissions of the cloned repository. |
| [git_metadata.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/git_metadata.py)     | The code snippet provides helper methods to fetch and process metadata for a GitHub repository. It retrieves various details such as repository name, owner, description, statistics, URLs, programming languages, topics, and license information.                                                                                                   |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* Python: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

### ⚙️ Installation

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
Use the following command to run readme-ai:
```sh
python main.py
```

### 🧪 Tests
To execute tests, run:
```sh
pytest
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/readme-ai/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/eli64s/readme-ai/issues)**: Submit bugs found or log feature requests for readme-ai.

<details closed>
<summary>Contributing Guidelines</summary>

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

[**Return**](#-quick-links)

---
