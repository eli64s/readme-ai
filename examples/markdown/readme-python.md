<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">README-AI</h1>
</p>
<p align="center">
    <em>Revolutionize your readme with readme-ai!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&color=ff69b4" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=ff69b4" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=ff69b4" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=ff69b4" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
	<br>
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>   - [⚙️ Installation](#️-installation)
>   - [🤖 Running readme-ai](#-running-readme-ai)
>   - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The readme-ai project is a powerful tool that leverages AI to automatically generate high-quality and informative README files for software projects. By analyzing the codebase and extracting relevant information, readme-ai creates well-structured documentation that includes project descriptions, installation instructions, usage examples, and more. The project's value proposition lies in simplifying and streamlining the often tedious task of writing comprehensive READMEs, allowing developers to focus more on coding and less on documentation. With its intuitive CLI and seamless integration with common development workflows, readme-ai greatly improves project onboarding, collaboration, and overall code quality. By utilizing cutting-edge technologies like openai and gitpython, readme-ai ensures accuracy and relevance in generating READMEs that resonate with both developers and end-users.

---

## 📦 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The readme-ai project follows a modular architecture and is built using Python. It utilizes the asyncio library for asynchronous programming. The core component is the readmeai package, which provides a CLI for generating AI-generated READMEs. The project architecture allows for easy extensibility and customization. |
| 🔩 | **Code Quality**  | The project maintains good code quality and adheres to Python coding standards. It follows PEP 8 guidelines for code style and uses a linter to ensure consistency. The codebase is well-organized and readable, making it easy to understand and maintain. |
| 📄 | **Documentation** | The project has clear and extensive documentation. It includes a readme file that provides an overview of the project, installation instructions, and usage examples. The repository also contains code comments and docstrings to facilitate code understanding. Additionally, a comprehensive documentation website is available, covering various aspects of the project in detail. |
| 🔌 | **Integrations**  | The project has several key integrations and external dependencies. These include libraries such as aiohttp, jinja2, huggingface-hub, requests, pyyaml, and tokenizers. It also leverages external services like GitHub Actions for continuous integration and deployment. These integrations enhance functionality and improve development workflows. |
| 🧩 | **Modularity**    | The project demonstrates a high degree of modularity. It follows the single responsibility principle, with each module focusing on a specific aspect of functionality. The codebase is well-organized into directories, making it easy to reuse and extend specific components. This modularity promotes code readability, maintainability, and reusability. |
| 🧪 | **Testing**       | The project uses a combination of testing frameworks and tools. It includes pytest, pytest-asyncio, and pytest-sugar for unit testing and test automation. The codebase has good test coverage, with test scripts covering various functionalities. Testing ensures the reliability and correctness of the project. |
| ⚡️  | **Performance**   | The project is optimized for efficiency, speed, and resource usage. It leverages asynchronous programming using asyncio to handle multiple requests concurrently, resulting in improved performance. Additionally, it utilizes caching and compression techniques to optimize network communication. Overall, the project exhibits good performance characteristics. |
| 🛡️ | **Security**      | The project incorporates measures to ensure data protection and access control. It uses secure communication protocols such as HTTPS and includes security libraries like certifi. The repository actively maintains and updates dependencies to address security vulnerabilities promptly. Secure coding practices are followed to prevent common security issues. |
| 📦 | **Dependencies**  | The project relies on various external libraries and dependencies. Some key libraries include aiohttp, jinja2, huggingface-hub, requests, pyyaml, and tokenizers. These dependencies provide essential functionality, such as HTTP requests, template rendering, and natural language processing. |


---

## 📂 Repository Structure

```sh
└── readme-ai/
    ├── .github
    │   ├── release-drafter.yml
    │   └── workflows
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── docs
    │   ├── cli.md
    │   ├── concepts.md
    │   ├── configuration.md
    │   ├── contributing.md
    │   ├── css
    │   ├── examples.md
    │   ├── features.md
    │   ├── how-it-works.md
    │   ├── index.md
    │   ├── installation.md
    │   ├── js
    │   ├── overrides
    │   ├── prerequisites.md
    │   └── usage.md
    ├── examples
    │   ├── images
    │   └── markdown
    ├── mkdocs.yml
    ├── noxfile.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai
    │   ├── __init__.py
    │   ├── app.py
    │   ├── cli
    │   ├── config
    │   ├── core
    │   ├── exceptions.py
    │   ├── llms
    │   ├── markdown
    │   ├── parsers
    │   ├── services
    │   └── settings
    ├── scripts
    │   ├── clean.sh
    │   ├── docker.sh
    │   ├── pypi.sh
    │   ├── run_batch.sh
    │   └── test.sh
    ├── setup
    │   ├── environment.yaml
    │   ├── requirements.txt
    │   └── setup.sh
    └── tests
        ├── __init__.py
        ├── conftest.py
        ├── test_app.py
        ├── test_cli
        ├── test_config
        ├── test_core
        ├── test_exceptions.py
        ├── test_llms
        ├── test_markdown
        ├── test_parsers
        └── test_services
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/master/Dockerfile)         | The Dockerfile in the parent repository is responsible for building a Docker image that sets up the necessary environment and installs the readmeai package from PyPI. It then configures the image to run the CLI provided by the readmeai package as the default command.                                                                                                                                                                                      |
| [Makefile](https://github.com/eli64s/readme-ai/blob/master/Makefile)             | This code snippet is part of a Makefile in the parent repository. It defines commands for cleaning up, formatting, linting, testing, and generating requirements. It also includes a word search function for the repository. It ensures code quality and facilitates the development and maintenance processes.                                                                                                                                                 |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/master/pyproject.toml) | The pyproject.toml file in the repository defines the configuration and dependencies for the readme-ai project. It specifies the project name, version, description, authors, license, and other metadata. It also lists the required libraries and their versions, including click, colorlog, gitpython, openai, and others. Additionally, it contains optional dependencies for Google Cloud AI Platform and defines settings for code formatting and linting. |
| [poetry.lock](https://github.com/eli64s/readme-ai/blob/master/poetry.lock)       | The code snippet plays a critical role in the parent repository's architecture by achieving certain features. It is implemented in a well-structured repository that includes various supplementary materials such as a changelog, code of conduct, and license.                                                                                                                                                                                                 |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/master/noxfile.py)         | This code snippet in `noxfile.py` automates testing using Nox and pytest. It installs the package, runs test suites, and generates test coverage reports across multiple Python versions.                                                                                                                                                                                                                                                                        |

</details>

<details closed><summary>setup</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                 |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh)                 | The `setup.sh` script in the `setup` directory of the repository is responsible for setting up the README-AI environment. It checks for the existence of necessary tools, installs missing dependencies, creates a conda environment, activates it, and installs required packages. This script ensures a smooth and hassle-free setup process for using the README-AI application. |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt) | The code snippet located in the `setup/requirements.txt` file defines the required dependencies for the project. It specifies the versions of various Python packages that are necessary for the project to function correctly.                                                                                                                                                     |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml) | This code snippet, located in the setup/environment.yaml file, defines the required environment for the readme-ai repository. It specifies the Python version and dependencies needed for the project, such as the required packages listed in the requirements.txt file.                                                                                                           |

</details>

<details closed><summary>scripts</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                            |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh) | The code snippet `run_batch.sh` is responsible for running a batch process to generate readme files for multiple repositories. It takes a list of repository URLs, generates readme files with customized badges and styling, and saves them with version and date stamps.                                                                                                                     |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh)           | The `pypi.sh` script in the `scripts` directory is responsible for deploying a new version of the `readmeai` package to PyPI. It cleans previous build files, builds the package, and then uploads it to the PyPI repository using Twine. This script is critical for releasing new versions of the `readmeai` package to end users.                                                           |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh)         | The `clean.sh` script in the `scripts` folder of the repository is responsible for removing various artifacts and files generated during the build, testing, and development processes. It provides commands to clean the build artifacts, Python file artifacts, test and coverage artifacts, backup files, and cache directories. This script helps maintain a clean and organized codebase. |
| [test.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/test.sh)           | The code snippet in scripts/test.sh activates the readmeai conda environment and runs pytest with coverage analysis. It generates a coverage report and fails if coverage falls below 90%.                                                                                                                                                                                                     |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh)       | The docker.sh script in the scripts directory of the repository builds and publishes a Docker image for the readme-ai application. It uses Docker Buildx to create a multi-platform image and pushes it to the Docker registry.                                                                                                                                                                |

</details>

<details closed><summary>.github</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                            |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml) | The code snippet in the file path `.github/release-drafter.yml` is responsible for configuring the release notes generator within the parent repository. It defines templates and labels for different types of changes (features, bug fixes, etc.) and specifies the format of the release notes. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                         |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                             |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml)                 | This code snippet is a GitHub Action workflow file called coverage.yml located in the.github/workflows directory of the parent repository. It is responsible for generating code coverage reports and uploading them to a specified location.                                   |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml) | The code snippet in the file release-pipeline.yml implements a GitHub Actions workflow for automating the release process in the repository. It ensures that each release is properly documented and drafted, improving the efficiency and reliability of the release pipeline. |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml)   | This code snippet is part of the repository's workflow configuration. It sets up a release drafter for automated release notes generation and management.                                                                                                                       |

</details>

<details closed><summary>readmeai</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                   |
| [app.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/app.py)               | The code snippet in `readmeai/app.py` is the main module for the README-AI CLI application. It handles the generation of the README file by orchestrating the process and utilizing various components such as the configuration settings, Git repository, preprocessing functions, model handler, and markdown builder. It also includes error handling and logging functionalities. |
| [exceptions.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/exceptions.py) | The `exceptions.py` file in the `readmeai` directory of the codebase defines custom exceptions for the `readme-ai` application. It includes exceptions for git cloning, git validation, readme generation, file system errors, file reading, and file writing. These exceptions handle specific error scenarios that may occur during the execution of the application.               |

</details>

<details closed><summary>readmeai.settings</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/ignore_files.toml)         | The code snippet in the `readmeai/settings/ignore_files.toml` file is responsible for defining the files and directories to be ignored in the repository. It lists various file extensions, directories, and specific filenames to exclude when performing operations within the codebase.                                                                                                                                                                                                                                  |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_names.toml)     | This code snippet in the `readmeai/settings/language_names.toml` file contains a mapping of programming language file extensions to their corresponding names. It is used to provide consistent and readable language names in the parent repository's codebase.                                                                                                                                                                                                                                                            |
| [config.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/config.toml)                     | This code snippet in the `readmeai/settings/config.toml` file defines the configuration settings for the `readme-ai` project. It specifies file resources, Git repository settings, language model API settings, and markdown template settings. The code enables the project to work with dependencies, generate badges and tables, and provide integration with other components.                                                                                                                                         |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/dependency_files.toml) | The code snippet located at `readmeai/settings/dependency_files.toml` contains a list of file names grouped by programming language. These file names represent various dependency files used in the parent repository, such as package.json for JavaScript/Node.js projects, requirements.txt for Python projects, and Gemfile for Ruby projects. The purpose of this code is to provide a centralized reference for the different dependency file names in the repository in order to ensure consistency and ease of use. |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_setup.toml)     | The code snippet in `readmeai/settings/language_setup.toml` is responsible for defining the setup and run instructions for various programming languages in the `readme-ai` repository. It specifies the installation commands, run commands, and test commands for each language used in the repository.                                                                                                                                                                                                                   |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [registry.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/registry.py) | This code snippet provides an abstract factory for creating parsers for different types of dependency files. It returns a dictionary of callable methods that correspond to file parsers for various programming languages and technologies. This allows the parent repository to easily identify and parse different types of dependency files in a unified way.                                                                                                                                                                                                                                                                                        |
| [docker.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/docker.py)     | Code Summary:This code snippet includes two parsers, DockerfileParser and DockerComposeParser, used to extract package names and services respectively from Docker-related files. They leverage regular expressions and YAML parsing to achieve this.Parent Repository's Architecture:The parent repository has a clear structure with various files and directories such as documentation, examples, tests, and scripts. It follows best practices including a Makefile and Dockerfile for building and running the project. The codebase is organized using packages and modules, with the parsers mentioned above being part of the readmeai package. |
| [npm.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/npm.py)           | The `npm.py` code snippet is part of the `readmeai` repository and includes two file parsers, `PackageJsonParser` and `YarnLockParser`, which parse JSON dependency files (`package.json` and `yarn.lock`, respectively) and extract the names of the dependencies. These parsers are crucial for analyzing and understanding the project's dependency management and package information.                                                                                                                                                                                                                                                               |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cpp.py)           | The code snippet in `readmeai/parsers/cpp.py` is responsible for parsing C/C++ project dependency files. It includes parsers for CMakeLists.txt, configure.ac, and Makefile.am files. These parsers extract dependencies and libraries from the respective files using regular expressions. The extracted dependencies are returned as a list.                                                                                                                                                                                                                                                                                                           |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/gradle.py)     | This code snippet includes parsers for extracting package names from Gradle (build.gradle) and Kotlin Gradle (build.gradle.kts) dependency files. The parsers use regular expressions to identify and extract the relevant information. The package names are then returned as a list. These parsers play a critical role in the parent repository's architecture by enabling the extraction of dependency information from Gradle files.                                                                                                                                                                                                                |
| [swift.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/swift.py)       | This code snippet is a `SwiftPackageParser` class that extracts package names from a `Package.swift` file in a Swift project. It searches for package definitions and extracts the names using regular expressions. The parsed package names are returned as a list of strings. This parser plays a crucial role in the codebase by enabling the extraction and processing of package dependencies in Swift projects.                                                                                                                                                                                                                                    |
| [python.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/python.py)     | This code snippet includes parsers for various Python dependency file formats such as requirements.txt, TOML, and YAML. These parsers extract package names from the respective files while handling different syntax variations.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [go.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/go.py)             | This code snippet represents a GoModParser class that is responsible for parsing the content of go.mod files and extracting package dependencies. It uses regular expressions to match lines containing package information and extracts the package names. If any parsing errors occur, it handles them appropriately. This parser plays a critical role in the parent repository's architecture by enabling the extraction of package dependencies from go.mod files.                                                                                                                                                                                  |
| [maven.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/maven.py)       | This code snippet is a parser for Maven dependency files in the pom.xml format. It extracts package names from the file and returns a set of dependencies. If any dependency contains spring, it is also added to the set.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [rust.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/rust.py)         | This code snippet contains a parser for Rust dependency files, specifically for `cargo.toml` files. It extracts the names of packages from the TOML file, including those listed under dependencies, dev-dependencies, and additional dependencies specified in the file. If a parsing error occurs, it handles it accordingly.                                                                                                                                                                                                                                                                                                                          |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                               |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py)   | The code snippet in `readmeai/core/preprocess.py` is crucial for the parent repository's architecture. It processes the input repository files, extracts metadata, generates a context of file information, and determines dependencies. This information is used to build the README file for the repository.                                                                                                    |
| [logger.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/logger.py)           | This code snippet implements a custom logger for the readme-ai CLI. It configures the logger with a colored log formatter and different log levels. It provides methods to log messages at different levels such as info, debug, warning, error, and critical. The logger can be instantiated with a specific name and log level.                                                                                 |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/factory.py)         | The `FileHandler` class in the `readmeai/core/factory.py` file is responsible for reading and writing different file formats such as JSON, Markdown, TOML, TXT, and YAML. It provides methods to read and write files with different extensions, abstracting the underlying file I/O operations. This code snippet plays a critical role in managing file operations within the parent repository's architecture. |
| [model.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/model.py)             | The code snippet in `readmeai/core/model.py` is a handler for the LLM API that generates text for the README.md file. It configures the HTTP client, processes prompts in batches, and handles the API's response, including caching. It also handles code summaries for the README.md file.                                                                                                                      |
| [base_parser.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/base_parser.py) | This code snippet is a base parser for dependency file parsers. It provides an abstract class with methods to parse the content of a dependency file and handle parsing errors. It also logs error messages when parsing fails. This code plays a critical role in the parent repository's architecture as it defines the foundation for creating specific parsers for different types of dependency files.       |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py)             | This code snippet provides utility methods for processing files and text. It includes functions for formatting markdown tables and text, post-processing responses, getting resource paths, checking if files should be ignored, and validating URLs. These utilities are used in the parent repository's architecture to enhance text processing and manipulation.                                               |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                |
| [enums.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/enums.py)           | The code snippet in `readmeai/config/enums.py` provides Enum classes for the `readme-ai` CLI. It defines various options related to Git service details, badge icons, and header images used in the README file. These Enum classes help in providing standardized values and templates for different configurations.                                                                                              |
| [validators.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/validators.py) | This code snippet provides methods to validate command-line arguments and settings. It includes validators for the LLM API settings and Git repository settings, such as validating repository URLs or paths, getting the full name of the repository, and setting the Git service host and name. These validators play a critical role in ensuring the integrity and accuracy of the inputs provided by the user. |
| [settings.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py)     | This code snippet contains data models and functions for configuring the readme-ai CLI tool. It defines various settings related to files, Git repositories, API models, markdown templates, and prompt templates. These settings are used to generate the README.md file.                                                                                                                                         |

</details>

<details closed><summary>readmeai.markdown</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [tree.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tree.py)             | Code Summary:The tree code snippet generates a directory tree structure for a code repository. It takes the repository name, root directory, repository URL, and maximum depth as input. It builds a hierarchical tree structure by recursively traversing the directories and files in the repository, and then formats and returns the tree structure in a readable string format.Parent Repository Architecture:This code snippet is part of the readme-ai repository. This repository has a structure that includes documentation, examples, scripts, tests, and a Python package named readmeai. The tree code is located in the readmeai/markdown directory. It serves as a utility for generating a visual representation of the repository's directory structure in a hierarchical tree format. |
| [builder.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/builder.py)       | This code snippet is responsible for building various sections of the README Markdown file in the `readmeai/markdown/builder.py` file. It generates the header, code summaries, directory tree structure, and getting started sections. It also removes emojis from certain sections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [badges.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/badges.py)         | The `badges.py` code snippet in the `readmeai/markdown` directory is responsible for building and formatting badges in the README.md file. It provides functions to generate HTML badges for project dependencies and metadata using shields.io and skill icons.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [tables.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tables.py)         | This code snippet in the `readmeai/markdown/tables.py` file is responsible for constructing markdown tables to store LLM text responses in the README file. It provides functions to build the table, create hyperlinks for files, extract folder names, format the table, generate tables for each sub-directory, and group summaries by folder. These functions contribute to organizing and presenting the LLM text responses in a readable format in the README file.                                                                                                                                                                                                                                                                                                                               |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/quickstart.py) | The code in `readmeai/markdown/quickstart.py` dynamically creates the Quickstart section of the README file. It counts the occurrences of each language in the summaries, determines the top language, and retrieves its setup commands. It generates the Quick Start section of the README file based on this information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [options.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py)   | The `options.py` code snippet provides command-line interface options for the `readme-ai` application. It includes options for aligning text, specifying an API key, selecting badge styles, adding emojis, choosing an image, setting language and model options, generating an offline README file, specifying an output file name, providing a repository URL, configuring model temperature, using a custom template, and configuring Google Vertex AI. |
| [commands.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/commands.py) | This code snippet contains the CLI entrypoint for the readme-ai application within the parent repository. It defines the main function that parses command line options and invokes the readme_agent function with the provided arguments. The main function serves as the entry point for the readme-ai CLI application.                                                                                                                                   |

</details>

<details closed><summary>readmeai.llms</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                |
| [cache.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/cache.py)       | This code snippet is a custom cache manager that handles the caching of LLM (Language Learning Models) responses. It allows retrieval of responses from the cache if they are available and not expired, and also provides the ability to add new responses to the cache while respecting a maximum size limit. The cache can be cleared entirely if needed.                       |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/prompts.py)   | This code snippet, located in the readmeai/llms/prompts.py file, is part of the readme-ai repository. It manages prompts for API calls in the LLM (Linguistic Learning Model). It generates and injects prompts based on the provided context, and sets prompt contexts for generating prompts to be used by the LLM API.                                                          |
| [tokenize.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/tokenize.py) | This code snippet in the readme-ai repository's architecture is responsible for tokenization utilities in the CLI application. It includes functions for counting tokens, truncating text based on a maximum token limit, and updating the maximum token count based on a specific prompt. These utilities assist in processing and manipulating text data within the application. |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                     |
| [git_metadata.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_metadata.py) | This code snippet provides helper methods to fetch and parse metadata from a Git host provider for a repository. The main feature is retrieving repository metadata including statistics, details, URLs, programming languages, topics, and license information. This code is part of the `readme-ai` repository and supports its architecture by facilitating the gathering of repository information. |
| [git_utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_utils.py)       | This code snippet provides essential Git operations for cloning and validating repositories in the `readme-ai` repository. It includes functions for cloning a repository, removing hidden files, fetching the API URL of a Git service, finding the path to the Git executable, validating file permissions, and validating the Git executable path.                                                   |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

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
- **[Report Issues](https://github.com/eli64s/readme-ai/issues)**: Submit bugs found or log feature requests for Readme-ai.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/eli64s/readme-ai
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
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
