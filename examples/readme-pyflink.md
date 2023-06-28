
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
flink-flow
</h1>
<h3>◦ Flink, flow, conquer code.</h3>
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

![GitHub top language](https://img.shields.io/github/languages/top/eli64s/flink-flow?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/eli64s/flink-flow?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/eli64s/flink-flow?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/eli64s/flink-flow?style&color=5D6D7E)
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is focused on creating a data processing pipeline using Apache Flink and Python. It provides functionalities for setting up a Flink cluster, processing data streams, generating alerts for flagged records, and handling alerts through a REST API. Its value proposition lies in enabling efficient real-time data processing, scalable cluster management, and seamless integration with Python for data analysis and alert handling.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**    | The codebase follows a modular architecture, with separate files for different components such as alerts handler, logger, and consumer. It leverages Apache Flink for stream processing and utilizes Python for scripting and data manipulation. The architecture allows for easy scalability and extensibility.    |
| **📖 Documentation**   | The codebase lacks comprehensive documentation. There are some comments in the code, but they are limited and do not provide a detailed explanation of the design choices or overall system functionality. Improving the documentation would enhance the codebase's readability and maintainability.    |
| **🔗 Dependencies**    | The codebase has dependencies on external libraries such as PyFlink, aiohttp, Apache Avro, logging, and colorlog. These libraries provide essential functionality for tasks such as stream processing, API handling, logging, and serialization. The usage of external libraries enhances the capabilities of the system without reinventing the wheel.    |
| **🧩 Modularity**      | The system demonstrates good modularity, with separate files for different components. This modular approach allows for easier maintenance, testing, and reusability of code. The components can be easily replaced, upgraded, or extended without affecting the entire system.    |
| **✔️ Testing**         | The codebase does not have a comprehensive testing strategy. There are no dedicated test files or frameworks in place. This makes it challenging to ensure the correctness and reliability of the system. Implementing unit tests, integration tests, and end-to-end tests would enhance the testing coverage and overall system quality.    |
| **⚡️ Performance**     | The codebase's performance depends on the underlying technologies used, such as Apache Flink. Apache Flink is known for its high-performance stream processing capabilities. However, without performance benchmarks or optimization techniques specific to the codebase, it is challenging to assess the system's performance accurately.    |
| **🔐 Security**        | The codebase does not explicitly address security measures. It may be necessary to implement authentication, authorization, and data encryption to protect sensitive information. Without detailed security measures, the system's data and functionality are potentially vulnerable.    |
| **🔀 Version Control** | The codebase utilizes Git for version control, as evidenced by its presence on GitHub. However, further exploration of the repository history, branches, and commit messages is needed to gauge the effectiveness of the version control strategy. Regular use of branches and descriptive commit messages is recommended to track changes and collaborate effectively.    |
| **🔌 Integrations**    | The system interacts with other systems through the REST API alerts handler. This allows seamless integration with external systems, enabling the exchange of data or triggering actions based on alerts. The codebase could benefit from additional integrations with monitoring systems, database connectors, or other APIs to

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

| File                                                                | Summary                                                                                                                                                                                                                                                                        |
| ---                                                                 | ---                                                                                                                                                                                                                                                                            |
| [setup.py](https://github.com/eli64s/flink-flow/blob/main/setup.py) | The code snippet is a setup.py file used for packaging a Python project. It collects required packages from a requirements.txt file and defines additional packages for documentation, code style, and testing. It also specifies the project name, version, and dependencies. |

</details>

<details closed><summary>Setup</summary>

| File                                                                      | Summary                                                                                                                                                                                                                         |
| ---                                                                       | ---                                                                                                                                                                                                                             |
| [setup.sh](https://github.com/eli64s/flink-flow/blob/main/setup/setup.sh) | This code snippet checks for Java 11, Python 3.7, and Conda installations. It then downloads and extracts PyFlink, sets environment variables, and creates aliases for easier usage. Finally, it displays a completion message. |

</details>

<details closed><summary>Scripts</summary>

| File                                                                        | Summary                                                                                                                                                                                                                           |
| ---                                                                         | ---                                                                                                                                                                                                                               |
| [run.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/run.sh)     | The code snippet starts a Flink cluster, submits a PyFlink job called "word_count.py", and then stops the Flink cluster.                                                                                                          |
| [clean.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/clean.sh) | This code snippet performs various cleanup operations such as deleting backup files, purging Python cache, removing build artifacts, deleting Jupyter notebook checkpoints, and clearing pytest cache. It also deletes log files. |

</details>

<details closed><summary>Src</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [alerts_handler.py](https://github.com/eli64s/flink-flow/blob/main/src/alerts_handler.py) | The code snippet provides a REST API alert handler for the Flink consumer. It allows sending alerts to an API in batches using aiohttp and serializes the alerts using Apache Avro. The code also includes functions to buffer alerts and send them in batches.                                                                                                                                                                                                                                                                                                                            |
| [logger.py](https://github.com/eli64s/flink-flow/blob/main/src/logger.py)                 | The provided code snippet is a Logger class that configures and provides functions to log messages with different severity levels. It uses the Python logging library to create a logger object and sets the log level to DEBUG by default. The logger is configured to output logs to the console with colored formatting using the colorlog library. It provides functions to log messages with different severity levels such as info, debug, warning, error, and critical. Each function passes the log message to the underlying logger object with the corresponding severity level. |
| [consumer.py](https://github.com/eli64s/flink-flow/blob/main/src/consumer.py)             | This code snippet leverages Apache Flink and Python to process a data stream. It sets up the Flink environment, creates tables, performs windowed joins, and generates alerts for flagged records.                                                                                                                                                                                                                                                                                                                                                                                         |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 💻 Installation

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

### 🎮 Using flink-flow

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

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
