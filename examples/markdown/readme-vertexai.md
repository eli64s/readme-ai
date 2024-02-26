<p align="left">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" alt="project-logo">
</p>
<p align="left">
    <h1 align="left">README-AI</h1>
</p>
<p align="left">
    <em>Automate Your README: Unlock Insights, Enhance Documentation</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&logo=opensourceinitiative&logoColor=white&color=skyblue" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&logo=git&logoColor=white&color=skyblue" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=skyblue" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=skyblue" alt="repo-language-count">
<p>
<p align="left">
		<em>Developed with the software and tools below.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat-square&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
	<br>
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary><h4>Table of Contents</h4></summary>

- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Install](#️-install)
  - [► Using readme-ai](#-using-readme-ai)
  - [🧪 Tests](#-tests)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

Readme-AI is a meticulously crafted Python package that leverages AI's prowess to enhance the readability and cohesiveness of technical documentation. Its core functionality revolves around automating the generation of appealing and structured README files from unstructured Markdown documents. By seamlessly integrating with popular AI language models (GPT-3, BLOOM, etc.), the project allows users to transform complex technical concepts into clear and engaging prose, ensuring a seamless onboarding experience for developers and users alike. Readme-AI stands out as an invaluable tool for open-source projects, documentation teams, and technical writers seeking to elevate the quality and accessibility of their documentation.

---

## 📦 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | Monolithic Python codebase built on top of the Hugging Face Tokenizer library for natural language processing.|
| 🔩 | **Code Quality**  | Linted using flake8, following PEP-8 styling conventions. Unit tests cover core functionality for different input formats and scenarios. |
| 📄 | **Documentation** | Minimal README file, lacks detailed user guide and API documentation. |
| 🔌 | **Integrations**  | Hugging Face Tokenizer library for NLP tasks and OpenAI API for code generation. |
| 🧩 | **Modularity**    | Not modularized; tightly coupled codebase with limited code reusability. |
| 🧪 | **Testing**       | Unit tests using pytest, ensuring functionality for various input formats and scenarios. |
| ⚡️  | **Performance**   | Potentially slow for large codebases due to the extensive NLP analysis required for readme summarization. |
| 🛡️ | **Security**      | No apparent security measures implemented within the codebase. |
| 📦 | **Dependencies**  | Hugging Face Tokenizer library, OpenAI API library, and other Python standard libraries. |

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
    │   ├── css
    │   ├── docs
    │   ├── js
    │   └── overrides
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
    │   └── run_batch.sh
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

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                              |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/master/Dockerfile)         | Dockerfile constructs a custom image for the repository, facilitating its deployment in multi-platform environments. It establishes a non-root user and sets necessary permissions, installs system dependencies, and finally installs the readmeai package from PyPI.                                                                                                           |
| [Makefile](https://github.com/eli64s/readme-ai/blob/master/Makefile)             | Enhancing developer efficiency, this Makefile automates routine tasks within the project: code cleanup, formatting, and linting. It supports conda package creation and provides options for git operations such as removing cached files and displaying logs. Additionally, it facilitates testing with nox and pytest, and enables directory-wide searches for specific terms. |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/master/pyproject.toml) | Generates a project's README file with automated content using poetry, including dependency management and documentation configuration.                                                                                                                                                                                                                                          |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/master/noxfile.py)         | Automates testing with nox and pytest, ensuring consistent test execution across multiple Python versions.                                                                                                                                                                                                                                                                       |

</details>

<details closed><summary>setup</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh)                 | The setup script for README-AI automates environment setup by checking for and installing necessary tools like Git, conda, and Python. It creates and activates a conda environment with the required Python version and dependencies. The script also adds the environment's Python path to PATH and installs packages using pip. |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt) | The requirements.txt file specifies the Python packages and their versions needed for the project to run. It ensures compatibility and proper functioning of various modules and components within the codebase.                                                                                                                   |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml) | This environment.yaml file defines a Python conda environment named `readmeai` for the ReadmeAI codebase. It specifies Python version, installs `pip`, and utilizes the `requirements.txt` file to install necessary Python packages. This allows for consistent and isolated development and deployment environments.             |

</details>

<details closed><summary>scripts</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                                                       |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                           |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh) | Automates the creation of README files using pre-defined templates, allowing users to quickly and consistently generate comprehensive documentation for their repositories. Key features include badge customization, image selection, alignment options, and error handling. |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh)           | Facilitates deployment of the `readmeai` package to the PyPI repository, allowing for convenient installation and distribution through pip.                                                                                                                                   |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh)         | Facilitates codebase maintenance by orchestrating cleanup tasks across the project.Features include:-Build artifact removal-Pyc file cleanup-Test and coverage remnant deletion-Cache and backup file removal                                                                 |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh)       | The `docker.sh` script automates the process of building and publishing a Docker image for the `readmeai` project. It supports building both standard and multi-platform images, ensuring the project's availability on various platforms.                                    |

</details>

<details closed><summary>.github</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                |
| ---                                                                                                | ---                                                                                                                                                                                                                    |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml) | This release drafter configures the repository to follow the keep-a-changelog convention. It classifies changes into categories like Features, Bug Fixes, and Documentation, generating release notes based on labels. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                   |
| ---                                                                                                            | ---                                                                                                                                                                                                       |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml)                 | Monitors code coverage for the repository and uploads it to Codecov upon each new push. Integrates with GitHub Actions for automated execution.                                                           |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml) | Automates release management by leveraging GitHub actions triggering on pushes to the `main` branch. It builds and tests the code, generates and uploads release artifacts, and creates a GitHub release. |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml)   | Automates creation of GitHub releases and changelogs for the project, ensuring consistent and up-to-date documentation.                                                                                   |

</details>

<details closed><summary>readmeai</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                |
| [app.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/app.py)               | The `app.py` script serves as the entry point for the readme-ai CLI tool. It orchestrates the README generation process by loading configuration, cloning the target repository, and preprocessing its contents. It interacts with the LLM API to generate text, incorporates it into a Markdown template, and ultimately saves the generated README to the specified output file. |
| [exceptions.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/exceptions.py) | The `exceptions.py` file in `readme-ai` defines custom exceptions for various scenarios. These exceptions handle errors during repository cloning, validation, and file system operations. It also manages exceptions during readme generation and unsupported LLM API service usage.                                                                                              |

</details>

<details closed><summary>readmeai.settings</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/ignore_files.toml)         | In the settings module of the `readmeai` package, `ignore_files.toml` defines a list of directories and file extensions to ignore during parsing and processing. This helps exclude unnecessary or irrelevant files from analysis, ensuring streamlined and focused operations within the application's architecture.                                                                                                                                                                       |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_names.toml)     | Language names are mapped to their file extensions in this settings file, allowing the codebase to identify and interpret code snippets associated with specific programming languages.                                                                                                                                                                                                                                                                                                     |
| [config.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/config.toml)                     | This code snippet, located in the `settings/config.toml` file of the `readme-ai` repository, serves as a configuration file for the project. It defines various settings related to file handling, Git repository, language model API, Markdown template, project badges, skills, and table of contents. These settings guide the behavior and presentation of the project, ensuring consistent formatting, proper dependency management, and seamless integration with external resources. |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/dependency_files.toml) | This code defines dependency file names for various languages within the project. The specified file names are grouped by language and utilized to identify project dependencies.                                                                                                                                                                                                                                                                                                           |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_setup.toml)     | This code configures the programming language setup for the project. It defines default installation, run, and test commands for various languages, including Python, JavaScript, C++, and others. This centralizes the language-specific configuration, facilitating consistent language handling and testing.                                                                                                                                                                             |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [registry.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/registry.py) | The `parser_factory` function in `readmeai/parsers/registry.py` abstracts dependency file parsing by producing a mapping of dependency file types to their associated parsers. This facilitates seamless handling of various dependency formats, including those used by Python, C/C++, JavaScript/Node.js, Kotlin/Kotlin DSL, Go, Java, Rust, Swift, Dockerfile, and docker-compose.                                                                                                                                                                                                  |
| [docker.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/docker.py)     | The Dockerfile parser extracts package names and versions from Dockerfile dependency files. It handles parsing errors and returns a list of dependencies. Additionally, there's a DockerCompose parser that extracts a list of services from docker-compose.yaml files.                                                                                                                                                                                                                                                                                                                |
| [npm.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/npm.py)           | Parses JSON dependency files, such as `package.json`, to extract a list of dependencies. Supports sections like "dependencies," "devDependencies," and "peerDependencies." Handles parsing errors and logs them.                                                                                                                                                                                                                                                                                                                                                                       |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cpp.py)           | The code snippet contained within the `readmeai/parsers/cpp.py` file is a collection of parser classes that analyze C/C++ project dependency files. The `CMakeParser` class extracts dependencies, libraries, and software from `CMakeLists.txt` files, while the `ConfigureAcParser` class extracts package names from `configure.ac` files. The `MakefileAmParser` class, on the other hand, identifies dependencies from `Makefile.am` files. These parsers work together to collect project dependencies and enhance the codebase's overall understanding of project requirements. |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/gradle.py)     | Parses Gradle dependency files to extract package names and groups them into a flat list of unique package names. It handles errors during parsing and provides meaningful error messages.                                                                                                                                                                                                                                                                                                                                                                                             |
| [swift.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/swift.py)       | SwiftPackageParser extracts package names from Swifts Package.swift files. It supports URLs, names, and dependencies. The extracted names provide insights into a projects dependencies.                                                                                                                                                                                                                                                                                                                                                                                               |
| [python.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/python.py)     | Parses Python dependency files (requirements.txt, TOML, YAML) to extract package names, excluding version specifiers. Supports various package managers like Pip, Poetry, and Conda.                                                                                                                                                                                                                                                                                                                                                                                                   |
| [go.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/go.py)             | Parse dependencies from Go's `go.mod` files. Handles parsing errors gracefully.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [maven.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/maven.py)       | MavenParser, part of readmeais architecture, parses Mavens pom.xml files to extract package names. It uses regular expressions to identify dependencies and includes Spring if detected. The parser handles parsing errors and returns a set of dependencies.                                                                                                                                                                                                                                                                                                                          |
| [rust.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/rust.py)         | Rust dependency file parser for Readme AI.** Captures package names from Rust `cargo.toml` files, including dependencies, dev-dependencies, and nested dependencies. Handles parsing errors gracefully.                                                                                                                                                                                                                                                                                                                                                                                |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py) | This code, found in the "readmeai/core/preprocess.py" file of the repository, is responsible for processing the input repository files. It extracts metadata and generates a list of FileContext objects, each representing a file. The FileContext object contains information such as file path, extension, content, token count, language, and dependencies.The code also identifies dependency files, GitHub workflows, and maps file extensions to programming languages. It leverages the parser factory to extract dependencies from specific file types. Additionally, it tokenizes file content for LLM models and applies language mapping.The process_repository function orchestrates the preprocessing by generating repo_context, dependencies, dependency_dict, and the markdown tree. This data is used to build a comprehensive README.md file and provide insights into the repository's content, structure, and dependencies. |
| [logger.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/logger.py)         | In the readme-ai repository, the logger.py module provides a custom logging implementation for the CLI. It features colorized logs with level-specific emojis and a granular logging level configuration. The logger can log messages at various levels, including debug, info, warning, error, and critical. The module ensures that only one instance of the logger exists for each name, preventing multiple instances with the same name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [model.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/model.py)           | ModelHandler, a core component of the codebase, provides an abstract base class for LLM implementations. It initializes LLM API settings, manages HTTP clients, and facilitates batch processing of prompts. The class utilizes various helper functions for prompt context formatting, token adjustment, and response handling, enabling efficient and structured communication with LLM APIs to generate code summaries and enhance readme documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [parser.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/parser.py)         | Defines an abstract base class for dependency file parsers, providing a standardized error handling mechanism for parsing exceptions and a uniform interface for parsing file content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py)           | The `readmeai.core.utils` module provides utility methods for the ReadMe AI CLI application. It offers functions for formatting Markdown text, tables, and LLM responses. Additionally, it includes methods to retrieve resource paths and check if files should be ignored during LLM processing. The module is crucial in setting up LLM environment variables based on the specified service, ensuring seamless integration with OpenAI or Vertex AI. It also plays a role in enabling offline mode when necessary, allowing the generation of README files without an active internet connection.                                                                                                                                                                                                                                                                                                                                            |
| [file_io.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/file_io.py)       | File I/O factory class to read and write files. It supports JSON, MD, TOML, TXT, and YAML file formats. It handles file reading and writing operations efficiently through method caching.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                            |
| ---                                                                                            | ---                                                                                                                                                                                                                                |
| [enums.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/enums.py)           | Defines enums for Git service details, README badge and image options, LLM API keys, and LLM environment variables.                                                                                                                |
| [validators.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/validators.py) | This config validator ensures valid Git settings for the repository and user. It validates repository URLs and paths, extracts full names, sets Git service hosts, host domains, and repository names.                             |
| [settings.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py)     | This TOML file contains application-wide configuration settings for the readme-ai CLI tool, including file paths, git settings, markdown settings, and configuration helper functions. It also provides a customizable data model. |

</details>

<details closed><summary>readmeai.markdown</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [tree.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tree.py)             | Generates a comprehensive directory tree structure for a code repository, displaying its organization and hierarchy up to a defined maximum depth. Facilitates understanding of the repository's layout and organization.                                                                                                                                                                                                                                                                           |
| [builder.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/builder.py)       | This code snippet within readmeai/markdown/builder.py constructs the README Markdown file for the project. It optimally displays:-Project header with name, slogan, badges-Overview, features-Directory tree structure-Code summaries in modular widgets-Quickstart guide for project setup and usage-Contributing guidelines                                                                                                                                                                       |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/utils.py)           | The code in `markdown/utils.py` plays a crucial role in the `readme-ai` repository by providing utilities to enhance markdown content:-Removes emojis from markdown text to maintain consistency and improve readability.-Splits markdown documents into sections based on level 2 headings, facilitating modularization and content organization.-Updates the names of markdown files by removing emojis, underscores, and leading spaces, ensuring compatibility with the repository's structure. |
| [badges.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/badges.py)         | Central to the readmeai package, the `badges.py` module constructs and formats badges that adorn the project's README file. It includes functionality to:-Read badge icon SVGs from configuration files.-Create HTML badges for project dependencies and metadata using shields.io (optional).-Format and align badges for optimal display.-Generate skill badges using skill icons.                                                                                                                |
| [tables.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tables.py)         | This code generates Markdown tables for LLM text responses in a README file. It creates hyperlinks to repository files, extracts summaries, and groups them by folder. These tables highlight file modifications and provide convenient access to LLM-generated content within the project's documentation.                                                                                                                                                                                         |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/quickstart.py) | This code dynamically creates the Quickstart section of the README file. It identifies the top programming language used in the repository and generates usage, installation, and testing instructions. Additionally, it counts language occurrences and retrieves setup commands for the top language.                                                                                                                                                                                             |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                            |
| [options.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py)   | In the `readmeai` repository, the `options.py` file defines command-line options for the `readme-ai` application. It offers customizable settings like image selection, language, model, and output file name for generating README files. The options facilitate user input, supporting various media formats, language preferences, and fine-tuning the AI model's behavior. |
| [commands.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/commands.py) | This CLI entrypoint serves as the main interface for the readme-ai application. It orchestrates and executes the core functionality of the app, allowing users to generate and customize readmes through a command-line interface.                                                                                                                                             |

</details>

<details closed><summary>readmeai.llms</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [registry.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/registry.py) | The `model_handler` function in `llms/registry.py` serves as a factory method to instantiate the appropriate LLM (Large Language Model) implementation module. It dynamically returns an LLM handler based on the LLM API service specified in the configuration. The registry of available LLM services includes `offline`, `openai`, and `vertex`. If an unsupported service is requested, an exception is raised to alert the user.                                                           |
| [offline.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/offline.py)   | The `OfflineModeHandler` class enables offline mode when no LLM API service is specified. It provides default placeholders, prompts, and settings to ensure functionality in offline mode, handling file summaries and response generation seamlessly.                                                                                                                                                                                                                                           |
| [vertex.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/vertex.py)     | VertexAIHandler encapsulates Google Vertex AIs Generative Models API for LLM tasks. It initializes API settings, handles responses, and includes retry logic for resilience. The handler considers prompt length, truncation, and provides formatted responses. Its part of ReadmeAIs LLM module, integrating with the repositorys configuration and logging infrastructure.                                                                                                                     |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/tokens.py)     | This module contains tokenization functions for the readme-ai CLI app. It calculates the token count, truncates text to a given token limit, and adjusts the limit based on the prompt's validity. The encoding cache optimizes token encoding for different encodings.                                                                                                                                                                                                                          |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/prompts.py)   | In the readmeai repository, the prompts.py script handles prompt management for LLM API calls. It generates custom prompts for summarizing, featuring, and creating overviews and slogans. The script supports injecting context into prompts, extracting templates, and setting up prompt contexts for summaries, features, overviews, and slogans.                                                                                                                                             |
| [openai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/openai.py)     | Within the readmeai codebase, the `openai.py` file implements an OpenAI API LLM utilizing `tenacity` for resilience against potential network or server-related issues. Through an asynchronous request, it handles and processes OpenAI API responses, delivering generated text. The LLMs configuration, which encompasses settings like model selection, temperature, and token limits, is also managed within this file, contributing to the codebases overall flexibility and adaptability. |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                     |
| [git_metadata.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_metadata.py) | This code retrieves repository metadata from GitHub API and stores it in a dataclass. It includes repository statistics, details, programming languages, license information, and additional settings.                                                                                                                                                                                  |
| [git_utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_utils.py)       | The `git_utils.py` module provides Git operations for cloning and validating repositories within the `readmeai` project. It facilitates cloning repositories, validating file permissions, and fetching Git API and file URLs. This module plays a crucial role in interacting with remote repositories, handling Git-related tasks, and ensuring the integrity of cloned repositories. |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

### ⚙️ Install

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

### ► Using `readme-ai`

Use the following command to run readme-ai:

```sh
python main.py
```

### 🧪 Tests

Use the following command to run tests:

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

- **[Report Issues](https://github.com/eli64s/readme-ai/issues)**: Submit bugs found or log feature requests for the `readme-ai` project.
- **[Submit Pull Requests](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/readme-ai/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
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
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/eli64s/readme-ai/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eli64s/readme-ai">
   </a>
</p>
</details>

---

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
