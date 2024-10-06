[<img src="https://www.svgrepo.com/show/395851/balloon.svg" align="left" width="20%" padding="20">]()

## &nbsp;&nbsp; README-AI

&nbsp;&nbsp;&nbsp;&nbsp; *Empowering READMEs with AI magic!*

<p align="left">&nbsp;&nbsp;
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&logo=opensourceinitiative&logoColor=white&color=DE3163" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=DE3163" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=DE3163" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=DE3163" alt="repo-language-count">
</p>

<br>

##### 🔗 Quick Links

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
    - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

README-AI is an innovative open-source project that leverages AI models to automatically generate README files for software repositories. By analyzing code structures and metadata, README-AI creates comprehensive documentation, including code summaries, badges, and directory structures. This project streamlines the documentation process, enhancing project visibility and developer collaboration.

---

## 👾 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project has a modular architecture with clear separation of concerns. It leverages various AI libraries for content generation and integrates well with external services like Google Generative AI. The codebase is organized and follows best practices for scalability and maintainability. |
| 🔩 | **Code Quality**  | The codebase maintains high quality with consistent style and adherence to PEP 8 standards. It includes comprehensive unit tests and continuous integration with GitHub Actions for automated checks. Code reviews and linting tools ensure clean and readable code. |
| 📄 | **Documentation** | The project provides extensive documentation covering installation, usage, and contribution guidelines. It includes detailed explanations of the codebase, API references, and examples for users to easily understand and contribute to the project. |
| 🔌 | **Integrations**  | Key integrations include Google Generative AI for content creation, GitHub Actions for CI/CD, and various AI libraries for text processing. External dependencies like requests, aiosignal, and multidict enhance functionality and extend capabilities. |
| 🧩 | **Modularity**    | The codebase exhibits high modularity with reusable components and clear interfaces. It allows for easy extension and customization of features without impacting the core functionality. The project structure promotes code reusability and maintainability. |
| 🧪 | **Testing**       | Testing frameworks like pytest and pytest-asyncio are used for unit and asynchronous testing. The codebase includes test coverage reports and test automation tools to ensure robustness and reliability of the project. |
| ⚡️  | **Performance**   | The project demonstrates efficient resource usage and speed in content generation tasks. It leverages asynchronous processing with libraries like aiohttp and async-timeout for improved performance. Continuous optimization efforts ensure smooth execution and responsiveness. |
| 🛡️ | **Security**      | Security measures include data protection mechanisms, access control policies, and secure communication protocols. Dependencies like google-auth and rsa enhance security features, while best practices are followed to safeguard user data and prevent vulnerabilities. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include Google Generative AI, requests, pytest, aiosignal, and multidict. These libraries enhance functionality, provide essential features, and integrate seamlessly with the project for enhanced capabilities. |

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
    │   ├── _agent.py
    │   ├── _exceptions.py
    │   ├── cli
    │   ├── config
    │   ├── core
    │   ├── generators
    │   ├── models
    │   ├── parsers
    │   ├── services
    │   └── utils
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
        ├── cli
        ├── config
        ├── conftest.py
        ├── core
        ├── generators
        ├── models
        ├── parsers
        ├── services
        ├── test_agent.py
        ├── test_exceptions.py
        └── utils
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/main/Dockerfile) | Builds a Docker image for the readmeai package, setting up a non-root user, installing dependencies, and configuring the environment. The image runs the readmeai CLI by default. |
| [Makefile](https://github.com/eli64s/readme-ai/blob/main/Makefile) | Manages repository cleanup, formatting, linting, and testing tasks.-Builds Conda package, generates requirements file, and searches for a word in the directory.-Executes various commands for maintaining code quality and project organization. |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/main/pyproject.toml) | Generates README files using AI models. Key features include markdown generation, badge integration, and AI-powered content creation. Supports Python, markdown, and various AI libraries. |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/main/noxfile.py) | Executes tests across multiple Python versions by installing the package and running the test suite with coverage reports. The code ensures seamless testing workflow for the repositorys Python versions. |

</details>

<details closed><summary>setup</summary>

| File | Summary |
| --- | --- |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/main/setup/setup.sh) | Facilitates environment setup for README-AI project. Checks for and installs dependencies like tree, Git, Conda, and Python 3.8+. Creates readmeai Conda environment, activates it, adds Python path to PATH, and installs required packages. |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/main/setup/requirements.txt) | Specifies dependencies for the project, ensuring compatibility with Python versions. Key libraries include aiohttp, pydantic, and google-ai-generativelanguage. Enhances functionality and performance through external packages. |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/main/setup/environment.yaml) | Defines project dependencies and environment settings for the readmeai package. Specifies Python version, required packages, and channels for package installation. |

</details>

<details closed><summary>tests</summary>

| File | Summary |
| --- | --- |
| [parsers](https://github.com/eli64s/readme-ai/blob/main/tests/parsers) | Validates data parsing functionality ensuring accurate extraction and transformation. Enhances data integrity and reliability within the repositorys architecture. |

</details>

<details closed><summary>scripts</summary>

| File | Summary |
| --- | --- |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/run_batch.sh) | Generates dynamic markdown files for multiple repositories, customizing badges, alignment, and images. Executes commands based on repository index, incorporating various API options and styling choices. |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/pypi.sh) | Deploys the readmeai package to PyPI, ensuring a clean build and successful upload. Utilizes twine for secure distribution, enhancing the project's accessibility and visibility within the Python community. |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/clean.sh) | Cleans build, test, coverage, and Python artifacts by removing various artifact directories and files. Provides commands for cleaning specific artifact types. |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/main/scripts/docker.sh) | Builds and publishes a Docker image for the readme-ai project, supporting multiple platforms. Executes Docker Buildx commands to create, build, and push the image. |

</details>

<details closed><summary>.github</summary>

| File | Summary |
| --- | --- |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/release-drafter.yml) | Defines release categories and templates based on conventional changelog standards. Categorizes changes into features, bug fixes, chores, deprecations, removals, security, documentation, and dependency updates. Resolves version increments and generates release notes. |

</details>

<details closed><summary>.github.workflows</summary>

| File | Summary |
| --- | --- |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/coverage.yml) | Generates test coverage reports for the README AI project. Integrates with GitHub Actions to ensure code quality and maintain high test coverage levels. |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-pipeline.yml) | Automates release process, ensuring smooth deployment. Orchestrates versioning, changelog updates, and GitHub releases. Enhances project management and collaboration. |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/main/.github/workflows/release-drafter.yml) | Automates release notes generation based on pull requests, enhancing project transparency and communication. Integrates with GitHub Actions to streamline the release process and foster community engagement. |

</details>

<details closed><summary>readmeai</summary>

| File | Summary |
| --- | --- |
| [_agent.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/_agent.py) | Generates README.md file using AI models, handles API settings, and orchestrates file generation process. Clones repository, preprocesses files, requests AI model responses, and builds README.md with features. Handles image generation based on API availability. |
| [_exceptions.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/_exceptions.py) | CLIError, GitCloneError, GitValidationError, FileSystemError, FileReadError, FileWriteError, ReadmeGeneratorError, UnsupportedServiceError. Each exception handles specific errors related to CLI, Git operations, file system, readme generation, and service handling. |

</details>

<details closed><summary>readmeai.parsers</summary>

| File | Summary |
| --- | --- |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/factory.py) | Registers various file parsers for different programming languages and package managers. Provides a dictionary of callable parser methods for project file parsing. |

</details>

<details closed><summary>readmeai.parsers.configuration</summary>

| File | Summary |
| --- | --- |
| [ansible.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/configuration/ansible.py) | Extracts Ansible configuration details from playbook.yml and site.yml files. |
| [properties.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/configuration/properties.py) | Extracts configuration properties from.properties files using regex patterns for JDBC connection strings and other packages. |
| [apache.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/configuration/apache.py) | Parses Apache configuration files for the README AI repository, extracting key settings and directives. |
| [docker.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/configuration/docker.py) | Parses Docker configuration files to extract package names and services. Handles Dockerfile and docker-compose.yaml parsing errors gracefully. |
| [nginx.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/configuration/nginx.py) | Parses Nginx configuration files in the readme-ai repository, extracting key settings and directives. |

</details>

<details closed><summary>readmeai.parsers.language</summary>

| File | Summary |
| --- | --- |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/language/cpp.py) | CMakeParser for CMakeLists.txt, ConfigureAcParser for configure.ac, and MakefileAmParser for Makefile.am. Each parser handles specific file types to identify dependencies, libs, and software. |
| [swift.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/language/swift.py) | Extracts Swift package names from Package.swift files by parsing dependencies. |
| [python.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/language/python.py) | Parses Python dependency files to extract package names without version specifiers.-Handles requirements.txt, TOML (Pipenv, Poetry, Flit), and YAML (environment.yml) formats.-Ensures robust error handling for parsing exceptions. |
| [go.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/language/go.py) | Extracts Go package dependencies from go.mod files using regex pattern matching. Inherits from BaseFileParser to parse content and handle parsing errors. Contributes to the repositorys parsers module for language-specific file parsing. |
| [rust.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/language/rust.py) | Extracts Rust package names from cargo.toml files using toml parsing library. |

</details>

<details closed><summary>readmeai.parsers.cicd</summary>

| File | Summary |
| --- | --- |
| [bitbucket.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/cicd/bitbucket.py) | Extracts Bitbucket Pipelines configuration details for CI/CD workflows. |
| [travis.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/cicd/travis.py) | Extracts CI/CD configurations from.travis.yml files. |
| [gitlab.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/cicd/gitlab.py) | Extracts GitLab CI configuration details from.gitlab-ci.yml files. |
| [jenkins.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/cicd/jenkins.py) | Extracts Jenkinsfile configurations for CI/CD pipelines. Identifies and parses Jenkinsfile settings for automation and deployment processes within the repositorys architecture. |
| [github.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/cicd/github.py) | Extracts GitHub Actions configurations for CI/CD pipelines from.github/workflows/ directory. |
| [circleci.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/cicd/circleci.py) | Parses CircleCI configuration files in the readme-ai repository. |

</details>

<details closed><summary>readmeai.parsers.orchestration</summary>

| File | Summary |
| --- | --- |
| [kubernetes.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/orchestration/kubernetes.py) | Parses Kubernetes configuration files for the README AI repository. |

</details>

<details closed><summary>readmeai.parsers.infrastructure</summary>

| File | Summary |
| --- | --- |
| [terraform.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/infrastructure/terraform.py) | Extracts Terraform configurations from main.tf files for parsing. |
| [cloudformation.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/infrastructure/cloudformation.py) | Extracts AWS CloudFormation configuration details from cloudformation.yaml files. |

</details>

<details closed><summary>readmeai.parsers.package</summary>

| File | Summary |
| --- | --- |
| [composer.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/composer.py) | Extracts PHP Composer configuration details from composer.json files. |
| [npm.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/npm.py) | Extracts dependencies from package.json and yarn.lock files for the parent repositorys architecture. Parses JSON dependency files and yarn.lock files to retrieve package names for different sections. |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/gradle.py) | Parses Gradle dependency files to extract package names. Handles both build.gradle and build.gradle.kts formats, utilizing regex patterns for parsing. Implements error handling for parsing exceptions. |
| [nuget.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/nuget.py) | Parses NuGet.Config files for.NET configuration settings. |
| [yarn.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/yarn.py) | Extracts package names from a yarn.lock file using regex pattern matching. |
| [pip.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/pip.py) | Extracts and interprets Pip configuration files for the parent repositorys AI documentation tool. |
| [maven.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/maven.py) | Extracts Maven package names from pom.xml files, handling parsing errors. Parses groupId, artifactId, and version using regex. Appends spring if found in dependencies. Returns a set of unique dependencies. |
| [gem.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parsers/package/gem.py) | Parses Gemfile.lock (Ruby) configuration files in the readme-ai repository. |

</details>

<details closed><summary>readmeai.core</summary>

| File | Summary |
| --- | --- |
| [models.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/models.py) | Orchestrates batch processing of prompts for Large Language Model API, handling dependencies and file contexts.-Generates text responses based on prompts, including code summaries for project files.-Manages HTTP client session lifecycle for API requests. |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/preprocess.py) | Generates FileContext instances for repository files, extracts metadata, and processes dependencies using a factory pattern. Returns a list of dependencies and raw file data. |
| [parsers.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/parsers.py) | Defines an abstract base class for dependency file parsers in the core module. Implements methods for parsing file content and handling parsing errors. Centralizes error logging for consistent exception handling. |
| [logger.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/logger.py) | Implements a custom logger with color and emoji support for the readme-ai package. Provides logging methods for different levels. |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/utils.py) | Defines utility methods for configuring LLM API environments. Enumerates keys for service environment variables. Sets service to offline mode if necessary. Retrieves and validates LLM environment variables based on specified service, handling offline mode and missing keys. |

</details>

<details closed><summary>readmeai.config</summary>

| File | Summary |
| --- | --- |
| [validators.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/validators.py) | Validates Git repository URLs and paths, extracting repository names and setting Git service hosts based on input. |
| [settings.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings.py) | Defines configuration settings for readme-ai package, including API, file paths, Git repository, Markdown templates, and model settings. Loads base and additional configuration files for CLI. |

</details>

<details closed><summary>readmeai.config.settings</summary>

| File | Summary |
| --- | --- |
| [prompts.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/prompts.toml) | Summarize** the purpose and features of the `prompts.toml` file in the `readmeai` repository. Describe large language model prompt templates for generative tasks, focusing on architecture, code quality, documentation, integrations, modularity, testing, performance, security, dependencies, and scalability. |
| [parsers.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/parsers.toml) | Defines project configuration files to parse CI/CD, configuration, infrastructure, monitoring, orchestration, package managers, properties, and language-specific files. |
| [blacklist.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/blacklist.toml) | Filters out specified directories, file extensions, and file names from preprocessing in the repository. Helps maintain a clean codebase by excluding common unwanted files and folders during development and deployment processes. |
| [languages.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/languages.toml) | Defines programming language extensions and their names for the project. Centralizes language configuration for consistency across the codebase. Facilitates language-specific operations and enhances code readability. |
| [config.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/config.toml) | Defines default API, file resources, Git repo, language model, Markdown template settings, badges, TOC, project structure, modules, installation, usage, tests, roadmap, contributing, license, acknowledgments, and contact details for the parent repository. |
| [markdown.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/markdown.toml) | Defines Markdown templates for README.md, including badges, quick links, project structure, and contributing guidelines. |
| [commands.toml](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/commands.toml) | Defines language-specific commands for installation, running, and testing in the project. Organized by programming language, it provides standardized instructions for developers to set up, execute, and test code across various languages. |

</details>

<details closed><summary>readmeai.ingestion./summary>

| File | Summary |
| --- | --- |
| [file_handler.py](https://github.com/eli64s/readme-ai/blob/main/readmeai.ingestion.file_handler.py) | Handles file I/O operations for various file formats, including JSON, Markdown, TOML, TXT, and YAML. Provides methods to read and write content to files, with error handling. Implements a caching mechanism for efficient file reading. |
| [text_cleaner.py](https://github.com/eli64s/readme-ai/blob/main/readmeai.ingestion.text_cleaner.py) | Cleans and formats LLM API responses by post-processing text. Removes unwanted characters, formats Markdown tables, and ensures proper capitalization. Enhances readability and structure of generated text. |
| [file_resources.py](https://github.com/eli64s/readme-ai/blob/main/readmeai.ingestion.file_resources.py) | Retrieves absolute path to package resource file, prioritizing `importlib.resources` over `pkg_resources`. Handles resource access errors gracefully. |

</details>

<details closed><summary>readmeai.models</summary>

| File | Summary |
| --- | --- |
| [offline.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/models/offline.py) | Defines an OfflineHandler model for CLI operation without an LLM API service. Sets default values for offline mode and returns placeholder text instead of LLM API responses. |
| [gemini.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/models/gemini.py) | Implements Google Clouds Gemini API handler with retry logic for generating text responses. Handles API requests, processes responses, and logs output. Inherits from a base model handler and initializes API settings. |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/models/tokens.py) | Handles tokenization and truncation of text based on specified settings. Counts tokens in a text string, truncates text to a maximum token count, and adjusts the maximum token count based on a specific prompt. Caches encoding for efficiency. |
| [dalle.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/models/dalle.py) | Generates and downloads images using OpenAIs DALL-E model. Initializes model settings, formats prompt string, and handles image generation and download. Handles errors and logs events. |
| [factory.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/models/factory.py) | Generates appropriate LLM handler based on CLI input using a model factory. Handles different LLM services like Offline, OpenAI, and Gemini. Ensures compatibility with CLI configurations. |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/models/prompts.py) | Generates and formats prompts for LLM API requests based on provided context. Retrieves prompt templates and injects context into them. Async functions create additional and summary prompts for LLM API, incorporating various data points. |
| [openai.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/models/openai.py) | Implements OpenAI API LLM handler with Ollama support. Initializes model settings, builds payload for API requests, and processes responses. Handles retries for network errors. Logs responses and cleans generated text. |

</details>

<details closed><summary>readmeai.cli</summary>

| File | Summary |
| --- | --- |
| [options.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/options.py) | Defines CLI options for badge icons, header images, and LLM API key selection. Enables user input for custom image URLs and badge styles. Facilitates setting alignment, language, model, and output file for README generation. |
| [main.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/cli/main.py) | Orchestrates CLI commands for readme-ai package.-Parses user inputs for AI model generation.-Integrates with readme_agent for generating READMEs.-Facilitates customization of output through various options. |

</details>

<details closed><summary>readmeai.generators</summary>

| File | Summary |
| --- | --- |
| [tree.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/tree.py) | Generates directory tree structure for a code repository, enhancing visualization and organization. Builds a formatted tree with specified depth, improving repository navigation and understanding. |
| [builder.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/builder.py) | Header, code summaries, directory tree, Getting Started, and Contributing. Builds the README file with badges, tables, tree structure, setup data, and contribution guidelines. Handles customization based on configuration settings. |
| [utils.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/utils.py) | Removes default emojis from markdown content-Splits markdown by level 2 headings-Updates heading names by removing emojis, underscores, and spaces |
| [badges.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/badges.py) | Generates and formats SVG badges for README using shields.io and skill icons. Builds metadata badges, HTML badges for project dependencies, and skill icons. Handles badge alignment and styles based on configuration settings. |
| [tables.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/tables.py) | Generates markdown tables for code summaries, grouping them by sub-directory. Formats data into readable tables for README files, enhancing project documentation. |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/quickstart.py) | Generates the Quickstart section for the README by dynamically determining top language, setup commands, and prerequisites based on code summaries and configuration settings. |

</details>

<details closed><summary>readmeai.services</summary>

| File | Summary |
| --- | --- |
| [git.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/git.py) | Implements Git operations for cloning and validating repositories. Enumerates Git service providers with API and file URL templates. Functions for cloning, removing hidden files, fetching API URLs, and finding Git executable paths. |
| [metadata.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/services/metadata.py) | Retrieves GitHub repository metadata via the host providers API. Parses raw data into a structured dataclass containing repository details, statistics, URLs, programming languages, topics, and license information. Handles errors gracefully. |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version x.y.z`

### 📦 Installation

Build the project from source:

1. Clone the readme-ai repository:
```sh
❯ git clone https://github.com/eli64s/readme-ai
```

2. Navigate to the project directory:
```sh
❯ cd readme-ai
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

### 🧪 Tests

Execute the test suite using the following command:

```sh
❯ pytest
```

---

## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

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

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
