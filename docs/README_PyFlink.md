
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
STREAM-ON
</h1>
<h3 align="center">📍 Streamline your coding journey with STREAM-ON.</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=for-the-badge&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=for-the-badge&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />

<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=for-the-badge&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka" />
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

The project is a Python-based stream processing application that uses Apache Flink for real-time data processing. It includes modules for handling alerts, logging, and managing a Flink cluster. The project automates the process of starting and stopping a Flink cluster, processing data streams, and sending alerts based on flagged data. Its value proposition lies in its ability to efficiently handle large-scale data streams and provide real-time analytics.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a well-organized structure with separate directories for scripts, source code, and setup files, making the repository easy to navigate and understand. |
| **📝 Code Documentation** | The codebase includes code comments and docstrings that provide clear and concise descriptions of the purpose and functionality of each module and function. |
| **🧩 Dependency Management** | The codebase uses a "requirements.txt" file and a setup script to manage dependencies and ensure consistency across development and deployment environments. |
| **♻️ Modularity and Reusability** | The codebase follows the modular design pattern, with different modules responsible for specific functionality. This approach allows for easy reuse of individual modules in other projects. |
| **✔️ Testing and Quality Assurance** | The codebase includes a "clean.sh" script that clears any pytest caches, enforces linting rules, and deletes unnecessary files to ensure high code quality. |
| **⚡️ Performance and Optimization** | The codebase leverages Apache Flink for efficient stream processing and utilizes batching and locking mechanisms to optimize API requests and ensure thread-safe processing of alerts. |
| **🔒 Security Measures** | The codebase does not contain any explicit security measures, but it follows good coding practices, such as input validation and exception handling, to minimize security vulnerabilities. |
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub and uses Git for version control, allowing for easy collaboration and version tracking. |
| **🔌 External Integrations** | The codebase integrates with Apache Flink and PyFlink for stream processing and with aiohttp for sending alerts to an API. |
| **📈 Scalability and Extensibility** | The codebase is built on top of Apache Flink, a highly scalable stream processing framework, and follows the modular design pattern, which makes it easily extensible for future components and features. |

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

| File     | Summary                                                                                                                                                                                                                                                                                                                                              | Module   |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| setup.py | The code snippet is a Python setup file that specifies the dependencies, packages, and other details required to build and distribute a Python package. It reads the dependencies from a "requirements.txt" file and sets up additional optional packages for development and testing. It also sets the Python version requirement to 3.7 or higher. | setup.py |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                              | Module           |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This Bash script starts a Flink cluster using the "start-cluster.sh" script, submits a PyFlink job using the "run" command with a specified Python script, and stops the Flink cluster using the "stop-cluster.sh" script. It automates the process of starting and stopping a Flink cluster and running a PyFlink job.                                                                              | scripts/run.sh   |
| clean.sh | This Bash script is designed to clean up various types of files and directories in a Python project. Specifically, it deletes files with certain extensions, removes Python cache files and directories, removes build artifacts and Jupyter notebook checkpoints, clears any pytest caches, and deletes log files. Overall, this script helps ensure the project is in a clean and organized state. | scripts/clean.sh |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                       | Module         |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | This code snippet checks for Java 11, Python 3.7, and Conda installations, installing them if necessary. It then downloads and extracts PyFlink, sets necessary environment variables, and creates aliases for zsh. Finally, it provides a message indicating that PyFlink setup is complete. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                             | Module                |
|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| alerts_handler.py | The provided code snippet is a Python module for handling alerts in a REST API for Flink consumers. The module provides functions for sending alerts to an API using aiohttp in batches, adding alerts to a buffer and sending them to the API in batches, and serializing alerts using Apache Avro. The module also includes a global buffer and lock for thread-safe processing of alerts.        | src/alerts_handler.py |
| logger.py         | The code snippet provides a Logger class that can be used to log messages of varying levels. The Logger class uses the logging and colorlog modules to set up a logger with different log colors corresponding to different log levels. The class has methods for logging at different levels (info, debug, warning, error, and critical).                                                          | src/logger.py         |
| consumer.py       | The code processes a data stream using Apache Flink and Python. It configures and creates a Flink execution environment, creates source and batch tables, joins the tables, and filters out flagged data that does not match. It then prints the data stream and executes a loop to gather all tasks. Finally, it sends an alert based on flagged data and shuts down the stream processing engine. | src/consumer.py       |

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
> - [ ] ...


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
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
