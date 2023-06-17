
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
flink-flow
</h1>
<h3 align="center">📍 Flow with Flink, streamline with flink-flow.</h3>
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
  - [🤖 Using flink-flow](#-using-flink-flow)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The "flink-flow" project provides a Python-based data stream processing pipeline using Apache Flink. It offers functionality such as checkpointing, table creation and windowed join operations, as well as handling errors and exceptions, and enabling REST API alert handling. Its value proposition lies in enabling streamlined and efficient real-time data processing for a range of applications.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase is organized into a Python package with a clear hierarchy of modules. It also includes a setup script for easy installation and deployment. |
| **📝 Code Documentation** | The codebase has comprehensive inline documentation using docstrings, which enables easy understanding and maintenance of the code. |
| **🧩 Dependency Management** | The codebase uses Conda for dependency management and specifies package dependencies in a separate file, which ensures easy installation and management of dependencies. |
| **♻️ Modularity and Reusability** | The codebase is modularized into small, reusable components that are loosely coupled and encapsulated, which promotes reusability and maintainability. |
| **✔️ Testing and Quality Assurance** | The codebase includes a test suite using the pytest framework, which enables automated unit and integration testing to ensure code correctness and quality. |
| **⚡️ Performance and Optimization** | The codebase leverages Apache Flink for data streaming and processing, which provides high performance and scalability, and implements best practices such as checkpointing to ensure fault tolerance. |
| **🔒 Security Measures** | The codebase implements security measures such as serialization using Apache Avro and exception handling to prevent potential security vulnerabilities and data breaches. |
| **🔄 Version Control and Collaboration** | The codebase uses Git for version control and includes a clear commit history and pull request templates, which enables easy collaboration and maintenance of the codebase. |
| **🔌 External Integrations** | The codebase includes external integrations such as PyFlink and aiohttp to handle REST API requests, which enables seamless integration with other technologies and systems. |
| **📈 Scalability and Extensibility** | The codebase is designed to handle large volumes of data and can be easily extended by adding more modules or integrating with other data sources or systems.

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

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                      | Module   |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| setup.py | The code sets up a Python package called STREAM-ON with version 0.1, and specifies its dependencies based on the packages listed in requirements.txt. Additionally, it defines extra packages for development and testing purposes, such as documentation, code styling, and testing frameworks. Finally, it uses setuptools to find and include all packages under the specified namespace. | setup.py |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                          | Module           |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This Bash script starts a Flink cluster, runs a PyFlink job to perform word count and finally stops the Flink cluster. The script executes three commands: start-cluster.sh, flink run and stop-cluster.sh, respectively.                                                                                                                                                        | scripts/run.sh   |
| clean.sh | The provided code snippet is a bash script that performs various cleanup and backup tasks. It deletes files ending with ".py-e", removes Python cache files including ".DS_Store", ".pyc" and "__pycache__" directories, deletes build artifacts, removes Jupyter notebook checkpoints and clears the pytest cache. Additionally, it also deletes files with a ".log" extension. | scripts/clean.sh |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                  | Module         |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | This Bash script checks if Java 11, Python 3.7, and Conda are installed and installs them if not. It then downloads and extracts PyFlink, sets environment variables, sets aliases for zsh, and outputs a message indicating that the setup is complete. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                             | Module                |
|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| alerts_handler.py | The provided code snippet is a REST API alert handler for a Flink consumer. It buffers alerts and sends them in batches to the API address specified in the code. The alerts are serialized using Apache Avro. The code uses aiohttp to handle the API requests and is designed to handle exceptions and errors when sending alerts to the API.                                                                                     | src/alerts_handler.py |
| logger.py         | The provided code snippet contains a Logger class that is configured to log messages at different levels of severity. The logger uses a color-coded format and allows for messages to be logged with different severity levels such as info, debug, warning, error, and critical. It also allows for the customization of log colors and formats.                                                                                   | src/logger.py         |
| consumer.py       | This code snippet provides a data stream processing pipeline with Apache Flink and Python. It sets up a Flink execution environment with checkpointing and buffer timeout settings, creates source and batch tables in Flink table environment, performs a windowed join operation between these tables and a data stream, and sends an alert for each flagged record. It uses asyncio to orchestrate the stream processing engine. | src/consumer.py       |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

### 🖥 Installation

1. Clone the flink-flow repository:
```sh
git clone https://github.com/eli64s/flink-flow
```

2. Change to the project directory:
```sh
cd flink-flow
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using flink-flow

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
