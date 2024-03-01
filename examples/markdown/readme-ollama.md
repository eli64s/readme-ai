<p align="left">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100" alt="project-logo">
</p>
<p align="left">
    <h1 align="left">README-AI</h1>
</p>
<p align="left">
    <em>Generate Proactive Readmes with readme-ai!</em>
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

 The readme-ai project is an open-source tool designed to automate the creation of high-quality README files for GitHub repositories. The core functionalities of this project are housed within the `readmeai` directory, which includes scripts and utilities for extracting and summarizing key information from code and documentation files.

---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | Python based project with a command line interface (CLI) and integrations using Google Cloud Platform (GCP), OpenAI, and various other external libraries. |
| 🔩 | **Code Quality**  | Employs code formatting tools like `black` for consistency, static analysis tools such as `pylint`, `ruff`, and type hints to enhance the quality. |
| 📄 | **Documentation** | Includes extensive documentation using Markdown format for README.md, project setup instructions, and API specifications (OpenAPI/gRPC) via Mkdocs. |
| 🔌 | **Integrations**  | Integrated with GCP services such as BigQuery, Cloud Resource Manager, AI Platform, and others through Google-Cloud libraries. Utilizes OpenAI for text generation, AioHTTP for web requests. |
| 🧩 | **Modularity**    | Organized into various subdirectories such as 'cli', 'api', and 'docs'. Adheres to the Single Responsibility Principle, separating functional components. |
| 🧪 | **Testing**       | Employs pytest for testing; tests include unit tests, integration tests, end-to-end tests, and regression tests with the help of Google's Tenacity library for retries and fixtures. |
| ⚡️  | **Performance**   | Not explicitly stated but can be assumed to optimize performance in several ways such as parallel testing using `pytest-xdist`, handling larger datasets through efficient algorithms (e.g., Numpy), etc. |
| 🛡️ | **Security**      | Employs secure communication between clients and servers using TLS, Google-Cloud-IAM, and GitHub actions for access control. |
| 📦 | **Dependencies**  | Consists of a mix of runtime and development dependencies defined by `requirements.txt`, `pyproject.toml`, and other files. Includes Google Cloud libraries, text manipulation libraries like `shapely`, and others. |

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

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                              | ---                                                                                                                                                                                                                                                                                                                                           |
| [Dockerfile](https://github.com/eli64s/readme-ai/blob/master/Dockerfile)         | Dockerfile in the repository sets up a production environment for the readme-ai project using Python 3.10. It installs required dependencies, creates a non-root user, and configures the PATH for running the `readmeai` Command Line Interface (CLI).                                                                                       |
| [Makefile](https://github.com/eli64s/readme-ai/blob/master/Makefile)             | The Makefile in this repository serves as a build automation tool. It defines targets for formatting, linting, testing, and package management. Commands like `format`, `lint`, and `nox` execute respective tasks using specified tools. Additionally, it has targets for cleaning files and displaying Git log information.                 |
| [pyproject.toml](https://github.com/eli64s/readme-ai/blob/master/pyproject.toml) | The `pyproject.toml` file configures the Python projects build system using Poetry, defining package metadata and dependencies for readmeai". This automated README generator utilizes large language model APIs. Key features include POETITY as build-backend, dependency management, and support for various tools like Pytest and Mkdocs. |
| [noxfile.py](https://github.com/eli64s/readme-ai/blob/master/noxfile.py)         | The noxfile.py in this repository configures automated testing with Nox and pytest across various Python versions, installing required dependencies for tests run.                                                                                                                                                                            |

</details>

<details closed><summary>setup</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                         |
| [setup.sh](https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh)                 | The setup.sh script is part of the README-AI projects setup folder. It ensures prerequisites, such as Git, tree command, Conda, and Python (version 3.8+), are installed before creating and activating a virtual environment named readmeai". This environment will be used to manage project dependencies listed in requirements.txt. The script concludes by installing the required packages using pip. |
| [requirements.txt](https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt) | Requires Python >=3.9, <4.0, and several third-party packages such as grpcio, googleapis-common-protos, protobuf, idna, packaging, proto-plus, pydantic, setuptools, shapely, six, smmap, sniffio, tenacity, tiktoken, toml, and tqdm. Avoids words like This file or This code.                                                                                                                            |
| [environment.yaml](https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml) | The `setup/environment.yaml` configures Conda environment for readme-ai project. It specifies the channel sources, python version requirement, and dependencies including pip and pip installments from requirements file.                                                                                                                                                                                  |

</details>

<details closed><summary>scripts</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [run_batch.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh) | Script to generate README files using readmeai package for multiple repositories with random badge styles, image styles, and alignments. Configuration files and dependencies are organized under the repository structure.                                                                                                                                                                                                            |
| [pypi.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh)           | This Bash script automates the process of building and uploading a Python package to PyPI (Python Package Index) using environment variables and helper functions. It ensures cleanliness by first running scripts/clean.sh and then builds the project before deploying the distribution files with `twine`.                                                                                                                          |
| [clean.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh)         | The scripts/clean.sh file is a Bash script responsible for cleaning various artifacts from the project directory, ensuring a fresh build environment. It comprises functions to remove build artifacts (.pyc, *.egg), Python cached files, test and coverage results, backup files, and cache directories. Users can invoke specific cleanup tasks via commands such as clean-build, clean-test, or call the entire script with clean. |
| [docker.sh](https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh)       | The scripts/docker.sh script automates Docker image build, publish, and multi-platform building using Buildx. It uses the configuration IMAGE=readme-ai and VERSION=latest, creating and pushing the corresponding Docker images.                                                                                                                                                                                                      |

</details>

<details closed><summary>.github</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml) | In the given GitHub repository, the `.github/release-drafter.yml` file serves as a configuration for automated release note generation using the release drafter from keepachangelog.com. It defines template structures for naming tags and categorizing changes based on labels, and enables various change types including features, bug fixes, chores, deprecated items, removals, security issues, and documentation updates. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                    |
| [coverage.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml)                 | The.github/workflows/coverage.yml file in this repository configures continuous integration for running tests and measuring code coverage using GitHub Actions. This promotes maintainability, reliability, and maintaining a high coding standard within the project.                                 |
| [release-pipeline.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml) | The `release-pipeline.yml` file in the GitHub actions folder configures a continuous integration and deployment workflow for the repository. It automates building, testing, and releasing new versions of the project to the main branch and other targets, ensuring software quality and efficiency. |
| [release-drafter.yml](https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml)   | The `release-drafter.yml` file in the repositorys.github directory configures automated workflows for releasing new project versions. It facilitates creation of tagged releases, generating change logs, and drafting release notes based on commit messages.                                         |

</details>

<details closed><summary>readmeai</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                     |
| [readmeai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/readmeai.py)     | The `readmeai.py` file orchestrates the generation process of README files by managing configuration settings, interacting with Git repositories, processing dependencies, and utilizing AI models for file summarization and feature extraction. This results in a dynamic, customizable, and informative README file. |
| [exceptions.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/exceptions.py) | Custom exceptions classes for readme-ai application are defined in this file. It includes base exception (ReadmeAiException), CLI error, Git clone/validation errors, file system errors, readme generation errors, and unsupported service errors to handle various exceptions within the application.                 |

</details>

<details closed><summary>readmeai.parsers</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                       |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                           |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/factory.py) | The readmeai/parsers/factory.py abstracts parsing of various project files by managing a registry of BaseFileParser subclasses. It assigns specific file extensions to their respective parser classes for efficient and flexible file analysis within the ReadMe AI project. |

</details>

<details closed><summary>readmeai.parsers.configuration</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                       |
| [ansible.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/ansible.py)       | In the readmeai repository, the ansible.py file, located in parsers/configuration/, serves to parse Ansible configuration files such as playbook.yml and ansible/site.yml. It contributes to the overall functionality of the project which focuses on analyzing various configuration files using diverse parsing techniques.                                            |
| [properties.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/properties.py) | In this repository, a PropertiesParser class is defined for handling.properties files within the readmeai project. This parser extracts JDBC connection strings using a specific regex and identifies other packages through another regex. These extracted items are then returned as a list.                                                                            |
| [apache.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/apache.py)         | The `apache.py` file, located under `readmeai/parsers/configuration/`, is a parser designed specifically for processing Apache (httpd.conf) configuration files within the larger project repository structure.                                                                                                                                                           |
| [docker.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/docker.py)         | In the readmeai repository, this file contains parsing logic for extracting information from Docker configuration files (Dockerfile and docker-compose.yaml). The DockerfileParser and DockerComposeParser classes identify dependencies in Dockerfiles and list services in docker-compose files, respectively. Both parsers inherit from the base BaseFileParser class. |
| [nginx.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/configuration/nginx.py)           | In the readmeai repository, this Python file (nginx.py) is part of the parsers/configuration folder. It serves to parse Nginx configuration files (nginx.conf). This contributes to the overall architecture by enabling interpretation and processing of crucial configuration data for effective management and integration with the broader system.                    |

</details>

<details closed><summary>readmeai.parsers.language</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                      |
| [cpp.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/cpp.py)       | This Python file, located in `readmeai/parsers/language/cpp.py`, provides dependency parsing for C and C++ projects using various file types like CMakeLists.txt, configure.ac, and Makefile.am. It extracts dependencies, libraries, and software names from these files, enabling better documentation of project dependencies within the larger repository structure. |
| [swift.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/swift.py)   | Or.package(name:, as well as lines with "dependencies:. Extracted package names are then returned as a list.                                                                                                                                                                                                                                                             |
| [python.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/python.py) | Requirements.txt, TOML, and YAML. These parsers extract package names from each file format, excluding version specifiers, for further processing in the project. The base class BaseFileParser is inherited, ensuring a consistent parsing interface across file types.                                                                                                 |
| [go.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/go.py)         | In the readmeai repository, the file `go.py` under `parsers/language/` processes dependencies from Go.mod files. This parser, an extension of `BaseFileParser`, extracts package names by using regular expressions and returns them as a list.                                                                                                                          |
| [rust.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/language/rust.py)     | The rust.py file in the readmeai/parsers/language directory parses Rust's Cargo.toml dependency files using TOML library, extracting package names for further processing within the ReadMe.AI project architecture.                                                                                                                                                     |

</details>

<details closed><summary>readmeai.parsers.cicd</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                               |
| [bitbucket.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/bitbucket.py) | The `bitbucket.py` script in the `readmeai/parsers/cicd` folder is designed to parse Bitbucket Pipelines configuration files (bitbucket-pipelines.yml). This contributes to the overall architecture of the repository, enabling analysis and interpretation of continuous integration and delivery configurations within the system.                                                                             |
| [travis.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/travis.py)       | The travis.py file in readmeai/parsers/cicd directory is a parser designed for processing.travis.yml configuration files in the context of the CI/CD architecture within this repository. Its main purpose lies in extracting and analyzing relevant information from these files, enhancing the functionality and interoperability of various workflows managed by this project's continuous integration system. |
| [gitlab.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/gitlab.py)       | The readmeai/parsers/cicd/gitlab.py script parses GitLab's.gitlab-ci.yml configuration files within the project. It is a crucial component in the repository's CI/CD infrastructure, enabling seamless integration with GitLab's continuous delivery workflows.                                                                                                                                                   |
| [jenkins.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/jenkins.py)     | In the readmeai repository, the jenkins.py file under parsers/cicd processes Jenkinsfile configurations. It contributes to the pipeline by parsing and interpreting these specific configuration files within the Continuous Integration/Continuous Delivery (CI/CD) system context.                                                                                                                              |
| [github.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/github.py)       | The github.py file, located in the readmeai/parsers/cicd directory, is designed to parse GitHub Actions (.github/workflows/) configuration files within a repository. By extracting and processing this information, it supports the overall functionality of the readme-ai project, which aims to generate and enhance README files.                                                                             |
| [circleci.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cicd/circleci.py)   | In the readmeai repository, this Python script situated within /parsers/cicd/circleci.py processes.circleci/config.yml. It parses CircleCI configuration files, contributing to the continuous integration and delivery (CI/CD) workflow in this project architecture.                                                                                                                                            |

</details>

<details closed><summary>readmeai.parsers.orchestration</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                               |
| ---                                                                                                           | ---                                                                                                                                                                                                                   |
| [kubernetes.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/orchestration/kubernetes.py) | The kubernetes.py file in readmeai/parsers/orchestration processes Kubernetes configuration files, contributing to the readmeai project that analyses and generates documentation from various configuration formats. |

</details>

<details closed><summary>readmeai.parsers.infrastructure</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                |
| [terraform.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/infrastructure/terraform.py)           | In the readmeai repository, this Python script (terramform.py) is a parser for main.tf configuration files used with Terraform infrastructure management tool. It contributes to the automated processing of Terraform configurations within the project's CI/CD pipeline.                                                                                                         |
| [cloudformation.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/infrastructure/cloudformation.py) | In the given repository, the `readmeai/parsers/infrastructure/cloudformation.py` file is responsible for parsing AWS CloudFormation configuration files (`.yaml`) as part of the infrastructure parser component. This enhances the overall functionality of the project by enabling easier handling and understanding of CloudFormation templates within the parent architecture. |

</details>

<details closed><summary>readmeai.parsers.package</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [composer.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/composer.py) | The `readmeai/parsers/package/composer.py` script is a parser designed for processing PHP Composer (composer.json) configuration files within the given repository structure. This parsing capability enables automated analysis and interpretation of these configuration files as part of the larger projects infrastructure.                                                                                                                                                                                                                                                                                                                                                                       |
| [npm.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/npm.py)           | In this repository, there are two parsing files, one for npm.py and another for yarn.lock, located in the /readmeai/parsers/package/ folder. The npm.py file is designed to parse JSON dependency files using the json and re libraries. It extracts package names from dependencies, devDependencies, and peerDependencies sections of the JSON file. Meanwhile, the YarnLockParser class in yarn.lock processes the yarn.lock file using regular expressions to obtain the same information. Together, these parsing files enhance the functionality of this open-source project, enabling it to process multiple dependency file formats and extract necessary package names for further analysis. |
| [gradle.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/gradle.py)     | In the given open-source project repository, there are parsers for extracting package names from different types of dependency files. The file at readmeai/parsers/package/gradle.py is dedicated to parsing Gradle (.gradle and.gradle.kts) files. This parser utilizes regular expressions to identify dependencies' package names and extract them, expanding the set of supported configuration formats in the repository architecture.                                                                                                                                                                                                                                                           |
| [nuget.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/nuget.py)       | The `nuget.py` file in the `readmeai/parsers/package` directory is responsible for parsing NuGet configuration files within the.NET ecosystem. This contributes to the overall functionality of the repository by enabling effective handling and interpretation of.NET package management configurations.                                                                                                                                                                                                                                                                                                                                                                                            |
| [yarn.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/yarn.py)         | The readmeai/parsers/package/yarn.py file is part of the dependency parsing module within the Readme-AI project. Its primary role is to extract package names from Yarn lock files using regular expressions, expanding the repository's capability in handling diverse dependency formats.                                                                                                                                                                                                                                                                                                                                                                                                           |
| [pip.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/pip.py)           | In the given repository, the pip.py file, located under readmeai/parsers/package, is designed to parse Pip configuration files such as requirements.txt and Pipfile. This contributes to the overall functionality of the project by enabling processing of dependency declarations within these formats.                                                                                                                                                                                                                                                                                                                                                                                             |
| [maven.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/maven.py)       | The `MavenParser` file in the readmeai/parsers/package directory is a Python script designed to extract package names from Maven dependency files written in pom.xml format. It utilizes regular expressions and the BaseFileParser class to parse and identify dependencies within pom.xml content, returning a list of distinct package names as output. This functionality complements the architecture of the readmeai repository by enabling automatic extraction and management of Java project dependencies.                                                                                                                                                                                   |
| [gem.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/package/gem.py)           | The `gem.py` file in the `readmeai/parsers/package` directory is responsible for parsing Rubys Gemfile.lock configuration files. This contributes to the overall functionality of the repository by supporting the extraction and processing of configuration data across multiple package formats, thereby enhancing the readability and analysis capabilities offered by this open-source project.                                                                                                                                                                                                                                                                                                  |

</details>

<details closed><summary>readmeai.core</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [models.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/models.py)         | Pythonasync def generate_summary(self, file_context): "Generates a summary for a given context (file). Parameters----------file_context Context in the form of a dictionary containing the file path and its contents. Returns-------str: Summary text. " # Ensure file_context is a list if isinstance(file_context, (list, tuple)): file_path, file_content = file_context else: raise ValueError(Invalid'file_context format.") file_name = Path(file_path).stem.replace(_, ).capitalize() file_type = Path(file_path).suffix[1:].lower() # Define prompt using the provided context (file) and metadata (project name) prompt = self.prompts[prompts][file_summary].format(self.config.md.tree, file_name, file_type) tokens = update_max_tokens(self.tokens, prompt) summary, _ = await |
| [preprocess.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py) | Preprocessor function takes a ConfigLoader instance and temporary directory as inputs. It initializes RepositoryProcessor instance, generates FileContext objects from repository files, maps file extensions to programming languages, and retrieves dependencies between files. The returned data includes a list of dependencies, raw files, and their content, and the generated readme tree in Markdown format.                                                                                                                                                                                                                                                                                                                                                                         |
| [parsers.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/parsers.py)       | Abstract base class for parsing dependency files is defined in this Python file. The `BaseFileParser` class includes an abstract `parse()` method to parse content into a list of dependencies, logging error messages with the `log_error()` function upon parsing failures, and handling exceptions with the `handle_parsing_error()` function. This is part of the readme-ai projects core functionality.                                                                                                                                                                                                                                                                                                                                                                                 |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py)           | Utility methods script in readmeais core module for filtering files and setting LLM engine based on config or environment variables, ensuring appropriate usage of specified services in the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

</details>

<details closed><summary>readmeai.config</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [enums.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/enums.py)           | In the readme-ai repository, the config/enums.py file defines enums for Git service details, CLI options for badge icons and header images, model options for the LLM API key, and secret keys for environment variables. These enums facilitate customizing various aspects of the README file generation process.                                                                                                                                  |
| [validators.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/validators.py) | The `validators.py` file in `readmeai/config` defines a `GitValidator` class responsible for validating Git repository URLs or paths. This class includes methods for checking the format of provided repositories and extracting repository names based on popular Git services, such as GitHub, GitLab, and Bitbucket. Validation failure results in a raised `GitValidationError`.                                                                |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/utils.py)           | This utility module in `readmeai/config/utils.py` enables loading configuration files from package resources, supporting both TOML and JSON formats. It uses importlib and Pathlib to locate the files within the readmeai package based on a given file path and submodule. In case of issues with importlib, it also falls back to using pkg_resources. The primary goal is to facilitate configuration file handling within the readmeai project. |
| [settings.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py)     | This Python file, located in `readmeai/config/settings.py`, defines classes and settings for configuring the readme-ai CLI tool. The file includes settings for LLM API, Git repository, Markdown templates, and file paths used by the tool. Pydantic is utilized to validate and sanitize user input.                                                                                                                                              |

</details>

<details closed><summary>readmeai.config.settings</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [prompts.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/prompts.toml)     | This Toml configuration file, located at `readmeai/config/settings/prompts.toml`, defines templates for generating text for the `README.md` file using placeholders that will be replaced with actual project data. The `avatar` and `features` prompts define a template each for creating an avatar image and a Markdown table summarizing the project features, respectively. Both templates contain placeholders referring to project details which will be filled in during rendering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [parsers.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/parsers.toml)     | The provided TOML file in `readmeai/config/settings/parsers.toml` lists configuration files and dependencies to be parsed within the repository. It covers CI/CD, configuration, infrastructure, monitoring and logging, package managers, language/framework-specific, and others, ensuring comprehensive analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [blacklist.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/blacklist.toml) | In this configuration file, directories and file extensions are defined for exclusion during preprocessing within the open-source project. This ensures that non-essential files do not undergo processing, streamlining workflows while maintaining efficient resource utilization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [languages.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/languages.toml) | In the given repository, this configuration file, located at `readmeai/config/settings/languages.toml`, defines programming language extensions and their corresponding names for easy reference. The file contributes to the overall organization of the project by providing a clear mapping for various file types within the given ecosystem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [config.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/config.toml)       | Def __init__(self, project_path: str): self.project_path = project_path self.template = self._load_template() def generate(self, project_data: Dict[str, Any]): data = {k: v for k, v in project_data.items() if k!= repo_url} template = self.template.env.get_template(readme_template.md) return template.render(project=data) def _load_template(self): env = Environment(loader=FileSystemLoader(templates)) return envif __name__ == __main__: # Set project path and data as needed project_data = { name: My Project Name, host: https://github.com/{yourusername}, full_name: {repository}, repo_url: https://github.com/yourusername/{repository}.git } # Initialize the ReadmeAI instance and generate the template file readme = ReadmeAI(os.getcwd()) output_str = readme.generate(project_data).decode() # Replace existing readme                                                                                                                                                                                                                                                                                                     |
| [markdown.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/markdown.toml)   | Ill give you a Python-focused README template that includes an overview, features, directory structure, modules, quickstart guide, project roadmap, licensing information, and acknowledgments section. You can customize the contact info and contributor graph as well.Now let me elaborate on my response: I'll provide you with a `{project_name}`-focused README template that includes an overview (explaining what {project_name} does), features (listing its key benefits), directory structure (describing the project layout), modules (detailing {project_name}'s major components), quickstart guide (a step-by-step guide installing and using it), project roadmap (describing future developments), licensing information, and acknowledgments (crediting external resources). You can customize the contact info and contributor graph as well.=========================================================================================================In more detail: I'll give you a README template for a {project_name} Python project which includes:1. An overview, explaining what {project_name} does (maximum 60 tokens). |
| [commands.toml](https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/commands.toml)   | This `commands.toml` config file defines programming language-specific install, run, and test commands for a project. It facilitates easy setup and execution of projects written in various languages within the repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

</details>

<details closed><summary>readmeai.utils</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [formatter.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/formatter.py)       | This Python module, named formatter.py located in readmeai/utils, contains utility functions for cleaning and formatting text generated by Large Language Models (LLMs). The primary function, `clean_text`, formats text by removing specific patterns and rephrasing them, eliminating unwanted characters, and ensuring consistent capitalization at the beginning of a string. Another function, `fix_md_table_rows`, specifically formats a Markdown table with feature and description columns. The `format_md_table` function extracts and formats Markdown tables from text using regular expressions. The final function, `format_response`, processes LLM responses based on their type, either features, features\_synthesized, or general responses, applying the relevant formatting accordingly. |
| [file_handler.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/file_handler.py) | File utils/file\_handler.py in readmeai repository is a utility class that simplifies file I/O operations by handling reading and writing of JSON, Markdown, TOML, YAML, and text files using factory methods. It caches results for optimization, and includes error handling for common exceptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [logger.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/logger.py)             | Custom logger implementation in readmeai/utils/logger.py enhances the CLI with colored log output and custom emojis for different log levels, providing clearer and more engaging logging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

</details>

<details closed><summary>readmeai.models</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [offline.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/offline.py) | The OfflineHandler class in readmeai/models/offline.py facilitates offline mode by setting default placeholders when the Large Language Model (LLM) API service isn't specified. This enables the application to run without an external API call, improving overall system efficiency.                                                                                                                                                                                                                  |
| [vertex.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/vertex.py)   | The readmeai/models/vertex.py file implements a handler for generating text using Google Vertex AI's Large Language Model (LLM) API. This handler initializes the necessary authentication, sets up the required configurations, and defines methods to make API requests and handle responses. It includes error handling and retry mechanisms in case of connection issues. The file is part of a larger project, as indicated by the repository structure.                                            |
| [tokens.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/tokens.py)   | In the `readmeai/models/tokens.py` file, youll find tokenization utilities for the readme-ai CLI application. The script offers functions like count_tokens and truncate_tokens to manage text strings based on specific token encodings. Additionally, it provides an update_max_tokens function to adjust maximum token numbers according to given prompts.                                                                                                                                            |
| [factory.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/factory.py) | In the `readmeai` repository, `models/factory.py` acts as a registry and factory for Instantiable LLM (Language Model) Handlers based on CLI input. It supports offline, ollama, openai, and vertex services. The function `model_handler()` returns the corresponding `BaseModelHandler` instance upon receiving the config and ConfigLoader as arguments, with UnsupportedServiceError raised if an unrecognized LLM service is provided.                                                              |
| [prompts.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/prompts.py) | The `models/prompts.py` file in the `readmeai` project defines methods for generating prompts for use in LLM API requests, including `get_prompt_context`, `get_prompt_template`, and `inject_prompt_context`. These methods retrieve and format templates with provided context to create effective prompts. Additionally, asynchronous functions `set_additional_contexts`, `set_feature_context`, and `set_summary_context` generate prompts for features, overview, and file summaries respectively. |
| [openai.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/models/openai.py)   | The `OpenAIHandler.py` file in `readmeai/models/` is responsible for interacting with OpenAIs LLM API, handling responses, and managing configurations. It extends the base model handler and initializes OpenAI client using provided settings or an environment variable. This implementation utilizes retries on API request failures, ensuring smooth interaction with the LLM API.                                                                                                                  |

</details>

<details closed><summary>readmeai.cli</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                      |
| [options.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py) | The options.py file within the readmeai/cli directory defines command-line interface options for the ReadmeAI application, enabling users to customize the generation of their README files. Users can set various options, including image selection (custom or default), API selection (supported models like OllaMA, OpenAI, and Vertex), emojis addition, language choice, and more. |
| [main.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/main.py)       | The readmeai/cli/main.py file serves as the CLI entrypoint for the readme-ai application. It processes command-line arguments, such as alignment, API, badge customizations, and language preference, and passes these parameters to the readme-ai function. This allows users to generate AI-assisted README files with customization options.                                          |

</details>

<details closed><summary>readmeai.generators</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [tree.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tree.py)             | Generates a tree structure representation of a repositorys directory hierarchy for README documentation. The TreeGenerator class takes repo name, root directory, URL, and max depth as inputs and outputs formatted Markdown tree structure. (60 tokens)                                                                                                                                                                                                                                          |
| [builder.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/builder.py)       | The `readmeai/generators/builder.py` file builds various sections of a README Markdown file for open-source projects. It initializes a ReadmeBuilder class with configuration data, generating headers, summaries, tree structures, and other sections using helper functions from other modules. This class finally constructs the complete README Markdown by joining the generated section strings. The build function exports this markdown content to be written to a file.                   |
| [utils.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/utils.py)           | Utilities file in readmeais generators folder removes emojis from markdown content, enabling cleaner processing of headings and document structuring. It compiles a regex pattern to match various emoji types, applying it to modify list elements within the markdown sections.                                                                                                                                                                                                                  |
| [badges.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/badges.py)         | This Python file, located in readmeai/generators/badges.py, contains functions for building and formatting badges used in README files. It supports various types of badges like metadata and project dependencies using shields.io or skill icons from the skill-icons repository. The formatted badges can be aligned as per the config settings.                                                                                                                                                |
| [tables.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tables.py)         | This Python file, located in readmeai/generators/tables.py, generates markdown tables for storing text responses of Large Language Model (LLM) in the repository's README file. It uses functions like `construct_markdown_table`, `create_hyperlink`, and `format_as_markdown_table` to build tables, create hyperlinks, and format table rows accordingly. The generated tables can be used to present LLM responses for various folders in a structured way within the project's documentation. |
| [quickstart.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/quickstart.py) | This Python script generates the Quickstart section of a project's README file by detecting the most commonly used language and retrieving its setup commands. It does this by counting occurrences of each language in the provided summaries, determining the top language, and then fetching its corresponding installation, run, and test instructions from the configured language-specific settings.                                                                                         |

</details>

<details closed><summary>readmeai.services</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                           |
| [git.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/git.py)           | This Python module, located at readmeai/services/git.py, handles Git operations for cloning and validating repositories. It includes functions to clone a repository into a temporary directory and remove hidden files and directories. Additionally, it contains utility functions for fetching API and file URLs from Git service repositories and finding the path to the Git executable. |
| [metadata.py](https://github.com/eli64s/readme-ai/blob/master/readmeai/services/metadata.py) | The `metadata.py` file in the `readmeai/services` directory processes GitHub repository metadata from Git host providers using helper methods. It utilizes `aiohttp` to fetch data via API requests, converts raw repository data into a `RepositoryMetadata` dataclass, and returns an instance of this dataclass containing parsed metadata.                                                |

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
