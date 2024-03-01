<p align="left">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100" alt="project-logo">
</p>
<p align="left">
    <h1 align="left">README-AI</h1>
</p>
<p align="left">
    <em>Unlock README Potential with AI</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&logo=opensourceinitiative&logoColor=white&color=blue" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=blue" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=blue" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=blue" alt="repo-language-count">
<p>
<p align="left">
		<em>Developed with the software and tools below.</em>
</p>
<p align="left">
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

Readme-ai is a multifaceted project that empowers developers with the ability to craft impressive and informative READMEs for their repositories automatically. It leverages advancements in machine learning to analyze code and project context, generating comprehensive and well-written README files. readme-ais seamless compatibility with a wide range of programming languages makes it an indispensable tool for developers seeking to enhance their documentation practices and showcase their projects effectively. By integrating with popular platforms such as GitHub, GitLab, and Azure DevOps, readme-ai streamlines the readme generation process, making it accessible to developers of all skill levels.

---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | *Deployed as a Docker image, combining Git, Python, and the readmeai package.* |
| 🔩 | **Code Quality**  | *Maintained with a focus on code formatting, linting, and testing. Unit tests cover core functionalities.* |
| 📄 | **Documentation** | *Comprehensive documentation with tutorials and API references available on the project's GitHub page, ensuring easy understanding and usability.* |
| 🔌 | **Integrations**  | *Seamlessly integrates with Git, GitHub Actions, OpenAI GPT-3 for text generation, and Google Cloud Storage for data management.* |
| 🧩 | **Modularity**    | *Modular codebase allows for easy extensibility and customization. Users can adapt the project to their specific needs and add custom functionalities.* |
| 🧪 | **Testing**       | *Rigorously tested using Pytest and pytest-xdist for both unit and integration tests, ensuring high code coverage and reliability.* |
| ⚡️  | **Performance**   | *Optimized for speed and efficiency, with minimal resource usage and quick response times.* |
| 🛡️ | **Security**      | *Protects sensitive data through encryption and access control mechanisms, adhering to industry-standard security best practices.* |
| 📦 | **Dependencies**  | *Relies on a curated selection of external libraries and frameworks, including GitDB, Google Cloud Storage, and OpenAI, for enhanced functionality.* |

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

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                              | ---                                                                                                                                                                                                                                                                                                                                              |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/master/Dockerfile)         | This Dockerfile creates a container image with the necessary dependencies and environment to run the readmeai command-line interface (CLI). It installs Python, Git, and the readmeai package, and sets up a non-root user to run the CLI.                                                                                                       |
| [Makefile](https://github.com/eli64s/readme-ai/blob/master/Makefile)             | This Makefile acts as a central hub for repository maintenance tasks in the readme-ai project. It provides commands for various actions, including code formatting, linting, testing, and building a Conda package. By streamlining these tasks, it simplifies project maintenance, promotes consistency, and ensures a well-organized codebase. |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/master/pyproject.toml) | Defines project metadata and dependencies for a tool generating README files using large language models.                                                                                                                                                                                                                                        |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/master/noxfile.py)         | This file, `noxfile.py`, in the `readme-ai` repository, automates testing using nox and pytest. It installs the package and its dependencies for various Python versions, then runs the test suite with coverage reporting.                                                                                                                      |

</details>

<details closed><summary>setup</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                        |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                            |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh)                 | This setup script initializes a conda environment for the README-AI project. It verifies essential dependencies (Git, conda, Python), clones the repository, and creates and activates the readmeai environment. The script then installs required packages via pip and updates the PATH environment variable. |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt) | This file manages Python dependencies for the project, ensuring compatibility with specific Python versions and operating systems. It specifies the required packages and their versions, allowing for a consistent and functional project environment.                                                        |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml) | This file defines the environment configuration for the Readme AI application. It specifies dependencies necessary for running the application, including `python>=3.9`, `pip`, and packages listed in `requirements.txt`.                                                                                     |

</details>

<details closed><summary>scripts</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                                                                                  |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh) | This code automates the generation of ReadMe files for multiple repositories using various configurations. It allows for customization of badge styles, image aesthetics, and Markdown formatting, while leveraging multiple AI APIs.                                                                                                |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh)           | Deploys the `readmeai` package to PyPI.**Critical Features:**-Cleans the build environment.-Builds the package.-Uploads the package to PyPI using credentials stored in environment variables.                                                                                                                                       |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh)         | This script, within the readme-ai repository, provides a comprehensive cleaning mechanism for various artifacts generated during development processes. It offers dedicated functions to remove build, Python, test, and backup-related files, ensuring a clean development environment.                                             |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh)       | The `scripts/docker.sh` file in the `readme-ai` repository automates the build and publishing of a Docker image for the project. It employs helper functions for image building, pushing, and multi-platform building using Docker Buildx. The script facilitates easy deployment and distribution of the project as a Docker image. |

</details>

<details closed><summary>.github</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                 |
| ---                                                                                                | ---                                                                                                                                                                                                                                                     |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml) | The `.github/release-drafter.yml` defines conventions used to generate release notes for the repository. It categorizes changes into types (e.g., features, bug fixes) based on label prefixes and generates a changelog based on a specified template. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                           |
| ---                                                                                                            | ---                                                                                                                                                                                                                                               |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml)                 | Enhances the parent repositorys software testing strategy by automating code coverage analysis. Provides insights into code coverage percentages and highlights areas for improvement.                                                            |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml) | Automates the release pipeline for the readme-ai repository using GitHub Actions. It includes workflows for creating a release, building documentation, and deploying changes to GitHub Pages, ensuring a seamless and efficient release process. |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml)   | Automates the drafting of GitHub releases by leveraging a template and pre-populated information, ensuring consistent and informative release notes.                                                                                              |

</details>

<details closed><summary>readmeai</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                 |
| [readmeai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/readmeai.py)     | This code orchestrates the generation of a README file based on user inputs and configuration. It interacts with a language model to generate summaries, overviews, and slogans that enhance the READMEs content. The code reads from a user-specified repository, processes dependencies, and incorporates user-provided customization options to craft a tailored README.         |
| [exceptions.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/exceptions.py) | This Python code defines a set of custom exception classes for the Readme-AI application. It encompasses exceptions for issues encountered during CLI operations, Git cloning and validation, file system operations (read and write errors), readme generation, and unsupported LLM services. These exceptions are used to handle errors and provide meaningful messages to users. |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                      | Summary                                                                                                                                                                                                      |
| ---                                                                                       | ---                                                                                                                                                                                                          |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/factory.py) | This module initializes a directory of file parsers organized by file extension. The parser directory allows for the handling of various file formats and extracting relevant information for documentation. |

</details>

<details closed><summary>readmeai.parsers.configuration</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                        |
| [ansible.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/ansible.py)       | The `ansible.py` file parses Ansible configuration files, including `playbook.yml` and `ansible/site.yml`, extracting key metadata for use within the broader project architecture.                                                                                                                                                                                        |
| [properties.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/properties.py) | Parse.properties configuration files to extract key names.**Critical Features-Extracts JDBC connection strings.-Identifies other package names from key-value pairs.                                                                                                                                                                                                       |
| [apache.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/apache.py)         | The `apache.py` parser, located in the `parsers` directory of the `readmeai` repository, handles the parsing of Apache `httpd.conf` configuration files. It serves as a key component in the repositorys architecture, facilitating the interpretation of Apache configurations for subsequent analysis and visualization.                                                 |
| [docker.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/docker.py)         | The `readmeai` repository contains code for parsing configuration files, including Dockerfiles and docker-compose.yaml files. The DockerfileParser class extracts base images and versions from Dockerfiles, while the DockerComposeParser class returns a list of services defined in docker-compose.yaml. These parsers are part of the readmeai core parsing framework. |
| [nginx.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/nginx.py)           | The Nginx parser in `readmeai/parsers/configuration/nginx.py` extracts configuration data from Nginx configuration files (nginx.conf). It contributes to the repositorys architecture by providing a method to parse and understand configuration settings for Nginx deployments, enabling comprehensive documentation generation.                                         |

</details>

<details closed><summary>readmeai.parsers.language</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                        |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/cpp.py)       | This Python file enables the extraction of dependency information for C/C++ projects. It offers three parsers to parse various file formats, like CMakeLists.txt, configure.ac, and Makefile.am, to detect dependencies, libraries, and packages. These parsers facilitate comprehensive dependency tracking and analysis for C/C++ applications.          |
| [swift.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/swift.py)   | Section.                                                                                                                                                                                                                                                                                                                                                   |
| [python.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/python.py) | Parses `Requirements.txt`, `pyproject.toml`, `environment.yml` to extract package names, excluding version specifiers. Supports major packaging systems like Pipenv and Poetry.                                                                                                                                                                                   |
| [go.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/go.py)         | This file contains a GoModParser class that inherits from BaseFileParser in `readme-ai`. Its designed to parse `requirements.txt` files and extract Python package names from them. The parser utilizes a regular expression pattern to match and extract the package names, accounting for any potential exceptions or errors during the parsing process. |
| [rust.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/rust.py)     | Parses Rust cargo.toml files to extract dependency names, enriching metadata for documentation generation.**Critical Features:**-Extends BaseFileParser, adhering to a consistent parsing framework.-Handles parsing errors gracefully, logging them for further analysis.                                                                                 |

</details>

<details closed><summary>readmeai.parsers.cicd</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                               |
| [bitbucket.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/bitbucket.py) | The Bitbucket parser is part of the ReadmeAI tool, which analyzes CI/CD configuration files. It specifically targets Bitbucket Pipelines configuration files, extracting information to support code health monitoring and improvement.                                                                                                                                                           |
| [travis.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/travis.py)       | This parser parses `.travis.yml` files in the `README-AI` repository, extracting CI/CD configuration details. It aids in providing insights into the repositorys CI/CD pipeline.                                                                                                                                                                                                                  |
| [gitlab.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/gitlab.py)       | In the context of the readme-ai codebase, the gitlab.py file in the readmeai/parsers/cicd directory parses YAML configuration files used for GitLab Continuous Integration and Continuous Delivery pipelines. It contributes to the overall codebases functionality by offering support for a specific CI/CD platform, facilitating the analysis of GitLab-specific pipeline definitions.         |
| [jenkins.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/jenkins.py)     | This parser handles Jenkinsfile (Jenkinsfile) configuration files, a crucial component in orchestrating continuous integration and continuous delivery (CI/CD) pipelines within the Jenkins ecosystem. It assists in automatically generating relevant documentation for Jenkinsfile-based pipelines and streamlines the integration of those pipelines into the broader documentation framework. |
| [github.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/github.py)       | Parses GitHub Actions configuration files (.github/workflows/).**Critical Features:**-Extracts workflow names, triggers, and jobs.-Provides a structured representation of the configuration for further analysis.                                                                                                                                                                                |
| [circleci.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/circleci.py)   | The `circleci.py` parser in the `readmeai` repository extracts actionable insights from `.circleci/config.yml` configuration files. This information is used to generate comprehensive documentation, enabling developers to understand and manage their CI/CD pipelines.                                                                                                                         |

</details>

<details closed><summary>readmeai.parsers.orchestration</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                  |
| [kubernetes.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/orchestration/kubernetes.py) | The `kubernetes.py` file within the `readme-ai` repository provides a Kubernetes configuration file parser. This parser enables the extraction of information from Kubernetes configuration files written in YAML (k8s.yml) format. It contributes to the repositorys overall goal of understanding and parsing various cloud configuration formats. |

</details>

<details closed><summary>readmeai.parsers.infrastructure</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                               |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                   |
| [terraform.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/infrastructure/terraform.py)           | Parses Terraform Configuration:** Analyzes `main.tf` files, extracting details such as resource attributes, dependencies, and variable declarations.-**Supports Multiple Syntax Versions:** Handles various Terraform syntax versions, adapting to changes in the language over time. |
| [cloudformation.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/infrastructure/cloudformation.py) | The `cloudformation.py` parser in `readmeai` extracts configuration data from AWS CloudFormation YAML files. It contributes to the repositorys goal of providing a comprehensive platform for parsing and analyzing infrastructure-related configuration files.                       |

</details>

<details closed><summary>readmeai.parsers.package</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [composer.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/composer.py) | The `composer.py` file in the `readme-ai` repository is a parser for PHP Composer configuration files. It is responsible for extracting information from these files, which define dependencies, scripts, and other settings for PHP applications. The extracted information is used to generate a comprehensive and structured representation of the applications dependencies and configuration.                                          |
| [npm.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/npm.py)           | This file contains parsers for `package.json` and `yarn.lock` files. It extracts dependencies from JSON-formatted `package.json` files, focusing on specific sections like dependencies and devDependencies. For `yarn.lock` files, it uses regular expressions to identify package names. These parsers inherit from a base parser class for error handling.                                                                               |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/gradle.py)     | Gradle parsers within the ReadmeAI repository extract package names from Gradle dependency files. They support both build.gradle and build.gradle.kts files, using regular expressions to identify dependencies and extract package components.                                                                                                                                                                                             |
| [nuget.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/nuget.py)       | The `nuget.py` file in the `readmeai` repository parses NuGet.Config configuration files (.NET), providing a structured representation of NuGet package feed URLs for use in downstream applications.                                                                                                                                                                                                                                       |
| [yarn.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/yarn.py)         | Parses `yarn.lock` files to extract package names.**Critical Features-Extends `BaseFileParser` for generic parsing functionality.-Uses regex to extract package names from the `yarn.lock` file.-Handles parsing errors and provides error messages.                                                                                                                                                                                        |
| [pip.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/pip.py)           | In the context of its parent repository, `pip.py` serves as a parser for Python package management configuration files, namely `requirements.txt` and `Pipfile`. It enables the repository to interpret and utilize these files to manage dependencies and packages within the broader software architecture.                                                                                                                               |
| [maven.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/maven.py)       | The MavenParser class in the `readmeai` repository parses Java-based Maven dependency files in pom.xml format. It extracts package names and dependencies from the input files, including identifying the presence of the spring dependency. The extracted dependencies are then returned as a set of unique names. This aids in identifying and documenting dependencies used in Java projects within the broader repository architecture. |
| [gem.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/gem.py)           | The `gem.py` file in the `readmeai` repository parses `Gemfile.lock` configuration files in Ruby. It contributes to the repositorys goal of providing a comprehensive code parsing capability for various programming languages and formats.                                                                                                                                                                                                |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [models.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/models.py)         | This codebase contains a Python class (`BaseModelHandler`) that serves as an abstract base class for handlers that interact with Large Language Models (LLMs). Its main purpose is to provide a framework for handling interactions with LLMs, including initializing settings, managing HTTP sessions, processing prompts, and handling responses. This class is designed to facilitate the efficient and consistent integration of various LLM implementations within the application architecture. |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py) | The `preprocess.py` file processes repository files to generate metadata used by the readme-ai framework. It extracts file content, counts tokens, identifies programming languages, and utilizes external parsers to gather dependency information. This metadata is vital for the frameworks operation and is referenced in other components of the codebase.                                                                                                                                       |
| [parsers.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/parsers.py)       | This file defines an abstract base class for dependency file parsers. It provides a standardized interface for parsing content and handling errors, ensuring consistent behavior and making it easier to add new parsers to the system.                                                                                                                                                                                                                                                               |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py)           | Utility functions for the readme-ai CLI application.**Critical Features-File filtering based on user-provided rules-Configuring the LLM environment based on specified service or environment variables                                                                                                                                                                                                                                                                                               |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                      |
| [enums.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/enums.py)           | Git service (e.g., GitHub, GitLab)-Badge icons (e.g., flat, plastic)-Header images (e.g., custom, default)-LLM API key (e.g., OpenAI, VertexAI)-LLM environment variables (e.g., OPENAI_API_KEY)                                                                                                                                                                         |
| [validators.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/validators.py) | This code validates user-provided Git repository settings. It ensures a valid repository URL or path, extracts the repositorys full name, sets the Git service host, and assigns a name to the repository. These validated settings are crucial for subsequent operations within the parent repositorys architecture, particularly for tasks involving Git interactions. |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/utils.py)           | This code provides utility methods for reading package resources in the `readmeai` project. It leverages `importlib.resources` for accessing TOML and JSON files. If it encounters any errors, it uses `pkg_resources` as a fallback. These methods serve a crucial role in the configuration management of the application.                                             |
| [settings.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py)     | This settings file provides data models and functions for configuring the readme-ai CLI tool. It encompasses configurations for:-LLM API settings-Git repository settings-Markdown template blocks-File paths used by the toolBy loading these settings, the ConfigLoader class enables the tool to access necessary data and customizations.                            |

</details>

<details closed><summary>readmeai.config.settings</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [prompts.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/prompts.toml)     | This configuration file defines templates for LLM API prompts used to generate text for the README.md file. Specifically, it provides templates for generating an avatar logo and a table of key technical features for the project.                                                                                                                                                                                                                    |
| [parsers.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/parsers.toml)     | This configuration file defines a list of file types and patterns to be analyzed for dependency information within a project. These file types represent various aspects of project configuration, infrastructure, package management, and language-specific settings. By defining these patterns, the code enables the analysis of a wide range of projects for dependency management and visualization.                                               |
| [blacklist.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/blacklist.toml) | Within the repositorys architecture, the `blacklist.toml` file plays a crucial role in preprocessing. It defines directories, file extensions, and specific files to exclude. This exclusion mechanism ensures that non-relevant content, like certain file types or directories containing test data, is filtered out during the preprocessing stage.                                                                                                  |
| [languages.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/languages.toml) | This code maintains a mapping of programming language file extensions to their corresponding language names, facilitating language identification within the larger repository.                                                                                                                                                                                                                                                                         |
| [config.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/config.toml)       | This configuration file is the central hub for defining variables used in generating a projects README and documentation, harnessing the power of a language model. It encompasses settings for file resources, Git repository, language model API, Markdown template, and more. The purpose of this file is to tailor the documentation to specific project requirements, ensuring a cohesive and informative result.                                  |
| [markdown.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/markdown.toml)   | This `markdown.toml` file defines templates for constructing a README.md file using Markdown. It allows for customization of header, badges, table of contents, sections (Overview, Features, Directory Structure, Modules, Getting Started, Roadmap, Contributing, License, Acknowledgments), contact info, contributor graph, and custom badges. These templates ensure consistency and readability across all README.md files within the repository. |
| [commands.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/commands.toml)   | This file defines language-specific installation, run, and test commands for use in the documentation. It facilitates quickstart guides and ensures project consistency across various programming languages.                                                                                                                                                                                                                                           |

</details>

<details closed><summary>readmeai.utils</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [formatter.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/formatter.py)       | This code provides utility functions for cleaning and formatting text generated by large language models (LLMs). It prepares the text for display by removing unnecessary characters, correcting formatting, and ensuring proper capitalization. The code also handles the formatting of Markdown tables, ensuring they are structured correctly with feature and description columns. The formatted response is returned, ready for presentation. |
| [file_handler.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/file_handler.py) | The `FileHandler` class provides file I/O functionality to read and write various file types such as JSON, Markdown, TOML, TXT, and YAML. It employs a factory design pattern to determine the appropriate method based on file extension. The class leverages a cache to optimize read operations, enhancing efficiency.                                                                                                                          |
| [logger.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/logger.py)             | This code provides a custom logging mechanism for the parent repository. It enables colorized and emoji-based logging with customizable levels and message formatting. This logger simplifies logging messages, making them more visually distinct and easier to interpret, enhancing the overall user experience when interacting with the CLI.                                                                                                   |

</details>

<details closed><summary>readmeai.models</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                    |
| [offline.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/offline.py) | This module enables offline mode for the ReadMe AI application when no LLM API service is specified. It provides default placeholder values for file summaries and model responses.                                                                                                                                                                                                                    |
| [vertex.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/vertex.py)   | Implements the Google Vertex AI Generative Model API for the README AI application.**Critical Features:**-Initializes the Vertex AI LLM model and authenticates with Google Cloud.-Handles API responses and formats generated text.-Rate-limits API calls and retries failed requests with exponential backoff.-Provides async context manager for HTTP client management.                            |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/tokens.py)   | This file provides tokenization utilities for the CLI application. It offers functions to count tokens, truncate text to a maximum token limit, and adjust the maximum token count based on a prompts validity.                                                                                                                                                                                        |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/factory.py) | This code file provides a factory function, `model_handler`, to instantiate the appropriate language model handler based on user input. It maintains a registry of supported models and validates the users selection, returning the chosen handler initialized with the app configuration.                                                                                                            |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/prompts.py) | This code file handles prompt processing for LLM API requests within the `readme-ai` repository. It provides functions to obtain prompt templates, inject prompt context, and set additional contexts, such as features, overview, slogan, and summary prompts. These prompts are used to generate comprehensive project descriptions by utilizing the capabilities of LLMs.                           |
| [openai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/openai.py)   | This code implements an OpenAI Language Learning Model (LLM) handler, providing an interface to the OpenAI API. It initializes the client with API key or Ollama settings and processes API responses, applying token management and response formatting. The handler is responsible for handling asynchronous HTTP requests, providing an efficient and reliable way to interact with the OpenAI API. |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                |
| [options.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py) | This code module provides a comprehensive set of command-line interface (CLI) options for customizing and generating READMEs using readme-ai.**Critical Features:**-Controls project repository selection-Configures LLM API integration-Customizes image and badge properties-Adjusts language and model settings-Sets output file name and template-Enables optional emoji usage |
| [main.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/main.py)       | The main.py" file serves as the entry point for the readme-ai CLI application. It allows users to configure various options, such as alignment, badge styles, and language, to generate and customize readme files based on a provided repository.                                                                                                                                 |

</details>

<details closed><summary>readmeai.generators</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                     |
| [tree.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tree.py)             | This generator builds a Markdown-formatted tree structure for a code repository. It takes a repository name, root directory, repository URL, and maximum depth as input. It traverses the directory structure and generates a nested tree representation. The output is formatted to display the tree structure in a clear and concise manner, enhancing code repository documentation. |
| [builder.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/builder.py)       | The builder.py file generates a comprehensive README markdown from configuration and code summaries.**Features:**-Headers with badges and slogans-Code summaries with tables and examples-Directory tree structure-Quickstart guide-Contributing guidelines                                                                                                                             |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/utils.py)           | Removing default emojis from Markdown content.-Splitting Markdown documents into sections based on level 2 headings.-Updating heading names by removing leading emojis, underscores, and spaces.                                                                                                                                                                                        |
| [badges.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/badges.py)         | Metadata badges using `shields.io` and skill icons from `skill-icons`. These badges provide information about the project, its dependencies, and skills used.                                                                                                                                                                                                                           |
| [tables.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tables.py)         | This code in `readmeai/generators/tables.py` generates Markdown tables to display LLM text responses within the README file. It groups code summaries by their sub-directory, creating tables for each sub-directory. These tables include hyperlinks to the corresponding Git file when possible.                                                                                      |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/quickstart.py) | The `quickstart.py` script generates the Quick Start section of a project's README file. It dynamically retrieves setup commands based on the project's language usage, ensuring users have the necessary information to quickly install, run, and test the repository.                                                                                                                 |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                              |
| [git.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git.py)           | The `git.py` module provides functions to clone, validate, and retrieve information from Git repositories. Key tasks:-Clone a repository to a temporary directory.-Remove hidden files and directories to improve readability.-Determine the Git service (e.g., GitHub, GitLab) and retrieve the API URL.-Find the URL of a file within a remote repository.-Validate file permissions to ensure correct access. |
| [metadata.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/metadata.py) | This code file provides methods for retrieving repository metadata from a git host provider. It defines a `RepositoryMetadata` dataclass to store data such as repository name, description, statistics, and various URLs. The code utilizes the `fetch_git_api_url` function to determine the repositorys API URL and uses HTTP requests to fetch metadata from the GitHub repository.                          |

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

> Run readme-ai using the command below:
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
