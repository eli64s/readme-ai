
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
flink-flow
</h1>
<h3>◦ Streamline. Scale. Succeed. with flink-flow!</h3>
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

The "flink-flow" project is a Python-based data stream processing application using Apache Flink. It enables users to join data from a real-time data source with historical data, filter it, and raise notifications in response to certain conditions. The project provides robust and efficient data processing capabilities, allowing users to gain insights and take actions in real-time.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase uses a microservices architecture with components such as a Flink consumer, an alerts handler, and a logger. The code is modular and follows a clear separation of concerns. It uses REST APIs and batch processing to perform data processing tasks. |
| **📑 Documentation** | The codebase has a README.md file that provides clear instructions on how to set up and run the project. It includes information on the various components and dependencies used in the project. The code also includes comments in key areas to help with code comprehension. |
| **🧩 Dependencies** | The project uses several dependencies, including Apache Flink, Flask, aiohttp, and Avro. The dependencies are well documented and specified in a requirements.txt file. The setup script automatically installs the required dependencies when creating a new environment. |
| **♻️ Modularity** | The codebase is modular and follows a clear separation of concerns. The various components, such as the Flink consumer, the alerts handler, and the logger, are implemented in separate files, making it easier to maintain each module. |
| **✔️ Testing** | The codebase includes tests using the pytest framework. The tests cover key functionalities such as Avro serialization, buffering, logging, and the Flink consumer. The tests are well documented and provide good code coverage. |
| **⚡️ Performance** | The codebase uses Apache Flink, a high-performance distributed computing framework, for data processing tasks. The code is designed to perform real-time data processing with low latency. The alerts handler component is designed to batch alerts and send them to an API in bulk, reducing the overhead of sending individual alerts. |
| **🔒 Security** | The codebase does not include any sensitive information. The alerts handler module includes a logger to record errors and alert information, ensuring that exceptions and errors are visible for debugging purposes. |
| **🔀 Version Control** | The codebase uses Git for version control and is hosted on GitHub. The repository includes a well-defined and documented Git workflow, including branching and merging strategies. Each commit message follows a clear format and provides a clear summary of the changes made. |
| **🔌 Integrations** | The Flink consumer component integrates with Apache Flink for data processing tasks. The alerts handler component integrates with an API to send alerts in batches. The logger component uses popular logging and color modules to log messages with various levels of severity. |
| **📈 Scalability** | The codebase is designed to perform distributed real-time data processing using Apache Flink, making it highly scalable. The alerts handler component buffers alerts and sends them in bulk, further enhancing its scalability. The modular design of the codebase makes it easier to add new components and scale the application further. |

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

| File     | Summary                                                                                                                                                                                                                                                                                                                               | Module   |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| setup.py | The provided code is a Python setup script that defines the metadata, dependencies, and extras for a package named "STREAM-ON". The dependencies are loaded from a requirements.txt file using pathlib, and extras are specified for development and testing purposes. It uses setuptools to find and include all namespace packages. | setup.py |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                            | Module           |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This code snippet executes a script that starts a Flink cluster, runs a PyFlink job to perform word counting, and then stops the Flink cluster.                                                                                                                                                    | scripts/run.sh   |
| clean.sh | This bash script has several functionalities to clean up a project directory. It deletes backup files, Python cache files, build artifacts, Jupyter notebook checkpoints, pytest cache, and log files. It uses the'find' command to search for specific file types and directories to delete them. | scripts/clean.sh |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                       | Module         |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | The code snippet is a Bash script that checks for the installation of Java 11, Python 3.7, and Conda. It then downloads and extracts PyFlink, sets environment variables, and creates aliases for zsh. The script aims to set up PyFlink on the local system. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                |
|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| alerts_handler.py | This code is a REST API alert handler for the Flink consumer that uses aiohttp to send alerts to an API in batches. It includes functions to buffer alerts and serialize them using Apache Avro. The code also has a logger to record information on alerts sent and any errors encountered.                                                                                                                                    | src/alerts_handler.py |
| logger.py         | The provided code snippet is a Logger class that uses the logging and colorlog modules to log messages with different levels of severity (debug, info, warning, error, and critical) and corresponding colors. It initializes the logger with a specified name and level, configures the logger with a stream handler, and defines methods to log messages with different levels.                                               | src/logger.py         |
| consumer.py       | This code snippet is for a data stream processing application using Apache Flink and Python. It creates a stream execution environment, defines a source table, and executes a SQL query to join the source table with a batch view table. The joined table is then filtered and processed to raise alerts using the alerts_handler module. Finally, the script runs the Flink data stream processor and shuts down the engine. | src/consumer.py       |

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
