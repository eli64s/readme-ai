<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">PYFLINK-POC</h1>
</p>
<p align="center">
    <em>Stream like a pro with PyFlink!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/pyflink-poc?style=plastic&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/pyflink-poc?style=plastic&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/pyflink-poc?style=plastic&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/pyflink-poc?style=plastic&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=plastic&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=plastic&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=plastic&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=plastic&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=plastic&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=plastic&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/Markdown-000000.svg?style=plastic&logo=Markdown&logoColor=white" alt="Markdown">
</p>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running pyflink-poc](#-running-pyflink-poc)
    - [🧪 Tests](#-tests)
- [🛠 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The pyflink-poc project is a Python codebase that focuses on integrating Apache Flink and Apache Kafka for stream processing. It aims to provide a seamless and efficient way to process and analyze large-scale streaming data. The core functionalities of the project include establishing real-time data pipelines, performing data transformations and aggregations, and implementing scalable and fault-tolerant stream processing applications. By leveraging the power of Apache Flink and Apache Kafka, this project enables users to build robust and high-performance stream processing solutions, making it valuable for industries that deal with real-time data analysis, such as finance, e-commerce, and IoT.

---

## 📦 Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The codebase follows a simple structure where the main source code files are located in the `src/` directory. It appears to be a data processing pipeline using Apache Flink and Apache Kafka.             |
| 📄 | **Documentation**  | There is no specific information about the documentation in the repository. |
| 🔗 | **Dependencies**   | The codebase relies on various external libraries such as `sh`, `yaml`, `pyflink`, `asyncio`, `aioresponses`, `aiohttp`, `toml`, etc. It also mentions dependencies related to Apache Kafka and Apache Flink.|
| 🧩 | **Modularity**     | The system seems to be organized into smaller components/files such as `alerts_handler.py`, `consumer.py`, and `logger.py`. However, a more detailed analysis of modularity is not possible without further examination of the codebase. |
| 🧪 | **Testing**        | There are no specific details about the testing strategies or tools used in the repository. |
| ⚡️ | **Performance**     | There is no information available about performance considerations or any performance optimization techniques employed in the codebase. |
| 🔐 | **Security**       | The repository does not provide any specific information about security measures. It's important to note that ensuring data security and maintaining functionality should be a priority for any production system. |
| 🔀 | **Version Control**| The repository uses Git for version control. Further details about version control strategies and tools are not available in the repository. |
| 🔌 | **Integrations**   | The codebase appears to have integrations with Apache Flink and Apache Kafka. Specific details about other integrations or external services are not provided. |
| 📶 | **Scalability**    | It is difficult to assess the system's scalability without further information. However, being built on Apache Flink and Apache Kafka, both known for their scalability, suggests that the system might have scalability potential.    |

---

## 📂 Repository Structure

```sh
└── pyflink-poc/
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

| File                                                                                 | Summary                                                                                                                                                                                                                                                                |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                    |
| [requirements.txt](https://github.com/eli64s/pyflink-poc/blob/main/requirements.txt) | This code snippet, part of the pyflink-poc repository, handles alerts, consumers, and logging. It utilizes dependencies such as pandas, asyncio, and aiohttp. It also incorporates software like apache-flink, apache-kafka, and pyflink.                              |
| [setup.py](https://github.com/eli64s/pyflink-poc/blob/main/setup.py)                 | This code snippet, setup.py, is responsible for setting up the project dependencies and packages. It reads the requirements.txt file and installs the necessary packages for the repository. It also includes extra requirements for development and testing purposes. |

</details>

<details closed><summary>setup</summary>

| File                                                                       | Summary                                                                                                                                                                                                                                                                                                      |
| ---                                                                        | ---                                                                                                                                                                                                                                                                                                          |
| [setup.sh](https://github.com/eli64s/pyflink-poc/blob/main/setup/setup.sh) | This code snippet sets up the environment for PyFlink, installing Java 11 and Python 3.7, creating a Conda environment, downloading and extracting PyFlink, and setting environment variables and aliases. It ensures that all necessary software and dependencies are in place for PyFlink to run smoothly. |

</details>

<details closed><summary>scripts</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                        |
| [run.sh](https://github.com/eli64s/pyflink-poc/blob/main/scripts/run.sh)     | This code snippet is responsible for starting and stopping a Flink cluster and submitting a PyFlink job to it. It is located in the scripts directory of the parent repository. The main file is run.sh.                                                                                                                                                                   |
| [clean.sh](https://github.com/eli64s/pyflink-poc/blob/main/scripts/clean.sh) | The `clean.sh` script in the `scripts` directory of the codebase is responsible for cleaning up and removing various artifacts and files that are not needed. It deletes backup files, Python cache files, build artifacts, Jupyter notebook checkpoints, pytest cache, and log files. This script ensures a clean and organized codebase by removing unnecessary clutter. |

</details>

<details closed><summary>conf</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                      |
| [flink-config.yaml](https://github.com/eli64s/pyflink-poc/blob/main/conf/flink-config.yaml) | This code snippet includes the Flink configuration file `flink-config.yaml` that specifies various settings for Flink job execution, such as parallelism, resource allocation, state backend, logging, and high availability. It is an essential component of the parent repository's architecture as it ensures optimal performance and fault tolerance for Flink jobs. |
| [conf.toml](https://github.com/eli64s/pyflink-poc/blob/main/conf/conf.toml)                 | This code snippet in the pyflink-poc repository focuses on configuration constants related to Kafka and Flink. It defines the Kafka bootstrap servers and topic, as well as the Flink job manager and parallelism. It plays a critical role in setting up and connecting the components of the repository's architecture.                                                |

</details>

<details closed><summary>src</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [alerts_handler.py](https://github.com/eli64s/pyflink-poc/blob/main/src/alerts_handler.py) | The code snippet in the `alerts_handler.py` file is responsible for handling and sending alerts to an API in batches using aiohttp. It includes functions to serialize alerts using Apache Avro and buffer alerts before sending them. The code also implements a logger for tracking the status of the alert handling process.                                                                                                                                                                                                                     |
| [logger.py](https://github.com/eli64s/pyflink-poc/blob/main/src/logger.py)                 | The code snippet contains a Logger class that provides logging functionality for the project. It configures the logger, sets the log level, and formats log messages with colors. It supports logging at different levels such as info, debug, warning, error, and critical.                                                                                                                                                                                                                                                                        |
| [consumer.py](https://github.com/eli64s/pyflink-poc/blob/main/src/consumer.py)             | This code snippet is part of a larger repository for a data stream processing project using Apache Flink with Python. The code sets up the execution environment and time characteristics, enables checkpointing for fault tolerance, and creates a table environment for processing streaming data. It also defines functions to create the source table and batch view, processes flagged records, and orchestrates the stream processing engine. The code demonstrates the use of Flink APIs for data manipulation and aggregation over streams. |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* Python: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

### ⚙️ Installation

1. Clone the pyflink-poc repository:
```sh
git clone https://github.com/eli64s/pyflink-poc
```

2. Change to the project directory:
```sh
cd pyflink-poc
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running pyflink-poc
Use the following command to run pyflink-poc:
```sh
python main.py
```

### 🧪 Tests
To execute tests, run:
```sh
pytest
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/eli64s/pyflink-poc/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/pyflink-poc/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/eli64s/pyflink-poc/issues)**: Submit bugs found or log feature requests for pyflink-poc.

<details closed>
<summary>Contributing Guidelines</summary>

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

[**Return**](#-quick-links)

---
