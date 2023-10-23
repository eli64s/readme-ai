<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>FLINK-FLOW</h1>
<h3>◦ Flawlessly stream, analyze, and scale with flink-flow!</h3>
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
- [📂 repository Structure](#-repository-structure)
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

The "flink-flow" repository is a project that focuses on data stream processing using Apache Flink and Python. It provides a directory structure with configuration files, script files for cleaning and running the code, and source code files for handling alerts, consuming data, and logging. The project's value proposition lies in its ability to process data streams efficiently and perform join operations, filtering, and processing of flagged records, while also providing functionality for sending alerts and logging. It integrates with Apache Kafka and includes dependencies for libraries like pandas and asyncio for data processing and web requests.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architecture, organizing components into separate files in the `src` directory. The system uses Apache Flink and Python for data stream processing, with tables defined in the Flink table environment and windowed streams created for join operations. The system also includes an alert handler component, a logger component, and script files for running and cleaning the codebase. |
| 📄 | **Documentation**  | The repository lacks extensive documentation. While there are some inline code comments, a more comprehensive documentation including a README file would greatly improve the overall understanding and usage of the codebase. |
| 🔗 | **Dependencies**   | The system relies on multiple external dependencies, including pandas for data processing, aiohttp for web requests, aioresponses for mocking HTTP responses, and PyFlink for interacting with Apache Flink. It also relies on Apache Kafka for data streaming and includes a Flink configuration file for setting various parameters. |
| 🧩 | **Modularity**     | The codebase demonstrates good modularity by organizing components into separate files in the `src` directory. Each component has a specific responsibility, such as the alert handler, consumer, and logger. This modular design allows for easier maintenance, testing, and code reuse. |
| 🧪 | **Testing**        | There is no explicit mention of testing strategies and tools in the codebase. The addition of unit tests, integration tests, and possibly test automation frameworks would greatly enhance the reliability and maintainability of the system. |
| ⚡️  | **Performance**    | The codebase does not provide explicit performance optimizations. However, being built on top of Apache Flink, it leverages the performance benefits of Flink's distributed processing and fault tolerance capabilities. It also utilizes windowed streams for efficient data processing and consumes data in a continuous stream, allowing real-time analysis. |
| 🔐 | **Security**       | The codebase does not explicitly address security measures. Additional security measures could include implementing authentication and authorization mechanisms, encrypting sensitive data, and ensuring protection against common security vulnerabilities. |
| 🔀 | **Version Control**| The codebase is hosted on GitHub, indicating the use of Git for version control. However, specific version control strategies or tools are not explicitly mentioned in the provided information. Proper branching, version tagging, and frequent commits can enhance collaboration and code management. |
| 🔌 | **Integrations**   | The system integrates with various external systems and services. It interacts with Apache Kafka for data streaming and uses PyFlink to interface with Apache Flink for data processing. Additionally, it includes dependencies such as pandas for data processing and aiohttp for web requests. |
| 📶 | **Scalability**    | The system's architecture supports scalability through its use of Apache Flink, which is designed for distributed stream processing. By leveraging Flink's parallelism, fault tolerance, and dynamic scaling capabilities, the system can handle growth in data volume and processing requirements. Care should be taken to optimize resource allocation and ensure efficient utilization of computing resources. |

---


## 📂 Repository Structure

```sh
└── flink-flow/
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

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [requirements.txt](https://github.com/eli64s/flink-flow/blob/main/requirements.txt) | The code is a directory tree for a project called "flink-flow". It includes configuration files in the "conf" folder, script files in the "scripts" folder, a setup script in the "setup" folder, and source code files in the "src" folder. The "requirements.txt" file lists the required dependencies for the project, which include libraries for data processing with pandas and asyncio, web requests with aiohttp and aioresponses, and integration with Apache Flink and Kafka. |
| [setup.py](https://github.com/eli64s/flink-flow/blob/main/setup.py)                 | The code in `setup.py` is used to set up the Python package `STREAM-ON`. It specifies the required packages for installation, including those listed in `requirements.txt`. Additionally, it includes extra packages for development and testing, such as documentation, coding style, and testing libraries. The setup also defines the package name, version, author details, Python version requirement, and URL.                                                                    |

</details>

<details closed><summary>Setup</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                             |
| [setup.sh](https://github.com/eli64s/flink-flow/blob/main/setup/setup.sh) | The code in setup.sh checks for Java 11 and Python 3.7 installations and installs them if they are not found. It then creates a Conda environment with Python 3.8 and installs Apache Flink and PyFlink. The script also downloads and extracts PyFlink, sets environment variables, and creates aliases for running and managing Flink jobs. Finally, it confirms the completion of the PyFlink setup process. |

</details>

<details closed><summary>Scripts</summary>

| File                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [run.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/run.sh)     | The code in the `run.sh` script is used to start and stop a Flink cluster and submit a PyFlink job. It starts the Flink cluster using the `start-cluster.sh` script, submits the PyFlink job using the `word_count.py` script, and stops the Flink cluster using the `stop-cluster.sh` script.                                                                                                                                        |
| [clean.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/clean.sh) | The code in `clean.sh` is a bash script that performs various cleanup tasks in a directory. It deletes backup files with the extension `.py-e`, cleans up Python cache files (`.DS_Store`, `.pyc`, `__pycache__`), removes build artifacts (`build/`, `dist/`, `*.egg-info/`), deletes Jupyter notebook checkpoints (`.ipynb_checkpoints`), removes pytest cache (`.pytest_cache/`), and deletes log files with the extension `.log`. |

</details>

<details closed><summary>Conf</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [flink-config.yaml](https://github.com/eli64s/flink-flow/blob/main/conf/flink-config.yaml) | The code represents a Flink configuration file (flink-config.yaml) that sets various parameters for running Flink jobs. It includes settings for the JobManager, TaskManager, High Availability, parallelism, state backend, and logging.                                                                                                                                                                                                                                                                                  |
| [conf.toml](https://github.com/eli64s/flink-flow/blob/main/conf/conf.toml)                 | The code above represents a directory tree structure containing various files and folders. The `conf/conf.toml` file holds configuration constants for Kafka and Flink. It specifies the Kafka bootstrap servers and the Kafka topic to be used. It also specifies the Flink job manager and the desired parallelism level. The code provides a structured setup for working with Kafka and Flink, including scripts for cleaning and running the code, as well as files for handling alerts, consuming data, and logging. |

</details>

<details closed><summary>Src</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [alerts_handler.py](https://github.com/eli64s/flink-flow/blob/main/src/alerts_handler.py) | The code in the `src/alerts_handler.py` file is a REST API alert handler for a Flink consumer. It contains functions for sending alerts to an API using `aiohttp` in batches, buffering alerts before sending them to the API, and serializing alerts using Apache Avro. The code also includes a global variable for storing alerts in a buffer and a global lock to ensure thread safety when accessing the buffer.                                                                                                                       |
| [logger.py](https://github.com/eli64s/flink-flow/blob/main/src/logger.py)                 | The code defines a Logger class that provides logging functionality for the project. It initializes a logger with a specified name and logging level, configures the logger with a colorlog formatter, and sets up handlers for log messages. It also defines methods for logging messages at different levels including info, debug, warning, error, and critical.                                                                                                                                                                         |
| [consumer.py](https://github.com/eli64s/flink-flow/blob/main/src/consumer.py)             | The code is an implementation of data stream processing using Apache Flink and Python. It sets up a stream execution environment with specific configurations such as parallelism, time characteristics, checkpointing, and buffer timeout. It creates tables in the Flink table environment and defines windowed streams based on the tables. It performs join operations on the streams, filters the joined data, and processes flagged records by sending alerts. The result is printed and the Flink data stream processor is executed. |

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

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/eli64s/flink-flow/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/flink-flow/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/eli64s/flink-flow/issues)**: Submit bugs found or log feature requests for ELI64S.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
