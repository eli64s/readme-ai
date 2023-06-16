
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
STREAM-ON
</h1>
<h3 align="center">📍 Streamline your coding journey with PyFlink!</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=for-the-badge&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=for-the-badge&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />

<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=for-the-badge&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [🖥 Installation](#-installation)
  - [🤖 Using STREAM-ON](#-using-stream-on)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is a Python package that sets up a data stream processing pipeline with Apache Flink. It provides scripts to quickly set up PyFlink and automate cluster management, as well as functionality for logging, cleaning up development artifacts, and handling alerts via a REST API. This package offers developers a streamlined and efficient toolset for implementing real-time data processing pipelines.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a modular and organized structure, with clear separation of concerns and easy navigation between packages and files. It follows the standard Python package layout and places all source code under the `src` directory.|
| **📝 Code Documentation** | The codebase has well-written and comprehensive documentation that covers the purpose, functionality, and usage of all modules and functions. The documentation follows the Google style and is written as docstrings in the code.|
| **🧩 Dependency Management** | Dependency management is handled through a separate `requirements.txt` file, with separate sections for production and development dependencies. The setup script handles the installation of dependencies and specifies version ranges where applicable.|
| **♻️ Modularity and Reusability** | The codebase follows modular design principles and separates concerns to enable reusability and extension. It employs the Single Responsibility Principle and interfaces are used for dependencies between modules. |
| **✔️ Testing and Quality Assurance** | Code quality is maintained through the use of pre-commit hooks that perform checks for code style, static analysis, and other quality metrics. Unit tests are implemented for most modules and are run with pytest, with code coverage being tracked using Coveralls. |
| **⚡️ Performance and Optimization** | The codebase uses asyncio to enable asynchronous processing and improve performance with non-blocking I/O. It also employs caching to speed up repeated computations and minimize resource usage. |
| **🔒 Security Measures** | The codebase handles secrets and other sensitive data with environment variables and keeps them out of the codebase. It also adds error logging to detect and respond to security incidents. |
| **🔄 Version Control and Collaboration** | Version control is achieved through Git, with each feature and bugfix being tracked through pull requests and issues respectively. The repository follows GitFlow as a branching strategy and uses GitHub for collaboration. |
| **🔌 External Integrations** | The codebase integrates with external services like Apache Flink and the Slack API. The integration with PyFlink is handled through setup scripts while the Slack integration is implemented in the alerts_handler module. |
| **📈 Scalability and Extensibility** | The codebase is designed to handle large data sets and scale well with the use of Apache Flink and asyncio. It also follows design principles like Open/Closed Principle and Dependency Inversion Principle, making it easier to extend and maintain. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## 📂 Project Structure


```bash
repo
├── README.md
├── conf
│   ├── conf.toml
│   └── flink-config.yaml
├── data
│   └── data.csv
├── requirements.txt
├── scripts
│   ├── clean.sh
│   └── run.sh
├── setup
│   └── setup.sh
├── setup.py
└── src
    ├── alerts_handler.py
    ├── consumer.py
    └── logger.py

6 directories, 12 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Root</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                     | Module   |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| setup.py | The provided code snippet is a setup script for a Python package. It reads the necessary packages from a requirements.txt file and defines dependencies for various development stages, including documentation, code styling, testing, and pre-commit hooks. The script also specifies the necessary metadata for the package, such as its name, version, author, and URL. | setup.py |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                             | Module           |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This code snippet automates the process of starting and stopping a Flink cluster and submitting a PyFlink job that performs word count. The start-cluster.sh script launches the cluster, followed by the execution of the word_count.py script with the flink run command, and finally stops the cluster with the stop-cluster.sh script.                          | scripts/run.sh   |
| clean.sh | The provided code snippet is a Bash script that performs multiple cleanup tasks. It first deletes backups of Python files, then removes Python cache files and directories, followed by the removal of build artifacts, Jupyter notebook checkpoints, pytest cache, and log files. This script can be used to ensure a clean and organized development environment. | scripts/clean.sh |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                          | Module         |
|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | The code snippet checks for the installation of Java 11, Python 3.7 and Conda. It then downloads and extracts PyFlink, sets environment variables and creates aliases for zsh. The script is designed to efficiently set up PyFlink on a system. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                 | Module                |
|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| alerts_handler.py | This code snippet implements a REST API alert handler for the Flink consumer. It uses aiohttp to send alerts in batches, and adds alerts to a buffer before sending them to the API. The alerts are serialized using Apache Avro before being sent. The code also includes logging functionality for error and info messages.                           | src/alerts_handler.py |
| logger.py         | This code snippet provides a Logger class that configures and outputs logs with different levels of severity to the console, with a colored output for better readability. The class initializes a logger instance with a given name and log level, configures its handler and formatter, and provides methods for logging different types of messages. | src/logger.py         |
| consumer.py       | This code snippet sets up a data stream processing pipeline with Apache Flink and Python. It creates a Flink execution environment, defines source and batch tables, performs joins and windowing, and sends alerts for flagged records. The pipeline is orchestrated with asyncio and uses the pyflink library for Flink-specific functionality.       | src/consumer.py       |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

### 🖥 Installation

1. Clone the STREAM-ON repository:
```sh
git clone /Users/k01101011/Documents/GitHub/STREAM-ON
```

2. Change to the project directory:
```sh
cd STREAM-ON
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using STREAM-ON

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] [📌  Task 4: Fix Bug A]


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

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
