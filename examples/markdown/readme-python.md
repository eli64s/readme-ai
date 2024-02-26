<p align="left">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" alt="project-logo">
</p>
<p align="left">
    <h1 align="left">README-AI</h1>
</p>
<p align="left">
    <em>Generate Engaging READMEs with ReadmeAI in Seconds!</em>
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

The `readme-ai` project is an AI-powered tool for automating README file generation within a code repository. Using natural language models, it extracts project metadata, dependencies, and setup instructions to create comprehensive READMEs. The system supports multiple programming languages, integrates with Git services, and offers CLI functionality for customization. By simplifying the documentation process, `readme-ai` enhances project discoverability, improves onboarding for new contributors, and ensures consistent communication of project details. With features like badge generation, directory tree structure, and multilingual support, `readme-ai` streamlines README creation, fostering better project understanding and collaboration.

---

## 📦 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture with various components like parsers, generators, file handlers, and CLI functionalities. It leverages AI models for README generation and integrates with Git services efficiently. |
| 🔩 | **Code Quality**  | The codebase maintains high standards of quality with consistent style, modular design, and clear documentation. It follows best practices for Python development, ensuring readability and maintainability. |
| 📄 | **Documentation** | Extensive documentation covers setup, usage, architecture, and contribution guidelines. Detailed explanations, examples, and API references aid users in understanding and extending the project. |
| 🔌 | **Integrations**  | The project integrates with Git services, LLM APIs, and various Python libraries for functionality like file parsing, text generation, and repository metadata retrieval. These integrations enhance the project's capabilities. |
| 🧩 | **Modularity**    | The codebase is highly modular, allowing easy extension and reuse of components. Each module focuses on a specific task, promoting code organization and scalability. |
| 🧪 | **Testing**       | Testing is thorough with frameworks like `pytest`, coverage reporting, and automated testing pipelines. Test suites ensure code reliability and prevent regressions. |
| ⚡️  | **Performance**   | The project emphasizes efficiency, utilizing asynchronous programming, optimized algorithms, and caching mechanisms to enhance speed and resource utilization. |
| 🛡️ | **Security**      | Security measures include API key handling, data encryption, and access control for repository cloning. The project adheres to best practices for data protection and secure interactions. |
| 📦 | **Dependencies**  | Key dependencies include libraries for Git operations, HTTP requests, Markdown generation, AI models, and testing frameworks. These dependencies enhance functionality and streamline development. |

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

| File                                                                             | Summary                                                                                                        |
| ---                                                                              | ---                                                                                                            |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/master/Dockerfile)         | Dockerfile sets up Python environment and installs readmeai package for CLI usage.                             |
| [Makefile](https://github.com/eli64s/readme-ai/blob/master/Makefile)             | Makefile manages repository cleanup, linting, and testing with commands like format, lint, pytest, and search. |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/master/pyproject.toml) | Automated README file generator for the readme-ai repository architecture.                                     |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/master/noxfile.py)         | Automated test suite for the repository using `nox` and `pytest` across various Python versions.               |

</details>

<details closed><summary>setup</summary>

| File                                                                                       | Summary                                                                                                                                          |
| ---                                                                                        | ---                                                                                                                                              |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh)                 | The `setup.sh` file provides an automated setup for the `readme-ai` repository, ensuring the correct environment and dependencies are installed. |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt) | Manages Python package requirements for the repository with version constraints.                                                                 |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml) | Generates environment settings for readme-ai project using Conda with Python dependencies.                                                       |

</details>

<details closed><summary>scripts</summary>

| File                                                                                 | Summary                                                                                                                             |
| ---                                                                                  | ---                                                                                                                                 |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh) | Automated batch creation of README files for various repositories using different styles and badges.                                |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh)           | Pypi.sh` script automates building & uploading `readmeai` package to PyPI.                                                          |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh)         | The `clean.sh` script removes artifacts, including build, test, and cache files within the project structure.                       |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh)       | The `docker.sh` script in the `scripts` folder sets up a Docker Buildx builder, builds and publishes a multi-platform Docker image. |

</details>

<details closed><summary>.github</summary>

| File                                                                                               | Summary                                                                                                            |
| ---                                                                                                | ---                                                                                                                |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml) | Manages release drafting in the repository following conventional versioning schemes and changelog categorization. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                           | Summary                                                                           |
| ---                                                                                                            | ---                                                                               |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml)                 | Generates test coverage report via GitHub Actions for ReadmeAI.                   |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml) | Enables automated releases via GitHub Actions for the `readme-ai` repository.     |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml)   | Enables automated release drafting using GitHub Actions for readme-ai repository. |

</details>

<details closed><summary>readmeai</summary>

| File                                                                                    | Summary                                                                                                                                         |
| ---                                                                                     | ---                                                                                                                                             |
| [app.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/app.py)               | Generates README files using an AI model. Handles data extraction, template customization, and README generation within a repository structure. |
| [exceptions.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/exceptions.py) | Custom exceptions for the readme-ai app handle errors in Git operations, file system tasks, readme generation, and unsupported services.        |

</details>

<details closed><summary>readmeai.settings</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                               |
| ---                                                                                                              | ---                                                                                                                                                                                                                                   |
| [ignore_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/ignore_files.toml)         | Manages ignored files and directories using specific patterns and rules.                                                                                                                                                              |
| [language_names.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_names.toml)     | Defines programming languages by file extensions for the README AI project's codebase.                                                                                                                                                |
| [config.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/config.toml)                     | The code in `readmeai/settings/config.toml` defines resources, API settings, and markdown templates for the `readme-ai` repository. It configures files, Git repo, a language model API, and markdown elements for badges and tables. |
| [dependency_files.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/dependency_files.toml) | Manages dependency file names across various programming languages.                                                                                                                                                                   |
| [language_setup.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/settings/language_setup.toml)     | Configures language-specific setup and run instructions for various programming languages in the repository.                                                                                                                          |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                        | Summary                                                                                                |
| ---                                                                                         | ---                                                                                                    |
| [registry.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/registry.py) | Registry.py` provides a factory for various file parsers used in the project's architecture.           |
| [docker.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/docker.py)     | Parses Docker & Docker Compose files to extract dependency/service names for the ReadmeAI project.     |
| [npm.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/npm.py)           | Parses dependencies from package.json and yarn.lock files in readme-ai repository.                     |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cpp.py)           | Handles C/C++ project dependency parsing in `readme-ai` repository's architecture.                     |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/gradle.py)     | Contribute parsers for extracting package names from Gradle files.                                     |
| [swift.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/swift.py)       | Extracts package names from Swift Project files.                                                       |
| [python.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/python.py)     | Extract package names for various file formats like requirements.txt, TOML, and YAML.                  |
| [go.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/go.py)             | Parse package dependencies from go.mod files in repository's structure. Aids in analyzing Go projects. |
| [maven.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/maven.py)       | MavenParser extracts Java package names from pom.xml files in the README AI project.                   |
| [rust.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/rust.py)         | Extract Rust package names from cargo.toml using toml parser.                                          |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                         | Summary                                                                                                                                                                              |
| ---                                                                                          | ---                                                                                                                                                                                  |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py) | Generates metadata for repository files and extracts dependencies. Processes files to create FileContext instances, mapping languages, and token counts.                             |
| [logger.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/logger.py)         | The `logger.py` file offers a customized logging solution with emoji-based log levels for the `readme-ai` project.                                                                   |
| [model.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/model.py)           | Abstract base class for handling LLM API implementations, facilitating HTTP client configuration, response handling, and batch request processing for generating text using LLM API. |
| [parser.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/parser.py)         | Parses content into dependencies, logs errors, and handles exceptions.                                                                                                               |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py)           | The `utils.py` file provides utility functions for processing text responses from the LLM engine and checking file ignore criteria.                                                  |
| [file_io.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/file_io.py)       | File I/O factory class for reading/writing files based on their extensions.                                                                                                          |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                           | Summary                                                                                                  |
| ---                                                                                            | ---                                                                                                      |
| [enums.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/enums.py)           | Git services, badge icons, header images, LLM API key, and secret keys.                                  |
| [validators.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/validators.py) | Validates Git repository URL or path.-Retrieves repository name.-Determines git service host and domain. |
| [settings.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py)     | File paths, Git repo details, LLM API, Markdown templates, and prompts.                                  |

</details>

<details closed><summary>readmeai.markdown</summary>

| File                                                                                             | Summary                                                                                                                                                                                               |
| ---                                                                                              | ---                                                                                                                                                                                                   |
| [tree.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tree.py)             | Generates a directory tree structure for a code repository.                                                                                                                                           |
| [builder.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/builder.py)       | Generates various README sections based on project configuration, including badges, code summaries, directory structure, setup guide, and contributing information.                                   |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/utils.py)           | The `utils.py` file in the `readmeai/markdown` directory provides functions to manipulate markdown content, allowing the removal of default emojis and splitting markdown sections based on headings. |
| [badges.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/badges.py)         | Generates badges for the README using icons from shields.io and skill-icons.                                                                                                                          |
| [tables.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/tables.py)         | Creates markdown tables for LLM text responses in README by grouping code summaries by sub-directory.                                                                                                 |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/markdown/quickstart.py) | Generates Quickstart section content for the README, determining top language setup and requirements dynamically.                                                                                     |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                    | Summary                                                                                                                    |
| ---                                                                                     | ---                                                                                                                        |
| [options.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py)   | Defines command-line options for generating README files with badges, logos, and multilingual support.                     |
| [commands.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/commands.py) | Entry point CLI commands for readme-ai app, processing various inputs to generate optimized README files for repositories. |

</details>

<details closed><summary>readmeai.llms</summary>

| File                                                                                     | Summary                                                                                                                                                       |
| ---                                                                                      | ---                                                                                                                                                           |
| [registry.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/registry.py) | The `registry.py` file in the `readmeai/llms` directory selects the proper LLM implementation based on configuration.                                         |
| [offline.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/offline.py)   | The `OfflineModeHandler` in `llms/offline.py` enables offline mode when no LLM API service is specified, providing default placeholders for output.           |
| [vertex.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/vertex.py)     | Implements Vertex AI Generative Models API for text generation. Handles responses, retries on errors, and formats output.                                     |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/tokens.py)     | The `tokens.py` file in `readme-ai` calculates, truncates, and updates token counts for text prompts in the CLI app.                                          |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/prompts.py)   | Manages various prompt contexts and templates for the LLM API calls within the project structure.                                                             |
| [openai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/llms/openai.py)     | This code file implements an OpenAI API handler for generating text responses. It handles responses, truncates prompts if necessary, and logs generated text. |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                                 | Summary                                                                                                                                      |
| ---                                                                                                  | ---                                                                                                                                          |
| [git_metadata.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_metadata.py) | Fetches GitHub repository metadata for integration into the project, offering detailed information on the repository and its statistics.     |
| [git_utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git_utils.py)       | The `git_utils.py` file handles cloning repositories and fetching Git API URLs, supporting the core functionality of the `readmeai` project. |

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
