<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">README-AI</h1>
</p>
<p align="center">
    <em>Automated README documenation generator!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#-repository-structure)
- [📦 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

The `readme-ai` project is an automated README generator leveraging AI to synthesize content for developer tools. It offers functionalities like parsing various configuration files, extracting dependencies, and generating markdown files with badges. With features such as automated test setup, Docker image building, and PyPI deployment, `readme-ai` streamlines the process of creating engaging project documentation. By utilizing large language model APIs, this tool enhances developer productivity by automating the generation of README files based on repository settings and model configurations.

---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project leverages a Python 3.10 environment, utilizing the readmeai package for AI content synthesis. It includes a CLI entrypoint for generating README files based on repository and model settings. |
| 🔩 | **Code Quality**  | The codebase follows best practices with automated testing using nox and pytest. It includes linting, formatting, and packaging commands in the Makefile for maintaining code quality. |
| 📄 | **Documentation** | Extensive documentation is provided for setting up the environment, managing dependencies, and automating tasks. README files are generated with badges and content for various GitHub repositories. |
| 🔌 | **Integrations**  | Key integrations include Google Cloud services, OpenAI for language models, and GitHub Actions for automated workflows like release management and coverage monitoring. |
| 🧩 | **Modularity**    | The codebase is modular with abstract factory modules for parsers, parsers for various languages and frameworks, and utility functions for file handling and logging. |
| 🧪 | **Testing**       | Testing frameworks like pytest are used for automated testing, with additional tools like pytest-asyncio for asynchronous testing and pytest-cov for coverage reporting. |
| ⚡️  | **Performance**   | The project focuses on efficiency with tools like aiohttp for asynchronous HTTP requests, tenacity for retry logic, and anyio for asynchronous concurrency. |
| 🛡️ | **Security**      | Security measures include handling API keys securely, validating Git repository URLs, and managing file permissions for cloning and fetching repositories. |
| 📦 | **Dependencies**  | Key dependencies include shapely, cachetools, aiohttp, OpenAI, numpy, google-cloud services, pytest, and various other libraries for different functionalities. |

---

## 🗂️ Repository Structure

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

## 📦 Modules

<details closed><summary>.</summary>

| File                                                                             | Summary                                                                                                                  |
| ---                                                                              | ---                                                                                                                      |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/master/Dockerfile)         | The Dockerfile sets up a Python 3.10 environment, installs readmeai package, and configures the CLI entrypoint.          |
| [Makefile](https://github.com/eli64s/readme-ai/blob/master/Makefile)             | The Makefile in the repository provides commands for cleaning, formatting, linting, testing, and packaging the software. |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/master/pyproject.toml) | Automated README generator for developer tools, leveraging large language model APIs.                                    |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/master/noxfile.py)         | Automated test setup using nox and pytest for the readme-ai repository.                                                  |

</details>

<details closed><summary>setup</summary>

| File                                                                                       | Summary                                                                                                                              |
| ---                                                                                        | ---                                                                                                                                  |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh)                 | The `setup.sh` script automates environment setup for the README-AI project, ensuring Python compatibility and package installation. |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt) | Manages Python package dependencies for the readme-ai project using requirements.txt.                                                |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml) | Define software dependencies for the `readmeai` project using Conda and Python.                                                      |

</details>

<details closed><summary>scripts</summary>

| File                                                                                 | Summary                                                                              |
| ---                                                                                  | ---                                                                                  |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh) | Generates markdown files with badges and content for various GitHub repositories.    |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh)           | Automates PyPI deployment for `readmeai` package using `twine` and `build`.          |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh)         | The `clean.sh` script removes build, test, and Python artifacts from the repository. |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh)       | Automates Docker image building and publishing for readme-ai repository.             |

</details>

<details closed><summary>.github</summary>

| File                                                                                               | Summary                                                                  |
| ---                                                                                                | ---                                                                      |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml) | Automated release drafter for versioning based on changelog conventions. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                           | Summary                                                                                 |
| ---                                                                                                            | ---                                                                                     |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml)                 | Automated coverage workflow for readme-ai project. Monitors test coverage on each push. |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml) | Automates release pipeline using GitHub Actions for the readme-ai repository.           |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml)   | Automates release notes generation using Release Drafter in the GitHub workflow.        |

</details>

<details closed><summary>readmeai</summary>

| File                                                                                    | Summary                                                                                           |
| ---                                                                                     | ---                                                                                               |
| [readmeai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/readmeai.py)     | Generates README file based on repository and model settings, utilizing AI for content synthesis. |
| [exceptions.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/exceptions.py) | CLI, Git, file system errors, readme generation, and unsupported services.                        |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                      | Summary                                                                                   |
| ---                                                                                       | ---                                                                                       |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/factory.py) | Abstract factory module for project file parsers across various languages and frameworks. |

</details>

<details closed><summary>readmeai.parsers.configuration</summary>

| File                                                                                                          | Summary                                                                                                               |
| ---                                                                                                           | ---                                                                                                                   |
| [ansible.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/ansible.py)       | Parse Ansible configuration files for repositorys AI project.                                                         |
| [properties.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/properties.py) | Parser for.properties configuration files extracting connection strings and package names.                            |
| [apache.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/apache.py)         | Parser for Apache configuration files in the `readme-ai` repository.                                                  |
| [docker.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/docker.py)         | Parser for Docker configuration files extracting package names from Dockerfile and services from docker-compose.yaml. |
| [nginx.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/nginx.py)           | Parser for Nginx configuration files in the `readme-ai` repository.                                                   |

</details>

<details closed><summary>readmeai.parsers.language</summary>

| File                                                                                             | Summary                                                                                                      |
| ---                                                                                              | ---                                                                                                          |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/cpp.py)       | CMake, configure.ac, Makefile.am.                                                                            |
| [swift.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/swift.py)   | Parse Swift Package.swift files to extract package names for dependencies.                                   |
| [python.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/python.py) | Parses Python dependency files in TOML and YAML formats, extracting package names for various build systems. |
| [go.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/go.py)         | Parse Go package dependencies from go.mod files in the readmeai/parsers/language/go.py file.                 |
| [rust.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/rust.py)     | Extract Rust package names from cargo.toml files in the repository.                                          |

</details>

<details closed><summary>readmeai.parsers.cicd</summary>

| File                                                                                               | Summary                                                                           |
| ---                                                                                                | ---                                                                               |
| [bitbucket.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/bitbucket.py) | Parser for Bitbucket Pipelines configuration files in the `readme-ai` repository. |
| [travis.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/travis.py)       | Parser for.travis.yml configuration files in the readme-ai repository.            |
| [gitlab.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/gitlab.py)       | Parser for GitLab CI configuration files in the readme-ai repository.             |
| [jenkins.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/jenkins.py)     | Parser for Jenkinsfile configuration files in the readme-ai repository.           |
| [github.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/github.py)       | Parser for GitHub Actions configuration files in the `readme-ai` repository.      |
| [circleci.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/circleci.py)   | Parser for CircleCI configuration files in the readme-ai repository.              |

</details>

<details closed><summary>readmeai.parsers.orchestration</summary>

| File                                                                                                          | Summary                                                                  |
| ---                                                                                                           | ---                                                                      |
| [kubernetes.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/orchestration/kubernetes.py) | Parser for Kubernetes configuration files in the `readme-ai` repository. |

</details>

<details closed><summary>readmeai.parsers.infrastructure</summary>

| File                                                                                                                   | Summary                                                                         |
| ---                                                                                                                    | ---                                                                             |
| [terraform.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/infrastructure/terraform.py)           | Parser for Terraform configuration files in the `readme-ai` repository.         |
| [cloudformation.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/infrastructure/cloudformation.py) | Parse AWS CloudFormation configuration files in the `cloudformation.py` parser. |

</details>

<details closed><summary>readmeai.parsers.package</summary>

| File                                                                                                | Summary                                                                                                                              |
| ---                                                                                                 | ---                                                                                                                                  |
| [composer.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/composer.py) | Parse PHP Composer configuration files for repositorys architecture.                                                                 |
| [npm.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/npm.py)           | Parse npm and yarn.lock files to extract dependencies for documentation generation.                                                  |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/gradle.py)     | Parser for extracting package names from Gradle dependency files.                                                                    |
| [nuget.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/nuget.py)       | Parser for NuGet.Config files in.NET, located in readmeai/parsers/package/nuget.py.                                                  |
| [yarn.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/yarn.py)         | Parser for yarn.lock files extracting package names.                                                                                 |
| [pip.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/pip.py)           | Parser for Pip configuration files in the readme-ai repository.                                                                      |
| [maven.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/maven.py)       | MavenParser extracts package names from Maven pom.xml files. **Features:** Parses pom.xml for dependencies, handling parsing errors. |
| [gem.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/gem.py)           | Parser for Gemfile.lock (Ruby) configuration files in the readme-ai repository.                                                      |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                         | Summary                                                                                                                                                     |
| ---                                                                                          | ---                                                                                                                                                         |
| [models.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/models.py)         | Abstract base class for the Large Language Model (LLM) API handlers. Manages HTTP client, processes prompts, and generates text responses from the LLM API. |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py) | Processes repository files, extracts metadata, and generates file context. Handles dependencies, languages, and tokenizes content.                          |
| [parsers.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/parsers.py)       | Abstract base class for dependency file parsers in the `readme-ai` repository.                                                                              |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py)           | Filter files based on rules, set LLM environment variables.                                                                                                 |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                           | Summary                                                                                 |
| ---                                                                                            | ---                                                                                     |
| [enums.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/enums.py)           | Enums defining options for Git services, badges, images, and LLM API keys.              |
| [validators.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/validators.py) | Validates Git repository URLs and paths, extracting repository names and service hosts. |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/utils.py)           | Utility methods for reading package resources, handling different file formats.         |
| [settings.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py)     | API, Git, Markdown, Resources.                                                          |

</details>

<details closed><summary>readmeai.config.settings</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                                                            |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                                                |
| [prompts.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/prompts.toml)     | The `prompts.toml` file in `readmeai/config/settings` provides templates for generating README content. It includes prompts for creating a project logo and a Markdown table summarizing key project features. The file aims to streamline the process of crafting engaging project documentation. |
| [parsers.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/parsers.toml)     | Parse and analyze project configuration and dependency files for various CI/CD, configuration, infrastructure, monitoring, and orchestration setups.                                                                                                                                               |
| [blacklist.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/blacklist.toml) | Excludes specified directories, file extensions, and names from preprocessing.                                                                                                                                                                                                                     |
| [languages.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/languages.toml) | Defines programming language extensions and their names for the project.                                                                                                                                                                                                                           |
| [config.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/config.toml)       | This code file configures settings for the README AI project, including file resources, Git repository, language model API, and markdown templates.                                                                                                                                                |
| [markdown.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/markdown.toml)   | This code file generates a README.md template for the parent repository, showcasing project details and badges.                                                                                                                                                                                    |
| [commands.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/commands.toml)   | Config file specifying language-specific install, run, and test commands for various programming languages.                                                                                                                                                                                        |

</details>

<details closed><summary>readmeai.utils</summary>

| File                                                                                              | Summary                                                                                                |
| ---                                                                                               | ---                                                                                                    |
| [formatter.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/formatter.py)       | Utility functions for cleaning and formatting text generated by LLMs.                                  |
| [file_handler.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/file_handler.py) | FileHandler class for reading and writing various file formats with caching support.                   |
| [logger.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/logger.py)             | Custom logger for readme-ai CLI with colored log output and emoji indicators for different log levels. |

</details>

<details closed><summary>readmeai.models</summary>

| File                                                                                     | Summary                                                                                                                              |
| ---                                                                                      | ---                                                                                                                                  |
| [offline.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/offline.py) | OfflineHandler in `readmeai/models/offline.py` manages offline mode, providing default placeholders when API service is unavailable. |
| [vertex.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/vertex.py)   | Implements Google Vertex AI LLM API for generative models with retry logic and response handling.                                    |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/tokens.py)   | Count tokens, truncate text, and adjust max tokens based on a prompt.                                                                |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/factory.py) | Registry for LLM handlers based on CLI input, instantiates appropriate handler.                                                      |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/prompts.py) | Handles prompt processing for LLM API requests, generating and formatting prompts based on context and templates.                    |
| [openai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/openai.py)   | <code>► INSERT-TEXT-HERE</code>                                                                                                      |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                  | Summary                                                                                                                               |
| ---                                                                                   | ---                                                                                                                                   |
| [options.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py) | Align text, select model, badge style, emojis, image, language, tokens, model, output, repository, temperature, template, tree depth. |
| [main.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/main.py)       | CLI entrypoint for readme-ai app, facilitating generation of README files with customizable options.                                  |

</details>

<details closed><summary>readmeai.generators</summary>

| File                                                                                               | Summary                                                                                                                              |
| ---                                                                                                | ---                                                                                                                                  |
| [tree.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tree.py)             | Generates directory tree structure for a code repository.                                                                            |
| [builder.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/builder.py)       | Header, code summaries, directory tree, quickstart, and contributing.                                                                |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/utils.py)           | The `utils.py` file in `readmeai/generators` removes emojis from markdown content and splits markdown documents by level 2 headings. |
| [badges.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/badges.py)         | Generates badges for README using shields.io and skill icons.                                                                        |
| [tables.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tables.py)         | Generates markdown tables for LLM text responses in README using provided data.                                                      |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/quickstart.py) | Generates Quickstart section for README with top language setup commands and prerequisites.                                          |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                         | Summary                                                                                                                                                |
| ---                                                                                          | ---                                                                                                                                                    |
| [git.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git.py)           | Git.py provides functions for cloning, validating repositories, and fetching API URLs. It also handles git executable validation and file permissions. |
| [metadata.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/metadata.py) | Retrieve GitHub repository metadata using helper methods for Git host providers.                                                                       |

</details>

---

## 🚀 Getting Started

**System Requirements**

* **Python**: `version x.y.z`

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the readme-ai repository:
>
> ```console
> $ git clone https://github.com/eli64s/readme-ai
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd readme-ai
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

### 🤖 Usage

<h4>From <code>source</code></h4>

> Run readme-ai using one of the following commands:
> ```console
> $ python main.py
> ```

### 🧪 Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

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
<p align="center">
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
