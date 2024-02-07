<p align="left">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="left">
    <h1 align="left">README-AI</h1>
</p>
<p align="left">
    <em>AI-Powered ReadMe Generator: Transforming Code into Clarity</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&color=orange" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=orange" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=orange" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=orange" alt="repo-language-count">
<p>
<p align="left">
		<em>Developed with the software and tools below.</em>
</p>
<p align="left">
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
>   - [►Running readme-ai](#-running-readme-ai)
>   - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

ReadMe-AI is a tool for automating the generation of well-structured and informative README.md files using language models (LMs). It analyzes code and metadata from a provided Git repository, leveraging LMs to summarize code snippets, create section headers, and generate quickstart guides. The generated README.md files can include badges, tables, and images, providing a comprehensive overview of the project. ReadMe-AI streamlines the process of creating professional-looking READMEs, saving developers valuable time and effort.

---

## 📦 Features

|   | Feature            | Description |
|----|--------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**   | CLI-based, leveraging Hugging Face's Transformers library and OpenAI API for text generation and summarization. |
| 🔩 | **Code Quality**   | Well-structured codebase adhering to PEP8 standards, with a good level of unit test coverage. |
| 📄 | **Documentation**  | Comprehensive documentation and tutorial available on the repository's README, covering installation, usage, and contributing. |
| 🔌 | **Integrations**   | Seamlessly integrates with Hugging Face's Transformers library and offers optional OpenAI API integration. |
| 🧩 | **Modularity**     | Modular design allows for easy customization and extension of the code for specific use cases. |
| 🧪 | **Testing**       | Unit and integration tests using pytest, ensuring code stability and functionality. |
| ⚡️  | **Performance**   | Lightweight and efficient, designed for quick execution and generation of summaries. |
| 🛡️ | **Security**      | No sensitive data is stored or transmitted, ensuring user privacy and security. |
| 📦 | **Dependencies**   | Embraces popular Python libraries such as Hugging Face, OpenAI, pydantic, click, and pytest. |


---

## 📂 Repository Structure

```sh
└── readme-ai/
    ├── .github
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── docs
    ├── examples
    ├── mkdocs.yml
    ├── noxfile.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai
    ├── scripts
    ├── setup
    └── tests
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/master/Dockerfile)         | Dockerfile sets up a Python 3.10 environment for the `readmeai` package installation and execution. It uses a non-root user for security                                                                                                                                                                                                                                                         |
| [Makefile](https://github.com/eli64s/readme-ai/blob/master/Makefile)             | Makefile automates various tasks for the readme-ai repository.-Commands include code formatting, linting, testing, and building a conda package.-Facilitates repository cleanup, git operations, and documentation generation.-Promotes efficient development and maintenance of the project's codebase.-Serves as a central point for managing development tasks and enhancing project quality. |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/master/pyproject.toml) | pyproject.toml manages dependencies for the readmeai package, which auto-generates README files using AI language models.-It specifies dependencies, scripts, and other metadata for the project.                                                                                                                                                                                                |
| [poetry.lock](https://github.com/eli64s/readme-ai/blob/master/poetry.lock)       | Central entity in a codebase for generating summaries of code snippets and their significance within the overall architecture.                                                                                                                                                                                                                                                                   |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/master/noxfile.py)         | Automates testing across various Python versions using Nox.-Installs dependencies based on specified groups.-Executes tests with coverage reporting.-Supports isolating environments for testing.-Compatible with Python 3.9-3.12.-Promotes consistent testing practices in the project.-Enhances the stability and reliability of the codebase.                                                 |

</details>

<details closed><summary>setup</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                    |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh)                 | Sets up a conda environment named readmeai for running the README-AI project. It checks for and installs Git, conda, Python 3.8+, and required packages from requirements.txt. Guides users to activate the environment and adds Python path to the PATH environment variable.                                                                         |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt) | Specifies required dependencies for the repository's Python environment.-Ensures compatibility with Python versions 3.8.1 to 3.9.-Includes HTTP libraries, data processing tools, and utilities.-Supports integrations with services like OpenAI and Hugging Face Hub.-Contributes to the repository's functionality for text processing and AI tasks. |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml) | Defines a conda environment for the `readmeai` package.-Specifies Python version, installs `pip`, and lists required packages.-Simplifies package installation and ensures reproducible environment.                                                                                                                                                   |

</details>

<details closed><summary>scripts</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh) | Certainly! Here's a succinct summary of the provided code snippet in relation to the parent repository's architecture:This script, run_batch.sh, plays a crucial role in automating the generation of markdown documentation for various code repositories using the readme-ai package. It iterates through a list of repositories, dynamically generating markdown files with customized styling options, including badges, images, and layout preferences. The script aims to streamline the process of creating standardized and visually appealing documentation for a large number of repositories. |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh)           | Uploads the Python package from the project to PyPI.-Automates the process of cleaning, building, and uploading the package along with authentication.-Facilitates the distribution of the package to users via PyPI.                                                                                                                                                                                                                                                                                                                                                                                    |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh)         | clean.sh script assists in cleaning build, test, coverage, and Python artifacts from the codebase. It offers various commands to selectively remove different types of artifacts. It plays a crucial role in maintaining a clean and organized codebase by eliminating unnecessary files.                                                                                                                                                                                                                                                                                                                |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh)       | Code builds and pushes a multi-platform Docker image from the current directory.-Image is named readme-ai with version latest by default.-Utilizes Docker Buildx for multi-platform builds.-Success message includes the published image name.-Found in `scripts/docker.sh` of the `readme-ai` repository.                                                                                                                                                                                                                                                                                               |

</details>

<details closed><summary>.github</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml) | Sure, here is a succinct summary of the code snippet's role and features, emphasizing its significance to its parent repository's architecture:The `.github/release-drafter.yml` file plays a crucial role in automating the changelog generation and release process for the readme-ai repository. It enables the creation of well-structured changelogs by associating labels with different categories, ensuring clear and consistent documentation of changes. This contributes to a well-maintained and organized codebase, improving the overall clarity and transparency of the repository's development history. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                           | Summary                                                                                                                                                      |
| ---                                                                                                            | ---                                                                                                                                                          |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml)                 | Automates test coverage reporting for Python projects. Integrates with Codecov to display coverage results as a badge on the repository's README.            |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml) | Automates software release pipeline: versioning, building, testing, and deploying code. Integrates with CI/CD tools for continuous integration and delivery. |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml)   | Automates creation of GitHub releases based on commits and PRs. Integrates with Drafter gem.                                                                 |

</details>

<details closed><summary>readmeai</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [app.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/app.py)               | Sure, here is a summary of the code snippet in relation to its parent repository's architecture:-Main method of the readme-ai CLI app.-Orchestrates the generation of a README.md file using a large language model.-Clones a Git repository, processes its contents, and generates summaries using the model.-Builds the README.md file using generated summaries, repository metadata, and a template.-Saves the generated README.md file to a specified output path. |
| [exceptions.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/exceptions.py) | Handles exceptions for the readme-ai application, including Git cloning/validation errors, readme generation issues, and file system operations.                                                                                                                                                                                                                                                                                                                        |

</details>

<details closed><summary>readmeai.settings</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/ignore_files.toml)         | Defines a list of directories, extensions, and files to be ignored by the codebase.-Ensures uniformity in code structure, enhancing code maintainability and readability.-Aligns with best practices for version control and project management.-Promotes consistency in code practices across the project team, fostering collaboration.                                                                                                                                                                            |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_names.toml)     | Defines language file extensions and corresponding names.-Enables language recognition based on file extension.-Supports syntax highlighting, code completion, and other features.-Provides a common mapping for various programming languages.-Helps with language-specific operations within the parent repository.                                                                                                                                                                                                |
| [config.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/config.toml)                     | This code configures settings for a ReadMe.AI project. Features include OpenAI integration, Markdown templating, and project details. The config.toml file is essential for personalizing and running the project.                                                                                                                                                                                                                                                                                                   |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/dependency_files.toml) | This dependency file (`dependency_files.toml`) is used in the repository to specify the file names indicating dependencies used in the project. These files are used by different languages and technologies, including Python, JavaScript/Node.js, Java, Kotlin, TypeScript, Go, Rust, C/C++, C#, PHP, Ruby, Swift, Haskell, Clojure, Elixir, Dart/Flutter, R, Scala, Groovy, Lua, Julia, F#, Objective-C, Matlab, and Perl.                                                                                        |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_setup.toml)     | Sure, here is a succinct summary of the provided code snippet and its role within the repository:In the readmeai/settings/language_setup.toml file, language-specific installation, execution, and testing commands are defined for various programming languages. These instructions guide users in setting up and running code examples for each language within the repository. This file facilitates a consistent and user-friendly experience when working with different programming languages in the project. |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                        |
| [registry.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/registry.py) | This code creates a registry of dependency file parsers. It provides a dictionary of callable file parser methods, allowing the program to identify and handle different dependency file formats. Each entry in the dictionary specifies the file pattern and matches it to a specific parser from the `readmeai.parsers` module.          |
| [docker.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/docker.py)     | The code in `readmeai/parsers/docker.py` parses Dockerfiles for base images and versions and Docker Compose files for services. This helps identify dependencies used in containerized applications.                                                                                                                                       |
| [npm.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/npm.py)           | Parses JSON dependency files (`package.json`) and Yarn lockfiles (`yarn.lock`) to extract package names.-Integrates with the parent repository's dependency parsing architecture via the `readmeai.core.base_parser` module.-Handles parsing errors and logs them using the `readmeai.core.logger` module.                                 |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cpp.py)           | Sure, here is a concise summary of the code snippet in no more than 50 tokens:`readmeai/parsers/cpp.py` parses C/C++ dependency files (CMakeLists.txt, configure.ac, and Makefile.am) to extract dependencies, libraries, and software crucial for understanding a project's technology stack.                                             |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/gradle.py)     | Parsers for Gradle dependency files (`.gradle` and `.gradle.kts`).-Extracts package names from dependencies specified in the Gradle files.-Utilizes regular expressions to match dependency patterns.-Handles parsing errors and returns a list of package names.-[README AI Repository](https://github.com/joelparkerhenderson/README.ai) |
| [swift.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/swift.py)       | SwiftPackageParser in readmeai extracts package names from Swift Package.swift files, aiding dependency analysis for Swift projects.                                                                                                                                                                                                       |
| [python.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/python.py)     | Parses Python dependency files (requirements.txt, pyproject.toml, environment.yml).-Extracts package names, excluding version specifiers.-Supports Pipfile, Poetry, Flit, and Conda environment.yml formats.-Handles errors and provides informative error messages.                                                                       |
| [go.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/go.py)             | Sure, here is a summary of the code snippet in no more than 50 tokens:**Go Mod Parser for Dependency Management**-Parses `go.mod` files to extract dependency package names.-Supports versioned dependency formats.-Integrates with the base parser for error handling.                                                                    |
| [maven.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/maven.py)       | The `MavenParser` in `readmeai/parsers/maven.py` parses Maven dependency files (pom.xml) to extract package names. It uses regex to identify dependencies, including spring if present. The parsed dependencies are returned as a set to avoid duplicates.                                                                                 |
| [rust.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/rust.py)         | Rust dependency parser within the readme-ai package extracts package names from Rust's cargo.toml files, supporting both dependencies and dev-dependencies. It handles parsing errors gracefully.                                                                                                                                          |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                       |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py)   | The `preprocess.py` script processes repository files, extracting metadata and generating `FileContext` objects for each.-It determines dependencies using parsers and tokenizes content if the LLM is offline.-File extensions are mapped to programming languages.-It returns a list of `FileContext` objects, dependencies, raw files, and the Markdown tree for readme generation.                    |
| [logger.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/logger.py)           | Centralized logging module for the readme-ai CLI. Provides a consistent, color-coded logging interface and colored output with emojis for different log levels. Facilitates logging messages from various modules within the CLI application.                                                                                                                                                             |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/factory.py)         | File handler factory class (`FileHandler`) for reading and writing files in various formats.-Handles JSON, MD, TOML, TXT, and YAML file formats.-Provides `read` and `write` methods that can be used in a uniform manner across all supported file formats.-Uses a cache to improve performance for frequently accessed files.-Raises exceptions in case of errors during file read or write operations. |
| [model.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/model.py)             | ModelHandler class manages LLM API interactions for README.md generation.-Initializes essential attributes and configures HTTP client for requests.-Supports batch processing of prompts, ensuring efficient API utilization.-Handles errors during requests with retries and caching mechanisms.-Generates summaries for code files by analyzing file content and context.                               |
| [base_parser.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/base_parser.py) | Sure, here is a succinct summary of the provided code snippet in 49 tokens:The abstract base class `FileParser` defines the interface for dependency file parsers. It provides a standardized way to parse dependency files and handle parsing errors across different parsers.                                                                                                                           |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py)             | Sure, here's a summary of the code snippet in 50 tokens:This code defines functions for formatting Markdown tables, cleaning and formatting generated text, and post-processing API responses. It also provides a utility for retrieving resource paths and checking if a file should be ignored based on configuration settings.                                                                         |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                      |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                          |
| [enums.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/enums.py)           | Defines enums for Git services and README file badges/images.-GitService enum provides Git service details, API URLs, and file URL templates.-BadgeOptions enum offers various styles for README badge icons.-ImageOptions enum provides predefined images for README header.                |
| [validators.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/validators.py) | Provides essential Git repository-related validations for a command-line interface (CLI) tool.-Ensures valid repository URLs, paths, full repository names, Git host domains, and sets the Git service host.-Helps maintain the accuracy and integrity of Git-related tasks in the CLI tool. |
| [settings.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py)     | The `load_config` function in `settings.py` reads configuration constants from a TOML file. Configuration data is validated with Pydantic and cached efficiently. This configuration data drives the generation of Markdown files.                                                           |

</details>

<details closed><summary>readmeai.markdown</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                    |
| [tree.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tree.py)             | Generates directory tree structure for a code repository-Supports specified depth and root directory-Displays tree structure in markdown format-Includes optional repository name and URL-Adds summary for directories at depth 2                                                                                                                                                                      |
| [builder.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/builder.py)       | In the readmeai package, the builder.py module constructs the README Markdown file. It generates sections like the header, summaries, tree structure, quickstart, and contributing guidelines. Markdown is formatted for tables and other elements. Customizations are made based on configuration options like emojis and badge styles.                                                               |
| [badges.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/badges.py)         | Generates badges in a README.md file for displaying project metadata and dependencies.-Supports two badge styles: default and skills-light.-Uses shields.io for metadata badges and skill-icons or shields.io for dependency badges.-Creates HTML-formatted badge strings for insertion into the README.md file.-Customizable through configuration settings for badge style, color, and alignment.    |
| [tables.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tables.py)         | Sure, here is a 50-token summary of the provided code snippet within its parent repository's architecture, including supplementary details:-Creates Markdown tables to showcase LLM text responses within a project's README.-Key features:-Dynamic table generation from data.-Hyperlinks to code files.-Grouping and formatting code summaries.-Integrates seamlessly with the readme-ai repository. |
| [utilities.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/utilities.py)   | Python utility in readmeai/markdown removes emojis from Markdown content, especially heading lines and specific sections. It utilizes a pre-defined emoji pattern to match and remove those symbols within the text.                                                                                                                                                                                   |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/quickstart.py) | Gathers data for the Quickstart section of the README.-Calculates language usage statistics from code summaries.-Identifies the primary language and retrieves its setup commands.-Generates a ProjectSetup object with installation, running, and testing instructions.                                                                                                                               |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                        |
| [options.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py)   | Command-line interface options for the readme-ai application.-Includes options for API key, badges, emojis, image, language, max_tokens, model, offline mode, output file, repository URL, temperature, template file, tree depth, and Vertex AI configuration.                                                                                                                                            |
| [commands.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/commands.py) | Central CLI command for `readme-ai` app, offering a rich set of options.-Facilitates user interaction and configuration for generating README files.-Easily customizable through command-line arguments, enabling tailored README creation.-Implements a concise and user-friendly interface for generating ReadMe files.-Integrates with the larger app architecture, serving as the primary entry point. |

</details>

<details closed><summary>readmeai.llms</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [cache.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/cache.py)       | The CacheManager class in the `readme-ai/llms` module serves as a custom cache for handling LLM responses. It supports caching with optional expiry times to optimize performance. Each response is hashed and stored using an efficient storage mechanism. The cache manager features methods for retrieving cached responses and adding new ones while adhering to a specified maximum size limit. It also includes a mechanism for evicting the oldest item when the cache reaches its limit. |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/prompts.py)   | In the `readmeai` package, `readmeai/llms/prompts.py` manages prompts for LLM API calls. It includes functions to retrieve prompt templates, inject context, and generate prompts for specific types like features, overviews, and slogans. These prompts are used to generate improved README content based on code analysis and user-provided context.                                                                                                                                         |
| [tokenize.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/tokenize.py) | The `tokenize.py` module in `readme-ai` provides text tokenization utilities. Functions like `count_tokens` calculate the number of tokens in a text string, while `truncate_tokens` truncates text to a specified token limit. The module caches encodings for different encoding schemes to optimize performance. It also dynamically adjusts maximum token limits based on specific prompts, ensuring optimal tokenization results.                                                           |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                         |
| [git_metadata.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_metadata.py) | This code helps retrieve Git repository metadata. It defines a dataclass to store the data, parses the raw data, and fetches metadata from a given repository. It relies on other helper functions to construct the correct API URL, which is flexible enough to work with various Git hosts. The metadata includes repo name, owner, star count, programming languages, topics, license details, and more. |
| [git_utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_utils.py)       | Clones Git repos and returns the path to the local clone.-Fetches Git API and file URLs based on the repo URL.-Validates and rectifies file permissions and Git executable path.-Ensures consistent repo cloning and URL generation for various Git services.-Offers a path to the Git executable, considering different OS and environments.                                                               |

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

### ► Running `readme-ai`

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
