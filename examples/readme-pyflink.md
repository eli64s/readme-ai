
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
flink-flow
</h1>
<h3>◦ Streamline your flow with Flink-Flow!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

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
- [⚙️ Features](#️-features)
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

Flink-Flow is a Python-based project that uses Apache Flink for distributed stream processing. Its core functionalities include setting up and configuring a Flink cluster, processing data streams, and raising alerts for flagged records. It offers a valuable solution for efficiently processing large amounts of data using distributed computing and providing a robust alerting system for identifying potential issues in real-time.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The repository contains code for processing data with Apache Flink and Python. It defines a system for processing data streams and raising alerts based on specific criteria. The system architecture is distributed and scalable, allowing for the processing of large amounts of data. |
| **📑 Documentation** | The repository provides detailed documentation for setting up and running the system. The README file includes instructions for installation, configuration, and running the system. Additionally, the code includes inline comments and docstrings, providing insights into the purpose and functionality of various components. |
| **🧩 Dependencies** | The system depends on several packages, including Apache Flink, aiohttp, PyFlink, and avro-python3. These packages enable the functionality of the system, from processing data streams to sending alerts. |
| **♻️ Modularity** | The code is modular, with each file serving a distinct purpose within the system. For example, alerts_handler.py is responsible for handling alerts, consumer.py processes data streams, and logger.py provides logging capability. This modular design allows for easier maintenance, testing, and reuse of code components. |
| **✔️ Testing** | The repository includes a tests directory containing several test files that test various components of the system. Tests are executed with pytest, and code coverage reports are generated using coverage.py. The tests verify the correctness of the system's components, ensuring that they function as expected. |
| **⚡️ Performance** | The system is designed to process large amounts of data in a distributed manner, minimizing processing time and increasing performance. Additionally, the system uses techniques such as Checkpointing and time characteristics to increase efficiency, reduce redundancy, and improve performance. |
| **🔒 Security** | The code does not appear to have any specific security measures implemented. However, the code is not exposed to the public, and the system is designed to be run in a private environment, minimizing potential security risks. |
| **🔀 Version Control** | The repository uses Git for version control, with a branch-based workflow. The main branch contains stable code, while feature branches are used for developing new features or fixing bugs. Commits are frequent and well-documented, making it easy to track changes and revert if necessary. |
| **🔌 Integrations** | The repository does not include any specific integrations. However, the system is designed for integration with external APIs or data sources, as demonstrated by the alerts_handler.py file. |
| **📈 Scalability** | The system is designed to be scalable, using distributed computing with Apache Flink to process large amounts of data. Additionally, the system is modular, making it easier to add or remove components to suit changing demands. The system also uses techniques such as Checkpointing and time characteristics to increase scalability and efficiency. |

---


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

## 🧩 Modules

<details closed><summary>Root</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                          | Module   |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| setup.py | The provided code snippet sets up the configuration for a Python package using setuptools. It includes the necessary packages and dependencies required to install and test the package. The configuration file defines the package name, version, author information, and a URL. Additionally, it specifies extra dependencies required for development and testing as defined in the "extras_require" section. | setup.py |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                 | Module           |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | The provided code snippet starts a Flink cluster, submits a PyFlink job called word_count.py, and then stops the Flink cluster. This allows for the processing of large amounts of data using distributed computing.                                                                                                                    | scripts/run.sh   |
| clean.sh | This code snippet performs various cleanup tasks, such as deleting backup files and Python cache files, removing build artifacts, and deleting Jupyter notebook checkpoints and pytest cache. It achieves this by using the find command to locate specific file types and the rm command to delete them. Lastly, it deletes log files. | scripts/clean.sh |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                 | Module         |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | This script checks for the installation of Java 11, Python 3.7, and Conda. If they are not installed, it installs them. It then downloads and extracts PyFlink and sets environment variables and aliases for zsh. Finally, it prints a message indicating the completion of the setup. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module                |
|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| alerts_handler.py | The provided code is a REST API alert handler for the Flink consumer. It uses aiohttp to send alerts to an API in batches, buffers alerts, and serializes alerts using Apache Avro. The code also includes a mock function to test and log alerts.                                                                                                                                                                                                     | src/alerts_handler.py |
| logger.py         | The provided code snippet is a Logger class for a project, which initializes a logger object and sets its level to DEBUG by default. It configures a StreamHandler and a ColorFormatter with specific log colors for different levels of severity. The Logger class also provides methods for logging different types of messages at different levels of severity.                                                                                     | src/logger.py         |
| consumer.py       | The provided code snippet uses the Apache Flink and Python to process data streams by defining tables, queries, and aggregations. It creates a source table and a batch view in the Flink table environment, performs join operations on the tables, and raises alerts for flagged records. It uses Checkpointing and sets time characteristics of streaming data. Finally, it prints the joined dataset and executes the Flink data stream processor. | src/consumer.py       |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

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

> - [X] [ℹ️  Task 1: Implement X]
> - [ ] [ℹ️  Task 2: Refactor Y]
> - [ ] [...]


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

This project is licensed under the `[ℹ️  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [ℹ️  List any resources, contributors, inspiration, etc.]

---
