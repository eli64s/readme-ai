<div align="left">
<h1><img src=https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png width="100" />
<br>FLINK-FLOW</h1>
<h3>◦ Unleash the power of your code repository.</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="left">
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
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running flink-flow](#-running-flink-flow)
    - [🧪 Tests](#-tests)
- [🚧 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The code repository flink-flow is a project that utilizes Apache Flink and Python to set up a stream processing environment, perform joins and filtering operations on data, and raise alerts for flagged records. It includes dependencies such as pandas, asyncio, aiohttp, aioresponses, apache-flink, apache-kafka, and pyflink. The repository structure consists of configuration files, setup scripts, and source code files for handling alerts, logging, and the stream consumer. The project's value proposition lies in its ability to facilitate efficient stream processing and alert handling, making it suitable for real-time data analysis and monitoring applications.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The system follows a modular architecture, with different components and scripts organized into separate directories. The main components are `src`, `scripts`, `conf`, and `setup`. The architecture can be further analyzed by studying the codebase organization and the interactions between different components.             |
| 📄 | **Documentation**  | The repository contains minimal documentation. It would be beneficial to have more comprehensive documentation that explains the purpose and functionality of each component and script. Some code files do have comments, but overall, there is room for improvement in terms of documentation quality and comprehensiveness.|
| 🔗 | **Dependencies**   | The system relies on several external libraries and systems. The `requirements.txt` file specifies the required libraries and dependencies, including pandas, asyncio, aiohttp, aioresponses, apache-flink, apache-kafka, and pyflink. These dependencies are crucial for the system's functionality, and their proper installation and configuration are necessary.   |
| 🧩 | **Modularity**     | The system demonstrates good modularity by organizing its components into separate directories. The `src` directory contains the main application logic, with files like `alerts_handler.py`, `consumer.py`, and `logger.py`. The `scripts` directory contains utility scripts, such as `run.sh` and `clean.sh`, which perform specific tasks. The `setup` directory contains the `setup.sh` script, which sets up the environment and installs dependencies. This organization allows for better codebase management and reusability of components. |
| 🧪 | **Testing**        | The repository does not provide explicit information about testing strategies and tools. It would be helpful to have information about the testing approach used, such as the frameworks or libraries employed for unit testing, integration testing, or end-to-end testing. Additionally, it would be beneficial to have a separate directory or file dedicated to testing code. Proper testing is essential for ensuring the reliability and correctness of the system.   |
| ⚡️  | **Performance**    | There is no explicit information about performance analysis or optimization. However, good design choices and the use of efficient libraries like `pandas` and `pyflink` can contribute to the system's performance. Further analysis of the codebase and profiling performance-critical sections would be necessary to provide a more accurate assessment of performance characteristics.   |
| 🔐 | **Security**       | The repository does not explicitly specify security measures. However, it is important to follow security best practices when using external libraries and systems like Apache Flink and Apache Kafka. The implementation should prevent vulnerabilities like code injection, data breaches, or unauthorized access. Proper authentication, encryption, and access control mechanisms should be considered where necessary.   |
| 🔀 | **Version Control**| The repository uses Git for version control. It would be beneficial to have more information about the version control strategies and tools employed, such as the branching model and any associated workflows. Proper version control practices ensure the ability to track changes, collaborate effectively, and maintain a stable codebase.   |
| 🔌 | **Integrations**   | The system interacts with external systems like Apache Flink and Apache Kafka. The dependencies on these systems are managed through the `requirements.txt` file, which specifies the required versions

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


## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                | Summary                                                                                                                                                                                                                           |
| ---                                                                                 | ---                                                                                                                                                                                                                               |
| [requirements.txt](https://github.com/eli64s/flink-flow/blob/main/requirements.txt) | The code in `requirements.txt` specifies the required libraries and dependencies for the project, including pandas, asyncio, aiohttp, aioresponses, apache-flink, apache-kafka, and pyflink.                                      |
| [setup.py](https://github.com/eli64s/flink-flow/blob/main/setup.py)                 | The code snippet in `setup.py` sets up the metadata and dependencies for the repository. It defines the required packages, author information, Python version compatibility, and additional packages for development and testing. |

</details>

<details closed><summary>setup</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                       | ---                                                                                                                                                                                                                                                                                                                                       |
| [setup.sh](https://github.com/eli64s/flink-flow/blob/main/setup/setup.sh) | The code snippet in setup/setup.sh performs the following functionalities:-Checks for Java 11 installation-Checks for Python 3.7 installation-Creates a Conda environment with Python 3.8 and installs Apache Flink and PyFlink-Downloads and extracts PyFlink-Sets environment variables-Sets aliases for zsh-Outputs completion message |

</details>

<details closed><summary>scripts</summary>

| File                                                                        | Summary                                                                                                                                                                                                                                                                                                                   |
| ---                                                                         | ---                                                                                                                                                                                                                                                                                                                       |
| [run.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/run.sh)     | The code snippet in `scripts/run.sh` starts and stops a Flink cluster and submits a PyFlink job for word counting.                                                                                                                                                                                                        |
| [clean.sh](https://github.com/eli64s/flink-flow/blob/main/scripts/clean.sh) | The code snippet in scripts/clean.sh accomplishes the following tasks:-Deletes backup files with.py-e extension.-Deletes Python cache files with.DS_Store and.py[co] extensions.-Deletes __pycache__ directories.-Removes build artifacts.-Deletes Jupyter notebook checkpoints.-Removes pytest cache.-Deletes log files. |

</details>

<details closed><summary>conf</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                    |
| [flink-config.yaml](https://github.com/eli64s/flink-flow/blob/main/conf/flink-config.yaml) | The code snippet in `conf/flink-config.yaml` provides the Flink configuration settings for the parent repository. It specifies the JobManager and TaskManager configurations, high-availability settings, parallelism and resource allocation, state backend configuration, and logging configuration. |
| [conf.toml](https://github.com/eli64s/flink-flow/blob/main/conf/conf.toml)                 | The code snippet defines configuration constants for Kafka and Flink in the file conf.conf.toml within the repository structure.                                                                                                                                                                       |

</details>

<details closed><summary>src</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                           |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                               |
| [alerts_handler.py](https://github.com/eli64s/flink-flow/blob/main/src/alerts_handler.py) | The code snippet in src/alerts_handler.py handles the sending and buffering of alerts from a Flink consumer to a REST API. It includes functions to send alerts in batches, serialize alerts using Apache Avro, and handle exceptions.                                                            |
| [logger.py](https://github.com/eli64s/flink-flow/blob/main/src/logger.py)                 | The provided code snippet is a Logger class that sets up a logging framework for the project. It configures the logger with a specific log level and a colored log formatter. It provides methods for logging messages at different log levels such as info, debug, warning, error, and critical. |
| [consumer.py](https://github.com/eli64s/flink-flow/blob/main/src/consumer.py)             | The code in `consumer.py` sets up a stream processing environment using Apache Flink and Python. It creates a source table, a batch view, and performs joins and filtering operations on the data. It also raises alerts for flagged records and prints the result to the console.                |

</details>

---

## 🚀 Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`

### ⚙️ Installation

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


## 🚧 Project Roadmap

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
