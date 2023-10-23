<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>FLINK-FLOW</h1>
<h3>◦ Flow like a Flink!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=flat-square&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />
<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=flat-square&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
</p>
<img src="https://img.shields.io/github/license/eli64s/flink-flow?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/eli64s/flink-flow?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/eli64s/flink-flow?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/eli64s/flink-flow?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running flink-flow](#-running-flink-flow)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository contains code for a data stream processing system using Apache Flink and Python. It provides functionality for processing streaming data, creating tables, performing join operations, filtering records, sending alerts, and shutting down the processing engine. The code includes dependencies for asynchronous programming, data manipulation, web requests, mocking HTTP responses, and integrating Apache Flink and Kafka. Additionally, it provides setup scripts for installing required packages and environment configuration files for optimal performance and functionality.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase uses Apache Flink and Kafka for stream processing. It follows a modular structure with separate files for handling alerts, consuming data, and logging. It also includes setup and configuration files.                                                  |
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation.                                                               |
| 🔗 | **Dependencies**   | The codebase relies on external libraries such as aioresponses, pandas, aiohttp, and pyflink for data processing, HTTP requests, and integration with Apache Flink and Kafka.                                                               |
| 🧩 | **Modularity**     | The codebase is organized into separate files for alerts handling, consuming data, and logging. These files can be easily interchanged and extended.                                                                  |
| 🧪 | **Testing**        | The codebase lacks information about testing strategies and tools.                                                |
| ⚡️  | **Performance**    | The codebase utilizes Apache Flink, known for its high-performance stream processing capabilities. It also uses async programming techniques to improve efficiency.                                              |
| 🔐 | **Security**       | The codebase does not have specific measures for security.                                                         |
| 🔀 | **Version Control**| The repository uses Git version control.                                                                       |
| 🔌 | **Integrations**   | The codebase integrates with Apache Flink and Apache Kafka for stream processing. It also uses aioresponses library for mocking HTTP responses.                                              |
| 📶 | **Scalability**    | Apache Flink is designed for horizontal scalability, allowing the system to handle growth efficiently. The codebase can leverage the scalability features provided by Flink.            |

---


## 📂 Repository Structure

```sh
└── ./
    ├── conf/
    │   ├── conf.toml
    │   └── flink-config.yaml
    ├── requirements.txt
    ├── scripts/
    │   ├── clean.sh
    │   └── run.sh
    ├── setup/
    │   └── setup.sh
    ├── setup.py
    └── src/
        ├── alerts_handler.py
        ├── consumer.py
        └── logger.py

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [requirements.txt](https://github.com/eli64s/flink-flow/blob/main/requirements.txt) | The code in the requirements.txt file defines the dependencies required for a project. The listed libraries pertain to asynchronous programming, data manipulation with pandas, web requests with aiohttp, mocking HTTP responses with aioresponses, and integrating Apache Flink and Kafka.                                                                                                                                         |
| [setup.py](https://github.com/eli64s/flink-flow/blob/main/setup.py)                 | This is a setup script (`setup.py`) for a Python project named "STREAM-ON". It specifies the project's dependencies, including the required packages listed in `requirements.txt` file. It also defines additional packages for development (`docs_packages`, `style_packages`, `test_packages`) and sets up the project's metadata (name, version, description, author, etc.) for distribution and installation using `setuptools`. |

</details>

<details closed><summary>Setup</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [setup.sh](https://github.com/eli64s/flink-flow/blob/main/setup/setup.sh) | The code in the `setup.sh` script performs the following functionalities:1. Checks for the installation of Java 11 and installs it if necessary.2. Checks for the installation of Python 3.7 and installs it if necessary.3. Creates a Conda environment named `pyflink` with Python 3.8 and activates it.4. Installs Apache Flink and PyFlink using `pip` in the `pyflink` environment.5. Downloads and extracts PyFlink binaries.6. Sets environment variables for Flink Conda home, PATH, and PYTHONPATH.7. Sets aliases for convenient usage in zsh.8. Prints a completion message when the setup is done. |

</details>

<details closed><summary>Scripts</summary>

| File                                                                        | Summary                                                                                                                                                                                                                                                                                                                               |
| ---                                                                         | ---                                                                                                                                                                                                                                                                                                                                   |
| [run.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/run.sh)     | The code in the "scripts/run.sh" file starts a Flink cluster, submits a PyFlink job using the "word_count.py" script, and then stops the Flink cluster. This script is part of a larger directory tree that includes configuration files, additional scripts, and source code files for handling alerts, consuming data, and logging. |
| [clean.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/clean.sh) | The code in'clean.sh' is a script that performs various cleaning tasks on a directory. It deletes backup files, cleans up Python cache files, removes build artifacts, Jupyter notebook checkpoints, pytest cache, and log files.                                                                                                     |

</details>

<details closed><summary>Conf</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [flink-config.yaml](https://github.com/eli64s/flink-flow/blob/main/conf/flink-config.yaml) | The code provided is a Flink configuration file (flink-config.yaml) that contains various settings for the Flink framework. It includes configurations for the JobManager and TaskManager, high availability settings, parallelism and resource allocation, state backend configuration, and logging configuration. These settings ensure optimal performance and functionality of Flink for data processing and analysis tasks. |
| [conf.toml](https://github.com/eli64s/flink-flow/blob/main/conf/conf.toml)                 | This code defines configuration constants for a Kafka and Flink setup. It specifies the Kafka bootstrap servers and topic, as well as the Flink job manager and parallelism level. These constants can be used in other parts of the code to connect to Kafka and configure Flink jobs.                                                                                                                                          |

</details>

<details closed><summary>Src</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [alerts_handler.py](https://github.com/eli64s/flink-flow/blob/main/src/alerts_handler.py) | This code defines a module for handling alerts in a Flink consumer. It includes functions for sending alerts to an API using aiohttp, buffering alerts in batches, and serializing alerts using Apache Avro. Alerts are stored in a buffer and sent to the API when the buffer reaches a certain size. The code also includes a logger for logging information and errors.                                                                                                                         |
| [logger.py](https://github.com/eli64s/flink-flow/blob/main/src/logger.py)                 | The code defines a Logger class that encapsulates logging functionality for a project. It sets up a logger object with a specified name and level, and configures it with a colorized log formatter. The logger provides methods for logging different levels of messages (info, debug, warning, error, critical) and formats them with the specified logger name, level, and log message.                                                                                                         |
| [consumer.py](https://github.com/eli64s/flink-flow/blob/main/src/consumer.py)             | The code is for a data stream processing system using Apache Flink and Python. It sets up the environment for processing streaming data, creates a source table, and a batch view in the Flink table environment. It then performs a join operation on the source table and the batch view, filters out records that don't match certain criteria, and processes the flagged records by sending alerts. Finally, it executes the Flink data stream processor and shuts down the processing engine. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

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


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

[**Discussions**](https://github.com/eli64s/flink-flow/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/eli64s/flink-flow/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/eli64s/flink-flow/blob/main/CONTRIBUTING.md)

- Contributions are welcome! Please follow these steps:

1. Fork the project repository to your GitHub account.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive such as `new-feature-x` or `bugfix-issue-x`.
```sh
git checkout -b new-feature-x
```
4. Develop your changes locally.
5. Commit your updates with a clear explanation of the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub.
```sh
git push origin new-feature-x
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
8. Once your pull request is reviewed, it will be merged into the main branch of the project repository.

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
