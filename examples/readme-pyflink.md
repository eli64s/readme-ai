<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>flink-flow
</h1>
<h3>◦ Streaming made seamless</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />
<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/eli64s/flink-flow?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/eli64s/flink-flow?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/eli64s/flink-flow?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/eli64s/flink-flow?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running flink-flow](#-running-flink-flow)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is a scalable data stream processing system built on Apache Flink and Python. It enables distributed processing of streaming data using Flink's powerful capabilities and leverages Python's data manipulation and web request functionalities. The system includes a REST API alert handler for sending alerts to external APIs, a logger for efficient logging, and a consumer module for processing and analyzing data streams. The project's value proposition lies in its ability to handle high-throughput data streams, perform complex processing tasks, and provide fault-tolerance and scalability for real-time data analysis.

---

## 📦 Features

| Feature                | Description                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a distributed stream processing architecture using Apache Flink and Python. It leverages PyFlink, aiohttp, and Avro for efficient and scalable data processing. |
| **📃 Documentation**   | The codebase lacks comprehensive documentation, which could make it challenging for new contributors to understand and use the project effectively.                             |
| **🔗 Dependencies**    | The codebase relies on several external libraries, such as pandas, asyncio, aiohttp, aioresponses, apache-flink, pyflink, and apache-kafka, to enable various functionalities.   |
| **🧩 Modularity**      | The codebase is organized into separate files, each serving a specific purpose, such as setup, configuration, API handling, logging, data processing, and cleaning tasks.         |
| **🧪 Testing**          | The codebase lacks explicit testing strategies and tools, making it difficult to assess the overall code quality and reliability.                                           |
| **⚡️ Performance**      | The system's performance is highly dependent on the efficiency and scalability of Apache Flink and PyFlink for distributed stream processing, ensuring high throughput and fault tolerance.  |
| **🔐 Security**        | The codebase does not explicitly address security measures. However, using well-maintained external libraries like aiohttp and PyFlink can provide some level of security.            |
| **🔀 Version Control** | The codebase utilizes Git for version control, allowing for collaborative development, tracking changes, and managing code revisions effectively.                          |
| **🔌 Integrations**    | The system integrates with external services, such as REST APIs and Kafka, for sending alerts and handling high-throughput messaging, respectively.                             |
| **📶 Scalability**     | With Apache Flink and PyFlink, the system can handle high volumes of data and scale horizontally by adding more task managers to the Flink cluster for distributed processing.   |

---


## 📂 Repository Structure


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

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                             |
| ---                                                                                 | ---                                                                                                                                                                                                                                                 |
| [requirements.txt](https://github.com/eli64s/flink-flow/blob/main/requirements.txt) | The code uses pandas for data manipulation, asyncio and aiohttp for asynchronous web requests, aioresponses for mocking HTTP responses, apache-flink and pyflink for distributed stream processing, and apache-kafka for high-throughput messaging. |
| [setup.py](https://github.com/eli64s/flink-flow/blob/main/setup.py)                 | This code is a setup script for a Python package. It defines the package name, version, dependencies, and other metadata. It also includes extra requirements for development and testing.                                                          |

</details>

<details closed><summary>Setup</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                     |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                         |
| [setup.sh](https://github.com/eli64s/flink-flow/blob/main/setup/setup.sh) | This code is a shell script that automates the setup process for PyFlink, a Python API for Apache Flink. It checks for Java 11 and Python 3.7 installations, installs them if necessary, creates a Conda environment, downloads and extracts PyFlink, sets environment variables, and sets aliases for zsh. |

</details>

<details closed><summary>Scripts</summary>

| File                                                                        | Summary                                                                                                                                                                                    |
| ---                                                                         | ---                                                                                                                                                                                        |
| [run.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/run.sh)     | This code script starts a Flink cluster, submits a PyFlink job (word_count.py), and then stops the Flink cluster.                                                                          |
| [clean.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/clean.sh) | This script performs a series of cleanup tasks. It deletes backup files, cleans up Python cache files, removes build artifacts, Jupyter notebook checkpoints, pytest cache, and log files. |

</details>

<details closed><summary>Conf</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                    |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                        |
| [flink-config.yaml](https://github.com/eli64s/flink-flow/blob/main/conf/flink-config.yaml) | This code is a Flink configuration file that sets various properties for the Flink job manager, task manager, high availability, parallelism, state backend, and logging. It specifies parameters such as memory size, number of threads, storage directories, quorum, and logging levels. |
| [conf.toml](https://github.com/eli64s/flink-flow/blob/main/conf/conf.toml)                 | This code defines configuration constants for connecting to a Kafka server and a Flink job manager. It specifies the bootstrap servers, topic, job manager address, and parallelism for Flink tasks.                                                                                       |

</details>

<details closed><summary>Src</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                               |
| [alerts_handler.py](https://github.com/eli64s/flink-flow/blob/main/src/alerts_handler.py) | This code is a REST API alert handler that sends alerts to an external API in batches. It includes functions for buffering alerts, serializing them using Avro, and sending them asynchronously using aiohttp. The code also includes error handling and logging capabilities.                                                                                                                                    |
| [logger.py](https://github.com/eli64s/flink-flow/blob/main/src/logger.py)                 | The code defines a Logger class that configures a logging module to provide colorful and formatted log messages. It supports different log levels and logging methods such as info, debug, warning, error, and critical.                                                                                                                                                                                          |
| [consumer.py](https://github.com/eli64s/flink-flow/blob/main/src/consumer.py)             | This code implements data stream processing using Apache Flink and Python. It sets up the Flink execution environment, creates tables, defines processing logic, and handles alerts for flagged records. The stream and batch data are joined, filtered, and processed, with results printed and saved to an output sink. Checkpointing and buffering mechanisms ensure fault-tolerance and efficient processing. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 🔧 Installation

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

### 🤖 Running flink-flow

```sh
python main.py
```

### 🧪 Tests
```sh
pytest
```

---


## 🛣 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
