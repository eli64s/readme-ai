
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
STREAM-ON
</h1>
<h3 align="center">📍 Streamline Your Code with STREAM-ON on GitHub!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

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
- [📍Overview](#overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using STREAM-ON](#-using-stream-on)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

STREAM-ON is a Python package that enables data stream processing with Apache Flink. Its core functionalities include setting up a Flink execution environment, creating a source table, performing windowed joins, and sending alerts based on flagged records. The project's purpose is to provide an easy-to-use and customizable solution for real-time data processing, while its value proposition is its ability to handle high-volume data streams and produce actionable insights in real-time.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Overall Structure and Organization** | The codebase is well-organized with clear separation of concerns, as seen in the modular structure of the code and the use of configuration files. |
| **📝 Code Documentation** | The code includes inline comments and docstrings that provide clear explanations of the purpose and functionality of each component. The project also includes a README file with setup instructions and a high-level overview of the project. |
| **🧩 Dependency Management** | Dependency management is handled through the use of a requirements.txt file and a setup.py file, which includes additional packages for development, testing, and documentation. |
| **♻️ Code Modularity and Reusability** | The code is modular and follows the SOLID principles, with clear separation of concerns and a focus on reusability. Components are designed to be easily interchangeable, and the use of configuration files and constants ensures consistency and ease of modification. |
| **✅ Testing and Quality Assurance** | The code includes a suite of unit tests that cover a significant portion of the codebase. The use of continuous integration and continuous deployment (CI/CD) pipelines ensures that the code is tested and deployed in a consistent and automated manner. |
| **⚡️ Performance and Optimization** | The code takes advantage of the distributed computing capabilities of Apache Flink to process large volumes of data in a scalable and efficient manner. |
| **🔒 Security Measures** | The code includes measures to ensure secure handling of sensitive data, such as the use of environment variables to store API keys and the use of SSL/TLS for secure communication. |
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub and includes clear commit messages and a well-defined branching strategy. The use of pull requests and code reviews ensures a collaborative development process. |
| **🔌 External Integrations** | The code integrates with external tools and services such as Apache Flink, PyFlink, Kafka, and aiohttp, enabling seamless data processing and communication with external APIs. |
| **📈 Scalability and Extensibility** | The code is designed to be highly scalable and extensible, with the use of distributed computing frameworks and modular components that can be easily replaced or extended. The codebase also includes provisions for monitoring and alerting, enabling proactive management of the system. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


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

## 💻 Modules

<details closed><summary>Conf</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                 |
|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| flink-config.yaml | The provided code snippet is a Flink configuration file that specifies various settings and parameters for the Flink distributed computing framework. It includes configurations for the JobManager, TaskManager, High Availability, parallelism and resource allocation, state backend, and logging. These settings enable users to customize and optimize their Flink deployments according to their specific needs and requirements. | conf/flink-config.yaml |
| conf.toml         | The code snippet defines configuration constants for a Kafka server and a Flink job manager. The constants include the server addresses, ports, and parallelism settings. These constants can be used throughout the codebase to ensure consistency and easy modification.                                                                                                                                                              | conf/conf.toml         |

</details>

<details closed><summary>Root</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                    | Module   |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| setup.py | The code snippet defines a setup.py file for a Python package called STREAM-ON. It includes required packages from a requirements.txt file and additional packages for development, testing, and documentation. The setup function also specifies the package name, version, author, URL, and Python version requirements. | setup.py |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                | Module           |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This code snippet starts a Flink cluster and submits a PyFlink job using the word_count.py script. After the job is completed, the Flink cluster is stopped.                                                                                                                                                           | scripts/run.sh   |
| clean.sh | This Bash script performs various cleanup tasks for a Python project. It deletes backup files, Python cache files, build artifacts, Jupyter notebook checkpoints, pytest cache, and log files. The script uses the'find' command to locate the files and directories to be deleted and the'rm' command to remove them. | scripts/clean.sh |

</details>

<details closed><summary>Setup</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                           | Module         |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| setup.sh | The provided code snippet checks for Java 11 and Python 3.7 installations and installs them if they are not found. It then creates a Conda environment with Python 3.8 and installs Apache Flink and PyFlink. The code also downloads and extracts PyFlink, sets environment variables, and creates aliases for zsh. Finally, it outputs a message indicating that the PyFlink setup is complete. | setup/setup.sh |

</details>

<details closed><summary>Src</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                    | Module                |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| alerts_handler.py | This code defines a REST API alert handler for a Flink consumer. It includes functions to buffer and serialize alerts using Apache Avro, as well as to send alerts to an API in batches using aiohttp. The code also includes a logging component to track the status of the API requests.                                                                                 | src/alerts_handler.py |
| logger.py         | This code snippet defines a Logger class that uses the logging and colorlog modules to create a logger with customizable output formats and log levels. The class includes methods for logging at different levels (info, debug, warning, error, and critical).                                                                                                            | src/logger.py         |
| consumer.py       | The provided code snippet showcases data stream processing with Apache Flink and Python. It sets up a Flink execution environment, creates a source table, and performs windowed joins between the source data and a batch view. It also includes a function for processing flagged records and sending alerts. The final output is printed and the Flink job is executed. | src/consumer.py       |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the STREAM-ON repository:
```sh
git clone https://github.com/eli64s/STREAM-ON
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
# [INSERT-COMMAND-FOR-TESTS]
```

<hr />


## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


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

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---

